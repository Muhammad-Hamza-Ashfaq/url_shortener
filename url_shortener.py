# CodexCue Python Internship -- Project-2__URL_SHORTENER
# Muhammad Hamza Ashfaq -- h.ashfaq16@gmail.com

import pyshorteners
import tkinter as tk
from tkinter import messagebox

class URLShortener:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("500x200+400+100")
        
        # URL Entry
        tk.Label(root, text="Enter URL to shorten:", font=('Arial', 12)).pack(pady=10)
        self.url_entry = tk.Entry(root, width=50, font=('Arial', 12))
        self.url_entry.pack(pady=5)
        
        # Shorten Button
        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url, 
                                     font=('Arial', 12), bg='blue', fg='white')
        self.shorten_button.pack(pady=10)
        
        # Result Label
        self.short_url_label = tk.Label(root, text="", font=('Arial', 12), fg='blue', cursor="hand2")
        self.short_url_label.pack(pady=5)
        self.short_url_label.bind("<Button-1>", self.copy_to_clipboard)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, bg="green", fg="white", font=("Arial", 12))
        self.reset_button.pack(pady=2)
    
    def reset(self):
        self.url_entry.delete(0, tk.END)
        self.short_url_label.config(text="")
    
    def shorten_url(self):
        long_url = self.url_entry.get().strip()
        if not long_url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        try:
            # Validate URL format
            if not (long_url.startswith('http://') or long_url.startswith('https://')):
                long_url = 'https://' + long_url
                
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)
            self.short_url_label.config(text=short_url)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")
    
    def copy_to_clipboard(self, event):
        short_url = self.short_url_label.cget("text")
        if short_url:
            self.root.clipboard_clear()  # Clear clipboard first
            self.root.clipboard_append(short_url)  # Add fresh URL
            self.root.update()  # Keep the clipboard after window closes
            messagebox.showinfo("Copied", "Short URL copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortener(root)
    root.mainloop()

   # Test Email-1 : https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program 
   # Test Email-2 : https://realpython.com/python-gui-tkinter/