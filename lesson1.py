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

a = int(input())
if a % 2 == 0:
    print(a // 2)
else:
    print(0)


#1020

a, b = map(int, input().split())

print(min(a, b), max(a, b))



#1021


#1022