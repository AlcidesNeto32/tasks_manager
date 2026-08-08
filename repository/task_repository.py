from data_base.db_config import DataBase
from model.entity.task import Task
import sqlite3 as sql
from termcolor import colored
class TaskRepository:
    
    def save(self,task:Task):
        con = DataBase.connection()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO task('name','description','priority') VALUES (?,?,?)", [task.task_name,task.task_description,task.task_priority])
            con.commit()
        except sql.DataError as e:
            return colored("Ops! Values are wrong","red")
        finally:
            cur.close()
            DataBase.close_connection(con)

    def delete(self,id:int):
        with DataBase.connection() as con:
            con.cursor().execute("DELETE FROM task WHERE id = ?",(id,))
            con.commit()


    def show_all(self):
        with DataBase.connection() as con:
            tasks = con.cursor().execute("SELECT * FROM task").fetchall()
            return tasks
              
    def update(self,task:Task):
        with DataBase.connection() as con:
            con.cursor().execute("UPDATE task SET name = ?, description = ?, priority = ?, is_done = ?  WHERE id = ?",(task.task_name, task.task_description,task.task_priority,task.task_is_done,task.task_id))
            con.commit()
        
    def search_by_id(self,id:int):
        with DataBase.connection() as con:
            task = con.cursor().execute("SELECT * FROM task WHERE id = ?",(id,))
            return task