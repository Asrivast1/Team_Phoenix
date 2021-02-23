lst_1 = []
try:
    no_pizza, team_two, team_three, team_four = map(int, input().split()) # Taking multiple inputs in a single line
except:
    print("Please enter 4 numerical inputs only") # Try and catch for faulty input
for i in range(no_pizza) :
    lst_1.append([x for x in input().split()]) #Appending lists of no. of ingredients and names of ingredients
for i in range(len(lst_1)): #lst_1 contains all the pizza's information
     try: # Try catch and if else loop deleting inconsistent lists
        if len(lst_1[i]) == int(lst_1[i][0]): lst_1.remove(lst_1[i])
        else: pass
     except: print("Some input is wrong, Enter number of ingredients or number of ingredients not actually matching the declared number")
from collections import Counter
counts = dict(Counter(str(elem) for elem in lst_1))
lst_2=[]
print(counts)
for k, v in counts.items():
    if v>1: lst_2.append(eval(k))
for i in lst_1:
    for j in lst_2:
        if i == j:
            x = lst_1.index(i)
            lst_1[x].clear()
print(lst_1)
lst_two = []
lst_three = []
lst_four = []
for i in range(len(lst_1)): lst_1[i].insert(0, i+1)
print(lst_1)
print(len(lst_1))
for a in range(0, len(lst_1), 3) :
    try:
        while len(lst_1[a])>1:
            lst_two.append(lst_1[a])
            break
        while len(lst_1[a+1])>1:
            lst_three.append(lst_1[a+1])
            break
        while len(lst_1[a+2])>1:
            lst_four.append(lst_1[a+2])
            break
    except:pass
print(lst_two)
print(lst_three)
print(lst_four)
a = len(lst_two)%2
b = len(lst_three)%3
c = len(lst_four)%4
if a or b or c !=0:
    lst_two.pop()
    for i in range(b): lst_three.pop()
    for i in range(c): lst_four.pop()
else:pass
print(lst_two)
print(lst_three)
print(lst_four)
delivery = len(lst_two)+len(lst_three)+len(lst_four)
print(delivery)
for i in range(0, len(lst_two), 2):
    print(2, lst_two[i][0], lst_two[i+1][0])
for i in range(0, len(lst_three), 3):
    print(3, lst_three[i][0], lst_three[i+1][0], lst_three[i+2][0])
for i in range(0, len(lst_four), 4):
    print(4, lst_four[i][0], lst_four[i+1][0], lst_four[i+2][0], lst_four[i+3][0])