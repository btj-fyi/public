import sqlite3
import os
import constants
import logging


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
        con = sqlite3.connect(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), constants.database_filename
            )
        )
        self.cur = con.cursor()

        for table in constants.database_schema["tables"]:
            print(table)
            create_table_statement = f"CREATE TABLE IF NOT EXISTS {table} ("
            for column, type in constants.database_schema["tables"][table][
                "columns"
            ].items():
                create_table_statement += f"{column} {type},"
            create_table_statement = create_table_statement[:-1] + ")"

            print(create_table_statement)
            self.cur.execute(create_table_statement)

    def get_password(self):
        pass

    def update_password(self):
        pass

    def get_balance(self, account_id: int) -> float:
        try:
            balance = self.cur(
                f"SELECT balance FROM accouts WHERE account_id = {account_id}"
            )
            logging.INFO(balance)
            return balance
        except Exception as e:
            logging.ERROR(e)

    def update_balance(self, account_id: int, balance: float):
        try:
            res = self.cur(
                f"UPDATE accounts SET balance = {balance} WHERE account_id = {account_id}"
            )
            logging.INFO(res)
            return res
        except Exception as e:
            logging.ERROR(e)

    def create_user(self):
        pass

    def get_user_id(self, username: int):
        try:
            user_id = self.cur(f"SELECT user_id FROM users WHERE username = {username}")
            logging.INFO(user_id)
            return user_id
        except Exception as e:
            logging.ERROR(e)

    def update_user(
        self, user_id: int, username: str = None, fname: str = None, lname: str = None
    ):
        update_user_statement = "UPDATE users SET "
        if username != None:
            update_user_statement += f"username = '{username}',"
        if fname != None:
            update_user_statement += f"fname = '{fname}',"
        if lname != None:
            update_user_statement += f"lname = '{lname}',"
        update_user_statement = update_user_statement[:-1] + "WHERE user_id = {user_id}"
        try:
            res = self.cur(update_user_statement)
            logging.INFO(res)
            return res
        except Exception as e:
            logging.ERROR(e)

    def delete_user(self):
        pass

    def create_account(self):
        pass

    def get_accounts(self, user_id: int):
        try:
            res = self.cur(f"SELECT account_id FROM accounts WHERE owner = {user_id}")
            logging.INFO(res)
            return res
        except Exception as e:
            logging.ERROR(e)

    def update_account(self, user_id: int, type: str = None, owner: str = None):
        pass

    def delete_account(self):
        pass


def main():
    db = DB()


main()
