"""
Information
-----------
Author: Marcelo Luciano
Organization: Perseus

Summary
-------
A short script to create the Failure table in the local database.

Imports
-------
sqlite3
    For interacting with a local SQLite database.
"""

import sqlite3

# Define the project folder location.
proj_folder = "Projects/Failures"

# Open up a connection with the database.
conn = sqlite3.connect(f"{proj_folder}/res/database.db")
cur = conn.cursor()

# Create the table.
sql = """
    CREATE TABLE Failure (
        id integer PRIMARY KEY,
        project text NOT NULL,
        failure text NOT NULL,
        date text
    )
"""
cur.execute(sql)