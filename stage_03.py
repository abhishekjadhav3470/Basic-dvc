# Import the necessary libraries if required

# Read content from 'artifacts.txt'
with open("artifacts.txt", "r") as f:
    text = f.read()

# Append text to 'artifacts_02.txt'
with open("artifacts_02.txt", "a") as f:
    f.write(text + "\nAdded lines")

print("end of stage 03")
