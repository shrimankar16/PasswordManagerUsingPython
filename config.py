from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console
import sys
console = Console()
def config():
    db = dbconfig()
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An Error occured while trying to create a database")
        console.print_exception(show_locals=True)
        sys.exit(0)