from load_trucks import *
from options import *

# def main():
#     print("Welcome to WGUPS!!")
#     print("1. Print Total Mileage")
#     print("2. Get All Packages at a single time.")
#     print("3. Get A Specific package at a single time.")
#     print("4. Exit the Program")

#     #Continuous loop to display menu, breaks once user enters 4.
#     #O(n^2) due to case 2 and case 3 containing O(n) functions.
#     while True:
#         try:
#             i = int(input("Please enter one of the following options [1,2,3,4]: "))
#             match i:
#                 case 1:    # precautionary measure
#                     print(f'Total distance traveled is {lt.get_total_distance():.2f} miles.\n')
#                 case 2:
#                     time = input('Enter time in (HH:MM:SS) format: ')
#                     # get_all_packages(lt.hm, time)
#                     options.get_all_packages(time)
#                     break
#                 case 3:
#                     id = int(input('Enter package ID: '))
#                     time = input('Enter time in (HH:MM:SS) format: ')
#                     # get_single_package(lt.hm, id,time)
#                     options.get_single_package(id,time)
#                     break
#                 case 4:
#                     print('Have a good day.')
#                     break

#         except:
#             print('Invalid input, try again [main file].')
                
# if __name__ == "__main__":
#     main()


#################################################################################################


#################################################################################################

import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
# from load_trucks import get_total_distance
# from options import get_all_packages, get_single_package

class WGUPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WGUPS Delivery System")
        
        # Welcome Label
        self.welcome_label = tk.Label(root, text="Welcome to WGUPS!!", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)
        
        # Option Buttons
        self.btn_total_mileage = tk.Button(root, text="1. Print Total Mileage", command=self.show_total_mileage)
        self.btn_total_mileage.pack(pady=5)

        self.btn_all_packages = tk.Button(root, text="2. Get All Packages at a Single Time", command=self.get_all_packages)
        self.btn_all_packages.pack(pady=5)

        self.btn_single_package = tk.Button(root, text="3. Get A Specific Package at a Single Time", command=self.get_single_package)
        self.btn_single_package.pack(pady=5)

        self.btn_exit = tk.Button(root, text="4. Exit the Program", command=root.quit)
        self.btn_exit.pack(pady=5)
        
    def show_total_mileage(self):
        total_distance = lt.get_total_distance()
        messagebox.showinfo("Total Mileage", f"Total distance traveled is {total_distance:.2f} miles.")
    
    def get_all_packages(self):
        time = tk.simpledialog.askstring("Input", "Enter time in (HH:MM:SS) format:")
        if time:
            options.get_all_packages(time)  # This should print or process packages
    
    def get_single_package(self):
        package_id = tk.simpledialog.askinteger("Input", "Enter package ID:")
        time = tk.simpledialog.askstring("Input", "Enter time in (HH:MM:SS) format:")
        if package_id and time:
            options.get_single_package(package_id, time)  # This should print or process the specific package

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WGUPSApp(root)
    root.mainloop()
