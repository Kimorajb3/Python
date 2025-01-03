def cal_average(n1,n2,n3,n4,n5):
    return (n1+n2+n3+n4+n5)/5

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

def main():
    n1 = eval(input("Enter test score1: "))
    n2 = eval(input("Enter test score2: "))
    n3 = eval(input("Enter test score3: "))
    n4 = eval(input("Enter test score4: "))
    n5 = eval(input("Enter test score5: "))
    print("\nScore\tLetterGrade")
    print("------------------------")
    print(n1,"\t\t",determine_grade(n1))
    print(n2, "\t\t", determine_grade(n2))
    print(n3, "\t\t", determine_grade(n3))
    print(n4, "\t\t", determine_grade(n4))
    print(n5, "\t\t", determine_grade(n5))
    avg = calc_average(n1,n2,n3,n4,n5)
    print("\nAverage test score =",avg)

main()
