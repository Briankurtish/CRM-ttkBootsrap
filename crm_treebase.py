import tkinter as tk
import ttkbootstrap as ttk
import sqlite3

def on_menu_item_selected(option):
    print(f"Menu item selected: {option}")

root = ttk.Window(themename="superhero")
root.title("CRM Treeview TTkBootstrap")
root.geometry("1050x550")

#Create sample data
# data = [
#     ["Brain", "Cipher", 1, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 2, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 3, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 4, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 5, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 6, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 7, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 8, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 9, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 10, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 11, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 12, "123 Texas St", "California", "Famagusta", 52621],
#     ["Brain", "Cipher", 13, "123 Oklahoma St", "Texas", "Famagusta", 99450],
#     ["Logan", "Paul", 14, "123 Vegas St", "Las Vegas", "Vegas", 12389],
#     ["Derrick", "Hans", 15, "54 Nevada St", "Nevada", "Texas", 34672],
#     ["Curry", "Jones", 16, "123 Texas St", "California", "Famagusta", 52621],
# ]

#Database Section

#Create a database or connect to one that already exists
conn = sqlite3.connect('crm_tree.db')

#Create a cursor instance 
c = conn.cursor()

#Create Table
c.execute(""" 
          CREATE TABLE if not exists customers (
              first_name text,
              last_name text,
              id integer,
              address text,
              city text,
              state text,
              zipcode text)
          """)


#Add dummy data to table
# for record in data:
#     c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :state, :zipcode)",
              
#                {
#                 'first_name': record[0],
#                 'last_name': record[1],
#                 'id': record[2],
#                 'address': record[3],
#                 'city': record[4],
#                 'state': record[5],
#                 'zipcode': record[6],

#               }
              
#               )


#Commit the changes
conn.commit()

#Close the connection
conn.close()


#Query database

def query_database():
    #Create a database or connect to one that already exists
    conn = sqlite3.connect('crm_tree.db')

    #Create a cursor instance 
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers ")
    records = c.fetchall()
    
    #Add our data to the screen
    global count
    count = 0

    for record in records: 
        if count % 2 == 0: 
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('oddrow'))
        count += 1
        
    #Commit the changes
    conn.commit()

    #Close the connection
    conn.close()



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





#create record label frame
data_frame = ttk.Labelframe(root, text="Record",  bootstyle="info")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = ttk.Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = ttk.Entry(data_frame, bootstyle="info")
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = ttk.Label(data_frame, text="Last Name")
ln_label.grid(row=1, column=0, padx=10, pady=10)
ln_entry = ttk.Entry(data_frame, bootstyle="info")
ln_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = ttk.Label(data_frame, text="ID")
id_label.grid(row=0, column=2, padx=10, pady=10)
id_entry = ttk.Entry(data_frame, bootstyle="info")
id_entry.grid(row=0, column=3, padx=10, pady=10)

address_label = ttk.Label(data_frame, text="Address")
address_label.grid(row=1, column=2, padx=10, pady=10)
address_entry = ttk.Entry(data_frame, bootstyle="info")
address_entry.grid(row=1, column=3, padx=10, pady=10)

city_label = ttk.Label(data_frame, text="City")
city_label.grid(row=0, column=4, padx=10, pady=10)
city_entry = ttk.Entry(data_frame, bootstyle="info")
city_entry.grid(row=0, column=5, padx=10, pady=10)

state_label = ttk.Label(data_frame, text="State")
state_label.grid(row=1, column=4, padx=10, pady=10)
state_entry = ttk.Entry(data_frame, bootstyle="info")
state_entry.grid(row=1, column=5, padx=10, pady=10)

zip_label = ttk.Label(data_frame, text="ZipCode")
zip_label.grid(row=1, column=6, padx=10, pady=10)
zip_entry = ttk.Entry(data_frame, bootstyle="info")
zip_entry.grid(row=1, column=7, padx=10, pady=10)

#create search label frame
search_frame = ttk.Labelframe(root, text="Search by Last Name",  bootstyle="info")
search_frame.pack(fill="x", expand="yes", padx=20)

search_label = ttk.Label(search_frame, text="Search Value")
search_label.grid(row=0, column=0, padx=10, pady=10)

search_entry = ttk.Entry(search_frame, bootstyle="secondary")
search_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = ttk.Button(search_frame, text='Search Database', bootstyle="success")
search_button.grid(row=0, column=2,  padx=10, pady=10)

refresh_button = ttk.Button(search_frame, text='Refresh Database', bootstyle="secondary")
refresh_button.grid(row=0, column=3,  padx=10, pady=10)



#Move row up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

#Move row up
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

#Select Record Method

def select_record(e):
    #clear entry boxes
    fn_entry.delete(0, "end")
    ln_entry.delete(0, "end")
    id_entry.delete(0, "end")
    address_entry.delete(0, "end")
    city_entry.delete(0, "end")
    state_entry.delete(0, "end")
    zip_entry.delete(0, "end")
    
    #Grab record number 
    selected = my_tree.focus()
    
    #Grab record values
    values = my_tree.item(selected, 'values')
    
        # Outputs to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    state_entry.insert(0, values[5])
    zip_entry.insert(0, values[6])
    

#Clear Entries
def clear_entries():
     #clear entry boxes
    fn_entry.delete(0, "end")
    ln_entry.delete(0, "end")
    id_entry.delete(0, "end")
    address_entry.delete(0, "end")
    city_entry.delete(0, "end")
    state_entry.delete(0, "end")
    zip_entry.delete(0, "end")



#Create Button Frame
button_frame = ttk.Labelframe(root, text="Commands", bootstyle="info")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = ttk.Button(button_frame, text="Update Record", bootstyle="primary")
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = ttk.Button(button_frame, text="Add Record", bootstyle="success")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = ttk.Button(button_frame, text="Remove All Records", bootstyle="danger")
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = ttk.Button(button_frame, text="Remove One Selected", bootstyle="warning")
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = ttk.Button(button_frame, text="Remove Selected", bootstyle="warning")
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = ttk.Button(button_frame, text="Move Up", bootstyle="info", command= up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = ttk.Button(button_frame, text="Move Down", bootstyle="info", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = ttk.Button(button_frame, text="Clear Entries", command = clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

#Bind Treeview
my_tree.bind("<ButtonRelease-1>", select_record)


query_database()

root.mainloop()
