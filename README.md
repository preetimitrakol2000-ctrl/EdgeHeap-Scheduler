# EdgeHeap-Scheduler

A dependency-free Python event scheduler built for embedded IoT gateway pipelines. This subsystem manages telemetry data routing queues using a custom **Max-Heap Priority Queue**, guaranteeing immediate processing for severe machine failure alerts.

## ⚡ Algorithmic Metrics
* **Top Element Peek:** $O(1)$ read cost.
* **Packet Ingestion / Extraction:** Balanced $O(\log N)$ heap adjustment overhead, completely bypassing slow $O(N \log N)$ sorting approaches.
