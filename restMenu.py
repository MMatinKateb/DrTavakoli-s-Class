from os import _exit
from os import system

def draw_line():
    print('===' * 30)

class Rest:
    price = 0

    def __init__(self):
        self.orders = []

    def get_diet(self):
        draw_line()
        diet = input('Enter diet(Breakfast/Lunch/Dinner/Drink/Others): ')
        self.choice = diet

    def get_order(self):
        draw_line()
        if self.choice == 'Breakfast':
            self.meal = input("Your choice: 'Breakfast'\n$3 bacon\n$3 eggs\n$3 pancakes\n")
            self.orders.append(self.meal)
            return

        elif self.choice == 'Lunch':
            self.meal = input("Your choice: 'Lunch'\n$5 rice\n$5 chicken\n$5 pasta\n")
            self.orders.append(self.meal)
            return

        elif self.choice == 'Dinner':
            self.meal = input("Your choice: 'Dinner'\n$5 steak\n$3 eggs\n$5 spaghetti\n")
            self.orders.append(self.meal)
            return

        elif self.choice == 'Drink':
            self.meal = input("Your choice: 'Drink'\n$5 wine\n$1 soda\n$1 orange juice\n")
            self.orders.append(self.meal)
            return

        elif self.choice == 'Others':
            self.meal = input("Your choice: 'Others'\n$2 yogurt\n$2 salad\n$2 bread\n")
            self.orders.append(self.meal)
            return

        else:
            print("==> !!! [Invalid Input] !!!")

    def calculate_price(self):
        draw_line()
        for order in self.orders:
            if order == 'bacon' or order == 'eggs' or order == 'pancakes':
                self.price += 3
            elif order == 'rice' or order == 'chicken' or order == 'pasta' or order == 'steak' or order == 'wine' or order == 'spaghetti':
                self.price += 5
            elif order == 'soda' or order == 'orange juice':
                self.price += 1
            elif order == 'yogurt' or order == 'salad' or order == 'bread':
                self.price += 2
            else:
                print('==> !!! [Invalid Input in Orders] !!!')
                _exit(0)

        print(f"==> $$$ [Calculated price: ${self.price}] $$$")
    
    def payment(self):
        draw_line()
        opt = input("Enter 'pay' to pay\nEnter 'cancel' to cancel transcation\n")
        if opt == 'pay':
            print("Have a nice day! :)")
        elif opt == 'cancel':
            print("Cancelled.")
        else:
            print("==> !!! [Invalid Input] !!!")


def main():
    if __name__ == '__main__':
        obj = Rest()
        while True:
            try:
                system('clear')

                obj.get_diet()
                obj.get_order()

                cont = input('Want to continue?"y/n": ')
                if cont == 'y':
                    continue
                elif cont == 'n':
                    obj.calculate_price()
                    obj.payment()
                    break
                else:
                    print("==> !!! [Invalid Input] !!!")
                    continue
            
            except:
                draw_line()
                print("==> !!! [An Error Occured] !!!")
                continue
                
main()