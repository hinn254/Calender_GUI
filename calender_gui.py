# imports
from tkinter import *
from tkinter import messagebox
import calendar

# Function that will show calender
def show__calender():
    # root initialization
    root = Tk()
    # root configs
    root.config(background='pink')
    root.title("Benny's Calender")
    root.geometry('620x620')

    try:
        # value of year obtain from entry
        year_inputted = int(year.get())

        # passing the year_value to calender module
        calendar_content = calendar.calendar(year_inputted)

        # This label will contain the calender for the year passed/requested
        calendar_year = Label(root,text=calendar_content,font='Consolas 10 bold')
        calendar_year.grid(row=5, column=1, padx=20)
    # Catch ValueError
    except ValueError:
        messagebox.showwarning("Value Error",'PLease enter an integer')

    root.mainloop()

# if program is run directly
if __name__ == '__main__':
    # initialize window and it's configs
    window = Tk()
    window.config(background='white')
    window.title('Calender')
    window.geometry('215x160')

    # label
    cal = Label(window, text='CALENDER',bg='dark gray',font='times 28 bold')
    cal.grid(row=1, column=1)

    # year_label
    year_label = Label(window, text='Enter year', bg='light green')
    year_label.grid(row=2, column=1)

    # year_entry - gets value supplied in this entry widget
    year = StringVar()
    year_field = Entry(window,textvariable=year)
    year_field.grid(row=3,column=1)

    # button - shows the calender of the year entered --calls the show_calender function
    show = Button(window, text='Show Calender', fg='black',bg='red',command=show__calender)
    show.grid(row=4, column=1)

    # terminates the program
    exit = Button(window, text='Exit', fg='Black',bg='Red',command=exit)
    exit.grid(row=6,column=1)

    window.mainloop()
