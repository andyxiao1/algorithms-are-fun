class Mergesort:

    def recursive_sort(self, arr):
        if len(arr) == 0:
            return
        return self.recursive_sort_loop(arr, 0, len(arr) - 1)

    def recursive_sort_loop(self, arr, l, r):
        if l == r:
            return
        if r - l == 1:
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
            return

        m = (l + r) // 2
        self.recursive_sort_loop(arr, l, m)
        self.recursive_sort_loop(arr, m + 1, r)
        self.merge(arr, l, r, m)

    def merge(self, arr, l, r, m):
        temp = []
        i, j = l, m + 1

        while i <= m and j <= r:
            temp.append(min(arr[i], arr[j]))
            if arr[i] < arr[j]:
                i += 1
            else:
                j += 1
        if i > m:
            temp.extend(arr[j:r + 1])
        else:
            temp.extend(arr[i: m+1])
        arr[l:r + 1] = temp


arr = [3, 1, 5, 4, 2]
print(arr)
sortObj = Mergesort()
sortObj.recursive_sort(arr)
print(arr)
