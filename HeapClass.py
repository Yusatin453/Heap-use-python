#10124397
class MinHeap:
    def __init__(self, data=None):
        self.heap = []
        if data:
            self.heapify(data)

    def heapify(self, data):
        #  heap dari list data
        self.heap = list(data)
        n = len(self.heap)
        for i in reversed(range(n // 2)):
            self._sift_down(i)

    def insert(self, val):
        # Tambah elemen di akhir, dan tukar ke atas
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def delete(self):
        # Hapus root 
        if not self.heap:
            raise IndexError("delete from empty heap")
        root = self.heap[0]
        tail = self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self._sift_down(0)
        return root

    def _sift_up(self, idx):
        
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

class MaxHeap:
    def __init__(self, data=None):
        self.heap = []
        if data:
            self.heapify(data)

    def heapify(self, data):
        #  heap dari list data
        self.heap = list(data)
        n = len(self.heap)
        for i in reversed(range(n // 2)):
            self._sift_down(i)

    def insert(self, val):
        # Tambah elemen di akhir, lalu tukar ke atas
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def delete(self):
        # Hapus root (elemen terbesar)
        if not self.heap:
            raise IndexError("delete from empty heap")
        root = self.heap[0]
        tail = self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self._sift_down(0)
        return root

    def _sift_up(self, idx):
        # tukar posisi ke atas
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] < self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        # tukar posisi ke bawah
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != idx:
                self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                idx = largest
            else:
                break



data = [5, 3, 8, 1, 2, 7]
heapify = MaxHeap(data)
print('heapify:')
print(heapify.heap)       
print('insert:')
heapify.insert(10)
print(heapify.heap)
print('delete:')
deleted = heapify.delete()
print(f"deleted: {deleted}")
print(f"heap setelah deletion: {heapify.heap}") 
deleted = heapify.delete()
print(f"deleted: {deleted}")
print(f"heap setelah deletion: {heapify.heap}")
