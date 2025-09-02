from typing import Optional, List

from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].insert(0, (self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feedQ = []
        for twt in self.tweets.get(userId, []):
            heapq.heappush(feedQ, twt)
            if len(feedQ) > 10:
                heapq.heappop(feedQ)
        for follow in self.follows[userId]:
            f = self.tweets.get(follow, []) if follow != userId else []
            for feed in f:
                heapq.heappush(feedQ, feed)
                if len(feedQ) > 10:
                    heapq.heappop(feedQ)
        retList = heapq.nlargest(10, feedQ)
        return [i[1] for i in retList]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


if __name__ == "__main__":
    sol = Twitter()

    # print(sol.postTweet(1, 5))
    # print(sol.postTweet(1, 3))
    # print(sol.getNewsFeed(1))
    # print(sol.getNewsFeed(2))
    # print(sol.follow(1, 2))
    # print(sol.getNewsFeed(1))
    # print(sol.getNewsFeed(2))
    # print(sol.unfollow(1, 2))
    # print(sol.getNewsFeed(1))

    twitter = Twitter()
    for i in range(1, 12):
        twitter.postTweet(1, i)
    print(twitter.getNewsFeed(1))
    print(twitter.follow(2, 1))
    print(twitter.getNewsFeed(2))
    twitter.unfollow(2, 1)
    print(twitter.getNewsFeed(2))

    print("Running Solution...")
