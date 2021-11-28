from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()

#Title of Application
window.title("Feet to Meter Converter App")

# Setting Background
window.configure(background="light green")

#Setting Geometry Height & Width
window.geometry("320x220")

#Window is not resizable
window.resizable(width=False, height=False)

#######################################
##
def convert():
    value = float(ft_entry.get())
    # 1 ft = 0.3048 m 
    meter = value * 0.3048
    mt_value .set("%.4f" % meter)

##
def clear():
    ft_value.set("")
    mt_value.set("")
    

#######################################

## Adding FEET Label
ft_lb1 = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lb1.grid(column=0,row=0,padx=15,pady=15)

## Taking value from user
ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

#####################################

## Adding METER Label
mt_lb1 = Label(window,text="Meter",bg="brown",fg="white",width=14)
mt_lb1.grid(column=0,row=1,padx=15,pady=15)

##
mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=30)
mt_entry.delete(0,"end") 

##########################################

##
convert_btn = Button(window,text="Convert",bg="blue",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)

##
clear_btn = Button(window,text="clear",bg="black", fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

window.mainloop()
