from typing import Optional, List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # expand a window to size r,
        # presweep to determine current power
        def test(stations):
            width = len(stations)
            preSweep = [0] * (width + 2 * r)
            rngR = r
            rngL = r
            ptr = r

            stations = ([0] * r) + stations + ([0] * r)

            # extend the window to the right
            while ptr < width + r:
                preSweep[ptr] = stations[ptr]
                while abs(rngR - ptr) < r:
                    rngR += 1
                    preSweep[ptr] += stations[rngR]
                while abs(rngL - ptr) < r:
                    rngL -= 1
                    preSweep[ptr] += stations[rngL]

                ptr += 1
                rngR = ptr
                rngL = ptr
            if r > 0:
                preSweep = preSweep[r:-r]
            return min(preSweep)

        maxVal = 0
        ptr = 0
        while ptr < len(stations):
            stationCopy = stations.copy()
            stationCopy[ptr] += k
            t = test(stationCopy)
            maxVal = max(maxVal, t)
            ptr += 1
        return maxVal


"""
0 <= stations[i] <= 105
0 <= r <= n - 1
0 <= k <= 109
"""

if __name__ == "__main__":
    sol = Solution()
    stations = [4, 4, 4, 4]
    r = 0
    k = 3

    print(sol.maxPower(stations, r, k))
    print("Running Solution...")
