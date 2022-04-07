import os
import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH, messagebox
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

import pdfplumber
import tkinter.scrolledtext as scrolledtext
from nltk.tokenize import word_tokenize

# experiment imports
import nltk

nltk.download('punkt')
nltk.download('stopwords')

import yake
import yake.StopwordsList
import RAKE

# yake hyper parameters for experiment
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.6
deduplication_algo = 'seqm'  # jaro, levs, seqm
windowSize = 3
numOfKeywords = 50

# rake hyper parameters for experiment
min_chars = 1
max_words = 3
min_freq = 1

window = tk.Tk()
# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window_width = 950
window_height = 950

# find the center point
center_x = int(width / 2 - window_width / 2)
center_y = int(height / 2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.title("Key phrase Extractor Glossary")
window.resizable(1, 1)
window.geometry('%dx%d+0+0' % (width, height))
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.configure(background='grey')
window.configure(pady=0)


# file upload function
def upload_file():
    # capture the file path to use for key phrase extraction after its uploaded using a variable
    filetypes = [('Pdf files', '*.pdf'), ("All Files", "*.*")]
    filename = filedialog.askopenfilename(filetypes=filetypes)

    # extracting/mining pdf text doc
    all_text = ''
    with pdfplumber.open(filename.title()) as pdf:
        for pdf_page in pdf.pages:
            pdf_page_text = pdf_page.extract_text()
            # case normalisation of text
            all_text += '\n' + pdf_page_text.lower() + '\n'

    # file uploading button and function
    btn_extract = ttk.Button(fr_buttons, text="Extract and Display", command=lambda: txt_edit.insert(tk.END,
                                                                                                     update_txt(
                                                                                                         key_phrase_extraction(
                                                                                                             all_text,
                                                                                                             get(var),
                                                                                                             get(slider)))))
    btn_extract.grid(row=3, column=0, **paddings2, sticky=tk.W)

    # upload button lbel
    file_name = os.path.basename(filename)
    ttk.Label(fr_buttons, text=("...") + file_name + ("...")).grid(row=0, column=1, **paddings2, sticky=tk.W)


# extracting key phrases using yake or rake
def key_phrase_extraction(extracted_text, extraction_method, key_phrase_number):
    # yake extraction process
    if extraction_method == "Algorithm1":
        y_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                            dedupFunc=deduplication_algo,
                                            windowsSize=windowSize, top=numOfKeywords,
                                            features=None)

        y_keywords = [tup[0] for tup in y_extractor.extract_keywords(extracted_text)]

        # candidate sentences selection by returning all sentences in which the key phrase is in
        y_candidate_sents_dict = {kp.title() + ":" + "\n": [s + "\n" for s in nltk.sent_tokenize(extracted_text)
                                                            if kp in s] for kp in y_keywords}

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        y_candidate_sents_dict1 = {kp: [s + "\n" + "\n" for s in nltk.sent_tokenize(extracted_text) if kp in s] for kp
                                   in y_keywords}

        # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain the
        y_phrase_and_tup_sent = [(k, v[0]) for k, v in y_candidate_sents_dict.items() if len(v) > 0]

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        y_phrase_and_tup_sent1 = [(k, v[0]) for k, v in y_candidate_sents_dict1.items() if len(v) > 0]

        ind_key_phrase_and_tup_sent = [(str(c) + "). " + tup[0], tup[1]) for c, tup in
                                       enumerate(y_phrase_and_tup_sent, 1)]

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        ind_key_phrase_and_tup_sent1 = [(tup[0], tup[1]) for c, tup in enumerate(y_phrase_and_tup_sent1, 1)]

        # update the key phrase number var before extracting
        if 0 < key_phrase_number <= 20:
            out = [item for t in ind_key_phrase_and_tup_sent[:key_phrase_number] for item in t]
            # decoy
            yk = [tup[0] for tup in ind_key_phrase_and_tup_sent1][:key_phrase_number]

            # co-occurrence button for yake
            btn_concurrence = ttk.Button(fr_buttons, text="Phrase Concurrence Display",
                                         command=lambda: high(extracted_text, yk))
            btn_concurrence.grid(row=4, column=0, **paddings2, sticky=tk.W)

            return "".join(out)
    # rake extraction process
    elif extraction_method == "Algorithm2":
        # rake extraction process
        r_extractor = RAKE.Rake(RAKE.SmartStopList())
        # decoy for getting length
        decoy_keywords = [tup[0] for tup in r_extractor.run(extracted_text, min_chars, max_words, min_freq)]
        # rake length for sort order
        l_length = len(decoy_keywords)

        # rake keywords list ordered in their order of importance
        r_keywords = [tup[0] for tup in r_extractor.run(extracted_text, min_chars, max_words, min_freq)]

        # candidate sentences selection by returning all sentences in which the key phrase is mentioned in document
        r_candidate_sents_dict = {kp.title() + ":" + "\n": [s + "\n" + "\n" for s in
                                                            nltk.sent_tokenize(extracted_text) if kp in s] for kp in
                                  r_keywords}

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        r_candidate_sents_dict1 = {kp: [s + "\n" + "\n" for s in nltk.sent_tokenize(extracted_text)
                                        if kp in s] for kp in r_keywords}

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        r_phrase_and_tup_sent1 = [(k, v[0]) for k, v in r_candidate_sents_dict1.items() if len(v) > 0]

        # then choose top1 sentence for each key phrase extracted- which is the best sentence likely to contain definition
        r_phrase_and_tup_sent = [(k, v[0]) for k, v in r_candidate_sents_dict.items() if len(v) > 0]
        ind_key_phrase_and_tup_sent = [(str(c) + ").  " + tup[0], tup[1]) for c, tup in
                                       enumerate(r_phrase_and_tup_sent, 1)]

        # decoy for highlighting and getting key phrase without new lines characters, numbers etc.
        ind_key_phrase_and_tup_sent1 = [(tup[0], tup[1]) for c, tup in enumerate(r_phrase_and_tup_sent1, 1)]
        if 0 < key_phrase_number <= 20:
            out = [item for t in ind_key_phrase_and_tup_sent[:key_phrase_number] for item in t]
            # decoy rake keywords cleaned
            rk = [tup[0] for tup in ind_key_phrase_and_tup_sent1][:key_phrase_number]
            print(rk)
            btn_concurrence = ttk.Button(fr_buttons, text="Phrase Concurrence Display", command=lambda: high(extracted_text,rk))
            btn_concurrence.grid(row=4, column=0, **paddings2, sticky=tk.W)

            return "".join(out)


# def sort_tuple(tup):
#     tup.sort(key=lambda x: x[1])
#     return tup


# the get function for getting values/strings from gui input- slider and option buttons
def get(input_variable):
    print(input_variable.get())
    return input_variable.get()


def update_txt(text):
    txt_edit['state'] = 'normal'
    txt_edit.update()
    txt_edit.delete(1.0, tk.END)
    txt_edit.update()
    txt_edit.insert(tk.END, text)
    txt_edit.update()
    txt_edit['state'] = 'disabled'
    txt_edit.update()


def color_text(tag, word, fg_color='black', bg_color='white'):
    # add a space to the end of the word
    # problem is here not including words like "query window" something to do with space
    # check the other method - highlight_pattern
    word = word + " "
    txt_edit.insert(tk.END, word)
    end_index = txt_edit.index(tk.END)
    begin_index = "%s-%sc" % (end_index, len(word) + 1)
    txt_edit.tag_add(tag, begin_index, end_index)
    txt_edit.tag_config(tag, foreground=fg_color, background=bg_color)


def color_text2(tag, word, fg_color='black', bg_color='white'):
    # add a space to the end of the word
    end_index = txt_edit.index(tk.END)
    begin_index = "%s-%sc" % (end_index, len(word) + 1)
    txt_edit.tag_add(tag, begin_index, end_index)
    txt_edit.tag_config(tag, foreground=fg_color, background=bg_color)


def high(txt, kp_list):
    txt_edit['state'] = 'normal'
    txt_edit.update()
    txt_edit.delete(1.0, tk.END)
    txt_edit.update()

    # create a list of single words and try to process it before display
    # To do:
    # try to use white space tokenizer
    # fix rake highlighter - not highlighting only yake working
    # text fixing - making bold phrases, avoiding breaking up of phrases etc
    word_list = txt.split() # word_list = txt.split()

    # create a list of unique tags
    tags = ["tg" + str(k) for k in range(len(word_list))]
    # print(tags)
    for ix, word in enumerate(word_list):
        color_text(tags[ix], word)
        for i in range(len(kp_list)):
            # word[:len(myword)] for word ending with a punctuation
            if word[:len(kp_list[i])] == kp_list[i]:
                color_text2(tags[ix], word, fg_color='black', bg_color='yellow')
            # elif word[:len(myword2)] == myword2:
            #      color_text(tags[ix], word, 'black', 'yellow')
            # else:
            #      color_text(txt_edit, tags[ix], word)
    txt_edit.update()
    txt_edit['state'] = 'disabled'
    txt_edit.update()


paddings = {'padx': 0, 'pady': 0}
paddings2 = {'padx': 5, 'pady': 20}
# # left hand side button frame padding="0.5i"
fr_buttons = ttk.Frame(window, width=20, height=100, relief=tk.RIDGE, padding="0.5i")
fr_buttons.columnconfigure(0, weight=3)
fr_buttons.columnconfigure(1, weight=1)
fr_buttons.grid(row=0, column=0, **paddings, sticky=tk.NS)

# creating text box for text display
txt_edit = scrolledtext.ScrolledText(window, undo=True, bd=5, width=80, height=100, relief=tk.RIDGE, wrap=WORD)
txt_edit['font'] = ('consolas', '10')
txt_edit.grid(row=0, column=1, **paddings, sticky=tk.NS)

# styling the frame
# ttk.Style().configure('TFrame', background='grey', foreground = 'yellow')

# styling all buttons includes 2 buttons used as labels
ttk.Style().configure("TButton", width=25, height=25, padding=5, relief=tk.FLAT, background="#ccc")

#  styling option menu
menu_style = ttk.Style()
menu_style.configure('TMenubutton', width=10, height=10, padding=0, background="#ccc")

# styling the slider
slider_style = ttk.Style()
slider_style.configure('Horizontal.TScale', width=10, height=10, padding=0, background="#ccc")

# left hand buttons and grid pos and their padding in the frame
# upload button
btn_upload = ttk.Button(fr_buttons, text="Upload file:", style='TButton', command=lambda: upload_file())
btn_upload.grid(row=0, column=0, **paddings2, sticky=tk.W)

# option menu
extraction_method_list = [".....Select.....", "Algorithm1", "Algorithm2"]
var = StringVar(window)
var.set(extraction_method_list[0])
option = ttk.OptionMenu(fr_buttons, var, *extraction_method_list)
var.trace("w", var.get())
btn_opt_label = ttk.Button(fr_buttons, text='Extraction method:', style='TButton')
btn_opt_label['state'] = 'disabled'
# btn_opt_label.grid(row=1, column=0, sticky=tk.W, **paddings2)
btn_opt_label.grid(row=1, column=0, **paddings2, sticky=tk.W)
option.grid(row=1, column=1, **paddings2, sticky=tk.W)

# slider button
btn_slider_label = ttk.Button(fr_buttons, text='key phrases number:', style='TButton')
btn_slider_label['state'] = 'disabled'
btn_slider_label.grid(row=2, column=0, **paddings2, sticky=tk.W)

slider = tk.Scale(fr_buttons, from_=1, to=20, orient='horizontal')
slider.set(10)
slider.grid(row=2, column=1, **paddings2, sticky=tk.W)

# exit button
btn_exit = ttk.Button(fr_buttons, text="Exit", command=window.quit)
btn_exit.grid(row=5, column=0, **paddings2, sticky=tk.W)

window.mainloop()

# frame arrangements
#  https://stackoverflow.com/questions/45122244/having-frames-next-to-each-other-in-tkinter
# try this as an experiment in extraction process
# https://www.pythontutorial.net/tkinter/ttk-style/
# use disabled buttons lables to make it same as other buttons
# slider.update()
# print(slider.get())
# option.update()
# print(option.get())
# errors in when selecting algorithm option
