''' conditional statement : {if, else, elseif, switch}'''


age = int(input("Enter the age of the person: "))

if (age < 18):
    print("your aren't eligible to apply")
elif (age > 18 and age < 28): #[and , or, not]
    print("you are eligible to apply")
else:
    print("your aren't eligible to apply")


''' Ternary Operators '''
result = "True Condition" if age > 19 else "False Condition"
print(result)


'''nested if else statements'''
if (1):
    if (0):
        print("Both conditions are True")
    else:
        print("Condition 1 is True, but Condition 2 is False")
else:
    print("Condition 1 is False")


''' match case '''

value = int(input("Enter a number in between 1 and 3"))
match value:
        case 1:
            print("Case 1: One")
        case 2:
            print("Case 2: Two")
        case 3:
            print("Case 3: Three")
        case _:
            print("Default case: Value not matched")