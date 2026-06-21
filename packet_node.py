class TelemetryPacket:
    def __init__(self, sensor_id, signal_type, priority_value):
        self.id = sensor_id
        self.type = signal_type
        self.priority = priority_value # Highest ranking value indicates extreme severity
