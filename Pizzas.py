from collections import Counter
lst_1 = [] # For storing the information about pizza
fname = input("Enter the file name: ")
fhand = open(fname)
lst=[]
for line in fhand:
    lines = line.split()
    lst_1.append(lines)
lst_1.pop(0)
for i in range(len(lst_1)): #lst_1 contains all the pizza's information
     try: # Try catch and if else loop deleting inconsistent lists
        if len(lst_1[i]) == int(lst_1[i][0]): lst_1.remove(lst_1[i])
        else: pass
     except: print("Some input is wrong, Enter number of ingredients or number of ingredients not actually matching the declared number")
counts = dict(Counter(str(elem) for elem in lst_1)) # Using counter function to scrape off the repetition by forming key value pair
lst_2=[] # Auxiliary list
for k, v in counts.items():
    if v>1: lst_2.append(eval(k))
for i in lst_1:
    for j in lst_2:
        if i == j:
            x = lst_1.index(i)
            lst_1[x].clear()
lst_two = [] # For storing two teams pizza
lst_three = [] # For storing three teams pizza
lst_four = [] # For storing four teams pizza
for i in range(len(lst_1)): lst_1[i].insert(0, i+1) # Inserting index number of pizzas for easy facilitation
for a in range(0, len(lst_1), 3) : # Alloting pizzas to different teams
    try:
        while len(lst_1[a])>1:
            lst_two.append(lst_1[a])
            break
    except:continue
    try:
        while len(lst_1[a+1])>1:
            lst_three.append(lst_1[a+1])
            break
    except:continue
    try:
        while len(lst_1[a+2])>1:
            lst_four.append(lst_1[a+2])
            break
    except:continue
a = len(lst_two)%2 # Deleting non teamed pizzas
b = len(lst_three)%3
c = len(lst_four)%4
if a or b or c !=0:
    for i in range(a):lst_two.pop(0)
    for i in range(b): lst_three.pop(0)
    for i in range(c): lst_four.pop(0)
else:pass
list_a=[]
list_b=[]
list_c=[]
for i in range(0, len(lst_two)) : list_a.append([str(j) for j in lst_two[i]])
for k in range(0, len(lst_three)) : list_b.append([str(l) for l in lst_three[k]])
for m in range(0, len(lst_four)) : list_c.append([str(n) for n in lst_four[m]])
for pizza in list_a:pizza.pop(0)
for pizza in list_b:pizza.pop(0)
for pizza in list_c:pizza.pop(0)
list_x=[]
for i in range(0, len(lst_two), 2): # Printing number of pizzas delivered to each team
    try:
        while sorted(list_a[i]) != sorted(list_a[i+1]):
            list_x.append(lst_two[i][0])
            list_x.append(lst_two[i+1][0])
            break
    except:pass
for i in range(0, len(lst_three), 3):
    try:
        while sorted(list_b[i])!= sorted(list_b[i+1]) and sorted(list_b[i])!= sorted(list_b[i+3]):
            list_x.append(lst_three[i][0])
            list_x.append(lst_three[i+1][0])
            list_x.append(lst_three[i+2][0])
            break
    except:pass
for i in range(0, len(lst_four), 4):
    try:
        while sorted(list_c[i])!=sorted(list_c[i+1]) and sorted(list_c[i+2])!=sorted(list_c[i+3]) and sorted(list_c[i]) != sorted(list_c[i+3]):
            list_x.append(lst_four[i][0])
            list_x.append(lst_four[i+1][0])
            list_x.append(lst_four[i+2][0])
            list_x.append(lst_four[i+3][0])
            break
    except:pass
print(len(list_x)) # Number of pizzas delivered
for i in range(0, len(lst_two), 2): # Printing pizzas delivered to each team
    try:
        while sorted(list_a[i]) != sorted(list_a[i+1]):
            print(2, lst_two[i][0], lst_two[i+1][0])
            break
    except:pass
for i in range(0, len(lst_three), 3):
    try:
        while sorted(list_b[i])!= sorted(list_b[i+1]) and sorted(list_b[i])!= sorted(list_b[i+3]):
            print(3, lst_three[i][0], lst_three[i+1][0], lst_three[i+2][0])
            break
    except:pass
for i in range(0, len(lst_four), 4):
    try:
        while sorted(list_c[i])!=sorted(list_c[i+1]) and sorted(list_c[i+2])!=sorted(list_c[i+3]) and sorted(list_c[i]) != sorted(list_c[i+3]):
            print(4, lst_four[i][0], lst_four[i+1][0], lst_four[i+2][0], lst_four[i+3][0])
            break
    except:pass