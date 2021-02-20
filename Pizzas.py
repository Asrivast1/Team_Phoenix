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
print(lst_1)
print(sorted(lst_1[1])==sorted(lst_1[3]))




