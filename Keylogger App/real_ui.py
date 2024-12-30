import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import subprocess
from datetime import datetime
import sys  # Ensure sys is imported for script running
from pynput.keyboard import Listener

# from start_stop_keylogging import on_press, on_release, write_file
# from encryption import encrypting
# from decryption import decrypting


class ScriptRunner:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Stroker: A Keylogging App")
        self.window.geometry("400x700")
        self.window.configure(bg='#323231')

        self.script_entries = []

        # Apply custom theme
        self.apply_theme()

        # iOS-inspired styling with improvements
        self.create_ios_style_ui()

    def apply_theme(self):
        """Create a custom ttk theme for rounded corners and shadows."""
        style = ttk.Style(self.window)

        # Define styles for Entry widgets
        style.configure(
            "Rounded.TEntry",
            borderwidth=0,
            padding=5,
            relief="flat",
            foreground="white",
            fieldbackground="#F0F0F3",
            background="#F0F0F3",
            lightcolor="#D9D9D9"
        )
        style.map(
            "Rounded.TEntry",
            focus=[("active", "#E0E0E0")],
        )

        # Define styles for buttons
        style.configure(
            "Modern.TButton",
            font=('SF Pro Display', 16),
            padding=8,
            relief="flat",
            background="#007AFF",
            foreground="white",
            borderwidth=0
        )
        style.map(
            "Modern.TButton",
            background=[("active", "#0056b3")],
            foreground=[("active", "white")]
        )

        # Define styles for Labels
        style.configure(
            "Modern.TLabel",
            background="black",
            foreground="white",
            font=('SF Pro Display', 16),
            anchor="w"
        )

        # Add shadows (optional)
        style.configure(
            "Modern.TFrame",
            background="black",
        )

    def create_ios_style_ui(self):
        # Main container
        main_frame = ttk.Frame(self.window, style="Modern.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Keylogger",
            font=('SF Pro Display', 34, 'bold'),
            style="Modern.TLabel"
        )
        title_label.pack(pady=(0, 30))

        # Session name
        session_frame = ttk.Frame(main_frame, style="Modern.TFrame")
        session_frame.pack(fill=tk.X, pady=(0, 20))

        session_label = ttk.Label(
            session_frame,
            text="Keylog file name",
            style="Modern.TLabel"
        )
        session_label.pack(fill=tk.X)

        self.session_entry = ttk.Entry(
            session_frame,
            style="Rounded.TEntry"
        )
        self.session_entry.pack(fill=tk.X, pady=5)

        # Button data
        button_data = [
            ("Start Keylogging", self.start_keylogging),
            ("Stop Keylogging and Encrypt File", self.stop_and_encrypt),
            ("Open and Decrypt a Keylog File", self.open_and_decrypt)
        ]

        for label_text, action in button_data:
            btn_frame = ttk.Frame(main_frame, style="Modern.TFrame")
            btn_frame.pack(fill=tk.X, pady=10)

            # Button label
            btn_label = ttk.Label(
                btn_frame,
                text=label_text,
                style="Modern.TLabel"
            )
            btn_label.pack(fill=tk.X)

            # Script path entry
            script_entry = ttk.Entry(
                btn_frame,
                style="Rounded.TEntry"
            )
            script_entry.pack(fill=tk.X, pady=(5, 10))
            self.script_entries.append(script_entry)

            # Run button
            run_btn = ttk.Button(
                btn_frame,
                text="Run",
                command=action,
                style="Modern.TButton"
            )
            run_btn.pack(fill=tk.X)

        # Log display
        log_label = ttk.Label(
            main_frame,
            text="Logs",
            style="Modern.TLabel"
        )
        log_label.pack(fill=tk.X, pady=(20, 10))

        self.log_display = tk.Text(
            main_frame,
            height=10,
            font=('SF Pro Mono', 12),
            bd=1,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightcolor='#C7C7CC',
            highlightbackground='#C7C7CC'
        )
        self.log_display.pack(fill=tk.BOTH, expand=True)

    def start_keylogging(self):
        """Logic for starting the keylogging."""
        messagebox.showinfo("Start Keylogging", "Keylogging started.")

    def stop_and_encrypt(self):
        """Logic for stopping keylogging and encrypting the file."""
        messagebox.showinfo("Stop Keylogging and Encrypt", "Keylogging stopped and file encrypted.")

    def open_and_decrypt(self):
        """Logic for opening and decrypting a keylog file."""
        messagebox.showinfo("Open and Decrypt", "Opened and decrypted the keylog file.")

    def save_log(self, log_entry):
        os.makedirs('logs', exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join('logs', f'log_{timestamp}.json')

        with open(filename, 'w') as f:
            json.dump(log_entry, f, indent=4)

    def run(self):
        self.window.mainloop()


# Run the application
if __name__ == "__main__":
    app = ScriptRunner()
    app.run()
