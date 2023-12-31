'''
(Written In Python)
Copy Paste Into Your Own IDE
Find Your Future Career
'''

import tkinter as tk
import os
import sys
from tkinter import *
import subprocess

window = tk.Tk()
window.geometry("500x1000")
window.resizable(False, False)
window.configure(bg="#000220")

User = {
  "salary":"",
  "interest":"",
  "location":"",
  "hours":"",
  "balance":"",
  "flex":""
}

def Tech():
  User["interest"] = "Tech"
  print(User)
def Medical():
  User["interest"] = "Medical"
  print(User)
def Math():
  User["interest"] = "Math"
  print(User)
def Science():
  User["interest"] = "Science"
  print(User)
def Law():
  User["interest"] = "Law"
  print(User)
def Business():
  User["interest"] = "Business"
  print(User)
def Teaching():
  User["interest"] = "Teaching"
  print(User)
def High():
  User["salary"] = "High"
  print(User)
def Decent():
  User["salary"] = "Decent"
  print(User)
def NoPrefSal():
  User["salary"] = "No Pref"
  print(User)
def Office():
  User["location"] = "Office"
  print(User)
def WFH():
  User["location"] = "WFH"
  print(User)
def BothLoc():
  User["location"] = "Both"
  print(User)
def NoPrefLoc():
  User["location"] = "No Pref"
  print(User)
def Long():
  User["hours"] = "Long"
  print(User)
def Average():
  User["hours"] = "Average"
  print(User)
def Short():
  User["hours"] = "Short"
  print(User)
def NoPrefHours():
  User["hours"] = "No Pref"
  print(User)
def GoodBal():
  User["balance"] = "Good"
  print(User)
def MinBal():
  User["balance"] = "Min"
  print(User)
def NoPrefBal():
  User["balance"] = "No Pref"
  print(User)
def GoodFlex():
  User["flex"] = "Good"
  print(User)
def MinFlex():
  User["flex"] = "Min"
  print(User)
def NoPrefFlex():
  User["flex"] = "No Pref"
  print(User)
def quit():
  os._exit(os.EX_OK)

Software_Developer = {
  "salary":"Decent",
  "interest":"Tech",
  "location":"Both",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Nurse = {
  "salary":"Decent",
  "interest":"Medical",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Good"
}
Physician = {
  "salary":"High",
  "interest":"Medical",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
Financial_Manager = {
  "salary":"Decent",
  "interest":"Math",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
IT_Manager = {
  "salary":"Decent",
  "interest":"Tech",
  "location":"Office",
  "hours":"Average",
  "balance":"Min",
  "flex":"Min"
}
Web_Developer = {
  "salary":"Decent",
  "interest":"Tech",
  "location":"Both",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Dentist = {
  "salary":"High",
  "interest":"Medical",
  "location":"Office",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Lawyer = {
  "salary":"Decent",
  "interest":"Law",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
Veterinarian = {
  "salary":"High",
  "interest":"Medical",
  "location":"Office",
  "hours":"Average",
  "balance":"Min",
  "flex":"Good"
}
Orthodontist = {
  "salary":"High",
  "interest":"Medical",
  "location":"Office",
  "hours":"Average",
  "balance":"Min",
  "flex":"Good"
}
Pyschologist = {
  "salary":"Decent",
  "interest":"Science",
  "location":"Both",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Statistician = {
  "salary":"Decent",
  "interest":"Math",
  "location":"Office",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Teacher = {
  "salary":"Decent",
  "interest":"Teaching",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
Doctor = {
  "salary":"High",
  "interest":"Medical",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
Data_Scientist = {
  "salary":"Decent",
  "interest":"Science",
  "location":"Both",
  "hours":"Long",
  "balance":"Good",
  "flex":"Good"
}
Marketing_Manager = {
  "salary":"Decent",
  "interest":"Business",
  "location":"Both",
  "hours":"Avergae",
  "balance":"Good",
  "flex":"Good"
}
Engineer = {
  "salary":"Decent",
  "interest":"Science",
  "location":"Office",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Computer_Systems_Analyst = {
  "salary":"Decent",
  "interest":"Tech",
  "location":"Both",
  "hours":"Average",
  "balance":"Good",
  "flex":"Good"
}
Entrepreneur = {
  "salary":"Decent",
  "interest":"Business",
  "location":"Office",
  "hours":"Long",
  "balance":"Min",
  "flex":"Min"
}
Accountant = {
  "salary":"Decent",
  "interest":"Math",
  "location":"Both",
  "hours":"Average",
  "balance":"Good",
  "flex":"Min"
}

job_list = [Software_Developer, Nurse, Physician, Financial_Manager, 
            IT_Manager, Web_Developer, Dentist, 
            Lawyer, Veterinarian, Orthodontist, 
            Pyschologist, Statistician, Teacher, 
            Doctor, Data_Scientist, Marketing_Manager, 
            Engineer, Computer_Systems_Analyst, Entrepreneur, Accountant]

potential_jobs = []

def calc():
  
  Software_DeveloperCount = 0
  NurseCount = 0
  PhysicianCount = 0
  Financial_ManagerCount = 0
  IT_ManagerCount = 0
  Web_DeveloperCount = 0
  DentistCount = 0
  LawyerCount = 0
  VeterinarianCount = 0
  OrthodontistCount = 0
  PyschologistCount = 0
  StatisticianCount = 0
  TeacherCount = 0
  DoctorCount = 0
  Data_ScientistCount = 0
  Marketing_ManagerCount = 0
  EngineerCount = 0
  Computer_Systems_AnalystCount = 0
  EntrepreneurCount = 0
  AccountantCount = 0
  
  for keys in User.keys():
    if User["interest"] == Software_Developer["interest"]:
      if User[keys] == "No Pref":
        Software_DeveloperCount += 1
      if User[keys] == Software_Developer[keys]:
        Software_DeveloperCount += 1
    else:
      break
  if Software_DeveloperCount >= 4:
    potential_jobs.append("Software Developer")
  
  for keys in User.keys():
    if User["interest"] == Nurse["interest"]:
      if User[keys] == "No Pref":
        NurseCount += 1
      if User[keys] == Nurse[keys]:
        NurseCount += 1
    else:
      break
  if NurseCount >= 4:
    potential_jobs.append("Nurse")
  
  for keys in User.keys():
    if User["interest"] == Physician["interest"]:
      if User[keys] == "No Pref":
        PhysicianCount += 1
      if User[keys] == Physician[keys]:
        PhysicianCount += 1
    else:
      break
  if PhysicianCount >= 4:
    potential_jobs.append("Physician")
  
  for keys in User.keys():
    if User["interest"] == Financial_Manager["interest"]:
      if User[keys] == "No Pref":
        Financial_ManagerCount += 1
      if User[keys] == Financial_Manager[keys]:
        Financial_ManagerCount += 1
    else:
      break
  if Financial_ManagerCount >= 4:
    potential_jobs.append("Financial Manager")
  
  for keys in User.keys():
    if User["interest"] == IT_Manager["interest"]:
      if User[keys] == "No Pref":
        IT_ManagerCount += 1
      if User[keys] == IT_Manager[keys]:
        IT_ManagerCount += 1
    else:
      break
  if IT_ManagerCount >= 4:
    potential_jobs.append("IT Manager")
  
  for keys in User.keys():
    if User["interest"] == Web_Developer["interest"]:
      if User[keys] == "No Pref":
        Web_DeveloperCount += 1
      if User[keys] == Web_Developer[keys]:
        Web_DeveloperCount += 1
    else:
      break
  if Web_DeveloperCount >= 4:
    potential_jobs.append("Web Developer")
  
  for keys in User.keys():
    if User["interest"] == Dentist["interest"]:
      if User[keys] == "No Pref":
        DentistCount += 1
      if User[keys] == Dentist[keys]:
        DentistCount += 1
    else:
      break
  if DentistCount >= 4:
    potential_jobs.append("Dentist")
  
  for keys in User.keys():
    if User["interest"] == Lawyer["interest"]:
      if User[keys] == "No Pref":
        LawyerCount += 1
      if User[keys] == Lawyer[keys]:
        LawyerCount += 1
    else:
      break
  if LawyerCount >= 4:
    potential_jobs.append("Lawyer")
  
  for keys in User.keys():
    if User["interest"] == Veterinarian["interest"]:
      if User[keys] == "No Pref":
        VeterinarianCount += 1
      if User[keys] == Veterinarian[keys]:
        VeterinarianCount += 1
    else:
      break
  if VeterinarianCount >= 4:
    potential_jobs.append("Veterinarian")
  
  for keys in User.keys():
    if User["interest"] == Orthodontist["interest"]:
      if User[keys] == "No Pref":
        OrthodontistCount += 1
      if User[keys] == Orthodontist[keys]:
        OrthodontistCount += 1
    else:
      break
  if OrthodontistCount >= 4:
    potential_jobs.append("Orthodontist")
  
  for keys in User.keys():
    if User["interest"] == Pyschologist["interest"]:
      if User[keys] == "No Pref":
        PyschologistCount += 1
      if User[keys] == Pyschologist[keys]:
        PyschologistCount += 1
      else:
        break
  if PyschologistCount >= 4:
    potential_jobs.append("Pyschologist")
  
  for keys in User.keys():
    if User["interest"] == Statistician["interest"]:
      if User[keys] == "No Pref":
        StatisticianCount += 1
      if User[keys] == Statistician[keys]:
        StatisticianCount += 1
      else:
        break
  if StatisticianCount >= 4:
    potential_jobs.append("Statistician")
  
  for keys in User.keys():
    if User["interest"] == Teacher["interest"]:
      if User[keys] == "No Pref":
        TeacherCount += 1
      if User[keys] == Teacher[keys]:
        TeacherCount += 1
    else:
      break
  if TeacherCount >= 4:
    potential_jobs.append("Teacher")
  
  for keys in User.keys():
    if User["interest"] == Doctor["interest"]:
      if User[keys] == "No Pref":
        DoctorCount += 1
      if User[keys] == Doctor[keys]:
        DoctorCount += 1
    else:
      break
  if DoctorCount >= 4:
    potential_jobs.append("Doctor")
  
  for keys in User.keys():
    if User["interest"] == Data_Scientist["interest"]:
      if User[keys] == "No Pref":
        Data_ScientistCount += 1
      if User[keys] == Data_Scientist[keys]:
        Data_ScientistCount += 1
    else:
      break
  if Data_ScientistCount >= 4:
    potential_jobs.append("Data Scientist")
  
  for keys in User.keys():
    if User["interest"] == Marketing_Manager["interest"]:
      if User[keys] == "No Pref":
        Marketing_ManagerCount += 1
      if User[keys] == Marketing_Manager[keys]:
        Marketing_ManagerCount += 1
    else:
      break
  if Marketing_ManagerCount >= 4:
    potential_jobs.append("Marketing Manager")
  
  for keys in User.keys():
    if User["interest"] == Engineer["interest"]:
      if User[keys] == "No Pref":
        EngineerCount += 1
      if User[keys] == Engineer[keys]:
        EngineerCount += 1
    else:
      break
  if EngineerCount >= 4:
    potential_jobs.append("Engineer")
  
  for keys in User.keys():
    if User["interest"] == Computer_Systems_Analyst["interest"]:
      if User[keys] == "No Pref":
        Computer_Systems_AnalystCount += 1
      if User[keys] == Computer_Systems_Analyst[keys]:
        Computer_Systems_AnalystCount += 1
    else:
      break
  if Computer_Systems_AnalystCount >= 4:
    potential_jobs.append("Computer Systems Analyst")
  
  for keys in User.keys():
    if User["interest"] == Entrepreneur["interest"]:
      if User[keys] == "No Pref":
        EntrepreneurCount += 1
      if User[keys] == Entrepreneur[keys]:
        EntrepreneurCount += 1
    else:
      break
  if EntrepreneurCount >= 4:
    potential_jobs.append("Entrepreneur")
  
  for keys in User.keys():
    if User["interest"] == Accountant["interest"]:
      if User[keys] == "No Pref":
        AccountantCount += 1
      if User[keys] == Accountant[keys]:
        AccountantCount += 1
    else:
      break
  if AccountantCount >= 4:
    potential_jobs.append("Accountant")
  
  print(potential_jobs)

def run():
  window.destroy()
  subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

def bye():
  window.destroy()

def submit():
  calc()
  for widgets in window.winfo_children():
    widgets.destroy()
  name = tk.Label(window, text="Career Nominator", font=("Centaur", 20), bg="#000220", fg="yellow")
  name.place(x=155, y=5)
  leave = tk.Button(window, text="QUIT", fg="black", bg="red", font=("Centaur", 12, "bold"), border=True, borderwidth=4, command=bye)
  leave.place(x=220, y=930)
  again = tk.Button(window, text="AGAIN", fg="black", bg="#ADD8E6", font=("Centaur", 12, "bold"), border=True, borderwidth=8, command=run)
  again.place(x=213, y=870)
  title = tk.Label(window, text="Your Results:", font=("Centaur", 20), bg="#000220", fg="yellow")
  title.pack(pady=100)
  for x in range(0, len(potential_jobs)):
    results = tk.Label(window, text=potential_jobs[x], font=("Centaur", 20), bg="#000220", fg="yellow").pack()


name = tk.Label(window, text="Career Nominator", font=("Centaur", 20), bg="#000220", fg="yellow").pack(expand=True)
title = tk.Label(window, text="Pick One Option From Each Category!", font=("Centaur", 15), bg="#000220", fg="yellow").pack(expand=True)
title = tk.Label(window, text="Interest (Pick ONE)", font=("Centaur", 12),bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="Tech", command=Tech, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Medical", command=Medical, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Math", command=Math, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Science", command=Science, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Law", command=Law, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Business", command=Business, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Teaching", command=Teaching, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
title = tk.Label(window, text="Salary (Pick ONE)", font=("Centaur", 12), bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="High Pay", command=High, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Decent Pay", command=Decent, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="No Prefrence", command=NoPrefSal, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
title = tk.Label(window, text="Location (Pick ONE)", font=("Centaur", 12), bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="Office", command=Office, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Work From Home", command=WFH, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Both", command=BothLoc, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="No Prefrence", command=NoPrefLoc, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
title = tk.Label(window, text="Hours (Pick ONE)", font=("Centaur", 12), bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="Long Hours", command=Long, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Average Hours", command=Average, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Short Hours", command=Short, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="No Prefrence", command=NoPrefHours, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
title = tk.Label(window, text="Work-Life Balance (Pick ONE)", font=("Centaur", 12), bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="Good Balance", command=GoodBal, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Minimal Balance", command=MinBal, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="No Prefrence", command=NoPrefBal, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
title = tk.Label(window, text="Flexibility (Pick ONE)", font=("Centaur", 12), bg="#000220", fg="yellow").pack(expand=True)
button =  tk.Checkbutton(window,text="Good Amount of Flexibility", command=GoodFlex, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="Minimal Amount of Flexibility", command=MinFlex, bg="#000220", fg="yellow", selectcolor="black").pack(expand=True)
button =  tk.Checkbutton(window,text="No Prefrence", command=NoPrefFlex, bg="#000220", selectcolor="black", fg="yellow").pack(expand=True)
title = tk.Label(window, text="", font=("Centaur", 6), bg="#000220").pack(expand=True)
submit = tk.Button(window, text="SUBMIT", fg="black", bg="green", font=("Centaur", 12), border=True, borderwidth=8, command=submit).pack(expand=True)
quit = tk.Button(window, text="QUIT", fg="black", bg="red", font=("Centaur", 12, "bold"), border=True, borderwidth=4, command=quit).pack(expand=True, pady=10)
space = tk.Label(window, text="", font=("Centaur", 12, "bold"), bg="#000220").pack(expand=True)

window.mainloop()
