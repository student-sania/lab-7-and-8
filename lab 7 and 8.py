# lab 7
# task 1
student_marks = {}
for i in range(1):
    name = input("Enter student's name: ")
    marks = int(input("Enter obtained marks for {}: ".format(name)))
    student_marks[name] = marks
print("Student marks:", student_marks)
print(student_marks)

# task 2
student_dict = {}
def check_duplicate_key(name):
    if name in student_dict:
        print("Warning: Student '{}' already exists in the dictionary.".format(name))
        return True
    return False
for i in range(2):
    name = input("Enter student's name: ")
    marks = int(input("Enter obtained marks for {}: ".format(name)))
     
    while check_duplicate_key(name):
        name = input("Enter a different student's name: ")
        marks = int(input("Enter obtained marks for {}: ".format(name)))
  
    student_dict[name] = marks
print("Student dictionary:", student_dict)

# task 3
student_dict = {}
student_id_counter = 1  
def generate_student_id():
    global student_id_counter
    student_id = student_id_counter
    student_id_counter += 1
    return student_id
    
for i in range(2):
    name = input("Enter student's name: ")
    
    student_id = generate_student_id()
    marks = int(input("Enter obtained marks for {}: ".format(name)))
    student_dict[student_id] = {'name': name, 'marks': marks}

print("Student dictionary:", student_dict)

# task 4
Item_dict={"item_1":45.50,"item_2":35,"item_3":41.30,"item_4":55,"item_5":64}
max_value=0
for value in Item_dict.values():
    if value >max_value:
        max_value=value
print(max_value,"is max_value")
min_value=56
for value in Item_dict.values():
    if value<min_value:
        min_value=value
print(min_value,"is min_value")

# task 6 
dict={"sania":123,"minahil":456,"areeba":789,"farah":999,"tehreem":888}
print("Enter user name and password")
user_name=input()
password=input()

if user_name in dict.keys():
    dict[user_name]==password
    print("welcome")
else:
    print("sorry user does not exit")
    
# task 7
alphabet_frequency = {}
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
for char in sentence:
    if char.isalpha():
        alphabet_frequency[char] = alphabet_frequency.get(char, 0) + 1

for alphabet, frequency in alphabet_frequency.items():
    print(alphabet, ":", frequency)

# lab 8
# task 1
string= input("Enter a string:")
print(len(string))

# task 2
num1= int(input("Enter a number:"))
num2= int(input("Enter a number:"))
num3= int(input("Enter a number:"))
max_number= max(num1,num2,num3)
print(max_number)
min_number=min(num1,num2,num3)
print(min_number)

# task 3
list1=[4,5,6,3,2,1]
sum=0
for i in list1:
    sum = sum+i
print(sum)

# task 4
l1=[3,6,8,5,4,7]
print(sorted(l1))

# task 5
number= int(input("Enter a number:"))
absolute_value= abs(number)
print(absolute_value)

# task 6
user_input= input("Enter a value:")
data_type= type(user_input)
print(data_type)

# task 7
from datetime import datetime
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")

print("Current date in YYYY-MM-DD format:", formatted_date)    