#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 6.1 Test Average and Grade List
 # Due: 3/14/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
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
