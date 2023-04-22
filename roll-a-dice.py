import random
randomize = input("Enter if you want to roll the dice or not")

response = "yes"
while response == "yes": 
    y = random.randint(1,6)
    print("[{y} {y} {y}]")