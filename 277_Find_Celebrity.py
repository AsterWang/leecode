class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        result = 0
        tmp = result
        for i in range(1, n):
            if Celebrity.knows(result, i):
            	tmp = result
                result = i
        
        for j in range(n):
            if Celebrity.knows(j, result) or not Celebrity.knows(result, j):
                return -1
        return 1