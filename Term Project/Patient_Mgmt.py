#------------------------------------------------------------------
# Class: CIST 2742 Beginning Python Programming
# Term: Fall 2022
# Instructor: Jianmin Wang
# Description: Solution to Term Project(2): Patient Management System
# Due: 5/03/2022
# author Kimora Bailey
# version 1.0
#
# By turning in this code, I Pledge:
#  1. That I have completed the programming assignment independently.
#  2. I have not copied the code from a student or any source.
#  3. I have not given my code to any student.
#
#---------------------------------------------------------------------
import json
from json import JSONEncoder
import sys
import pickle

class Patient:
    def __init__(self, patid, fn, ln, addr, city, state, z, phonenum, econtact, econtactnum):
        self.__patid = patid
        self.__fn = fn
        self.__ln = ln
        self.__addr = addr
        self.__city = city
        self.__state = state
        self.__z = z
        self.__phonenum = phonenum
        self.__econtact = econtact
        self.__econtactnum = econtactnum

    def setpatid(self, patid):
        self.__patid = patid    
   
    def setfn(self, fn):
        self.__fn = fn
    
    def setln(self, ln):
        self.__ln = ln

    def setaddr(self, addr):
        self.__addr = addr

    def setcity(self, city):
        self.__city = city

    def setstate(self, state):
        self.__state = state
    
    def setz(self, z):
        self.__z = z
    
    def setphonenum(self, phonenum):
        self.__phonenum = phonenum
    
    def setecontact(self, econtact):
        self.__econtact = econtact

    def setecontactnum(self, econtactnum):
        self.__econtactnum = econtactnum


    def __repr__(self):
        return "\nPatient ID: " + str(self.__patid) + "\n" + "First Name: " + str(self.__fn) + "\n" \
               + "Last name: " + str(self.__ln) + "\n" + "Address: " + str(self.__addr) + "\n" + "City: " \
               + str(self.__city) + "\n" + "State: " + str(self.__state) + "\n" + "Zip: " + str(
            self.__z) + "\n" + "Phone #: " + \
               str(self.__phonenum) + "\n" + "Emergency Contact: " + str(
            self.__econtact) + "\n" + "Emergency Contact #: " + str(self.__econtactnum) + "\n" \

class Procedure:
    def __init__(self,patid,procn,procd,doctor,charges):
        self.__patid = patid
        self.__procn = procn
        self.__procd = procd
        self.__doctor = doctor
        self.__charges = charges

    def setpatid(self, patid):
        self.__patid = patid

    def setprocn(self, procn):
        self.__procn = procn

    def setprocd(self, procd):
        self.__procd = procd

    def setdoctor(self, doctor):
        self.__doctor = doctor

    def setcharges(self, charges):
        self.__charges = charges

    def __repr__(self):
        x = float(eval(str(self.__charges)))
        return "\nPatient ID: " + str(self.__patid) + "\n" + "Procedure: " + str(self.__procn) + "\n" \
               + "Date: " + str(self.__procd) + "\n" + "Practitioner: " + str(self.__doctor) + "\n" + "Charges: $" \
               + str(x) + "\n"\

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

Patdictionary = {}
Prdictionary = {}

def AddPat():  # Add a patient and his or her procedure(s)
    ID = input("Enter ID: ")
    FN = input("Enter First Name: ")
    LN = input("Enter Last Name: ")
    ADDR = input("Enter Address: ")
    CITY = input("Enter City: ")
    STATE = input("Enter State: ")
    ZIP = input("Enter ZIP: ")
    PHONE = input("Enter Phone Number: ")
    ECONTACT = input("Enter Emergency Contact: ")
    ECONTACTNUM = input("Enter Emergency Contact Phone #: ")

    PROCN = input("Enter Procedure Name: ")
    PROCD = input("Enter Procedure Date: ")
    DOC = input("Enter Practitioner: ")
    CHARGES = input("Enter Charges: $")

    p = Patient(ID, FN, LN, ADDR, CITY, STATE, ZIP, PHONE, ECONTACT, ECONTACTNUM)
    pr = Procedure(ID, PROCN, PROCD, DOC, CHARGES)
    Patdictionary[ID] = p
    Prdictionary[ID] = pr
    print(Patdictionary[ID])
    print(Prdictionary[ID])
    print('Patient Added Successfully')

def AddProc():
    PID = input("Enter Patient ID: ")
    PROCN = input("Enter Procedure Name: ")
    PROCD = input("Enter Procedure Date: ")
    DOC = input("Enter Practitioner: ")
    CHARGES = input("Enter Charges: $")
    pr = Procedure(PID, PROCN, PROCD, DOC, CHARGES)

    if PID not in Prdictionary:
        Prdictionary[PID] = pr
    else:
        Prdictionary[PID] = [Prdictionary[PID], pr]
    print(str(Prdictionary[PID]).strip('[]'))


def SearchPatByID():
    while True:
        ID = input("Enter Patient ID: ")
        if ID:
            if ID in Patdictionary:
                print(Patdictionary[ID])
                print(str(Prdictionary[ID]).strip('[]'))
                break
            else:
                print(" Not Found ")
                break
        else:
            print("Please Enter ID: ")
            continue

def UpdatePat():
    while True:
        ID = input("Enter ID: ")

        if ID:
            if ID in Patdictionary and Prdictionary:
                ID = input("Enter new ID: ")
                FN = input("Enter First Name: ")
                LN = input("Enter Last Name: ")
                ADDR = input("Enter Address: ")
                CITY = input("Enter City: ")
                STATE = input("Enter State: ")
                ZIP = input("Enter ZIP: ")
                PHONE = input("Enter Phone Number: ")
                ECONTACT = input("Enter Emergency Contact: ")
                ECONTACTNUM = input("Enter Emergency Contact Phone #: ")

                PROCN = input("Enter Procedure Name: ")
                PROCD = input("Enter Procedure Date: ")
                DOC = input("Enter Practitioner: ")
                CHARGES = input("Enter Charges: $")

                p = Patient(ID, FN, LN, ADDR, CITY, STATE, ZIP, PHONE, ECONTACT, ECONTACTNUM)
                pr = Procedure(ID, PROCN, PROCD, DOC, CHARGES)
                Patdictionary[ID] = p
                Prdictionary[ID] = pr
                break
            else:
                print(" Not Found ")
                break
        else:
            print("Please Enter ID: ")
            continue
def DelPat():
    while True:
        ID = input("Enter ID: ")
        if ID:
            if ID in Patdictionary and Prdictionary:
                del Patdictionary[ID]
                del Prdictionary[ID]
                break
            else:
                print(" Not Found ")
                break
        else:
            print("Please Enter ID: ")
            continue

def SavePatPick():
    file = open("patient.txt", "wb")
    pickle.dump(Patdictionary, file)
    file.close()

def SaveProcPick():
    File = open("procedure.txt", "wb")
    pickle.dump(Prdictionary, File)
    File.close()

def SavePatJson():
    Encoder().encode(Patdictionary)
    fp = open("patient.json", "w")
    json.dump(Patdictionary, fp, cls = Encoder)
    fp.close()

def SaveProcJson():
    Encoder().encode(Prdictionary)
    fp = open("procedure.json", "w")
    json.dump(Prdictionary, fp, cls=Encoder)
    fp.close()
try:
    file = open('patient.txt', 'rb')
    Patdictionary = pickle.load(file)
    file.close()
except:
    Patdictionary = {}

try:
    File = open('procedure.txt', 'rb')
    Prdictionary = pickle.load(File)
    File.close()
except:
    Prdictionary = {}

while True:
    print("1. Add Patient Info")
    print("2. Add Procedure")
    print("3. Search Patient by ID")
    print("4. Change Patient Info")
    print("5. Delete Patient")
    print("6. Exit")

    c = input("Input Response: ")
    if c == "1":
        AddPat()
    elif c == "2":
        AddProc()
    elif c == "3":
        SearchPatByID()
    elif c == "4":
        UpdatePat()
    elif c == '5':
        DelPat()
    elif c == '6':
        SavePatPick()
        SaveProcPick()
        SavePatJson()
        SaveProcJson()
        sys.exit()
    else:
        print('Enter correct response ')


