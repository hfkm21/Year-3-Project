from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdfplumber
import yake
from extractionMethod import yake_extraction


root = Tk()

# the window fits the screen of the user window
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))
root.resizable(True, True)

# should be removed later on
# root.withdraw()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)


def upload_file():
    # capture the file path to use for key phrase extraction after its uploaded using a variable
    filetypes = [('Pdf files', '*.pdf')]
    f = filedialog.askopenfile(filetypes=filetypes)
    ttk.Button(frm, text="Upload Pdf File", command=f).grid(column=1, row=0)
    print(f.name)  # printing file path required for extraction


    # extracting/mining all text information in the pdf to text
    all_text = ''
    with pdfplumber.open(f.name) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # print(text)
            all_text += '\n' + text
    print(all_text)  # working text mined successfully and printing in the terminal
    return all_text


# extracting using yake- using upload file which returns the mined pdf text
yake_extraction(upload_file())
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