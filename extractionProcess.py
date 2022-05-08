# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
#
# import foreground as foreground
# import numpy as np
# import pdfplumber
# import yake
# from extractionMethod import key_phrase_extraction
# import nltk
# from nltk.corpus import stopwords
#
# import tkinter as tk
# from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
# from tkinter import filedialog
# from tkinter import *
# from tkinter.ttk import *
# import pdfplumber
# from extractionMethod import key_phrase_extraction
# import tkinter.scrolledtext as scrolledtext
#
# root = Tk()
#
# # the window fits the screen of the user window
# # width, height = root.winfo_screenwidth(), root.winfo_screenheight()
# # root.geometry('%dx%d+0+0' % (width, height))
# # root.resizable(True, True)
#
# root.geometry('1000x1110')
# root.resizable(1, 1)
#
# # UI options
# paddings = {'padx': 5, 'pady': 5}
#
# # configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=2)
#
# txt_edit = scrolledtext.ScrolledText(root, undo=True, bd=5, width=130, height=150, relief="flat")
# txt_edit['font'] = ('consolas', '14')
# txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)
#
#
# # txt_edit.insert(tk.END, "Hey")
#
#
# def highlight_pattern(pattern, tag, start="1.0", end="end",
#                       regexp=False):
#     start = txt_edit.index(start)
#     end = txt_edit.index(end)
#     txt_edit.mark_set("matchStart", start)
#     txt_edit.mark_set("matchEnd", start)
#     txt_edit.mark_set("searchLimit", end)
#
#     count = IntVar()
#     while True:
#         index = txt_edit.search(pattern, "matchEnd", "searchLimit",
#                                 count=count, regexp=False)
#         if index == "": break
#         if count.get() == 0: break  # degenerate pattern which matches zero-length strings
#         txt_edit.mark_set("matchStart", index)
#         txt_edit.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
#         txt_edit.tag_add(tag, "matchStart", "matchEnd")
#
# #
# # text = " i love macdonalds cheese burgers and soft drinks"
# #
# # tk = word_tokenize(text)
# # print(tk)
#
#
# # similar to update but for highlighting
# def highlight():
#     # txt_edit['state'] = 'normal'
#     # txt_edit.update()
#     # txt_edit.delete(1.0, tk.END)
#     # txt_edit.update()
#     # maybe add the highlight method
#     # txt_edit.tag_add("start", "1.10", tk.END)
#     # txt_edit.tag_config("start", background="yellow", foreground="white")
#     txt_edit.insert(tk.END, "Welcome")
#     highlight_pattern("Welcome", "red")
#     # txt_edit.update()
#     # txt_edit['state'] = 'disabled'
#     # txt_edit.update()
#
#
# # highlight()
#
# def color_text(edit, tag, word, fg_color='black', bg_color='white'):
#     # add a space to the end of the word
#     word = word + " "
#     edit.insert('end', word)
#     end_index = edit.index('end')
#     begin_index = "%s-%sc" % (end_index, len(word) + 1)
#     edit.tag_add(tag, begin_index, end_index)
#     edit.tag_config(tag, foreground=fg_color, background=bg_color)
#
#
# text = "Up the hill went Jack and Jill, down fell Jill and cried!"
# # create a list of single words
# word_list = text.split()
# # create a list of single words for all text
# # print( word_list )  # test
#
# # pick word to be colored
# myword1 = 'Jack'
# myword2 = 'Jill'
# # create a list of unique tags
# tags = ["tg" + str(k) for k in range(len(word_list))]
# for ix, word in enumerate(word_list):
#     # word[:len(myword)] for word ending with a punctuation mark
#     if word[:len(myword1)] == myword1:
#         color_text(txt_edit, tags[ix], word, 'blue')
#     elif word[:len(myword2)] == myword2:
#         color_text(txt_edit, tags[ix], word, 'red', 'yellow')
#     else:
#         color_text(txt_edit, tags[ix], word)
#
# # Create a Tex Field
# # txt_edit.insert(tk.END, "Welcome Floyd")
# # txt_edit.config(state='disabled')
# # txt_edit.pack(expand=True, fill='both')
# # txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)
# # highlight_pattern(txt_edit, "Welcome Floyd", "red")
#
# # # function to open and upload the pdf file soon after creating the app window
# # def upload_file():
# #     # capture the file path to use for key phrase extraction after its uploaded using a variable
# #     filetypes = [('Pdf files', '*.pdf'), ("All Files", "*.*")]
# #     filename = filedialog.askopenfilename(filetypes=filetypes)
# #     # ttk.Button(frm, text="Upload Pdf File", command=f).grid(column=1, row=0)
# #     # print(filename.title())  # printing file path required for extraction
# #
# #     # extracting/mining all text information in the pdf to text
# #     all_text = ''
# #     with pdfplumber.open(filename.title()) as pdf:
# #         for pdf_page in pdf.pages:
# #             pdf_page_text = pdf_page.extract_text()
# #             # print(text)
# #             # case normalisation of text
# #             all_text += '\n' + pdf_page_text.lower()
# #     return all_text
# #
# #
# # # get text from the uploaded pdf doc
# # doc_text = upload_file()
# # print(doc_text)
# #
# # # left hand buttons and grid pos
# # btn_exit = ttk.Button(root, text="Exit", command=root.quit)
# # btn_exit.pack()
# # btn_exit.grid(row=0, column=0, sticky=tk.W, **paddings)
# #
# # btn_upload = ttk.Button(root, text="Upload file:", style='TButton', command=upload_file)
# # btn_upload.pack()
# # btn_upload.grid(row=1, column=0, sticky=tk.W, **paddings)
# stops = set(stopwords.words('english'))
# print(stops)
#
# root.mainloop()
#
# #  gcd algorithm
# # def gcd(a, b):
# #     if b == 0:
# #         return a
# #     else:
# #         return gcd(b, a % b)
# #
# #
# # # prints the greatest common divisor(gcd)/highest common factor(hcf)/Euclidean Algorithm/Euclid's Algorithm
# # print("The gcd of 3 and 12 is : ", end="")
# # print(gcd(3, 12))

import tkinter as tk

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


class ColorChart(tk.Frame):

    MAX_ROWS = 36
    FONT_SIZE = 10

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        r = 0
        c = 0

        for color in COLORS:
            label = tk.Label(self, text=color, bg=color,
                             font=("Times", self.FONT_SIZE, "bold"))
            label.grid(row=r, column=c, sticky="ew")
            r += 1

            if r > self.MAX_ROWS:
                r = 0
                c += 1

        self.pack(expand=1, fill="both")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Named Color Chart")
    app = ColorChart(root)
    root.mainloop()