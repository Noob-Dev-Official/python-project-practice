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

# Query the DB and
def show_all():
	conn = sqlite3.connect('customer.db')

	# create cursor - this executes sqlite commands
	c = conn.cursor()

	c.execute("SELECT rowid, * FROM Customers")

	names = c.fetchall()

	for name in names:
		print(str(name[0]) + "\t" + name[1] + "\t" + name[2] + "\t" + name[3])

	conn.commit()
	conn.close() 

# add a new record to the table
def add_one(first, last, email):
	conn = sqlite3.connect('customer.db')

	# create cursor - this executes sqlite commands
	c = conn.cursor()

	c.execute("INSERT INTO Customers VALUES (? ,? ,?)", (first, last, email))

	conn.commit()
	conn.close()

# delete a record from database
def delete_record(id):
	conn = sqlite3.connect('customer.db')

	# create cursor - this executes sqlite commands
	c = conn.cursor()

	c.execute("DELETE FROM Customers WHERE rowid=(?)", id)

	conn.commit()
	conn.close()

def add_many(list):
	conn = sqlite3.connect('customer.db')

	# create cursor - this executes sqlite commands
	c = conn.cursor()

	c.executemany("INSERT INTO Customers VALUES (?, ? ,?)", (list))

	conn.commit()
	conn.close()



print("Done")