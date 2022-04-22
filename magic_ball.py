import random

#Set a name variable
name = input("What's your name: ")
input(f"Welcome {name},\n Whats Your question for the magic ball???")

# print("\n")
# print("Play Magic 8 ball by selecting a number from 1 to 10")
# print("\n")


choice= random.randint(1,10)

if choice == 1:
   answer= "It's Certain"

elif choice == 2:
    answer ="Yes"

elif choice == 3:
    answer ="Most Likely"

elif choice == 4:
    answer ="ASk again later"

elif choice == 5:
    answer ="Outlook not so good"

elif choice == 6:
    answer ="Better Not Tell You Now"

elif choice == 7:
    answer ="My reply is no"

elif choice == 8:
    answer ="Dont Count on it"

elif choice == 9:
    answer ="Very Doubful"

else: 
    answer ="No"

print("Magic 8 Ball is: ",answer)
  