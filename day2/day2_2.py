file1 = open('day2_data.txt', 'r')
lines = file1.readlines()  

handScore = {
  "R": 1,
  "P": 2,
  "S": 3
}

roundScore = {
    "W" : 6,
    "D" : 3,
    "L" : 0   
}

selfHandDecode = {
    "R W" : "P",
    "R L" : "S",
    "R D" : "R",
    "P W" : "S",
    "P L" : "R",
    "P D" : "P",
    "S W" : "R",
    "S L" : "P",
    "S D" : "S",
}

def getScore(round) :    
    score = roundScore[round[-1]]
    score += handScore[selfHandDecode[round]]
    return score

# Opponent
# A - Rock
# B - Paper
# C - Sissors

# Self
# X - Lose
# Y - Draw
# Z - Win
formattedLines = [line.replace("A", "R") for line in lines]
formattedLines = [line.replace("B", "P") for line in formattedLines]
formattedLines = [line.replace("C", "S") for line in formattedLines]
formattedLines = [line.replace("X", "L") for line in formattedLines]
formattedLines = [line.replace("Y", "D") for line in formattedLines]
formattedLines = [line.replace("Z", "W") for line in formattedLines]
rounds = [line.strip() for line in formattedLines]
print(getScore(rounds[1]))

score = sum([getScore(round) for round in rounds])
print(score)

