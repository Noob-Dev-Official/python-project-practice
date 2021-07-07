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

# data insertion
many_customers = [
   ("Wes", "Brown", "wes@test.com"),
   ("Mary", "Brown", "mary@test.com"),
   ("Les", "Brown", "les@test.com"),
]

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

c.executemany(
   "INSERT INTO Customers VALUES (?,?,?)", many_customers
)

# commit our command
conn.commit()

# close our connection (by default, the file closes it but it is a good practice to close it)
conn.close()

print("Done")