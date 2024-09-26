list1 = []

limit = int(input("Enter limit value: " ))
for i in range(limit):
    
    e = input("Enter value:")
    
    list1.append(e)
    print("Updated List: ", list1)

for j in range(len(list1) - 1):
    for k in range(len(list1) - 1 - j):
        
        if list1[k] > list1[k + 1]:
            list1[k], list1[k + 1] = list1[k + 1], list1[k]
            print("List after swap " , list1)
    
    print("")

print("Sorted List:", list1)
