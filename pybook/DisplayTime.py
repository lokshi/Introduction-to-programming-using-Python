# Prompt the user for input
seconds = eval(input("Enter an integer for seconds: "))

# Get minutes and remaining seconds
minutes = seconds // 60     # Find minutes in seconds
remainingSeconds = seconds % 60   # Seconds remaining
print(str(seconds) + " seconds is " + str(minutes) +  
  " minutes and " + str(remainingSeconds) + " seconds")
