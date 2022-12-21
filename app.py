# To add all elements of list
s_expenses = [12, 31, 43, 65, 78]
a_expenses = [2, 5, 31, 1, 21, 30, 0, 5, 11, 7, 29]
j_expenses = [22, 13, 14, 17, 18]

the_big = a_expenses[0]

# finding the largest number in a list
for x in a_expenses:
    if (x > the_big):
        the_big = x
    print(x, the_big)

hello = [12,13,14,15,11]
t_s_n = hello[0]

for w in hello:
    if(w < t_s_n):
        t_s_n = w

print(t_s_n)


# finding number larger than 15
for i in a_expenses:
    if (i>15):
        print(i)

# algorithm

expenses_2 = ['12', '31', '43', '65', '78']
s = 0
print(s)
#
for n in s_expenses:
    s = s+n
#
print(s)

# creating a variable and initializing it
j = 0
#
#
for  k in a_expenses:
    j = j+k
#
print(j)
#
m = 0
for u in j_expenses:
    m = u+m
#
print(m)

