import random

# Generate a lottery number
lottery = random.randint(0, 999)

# prompt the user to enter a guess
guess = eval(input("Enter your lottery pick(three digit): "))

# Get digit from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery % 100

# Get digit from guess
guessDigit1 = guess // 100
guessDigit2 = guess % 100

print("The lottery number is", lottery)

# check the guess 
if guess == lottery:
    print("Exact match: you win $200")
elif ( guessDigit2 == lotteryDigit1 and \
      guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $150")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2 
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $100")
else:
    print("Sorry, no match")
