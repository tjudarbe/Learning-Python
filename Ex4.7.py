def computegrade(score):
    if newScore >= 0.9 and newScore < 1:
        return 'A'
    elif newScore >= 0.8 and newScore < 0.9:
        return 'B'
    elif newScore >= 0.7 and newScore < 0.8:
        return 'C'
    elif newScore >= 0.6 and newScore < 0.7:
        return 'D'
    elif newScore <= 0.6 and newScore < 0.6:
        return 'F'
    else:
        return 'Bad Score'

try:
    regScore = input("Enter score: ")
    newScore = float(regScore)
except:
    print('Bad Score')
    quit()

print(computegrade(newScore))
