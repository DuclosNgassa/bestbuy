from products import Product
from store import Store


def setup():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


def start(store: Store):
    while True:
        show_menu()
        user_input = input("Please choose a number: ")
        if not user_input.isdigit():
            print("Error with your choice. Please choose a number")
            continue
        else:
            result = process_input(store, user_input)
            if result == "exit":
                break


def show_menu():
    menu = """
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """
    print(menu)


def print_delimiter(c="-", factor: int = 20) -> None:
    print(c * factor)


def process_input(store: Store, user_input: str) -> str | None:
    user_input = int(user_input)
    if user_input <= 0 or user_input > 4:
        print("Error with your choice. Please choose a number between 1 and 4")
    match user_input:
        case 1:
            show_all_product(store)
        case 2:
            show_total_amount(store)
        case 3:
            make_an_order(store)
        case 4:
            print("Bye bye!")
            return "exit"
    return None


def show_all_product(store: Store):
    print_delimiter()
    print("Available products:")
    for i, p in enumerate(store.get_all_products()):
        print(f"{i + 1}. ", end="")
        p.show()
    print_delimiter()


def show_total_amount(store: Store):
    print_delimiter()
    print(f"Total of {store.get_total_quantity()} items in store")
    print_delimiter()


def make_an_order(store: Store):
    print_delimiter()
    show_all_product(store)
    print("When do you want to finish your order, enter empty text.")
    order_list: list[tuple[Product, int]] = []

    while True:
        user_input_product = input("Which product # do you want? ")
        if not user_input_product.strip():
            break

        user_input_quantity = input("What amount do you want? ")
        if not user_input_quantity.strip():
            break

        if not user_input_quantity.isdigit() or not user_input_product.isdigit():
            print("Error: Please enter valid positive numbers for product and quantity.\n")
            continue

        product_index = int(user_input_product) - 1
        quantity = int(user_input_quantity)
        selected_product = store.products[product_index]
        order_list.append((selected_product, quantity))

    if len(order_list) > 0:
        total_price = store.order(order_list)
        print(f"Order made! Total payment: {total_price}")

    print_delimiter()


if __name__ == "__main__":
    setup()
