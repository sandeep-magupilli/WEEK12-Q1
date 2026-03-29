import tkinter as tk
from tkinter import messagebox,filedialog
root=tk.Tk()
root.title("Advanced GUI App")
root.geometry("300x500")
frame=tk.Frame(root)
frame.pack()
scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
listbox=tk.Listbox(frame,yscrollcommand=scrollbar.set)
for item in ["gaming","dancing","Music","Travel","reading"]:
    listbox.insert(tk.END,item)
listbox.pack()
scrollbar.config(command=listbox.yview)
def show_msg():
    messagebox.showinfo("Greeting","Welcome sandeep!")
def open_file():
    filedialog.askopenfilename()
tk.Button(root,text="Show Greeting",command=show_msg).pack()
tk.Button(root,text="Browse File",command=open_file).pack()
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="Options",menu=file_menu)
file_menu.add_command(label="Browse",command=open_file)
file_menu.add_command(label="Quit",command=root.quit)
mb=tk.Menubutton(root,text="Settings",relief=tk.RAISED)
mb.menu=tk.Menu(mb,tearoff=0)
mb["menu"]=mb.menu
mb.menu.add_command(label="Profile")
mb.menu.add_command(label="Logout")
mb.pack()
root.mainloop()
