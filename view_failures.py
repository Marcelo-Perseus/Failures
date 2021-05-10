"""
Information
-----------
Author: Marcelo Luciano
Organization: Perseus

Summary
-------
This script prints out the failures stored in the database.

Imports
-------
sqlite3
    For interacting with the local SQLite database.
"""

import sqlite3

# Define the project folder
proj_folder = "Projects/Failures"

# Open the database.
conn = sqlite3.connect(f"{proj_folder}/res/database.db")
cur = conn.cursor()

def get_all_entries():
    """
    Returns a list of all of the entries stored in the database.

    Notes
    -----
    - This method does not filter the results, it just sorts them by
    date.

    Returns
    -------
    Returns a list of all of the entries stored in the database.
    """

    # Get all of the data in the database.
    sql = """
        SELECT * FROM Failure
        ORDER BY date
    """
    cur.execute(sql)

    # Return the data.
    return cur.fetchall()

# Grab all of the entries
entries = get_all_entries()

# Display all of the entries.
for (_, proj, failure, date) in entries:
    print(f"[{date}]: {proj} - {failure}")