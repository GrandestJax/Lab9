############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
Patients = (23)

while Patients >= 1:
    print"---------------------"
    print "what is your temperature?"
    print"---------------------"
    Temp_thing = int(raw_input())
    if Temp_thing >= 105:
        print"---------------------"    
        print "you need to go see a doctor"
        print"---------------------"    
    print"---------------------"    
    print "have you been sick in the past 24 hours?"
    print"---------------------"    
    Sick = raw_input()
    if Sick == "yes" and Temp_thing >= 102:
        print"---------------------"    
        print "Go to the hospital"
        print"---------------------"   
    print"---------------------"    
    print "have you been to africa in the past time?"
    print"---------------------"    
    Africa_chance = raw_input()
    if Africa_chance == "yes" and Sick == "yes" and Temp_thing >= 100:
        print"---------------------"    
        print "GO TO THE EMERGENCY ROOM"
        print"---------------------"
    Patients = Patients - 1
    print "NEXT!"