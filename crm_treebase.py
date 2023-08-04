import tkinter as tk
import ttkbootstrap as ttk

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

# Menubutton in the button bar
options_menu = ttk.Menubutton(buttonbar, bootstyle="outline", text="Options",style='Custom.TMenubutton')
options_menu.pack(side=tk.LEFT, padx=(10, 5), pady=5)

search_menu = ttk.Menubutton(buttonbar, bootstyle="outline", text="Search", style='Custom.TMenubutton')
search_menu.pack(side=tk.LEFT, padx=(10, 5), pady=5)


root.mainloop()
