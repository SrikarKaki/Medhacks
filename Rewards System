import math

#This is a condition that tests whether it should switch illnesses.
condition = True
#This is the points system that keeps track of their points.
point_system = 0
#This is the date that's kept track of, and the user can only cash in points when a week has passed.
day = 1
#This is the user's "bank balance".
bank_balance = 0
#This is the user's streak that shows how long they have met the goals.
streak_day = 0
#These are our available disease/illness options.
illness_book = ["Diabetes", "Arthritis", "Cancer", "Heart Disease", "Depression", "Asthma", "Alzheimer's", "Obesity", "High blood pressure", "High cholesterol", "Low blood pressure", "Back problems"]
#This is a dictionary of solutions and goals of the disease that they have.
solutions_book = {"Diabetes": ["Each day, make sure to exercise at least one hour, especially cardiovascular exercises, like running. This ensure weight loss, which is crucial for healthy living and controlling diabetes.", "Every day, eat a balanced diet, which includes plenty of fruits and vegetables, and make sure to avoid unhealthy foods like junk and sweets. This will help you lose weight and combat diabetes.", "Make sure to get at least 8 hours of quality sleep each night. This will help control multiple hormones that are essential to combat diabetes", "Try to drink at least 2 to 3 liters of water each day. Your blood sugar will then be stable, and organs will not be damaged.", "Remember to always take your medication each day to help you control your blood sugar levels. This will alleviate the effects of diabetes."], "Arthritis": ["Since your joints are hurting already, it's important to do light exercises to stimulate them and not hurt them. So, try to walk outside every day for at least an hour.", "Make sure to stretch at least an hour each day. This will lubricate your joints and increase your range of motion.", "Aim for at least 8 hours of good sleep each night. This will get you the necessary rest for dealing with arthritis.", "Try to eat a lot of fruits and vegetables every day (around 80 grams). Eating them will provide your body with antioxidants and anti-inflammatory agents that help with arthritis.", "Do not forget to take your recommened medication every day. This will help you manage the pains of arthritis."], "Cancer": ["Make sure to exercise at least an hour each day. This will help you lose weight and control your cancer cells.", "Always remember to eat a lot of fruits and vegetalbes every day (around 80 grams). This will provide a lot of nutrients and antioxidants, which helps to prevent and control cancer", "If you want your condition to improve, then make sure to not drink alcohol. This will help avoid the progression of cancer.", "When it is sunny outside, make sure to stay inside to avoid developing certain skin cancers. You can go out after the sun is not shining as hard, and don't forget to use sunscreen.", "Aim for at least 8 hours of sleep because during sleep, your body produces hormones that help control and combat cancer."], "Heart disease": ["Every day, aim for at least an hour of exercise because that will result in lower blood pressure and help you lose weight, leading to less severe heart problems", "Do not smoke. No smoking leads to stable blood pressures, heart rates, and oxygen can get around more easily.", "Always strive to eat heart-healthy and avoid junk food, including a lot of fruits, vegetables, and whole grains. This reduces cholesterol levels, making your heart healthier.", "Always try to get at least eight hours of sleep per day. This will regulate your blood pressure, weight, and heart rate.", "Make sure to spend at least 30 minutes each day relaxing and stress relieving. This ensures no damage to the heart." ], "Depression": ["Never forget to sleep at least 8 hours each night. This will make you more energized and help you have a more optimisitc view on life.", "Social aspects of life is extremely crucial in fighting depression, so make sure to spend some time talking to friends, family, or strangers.", "Spend at least an hour outside doing some form of exercise, especially in nature since the natural views will calm you down and make you happier.", "If you are free during the day or have free time, then find some fun activities to do, such as gaming, reading, sports, or others. This will make you 'productive' and make you happier.", "Relaxation is crucial in combating depression, so try to spend at least 30 minutes in meditation or just chilling."], "Alzheimer's": ["Do not forget to take your medicine every day. This will help you deal with memory loss.", "Spend at least an hour each day reading. Reading exercises your brain, thus slowing the progression of Alzheimer's.", "Never forget to call up your friends or family each day because that will help you remember more and train your brain.", "Always make sure to sleep at least 8 hours each night. This makes sure your brain gets the necessary rest, thus promoting brain health.", "When given the chances, try to do new things every day. This will stimulate the brain and improve brain health."], "Obesity": ["Every day, limit the amount of food you eat, and make sure you are eating healthy foods instead of junk food. This will help you lose weight.", "Do not forget to exercise at least an hour each day, especially cardiovascular exercises like running and walking. This will ensure losing the most weight.", "Make sure to sleep at least 8 hours of sleep each night in order to elevate leptin levels. This will result in feeling less hungrier.", "Whenever possible, avoid soda. This reduces sugar and calorie intake, leading to less weight gained.", "Every day, spend at least an hour outside doing some form of exercise, whether it's going for a walk or just shopping. This will help you lose weight."], "High blood pressure": ["Spend at least an hour each day exercising. This will strengthen your heart, thus lowering blood pressure.", "When eating every day, make sure that the food is heart-healthy and not junk food. Also include at least 80 grams of fruits and vegetables, which will provide the heart with nutrients and lower blood pressure.", "Every day, spend at least 30 minutes of relaxation, which will lead to less stress. This will cause blood pressure to drop due to calmness.", "Remember to always sleep at least 8 hours each night. This will help the blood pressure to drop and allows the heart to offload some stress", "Never smoke because the nicotine will raise your blood pressure and heart rate, so make sure to stay away from it every day."], "Low blood pressure": ["Drink at least 2-3 liters of water every day. This will help you increase your blood volume and avoid dehyrdation.", "Try not to drink alcohol because it will cause dehyration and lower blood pressure further.", "Every day, make sure to eat less because it will avoid lowering your blood pressure, and make sure to eat healthier because it can provide you with vitamins that boost your blood pressure via healthy blood cells.", "Never forget to take your medications every day. This will help you manage your blood pressure, leading to stableness.", "Aim for at least 8 hours of sleep each night because your heart can rest and pump blood more easily, leading to better blood pressure."], "Asthma": ["Try to exercise at least an hour each day, whether it's heavy or light exercises. This will help you strengthen your lungs and help defeat asthma.", "Make sure to always have an inhaler by your side every day. This will make it easier for you to breathe, thus helping with asthma.", "Every day, you have to avoid smoking because smoking will cause inflammation. Thus. not smoking will result in better lung function.", "Try to sleep at least 8 hours each night. This will help you breathe better and reduce the risk of asthma attacks.", "Always remember to drink at least 2-3 liters of water every day. This will help thin muscus in airways and lungs, making breathing easier."], "High cholesterol": ["Every day, always remember to eat heart-healhty foods and a balanced diet. This will decrease cholesterol in your system.", "Make sure to spend at least an hour each day exercising. This will help raise good cholesterol and flush out the bad ones, leading to a healthier system.", "Do not smoke. Smoking leads to an influx of bad cholesterol in your system, so make sure to avoid it every day.", "Always try to aim for at least 8 hours of sleep each night. This will help regulate hormone levels and stablize the cholesterol levels.", "Strive to drink at least 2-3 liters of water every day. This will help eliminate the bad cholesterol in your system."], "Back problems": ["Every hour, make sure to check on your posture. This will ensure constant reminder to sit up straight and avoid back problems.", "Make sure to sleep at least 8 hours every night. This will help you relax your back and maintain the curvature.", "Every day, try to find an hour of time stretching. This will result in better mobility and strengthening of your back.", "Make sure to exercise at least an hour each day. This will help strengthen your back, increase range of motion, and improve posture.", "Make sure to drink at least 2-3 liters of water every day. This will help to lubricate your joints and cushion the spine."]}

def main():
  global day
  global point_system
  global streak_day
  global bank_balance
  print("Day " + str(day))
  print("Streak: " + str(streak_day) + " days.")
  print("Bank Balance: $" + str(bank_balance))
  print("You have " + str(point_system) + " points.\n")
  edited_book = solutions_book
  condition = 0
  while True:
    type = input("What type of chronic illness do you have? ")
    type2 = type.rstrip(" .")
    type1 = type2.capitalize()
    if type1 in illness_book:
      statement = "\nHere are some goals for you to meet to alleviate " + type1.lower() + ":"
      print(statement)
      break
    else:
      print("\nSorry, we don't have that illness in our database.\nPlease choose an illness from: \nDiabetes\nArthritis\nCancer\nHeart disease\nDepression\nAlzheimer's\nObesity\nHigh blood pressure\nLow blood pressure\nHigh cholesterol\nBack problems\nAsthma\n")
  #This is checking what disease they entered, and it retrieves information based on that disease.
  if type1 == "Diabetes":
    diabetes()
  elif type1 == "Arthritis":
    arthritis()
  elif type1 == "Cancer":
    cancer()
  elif type1 == "Heart disease":
    heart_disease()
  elif type1 == "Depression":
    depression()
  elif type1 == "Alzheimer's":
    alzheimers()
  elif type1 == "Obesity":
    obesity()
  elif type1 == "High blood pressure":
    high_blood_pressure()
  elif type1 == "Low blood pressure":
    low_blood_pressure()
  elif type1 == "Asthma":
    asthma()
  elif type1 == "High cholesterol":
    high_cholesterol()
  elif type1 == "Back problems":
    back_problems()
  #This is reprinting the day, bank balance, and points after the first one has been printed. It also keeps track of all of the scores
  while True:
    if condition == 1:
      print("\nDay " + str(day))
      if streak_day == 1:
        print("Streak: " + str(streak_day) + " day.")
      elif streak_day >= 10:
        print("Streak: " + str(streak_day) + " days 🔥")
      else:
        print("Streak: " + str(streak_day) + " days.")
      print("Bank Balance: $" + str(bank_balance))
      if point_system == 1:
        print("You have " + str(point_system) + " point.")
      else:
        print("You have " + str(point_system) + " points.")
    #This checks to see if the user is inputting valid numbers into the program.
    while True:
      if day % 7 == 0:
        print("\nCongrats, you have reached the end of the week! Your reward points will be automatically converted into real cash the next day.")
        #This sets up a multiplier to the money they earn once their streak exceeds 10.
        if streak_day >= 10:
          Streak_day = math.log(streak_day, 10)
          Streak_Day = round(Streak_day, 2)
          bank_balance = round(bank_balance + point_system * 0.75 * Streak_Day, 2)
          point_system = 0
        else:
          bank_balance = bank_balance + point_system * 0.75
          point_system = 0
      decision = input("\nWhich goal do you want to accomplish? Type the number: ")
      #The try and except statements ensure that the code does not break when a string is inputted.
      try:
        if int(decision) <= 5 and int(decision) >=1:
          condition = True
          break
        elif int(decision) == 6:
          condition = False
          break
      except:
        print("Please insert a valid number.") 
    if condition == False:
      print("")
      condition = True
      main()
    #This is preparing the "int_decision" variable to be able to be used in the "solutions_book" dictionary, which is turned into the "Decision" variable.
    Decision = int(decision) - 1
    Locator = solutions_book[type1]
    #"Answer" variable is the list resulting from the dictionary.
    Answer = Locator[Decision]
    print("\n" + Answer)
    while True:
      Question = input("\nDid you accomplish this goal? (yes/no): ")
      Question.lower()
      Question.rstrip(" .")
      if Question == "yes":
        print("\nGreat job!")
        point_system += 1
        condition = 1
        day += 1
        streak_day += 1
        break
      elif Question == "no":
        print("\nDon't worry, you can always try again!")
        condition = 1
        day += 1
        streak_day = 0
        break

      
#These are the diseases/illnesses functions that have specific information attached to them.
def diabetes():
  goals = ["1. Exercise more", "2. Eat healthier", "3. Get more sleep", "4. Drink more water", "5. Take your medication", "6. Switch Illness"]
  for a in goals:
    print(a)

def arthritis():
  goals = ["1. Light exercises", "2. Stretch", "3. Get more sleep", "4. Eat more fruits and vegetables", "5. Take your medication", "6. Switch Illness"]
  for a in goals:
    print(a)

def cancer():
  goals = ["1. Get more exercise", "2. Eat healthier", "3. No alcohol", "4. Stay away from the sun", "5. Get more sleep", "6. Switch Illness"]
  for a in goals:
    print(a)

def heart_disease():
  goals = ["1. Get more exercise", "2. No smoking", "3. Eat healthier", "4. Get a ton of sleep", "5. Relieve your stress", "6. Switch Illness"]
  for a in goals:
    print(a)

def depression():
  chiu = ["1. Get more sleep", "2. Talk to others", "3. Get more exercise, especially in nature", "4. Do more fun activities", "5. Relax", "6. Switch Illness"]
  for nathan in chiu:
    print(nathan)

def alzheimers():
  shammu = ["1. Take your medication", "2. Read more", "3. Maintain social relations", "4. Sleep more", "5. Try new things", "6. Switch Illness"]
  for srikar in shammu:
    print(srikar)

def obesity():
  will = ["1. Eat less and healthier", "2. Exercise a lot", "3. Get more sleep", "4. Limit soda", "5. Leave the house more often", "6. Switch Illness"]
  for wu in will:
    print(wu)

def high_blood_pressure():
  aaron = ["1. Exercise more", "2. Eat healthier", "3. Reduce stress", "4. Sleep more", "5. Do not smoke", "6. Switch Illness"]
  for chen in aaron:
    print(chen)

def low_blood_pressure():
  jones = ["1. Drink more water", "2. Avoid alcohol", "3. Eat less and healthier", "4. Consume your medications", "5. Sleep more", "6. Switch Illness"]
  for bob in jones:
    print(bob)
    
def asthma():
  hacks = ["1. Get more exercise", "2. Use inhaler when uncomfortable", "3. Do not smoke", "4. Get sleep", "5. Stay hydrated", "6. Switch Illness"]
  for med in hacks:
    print(med)

def high_cholesterol():
  place = ["1. Eat more heart-healthy foods", "2. Exercise more", "3. No smoking", "4. Sleep more", "5. Drink more water", "6. Switch Illness"]
  for first in place:
    print(first)

def back_problems():
  go = ["1. Have a good posture", "2. Sleep more", "3. Stretch daily", "4. Exercise often", "5. Stay hydrated", "6. Switch Illness"]
  for lets in go:
    print(lets)

main()
