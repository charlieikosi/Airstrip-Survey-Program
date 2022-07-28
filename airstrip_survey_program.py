"""Airstrip Survey Program
   Author: Charlie Arua Ikosi
   Date: 22nd 10 2021
"""


import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import pandas as pd
from pathlib import Path
from tkinter import *
import os
import sys
#import openpyxl
import csv


MAIN_LIST = []
AIRSTRIP_DICTIONARY = {}


def print_code():
    """Function that takes the text input of code from the GUI"""
    code_input = code_text.get()
    return code_input

    
def print_airstrip():
    """Function that takes the text input of airstrip from the GUI"""    
    airstrip_input = airstrip_text.get()
    return airstrip_input


def print_striptype():
    """Function that takes the text input strip type from the GUI"""    
    striptype_input = striptype_text.get()
    return striptype_input
   

def print_latitude():
    """Function that takes the text input latitude from the GUI"""    
    latitude_input = latitude_text.get()
    return latitude_input


def print_longitude():
    """Function that takes the text input longitude from the GUI"""    
    longitude_input = longitude_text.get()
    return longitude_input


def print_elevation():
    """Function that takes the text input elevation from the GUI"""    
    elevation_input = elevation_text.get()
    return elevation_input


def print_district():
    """Function that takes the text input district from the GUI""" 
    district_input = district_text.get()
    return district_input


def print_province():
    """Function that takes the text input province from the GUI""" 
    province_input = province_text.get()
    return province_input


code_list =[]
airstrip_list = []
strip_list = []
latitude_list = []
longitude_list = []
elevation_list = []
district_list = []
province_list = []
def get_inputs():
    """Function that takes all the inputs from the GUI and then creates a dictionary 
    list of tuples for airstrips"""
    code = print_code()
    code_list.append(code)
    airstrip = print_airstrip()
    airstrip_list.append(airstrip)
    strip = print_striptype()
    strip_list.append(strip)
    latitude = print_latitude()
    latitude_list.append(latitude)
    longitude = print_longitude()
    longitude_list.append(longitude)
    elevation = print_elevation()
    elevation_list.append(elevation)
    district = print_district()
    district_list.append(district)
    province = print_province()
    province_list.append(province)
    dic1 = ("Code", code_list)
    dic2 = ("Airstrip Name", airstrip_list)
    dic3 = ("Strip Type", strip_list)
    dic4 = ("Latitude", latitude_list)
    dic5 = ("Longitude", longitude_list)
    dic6 = ("Elevation", elevation_list)
    dic8 = ("District", district_list)
    dic7 = ("Province", province_list)
    alls = dic1, dic2, dic3, dic4, dic5, dic6, dic8, dic7
    airstrip_dictionary = dict(alls)
    return airstrip_dictionary


def make_dataframe():
    """Function that takes the dictionary and creates a dataframe"""
    dictionary = get_inputs()
    df = pd.DataFrame(dictionary,columns=['Code','Airstrip Name','Strip Type',
                                          'Latitude','Longitude','Elevation',
                                          'District','Province'])
    clear_inputs()
    return df


def clear_inputs():
    airstrip_entry.delete(0, tk.END)
    code_entry.delete(0, tk.END)
    province_entry.delete(0, tk.END)
    latitude_entry.delete(0, tk.END)
    elevation_entry.delete(0, tk.END)
    longitude_entry.delete(0, tk.END)
    district_entry.delete(0, tk.END)
    striptype_entry.delete(0, tk.END)
 
        
def exportexcel():
    """Create a Pandas excel writer using XLSXwriter  as the negine"""
    excelwriter = pd.ExcelWriter(r"G:/UC/Course/COSC480/PROGRAMS/cosc480/aiports.xlxs")
    df = make_dataframe()
    df.to_excel(excelwriter,sheet_name="Analysis")
    excelwriter.save()
    excelwriter.close()

    messagebox.showinfo("Excel Export","Export completed")
    
    
def exportcsv():
    """Function that creates a csv file"""
    airports = make_dataframe()
    airports.to_csv("G:\\UC\\Course\\COSC480\\PROGRAMS\\cosc480\\aiports.csv")

    messagebox.showinfo("CSV Export","Export completed")
    
    
# main window settings
window = tk.Tk() 
window.title("Airstrip Survey")
window.geometry("450x450") # sets the dimensions of the GUI window



# Input-Airstrip ICAO / IATA code
code_text = StringVar()
code_label = tk.Label(master=window, text="Code:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
code_label.grid(row=0, column=0)
code_entry = tk.Entry(master=window, width = 40, textvariable=code_text)
code_entry.grid(row=0, column=1)


# Input-Airstrip Name
airstrip_text = StringVar()
airstrip_label = tk.Label(master=window, text="Airstrip Name:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
airstrip_label.grid(row=1, column=0)
airstrip_entry = tk.Entry(master=window, width = 40, textvariable=airstrip_text)
airstrip_entry.grid(row=1, column=1)


# Input-Strip Type
striptype_text = StringVar()
striptype_label = tk.Label(master=window, text="Strip Type:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
striptype_label.grid(row=2, column=0)
striptype_entry = tk.Entry(master=window, width = 40, textvariable=striptype_text)
striptype_entry.grid(row=2, column=1)


# Input-Latitude
latitude_text = StringVar()
latitude_label = tk.Label(master=window, text="Latitude:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
latitude_label.grid(row=3, column=0)
latitude_entry = tk.Entry(master=window, width = 40, textvariable=latitude_text)
latitude_entry.grid(row=3, column=1)


# Input-Longitude
longitude_text = StringVar()
longitude_label = tk.Label(master=window, text="Longitude:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
longitude_label.grid(row=4, column=0)
longitude_entry = tk.Entry(master=window, width = 40, textvariable=longitude_text)
longitude_entry.grid(row=4, column=1)


# Input-Elevation
elevation_text = StringVar()
elevation_label = tk.Label(master=window, text="Elevation:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
elevation_label.grid(row=5, column=0)
elevation_entry = tk.Entry(master=window, width = 40, textvariable=elevation_text)
elevation_entry.grid(row=5, column=1)


# Input-District
district_text = StringVar()
district_label = tk.Label(master=window, text="District:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
district_label.grid(row=6, column=0)
district_entry = tk.Entry(master=window, width = 40, textvariable=district_text)
district_entry.grid(row=6, column=1)


# Input-Province
province_text = StringVar()
province_label = tk.Label(master=window, text="Province:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10)
province_label.grid(row=7, column=0)
province_entry = tk.Entry(master=window, width = 40, textvariable=province_text)
province_entry.grid(row=7, column=1)


# Button 1-Add
add_button = tk.Button(master=window, text="Add", width=36, command=make_dataframe)
add_button.grid(row=8, column=1)


# Button 2-Export Excel
add_button = tk.Button(master=window, text="Export to Excel", width=36, command=exportexcel)
add_button.grid(row=9, column=1)


# Button 3 - Export to CSV
add_button = tk.Button(master=window, text="Export to CSV", width=36, command=exportcsv)
add_button.grid(row=10, column=1)


# run the program
window.mainloop()