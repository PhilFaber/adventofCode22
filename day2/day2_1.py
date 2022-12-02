file1 = open('day2_data.txt', 'r')
lines = file1.readlines()  

handScore = {
  "R": 1,
  "P": 2,
  "S": 3
}

bizRules = {
    "R R" : 3,
    "R P" : 6,
    "R S" : 0,
    "P R" : 0,
    "P P" : 3,
    "P S" : 6,
    "S R" : 6,
    "S P" : 0,
    "S S" : 3,
}

def getScore(round) :
    score = handScore[round[-1]]
    score += bizRules[round]
    return score

# Opponent
# A - Rock
# B - Paper
# C - Sissors

# Self
# X - Rock
# Y - Paper
# Z - Scissors
formattedLines = [line.replace("A", "R") for line in lines]
formattedLines = [line.replace("B", "P") for line in formattedLines]
formattedLines = [line.replace("C", "S") for line in formattedLines]
formattedLines = [line.replace("X", "R") for line in formattedLines]
formattedLines = [line.replace("Y", "P") for line in formattedLines]
formattedLines = [line.replace("Z", "S") for line in formattedLines]
rounds = [line.strip() for line in formattedLines]

score = sum([getScore(round) for round in rounds])
print(score)

