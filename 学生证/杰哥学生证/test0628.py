import tkinter as tk
from tkinter import filedialog

# def upload_file():
#     selectFile = tk.filedialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
#     entry1.insert(0, selectFile)
#     print(selectFile)
#
# root = tk.Tk()
#
# frm = tk.Frame(root)
# frm.grid(padx='20', pady='30')
# btn = tk.Button(frm, text='上传文件', command=upload_file)
# btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
# entry1 = tk.Entry(frm, width='40')
# entry1.grid(row=0, column=1)
#
# root.mainloop()


import tkinter as tk
from tkinter import filedialog


def upload_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if filename:
        print(f"Selected file: {filename}")
        # 这里可以添加处理上传文件的代码


root = tk.Tk()
root.title('文件上传框')
root.geometry('300x150')

upload_button = tk.Button(root, text='上传文件', command=upload_file)
upload_button.pack(expand=True)

root.mainloop()
