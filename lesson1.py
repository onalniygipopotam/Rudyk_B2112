#1001
#Дано чотири дійсні числа a b c d Знайти їх суму.
# p = float(input())
# rounded_value = round(p)
# integer_part = int(p)
# fractional_part = round(p - integer_part, 1)

# print(rounded_value)
# print(integer_part)
# print(f"{fractional_part:.1f}")
# a, b, c, d = map(float, input().split())
# result = a + b + c + d
# print(f"{result:.4f}")


# a,b = map(int, input().split())
# P = (a+b) * 2
# print(P)


# x, y = input().split()
# x, y = int(x), int(y)
# print(x % y)
# print(y % x)


#1007

# N = float(input())
# integer_part = int(N)
# result = 2 * integer_part
# print(result)


#1008

# P, K = map(float, input().split())
# fractional_part = P - int(P)
# result = fractional_part * K
# rounded_result = round(result)
# print(rounded_result)


#1009

# a1, b1, a2, b2 = map(int, input().split())
# S1 = a1 * b1
# S2 = a2 * b2
# result = abs(S1 - S2)
# print(result)


#1010

# N = int(input())
# tens = N // 10
# units = N % 10
# result = tens * units
# print(result)

#1011

# N = int(input())
# hundreds = N // 100
# tens = (N // 10) % 10
# units = N % 10
# print(units, tens, hundreds)

#1012

# a = int(input())
# if a <= 100:
#    V = a ** 3
#    print( V)
# else:
#    print( )


#1013

# x, y = map(int, input().split())
# if abs(x) <= 1000 and abs(y) <= 1000:
#     average = (x + y) / 2
#     print(f"{average:.2f}")
# else:
#     print()


#1014

# n = int(input())
# if 100 <= n <= 999:
#     left_digit = n // 100
#     remaining = n % 100
#     new_number = remaining * 10 + left_digit
#     print(f"{new_number:03}")
# else:
#    print()


#1015

# N = int(input())
# if 0 < N < 100000:
#     minutes = N // 60
#     print(minutes)
# else:
#     print()


#1016

# A, B = map(int, input("").split())
# if 0 < B < A < 10**6:
#     unused_length = A % B
#     print(unused_length)
# else:
#    print()


#1017

# X = int(input())
# if 0 <= X <= 10**9:
#     if X % 2 == 0:
#          print("Yes")
#     else:
#         print("No")
# else:
#     print()


#1018

# a, b = map(int, input().split())
# if abs(a) < 10**9 and abs(b) < 10**9:
#     larger = max(a, b)
#     result = 2 * larger
#     print(result)
# else:
#    print()


#1019

# a = int(input())
# if a % 2 == 0:
#    print(a // 2)
# else:
#   print(0)


#1020

# a, b = map(int, input().split())

# print(min(a, b), max(a, b))



#1021
# P = float(input())
# if P.is_integer():
#     print("Yes")
# else:
#     print("No")


#1022
# a, b, c, d = map(int, input().split())
# minimum = min(a, b, c, d)
# maximum = max(a, b, c, d)
# print(minimum, maximum)


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


#1029
# x = float(input())
# if x == 1 or x == -1:
#   print("No")
# else:
#     y = (x**3 + 2) / (x**2 - 1) + 5
#      print(f"{y:.3f}")


#1030
# N = int(input())
# first_digit = N // 10
# second_digit = N % 10
# if second_digit == 0:
#     print("NO")
# else:
#     result = first_digit // second_digit
#     print(result)



#1035

# def find_initial_loafs(k):
#     loaves = 0
#     for _ in range(k):
#         loaves = 2 * (loaves + 0.5)
#    return int(loaves)
#
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     print(find_initial_loafs(k))


