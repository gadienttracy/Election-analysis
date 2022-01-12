voting_data = [{'county':'Arapahoe', 'registered_voters': 422829}, {'county':'Denver', 'registered_voters': 463353}, {'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    for county, voters in county_dict.items():
        print(f'{voting_data["county"]} county has {voting_data["registered_voters"]} registered voters.')




# print(f'{voting_data[0]["county"]} county has {voting_data[0]["registered_voters"]} registered voters.')

    