from packet_node import TelemetryPacket
from max_heap import PriorityMaxHeap

if __name__ == "__main__":
    print("📡 Instantiating Embedded Max-Heap Gateway Scheduler...\n")

    scheduler = PriorityMaxHeap()

    # Load overlapping telemetry signals into the gateway pool
    scheduler.insert_packet(TelemetryPacket("Temp_01", "ROUTINE_LOG", priority_value=1))
    scheduler.insert_packet(TelemetryPacket("Boiler_04", "CRITICAL_OVERHEAT", priority_value=10))
    scheduler.insert_packet(TelemetryPacket("Valve_02", "PRESSURE_WARNING", priority_value=5))

    print("📥 Ingested Messages: Temp_01 (P=1), Boiler_04 (P=10), Valve_02 (P=5)")

    critical_dispatch = scheduler.extract_critical_packet()
    print("\n🚀 Gateway Dispatch Decision Engine Output:")
    print(f"   👉 Selected Source Node: {critical_dispatch.id}")
    print(f"   👉 Executed Signal Category Type: {critical_dispatch.type}")
    print(f"   👉 Verified Heap Evaluation Priority: Rank {critical_dispatch.priority}")
.
