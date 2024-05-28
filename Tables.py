#Let's make a table program!
multiplier = int(input("What is the multiplier? "))
till = int(input("Till where do you want to multiply? "))
multiplicand = 1
while multiplicand <= till :
    print(multiplier , "*" , multiplicand , "=" , multiplier * multiplicand)
    multiplicand = multiplicand + 1
