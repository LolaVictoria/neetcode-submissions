class Twitter:

    def __init__(self):
        self.followers = {}
        self.tweets = {}
        self.time = 0


        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followers.get(userId, set()) | {userId}
        for user in users:
            for time, tweetId in self.tweets.get(user, []):
                heapq.heappush(heap, (-time, tweetId))
        res = []
        for _ in range(10):
            if not heap:
                break
            time, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res

         

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)

            

        
