import random
import time

#defining a function named computer_guess having two parameters x and y

def computer_guess(x,y):
    low=lr
    high=ur
    feedback=''

    #here we consider too high as h, too low as l and correct as c
    # the following loop will continue to run till feedback is not 'c' i.e. correct

    while feedback !='c':

        #if lr and ur set to same value, it throws an error.
        #this if conditon is used to fix that error.

        if low!=high:
            guess=random.randint(low, high)
        else:
            guess=low   #could also be high; because low=high

        feedback=input(f"Is {guess} too high(h), too low(l) or correct(c)?")
        if feedback=='h':
            high=guess-1  #cancel out all the values >= recent guess and set guess-1 value as high

        elif feedback=='l':
            low=guess+1   #cancel out all the values <= recent guess and set guess+1 value as low

    # if while condition is false, it directly comes to this line.
    print(f"Yay! The computer guessed the number {guess} correctly !!!")

print("Please think of a number in your mind ( Don't mention it! )")
time.sleep(4)  #waits execution of the current thread for 4 seconds.

#taking lower and upper limit of the range from the user

lr=int(input("Enter lower limit of a range between which the computer has to guess your number:"))
ur=int(input("Enter upper limit of a range between which the computer has to guess your number:"))

#calling the function

computer_guess(lr,ur)
