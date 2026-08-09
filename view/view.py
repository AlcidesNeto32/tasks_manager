from termcolor import colored
from model.service.task_service import TaskService
from model.entity.task import Task
import time 
menu = colored("""
-------------------------
MENU
-------------------------
1.Insert task
2.Show task 
3.Show all tasks
4.Update task info
5.Delete task
6.End task
7.Exit""","blue")

tsk_service = TaskService()
def start():
    while True:
        print(menu)
        try:
            choice = int(input(colored("Choice: ","blue")))
            match(choice):
                case 1:
                    while True:
                        name = input(colored("Task name: ","blue"))
                        description = input(colored("Description: ","blue"))
                        priority = input(colored("Priority: (Maximum,Medium,Minimum)","blue"))
                        print(tsk_service.save_task(Task(name=name,description=description,priority=priority)))
                        go_menu = input(colored("Go to menu? Y/N ","blue"))
                        
                        if go_menu.upper() in ["Y","N"]:
                            if go_menu.upper() == "Y":
                                break
                            else: 
                                continue
                        else: 
                            print(colored("Enter a option valid!","red"))
                case 2:
                    id = input(colored("Enter id: ","yellow"))
                    print(colored(tsk_service.search_task_by_id(id),"yellow"))
                case 3:
                    tasks = tsk_service.show_all_tasks()
                    for task in tasks:
                        print(colored(task,"yellow"))
                        time.sleep(1)
                    time.sleep(1)
                case 4:
                    while True:
                        id = int(input(colored("Enter id: ","blue")))
                        task_update = tsk_service.search_task_by_id(id)
                        is_that_task = input(colored(f"{task_update}\nis that task? Y/N ","yellow"))
                        
                        if is_that_task.upper() == "Y":
                            task_update.set_task_name = input(colored("Task name: ","blue"))
                            task_update.set_task_description = input(colored("Description: ","blue"))
                            task_update.set_task_priority = input(colored("Priority: (Maximum,Medium,Minimum) ","blue"))
                            print(tsk_service.update_task(task_update))
                            time.sleep(1)
                            break
                            
                case 5:
                    id = int(input(colored("Enter id: ","blue")))
                    print(tsk_service.delete_task(id))
                    time.sleep(1)
                    
                case 6:
                    tasks = tsk_service.show_all_tasks()
                    for task in tasks:
                        if task.task_is_done != True:
                            print(colored(f"ID:{task.task_id}\nNAME:{task.task_name}\n","yellow"))
                            time.sleep(1)
                    id = int(input(colored("Enter id: ","blue")))
                    print(tsk_service.update_status_task(id))
                    
                case 7:
                    print(colored("Bye.","blue"))
                    break
                case _:
                    print(colored("Ops! this option does not exists","red"))
        except ValueError:
            print(colored("Ops! Enter only numbers!","red"))
        
