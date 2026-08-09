from repository.task_repository import TaskRepository
from termcolor import colored
from model.entity.task import Task

repository = TaskRepository()
class TaskService:  
    
    def row_to_task(self,sql=None,sql_list:list = None):
        if sql:
            for info in sql:
                return Task(
                    id = info[0],
                    name = info[1],
                    description = info[2],
                    priority = info[3],
                    created_at = info[4],
                    is_done = info[5] == 1 # if one, it mean the task is done
                )
        else:
            task_list = []
            for info in sql_list:
                task_list.append(
                    Task(
                        id = info[0],
                        name = info[1],
                        description = info[2],
                        priority = info[3],
                        created_at = info[4],
                        is_done = info[5] == 1
                    )
                )
            return task_list
                
    def update_task(self,task:Task):
        try:
            repository.update(task=task)
            return colored("Task updated!","green")
        except:
            return colored("Ops! A error happend!","red")
        
    def show_all_tasks(self):
        return self.row_to_task(sql_list= repository.show_all())
    
    def search_task_by_id(self,id:int):
        return self.row_to_task(sql=repository.search_by_id(id))
    
    def save_task(self,task:Task):
        repository.save(task=task)
        return colored("Task saved!","green")
    
    def delete_task(self,id:int):
        if self.search_task_by_id(id):
            repository.delete(id)
            return colored("Task deleted!","green")
        else:
            return colored("Task does not exist!","red")
    
    def update_status_task(self,id:int):
        task = self.search_task_by_id(id)
        task.set_task_is_done = True
        self.update_task(task)
        return colored("Status updated!","green")