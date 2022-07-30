import tkinter


def button_clicked():
    new_text = Input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50 )

# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Next Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
Input = tkinter.Entry(width=10)
Input.grid(column=3, row=2)


window.mainloop()
