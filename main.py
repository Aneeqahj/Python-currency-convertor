# All the imports
from tkinter import *
import requests

# Let's start with the design of the GUI
root = Tk()
root.title("Currency Converter")
root.resizable("false", "false")
root.geometry("500x400")
root.config(bg="violet")

value = IntVar()

# Retrieving the information from an external JSON file as a source of reference
information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
# print(conversion_rate)


# Creating a label and entry for the results
value_label = Label(root, text="Value")
value_label.config(bg="violet")
value_label.pack()

value_entry = Entry(root, textvariable=value, width=40)
value_entry.config(bg="lightpink")
value_entry.pack()

# Creating the FROM (Standard value is USD)
from_label = Label(root, text="From: USD")
from_label.config(bg="violet")
from_label.pack()

# Doing the Conversion of the data with its loop
convert = Label(root, text="To:")
convert.config(bg="violet")
convert.pack()

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.pack()

convert_label = Label(root, text="Converted to: ")
convert_label.config(bg="violet")
convert_label.pack()


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans


convert_btn = Button(root, command=convert_curr, text="Convert", width=20, borderwidth=7)
convert_btn.config(bg="lightpink")
convert_btn.pack()

root.mainloop()
