import collections
result = collections.OrderedDict()
sum_, votes = 0, []
with open("input.txt") as file:
    for line in file:
        words = line.split()
        result[' '.join(words[:-1])] = 0
        votes.append([' '.join(words[:-1]), int(words[-1])])
        sum_ += int(words[-1])
first_div = sum_ / 450
free_place = 450
for i in range(len(votes)):
    party = votes[i]
    result[party[0]] += party[1] // first_div
    party.append(party[1] % first_div)
    free_place -= party[1] // first_div
votes.sort(key=lambda x : x[2], reverse=True)
for i in range(int(free_place)):
    result[votes[i][0]] += 1
for name in result.keys():
    print(name, int(result[name]))