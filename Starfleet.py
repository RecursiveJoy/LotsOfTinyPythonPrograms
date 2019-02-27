print("Welcome to the Starfleet Academy Online Application.")
Name = input("Enter your first name:")
Age = int(input ("How old are you?"))
GPA = float(input ("What is your GPA?"))
SAT = int(input("What is your SAT score?"))
Race = input("What species are you?")

goodRace = False
goodGPA = False
goodSAT = False
goodAge = False
eligibility = False
output = True



if GPA >= 2.0 and GPA <= 4.0:
    goodGPA = True

if Age >= 17:
    goodAge = True

if SAT >= 800 and SAT <= 1600:
    goodSAT = True




if Race == "Human" or Race =="Vulcan" or Race == "Klingon":
    goodRace = True

if Race == "Vulcan" and Age == 16:
    goodAge = True




if SAT >= 1500:
    goodSAT = True
    goodAge = True
    goodGPA = True

if SAT >= 1100 or GPA >= 3.5:
    goodSAT = True
    goodGPA = True



if GPA > 4.0 or SAT > 1600:
    output = False
if Race != "Human" and Race != "Klingon" and Race != "Vulcan" and Race != "Romulan":
    output = False



if goodGPA and goodSAT and goodRace and goodAge: 
    eligibility = True


if output == False:
    print("You provided invalid data. Try again.")
    eligibility = False

print("Applicant name:", Name)
print("Age:", Age)
print("GPA:", GPA)
print("SAT score:", SAT)
print("Race:", Race)


if eligibility:
    print("You are eligible to apply for Starfleet.")
else:
    print("You are not currently eligible to apply for Starfleet.")
    if goodRace == False:
        print("We are only accepting applications from Humans, Vulcans, and Klingons.")
    if goodSAT == False or goodGPA == False:
        print("You do not meet our academic requirements.")
    if goodAge == False:
        print("You do not meet our age requirements at this time.")
