import tkinter as tk
from tkinter import ttk


class SearchableComboBox:
    """A ListBox class that provides a searchable dropdown list."""
    def __init__(self, entry_widget, options):
        self.options = options  # List of options for the dropdown
        self.entry = entry_widget  # External Entry widget to display dropdown
        
        # Bind the Entry widget to filter and display the dropdown
        self.entry.bind("<KeyRelease>", self.on_entry_key)  # Filter options as keys are pressed
        self.entry.bind("<FocusIn>", self.show_dropdown)  # Show dropdown when entry is focused

        # Create Listbox as a dropdown
        self.listbox = tk.Listbox(self.entry.master, height=5, width=30)  # Place dropdown in the same parent widget
        self.listbox.bind("<<ListboxSelect>>", self.on_select)  # Selects the chosen option from the dropdown
        self.listbox.bind("<FocusOut>", self.hide_dropdown)  # Hide dropdown when focus is lost

        # Populate listbox initially with all options
        for option in self.options:
            self.listbox.insert(tk.END, option)

    def on_entry_key(self, event):
        """Filter options based on typed input and update dropdown list."""
        typed_value = self.entry.get().strip().lower()  # Get and normalize input text
        self.listbox.delete(0, tk.END)  # Clear previous options

        if not typed_value:  # Show all options if no input
            for option in self.options:
                self.listbox.insert(tk.END, option)
        else:
            # Filter options starting with the typed input
            filtered_options = [option for option in self.options if option.lower().startswith(typed_value)]
            for option in filtered_options:
                self.listbox.insert(tk.END, option)  # Populate listbox with filtered options

        self.show_dropdown()  # Ensure dropdown is visible with updated options

    def on_select(self, event):
        """Set the selected option in the entry widget and hide the dropdown."""
        selected_index = self.listbox.curselection()
        if selected_index:  # If an option was selected
            selected_option = self.listbox.get(selected_index)  # Get selected option
            self.entry.delete(0, tk.END)  # Clear current entry text
            self.entry.insert(0, selected_option)  # Insert selected option into entry
        self.hide_dropdown()  # Hide dropdown after selecting an option

    def show_dropdown(self, event=None):
        """Display the dropdown list just below the entry widget."""
        self.listbox.place(in_=self.entry, x=0, rely=1, relwidth=1.0, anchor="nw")  # Position listbox below entry
        self.listbox.lift()  # Bring listbox to the front

    def hide_dropdown(self, event=None):
        """Hide the dropdown list."""
        self.listbox.place_forget()  # Remove listbox from display


class BudgetApp:
    """Main application class for the Budget Manager."""
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Manager")
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.main_screen()  # Display main screen

    def main_screen(self):
        """Screen for adding a new expense with a dropdown for categories."""
        self.clear_frame(self.main_frame)  # Clear any existing widgets in main frame

        # Options list for the dropdown
        options = [
            "Apple", "Apricot", "Avocado", "Artichoke",                # A
            "Banana", "Blueberry", "Blackberry", "Broccoli",           # B
            "Cherry", "Cantaloupe", "Carrot", "Cucumber",              # C
            "Date", "Durian", "Daikon", "Dill",                        # D
            "Eggplant", "Elderberry", "Endive", "Escarole",            # E
            "Fig", "Fennel", "Feijoa", "French Bean",                  # F
            "Grapes", "Gooseberry", "Garlic", "Ginger",                # G
            "Honeydew", "Habanero", "Horseradish", "Huckleberry",      # H
            "Indian Fig", "Iceberg Lettuce", "Italian Plum", "Ivy Gourd", # I
            "Jackfruit", "Jalapeno", "Jicama", "Juneberry",            # J
            "Kale", "Kiwi", "Kumquat", "Kohlrabi",                     # K
            "Lemon", "Lime", "Lychee", "Leek",                         # L
            "Mango", "Melon", "Mulberry", "Mushroom",                  # M
            "Nectarine", "Nance", "Napa Cabbage", "New Zealand Spinach", # N
            "Orange", "Olive", "Onion", "Oca",                         # O
            "Papaya", "Peach", "Pineapple", "Pear",                    # P
            "Quince", "Queen Anne Cherry", "Quandong", "Quinoa Greens", # Q
            "Raspberry", "Radish", "Rambutan", "Red Cabbage",          # R
            "Strawberry", "Starfruit", "Spinach", "Squash",            # S
            "Tomato", "Tangerine", "Turnip", "Tamarind",               # T
            "Ugli Fruit", "Ube", "Ulluco", "Umbrella Fruit",           # U
            "Vidalia Onion", "Vanilla Bean", "Velvet Apple", "Vine Tomato", # V
            "Watermelon", "Winter Squash", "Wax Apple", "Wild Leek",   # W
            "Xigua", "Ximenia", "Xylocarp", "Xanthan Gum Fruit",       # X
            "Yellow Pepper", "Yam", "Yuzu", "Yellow Watermelon",       # Y
            "Zucchini", "Ziziphus Fruit", "Zig-Zag Vine Fruit", "Zapote" # Z
        ]

        # Create entry field for expense name
        expense_name_var = tk.Entry(self.main_frame)  # Entry box for typing expense name
        expense_name_var.grid(row=1, column=0, pady=50)  # Position entry box

        # Create SearchableComboBox with the external entry widget
        SearchableComboBox(expense_name_var, options)  # Initialize dropdown with options

        # Create entry field for expense name
        expense_name_var1 = tk.Entry(self.main_frame)  # Entry box for typing expense name
        expense_name_var1.grid(row=4, column=0, pady=50)  # Position entry box

        options3 = ["Toyota Corolla", "Honda Civic", "Ford Mustang", 
        "Chevrolet Camaro", "BMW 3 Series", "Mercedes-Benz C-Class", 
        "Audi A4", "Tesla Model 3", "Nissan Altima", "Hyundai Elantra", 
        "Subaru Outback", "Jeep Wrangler", "Kia Soul", "Volkswagen Golf", 
        "Mazda CX-5", "Volvo XC40", "Lexus RX 350", "Porsche 911", 
        "Chevrolet Silverado", "Ford F-150"]

        # Create SearchableComboBox with the external entry widget
        SearchableComboBox(expense_name_var1, options3)  # Initialize dropdown with options

        options2 = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra", "Kangaroo", "Panda",
         "Koala", "Penguin", "Dolphin", "Whale", "Eagle", "Wolf", "Bear", "Fox", "Rabbit",
          "Deer", "Horse", "Camel", "Cheetah"]


        # Create entry field for expense name
        expense_name_var3 = tk.Entry(self.main_frame)  # Entry box for typing expense name
        expense_name_var3.grid(row=7, column=0, pady=50)  # Position entry box

        # Create SearchableComboBox with the external entry widget
        SearchableComboBox(expense_name_var3, options2)  # Initialize dropdown with options

    def clear_frame(self, frame):
        """Clear all widgets from a frame."""
        for widget in frame.winfo_children():
            widget.destroy()  # Destroy each widget in the frame


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Budget Manager")
    root.geometry("800x600")  # Set the window size to 800x600
    root.resizable(True, True)  # Allow resizing

    app = BudgetApp(root)
    root.mainloop()
