import heapq

class Tweet:
    def __init__(
        self, tweetId: int, userId: int, counter: int, prev: Tweet | None = None
    ):
        self.tweetId = tweetId
        self.counter = counter
        self.prev = prev

class User:
    def __init__(self, userId: int):
        self.userId = userId
        self.followers = {userId}
        self.last_tweet = Tweet(-1, userId, -1)

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.users = {}
        self.tweet_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._ensure_user(userId)
        tweet = Tweet(tweetId, userId, self.tweet_counter, user.last_tweet)
        self.tweets[tweetId] = user.last_tweet = tweet
        self.tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Obtain the tweet lists of all followers.
        # Then, add all non -1 pointers to the heap
        # heap_pop then repush 10 times (might not repush)
        user = self._ensure_user(userId)
        heap = []
        for follower_id in user.followers:
            acc = self.users[follower_id]
            tweetId = acc.last_tweet.tweetId
            if tweetId != -1:
                heapq.heappush_max(heap, (acc.last_tweet.counter, tweetId))
        
        trials = 0
        res = []
        while heap and trials < 10:
            _, tweetId = heapq.heappop_max(heap)
            res.append(tweetId)
            prev = self.tweets[tweetId].prev
            if prev.tweetId != -1:
                heapq.heappush_max(heap, (prev.counter, prev.tweetId))
            trials += 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._ensure_user(followerId).followers.add(followeeId)
        self._ensure_user(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self._ensure_user(followerId).followers.discard(followeeId)
        self._ensure_user(followeeId)

    def _ensure_user(self, userId: int) -> User:
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)