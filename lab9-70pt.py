############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer


print "Give me a celcius temperature"
Celcius = int(raw_input())
fahrenheit = Celcius * 9.0/5.0+32
print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "the fahrenheit is " +str(fahrenheit)
print "~~~~~~~~~~~~~~~~~~~~~~~~~~"