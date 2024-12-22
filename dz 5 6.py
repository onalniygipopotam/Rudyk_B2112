#1023
# x, y = map(int, input().split())
# if x < 0 and y > 0:
#     print("Yes")
# else:
#     print("No")


#1024
# x, y = map(int, input().split())
# if x > 0 and y > 0:
#    print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#    print(4)

#1025
# x, y, z = map(int, input().split())
# if x + y > z and x + z > y and y + z > x:
#     print("Yes")
# else:
#     print("No")


#1026
# a, b, c, d = map(int, input().split())
# if a < b < c < d:
#    print("Yes")
# else:
#   print("No")



#1027
# N = int(input())
# max_digit = 0
# while N > 0:
#     digit = N % 10
#   if digit > max_digit:
#         max_digit = digit
#     N = N // 10
# print(max_digit)



#1028
# 2N = int(input())
# a = N // 10
# b = N % 10
# square_N = N ** 2
# cube_sum_digits = (a + b) ** 3
# if square_N == cube_sum_digits:
#     print(a + b)
# else:
#     print(abs(a - b))
