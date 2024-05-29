#game/gui,py
import tkinter as tk
from tkinter import ttk

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Game")
        
        # Initialize light mode
        self.light_mode = True

        # Set up main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Text display box
        self.text_display = tk.Text(self.main_frame, wrap="word", state="disabled", height=15)
        self.text_display.grid(row=0, column=0, columnspan=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Input entry box
        self.entry_var = tk.StringVar()
        self.input_entry = ttk.Entry(self.main_frame, textvariable=self.entry_var)
        self.input_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.input_entry.bind("<Return>", self.process_input)
        
        # Submit button
        self.submit_button = ttk.Button(self.main_frame, text="Submit", command=self.process_input)
        self.submit_button.grid(row=1, column=1, sticky=tk.W)
        
        # Mode toggle button
        self.mode_button = ttk.Button(self.main_frame, text="Toggle Mode", command=self.toggle_mode)
        self.mode_button.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Configure scaling
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=0)
        self.main_frame.rowconfigure(2, weight=0)
        
        self.set_light_mode()

        self.input_value = None

    def process_input(self, event=None):
        input_text = self.entry_var.get()
        if input_text:
            self.display_text(f"> {input_text}")
            self.entry_var.set("")
            self.input_value = input_text
            self.root.quit()  # Stop the main loop

    def display_text(self, text):
        self.text_display.config(state="normal")
        self.text_display.insert(tk.END, text + "\n")
        self.text_display.config(state="disabled")
        self.text_display.see(tk.END)

    def toggle_mode(self):
        if self.light_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def set_light_mode(self):
        self.light_mode = True
        self.main_frame.configure(style='Light.TFrame')
        self.text_display.configure(bg="white", fg="black")
        self.input_entry.configure(style='Light.TEntry')
        self.submit_button.configure(style='Light.TButton')
        self.mode_button.configure(style='Light.TButton')

    def set_dark_mode(self):
        self.light_mode = False
        self.main_frame.configure(style='Dark.TFrame')
        self.text_display.configure(bg="black", fg="white")
        self.input_entry.configure(style='Dark.TEntry')
        self.submit_button.configure(style='Dark.TButton')
        self.mode_button.configure(style='Dark.TButton')

    def get_input(self):
        self.root.mainloop()  # Start the main loop
        input_value = self.input_value  # Store the input value
        self.input_value = None  # Reset input value
        return input_value

class GUIManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            root = tk.Tk()
            cls._instance = GameGUI(root)
        return cls._instance

def create_gui():
    return GUIManager.get_instance()

if __name__ == "__main__":
    gui = create_gui()
    gui.display_text("Welcome to the LitRPG Game!")
    while True:
        user_input = gui.get_input()
        if user_input.lower() == "exit":
            break
        gui.display_text(f"Processed input: {user_input}")
