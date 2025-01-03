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
