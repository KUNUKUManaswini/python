print("-------------smart school day planner---------------------")
wether=input("enter the wether?(sunny,cold,rainy)")
day=input("enter the day?(monday to sunday)")
home_work=input("is your homework done?(yes/no)")
if day==("saturday/sunday"):
    print("it's weekend, time to enjoy")
elif day==("monday"):
    print("time to go to school,and enjoy")
elif day==("friday"):
    print("last day of school,you can have a movie night ")
else:
    print("day not recognised")
if wether=="sunny" and home_work=="yes":
    print("you can go play")
if wether=="rainy":
    print("take your umbrella")
if wether=="sunny"and not home_work=="yes":
    print("complete home_workand then go to play")
elif wether=="sunny"and home_work=="yes" and not("in(saturday or sunday)"):
    print("all set for tommorw's school")
print("have a nice day")


