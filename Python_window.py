from tkinter import *
import webbrowser, sys

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# function searches for query in specified browser
# *args is here because otherwise
# root.bind('<Return>', callback) wouldn't work (bind passes args to function)
def callback(*args):
    if sys.argv[1]:
        print(sys.argv[1])
    query = E1.get()
    if query:
        query = query.replace(' ', '+')
        query = 'https://duckduckgo.com/?t=ffab&q=' + query
        webbrowser.open(query, new=2)
    elif sys.argv[1]:
        query = sys.argv[1]
        query = query.replace(' ', '+')
        query = 'https://duckduckgo.com/?t=ffab&q=' + query
        webbrowser.open(query, new=2)
    else:
        L2.config(text='Enter query')

# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")


#this adds text field
L1 = Label(root, text="Query")
L1.grid(row=0, column=0)
#this informs about empty query
L2 = Label(root, text="")
L2.grid(row=1,column=0)
#search field
E1 = Entry(root, bd=5)
E1.grid(row=0, column=1)

#this searches on "Enter" keyboard click
root.bind('<Return>', callback)
#this searches on "Submit" button click
MyButton1 = Button(root, text="Submit", width=10, command=callback)
MyButton1.grid(row=1, column=1)


# show window
root.mainloop()



#https://stackoverflow.com/questions/25427347/how-to-install-and-use-tkdnd-with-python-tkinter-on-osx