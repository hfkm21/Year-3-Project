from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import numpy as np
import pdfplumber
import yake
from extractionMethod import yake_extraction
import wikipedia

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
    # print(f.name)  # printing file path required for extraction

    # extracting/mining all text information in the pdf to text
    all_text = ''
    with pdfplumber.open(f.name) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # print(text)
            all_text += '\n' + text
    # print(all_text)  # working text mined successfully and printing in the terminal
    return all_text


# text preprocessing - create a branch first to test out different preprocessing methods
# , remember to commit and finally select or merge the branch with the final choice to the master and delete
# the development branch
# refer back to the yake paper
# https://www.kdnuggets.com/2019/04/text-preprocessing-nlp-machine-learning.html
# https://www.sciencedirect.com/science/article/abs/pii/S0020025519308588

def normalise():
    # extracting using yake- using upload file which returns the mined pdf text
    txt = upload_file()
    normalized_txt = txt.lower()
    return normalized_txt


text = normalise()
# print(text)


# # trying to get most frequent words and use the as stopwords
# doesn't work scrap it
# def most_frequent_words(txt):
#     split_it = txt.split()
#     Count = Counter(split_it)
#     freq = Count.most_common()
#     return freq
#
#
# stopwords = most_frequent_words(text)
# print(stopwords)
#
#
# def cleaned(stpw):
#     split_it = text.split()
#     cleaned_txt = [x for x in split_it if x in stpw not in split_it]
#     return cleaned_txt
#
#
# cleaned_text = cleaned(stopwords)

# after text processing is done  then do the core stuff, ways to improve the extraction, refer back to the
# yake paper, definitions on Wikipedia, highlighting occurrence etc
# yake_extraction(text)

# t = yake_extraction(text)
# print(t)


# getting definitions of words from wikipedia
# types of approaches that can be ued:
# use the links in the glossary
# only provide keywords with definitions provided
# use wiki trick to give definition for every word
# long phrase give link for each word
# changing the extracted phrases to a list or a dictionary
key_phrases_plus_score = yake_extraction(text)


# print(yake_extraction(text))

# the wikipedia api does not work for definitions because of disambiguation of some words use naive bayes classifier
# for retaining sentence(s) where the phrase is mentioned and by that you are likely to get the definition of a phrase
# use machine learning to do something similar as naive bayes classifier or better
# or use whats been discussed for next week meeting by julie

def definitions(extracted_phrases_plus_values):
    key_phrase_list = [tup[0] for tup in extracted_phrases_plus_values]
    print(key_phrase_list)
    print(wikipedia.summary(key_phrase_list[9]) + "\n")
    # for key_phrase in key_phrase_list:
    #     if len(key_phrase) == 3:
    #         print(wikipedia.summary(key_phrase) + "\n")

    return key_phrase_list


definitions(key_phrases_plus_score)
# print(wikipedia.summary("elon musk") + "\n")


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
