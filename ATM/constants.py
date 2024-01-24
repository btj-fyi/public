database_filename:str = "atm.db"
database_schema = {
    "database_name": "atm",
    "tables": {
        "users": {
            "columns": {
                "user_id":"int",
                "username":"varchar(255)",
                "fname":"varchar(255)",
                "lname":"varchar(255)",
                "password":"binary(32)",
            },
        "accounts": {
            "columns": {
                "account_id":"int",
                "owner":"varchar(255)", # aka owner's username
                "last_login_ts":"timestamp",
                "last_transaction_ts":"timestamp",
                },
            },
        "transactions": {
            "columns": {
                "timestamp":"timestamp",
                "user_id":"int",
                "type":"tinyint", # deposit, withdraw, transfer, wire, etc.
                "source_account_id":"int",
                "destination_account_id":"int",
                "quantity":"int",
                },
            },
        }, 
    },
}