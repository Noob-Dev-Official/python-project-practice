# print("hello")
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
# c.execute(
# """
#    CREATE TABLE Customers (
#       CustomerID INT PRIMARY KEY,
#       FirstName TEXT,
#       LastName TEXT
#       Email TEXT
#    )

# """
# )

# data insertion
# c.execute(
#    """
#       INSERT INTO Customers 
#          VALUES ("John", "Don", "test@test.com")
#    """
# )

c.execute(
   """
      INSERT INTO Customers 
         VALUES ("Me", "Don", "test@test.com")
   """
)

c.execute(
   """
      INSERT INTO Customers 
         VALUES ("You", "Don", "test@test.com")
   """
)

c.execute(
   """
      SELECT * FROM Customers
   """
)

# commit our command
conn.commit()

# close our connection (by default, the file closes it but it is a good practice to close it)
conn.close()

print("hello")