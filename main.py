import json
import operator

election = {}
with open('Form - Sat, 13 July 2024-4.json') as fp:
    data = json.load(fp)
    responses = data["responses"]
    questions = data["questions"]
    for question in questions:
        print(questions[question]["question"])
        print("\n\n")
        for response in responses:
            votes = response[question]
            vote_weight = 1
            for vote in votes:
                if vote == "Abstain":
                    break
                if vote in election:
                    election[vote] = election[vote] + vote_weight
                else:
                    election[vote] = vote_weight
                vote_weight = vote_weight/2
                
print(max(election.items(), key=operator.itemgetter(1)))
