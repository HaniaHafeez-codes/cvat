\# Objectives



\## MO-1: Endpoint response time



| Field | Entry |

|---|---|

| ID | MO-1 |

| What is measured | Time for GET of the per-class count endpoint for one task, from request sent to full response received. |

| How | Chrome DevTools, Network panel, total request time. 5 runs, raw numbers saved in docs/evidence. |

| Target | Median of 5 runs at or below 250 ms. |

| Why this number | The count should be one grouped query in the database, not rows loaded into Python. A target this low is only reachable if it is built that way. It is a first guess and will be checked against the real baseline. |

| Conditions | Chrome, cache disabled, logged in as superuser, local Docker stack, task #1 (1386 images, COCO val), nothing else running. |

| Not included | Video tasks, tasks with tracks, the first request after a cold start. |



Machine: Intel Core i7-8650U @ 1.90GHz, 16 GB RAM, Windows 11 (build 10.0.26200).

CVAT commit: c4f0c2a54dd7d95bc222836c645e8c290858fd05

