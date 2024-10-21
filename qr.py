import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from PIL import Image, ImageTk
import qrcode

# Declare the qr_img globally so it can be accessed by multiple functions
qr_img = None

def generate_qr():
    global qr_img  # Make qr_img accessible globally
    
    input_text = text_entry.get()
    if input_text.strip() == "":
        messagebox.showwarning("Input Error", "Please enter something to like.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img.thumbnail((200, 200))

    # Display QR code on the window
    img = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=img)
    qr_label.image = img

    # Enable the download button
    download_button.config(state=tk.NORMAL)

def download_qr():
    global qr_img
    if qr_img:
        qr_img.save("liked_qr_code.png")
        messagebox.showinfo("Saved", "QR Code has been saved as 'liked_qr_code.png'")
    else:
        messagebox.showerror("Error", "QR code is not generated yet.")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x500")
root.configure(bg="#2C3E50")

# Custom fonts and styles
title_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
label_font = tkFont.Font(family="Helvetica", size=12)
button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

# Title label
title_label = tk.Label(root, text="QR Code Generator", font=title_font, bg="#2C3E50", fg="white")
title_label.pack(pady=20)

# Input field label
input_label = tk.Label(root, text="Enter what you like:", font=label_font, bg="#2C3E50", fg="white")
input_label.pack(pady=10)

# Text entry field
text_entry = tk.Entry(root, width=35, font=("Arial", 12))
text_entry.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", font=button_font, bg="#E74C3C", fg="white", command=generate_qr)
generate_button.pack(pady=20)

# QR code display area
qr_label = tk.Label(root, bg="#2C3E50")
qr_label.pack(pady=10)

# Download button
download_button = tk.Button(root, text="Download QR Code", font=button_font, bg="#3498DB", fg="white", state=tk.DISABLED, command=download_qr)
download_button.pack(pady=20)

# Footer with credits
footer_label = tk.Label(root, text="Designed by Mr. Rahul Singh", font=("Arial", 10), bg="#2C3E50", fg="white")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the app
root.mainloop()
