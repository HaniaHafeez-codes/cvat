# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from . import views

urlpatterns = [
    path("test/tasks/<int:task_id>/class-counts", views.ClassCountsView.as_view()),
]