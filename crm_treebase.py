import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import sqlite3

def on_menu_item_selected(option):
    print(f"Menu item selected: {option}")

root = ttk.Window(themename="superhero")
root.title("CRM Treeview TTkBootstrap")
root.geometry("1050x550")

update_message = ToastNotification(title="Notification", 
                          message= "The record has been updated in the database successfully",
                          duration=3000,
                          alert=True,
                          
                          )
add_message = ToastNotification(title="Notification", 
                          message= "The record has been added to the database successfully",
                          duration=3000,
                          alert=True,
                          
                          )

delete_message = ToastNotification(title="Notification", 
                          message= "The record has been deleted from the database successfully",
                          duration=3000,
                          alert=True,
                          
                          )

#Query database
def query_database():
    
    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    
    #Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you

    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()
    
    #Add our data to the screen
    global count
    count = 0

    for record in records: 
        if count % 2 == 0: 
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('oddrow'))
        #increment the counter
        count += 1
    
    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()
    
#Function to search the database

def search_records():
    lookup_record = search_entry.get()
    
    #Close the search box
    search.destroy()
    
    #Clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

     #Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you

    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE last_name like ?", (lookup_record,))
    records = c.fetchall()

    #Add our data to the screen
    global count
    count = 0

    for record in records: 
        if count % 2 == 0: 
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid= count, text='', value=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=('oddrow'))
        #increment the counter
        count += 1

    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()
    
def lookup_records():
    global search_entry, search
    search = ttk.Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    #Create label frame
    search_frame = ttk.LabelFrame(search, text="Last Name")
    search_frame.pack(padx=10, pady=10)

    #Add entry box
    search_entry = ttk.Entry(search_frame, font=("Helvetica", 16))
    search_entry.pack(padx=20, pady=20)

    #Add Button
    search_button = ttk.Button(search, text="Search Records", command=search_records)
    search_button.pack(padx=20, pady=20)

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
search_menu_menu.add_command(label="Search", command=lookup_records)
search_menu_menu.add_separator()
search_menu_menu.add_command(label="Reset Table", command=query_database)

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

search_button = ttk.Button(search_frame, text='Search Database', bootstyle="success", command=search_records)
search_button.grid(row=0, column=2,  padx=10, pady=10)

refresh_button = ttk.Button(search_frame, text='Refresh Database', bootstyle="secondary", command=query_database)
refresh_button.grid(row=0, column=3,  padx=10, pady=10)


#remove many records from database
def remove_many():
    
    #Add message box
    response = messagebox.askyesno("Alert!", "Are you want to delete the selected records from the table?")

    #Add logic for message box
    if response == 1:
        
        #Designate Selections
        x = my_tree.selection()

         #Create List of Ids
        ids_to_delete = []

        #Add selections to ids_to_delete
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])
            
        # Delete from TreeView
        for record in x:
            my_tree.delete(record)
        
        #delete record from database
        #Create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')

        #create a cursor instance 
        #a cursor is like a little robot which you can send to go stuffs for you
        c = conn.cursor()
        
        #Delete selected records from the database table
        c.executemany("DELETE FROM customers WHERE id = ?", [(a, ) for a in ids_to_delete])

        #reset list
        ids_to_delete = []
        
        
        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()
        
        #Show toast
        delete_message.show_toast()
        
        #Clear entry boxes
        clear_entries()



#remove table from database
def remove_all():
    
    #Add message box
    response = messagebox.askyesno("Alert!", "Are you want to delete everything from the table?")
    
    
     #Add logic for message box
    if response == 1:
        #Clear the treeview
        for record in my_tree.get_children():
            my_tree.delete(record)
        
        #delete record from database
        #Create a database or connect to one that exists
        conn = sqlite3.connect('tree_crm.db')

        #create a cursor instance 
        #a cursor is like a little robot which you can send to go stuffs for you
        c = conn.cursor()
        
        #Delete everything from the database table
        c.execute("DROP TABLE customers")
        
        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()
        
        #Show toast
        delete_message.show_toast()
        
        #Clear entry boxes
        clear_entries()
        
        create_table_again()
        


#remove one record from the database
def remove_one():
    #removing from treeview
    x  = my_tree.selection()[0]
    my_tree.delete(x)
    
    #removing from database
    #Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you
    c = conn.cursor()
    
    #Delete from database
    c.execute("DELETE from customers WHERE oid =" + id_entry.get())
    
    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()
    
    #Show toast
    delete_message.show_toast()
    
    #Clear entry boxes
    clear_entries()

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
    

#update the database
def update_record():
    #Grab the record number
    selected = my_tree.focus()
    #Update record
    my_tree.item(selected, text='', values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zip_entry.get(),))
    
    
    #update the database 
    #Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you
    c = conn.cursor()
    
    c.execute(""" 
            UPDATE customers SET
            
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid """, 
            
            {
                'first': fn_entry.get(),
                'last' : ln_entry.get(),
                'oid': id_entry.get(),
                'address': address_entry.get(),
                'city': city_entry.get(),
                'state': state_entry.get(),
                'zipcode': zip_entry.get(),
            } )
    
    
    
    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()
    
    #Show toast
    update_message.show_toast()
    
     #Clear entry boxes
    clear_entries()
    
    
    

#Add new record to database
def add_record():
    #Create a database or connect to one that exists
    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you
    c = conn.cursor()
    
     #Add new record
    c.execute("INSERT INTO customers VALUES (:first, :last, :id, :address, :city, :state, :zipcode)", 

            {
                'first': fn_entry.get(),
                'last' : ln_entry.get(),
                'id': id_entry.get(),
                'address': address_entry.get(),
                'city': city_entry.get(),
                'state': state_entry.get(),
                'zipcode': zip_entry.get(),
            }

            )


    
    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()
    
      #Clear the TreeView table
    my_tree.delete(*my_tree.get_children())

    #Refresh treeview table
    query_database()

    #show toast message
    add_message.show_toast()
    
    #clear entry boxes
    clear_entries()
    

#Create table again after deletion
def create_table_again():
    #Create a database or connect to one that exists

    conn = sqlite3.connect('tree_crm.db')

    #create a cursor instance 
    #a cursor is like a little robot which you can send to go stuffs for you

    c = conn.cursor()

    #Create a table
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

    #Commit the changes
    conn.commit()

    #Close our connection
    conn.close()

    


#Create Button Frame
button_frame = ttk.Labelframe(root, text="Commands", bootstyle="info")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = ttk.Button(button_frame, text="Update Record", bootstyle="primary", command = update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = ttk.Button(button_frame, text="Add Record", bootstyle="success", command = add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = ttk.Button(button_frame, text="Remove All Records", bootstyle="danger", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = ttk.Button(button_frame, text="Remove One Selected", bootstyle="warning", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = ttk.Button(button_frame, text="Remove Selected", bootstyle="warning", command=remove_many)
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
