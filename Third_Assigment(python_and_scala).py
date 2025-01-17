# 1. convert kg to g.
def kg_to_g(kg):
    gms = kg*1000
    return gms

res = kg_to_g(22)
print(res)

#2. celcius to farenheit

def c_to_f(c):
    res = (c * 1.8) + 32
    return res

f = c_to_f(80)
print(f)

#3. biggest of three numbers.

# first= int(input("enter a number"))
# second= int(input("enter a number"))
# third= int(input("enter a number"))
# if (first>second and first>third):
#     print(first," is biggest")
# elif (second>first and second>third):
#     print(second," is biggest")
# else:
#     print(third ,"is biggest")


#4  Write a java program that performs the following tasks.
# a. Store a number in a variable
# b. If value is not in range (100-1000) prints wrong number else follows
# the steps
# c. Check even or odd
# d. If even divide the number by 3 and print the remainder
# e. If odd divide the number by 2 and print the remainder.
a=112
def func(a):
    range_list = list(range(100, 10001))
    if a not in range_list:
        return("wrong number")
    else:
        if a%2==0:
            rem = a/3
            return rem
        else:
            rem = a/2
            return rem
f = func(a)
print(f)


# 5. Declare & initialize a number. Check whether the number is in range 0-100
# or not. If not in range print invalid input. Else – if the number is in range 90-
# 100 then print Super Smart, 80-90 print Smart,70-80 print smart enough,
# 60-70 print just smart, 35-60 print no smart, 0-35 print dump.

a= 99
range_list = list(range(101))
if a not in range_list:
    print("Invalid Input")
elif a in list(range(90,101)):
    print("Super Smart")
elif a in list(range(80,90)):
    print("Smart")
elif a in list(range(70,80)):
    print("smart enough")
elif a in list(range(60,70)):
    print("just smart")
elif a in list(range(35,60)):
    print("no smart")
elif a in list(range(0,35)):
    print("dump")


# 6. Write a program to perform simple math based on the user inputs by using
# Switch condition.(+ , - , * , /)
# 7. Write a program to print “BIGDATA”for 60 times.

for i in range(61):
    print("BIGDATA")


# 8. Write a program to print all numbers which are divisible by 11 from 250 to
# 550.

res = []
for num in range(250,551):
    if num%11 == 0:
        res.append(num)

print(res)


# 9. Write a program to sum all the numbers from 56 to 153.

res = 0
for num in range(56,154):
    res += num
print(res)


# 10. Write a program to print all even numbers in range 700 to 900.

res = []
for num in range(700,901):
    if num%2==0:
        res.append(num)

print(res)


# 11. Write a program to print all odd numbers from 251 to 51. like (251,
# 249,...51)

for num in range(251,50,-1):
    if num%2!=0:
        print(num)


# 12. Write a Program to print the count of the even numbers between the given
# range?

def even_range(range1):
    res = 0
    for num in range(1,range1+1):
        if num%2 == 0:
            res += 1
    return res
a = even_range(10)
print(a)


# 13. Write a program to print alternate even numbers from 20 to 140. Like
# (20,24,28...)

for i in range(20,141,4):
    print(i)



# 14. Write a program to print alternate even numbers from 20 to 140. Like
# (22,26,30...)

for i in range(22,141,4):
    print(i)



# 15. Print following series 2*3,3*4,4*5,......16*17

for num in range(2,17):
    print(f" {num} * {num+1}  ")

# 16.sum of even numbers from 382 to 582
sum_382_582 = sum(n for n in range(382, 583) if n % 2 == 0)
print("The sum of even numbers from 382 to 582 is: ", sum_382_582)

# 17.print all alphabets using char variable
for i in range(65, 91):
    print(chr(i), end=" ")

# 18.average of 24 to 100:
sum = 0
for i in range(24, 101):
    sum = sum + i
avg = sum / 100 - 24
print("average :", avg)

# 19. sum of 5^2+6^2+….102^2
sum = 0
for i in range(5, 103):
    sum = sum + i * i
print("sum is  :", sum)

# 20.print A B 100 times
for i in range(100):
    print("A B", end=" ")

# 21 . @
for num in range(10, -6, -1):
    print(f" {num} @ {num - 1}  ")

# 22. 100,200,…1000  series :
for i in range(1, 11):
    print(i * 100, end=" ")

# 23. series  : 5^2  , 7^2 ,…..25^2
for i in range(5, 25, 2):
    print(i ** 2, end=" ")

# 24.  print  5 10, 5 10    7 times
for i in range(7):
    print("5,10", end=" ,")

25.
n = 5
for i in range(4, -13, -1):
    print(n, '*', i)
26.
for i in range(1, 37, 2):
    print(i, ',even', end=" ")

27.
for i in range(1, 36):
    if i % 3 != 0:
        print(i, end=" ")
    else:
        print('factor of 3', end=" ")

28.
for i in range(1, 24, 2):
    if i % 5 != 0:
        print(i, end=" ")
    else:
        print('divisible by 5', end="
    29.
    k = 0.5
while k <= 5.1:
    print(k ** 2)
    k = k + 0.2


# 30. Write a for loop that never ends?

def infinity():
    while True:
        yield


for num in infinity():
    pass

# 31. Write a Loop inside other loop and observe the execution flow?
for num1 in range(1, 2):
    for num2 in range(1, 5):
        print(num1 + num2)



