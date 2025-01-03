def determine_grade(score):
    if score < 60:
        letter = 'F'
    elif score < 70:
        letter = 'D'
    elif score < 80:
        letter = 'C'
    elif score < 90:
        letter = 'B'
    else:
        letter = 'A'
    return letter

def cal_average(lst):
    for i in range(5):
        sum = lst[i]

    avg = sum/5

    return avg

scList = []

print("Enter scores: ")
for i in range(0,5):
    score = int(input())

    scList.append(score)

print("Score \t Grade")
for i in range(5):
    print(scList[i], "\t", determine_grade(scList[i]))

print("The average of scores: ", cal_average(scList))
