import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper","expense_tracking_system.log")

@contextmanager
def get_db_cursor(commit = False):

    connection = mysql.connector.connect(
        host = "localhost" , 
        user = "root" ,
        password = "root" ,
        database = "expense_manager"
    )

    cursor = connection.cursor(dictionary = True)

    yield cursor 
    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):

    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s" , (expense_date,) )
        expenses = cursor.fetchall()

        return expenses


def fetch_expense_summary(start_date , end_date):

    logger.info(f"fetch_expense_summary called with {start_date} and {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT category , SUM(Amount) AS Total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category" , (start_date , end_date))
        summary = cursor.fetchall()

        return summary

def fetch_monthly_summary():

    logger.info(f"fetch_monthly_summary called")
    with get_db_cursor() as cursor:
        cursor.execute("select monthname(expense_date) as month , sum(amount) as total from expenses group by monthname(expense_date)")
        monthly_expenses = cursor.fetchall()

        return monthly_expenses    


def insert_expense(expense_date , amount , category , notes):

    logger.info(f"insert_expense called with date : {expense_date} , amount : {amount} , category : {category} , notes : {notes}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date , amount , category , notes) VALUES (%s, %s, %s, %s)" , 
                       (expense_date , amount , category , notes))    


def delete_expenses_for_date(expense_date):

    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s" , (expense_date,) )



if __name__ == "__main__":

    '''
    print("Insert a record")
    insert_expense("2026-10-27",100,"Food","Birthday Dinner")
    expenses = fetch_expenses_for_date("2026-10-27")
    print(expenses)
    print("Delete a record")
    delete_expenses_for_date("2026-10-27")
    expenses = fetch_expenses_for_date("2024-08-01")
    print(expenses)
    '''
    
 
