print ("===Guess the Number===")
import random
ans = random.randint(1,100)
count = 1
n = int(input("Guess a integer from 1 to 100: "))
while n != ans:
    if n > 100 or n < 1:
        print("Invaild input. Please try again.")
    elif n > ans:
        print("Your guess was too high.")
    elif n < ans:
        print("Your guess was too low.")
    count += 1
    n = int(input("Try another one: "))
print("Well done! The answer is "+str(ans)+". You've tried",count,"times.")

print("===Bus Fare===")
fr = int(input("What number stop are you at?\n>>"))
to = int(input("What is the stop you want to go to?\n>>"))
f = 5 + 2.5*abs(to-fr)
print("The fare from Stop",fr,"to Stop",to,"is $%.2f"%f+".")

print("===Is it a Strong Password?===")
p = input("Input a password.\n>>")
score = 0
if len(p) >= 7:
    score += 1
if not p.isalnum():
    score += 1
for i in p:
    if i.isupper():
        score += 1
        break
for i in p:
    if i.islower():
        score += 1
        break
for i in p:
    if i.isdigit():
        score += 1  
        break
if score == 5:
    print("Your password is strong.")
elif score == 4 or score == 3:
    print("Your password is moderately strong.")
elif score <= 2:
    print("Your password is weak.")
print("===Guess the Number (Through Letters)===")
import random
ans = random.randint(1,26)
ans = chr(ans+96)
count = 1
n = str.lower(input("Guess a letter: "))
while n != ans:  
    if not n.isalpha or len(n) >= 2:
        print("Invaild input. Try again.")
    elif n > ans:
        print("The letter is before your guess.")
    elif n < ans:
        print("The letter is after your guess.")
    count += 1
    n = str.lower(input("Guess a letter: "))
print("Well done! The answer is "+ans+". You've tried",count,"times.")