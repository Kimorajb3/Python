#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 3.4 Distance Travelled
 # Due: 2/14/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
def show_travel(time,speed):
    print("Hour\tDistance Travelled\n")
    print("-----\t----------------\n");
    for i in range(1,time+1):
        res = i *speed
        print('%d\t\t%.1f'%(i,res))

def main():
    speed=int(input("Enter the speed of the vehicle in mph: "))
    while speed <= 0:
        print("speed must be greater than zero \n")
        speed=int(input("Enter the speed of the vehicle in mph: "))
    time=int(input("Enter the number of hours travelled: "))
    while time <= 0:
        print("time must be greater than zero \n")
        time=int(input("Enter the number of hours travelled: "))
    show_travel(time,speed)

if __name__== "__main__":
    main()
