meat = 0
while meat < 5:
    print("Meat time boy.")
    meat = meat + 1

while True:
    print("What kind of meat do you like?")
    new_meat = input()
    if new_meat == "steak":
        break
print("Good choice")

a = [1, 3, 5, 7, 9, 11]
[i - 1 for i in a]
print(a)
