from typing import Optional, List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = []
        lastTime = max(endTime)
        dp = [
            0,
        ] * lastTime
        for index, t in enumerate(startTime):
            tmp = (t, endTime[index], profit[index])
            jobs.append(tmp)
        jobs.sort(key=lambda x: x[0])
        for j in jobs:
            print(j)

        for index in range(lastTime - 1):
            jList = [j for j in jobs if j[0] == index + 1]
            if len(jList) == 0:
                jList = [(0, 0)]
            else:
                jList.sort(key=lambda x: x[2])

            if index == 0:
                dp[index] = jList[0]
            else:
                dp[index] = max(dp[index - 1][2], jList[0][2])
        print(dp)
        pass


if __name__ == "__main__":
    sol = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]

    sol.jobScheduling(startTime, endTime, profit)
    print("Running Solution...")
