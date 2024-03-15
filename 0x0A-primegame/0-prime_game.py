#!/usr/bin/python3
""" ALX Interview: Prime Game """


def isWinner(x, nums):
   """
   This function determines who the winner of each game is.
   """
   if not nums or x < 1:
       return None
   max_num = max(nums)

   sieve = [True for _ in range(max(max_num + 1, 2))]
   for i in range(2, int(pow(max_num, 0.5)) + 1):
       if not sieve[i]:
           continue
       for j in range(i * i, max_num + 1, i):
           sieve[j] = False
   sieve[0] = sieve[1] = False
   y = 0
   for i in range(len(sieve)):
       if sieve[i]:
           y += 1
       sieve[i] = y
   player1 = 0
   for x in nums:
       player1 += sieve[x] % 2 == 1
   if player1 * 2 == len(nums):
        return None
   if player1 * 2 > len(nums):
       return "Maria"
   return "Ben"