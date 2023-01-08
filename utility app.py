print("------Welcome to GrabnGo------\n\n")


print("           MENU")
print("       List of Snacks:")
print("|Number 1 | Doritos Cheese = 2.50 AED")
print("|Number 2 | Piatos SourCream = 2.50 AED")
print("|Number 3 | Oman Chips = 2.50 AED")
print("|Number 4 | Loacker Wafer Chocolate = 4 AED")
print("|Number 5 | Loacker Wafer Vanilla  = 4 AED")
print("|Number 6 | Hersey Chocolate Bar = 5 AED")
print("|Number 7 | M&Ms Chocolate = 3 AED")
print("|Number 8 | Galaxy Chocolate Flute = 3 AED")
print("|Number 9 | Haribo Gummybear = 3 AED")
print("|Number 10 | Haribo Gummyworms = 3 AED ")

    

        
item = int(input("Please select a snack. If none, press 0: "))

if item == 1: 
  print("You have choosen Doritos Cheese")
  print("Cost: 2.50 AED")
  cost = 2.50
  money_in = int(input("Insert amount here:\n"))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")
      
elif item == 2:
  print("You have selected Piatos SourCream ")
  print("Cost: 2.50 AED")
  cost = 2.50
  money_in = int(input("Insert amount here:\n"))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 3:
  print("You have selected Oman Chips")
  print("Cost: 2.50 AED")
  cost = 2.30
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 4:
  print("You have selected Loacker Wafer Chocolate")
  print("Cost: 4 AED")
  cost = 4
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 5:
  print("You have selected Loacker Wafer Vanilla")
  print("Cost: 4 AED")
  cost = 4
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 6:
  print("You have selected Hersey Chocolate Bar")
  print("Cost: 5 AED")
  cost = 5
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 7:
  print("You have selected M&Ms Chocolate")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 8:
  print("You have selected Galaxy Chocolate Flute")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 9:
  print("You have selected Haribo Gummybear")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 10:
  print("You have selected Haribo Gummyworms")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif item == 0:
  print("Options for snacks has been declined.")

else:
  print("You have entered an invalid number.")

print("           MENU")
print("       List of Beverages:")
print("|Number 11 | Sweet Ice Tea Lemon = 7 AED")
print("|Number 12 | Chocolate Milk = 5 AED")
print("|Number 13 | Strawberry Milk = 5 AED")
print("|Number 14 | Pepsi = 3 AED")
print("|Number 15 | Coca Cola  = 3 AED")
print("|Number 16 | Fanta Orange = 5 AED")
print("|Number 17 | Vimto = 6 AED")
print("|Number 18 | Sprite = 5 AED")
print("|Number 19 | Dubai Water = 0.50 AED")
print("|Number 20 | Capri-Sun Fruitmix = 2 AED ")
        
Beverages = int(input("Please select a drink. If none, press 0: "))
          
if Beverages == 11:
  print("You have Sweet Ice Tea Lemon selected ")
  print("Cost: 7 AED")
  cost = 7
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 12:
  print("You have selected Chocolate Milk")
  print("Cost: 5 AED")
  cost = 5
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 13:
  print("You have selected Strawberry Milk")
  print("Cost: 5 AED")
  cost = 5
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 14:
  print("You have Pepsi selected ")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 15:
  print("You have Coca Cola selected ")
  print("Cost: 3 AED")
  cost = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 16:
  print("You have Fanta Orange selected ")
  print("Cost: 5 AED")
  cost = 6
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 17:
  print("You have Vimto selected ")
  print("Cost: 6 AED")
  cost = 6
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 18:
  print("You have Sprite selected ")
  print("Cost: 5 AED")
  cost = 5
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 19:
  print("You have Dubai Water selected ")
  print("Cost: 0.50 AED")
  cost = 0.50
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

elif Beverages == 20:
  print("You have Capri-Sun Fruitmix selected ")
  print("Cost: 2 AED")
  cost = 2
  money_in = int(input("Insert amount here: "))
  money_out = money_in - cost
  if money_in > cost:
    print("item recived and change of", money_out, "AED")
  elif money_in == cost:
    print("item recived")
  else:
    print("You have not given an enough amount to purchase ")

        
elif Beverages == 0:
  print("Choosing Beverages Had Been Skipped.")

else:
  print("You have entered an invalid number.")

print("Thank you for purchasing!. Have a nice day!. ")