# Our Task Array To Store All of our tasks
tasks = []

def addtask():
   task = input("Please Enter a Task:-")
   tasks.append(task)
   print(f"Task '{task}' added to the list")

def ListTasks():
   if not tasks:
      print("There are No tasks Currently:-")
   else:
      for index, task in enumerate(tasks):
         print(f"Task # {index}.{task}")
   
def DeleteTask():
   ListTasks()
   try:
       taskToDelete = int(input("The List Number you want to delete:-"))
       if taskToDelete >=0 and taskToDelete < len(tasks):
          tasks.pop(taskToDelete)
          print(f"Task {taskToDelete} Has Been Deleted")     
       else:
          print(f"Task #{taskToDelete} was not found.")
   except:
      print("Invalid input.")
               
if __name__ == "__main__":
    print("Welcome To-Do List **V1** ")
    while True:
        print("\n")
        print("Please Select One Of The Following Options:-")
        print("--------------------------------")
        # giving the users Choices
        print("1. Add a new Task")
        print("2. Delete a Task")
        print("3. list Tasks")
        print("4 Quit")
        
        choice = input("Enter Your Choice:-")
        
        if choice == "1":
            addtask()
        elif choice == "2":
            DeleteTask()
        elif choice == "3":
            ListTasks()
        elif choice == "4":
            break
        else:
            print("Invalid Input Please Try Again Later!")

    # This will happen when the user is done using the Application and decides to Quit 
    print("GoodBye Thank You For Using This Basic Python App \n Made By Mohd Mazin! 😉")
