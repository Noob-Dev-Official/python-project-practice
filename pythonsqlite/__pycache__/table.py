import sqlite3

conn = sqlite3.connect('customer.db')

# create cursor - this executes sqlite commands
c = conn.cursor()

# datatypes:
# NULL
# INTEGER
# TEXT
# REAL
# BLOB

# create a table
c.execute(
"""
   CREATE TABLE Customers (
      CustomerID INT PRIMARY KEY,
      FirstName TEXT,
      LastName TEXT
      Email TEXT
   )

"""
)

# commit our command
conn.commit()

# close our connection (by default, the file closes it but it is a good practice to close it)
conn.close()

print("Done")