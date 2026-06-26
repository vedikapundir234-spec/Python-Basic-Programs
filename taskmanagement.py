
#--------TASK MANAGEMENT APP-------#

def task():
    tasks=[]   #empty list 
    print("***WELCOME TO TASK MANAGEMENT APP***")

    total_task=int(input("Enter the total number of tasks:"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}:")
        tasks.append(task_name)            #adds tasks to the empty list

    print(f"Today's taskss are:\n{tasks}")

    while True:
        operation=int(input("Enter 1,2,3,4,or 5:\n1.Add\n2.Update\n3.Delete\n4.View\n5.Stop\n\n"))

        if operation==1:
            add=input("Enter task you want to add:")
            tasks.append(add)
            print(f"Task {add} has been successfully added..")
        elif operation==2:
            update=input("Enter the task you want to update:")
            if update in tasks:
                up=input("Enter new task:")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"Updated task:{up}")
            else:
                print("task not found")
        elif operation==3:
            delete=input("Enter the task you want to delete:")
            if delete in tasks:
                ind=tasks.index(delete)
                del tasks[ind]
                print(f"Task {delete} has been deleted..")
        elif operation==4:
            print(f"Total tasks are:{tasks}")
        elif operation==5:
            print("**Closing the program..**\n\nTHANKYOU")
            break
        else:
            print("INVALID OPERATION!")

task() 


