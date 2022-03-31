from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import numpy as np
import pdfplumber
import yake
from extractionMethod import key_phrase_extraction
import nltk
from nltk.corpus import stopwords


import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import pdfplumber
from extractionMethod import key_phrase_extraction
import tkinter.scrolledtext as scrolledtext

root = Tk()

# the window fits the screen of the user window
# width, height = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry('%dx%d+0+0' % (width, height))
# root.resizable(True, True)

root.geometry('1000x1110')
root.resizable(1, 1)

# UI options
paddings = {'padx': 5, 'pady': 5}

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)


txt_edit = scrolledtext.ScrolledText(root, undo=True, bd=5, width=130, height=150, relief="flat")
txt_edit['font'] = ('consolas', '14')

txt_edit.insert(tk.END, "Welcome Floyd")
txt_edit.config(state='disabled')
txt_edit.pack(expand=True, fill='both')
txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)

# # function to open and upload the pdf file soon after creating the app window
# def upload_file():
#     # capture the file path to use for key phrase extraction after its uploaded using a variable
#     filetypes = [('Pdf files', '*.pdf'), ("All Files", "*.*")]
#     filename = filedialog.askopenfilename(filetypes=filetypes)
#     # ttk.Button(frm, text="Upload Pdf File", command=f).grid(column=1, row=0)
#     # print(filename.title())  # printing file path required for extraction
#
#     # extracting/mining all text information in the pdf to text
#     all_text = ''
#     with pdfplumber.open(filename.title()) as pdf:
#         for pdf_page in pdf.pages:
#             pdf_page_text = pdf_page.extract_text()
#             # print(text)
#             # case normalisation of text
#             all_text += '\n' + pdf_page_text.lower()
#     return all_text
#
#
# # get text from the uploaded pdf doc
# doc_text = upload_file()
# print(doc_text)
#
# # left hand buttons and grid pos
# btn_exit = ttk.Button(root, text="Exit", command=root.quit)
# btn_exit.pack()
# btn_exit.grid(row=0, column=0, sticky=tk.W, **paddings)
#
# btn_upload = ttk.Button(root, text="Upload file:", style='TButton', command=upload_file)
# btn_upload.pack()
# btn_upload.grid(row=1, column=0, sticky=tk.W, **paddings)
stops = set(stopwords.words('english'))
print(stops)

root.mainloop()

#  gcd algorithm
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# # prints the greatest common divisor(gcd)/highest common factor(hcf)/Euclidean Algorithm/Euclid's Algorithm
# print("The gcd of 3 and 12 is : ", end="")
# print(gcd(3, 12))
