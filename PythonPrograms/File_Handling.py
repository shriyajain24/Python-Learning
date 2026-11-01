# Write :
file = open("myfile.txt", "w")

data = input("Enter data to write in file: ")
file.write(data)

file.close()

print("Data written successfully")


# Read :
file = open("myfile.txt", "r")

print("File Data:", file.read())

file.close()
