# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cvat.apps.engine.models import LabeledShape, Task


class ClassCountsView(APIView):
    # Replaces the default PolicyEnforcer, which requires an iam_permission_class
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)

        rows = (
            LabeledShape.objects.filter(job__segment__task=task)
            .values("label__name")
            .annotate(count=Count("id"))
            .order_by("-count", "label__name")
        )

        return Response(
            {
                "task_id": task.id,
                "counts": [{"label": row["label__name"], "count": row["count"]} for row in rows],
            }
        )