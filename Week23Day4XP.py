# Exercise 1 : Favorite Numbers
my_fav_numbers = {3, 7, 14}  
my_fav_numbers.update([21, 25]) 
my_fav_numbers.remove(25) 

friend_fav_numbers = {5, 10, 15}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)


# Exercise 2: Tuple
# Not possible to add more integers directly to the tuple, because tuples can not be changed.


# Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
print("Number of apples:", apple_count)
basket.clear()
print("Basket after emptying:", basket)


# Exercise 4: Floats
# A float is a number with a decimal point. The difference between an integer and a float is that integers are whole numbers without decimals.
float_sequence = [x * 0.5 for x in range(3, 11)]
print("Float sequence:", float_sequence)
# Another way to generate a float sequence is to use numpy's arange function, though it requires importing the numpy library.


# Exercise 5: For Loop
for i in range(1, 21):
    print(i)

print("Even indexed numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercise 6 : While Loop
user_name = ""
my_name = "YourName"  # Replace "YourName" with your actual name
while user_name != my_name:
    user_name = input("Enter your name: ")
print("You entered the correct name!")


# Exercise 7: Favorite fruits
favorite_fruits = input("Enter your favorite fruits, separated by a space: ").split()
chosen_fruit = input("Enter the name of a fruit: ")
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")


# Exercise 8: Who ordered a pizza?
toppings = []
while True:
    topping = input("Enter a topping for your pizza (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_price = 10 + 2.5 * len(toppings)
print("Your toppings:", toppings)
print("Total price:", total_price)


# Exercise 9: Cinemax
total_cost = 0
family_ages = [int(age) for age in input("Enter the ages of family members, separated by space: ").split()]
for age in family_ages:
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price
print("Total cost for family tickets:", total_cost)

teenager_names = ["Alice", "Bob", "Charlie"]
final_list = []
for name in teenager_names:
    age = int(input(f"Enter the age of {name}: "))
    if 16 <= age <= 21:
        print(f"{name} is not allowed to watch this mov
