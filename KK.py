import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

# Daily specials for the University Tuck Shop
daily_specials = {
    "Monday": [("Rajma/Curry Rice", 35), ("Dahi Tikki", 20), ("Dahi Papri/Chat Papri", 20)],
    "Tuesday": [("Chana Kulcha", 25), ("Chana Samosa", 27), ("Paneer Tikka", 45)],
    "Wednesday": [("Rajma/Curry Rice", 35), ("Spring Roll", 8), ("Potato Finger", 18)],
    "Thursday": [("Idli Sambhar", 25), ("Dosa Sambhar", 32), ("Vada Sambhar", 25), ("Chilli Potato", 25),("Sandwich", 17),
    ("Burger", 30),("Aloo Pattie", 16),("Paneer Pattie", 25), ("Chocolate", 20),("Lays", 20), ("Kurkure", 20), ("Maza/Appy", 10),
    ("Small Can", 21), ("Big Can", 34),("Veg Chowmein", 22),("Masala Pasta", 26),("Fried Rice", 18),("Egg Fried Rice", 28),("Bread Omelette", 22),
    ("Boiled Egg", 9),("Bun Samosa", 21),("Samosa", 10),("Egg Chowmein", 30),("Bun Omelette", 26),("Kitchen Tea", 10),
    ("Tea Bag Tea", 10),("Hot Coffee", 12),("Cardamom Tea", 13),
    ("Lemon Tea", 11)],
    "Friday": [("Chana Samosa", 27), ("Veg. Cutlet", 18), ("Aloo Bonda", 8),("Sandwich", 17),
    ("Burger", 30),("Aloo Pattie", 16),("Paneer Pattie", 25), ("Chocolate", 20),("Lays", 20), ("Kurkure", 20), ("Maza/Appy", 10),
    ("Small Can", 21), ("Big Can", 34),("Veg Chowmein", 22),("Masala Pasta", 26),("Fried Rice", 18),("Egg Fried Rice", 28),("Bread Omelette", 22),
    ("Boiled Egg", 9),("Bun Samosa", 21),("Samosa", 10),("Egg Chowmein", 30),("Bun Omelette", 26),("Kitchen Tea", 10),
    ("Tea Bag Tea", 10),("Hot Coffee", 12),("Cardamom Tea", 13),
    ("Lemon Tea", 11)],
    "Saturday": [("Aloo Paratha", 15), ("Paneer Paratha", 25), ("Potato Roll", 18), ("Bread Pakora", 11)],
    "Sunday": [("Bread Roll", 10), ("Pav Bhaji", 35), ("Veg Momos", 16)],
}

# Cart to store selected items
cart = []

# Function to update the cart dynamically
def update_cart(cart_label, total_label):
    cart_text = "Cart:\n" + "\n".join(f"{item} - Rs. {price}" for item, price in cart)
    cart_label.config(text=cart_text)
    
    # Calculate the total price
    total_price = sum(price for item, price in cart)
    total_label.config(text=f"Total: Rs. {total_price}")

# Function to add items to the cart
def add_to_cart(item, price, cart_label, total_label):
    cart.append((item, price))
    update_cart(cart_label, total_label)

# Function to open the University Tuck Shop screen with a scrollbar
def open_tuck_shop_screen(shop_name, img_path):
    shop_window = tk.Toplevel()
    shop_window.title(f"{shop_name} - Details")
    shop_window.geometry("800x600")
    shop_window.state('zoomed')
    shop_window.config(bg="white")

    # Title
    title_label = tk.Label(shop_window, text=shop_name, font=("Helvetica", 48), bg="#FFCCCB", fg="black")
    title_label.pack(fill="both", pady=20)

    # Main frame to organize image and items
    main_frame = tk.Frame(shop_window, bg="white")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Left frame for the image
    left_frame = tk.Frame(main_frame, bg="white")
    left_frame.pack(side="left", padx=20)

    # Display the image
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(left_frame, image=img, bg="white")
        img_label.image = img
        img_label.pack()
    except Exception as e:
        error_label = tk.Label(left_frame, text=f"Error loading image: {e}", bg="white", fg="red", font=("Helvetica", 16))
        error_label.pack()

    # Right frame for items and cart
    right_frame = tk.Frame(main_frame, bg="white")
    right_frame.pack(side="left", padx=50)

    if shop_name == "University Tuck Shop":
        # Scrollable canvas setup
        canvas = tk.Canvas(right_frame, bg="white", highlightthickness=0)
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        # Link canvas and scrollable frame
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display daily specials dynamically for the University Tuck Shop
        today = datetime.datetime.now().strftime("%A")
        specials = daily_specials.get(today, [])

        items_label = tk.Label(scrollable_frame, text=f"Specials for {today}", font=("Helvetica", 24), bg="white", fg="black")
        items_label.pack(pady=10)

        # Cart display
        cart_label = tk.Label(shop_window, text="Cart:\n", font=("Helvetica", 14), bg="white", justify="left")
        cart_label.pack(side="right", padx=10, pady=10)

        # Total price display
        total_label = tk.Label(shop_window, text="Total: Rs. 0", font=("Helvetica", 14), bg="white", justify="left")
        total_label.pack(side="right", padx=10, pady=10)

        # Display the daily specials for today
        for item, price in specials:
            item_button = tk.Button(
                scrollable_frame, text=f"{item} - Rs. {price}", font=("Helvetica", 16),
                bg="lightblue", command=lambda item=item, price=price: add_to_cart(item, price, cart_label, total_label), width=25
            )
            item_button.pack(pady=5)
        
        

        # Daily Menu heading without bold
        daily_menu_label = tk.Label(scrollable_frame, text="Daily Menu", font=("Helvetica", 24), bg="white", fg="black")
        daily_menu_label.pack(pady=20)

        # Add Aloo Sandwich item to the Daily Menu
        aloo_sandwich_button = tk.Button(
            scrollable_frame, text="Aloo Sandwich - Rs. 30", font=("Helvetica", 16),
            bg="lightblue", command=lambda: add_to_cart("Aloo Sandwich", 30, cart_label, total_label), width=25
        )
        aloo_sandwich_button.pack(pady=5)

        # Scanner Frame (Add scanner image)
        scanner_frame = tk.Frame(right_frame, bg="white")
        scanner_frame.pack(pady=20)

        scanner_label = tk.Label(scanner_frame, text="Scanner", font=("Helvetica", 24), bg="white", fg="black")
        scanner_label.pack(pady=10)

        try:
            # Add the scanner image
            scanner_image_path = r"C:\Users\Mayuri Kansal\Desktop\Pyhton\scanner.jpg"  # Change path if needed
            scanner_image = Image.open(scanner_image_path)
            scanner_image = scanner_image.resize((200, 200))  # Adjust size as needed
            scanner_image = ImageTk.PhotoImage(scanner_image)
            scanner_img_label = tk.Label(scanner_frame, image=scanner_image, bg="white")
            scanner_img_label.image = scanner_image
            scanner_img_label.pack(pady=10)
        except Exception as e:
            scanner_error_label = tk.Label(scanner_frame, text=f"Error loading scanner image: {e}", bg="white", fg="red", font=("Helvetica", 16))
            scanner_error_label.pack()
            

    # Back button to close the shop window (it doesn't return to the main screen)
    back_button = tk.Button(shop_window, text="Close", command=shop_window.destroy, bg="lightgreen", font=("Helvetica", 16))
    back_button.pack(pady=20)

# Function to open the second screen
def open_second_screen():
    second_window = tk.Toplevel()
    second_window.title("Tuck Shop App - Details")
    second_window.geometry("800x600")
    second_window.state('zoomed')
    second_window.config(bg="white")

    # Title
    title_label = tk.Label(second_window, text="TUCK SHOP", font=("Helvetica", 72), bg="#ADD8E6", fg="black")
    title_label.pack(fill="both", pady=50)

    # Frame for buttons to select Tuck Shops
    shop_buttons_frame = tk.Frame(second_window, bg="white")
    shop_buttons_frame.pack(pady=50)

    # Image paths
    image_paths = [
        r"C:\Users\Mayuri Kansal\Desktop\Pyhton\uni.jpg",
        r"C:\Users\Mayuri Kansal\Desktop\Pyhton\acads.jpg",
        r"C:\Users\Mayuri Kansal\Desktop\Pyhton\geeta.jpg"
    ]

    # Buttons for tuck shops
    university_button = tk.Button(shop_buttons_frame, text="University Tuck Shop",
                                   command=lambda: open_tuck_shop_screen("University Tuck Shop", image_paths[0]),
                                   bg="lightgreen", font=("Helvetica", 16), height=3, width=25)
    acads_button = tk.Button(shop_buttons_frame, text="Acads Tuck Shop",
                              command=lambda: open_tuck_shop_screen("Acads Tuck Shop", image_paths[1]),
                              bg="lightgreen", font=("Helvetica", 16), height=3, width=25)
    geeta_button = tk.Button(shop_buttons_frame, text="Geeta Tuck Shop",
                              command=lambda: open_tuck_shop_screen("Geeta Tuck Shop", image_paths[2]),
                              bg="lightgreen", font=("Helvetica", 16), height=3, width=25)

    university_button.grid(row=0, column=0, padx=10, pady=10)
    acads_button.grid(row=0, column=1, padx=10, pady=10)
    geeta_button.grid(row=0, column=2, padx=10, pady=10)

    # Frame for images below buttons
    image_frame = tk.Frame(second_window, bg="white")
    image_frame.pack(pady=50)

    for i, img_path in enumerate(image_paths):
        try:
            img = Image.open(img_path)
            img = img.resize((400, 300))
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(image_frame, image=img, bg="white")
            img_label.image = img
            img_label.grid(row=0, column=i, padx=10, pady=10)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

# Main Screen
root = tk.Tk()
root.title("Tuck Shop App")
root.geometry("800x600")
root.state('zoomed')
root.config(bg="#A7D8D9")

# Header Label
header_label = tk.Label(root, text="TUCK SHOP", font=("Helvetica", 48, "bold"), bg="#E6E6FA", fg="black")
header_label.pack(fill="both", expand=True)
header_label.bind("<Button-1>", lambda e: open_second_screen())

# Frame to hold images on the main screen
image_frame = tk.Frame(root, bg="#A7D8D9")
image_frame.pack(pady=10)

main_image_paths = [
    r"C:\Users\Mayuri Kansal\Desktop\Pyhton\image1.jpg",
    r"C:\Users\Mayuri Kansal\Desktop\Pyhton\image2.jpg",
    r"C:\Users\Mayuri Kansal\Desktop\Pyhton\image3.jpg",
    r"C:\Users\Mayuri Kansal\Desktop\Pyhton\image4.jpg"
]

for i, img_path in enumerate(main_image_paths):
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)
        row = i // 2
        col = i % 2
        img_label = tk.Label(image_frame, image=img, bg="#A7D8D9")
        img_label.image = img
        img_label.grid(row=row, column=col, padx=10, pady=10)
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")

# Acads and Geeta menus
acads_menu = [
    ("Sandwich", 17),
    ("Burger", 30),
    ("Aloo Pattie", 16),
    ("Paneer Pattie", 25),
    ("Chocolate", 20),
    ("Lays", 20),
    ("Kurkure", 20),
    ("Maza/Appy", 10),
    ("Small Can", 21),
    ("Big Can", 34),
    ("Kitchen Tea", 10),
    ("Tea Bag Tea", 10),
    ("Hot Coffee", 12),
    ("Cardamom Tea", 13),
    ("Lemon Tea", 11),
]
geeta_menu = [
    ("Sandwich", 17),
    ("Burger", 30),
    ("Aloo Pattie", 16),
    ("Paneer Pattie", 25),
    ("Chocolate", 20),
    ("Lays", 20),
    ("Kurkure", 20),
    ("Maza/Appy", 10),
    ("Small Can", 21),
    ("Big Can", 34),
    ("Kitchen Tea", 10),
    ("Tea Bag Tea", 10),
    ("Hot Coffee", 12),
    ("Cardamom Tea", 13),
    ("Lemon Tea", 11),
]

# Function to open the University Tuck Shop, Acads, or Geeta Tuck Shop screen
def open_tuck_shop_screen(shop_name, img_path):
    shop_window = tk.Toplevel()
    shop_window.title(f"{shop_name} - Details")
    shop_window.geometry("800x600")
    shop_window.state('zoomed')
    shop_window.config(bg="white")

    # Title
    title_label = tk.Label(shop_window, text=shop_name, font=("Helvetica", 48), bg="#FFCCCB", fg="black")
    title_label.pack(fill="both", pady=20)

    # Main frame to organize image and items
    main_frame = tk.Frame(shop_window, bg="white")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Left frame for the image
    left_frame = tk.Frame(main_frame, bg="white")
    left_frame.pack(side="left", padx=20)

    # Display the image
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(left_frame, image=img, bg="white")
        img_label.image = img
        img_label.pack()
    except Exception as e:
        error_label = tk.Label(left_frame, text=f"Error loading image: {e}", bg="white", fg="red", font=("Helvetica", 16))
        error_label.pack()

    # Right frame for items and cart
    right_frame = tk.Frame(main_frame, bg="white")
    right_frame.pack(side="left", padx=50)

    # Scrollable frame setup
    canvas = tk.Canvas(right_frame, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    # Link canvas and scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Cart display
    cart_label = tk.Label(shop_window, text="Cart:\n", font=("Helvetica", 14), bg="white", justify="left")
    cart_label.pack(side="right", padx=10, pady=10)

    # Total price display
    total_label = tk.Label(shop_window, text="Total: Rs. 0", font=("Helvetica", 14), bg="white", justify="left")
    total_label.pack(side="right", padx=10, pady=10)

    # Dynamically populate items based on the shop name
    if shop_name == "University Tuck Shop":
        today = datetime.datetime.now().strftime("%A")
        specials = daily_specials.get(today, [])
        items_label = tk.Label(scrollable_frame, text=f"Specials for {today}", font=("Helvetica", 24), bg="white", fg="black")
        items_label.pack(pady=10)
        menu_items = specials
    elif shop_name == "Acads Tuck Shop":
        menu_items = acads_menu
    elif shop_name == "Geeta Tuck Shop":
        menu_items = geeta_menu

    # Display menu items
    for item, price in menu_items:
        item_button = tk.Button(
            scrollable_frame, text=f"{item} - Rs. {price}", font=("Helvetica", 16),
            bg="lightblue", command=lambda item=item, price=price: add_to_cart(item, price, cart_label, total_label),
            width=25
        )
        item_button.pack(pady=5)

    # Back button to close the shop window
    back_button = tk.Button(shop_window, text="Close", command=shop_window.destroy, bg="lightgreen", font=("Helvetica", 16))
    back_button.pack(pady=20)
    # Function to open the University Tuck Shop, Acads, or Geeta Tuck Shop screen
def open_tuck_shop_screen(shop_name, img_path):
    shop_window = tk.Toplevel()
    shop_window.title(f"{shop_name} - Details")
    shop_window.geometry("800x600")
    shop_window.state('zoomed')
    shop_window.config(bg="white")

    # Title
    title_label = tk.Label(shop_window, text=shop_name, font=("Helvetica", 48), bg="#FFCCCB", fg="black")
    title_label.pack(fill="both", pady=20)

    # Main frame to organize image and items
    main_frame = tk.Frame(shop_window, bg="white")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Left frame for the image
    left_frame = tk.Frame(main_frame, bg="white")
    left_frame.pack(side="left", padx=20)

    # Display the image
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(left_frame, image=img, bg="white")
        img_label.image = img
        img_label.pack()
    except Exception as e:
        error_label = tk.Label(left_frame, text=f"Error loading image: {e}", bg="white", fg="red", font=("Helvetica", 16))
        error_label.pack()

    # Right frame for items and cart
    right_frame = tk.Frame(main_frame, bg="white")
    right_frame.pack(side="left", padx=50)

    # Scrollable frame setup
    canvas = tk.Canvas(right_frame, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    # Link canvas and scrollable frame
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Cart display
    cart_label = tk.Label(shop_window, text="Cart:\n", font=("Helvetica", 14), bg="white", justify="left")
    cart_label.pack(side="right", padx=10, pady=10)

    # Total price display
    total_label = tk.Label(shop_window, text="Total: Rs. 0", font=("Helvetica", 14), bg="white", justify="left")
    total_label.pack(side="right", padx=10, pady=10)

    # Dynamically populate items based on the shop name
    if shop_name == "University Tuck Shop":
        today = datetime.datetime.now().strftime("%A")
        specials = daily_specials.get(today, [])
        items_label = tk.Label(scrollable_frame, text=f"Specials for {today}", font=("Helvetica", 24), bg="white", fg="black")
        items_label.pack(pady=10)
        menu_items = specials
    elif shop_name == "Acads Tuck Shop":
        menu_items = acads_menu
    elif shop_name == "Geeta Tuck Shop":
        menu_items = geeta_menu

    # Display menu items
    for item, price in menu_items:
        item_button = tk.Button(
            scrollable_frame, text=f"{item} - Rs. {price}", font=("Helvetica", 16),
            bg="lightblue", command=lambda item=item, price=price: add_to_cart(item, price, cart_label, total_label),
            width=25
        )
        item_button.pack(pady=5)

    # Add scanner image to the right of the scrollable area (Common for all shops)
    scanner_frame = tk.Frame(right_frame, bg="white")
    scanner_frame.pack(pady=20)

    scanner_label = tk.Label(scanner_frame, text="Scanner", font=("Helvetica", 24), bg="white", fg="black")
    scanner_label.pack(pady=10)

    try:
        # Add the scanner image
        scanner_image_path = r"C:\Users\Mayuri Kansal\Desktop\Pyhton\scanner.jpg"  # Change path if needed
        scanner_image = Image.open(scanner_image_path)
        scanner_image = scanner_image.resize((200, 200))  # Adjust size as needed
        scanner_image = ImageTk.PhotoImage(scanner_image)
        scanner_img_label = tk.Label(scanner_frame, image=scanner_image, bg="white")
        scanner_img_label.image = scanner_image
        scanner_img_label.pack(pady=10)
    except Exception as e:
        scanner_error_label = tk.Label(scanner_frame, text=f"Error loading scanner image: {e}", bg="white", fg="red", font=("Helvetica", 16))
        scanner_error_label.pack()

    # Back button to close the shop window
    back_button = tk.Button(shop_window, text="Close", command=shop_window.destroy, bg="lightgreen", font=("Helvetica", 16))
    back_button.pack(pady=20)



root.mainloop()