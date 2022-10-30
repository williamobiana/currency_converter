# pip install tkinter
import tkinter as tk
from tkinter import *
import tkinter.messagebox

########## GUI config ##########
#create a GUI window with a title bar, close button
root = tk.Tk() 

#define title name
root.title("Currency Converter:Swapper") 

#define the frame and grid
Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

#define the label and grid
headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Currency Converter: Swapper', bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

#create global varaiables
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

#initialize the variable
variable1.set("currency")
variable2.set("currency")


####### Define Conversion Functions ####### 
#define function to perform a conversion
def RealTimeCurrencyConversion():
    #import the currencyRate function from the forex_python.converter module
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    #get the value of the variables
    from_currency = variable1.get()
    to_currency = variable2.get()

    #define conditions for an empty field
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency from menu.")
    else:
        amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amt = float(f"{amt:.4f}")
        Amount2_field.insert(0, str(new_amt))

#define function to reset
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


########## GUI label and padding ##########
#currency list
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

#create a background colour and size
root.configure(background='#e6e5e5')
root.geometry("700x400")

#define the labels and grid
Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

#text: amount text on row 2
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount:  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

#text: from currency on row 3
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency:  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

#text: to currency on row 4
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency:  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

#text: converted amount on row 8
label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount:  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

#padding on row 5
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

#padding on row 7
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)


########## GUI main function ##########
#create option menu
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

#create the grid on row 3 and row 4
FromCurrency_option.grid(row=3, column=1, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=1, ipadx=45, sticky=E)

#create amount field and grid for row 2 and row 8
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=1, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=1, ipadx=31, sticky=E)

#create a convert button and grid on row 6
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white", command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=1)

#padding on row 9
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

#create a clear_all button and grid on row 10
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white", command=clear_all)
Label_9.grid(row=10, column=1)


#launch converter GUI
root.mainloop()





