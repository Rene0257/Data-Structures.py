import random

num_list = [12, 34, 56, 25, 86, 90, 29, 35, 66, 75, 56, 346, 352, 765]
selected_num = random.choice(num_list)

print("Welcome to the Number Guessing Game!🤩")
print("Number List:", end=" ")
for i in num_list:
    if num_list.index(i) == -1:
        print(f"{i}.")
    else:
        print(f"{i},", end =" ")

user_guess = int(input("Guess any number: "))

if user_guess < selected_num:
    print("Guess a larger number.")
elif user_guess > selected_num:
    print("Guess a smaller number.")
else:
    print("Bravo! You found the number.🥳🥳🥳")

print("Thank you for playing the game!❤️")