#project 2
#project name = CAFE MANAGEMENT SYSYTEM

menu = {
    "pohe":30,
    "chai":10,
    "coffee":50,
    "milk":70
}

print("welcome to MAHESH COFFEE CENTRE")
print("pohe:Rs30\nchai:Rs10\ncoffee:Rs50\nmilk:Rs70")

order_total = 0

item_1 = input("enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your Item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available")        
another_order= input("do you want to add another item?(yes/no)")
if another_order == "Yes":
    item_2 = input("enter the name of second item:")
    if item_2 in menu:
            order_total+= menu[item_2]
            print(f"Item{item_2}has been added to order")
    else:
         print(f"ordered item {item_2}is not available")
print(f"the total amount for your order to pay is {order_total}")                 