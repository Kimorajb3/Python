#------------------------------------------------------------------
 # Class: CIST 2742 Beginning Python Programming
 # Term: Fall 2022
 # Instructor: Jianmin Wang
 # Description: Solution to Lab 5 File Processing
 # Due: 2/28/2022
 # author Kimora Bailey
 # version 1.0
 #
 # By turning in this code, I Pledge:
 #  1. That I have completed the programming assignment independently.
 #  2. I have not copied the code from a student or any source.
 #  3. I have not given my code to any student.
 #
 #---------------------------------------------------------------------
from datetime import datetime


# Function to collect data from the user
def collect_records():
	records = []
	while True:
		while True:
			try:
				stu_id = int(input("Enter student Id: "))
				if len(str(stu_id)) != 6:
					print("Invalid input. Try again")
					continue
				break
			except ValueError:
				print("Invalid input. Try again")
				continue
		fname = input("Enter first name: ").title()
		lname = input("Enter last name: ").title()
		test_scores = []
		for i in range(3):
			while True:
				try:
					score = int(input("Enter score of Test "+str(i+1)+": "))
					if score < 0 or score > 100:
						print("Invalid input. Try again")
						continue 
					test_scores.append(score)
					break
				except ValueError:
					print("Invalid input Try again")
					continue
		test_avg = sum(test_scores) / 3
		test_avg = round(test_avg, 2)
		if test_avg >= 90:
			grade = 'A'
		elif test_avg >= 80:
			grade = 'B'
		elif test_avg >= 70:
			grade = 'C'
		elif test_avg >= 60:
			grade = 'D'
		else:
			grade = 'F'
		records.append([stu_id, fname, lname, test_avg, grade])
		opinion = input('Want to add another record?(Y/N): ').upper()
		while opinion not in ['Y','N']:
			print("Invalid input. Try again")
			opinion = input('Want to add another record?(Y/N): ').upper()
		if opinion == 'N':
			break
		print()
	return records



# Function to write data to the file
def write_data(data):
	File = open("studentGrade.txt", 'w')
	File.write("Id,First name,Last name,Test average,Grade\n")
	for r in data:
		File.write(str(r[0])+","+r[1]+","+r[2]+","+str(r[3])+","+r[4]+"\n")
	File.close()
		


# Function to read data from text file
def read_data(filename):
	File = open(filename, 'r')
	for line in File:
		line = line.strip()
		if len(line) != 0:
			line = line.split(',')
			print("{:<13}{:<15}{:<15}{:<18}{}".format(line[0], line[1], line[2], line[3], line[4]))
	File.close()



# Function to search student data 
def search_student(data):
	key = input("Enter Id or First or Last name: ").title()
	found = 0
	if key.isdigit():
		key = int(key)
		for r in data:
			if r[0] == key:
				print(r)
				found += 1
	else:
		for r in data:
			if r[1]==key or r[2]==key:
				print(r)
				found += 1
	if found == 0:
		print("No match found!") 



# Function to write data to text file
def write_records(data):
	File = open("studentGradeReport.txt", "w")
	File.write("Student id,First name,Last name,Grade\n")
	for r in data:
		File.write(str(r[0])+","+r[1]+","+r[2]+","+r[4]+"\n")
	File.close()
		
	
	

# Main function
def main():
	stu_data = collect_records()
	write_data(stu_data)
	print("\n")
	read_data('studentGrade.txt')
	
	while True:
		option = input("\nSearch student?(Y/N): ").upper()
		while option not in ['Y','N']:
			print("Invalid input. Try again")
			option = input("\nSearch student?(Y/N): ").upper()
		if option == 'Y':
			search_student(stu_data)
		else:
			break
	
	write_records(stu_data)
	print("\nThank you & Bye!")
	
	
# Main function call
main()
