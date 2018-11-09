class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            print result
            result |= n & 1
            print result
            n >>= 1
            print n
        # return result