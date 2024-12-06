# Import library of functions
import file_control

def main():
  # Get tasks from file.py
  tasks = file_control.load_tasks()
  
  

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_tasks(tasks)
    elif choice == "3":
      complete(tasks)
    elif choice == "4":
      file_control.save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of taks and
# displays every task in the list.

#Display Task
def display_tasks(tasks):
  #display tasks on the list with their details
  for r in range(len(tasks)):
    for c in range(len(tasks[r])):
      if c == 0:
        print(f"{r+1}. {tasks[r][c]}", end="\t")
      elif c == len(tasks[r]) - 1:
        print(tasks[r][c])
      else:
        print(f"{tasks[r][c]}", end="\t")
    
    

def add_tasks(tasks):
  #Ask for the information about the task
  Title = input("What task would you like to add your to-do list? ")
  Description = input("Please add the description: ")
  Date = input("Please add the to-do date: ")
  Complete = "False"
  New_task = [Title, Description, Date, Complete]
  #Add new task to the list by appending
  tasks.append(New_task)
  # return updated list
  return tasks

#Function that marks the tasks as complete
#Takes Tasks and returns updated tasks
def complete(tasks):
  
  #display tasks
  display_tasks(tasks)

  #prompt for marking complete
  choice = input("which task would you like to mark complete? ")
  #change the status of the task in the list
  found = False
  for i in range(len(tasks)):
    if tasks[i][0] == choice:
      tasks[i][3] = "True"
      found = True

  if not found:
    print("The task was not found. ")

#return updated list
  return tasks




if __name__ == "__main__":
  main()
