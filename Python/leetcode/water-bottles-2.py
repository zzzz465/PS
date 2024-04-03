"""
You are given two integers numBottles and numExchange.

numBottles represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

Drink any number of full water bottles turning them into empty bottles.
Exchange numExchange empty bottles with one full water bottle. Then, increase numExchange by one.
Note that you cannot exchange multiple batches of empty bottles for the same value of numExchange. For example, if numBottles == 3 and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the maximum number of water bottles you can drink.
"""

"""
in this problem, we need to drink bottles many as possible as, by doing actions in the right order.
we can take think about two things.

actions that we can take in each step

1. should I drink n bottles?
2. or should I exchange empty bottles to a full bottle?

also, we have three related variables. full bottles, empty bottles, numExchange

but I think order of actions doesn't affact result.
because, numExchange only increase when we exchange empty bottles to a full bottle.
we cannot exchange multiple of them, only a full bottle per action.

also, we only consider how many bottles we can possibly drink, not finding minimum actions
these two reasons is why I concluded that the order of actions is not important.
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drinkCount = 0
        emptyBottles = 0

        while True:
            if numBottles > 0:
                drinkCount += numBottles
                emptyBottles += numBottles
                numBottles = 0
                continue

            if emptyBottles >= numExchange:
                numBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
                continue

            break

        return drinkCount


if __name__ == "__main__":
    result = Solution().maxBottlesDrunk(13, 6)
    print(result)
