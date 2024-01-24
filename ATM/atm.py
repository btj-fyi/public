import sqlite3
import logging
import constants

class ATM:
    def login(self):
        pass
    def logout(self):
        pass
    def balance(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def transfer(self):
        pass
    def wire(self):
        pass
    
class User:
    def __init__(self):
        pass
    def is_user(self):
        pass

class Account:
    def __init__(self):
        pass
    def create_account(self):
        pass
    def delete_account(self):
        pass
    def get_owner(self):
        pass

class DB:
    def __init__(self):
        # on first run, sqlite will create the db if it does not already exist
        con = sqlite3.connect(constants.database_filename)
        self.cur = con.cursor()

    def has_tables(self, cur) -> bool:
        res = self.cur.execute("SELECT name FROM sqlite_master")
        if res.fetchall != constants.required_tables:
            missing_tables = [x for x in res if x not in constants.required_tables]
            logging.info(f"{constants.database_name} is missing the following required tables")
            logging.info(missing_tables)
            return False
        return True
    
    def create_tables(self):
        
    

    def update_table(self):

def main():
    con = sqlite3.connect("atm.db")
    cur = con.cursor()
    pass

