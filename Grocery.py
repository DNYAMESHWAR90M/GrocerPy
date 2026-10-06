# ---------------------------------------------------------
#       GROCERY INVOICE SYSTEM (ATTRACTIVE EDITION)
# ---------------------------------------------------------

# ANSI Color Codes for Styling Terminal Output
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"

products = {
    "Fruits": {
        1: ("Apple", 120),
        2: ("Banana", 60),
        3: ("Mango", 150),
        4: ("Orange", 90)
    },
    "Vegetables": {
        1: ("Potato", 40),
        2: ("Tomato", 50),
        3: ("Onion", 35),
        4: ("Carrot", 60)
    },
    "Dairy": {
        1: ("Milk", 60),
        2: ("Butter", 55),
        3: ("Cheese", 120),
        4: ("Curd", 40)
    },
    "Snacks": {
        1: ("Chips", 20),
        2: ("Biscuits", 30),
        3: ("Chocolate", 50)
    },
    "Beverages": {
        1: ("Tea", 25),
        2: ("Coffee", 40),
        3: ("Cold Drink", 45)
    }
}

cart = []

print(CYAN + BOLD + "=" * 60)
print("             🛍️  WELCOME TO FRESHMART  🛍️              ")
print("=" * 60 + RESET)

customer = input(YELLOW + "Enter Customer Name: " + RESET).strip()
if not customer:
    customer = "Valued Customer"

while True:
    print(MAGENTA + "\n+==========================================+" + RESET)
    print(MAGENTA + "|" + BOLD + "               MAIN MENU                  " + RESET + MAGENTA + "|" + RESET)
    print(MAGENTA + "+==========================================+" + RESET)
    print("  1. 🍎 Fruits")
    print("  2. 🥕 Vegetables")
    print("  3. 🥛 Dairy")
    print("  4. 🍪 Snacks")
    print("  5. ☕ Beverages")
    print("  6. 🧾 Generate Invoice & Save")
    print("  7. 🚪 Exit")
    print(MAGENTA + "+==========================================+" + RESET)

    try:
        choice = int(input(YELLOW + "Enter Choice (1-7): " + RESET))
    except ValueError:
        print(RED + "❌ Invalid input! Please enter a number between 1 and 7." + RESET)
        continue

    if choice == 7:
        print(GREEN + "\n✨ Thank You for Visiting FreshMart! Have a great day! ✨" + RESET)
        break

    elif choice == 6:
        if len(cart) == 0:
            print(RED + "\n⚠️ Your cart is empty! Please add some items before generating an invoice." + RESET)
            continue

        # Build clean invoice content
        invoice_lines = []
        invoice_lines.append("=" * 60)
        invoice_lines.append("                    FRESHMART GROCERY                   ")
        invoice_lines.append("                 TAX INVOICE / RECEIPT                  ")
        invoice_lines.append("=" * 60)
        invoice_lines.append(f"Customer Name : {customer}")
        invoice_lines.append("-" * 60)
        invoice_lines.append("{:<18}{:<8}{:<10}{:<12}".format("Item Name", "Qty", "Price", "Amount"))
        invoice_lines.append("-" * 60)

        subtotal = 0

        for item in cart:
            name, qty, price = item
            amount = qty * price
            subtotal += amount
            invoice_lines.append("{:<18}{:<8}{:<10}{:<12}".format(name, qty, f"₹{price}", f"₹{amount}"))

        gst = subtotal * 0.05
        total = subtotal + gst

        invoice_lines.append("-" * 60)
        invoice_lines.append(f"{'Subtotal:':<36} ₹{subtotal:.2f}")
        invoice_lines.append(f"{'GST (5%):':<36} ₹{gst:.2f}")
        invoice_lines.append("=" * 60)
        invoice_lines.append(f"{'GRAND TOTAL:':<35} ₹{total:.2f}")
        invoice_lines.append("=" * 60)
        invoice_lines.append("           Thank You for Shopping With Us!          ")
        invoice_lines.append("=" * 60)

        invoice_output = "\n".join(invoice_lines)

        # Print styled invoice on screen
        print(GREEN + "\n" + invoice_output + RESET)

        # Save invoice to text file automatically
        filename = f"Invoice_{customer.replace(' ', '_')}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invoice_output)
            print(CYAN + f"\n📁 Success! Receipt automatically saved as: '{filename}'" + RESET)
        except Exception as e:
            print(RED + f"❌ Error saving file: {e}" + RESET)

        break

    elif 1 <= choice <= 5:
        category_map = {
            1: "Fruits",
            2: "Vegetables",
            3: "Dairy",
            4: "Snacks",
            5: "Beverages"
        }
        category = category_map[choice]

        while True:
            print(CYAN + f"\n--- 🛒 Browse {category} ---" + RESET)
            for key, value in products[category].items():
                print(f"  {key}. {value[0]} — ₹{value[1]}")
            print("  0. ⬅️ Back to Main Menu")

            try:
                p = int(input(YELLOW + "Choose Product Number: " + RESET))
            except ValueError:
                print(RED + "❌ Invalid input! Please enter a valid product number." + RESET)
                continue

            if p == 0:
                break

            if p in products[category]:
                name, price = products[category][p]
                
                try:
                    qty = int(input(YELLOW + f"Enter Quantity for {name}: " + RESET))
                    if qty <= 0:
                        print(RED + "❌ Quantity must be at least 1!" + RESET)
                        continue
                except ValueError:
                    print(RED + "❌ Invalid quantity! Please enter a numeric value." + RESET)
                    continue

                cart.append((name, qty, price))
                print(GREEN + f"✅ Added {qty}x {name} to your cart successfully!" + RESET)

            else:
                print(RED + "❌ Invalid Product Number! Please check the list." + RESET)

    else:
        print(RED + "❌ Invalid Choice! Please choose between 1 and 7." + RESET)