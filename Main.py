from tkinter import *
from passlib.hash import pbkdf2_sha256

# Placeholder function for database connection
def connect_to_database():
    # Replace this with your database connection logic
    return True  # Placeholder return value

def is_valid_login(username, password):
    # Replace this with actual database lookup and password comparison
    # using pbkdf2_sha256.verify()
    stored_hashed_password = "placeholder_hashed_password"  # Replace with actual hash
    return pbkdf2_sha256.verify(password, stored_hashed_password)

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if is_valid_login(username, password):
        # Open admin or user panel based on user type
        # TODO: implement this part based on logic
        show_message("Login successful!")
    else:
        show_error_message("Invalid credentials")

def signup_user():
    # Open signup page
    # TODO: implement this part to open your sig page
    show_message("Signup page not implemented yet.")

def show_message(message):
    messagebox.showinfo("Message", message)

def show_error_message(error):
    messagebox.showerror("Error", error)

root = Tk()
root.title("Store Stock Management")

# Create a canvas for the purple gradient background
canvas = Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Define the gradient colors
start_color = "#E6E6FA"
end_color = "#C6C4FD"

# Create the gradient effect
for i in range(canvas.winfo_width()):
    ratio = i / (canvas.winfo_width() - 1)
    color = blend_colors(start_color, end_color, ratio)
    canvas.create_line(i, 0, i, canvas.winfo_height(), fill=color)

# Login page elements
username_label = Label(root, text="Username:", font=("Arial", 12))
username_entry = Entry(root, font=("Arial", 12))

password_label = Label(root, text="Password:", font=("Arial", 12))
password_entry = Entry(root, font=("Arial", 12), show="*")

login_button = Button(root, text="Login", font=("Arial", 12), command=login_user)
signup_button = Button(root, text="Sign Up", font=("Arial", 12), command=signup_user)

# Arrange and style login elements
username_label.place(relx=0.3, rely=0.2, anchor=CENTER)
username_entry.place(relx=0.5, rely=0.2, anchor=CENTER, width=200)

password_label.place(relx=0.3, rely=0.35, anchor=CENTER)
password_entry.place(relx=0.5, rely=0.35, anchor=CENTER, width=200)

login_button.place(relx=0.4, rely=0.5, anchor=CENTER)
signup_button.place(relx=0.6, rely=0.5, anchor=CENTER)

# Signup page elements (replace with your signup form)
# signup_username_label = Label(root, text="Username:", font=("Arial", 12))
# signup_username_entry = Entry(root, font=("Arial", 12))
# signup_password_label = Label(root, text="Password:", font=("Arial", 12))
# signup_password_entry = Entry(root, font=("Arial", 12), show="*")
# signup_button = Button(root, text="Sign Up", font=("Arial", 12), command=signup_user)

# Function to blend colors for the gradient
def blend_colors(color1, color2, ratio):
    r1, g1, b1 = tuple(int(color1.lstrip('#'), 16) for i
