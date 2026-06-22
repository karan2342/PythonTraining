import random

#generate the  a random 4 digit number

secret_num = random.randrange(1000, 10000)

attempts = 0

print("Welcome to mastermind game!")
print("Try to guess 4 digit number. \n")

while True:
  
   try:
     guess = int(input("guess the 4 digit number : "))
     
     if guess <1000 or guess > 9999:
       print("Please Enter valid number")
       continue
     
   except ValueError:
     print("Please enter numeric digit only")
     continue
   
   attempts += 1
   
   #correct guess
   if guess == secret_num:
     print("You become a mastermind!")
     print(f"It took you only {attempts} tries ")
     break

   # convert number to string for digit comparison
   guess_str = str(guess)
   secret_str = str(secret_num)

   count = 0
   correct = ["X"] * 4

   # check each digit
   for i in range(4):
     if guess_str[i] == secret_str[i]:
       count += 1
       correct[i] = guess_str[i]

   print(f"Not quite the number. You got {count} digit(s) correct")

   if count > 0:
     print("Correctly placed digit(s):")
     print(" ".join(correct))

   print()
   