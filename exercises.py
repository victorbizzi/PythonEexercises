#test git








##############################################################################################################
#Replace character
filenames = ["1.PlayStation5.txt", "2.GTASanAndreas.docx", "3.WorkoutSeptemberToNovember.pdf" ]
for filename in filenames:
    #filename = filename.replace(".","-") #using this, it will modify the doc type. Ie.: file.pdf -> file-pdf
    filename = filename.replace(".","-",1) #using this, it will replace just the first
    print(filename)
"""
##############################################################################################################
#Add new feature to allows the user edit

todos = []
while True:
    user_action = input("Type add, show or edit: ")
    user_action = user_action.strip() #strip is used to remove blank spaces, so, if the user types "add ", the code will remove the blank space to become just "add"
    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("Number of the ToDo to edit: "))
            number = number -1
            new_todo = input("Enter the new ToDo: ")
            todos[number] = new_todo
        case "exit":
            break
print("Bye!")




##############################################################################################################
#Show all itens inside an array

meals = ["pasta", "pizza", "barbecue"]

for char in meals:
    print(char.capitalize())

##############################################################################################################
#Example inserting one letter per line

meals = ["pasta", "pizza", "salad"]

for meal in "meals":
    print(meal.capitalize())


##############################################################################################################
#Improved with Match and Case


todos = []
while True:
    user_action = input("Type add or show: ")
    user_action = user_action.strip() #strip is used to remove blank spaces, so, if the user types "add ", the code will remove the blank space to become just "add"
    match user_action:
        case "add":
            todo = input("Enter a to do: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
print("Bye!")

##############################################################################################################
#While to validate a password.

password = input("Enter the password: ")
pw = "a123!"
while password != pw:
    password = input("Enter the password: ")

print("Correct password!")


##############################################################################################################
#Improving the To Do Loop


user_prompt = "Enter a To Do: "
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo.title()) #to make each first letter being big. iE: "Hello, My Name Is Victor"
    print(todos)

##############################################################################################################
#Making some changes to add the item inside the array


user_prompt = "Enter a To Do: "
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize()) #to make the first letter being big
    print(todos)


##############################################################################################################
#The print is adding the previous Input inside the list
user_prompt = "Enter a To Do: "
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)

##############################################################################################################
#New Structure using While

user_prompt = "Enter a To Do: "
while True:
   todo = input(user_prompt)
   todos = [todo]
   print(todos)

##############################################################################################################
#Simple While structure. It prints numbers from X to Y
x = 1
while x <= 6:
    print(x)
    x = x + 1


##############################################################################################################
#Simple way to write a loop without complexibility

user_prompt = "Enter a To Do: "
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]

print(todos)
print(type(todos))

##############################################################################################################
#The following code counts how many characters (including blank spaces) the thext has.

text = input("Enter a title: ")

leng = len(text)
print("The title has", leng, "characters including blank spaces")
"""