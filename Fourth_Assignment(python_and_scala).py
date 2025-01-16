# 1. Program to find right angled triangle.
'''
*
**
***
****
*****
'''

for i in range(1,6):
    print("*" * i)

#2. Prgram to find a square pattern.
'''    
****
****
****
****
'''
i=1
num = 4
while i<=num:
    print("*" *num )
    i+=1

# 3. Inverted Triangle

'''
*****
****
***
**
*
'''

num = 5

for i in range(num, 0, -1):
    print("*" * i)

# 4. Hollow pattern

# Python 3 code for hollow rectangle
n=6
m=20
for i in range(1,n+1):
    for j in range(1,m+1):
        if (i == 1 or j == n or j == 1 or j == m):
            print("*", end = "")
        else:
            print(" ",end="")

    print()


# 5.
'''

*
*_*
*_*_*
*_*_*_*
*_*_*_*_*

'''

for i in range(1,6):
    res = "*_" *i
    print(res.strip("_"))


# 6.
'''
*
***
*****
*******
*********
*******
*****
***
*

'''
for i in range(1,9,2):
    print("*"*i)
for i in range(9,0,-2):
    print("*"*i)


# 7 .
'''
*******
*****
***
*
*
***
*****

'''

for i in range(7,0,-2):
    print("*"*i)
for i in range(1,7,2):
    print("*"*i)


# 8. butterfly pattern.

'''
*   *
** **
*****
** **
*   *


'''

N = 3
spaces = 2 * N - 1
stars = 0
for i in range(1, 2 * N):
    if i <= N:
        spaces = spaces - 2
        stars += 1
    else:
        spaces = spaces + 2
        stars -= 1

    for j in range(1, stars + 1):
        print("*", end="")

    for j in range(1, spaces + 1):
        print(" ", end="")

    for j in range(1, stars + 1):
        if j != N:
            print("*", end="")

    print()

#9.
'''
*
**
***
****
*****
****
***
**
*
'''

for i in range(1,5):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)


#10 .
'''
          * 
         * * * 
        * * * * * 
       * * * * * * * 
      * * * * * * * * *
'''

n=10
for i in range(1, 11,2):
    print(' '*n, end='')
    print('* '*(i))
    n-=1

