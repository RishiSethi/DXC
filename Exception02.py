try:
    file1 = open("studentMarks.txt", "r")
except:
    print("File doesn't exist in the directory")
else:
    print("File opened successfully")
finally:
    print("This block will execute all the time")