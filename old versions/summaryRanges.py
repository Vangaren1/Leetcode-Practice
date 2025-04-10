class Solution:
    def summaryRanges(self, nums):
        rList = []
        if len(nums)==0:
            return rList
        start = nums.pop(0)
        last = start
        if len(nums) == 0:
            return [str(start)]
        while len(nums) > 0:
            nextNum = nums.pop(0)
            print("nextNum: %d, start: %d, last: %d" % (nextNum, start, last))
            if nextNum == (last + 1):
                # if the next item in the list is 1 + the last, update last
                last = nextNum
                if len(nums) == 0:
                    # if the list is empty at this point, add to the return list
                    rList.append(str(start)+"->"+str(last))
            else:
                if last == start:
                    # if last == start, then there was only 1 number in the range
                    rList.append(str(start))
                else:
                    rList.append(str(start)+"->"+str(last))
                start = last = nextNum
            # if the list is empty, add the single item into return list
            if len(nums) == 0 and start == last:
                rList.append(str(start))
        return rList

        

obj = Solution()
test1 = [0,1,2,4,5,7]
# expected output ["0->2","4->5","7"]
test2 = [0,2,3,4,6,8,9]
# expected output ["0","2->4","6","8->9"]

# print(obj.summaryRanges(test1))
# print(obj.summaryRanges(test2))
print(obj.summaryRanges([-1]))