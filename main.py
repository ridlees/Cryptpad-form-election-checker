import json
import operator
import sys

def get_winner(path):
    election = {}
    with open(path) as fp:
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
                    if vote == "":
                        break
                    if vote in election:
                        election[vote] = election[vote] + vote_weight
                    else:
                        election[vote] = vote_weight
                    vote_weight = vote_weight/2
        return election
                


if __name__ == "__main__":
    path = sys.argv[1]
    election = get_winner(path)
    print(max(election.items(), key=operator.itemgetter(1)))
    print(election)
    print("\nDone!")
