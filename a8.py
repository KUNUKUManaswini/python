temprature=int(input("entertemprature"))
if temprature<20:
    print("it is cold today,wear jacket")
else:
    print("it is warm today,wear t-shirt")
rain=input("is it raining(yes/no)")
if rain=="yes":
    print("bring umbrella")
else:
    print("umbrella not required")
wind=int(input("enter wind speed"))
if wind<20:
    print("wear wind breaker")
else:
    print("wind breaker not required")
puddle=input("are there puddles(yes/no)")
if puddle=="yes":
    print("ground is wet ,wear boots")
else:
    print("ground is dry ,wear shoes")
    
