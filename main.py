from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    passw_e.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_e.get()
    email = email_e.get()
    password = passw_e.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty", title="Warning!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it okay to save?")

        if is_ok:
            with open("data.text", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_e.delete(0, END)
                passw_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row= 0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1, sticky="w")

email_l = Label(text="Email / Username:")
email_l.grid(column=0, row=2, sticky="w")

passw_l = Label(text="Password:")
passw_l.grid(column=0, row=3, sticky="w")

website_e = Entry(width=35)
website_e.focus()
website_e.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)

email_e = Entry(width=35)
email_e.insert(0, "your.email@email.com")
email_e.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)

passw_e = Entry(width=21)
passw_e.grid(column=1, row=3, sticky="ew", padx=5, pady=5)

gen_passw_b = Button(text="Generate Password", width=14, border=1, command=generate_password)
gen_passw_b.grid(column=2, row=3, sticky="w")

add_b = Button(text="Add", width=34, border=1, command=save)
add_b.grid(column=1, row=4, columnspan=2, sticky="we")


window.mainloop()