from typing import Optional, List


class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        index = self.findInsertIndex(num)
        self.array.insert(index, num)

    def findMedian(self) -> float:
        mid = self.size() // 2
        if self.size() % 2 == 1:
            return self.array[mid]
        return (self.array[mid] + self.array[mid - 1]) / 2

    def findInsertIndex(self, num: int) -> int:
        # if the array is simple, just check if it's empty, less than the 1 item, or greater than
        if self.size() == 0:
            return 0
        if self.size() == 1:
            if num < self.array[0]:
                return 0
            return 1
        left = 0
        right = len(self.array) - 1
        mid = (left + right + 1) // 2
        while left <= right:
            # check if mid is at either end of the array
            if mid == 0 and num < self.array[0]:
                return 0
            if mid == (self.size() - 1) and num > self.array[-1]:
                return self.size()

            # if num > array[grid] make left = mid +1 else  right = mid-1
            if mid < self.size():
                if self.array[mid] == num:
                    return mid
                if num > self.array[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            mid = (left + right + 1) // 2
        return mid

    def size(self) -> int:
        return len(self.array)


if __name__ == "__main__":
    medianFinder = MedianFinder()
    for i in (6, 10, 2, 6, 5, 0, 6, 1, 0, 0):
        medianFinder.addNum(i)
        print(medianFinder.findMedian())
    # arr = [1]
    # medianFinder.addNum(2)
    # # arr = [1, 2]
    # medianFinder.findMedian()
    # # return 1.5 (i.e., (1 + 2) / 2)
    # medianFinder.addNum(3)
    # # arr[1, 2, 3]
    # medianFinder.findMedian()
    # # return 2.0
    print("Running Solution...")
