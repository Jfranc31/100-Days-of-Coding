from tkinter import *
FONT = ("Arial", 20, "bold")


def calculate_km():
    """
    Calculate how many km are in the amount of miles given by user.
    """
    miles = Input.get()
    km = int(miles) * 1.609344
    km_value_label.config(text=str(round(km, 1)))


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

km_value_label = Label(text="0", font=FONT)
km_value_label.grid(column=1, row=1)

# Entry
Input = Entry(width=10)
Input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()
