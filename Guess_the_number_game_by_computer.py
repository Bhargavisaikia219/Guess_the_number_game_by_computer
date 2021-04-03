import random
import time

def computer_guess(x,y):
    low=lr
    high=ur
    feedback=''
    while feedback !='c':
        if low!=high:
            guess=random.randint(low, high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(h), too low(l) or correct(c)?")
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Yay! The computer guessed the number {guess} correctly !!!")

print("Please think of a number in your mind ( Don't mention it! )")
time.sleep(4)

lr=int(input("Enter lower limit of a range between which the computer has to guess your number:"))
ur=int(input("Enter upper limit of a range between which the computer has to guess your number:"))

computer_guess(lr,ur)
