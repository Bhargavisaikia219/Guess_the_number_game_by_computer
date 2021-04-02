import random
def computer_guess(x,y):
    low=lr
    high=ur
    feedback=''
    while feedback !='c':
        guess=random.randint(low, high)
        feedback=input(f"Is {guess} too high(h), too low(l) or correct(c)?")
    print(f"Yay! The computer guessed your number {guess} correctly!!!")

lr=int(input("Enter a range between which you what to guess a random number: lower limit:"))
ur=int(input("Enter a range between which you what to guess a random number: upper limit:"))

computer_guess(lr,ur)


