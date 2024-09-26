list = []  
limit = 16
for i in range (limit-len(list)):
    e = int(input("Enter Values"))
    list.append 

print("\nAccount Number: ", list)

x = list.pop() 

list.reverse()
print("Reversed: ", list)

for i in range(len(list)):
    if i % 2 == 0:
        list[i] *= 2
        if list[i] > 9:
            list[i] -= 9

print("Minus by 9: ",list)

e = sum(list) + x
print("Sum of all digits: ", e)
is_valid = e % 10 == 0
print("Is the account number valid? ", is_valid)
