import tkinter as tk
from PIL import Image
import os
import subprocess
import datetime
import webbrowser

# Create the main window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y coordinates for the window to be centered
x = int((screen_width/2) - (800/2))  # replace 800 with your window width
y = int((screen_height/2) - (600/2))  # replace 600 with your window height

# set the position of the window
root.geometry(f"800x650+{x}+{y-50}")
root.config(bg="#1C1C1E")
root.title("C0MP.INVESTS")

# Define the title and description
title_label = tk.Label(root, text="C0MP.INVESTS")
title_label.config(font=("Segoe UI Light", 36), fg="#FFFFFF", bg="#1C1C1E")
title_label.pack(pady=5)

description_label = tk.Label(
    root, text="C0MP.INVESTS OFFICIAL CS:GO INVESTMENTS TRACKER TOOL!")
description_label.config(font=("Segoe UI", 16), fg="#FFFFFF", bg="#1C1C1E")
description_label.pack(pady=50)

# Define the three buttons


def update_prices():
    filename = 'Script.py'
    subprocess.call(['python', filename])


update_prices_button = tk.Button(
    root, text="Update Prices", command=update_prices)
update_prices_button.config(font=("Segoe UI", 11), fg="#FFFFFF",
                            bg="#FF9500", activebackground="#E57F00", bd=0, pady=3, padx=0, width=30, height=2)
update_prices_button.pack(pady=20)


def check_last_price_record(directory):
    today = datetime.datetime.today()

    # Loop through files in directory and find the closest date to today
    closest_date = None
    closest_date_diff = None
    date_format = '%Y-%m-%d'
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_date_str = filename.split('[')[-1].split(']')[0]
            file_date = datetime.datetime.strptime(file_date_str, date_format)
            diff = abs(today - file_date).days
            if closest_date is None or diff < closest_date_diff:
                closest_date = file_date
                closest_date_diff = diff

    # Open the file with the closest date to today
    if closest_date is not None:
        filename = f"{directory}[{closest_date.strftime('%Y-%m-%d')}].txt"
        subprocess.call(["notepad.exe", filename])
    else:
        print(f"No text files found in the {directory} directory")


def check_last_price_record_steam():
    check_last_price_record("Steam/")


def check_last_price_record_normal():
    check_last_price_record("Statistics/")


check_last_price_record_steam_button = tk.Button(
    root, text="Open Steam Text", command=check_last_price_record_steam)
check_last_price_record_steam_button.config(font=(
    "Segoe UI", 11), fg="#FFFFFF", bg="#FF9500", activebackground="#168542", bd=0, pady=3, padx=20, width=25, height=2)
check_last_price_record_steam_button.pack(pady=20)


check_last_price_record_button = tk.Button(
    root, text="Check last Price Record", command=check_last_price_record_normal)
check_last_price_record_button.config(font=(
    "Segoe UI", 11), fg="#FFFFFF", bg="#FF9500", activebackground="#168542", bd=0, pady=3, padx=20, width=25, height=2)
check_last_price_record_button.pack(pady=20)


def open_link(event):
    webbrowser.open_new(
        "https://chrome.google.com/webstore/detail/steam-inventory-helper/cmeakgjggjdlcpncigglobpjbkabhmjl")


def open_info_window():
    # Create the info window
    info_window = tk.Toplevel(root)
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (800 // 2)
    y = (screen_height // 2) - (600 // 2)

    # Set the position and size of the window
    info_window.geometry(f"800x600+{x}+{y}")
    info_window.config(bg="#1C1C1E")
    info_window.title("Information")

    # Add a description and image to the info window
    info_description_label = tk.Label(
        info_window, text="""This application was made by Samuel Sampaio to\n track his CS:GO investments in a automatated and efficient way\n
    this app doesn't uses STEAM API and is completly client sided. No \ndata is being saved online! This app is only possible due to: """)
    info_description_label.config(
        font=("Segoe UI", 16), fg="#FFFFFF", bg="#1C1C1E")
    info_description_label.pack(pady=40)

    steam_inventory_helper_label = tk.Label(
        info_window, text="STEAM INVENTORY HELPER")
    steam_inventory_helper_label.config(
        font=("Segoe UI", 16), fg="#007AFF", bg="#1C1C1E", cursor="hand2")
    steam_inventory_helper_label.pack(pady=10)
    steam_inventory_helper_label.bind("<Button-1>", open_link)


info_button = tk.Button(root, text="Information", command=open_info_window)
info_button.config(font=("Segoe UI", 11), fg="#FFFFFF", bg="#007AFF",
                   activebackground="#0062CC", bd=0, pady=3, padx=20, width=25, height=2)
info_button.pack(pady=20)

# Run the main loop
root.mainloop()
