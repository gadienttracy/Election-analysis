pyprint("Hello World")

print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)


print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / 2 - 4))
print(5 + (9 * 3 / (2 - 4)))

counties_tuple = ("Arapahoe","Denver","Jefferson")
print (counties_tuple[1])

counties_dict = {}
counties_dict ["Arapahoe"]= 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print (counties_dict.get("Denver"))

voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"El Paso","registered_voters":461149})
print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")