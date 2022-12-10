fullname = input("Enter your fullname:\n") # Awonke@Mnotoza

# Option 1
names = fullname.split("@")
print(names)
first_name = names[0]
last_name = names[1]
print("Name: " + first_name + " " + last_name)

# Option 2
index_of_character = fullname.find("@")
first_name_2 = fullname[ : index_of_character]
last_name_2 = fullname[index_of_character + 1 : ]
print("Name: " + first_name_2 + " " + last_name_2)