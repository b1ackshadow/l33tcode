
import heapq
from typing_extensions import Type
from typing import List, NewType, Set, Dict


class Twitter:

    def __init__(self):
        self.feed = {}
        self.time = 0 # records tweet posted time and inc
        self.follow_set: Dict[int, Set[int]] = {}

    def add_tweet(self, userId, tweetId, time=None):
        if not time:
            time = self.time
        current_feed = self.feed.get(userId, [])
        current_feed.append((time, tweetId))
        self.feed[userId] = current_feed


    def update_followers_tweets(self, t_time, tweetId, followerId):

        print(f"updating feed for follower {followerId} with {tweetId} at time {t_time}")
        latest_tweet = self.time == t_time
        follower_feed = self.feed.get(followerId, [])
        print(f"followers feed {follower_feed}")
        if latest_tweet:
            print("latest tweet")
            # base case 
            # when are updating a latest users tweet it just goes to the end of the feed(latest)
            follower_feed.append((t_time, tweetId))

        # based on the time place the tweet in the feed in order
        else:
            i = len(follower_feed) - 1
            while t_time < follower_feed[i][0]:
                i -= 1
            print(f"insert tweet at index = {i}")
            follower_feed.insert(i + 1, (t_time, tweetId))

        self.feed[followerId] = follower_feed

    def postTweet(self, userId: int, tweetId: int) -> None:
        # print(f"user {userId} posted {tweetId} at {self.time}")
        # update this tweet to all the followers
        # for follower in self.follow_set.get(userId, []):
        #     print(f"updating {tweetId} for follower {follower} ")
        #     self.update_followers_tweets(self.time, tweetId, follower)

        # update users feed
        self.add_tweet(userId, tweetId)
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        return [tweetId for (_, tweetId) in self.feed[userId][10::-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.follow_set.get(followeeId, set())
        followers.add(followerId)
        self.follow_set[followeeId] = followers

        print(f"user {followerId} is follwing {followeeId}")
        print(f"Followee has {self.feed.get(followeeId)}")
        for (t_time, tweetId) in self.feed.get(followeeId, []):
            self.update_followers_tweets(t_time, tweetId, followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followee_tweets = self.feed[followeeId]
        for (_)
        s = self.follow_set.get(followeeId, set())
        s.remove(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

twitter = Twitter();
twitter.postTweet(1, 5); 
twitter.postTweet(1, 1); 
twitter.postTweet(1, 7); 
twitter.postTweet(1, 8); 
twitter.postTweet(1, 2); 
twitter.postTweet(2, 6); 
twitter.follow(1, 2);    
print(twitter.getNewsFeed(1))
# twitter.postTweet(2, 6); 
# print(twitter.getNewsFeed(1))
# twitter.follow(1, 2);    
# twitter.postTweet(2, 6); 
# twitter.getNewsFeed(1);  
# twitter.unfollow(1, 2);  
# twitter.getNewsFeed(1);  
