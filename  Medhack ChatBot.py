import matplotlib.pyplot as plt
from matplotlib import style
name = input(str("Enter patient name: "))
while True:
    gender = (input(str("Enter patient gender (Male, Female): "))).capitalize()
    if gender=='Male'or gender=='Female':
        break
    else:
        print("Sorry, please choose male or female!")
while True:
    age = int(input("Enter patient age: "))
    if age > 18:
        break
    else:
        print("Sorry, please enter adult age!")
SystolicBP = int(input("Enter your systolic blood pressure: "))
DiastolicBP = int(input("Enter your diastolic blood pressure: "))
HeartRate = int(input("Enter your heart rate: "))
OxygenLevel = int(input("Enter your oxygen level: "))
BMI = int(input("Enter your weight in KG: "))
BMI2 = float(input("Enter your height in M: "))
# Sample data
BMI3 = round(BMI/(BMI2*BMI2), 2)
# Create the bar graph
values = [SystolicBP, DiastolicBP, HeartRate, OxygenLevel, BMI3]
# Add labels and titles
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Medical Values for Patient' + " " + name)
while True:
    if SystolicBP<120:
        barplot=plt.bar(x='SystolicBP (mmHg)', height=SystolicBP, fc="Green", ec="black")
        break
    else: 
        if SystolicBP >= 120 and SystolicBP <= 129:
            barplot = plt.bar(x= 'Systolic BP (mmHg)', height = SystolicBP, fc="yellow", ec = 'black')
            break
        else:
            if SystolicBP >= 130 and SystolicBP <= 139:
                barplot = plt.bar(x= 'Systolic BP (mmHg)', height = SystolicBP, fc="Orange", ec = 'black')
                break
            else:
                if SystolicBP >= 140:
                    barplot = plt.bar(x= 'Systolic BP (mmHg)', height = SystolicBP, fc="Red", ec = 'black')
                    break
    values = SystolicBP
    plt.bar_label(barplot,labels=values,label_type="center")
while True:
    if DiastolicBP < 80:
        barplot = plt.bar(x= 'Diastolic BP (mmHg)', height = DiastolicBP, fc="Green", ec = 'black')
        break
    else:
        if DiastolicBP >=80 and DiastolicBP<=89:
            barplot = plt.bar(x= 'Diastolic BP (mmHg)', height = DiastolicBP, fc="yellow", ec = 'black')
            break
        else:
            if DiastolicBP >= 90:
                barplot = plt.bar(x= 'Diastolic BP (mmHg)', height = DiastolicBP, fc="Red", ec = 'black')
                break
    values = DiastolicBP
    plt.bar_label(barplot,labels=values,label_type="center")
while True:  
    if gender == 'Male' or 'male':
        if HeartRate <= 50 or HeartRate >= 100: 
            barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Red", ec = 'black')
            break
        else:
            if HeartRate >= 50 and HeartRate <=60 or HeartRate <100 and HeartRate >=83:
                barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Yellow", ec = 'black')
                break
            else:
                if HeartRate >60 and HeartRate<83: 
                    barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Green", ec = 'black')
                    break
    values = HeartRate
    plt.bar_label(barplot,labels=values,label_type="center")
while True:
    if gender == 'Female' or 'female':
        if HeartRate <= 60 or HeartRate >= 100: 
            barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Red", ec = 'black')
            break
        else:
            if HeartRate >= 60 and HeartRate <=66 or HeartRate <100 and HeartRate >=83:
                barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Yellow", ec = 'black')
                break
            else:
                if HeartRate >66 and HeartRate<83: 
                    barplot = plt.bar(x= 'Heart Rate (bpm)', height = HeartRate, fc="Green", ec = 'black')
                    break
    values = HeartRate
    plt.bar_label(barplot,labels=values,label_type="center")
while True:
    if OxygenLevel >=98 and OxygenLevel<=100:
        barplot = plt.bar(x= 'Oxygen Level (%)', height = OxygenLevel, fc="Green", ec = 'black')
        break
    else:
        if OxygenLevel >=95 and OxygenLevel <98:
            barplot = plt.bar(x= 'Oxygen Level (%)', height = OxygenLevel, fc="Yellow", ec = 'black')
            break
        else:
            if OxygenLevel >=90 and OxygenLevel <95:
                barplot = plt.bar(x= 'Oxygen Level (%)', height = OxygenLevel, fc="Orange", ec = 'black')
                break  
            else:    
                if OxygenLevel < 90:
                    barplot = plt.bar(x= 'Oxygen Level (%)', height = OxygenLevel, fc="Red", ec = 'black')
                    break
    values = SystolicBP
    plt.bar_label(barplot,labels=values,label_type="center")
while True:
    if BMI3 <18.5 or BMI3>30:
        barplot = plt.bar(x= 'BMI', height = BMI3, fc="Red", ec = 'black')
        break
    else:
        if BMI3 >=18.5 and BMI3 <25:
            barplot = plt.bar(x= 'BMI', height = BMI3, fc="Green", ec = 'black')
            break
        else:
            if BMI3 >=25 and BMI3 <=30:
                barplot = plt.bar(x= 'BMI', height = BMI3, fc="Orange", ec = 'black')
    values = SystolicBP
    plt.bar_label(barplot,labels=values,label_type="center")
plt.show()



