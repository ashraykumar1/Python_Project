#1. Print nu bers from 1 to 5 using for loop
for i in range(1,6):
    print(i)

#2. Print even numbers from 2 to 10 using while loop
i=2
while i<=10:
    if i%2 == 0:
        print(i)
    i+=1

#3. calculate the sum of all numbers from 1 to 50 using for loop.
res = 0
for i in range(1,51):
    res+=i
print(res)

#4. Print square of numbers from 1 to 5 using for loop.
for i in range(1,6):
    print(i*i)

#5. Print reverse of a given list using while loop

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start, end = 0, 9
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1

print(a)


#6. Generate and print first 5 multiples of 3 using for loop.
my_list = []
for i in range(1,16):
    if i%3 == 0:
        my_list.append(i)

print(my_list)


# 7. Print odd numbers from 1 to 15 using while loop.

i=1
while i<=15:
    if i%2 !=0:
        print(i)
    i+=1


#8. Caluclate the factorial of a given number using for loop.

num = 6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("factorial",factorial)


#9. Print the character of string in reverse order using for loop
string1 = "Ashray"
new_str = ""
rev_str = ""
for c in string1:
    rev_str = c + rev_str
print(rev_str)

#10. check if a number is prime using while loop.
def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i <=n:
        if n%i == 0:
            return False
        i+=1
    return True

p = is_prime(10)
if p :
    print("prime")
else:
    print("not prime")


# 12. Sum of all even numbers from 1 to 20 using while loop.
res = 0
i=1
while i<=20:
    if i%2 == 0:
        res = res+i
    i+=1

print(res)


#13. print the pattern
'''
*
**
***
****

'''
for i in range(1,5):
    print("*" * i + "\n" )


#13. Check the string is palindrome using for loop.
# string  = reverse of string.

string1 = "XAX"
rev_str = ""
for c in string1:
    rev_str = c + rev_str
if string1 == rev_str:
    print("palindrone")
else:
    print("not palindrone")

#14. print cube of number from 1 to 3 using while loop.

i=1
while i<=3:
    print(i*i*i)
    i+=1

#15. count the number of vowels in a given string.
vowels = ["a","e","i","o","u"]
string1 = "Kohli"
res = 0
for str1 in string1:
    if str1.lower() in vowels:
        res+=1
print(res)

#16. Print elements of list using while loop.
# first we need to caluclate the length of list.
my_list1 = [1,2,3,4,5]
len1 = 0
for i in my_list1:
    len1+=1
print(len1)

# now, using while loop to print elements of list

k = 0
while k<len1:
    print(my_list1[k])
    k+=1

# 17. caluclate product of numbers from 1 to 5 using for looop.

res = 1
for i in range(1,6):
    res*=i
print(res)

#18. Finding the patterm
'''
1
22
333
4444

'''
for i in range(1,5):
    print(f"{i}"*i )


#18. check if given number is perfect square using while loop.

num = 5
i=1
flag=0
while i<=num:
    if i*i == num:
        flag = 1
        break
    i+=1
print(flag)
if flag == 1:
    print(f"{num} is a Perfect Square")
else:
    print(f"{num} is not a Perfect Square")


