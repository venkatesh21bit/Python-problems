
menu = [("Idli", 20), ("Dosa", 40), ("Vada", 15), ("Pongal", 30), ("Biryani", 80), ("Parotta", 25), ("Chapati", 20), ("Kurma", 35)]


print("Welcome to our restaurant!")
print("Here is our menu:")
for dish, price in menu:
    print(f"{dish}: Rs.{price}")

order = []

while True:
    choice = input("Enter your choice of dish or type 'done' to finish ordering: ")
    if choice.lower() == "done":
        break
    else:
        for dish, price in menu:
            
       
        
            if choice.lower() == dish.lower():
                order.append((dish, price))
                print(f"Added {dish} to your order.")
                break
            else:
           
                print("Sorry, we don't have that dish. Please choose from the menu.")


total = 0
for dish, price in order:
    total += price


print("Your order summary:")
for dish, price in order:
    print(f"{dish}: Rs.{price}")
print(f"Total bill: Rs.{total}")
