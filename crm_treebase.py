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

root.mainloop()
