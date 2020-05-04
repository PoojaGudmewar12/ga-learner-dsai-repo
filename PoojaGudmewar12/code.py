# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class= class_1 + class_2
print('View the newly created register: \n',new_class)

# Append the list
new_class.append('Peter Warden')
# Print updated list
print('\nUpdated Register is: \n',new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print('Register after removeing unwanted name: \n',new_class)

# Step 2: Geoffrey Hinton Report

# Create the Dictionary
courses={'Math':65, 'English':70, 'Hstory':80,'French':70,'Science':60}
print('Marks obtained in each subject are:\n',courses)

# Slice the dict and stores  the all subjects marks in variable
all_marks=courses.values()
print('List of all marks: ',all_marks)
# Store the all the subject in one variable `Total`
total=sum(all_marks)
# Print the total
print('Total marks obtained by Geoffrey Hinton= ',total)
# Insert percentage formula
percentage=total*100/500
# Print the percentage
print('Percengae scored by Geoffrey Hinton= ',percentage)

# Step 3: Highest marks in subject mathematics

# Create the Dictionary
mathematics={'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
#Method 1:
topper=max(mathematics,key=mathematics.get)
print('Student who scored maximun in maths is: ',topper)

#Step 4: Print last name and first name on certificate

# Given string
# Create variable first_name 
spilt_list=topper.split()  # here you have limited ypur split to 2 elements
print('List after splitting: ',spilt_list)
first_name=spilt_list[0]
print('First Name is : ',first_name)
# Create variable Last_name and store last two element in the list
last_name=spilt_list[1]
print('Last Name is: ',last_name)
# Concatenate the string
full_name =last_name +' '+ first_name
# print the full_name
print('Full Name of topper is: ',full_name)
# print the name in upper case
certificate_name=full_name.upper()
print('Name on certificate will be: ',certificate_name)

# Code ends here


