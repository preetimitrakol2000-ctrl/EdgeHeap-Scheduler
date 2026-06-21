class PriorityMaxHeap:
    def __init__(self):
        self.heap_list = []

    def insert_packet(self, packet):
        self.heap_list.append(packet)
        self._bubble_up(len(self.heap_list) - 1)

    def extract_critical_packet(self):
        if not self.heap_list: return None
        if len(self.heap_list) == 1: return self.heap_list.pop()
        
        root_critical = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self._sink_down(0)
        return root_critical

    def _bubble_up(self, idx):
        while idx > 0 and self.heap_list[idx].priority > self.heap_list[(idx - 1) // 2].priority:
            parent = (idx - 1) // 2
            self.heap_list[idx], self.heap_list[parent] = self.heap_list[parent], self.heap_list[idx]
            idx = parent

    def _sink_down(self, idx):
        size = len(self.heap_list)
        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = left
            if right < size and self.heap_list[right].priority > self.heap_list[left].priority:
                largest = right
            if self.heap_list[idx].priority >= self.heap_list[largest].priority:
                break
            self.heap_list[idx], self.heap_list[largest] = self.heap_list[largest], self.heap_list[idx]
            idx = largest
