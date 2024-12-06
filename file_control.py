# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.
def load_tasks():
    #Open the file
    tasks = []
    try: 
        with open("List.txt", "r") as f:
    #Read the file
            line = f.readline()
            while line != "":
                #Remove the new line character after each line in list
                title = line.rstrip("\n")
                description = f.readline().rstrip("\n")
                date = f.readline().rstrip("\n")
                status = f.readline().rstrip("\n")
                new_task = [title, description, date, status]
                tasks.append(new_task)
                line = f.readline()
    #return list of tasks
    except FileNotFoundError: 
        return tasks
    return tasks

        
    



# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.
def save_tasks(tasks):
    #Open file with append
    with open("List.txt", "w") as f:
        #Write the tasks to the list
        for task in tasks:
            for info in task:
                f.write(info + '\n')
        

            
            
        print("File Saved")


    
        
        
    


