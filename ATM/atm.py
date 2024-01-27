import sqlite3
import os
from typing import Any
import constants
import logging
import time
import hashlib
from getpass import getpass

# TODO paramaterize SQL queries


class ATM:
    def __init__(self):
        self.username = None
        self.user_id = None
        self.locked = True
        self.focused_account_id: int = None
        self.menu()

    def menu(self):
        print("Press 1 to Login")
        print("Press 2 to Show Balance")
        print("Press 3 to Deposit")
        print("Press 4 to Withdraw")
        print("Press 5 to Transfer")
        print("Press 6 to Wire")
        print("Press 7 to Open a New Account")
        print("Press 8 to Close an Existing Account")
        print("Press 9 to Logout")
        user_input = input()
        match user_input:
            case "1":
                self.login()
            case "2":
                self.balance()
            case "3":
                self.deposit()
            case "4":
                self.withdraw()
            case "5":
                self.transfer()
            case "6":
                self.wire()
            case "7":
                self.open_account()
            case "8":
                self.close_account()
            case "9":
                self.logout()

    def login(self):
        print("Please, provide your username and password.")
        self.username = input("Username: ")
        self.user_id = User.is_user(self, self.username)
        if self.user_id:
            password = getpass("Password: ")
            if Password.verify_password(
                self, password, DB.get_password(self, self.user_id)
            ):
                print(
                    "The provided username and password are correct. Logging in..."  # noqa: E501
                )
                self.locked = False
                return
            else:
                print(
                    "The provided username or password are not correct. Please, try again..."  # noqa: E501
                )
                self.login()
        else:
            print("That username does not exist.")
            print("Press 1 to try again")
            print("Press 2 to create an account")
            user_input = input()
            if user_input == 1:
                self.login()
            elif user_input == 2:
                fname = input("First Name: ")
                lname = input("Last Name: ")
                new_username = input("Username:")
                new_password = input("Password:")
                User.create_user(
                    self,
                    new_username,
                    fname,
                    lname,
                    new_password,
                )

    def logout(self):
        self.locked = True
        self.user_id = None
        self.focused_account_id = None

    def select_account(self):
        if self.focused_account_id is not None:
            print(
                f"Would you like to continue using the account from your previous transaction ({self.focused_account_id})?"  # noqa: E501
            )
            print("Press 1 for YES")
            print("Press 2 for no NO")
            user_input = input()
            if user_input == 1:
                return self.focused_account_id
        accounts = User.get_accounts(self, self.user_id)
        for i, account in enumerate(accounts):
            print(f"Press {i+1} for {account}")
        user_input = input()
        # TODO add input validation
        self.focused_account_id = accounts[user_input - 1][1]
        return accounts[user_input - 1]

    def balance(self):
        if not self.locked:
            account_id = self.select_account()
            balance = Account.get_balance(self, account_id)
            print(f"${balance}")
        else:
            print("You are not logged in. Please, login and try again...")
            self.login()

    # TODO reduce DB calls by combining read and write operations here
    def deposit(self):
        if not self.locked:
            quantity = input("How much would you like to deposit:")
            account_id = self.select_account()
            existing_balance = Account.get_balance(self, account_id)
            new_balance = existing_balance + quantity
            Account.update_balance(self, account_id, new_balance)
            print(f"Your new balance is ${new_balance}")
        else:
            print("You are not logged in. Please, login and try again...")
            self.login()

    # TODO reduce DB calls by combining read and write operations here
    def withdraw(self):
        if not self.locked:
            quantity = input("How much would you like to withdraw:")
            account_id = self.select_account()
            existing_balance = Account.get_balance(self, account_id)
            new_balance = existing_balance - quantity
            Account.update_balance(account_id, new_balance)
            print(f"Your new balance is ${new_balance}")
        else:
            print("You are not logged in. Please, login and try again...")
            self.login()

    def transfer(self):
        if self.locked == False:
            quantity = input("How much would you like to transfer:")
            print("Select the source account")
            source_account_id = self.select_account()
            print("Select a destination account")
            accounts = User.get_accounts(self.user_id)
            for i, account in enumerate(accounts):
                print(f"Press {i+1} for {account}")
            user_input = input()
            # TODO add input validation
            destination_account_id = accounts[user_input - 1][1]
            Account.transfer(source_account_id, destination_account_id, quantity)

    def wire(self):
        if self.locked == False:
            quantity = input("How much would you like to wire:")
            print("Select the source account")
            source_account_id = self.select_account()
            destination_username = input(
                "What is the username of person you would like to wire to:"
            )
            if User.is_user(destination_username):
                print("Select the source account")
                source_account_id = self.select_account()
                Account.wire(source_account_id, destination_username, quantity)
            else:
                print("That username does not exist.")
                print("Press 1 to try again")
                print("Press 2 to exit")
                user_input = input()
                if user_input == 1:
                    self.wire()
                else:
                    self.menu()

    def open_account(self):
        pass

    def close_account(self):
        pass


class User:
    def __init__(self):
        self.db = DB()

    def create_user(
        self, username, fname, lname, password, user_created_ts=time.time()
    ):
        DB().create_user(username, fname, lname, password, user_created_ts)

    def delete_user(self, user_id):
        DB.delete_user(self, user_id)

    def is_user(self, username):
        user_id = DB.get_user_id_from_username(self, username)
        if user_id:
            return user_id

    def get_accounts(self, user_id):
        accounts = DB.get_accounts(self, user_id)
        return accounts


class Account:
    def __init__(self):
        pass

    def create_account(self, user_id: int, account_type: str):
        DB.create_account(user_id, account_type)

    def delete_account(self, account_id):
        DB.delete_account(account_id)

    def get_owner(self, account_id):
        user_id = DB.get_user_id_from_account_id(account_id)
        return user_id

    def get_balance(self, account_id) -> float:
        balance = DB.get_balance(account_id)
        return balance

    def update_balance(self, account_id, new_balance):
        DB.update_balance(account_id, new_balance)

    def transfer(self, source_account_id, destination_account_id, quantity):
        source_account_balance = DB.get_balance(source_account_balance)
        new_source_account_balance = source_account_balance - quantity
        destination_account_id = DB.get_balance(destination_account_id)
        new_destination_account_balance = destination_account_id + quantity
        DB.update_balance(source_account_id, new_source_account_balance)
        DB.update_balance(destination_account_id, new_destination_account_balance)

    def wire(self, source_account_id, destination_username, quantity):
        source_account_balance = DB.get_balance(source_account_id)
        new_source_account_balance = source_account_balance - quantity
        accounts = User.get_accounts(DB.get_user_id_from_username(destination_username))
        for account in accounts:
            if account[1] == constants.account_types["checking"]:
                destination_account_id = account[1]
                break
            else:
                print(
                    "Wire rejected. The provided user does not have a checking account."
                )
                return
        if destination_account_id:
            new_destination_account_balance = (
                DB.get_balance(destination_account_id) + quantity
            )
            DB.update_balance(source_account_id, new_source_account_balance)
            DB.update_balance(destination_account_id, new_destination_account_balance)


class Password:
    def __init__(self):
        self.salt = constants.password_salt

    def hash_password(self, password):
        password_hash = hashlib.sha256(
            (password + self.salt).encode("utf-8")
        ).hexdigest()
        return password_hash

    def verify_password(self, provided_password, stored_password):
        password_hash = hashlib.sha256(
            (provided_password + self.salt).encode("utf-8")
        ).hexdigest()
        return password_hash == stored_password


class DB:
    def __init__(self):
        # on first run, sqlite will create the db if it does not already exist
        self.con = sqlite3.connect(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                constants.database_filename,
            )
        )
        self.cur = self.con.cursor()

        for table in constants.database_schema["tables"]:
            logging.info(table)
            create_table_statement = f"CREATE TABLE IF NOT EXISTS {table} ("
            for column, type in constants.database_schema["tables"][table][
                "columns"
            ].items():
                create_table_statement += f"{column} {type},"
            create_table_statement = create_table_statement[:-1] + ")"

            logging.info(create_table_statement)
            self.cur.execute(create_table_statement)

    def get_password(self, user_id: str):
        get_password_statemet = f"SELECT password FROM users WHERE user_id = {user_id}"
        logging.info(get_password_statemet)
        try:
            password = self.cur.execute(get_password_statemet)
            return password
        except Exception as e:
            logging.error(e)

    def update_password(self, user_id: int, password: str):
        update_password_statement = (
            f"UDPATE users SET password = {password} WHERE user_id = {user_id}"
        )
        logging.info(update_password_statement)
        try:
            balance = self.cur.execute(update_password_statement)
            logging.info(balance)
            return balance
        except Exception as e:
            logging.error(e)

    def get_balance(self, account_id: int) -> float:
        get_balance_statemet = (
            f"SELECT balance FROM accouts WHERE account_id = {account_id}"
        )
        logging.info(get_balance_statemet)
        try:
            balance = self.cur.execute(get_balance_statemet)
            logging.info(balance)
            return balance
        except Exception as e:
            logging.error(e)

    def update_balance(self, account_id: int, new_balance: float):
        update_balance_statement = f"UPDATE accounts SET balance = {new_balance} WHERE account_id = {account_id}"
        logging.info(update_balance_statement)
        try:
            res = self.cur.execute(update_balance_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def get_user_id_from_username(self, username):
        get_user_id_from_username_statement = (
            f"SELECT user_id FROM users WHERE username = {username}"
        )
        logging.info(get_user_id_from_username_statement)
        try:
            user_id = self.cur.execute(get_user_id_from_username_statement)
            logging.info(user_id)
            return user_id
        except Exception as e:
            logging.error(e)

    def get_user_id_from_account_id(self, account_id: int):
        get_user_id_from_account_id_statement = (
            f"SELECT user_id FROM users WHERE username = {account_id}"
        )
        logging.info(get_user_id_from_account_id_statement)
        try:
            user_id = self.cur.execute(get_user_id_from_account_id_statement)
            logging.info(user_id)
            return user_id
        except Exception as e:
            logging.error(e)

    def create_user(
        self,
        username: str,
        fname: str,
        lname: str,
        password: str,
        user_created_ts: float = time.time(),
    ):
        password_hash = Password.hash_password(password)
        create_user_statement = f"INSERT INTO users (username,fname,lname,password,user_created_ts) VALUES ({username},{fname},{lname},{password_hash},{user_created_ts})"
        logging.info(create_user_statement)
        try:
            res = self.cur.execute(create_user_statement)
            self.con.commit()
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def update_user_info(
        self,
        user_id: str = None,
        username: str = None,
        fname: str = None,
        lname: str = None,
        last_login_ts: float = None,
        last_transaction_ts: float = None,
    ):
        update_user_statement = "UPDATE users SET "
        if username != None:
            update_user_statement += f"username = '{username}',"
        if fname != None:
            update_user_statement += f"fname = '{fname}',"
        if lname != None:
            update_user_statement += f"lname = '{lname}',"
        if last_login_ts != None:
            update_user_statement += f"last_login_ts = '{last_login_ts}',"
        if last_transaction_ts != None:
            update_user_statement += f"last_transaction_id = '{last_transaction_ts}',"
        update_user_statement = (
            update_user_statement[:-1] + f"WHERE user_id = {user_id}"
        )
        logging.info(update_user_statement)
        try:
            res = self.cur.execute(update_user_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def delete_user(self, user_id: int):
        delete_user_statement = f"DELETE FROM users WHERE user_id = {user_id}"
        logging.info(delete_user_statement)
        try:
            res = self.cur.execute(delete_user_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def create_account(
        self,
        owner_user_id: int,
        account_type: int,
        account_created_ts: float = time.time(),
    ):
        create_account_statement = f"INSERT INTO accounts (owner_user_id,account_type,account_created_ts) VALUES ({owner_user_id},{account_type},{account_created_ts})"
        logging.info(create_account_statement)
        try:
            res = self.cur.execute(create_account_statement)
            self.con.commit()
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def get_accounts(self, user_id: int) -> list[Any]:
        """
        Returns a list of tuples like, (account_type,account_id)
        """
        get_accounts_statement = (
            f"SELECT account_type, account_id FROM accounts WHERE owner = {user_id}"
        )
        logging.info(get_accounts_statement)
        try:
            res = self.cur.execute(get_accounts_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def update_account_info(
        self,
        user_id: int,
        account_type: str = None,
        owner_user_id: str = None,
        last_login_ts: float = None,
        last_transaction_id: float = None,
    ):
        update_account_statement = "UPDATE accounts SET "
        if account_type != None:
            update_account_statement += f"username = '{account_type}',"
        if owner_user_id != None:
            update_account_statement += f"fname = '{owner_user_id}',"
        if last_login_ts != None:
            update_account_statement += f"last_login_id = '{last_login_ts}',"
        if last_transaction_id != None:
            update_account_statement += (
                f"last_transaction_id = '{last_transaction_id}',"
            )
        update_account_statement = (
            update_account_statement[:-1] + f"WHERE user_id = {user_id}"
        )
        logging.info(update_account_statement)
        try:
            res = self.cur.execute(update_account_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def delete_account(self, account_id: int):
        delete_account_statement = f"DELETE FROM accounts WHERE user_id = {account_id}"
        logging.info(delete_account_statement)
        try:
            res = self.cur.execute(delete_account_statement)
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)

    def create_transaction(
        self,
        user_id: int,
        transcation_type: int,
        source_account_id: int = None,
        destination_account_id: int = None,
        quantity: float = 0.0,
        timestamp: float = time.time(),
    ):
        create_transaction_statement = f"INSERT INTO transactions (timestamp,user_id,transcation_type,source_account_id,destination_account_id,quantity) VALUES ({timestamp},{user_id},{transcation_type},{source_account_id},{destination_account_id},{quantity})"
        logging.info(create_transaction_statement)
        try:
            res = self.cur.execute(create_transaction_statement)
            self.con.commit()
            logging.info(res)
            return res.fetchall()
        except Exception as e:
            logging.error(e)


def main():
    db = DB()
    atm = ATM()
    account = Account()
    account_id = 12345667
    account.delete_account(account_id)


main()
