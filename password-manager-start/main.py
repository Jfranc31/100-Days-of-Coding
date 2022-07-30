from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Creates a password with a combination of letters, symbols, and numbers and shuffles it. Puts it on the password
    bar.
    """
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    generated_password = "".join(password_list)

    password_input.insert(index=0, string=generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Takes the inputs for the website and saves it into a json file. If the file was not already made, the function makes
    the file.
    """
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# -------------------------- FIND PASSWORD ----------------------------- #
def find_password():
    """
    Takes input from the website search bar and checks if it's in the json file. If it is, shows the email and password
    used for that website. If the file does not exist, it makes the file, and if the website is not saved, then it tells
    the user the website does not have info for it.
    """
    find_website = website_input.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if find_website in data:
            messagebox.showinfo(title=find_website, message=f'Email: {data[find_website]["email"]}\n '
                                                            f'Password: {data[find_website]["password"]}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {find_website} exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, 'davidfranco923@gmail.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text='Generate Password', command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text='Search', width=14, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
