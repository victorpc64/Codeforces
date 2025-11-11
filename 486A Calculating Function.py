#Input: an integer
#Output: the result of f(n) = -1 +2 -3 +4... + (-1)power n n 

n = int(input())

#The formula I deducted: if even, divide by 2; if odd, the negative coefficiente of n+1 divided by 2.
#It's a formula based on observation
if n % 2 == 0:
     solution = int(n / 2)
else:
    solution = int( -(n+1) / 2)
print(solution)



#I first tried as an answer the inner loop. It exceeded time, so I coded the outer loop to see the results of the first 99 numbers and deduct a formula.

# for j in range(1, 100):
#     solution = 0
#     multiplier = -1

#     for i in range(1, j+1):
#         solution = solution + (i * multiplier)
#         multiplier *= -1

#     print("%s = %s" % (j, solution))
          