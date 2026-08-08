import sqlite3 as sql
from termcolor import colored

class DataBase:
    def __init__(self):
        pass
    
    def connection():
        return sql.connect("project.db")
    def close_connection(con = None):
        if con:
            con.close()
            print(colored("This connection was closed!!","green"))
        else:
            print(colored("Can't close this connection!!","red"))