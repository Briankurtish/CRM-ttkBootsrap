import tkinter as tk
import ttkbootstrap as ttk

def on_menu_item_selected(option):
    print(f"Menu item selected: {option}")

root = ttk.Window(themename="superhero")
root.title("CRM Treeview TTkBootstrap")
root.geometry("1000x550")

# Set the ttkbootstrap theme to 'superhero'
style = ttk.Style()
style.theme_use('superhero')

# Define a custom style for the Menubutton
style.configure('Custom.TMenubutton', foreground='white')

# buttonbar
buttonbar = ttk.Frame(root, style='primary.TFrame')
buttonbar.pack(fill=tk.X, pady=1, side=tk.TOP)

# Menubutton in the button bar with the custom style
options_menu = ttk.Menubutton(buttonbar, bootstyle="outline", text="Options", style='Custom.TMenubutton')
options_menu.pack(side=tk.LEFT, padx=(10, 5), pady=5)

# Create a Menu widget for the Menubutton
options_menu_menu = ttk.Menu(options_menu)

# Add menu items to the Menu widget
options_menu_menu.add_command(label="Primary Color", command=lambda: on_menu_item_selected("Option 1"))
options_menu_menu.add_command(label="Secondary Color", command=lambda: on_menu_item_selected("Option 2"))
options_menu_menu.add_command(label="Highlight Color", command=lambda: on_menu_item_selected("Option 3"))
options_menu_menu.add_separator()
options_menu_menu.add_command(label="Reset Colors", command=())
options_menu_menu.add_separator()
options_menu_menu.add_command(label="Exit", command=root.quit)

# Assign the Menu widget to the Menubutton
options_menu["menu"] = options_menu_menu

search_menu = ttk.Menubutton(buttonbar, bootstyle="outline", text="Search", style='Custom.TMenubutton')
search_menu.pack(side=tk.LEFT, padx=(10, 5), pady=5)

# Create a Menu widget for the Menubutton
search_menu_menu = ttk.Menu(search_menu)

# Add menu items to the Menu widget
search_menu_menu.add_command(label="Search", command=lambda: on_menu_item_selected("Search Option 1"))
search_menu_menu.add_separator()
search_menu_menu.add_command(label="Reset Table", command=lambda: on_menu_item_selected("Search Option 2"))

# Assign the Menu widget to the Menubutton
search_menu["menu"] = search_menu_menu


# Treeview
tree_frame = ttk.Frame(root)
tree_frame.pack(fill=tk.BOTH)

#Create a treeview Scrollbar
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side='right', fill='y')


#Define columns for the treeview

columns = ("First Name", "Last Name", "ID", "Address", "City", "State", "ZipCode")

# Create a Treeview widget
my_tree = ttk.Treeview(tree_frame, bootstyle="primary", columns=columns, show="headings")
my_tree.pack(fill="both", padx=20, pady=20)  # Adjust pack options to occupy more space

#Configure the scrollbar
tree_scroll.config(command= my_tree.yview)




# Define Headings
my_tree.heading("#0", text="")
my_tree.heading("First Name", text="First Name")
my_tree.heading("Last Name", text="Last Name")
my_tree.heading("ID", text="ID")
my_tree.heading("Address", text="Address")
my_tree.heading("City", text="City")
my_tree.heading("State", text="State")
my_tree.heading("ZipCode", text="ZipCode")

# Set the column widths
my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column("First Name", width=100)
my_tree.column("Last Name", width=100)
my_tree.column("ID", width=50)
my_tree.column("Address", width=150)
my_tree.column("City", width=100)
my_tree.column("State", width=100)
my_tree.column("ZipCode", width=100)



#Create sample data
data = [
    ["Brain", "Cipher", 1, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 2, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 3, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 4, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 5, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 6, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 7, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 8, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 9, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 10, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 11, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 12, "123 Texas St", "California", "Famagusta", 52621],
    ["Brain", "Cipher", 13, "123 Oklahoma St", "Texas", "Famagusta", 99450],
    ["Logan", "Paul", 14, "123 Vegas St", "Las Vegas", "Vegas", 12389],
    ["Derrick", "Hans", 15, "54 Nevada St", "Nevada", "Texas", 34672],
    ["Curry", "Jones", 16, "123 Texas St", "California", "Famagusta", 52621],
]


#Add our data to the screen
global count
count = 0

for record in data: 
    if count % 2 == 0: 
        my_tree.insert(parent='', index='end', iid= count, text='', value=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('evenrow'))
    else:
         my_tree.insert(parent='', index='end', iid= count, text='', value=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('oddrow'))
    #increment the counter
    count += 1



root.mainloop()
