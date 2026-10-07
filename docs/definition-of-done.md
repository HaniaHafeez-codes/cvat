\# Definition of Done



Counts mean CVAT shapes (one database row per shape), not COCO annotations.

COCO annotations can import as several polygon shapes, so the two numbers

can differ (checked on image 139: 20 annotations, 22 shapes).

The chart lists only classes with at least one shape (79 of 80 labels in task 1).



\- \[x] Endpoint returns correct counts, checked against a known task.

&#x20; Evidence: person = 3683 from the endpoint and 3683 counted from the COCO file.

&#x20; docs/evidence/item1-endpoint-200.png, docs/evidence/item1-ground-truth-check.txt

\- \[x] Page renders the graph. Evidence: docs/evidence/item3-chart-task1.png

\- \[x] Empty case handled. Evidence: docs/evidence/item4-empty.png

\- \[x] Failed-request case handled. Evidence: docs/evidence/item4-error-404.png

\- \[x] No login is refused. Evidence: HTTP 401, docs/evidence/item5-no-login.png

\- \[ ] User without access to the task is refused. NOT DONE, see below.

\- \[ ] MO-1 measured, 5 runs, raw output saved. NOT DONE.

\- \[ ] MO-1 target met, or missed with the reason. NOT DONE.

\- \[ ] One extra grouping or filter. NOT DONE.

\- \[x] Everything I did not finish is listed below.



\## Not finished

\- Item 5, second half: any logged-in user can read any task's counts. The view

&#x20; uses IsAuthenticated only, because CVAT's default PolicyEnforcer requires an

&#x20; iam\_permission\_class (an OPA rule) per view and I did not get to that.

\- Item 6: the 250 ms target in objectives.md was set but never measured.

\- Item 7: no extra grouping. Grouping by shape type would fit, as task 1 holds polygons.

\- Items 8 and 9: no WebSocket live update, no reconnect.

\- Item 10: only one decision is recorded, in the Plan "Change" section.

\- The page is served by the test app, not inside the CVAT React UI or menu.

