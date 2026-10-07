\# Plan



CVAT commit: c4f0c2a54dd7d95bc222836c645e8c290858fd05

Machine: Intel Core i7-8650U @ 1.90GHz, 16 GB RAM, Windows 11 (build 10.0.26200)

Sample data: COCO 2017 val, 1386 images, one task.



\## Approach

New Django app `test` with one endpoint returning per-class annotation

counts for a task (aggregate query on shapes grouped by label, read from

the DB). A page in the web UI calls it and draws a bar chart.

Auth: CVAT's existing login; reject anonymous users and users without

access to the task.



\## Order and time budget (of 8h)

1\. Read CVAT code: Task -> Job -> Shape -> Label models      45 min

2\. Items 1-2: endpoint and page                               1h 30m

3\. Items 3-4: graph, empty and error states                   45 min

4\. Item 5: auth, show both refusals working                   30 min

5\. Item 6: one speed target, measure 5 runs                   30 min

6\. Item 7: one extra filter/grouping                          30 min

7\. Docs (Objectives, Definition of Done), evidence            30 min

8\. Loom recording, PR, submit                                 30 min



\## Deliberately skipping

Items 8-10 (WebSocket live updates, reconnect, decision record) unless

items 1-7 finish early. Will list what I did not reach in Definition of Done.

