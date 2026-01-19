import mysql.connector
from rich import print as printc
from rich.console import Console
def dbconfig():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user='pm',
            passwd='password'
        )
    except Exception as e:
        Console.print_exception(show_local=True)
    
    return db