# A python for loop can also be used to iterate through a list, tuple, string or even a dictionary'

name = "Hope"

for letter in name:
    if letter == "o":
        print("This is letter o")
    else:
        print(letter)

    print('================')
# below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]        
print(counties)

for county in counties:
    print(county)

    print('==========================')
for county in counties:
    if county == "Nakuru":
     print("county is part of the list")
     break
else:
     print("county not found")
print('==========================')
# the for loop can also be used to iterate through a dictionary

player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG", "Monaco", "France"],
    "nationality" : "French"
}
for key in player:
    print(key)
    for values in player:
     print(player[values])

    print('==========================')
    #  loop through the teams has played for
    for team in player["teams"]:
       print(team)
