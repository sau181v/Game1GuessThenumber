from random import randint

start = 1
end = 10000

values = randint(start, end)

print("the system has chosen a value between", start, "and", end)

guess = None
while guess != values:
    user_gn = input("enter the guessed number ")
    guess = int(user_gn)
    if values > guess:
        print("The value is higher ")
    elif values < guess:
        print("The value is lower ")

print("CONGRATULATIONS! you guessed the correct number.. you won")
