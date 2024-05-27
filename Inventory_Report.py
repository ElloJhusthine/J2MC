products = ['shampoo', 'body soap', 'conditioner','soy sauce','vinegar','salt','sugar','oil','dishwashing liquid','milk','coffee','detergent','fabric conditioner','pancit canton','canned goods']
price = [10, 15, 10, 20, 20, 15, 30, 30, 15, 10, 10, 10, 10, 20, 35]
quantity = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
total_sales = [0, 0, 0]

def main():
    print("\n >> Welcome to J2G Mini Store. :> << \n")
    while True:
        print("\n++++++++++++++ J2MC +++++++++++++")
        choose = int(input("\n[1] Inventory\n[2] Sales\n[3] Report\n[4] Exit\n> "))
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if choose == 1:
            print("\n+++++++++++++ Inventory ++++++++++++\n")
            for i in range(len(products)):
                print(f"[{i+1:2}] {products[i]:20} : Php {price[i]:2} --------- Quantity: {quantity[i]}")
            t = input('Do you want to start again?? (y/n): ')
            if t == 'y':
                print()
            else:
                print("\n=============== Thank you and God bless ❤ ===============")
                exit()
        elif choose == 2:
            print("\n+++++++++ Sales ++++++++\n")
            print('[ 1]Shampoo:\t\t\t\t\tPhp 11.2\n[ 2]Soap:\t\t\t\t\tPhp 16.8\n[ 3]Conditioner:\t\t\t\tPhp 11.2\n[ 4]Soy Sauce:\t\t\t\t\tPhp 22.4\n[ 5]Vinegar:\t\t\t\t\tPhp 22.4\n[ 6]Salt:\t\t\t\t\tPhp 16.8\n[ 7]Sugar:\t\t\t\t\tPhp 33.6\n[ 8]Oil:\t\t\t\t\tPhp 33.6\n[ 9]Dishwashing liquid:\t\t\t\tPhp 16.8\n[10]Milk:\t\t\t\t\tPhp 11.2\n[11]Coffee:\t\t\t\t\tPhp 11.2\n[12]Liquid detergent:\t\t\t\tPhp 11.2\n[13]Fabric conditioner:\t\t\t\tPhp 11.2\n[14]Pancit canton:\t\t\t\tPhp 22.4\n[15]Canned goods:\t\t\t\tPhp 34.2')
            item = int(input("What would you like to buy?: "))
            if item > 15 or item < 1:
                print('\n=============== Invalid Input!!! ===============\n')
            else:
                num_item = int(input("How many?: "))
                item_index = item - 1
                item_price = price[item_index]
                interest = item_price * 0.12
                total_pay = (item_price + interest) * num_item 
                print('\nYour total payment is:', round(total_pay, 2))
                payment = int(input('Enter your cash: '))
                sales(products, quantity, price, total_sales, item, num_item, payment, interest, total_pay)
        elif choose == 3:
            print("\n+++++++++++++ Reports ++++++++++++\n")
            for i in range(len(products)):
                print(f"[{i+1:2}] {products[i]:20} : Php {price[i]:2} -------- Quantity Left: {quantity[i]:3} -------- Sold: {100 - quantity[i]}")
            print("\n>> (12% interest) Total Sales: Php ", round(total_sales[0],2), "\t\tTotal Items Sold: ", total_sales[1], "\t\t Profit: Php ", round(total_sales[2], 2))
            t = input('\nDo you want to start again?? (y/n): \n')
            if t == 'y':
                print()
            else:
                print("\n=============== Thank you and God bless ❤ ===============\n")
                exit()
        elif choose == 4:
            print("\n=============== Thank you and God bless ❤ ===============\n")
            break
        else:
            print('\n=============== Invalid Input!!! ===============\n')
            
def sales(prod, qua, pr, total_sales, item, num_item, payment, interest, total_pay):
    item_index = item - 1
    item_name = prod[item_index]
   
    if payment < total_pay:
        print('The amount to pay: Php',round(total_pay,2))
        print("\nWarning!!!!\nYour money is only Php",payment,"\nSorry insufficient money!!!\n")
        return

    if qua[item_index] < num_item:
        print("\nThere are only", qua[item_index], item_name, "(s) left in stock.")
        cnt = input('Do you want to start again? (y/n): ')
        if cnt == 'y':
            return
        else:
            print("\n=============== Thank you and God bless ❤ ===============\n")
            exit()
    else:
        change = payment-total_pay
        print("Your change is:", round(change, 2))
        qua[item_index] -= num_item
        total_sales[0] += total_pay
        total_sales[1] += num_item
        total_sales[2] += interest * num_item
    
    cnt = input('\nDo you want to continue shopping? (y/n): ')
    if cnt != 'y':
        print("\n=============== Thank you and God bless ❤ ===============\n")
        exit() 

main()