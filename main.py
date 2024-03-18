from competition import Competition

participants1 = [
    {'name': "Habanero Hillary", 'chickenwings': 5 , 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob" , 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]
competition1 = Competition(participants1)
print("Example 1:")
print(competition1.scoreboard())


participants2 = [
    {'name': "Spicy Sam", 'chickenwings': 10 , 'hamburgers': 10, 'hotdogs': 10},
    {'name': "Cheesy Charlie" , 'chickenwings': 15, 'hamburgers': 5, 'hotdogs': 5},
    {'name': "Hotdog Harry" , 'chickenwings': 5, 'hamburgers': 5, 'hotdogs': 20}
]
competition2 = Competition(participants2)
print("\nExample 2:")
print(competition2.scoreboard())

participants3 = [
    {'name': "BBQ Betty", 'chickenwings': 15 , 'hamburgers': 10, 'hotdogs': 5},
    {'name': "Grill Master" , 'chickenwings': 20, 'hamburgers': 15, 'hotdogs': 10},
    {'name': "Sizzle Sally" , 'chickenwings': 10, 'hamburgers': 5, 'hotdogs': 5}
]
competition3 = Competition(participants3)
print("\nExample 3:")
print(competition3.scoreboard())
