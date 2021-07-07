import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()
# queries 

# display data from the database
# rowid is soemthing created by the sqlite3 automatically
c.execute("SELECT rowid, * FROM Customers")

# print(c.fetchall()) # fetches all the data 
# print(c.fetchone()) # fetches single data
# print(c.fetchone()[1]) # since the output is in tuple, each element in tuple is indexed by 0 so we can do this

names = c.fetchall()

# prints the names from the databse in a more readable way
for name in names:
	print(str(name[0]) + "\t" + name[1] + "\t" + name[2])



conn.commit()
conn.close() 