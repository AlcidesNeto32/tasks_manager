from datetime import datetime

class Task:

    def __init__(self,id = None,name=None,description=None,priority=None,created_at = None,is_done=False):
        self.__task_id = id
        self.__task_name = name
        self.__task_description = description
        self.__task_priority = priority
        self.__created_at = created_at
        self.__task_is_done = is_done
    
    @property
    def task_name(self):
        return self.__task_name
        
    @task_name.setter
    def set_task_name(self,new_name):
        self.__task_name = new_name
    
    @property
    def task_description(self):
        return self.__task_description

    @task_description.setter
    def set_task_description(self,new_description):
        self.__task_description = new_description
    
    @property
    def task_priority(self):
        return self.__task_priority
    
    @task_priority.setter
    def set_task_priority(self,new_priority):
        self.__task_priority = new_priority
    
    @property
    def task_id(self):
        return self.__task_id
    
    @task_id.setter
    def set_task_id(self,new_id):
        self.__task_id = new_id 
    
    @property
    def task_is_done(self):
        return self.__task_is_done
    
    @task_is_done.setter
    def set_task_is_done(self,done:bool):
        self.__task_is_done = done

    @property
    def created_at(self):
        return self.__created_at
    
    @created_at.setter
    def set_created_at(self,date):
        self.__created_at = date
        
    def __str__(self):
        return f"""
TASK ID: {self.__task_id}
NAME: {self.__task_name}
DESCRIPTION: {self.__task_description}
PRIORITY: {self.__task_priority}
IS DONE: {self.__task_is_done}
CREATED AT: {self.__created_at}"""