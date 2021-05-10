"""
Information
-----------
Author: Marcelo Luciano
Organization: Perseus

Summary
-------
A small script to add an entry to the failures database using sqlite3
and terminal input.

Imports
-------
sqlite3
    For interacting with a local SQLite database.
datetime
    For creating a timestamp for new failures.
"""

import sqlite3
import datetime

# Define a project folder.
proj_folder = "Projects/Failures"

# Open a connection to the database.
conn = sqlite3.connect(f"{proj_folder}/res/database.db")
cur = conn.cursor()

def add_failure(proj:str, failure:str):
    """
    Adds a failure to the Failures database.

    Parameters
    ----------
    proj: str
        The name of the project to add the failure to.
    failure: str
        A short description of the failure.
    """

    # Generate the current timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%m-%d-%Y")

    # Add the failure to the database.
    sql = """
        INSERT INTO Failure (project, failure, date) VALUES (?, ?, ?)
    """
    cur.execute(sql, (proj, failure, timestamp))

# Grab the user input
print("Project Name: ", end="")
proj = input()
print("Failure: ", end="")
failure = input()

# Add the entry to the database.
add_failure(proj, failure)

# Commit the changes
conn.commit()