database_filename: str = "atm.db"
account_types: dict = {
    "checking": 1,
    "savings": 2,
}
transaction_types: dict = {
    "deposit": 1,
    "withdraw": 2,
    "transfer": 3,
}
password_salt: str = "this_is_a_salt"
database_schema = {
    "database_name": "atm",
    "tables": {
        "users": {
            "columns": {
                "user_id": "integer primary key autoincrement",
                "username": "varchar(255)",
                "fname": "varchar(255)",
                "lname": "varchar(255)",
                "password": "binary(32)",
                "last_login_ts": "float",
                "last_transaction_ts": "float",
                "user_created_ts": "float",
            },
        },
        "accounts": {
            "columns": {
                "account_id": "integer primary key autoincrement",
                "owner_user_id": "varchar(255)",  # aka owner's username
                "account_type": "int",
                "balance": "float",
                "last_login_ts": "float",
                "last_transaction_ts": "float",
                "account_created_ts": "float",
            },
        },
        "transactions": {
            "columns": {
                "transaction_id": "integer primary key autoincrement",
                "timestamp": "float",
                "user_id": "int",
                "transaction_type": "int",  # deposit, withdraw, transfer, wire, etc.
                "source_account_id": "int",
                "destination_account_id": "int",
                "quantity": "int",
            },
        },
    },
}
