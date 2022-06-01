import random
print("Welcome to the Website Name Generator.")
# print("What's name of the city you grow up in?")
tech=input("What's the basic Technology you used in it?\n")
# print("What's your pet's name")
team_leader=input("What's your team leader's name\n")
work = input("What's the use of your website?\n")
field = input("this technology will be usefull for which field\n")
list = [tech , team_leader , work, field]
print("Your Website name could be www." + random.choice(list)  + random.choice(list) +".com")
print("Your Website name could be www." + random.choice(list) + random.choice(list) +".com")
print("Your Website name could be www." + random.choice(list) + random.choice(list) +".com")
