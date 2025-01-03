pc1 = input("Enter primary color:")
pc2 = input("Enter primary color:")

if (pc1 == "red" and pc2 == "blue") or (pc1 == "blue" and pc2 == "red"):
    print("When you mix red and blue, you get purple.")

elif (pc1 == "blue" and pc2 == "yellow") or (pc1 == "yellow" and pc2 == "blue"):
    print("When you mix blue and yellow, you get green.")

elif (pc1 == "yellow" and pc2 == "red") or (pc1 == "red" and pc2 == "yellow"):
    print("When you mix yellow and red, you get orange.")

else:
    print("You didn't input two primary colors.")
