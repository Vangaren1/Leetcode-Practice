from typing import Optional, List
from collections import deque


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers

        events.sort(key=lambda x: x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))

        events = deque(events)
        # when adding in users to auto login, use (timestamp, id#)
        autoLogin = deque()
        offset = 0

        while events:
            eType, timestamp, msg = events.popleft()

            while autoLogin and autoLogin[0][0] <= int(timestamp):
                _time, id = autoLogin.popleft()
                online[id] = True

            if eType == "MESSAGE":
                if msg == "ALL":
                    offset += 1
                elif msg == "HERE":
                    for i, on in enumerate(online):
                        if on:
                            mentions[i] += 1
                elif len(msg) > 0:
                    # extract ids from msg and increment those
                    ids = msg.split()
                    for id in ids:
                        i = int(id[2:])
                        mentions[i] += 1

            elif eType == "OFFLINE":
                id = int(msg)
                online[id] = False
                autoLogin.append((int(timestamp) + 60, id))

        return [m + offset for m in mentions]
        pass


if __name__ == "__main__":
    sol = Solution()
    numberOfUsers = 5
    events = [
        ["OFFLINE", "60", "3"],
        ["OFFLINE", "55", "2"],
        ["MESSAGE", "98", "HERE"],
        ["MESSAGE", "20", "HERE"],
        ["OFFLINE", "23", "0"],
        ["OFFLINE", "10", "1"],
    ]
    print(sol.countMentions(numberOfUsers, events))
    print("Running Solution...")
