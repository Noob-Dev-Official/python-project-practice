import database

# database.add_one("Jon", "Don", "jon@test.com")
# database.delete_record('6')
list = [
	("hello", "one", "hello@test.com"),
	("bye", "one", "bye@test.com")
]


database.add_many(list)

database.show_all()
