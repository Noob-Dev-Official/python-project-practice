print("hello")
print("Bye")
print(3 + 4)

#-------
lunch = 'Pizza'
#now call this variable
print('Lunch:')
print(lunch)

#-------
#let's make a price caluclator
tea_price_aed = 1
number_of_pieces = 5
print(tea_price_aed * number_of_pieces) #this will print 5

#------let's increase the price of coffee. To do this , we perform the following step
tea_price_aed = 1.5
number_of_pieces = 5
print(tea_price_aed * number_of_pieces) #this will print 7.5!

#---------
#concantenation
#we can add up any strings or numbers into a sentence
statement = 'I live in '
address = '345 Maxwell Street, New York City.'
full_address = statement + address

#now let's print it
print(full_address)

#---------
#python can also perform exponentiation by using this operator '**'
print (5 ** 2) #gives 25

#---------
#plus equals: we use it when we update a current value and want to save or use the updated vale as a current value
Muntasir_Age = 17
Muntasir_Age += 1
print(Muntasir_Age) 

#---------
#let's create a server based program which records and log an online shopping cart and price

#product description and price

#First product
game_bundle_description = 'This product has 20 pieces of games from Microsoft, Sony and EA games entertainment.'
game_bundle_price = 30.00

#Second product
xbox_description = 'This product is from Microsoft and has only one controller with HDMI wire and free LED 32 inch monitor. LIMITED TIME OFFER'
xbox_price = 120.50

#Third product
led_smart_tv = 'Samsung LED smart TV with free HDMI wire'
led_smart_tv_price = 200.00

#Fourth product
hp_laptop = 'HP laptop, core i7 seventh generation, NVIDIA integrated graphics card, Windows 10 pro ACTIVATED'
hp_laptop_price = 2500.00

#Sales Tax
sales_tax = 0.005

#Delivery calculation
delivery_cost = 15.00

#Customer 1
customer_one_total = 0
customer_one_item = ' ';

#purchase 1
customer_one_total += led_smart_tv_price
customer_one_item += led_smart_tv

#purchase 2p
customer_one_total += xbox_price
customer_one_item += xbox_description

#purchase 3
customer_one_total += game_bundle_price
customer_one_item += game_bundle_description

#checkout-->
#tax calculation and total purchase calculation
customer_one_purchase_tax = customer_one_total * sales_tax
customer_one_purchase_total = int(customer_one_total + delivery_cost + customer_one_purchase_tax)

#printing the purchase receipt
print('Your purchased items: ')
print(customer_one_item)

print('Your total purchase: ')
print(customer_one_purchase_total)
print('All the amount are in US dollars.')
print('Happy shopping! :-)')

#----------
#Let's make a function. A welcome message for new customers in an online shopping website
def user_message(user, offer):
    print('Hello, ' + user + '. Welcome Back')
    print("Today's offer is " + offer + ". HAPPY SHOPPING!")

#Now, let's call the function
#you can either call the funciton or make another variable to call define the parameters of the funciton and call it.
#user_message('John', '50% OFF on all electronics') ...first way, calling the function....
user_welcome = user_message('John', '50% OFF on all electronics') #...second way
print(user_welcome); #and so on

#--------
#practising in the university
#these are for making sets...
set_1 = {1,2,7}
set_2 = {3,4,5}
print(set_1)
print(set_2)

a, b = {1, 2, 3,}, {2.1,2.3,7.2}
print(b) #set b shows the number in an unordered manner.

c = {}
print(c)

