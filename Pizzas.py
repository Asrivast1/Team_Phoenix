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
lst_two = []
lst_three = []
lst_four = []
for i in range(len(lst_1)):
    if len(lst_1[i:])>=2 & (lst_1[i] & lst_1[i+1] != []) & (sorted(lst_1[i]) != sorted(lst_1[i+1])):
        while(len(lst_two)< 2*team_two):
            lst_two.append(lst_1[i])
            lst_two.append(lst_1[i+1])
            break
        break
    if len(lst_1[i:])>=3 & (lst_1[i] & lst_1[i+1] & lst_1[i+2] != []) & (sorted(lst_1[i]) != sorted(lst_1[i+1]) != sorted(lst_1[i+2])):
        while(len(lst_three)< 3*team_three):
            lst_three.append(lst_1[i])
            lst_three.append(lst_1[i+1])
            lst_three.append(lst_1[i+2])
            break
        break
    if len(lst_1[i:]) >= 4 & (lst_1[i] & lst_1[i+1] & lst_1[i+2] & lst_1[i+3] != []) & (sorted(lst_1[i]) != sorted(lst_1[i+1]) != sorted(lst_1[i+2]) != sorted(lst_1[i+3])):
        while(len(lst_four)< 4*team_four):
            lst_four.append(lst_1[i])
            lst_four.append(lst_1[i+1])
            lst_four.append(lst_1[i+2])
            lst_four.append(lst_1[i+3])
            break
        break
    continue
print(lst_two)
print(lst_three)