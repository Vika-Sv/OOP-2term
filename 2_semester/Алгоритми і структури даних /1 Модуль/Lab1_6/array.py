import random

class Array:
    def __init__(self, size, fill="random"):
        if fill == "random":
            self._data = [random.randint(0, 100_000) for _ in range(size)]
        elif fill == "sorted":
            self._data = list(range(size))
        elif fill == "reversed":
            self._data = list(range(size - 1, -1, -1))
        elif fill == "worst_bubble":
            self._data = list(range(size - 1, -1, -1))
        else:
            raise ValueError(f"Невідомий тип fill: {fill}")
        self.size = size

    def copy(self):
        return self._data[:]

    def merge_sort_desc(self):
        self._data = self._merge_sort(self._data)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid   = len(arr) // 2
        left  = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, L, R):
        res, i, j = [], 0, 0
        while i < len(L) and j < len(R):
            if L[i] >= R[j]:
                res.append(L[i]); i += 1
            else:
                res.append(R[j]); j += 1
        res.extend(L[i:]); res.extend(R[j:])
        return res

   
    def bubble_sort(self):
        a = self._data
        n = len(a)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
        self._data = a