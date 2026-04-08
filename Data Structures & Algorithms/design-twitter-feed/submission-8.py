class Twitter:

    def __init__(self):
        # a dictionary containing list of tweets from each user
        self.tweetMap = defaultdict(list)
        # a dictionary containing list of follows for each user
        self.follows = defaultdict(set)
        # a count ticker that acts as a date
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add a tweet to the list and increment counter
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # first get all follow list of a user and also add user to the follow list
        followers = self.follows[userId]
        followers.add(userId)

        # get latest tweets from each follow list and store in a heap with count for order
        # also get followerid and index of next element of that item
        minHeap = []
        res = []
        for f in followers:
            if f in self.tweetMap:
                index = len(self.tweetMap[f]) - 1
                count, tweetId = self.tweetMap[f][index]
                minHeap.append([count, tweetId, f, index - 1])
        heapq.heapify(minHeap)
        # pop the latest of the heap and also add the next upcoming index to the heap
        # make sure the new element has index higher than 0
        while minHeap and len(res) < 10:
            count, tweetId, f, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(minHeap, [count, tweetId, f, index - 1])
        return res




    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
