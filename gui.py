import crypto
import tkinter as tk
from tkinter import filedialog

def settings():
    global color_bg, color_fg
    color_bg = 'black'
    color_fg = 'white'

def test():
    content = wdgt_txt.get(1.0, tk.END)
    
    wdgt_txt.insert(1.0, content)

def clear():
    wdgt_txt.delete(1.0, tk.END)


def import_text():
    file = filedialog.askopenfile(title="Select text", filetypes=(("All files",'*.*'), ("Text files",'*.txt')))
    if file is None: return
    
    txt = "".join(file.readlines())
    
    wdgt_txt.delete(1.0, tk.END)
    wdgt_txt.insert(1.0, txt)
    
    file.close()


def mirror_text(x_axis=False, y_axis=False):
    line = wdgt_txt.get(1.0, tk.END)
    text = line_to_text(line)
    
    text_mirrored = crypto.mirror(text, x_axis=x_axis, y_axis=y_axis)
    text_mirrored = '\n'.join(text_mirrored)
    
    wdgt_txt.delete(1.0, tk.END)
    wdgt_txt.insert(1.0, text_mirrored)


def get_bf_results(lb_bf):
    line = wdgt_txt.get(1.0, tk.END)
    if len(line) <= 1: return
    
    text = line_to_text(line)
    bf_res_dict = crypto.brute_force(text)
    
    lb_bf.delete(0,tk.END)
    for i, key in enumerate(bf_res_dict):
        lb_bf.insert(i, str(key) + ": " + str(bf_res_dict[key]))


def crypt(type, entry_key, k):
    line = wdgt_txt.get(1.0, tk.END)
    if len(line) <= 1: return
    text = line_to_text(line)
    
    key = entry_key.get()
    
    res = type(text, key, k)
    
    wdgt_txt2.delete(1.0, tk.END)
    wdgt_txt2.insert(1.0, res)


def setup_analyse():
    global frame
    if 'frame' in globals(): frame.destroy()
    frame = tk.Frame(root)
    
    # IC #
    lbl_IC = tk.Label(frame, text="IC: 0.0", relief='sunken')
    lbl_IC.grid(row=0, column=0, sticky='ew')
    
    # letters frequency #
    frame_freq = tk.Frame(frame)

    tk.Label(frame_freq, text="Letters frequency:").grid(row=0, column=0, columnspan=2)
    
    lb_freq = tk.Listbox(frame_freq)
    lb_freq.grid(row=1, column=0)
    
    scroll_freq = tk.Scrollbar(frame_freq, command=lb_freq.yview)
    scroll_freq.grid(row=1, column=1, sticky='ns')
    lb_freq.configure(yscrollcommand=scroll_freq.set)
    
    frame_freq.grid(row=1, column=0)
    
    # key length #
    frame_pw_len = tk.Frame(frame)
    
    tk.Label(frame_pw_len, text="Potential key length:").grid(row=0, column=0, columnspan=2)
    
    lb_pw_len = tk.Listbox(frame_pw_len)
    lb_pw_len.grid(row=1, column=0)
    
    scroll_pw_len = tk.Scrollbar(frame_pw_len, command=lb_pw_len.yview)
    scroll_pw_len.grid(row=1, column=1, sticky='ns')
    lb_pw_len.configure(yscrollcommand=scroll_pw_len.set)
    
    frame_pw_len.grid(row=2, column=0)
    
    # mirror #
    btn_mirror = tk.Button(frame, text="Mirror on X axis", command=lambda: mirror_text(x_axis=True))
    btn_mirror.grid(row=5, column=0)
    
    btn_mirror = tk.Button(frame, text="Mirror on Y axis", command=lambda: mirror_text(y_axis=True))
    btn_mirror.grid(row=6, column=0)
    
    # analyse #
    tk.Button(frame, text="Analyse", command=lambda: analyse(lbl_IC, lb_freq, lb_pw_len)).grid(row=7, column=0)
    
    frame.grid(row=0, column=1, sticky='ns')


def setup_rot():
    global frame
    frame.destroy()
    frame = tk.Frame(root)
    
    # brute force #
    frame_bf = tk.Frame(frame)

    tk.Label(frame_bf, text="Results:").grid(row=0, column=0, columnspan=2)
    
    lb_bf = tk.Listbox(frame_bf)
    lb_bf.grid(row=1, column=0)
    
    scroll_freq = tk.Scrollbar(frame_bf, command=lb_bf.yview)
    scroll_freq.grid(row=1, column=1, sticky='ns')
    lb_bf.configure(yscrollcommand=scroll_freq.set)
    
    tk.Button(frame_bf, text="Brute Force", command=lambda: get_bf_results(lb_bf)).grid(row=2, column=0, columnspan=2)
    
    frame_bf.grid(row=0, column=0, columnspan=2)
    
    # key #
    lbl_key = tk.Label(frame, text="Key:")
    lbl_key.grid(row=1, column=0)
    
    entry_key = tk.Entry(frame)
    entry_key.grid(row=1, column=1)
    
    tk.Button(frame, text="Encrypt", command=lambda: crypt(crypto.ROT, entry_key, -1)).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="Decrypt", command=lambda: crypt(crypto.ROT, entry_key, 1)).grid(row=3, column=0, columnspan=2)
    
    frame.grid(row=0, column=1, sticky='ns')


def setup_substitution():
    global frame
    frame.destroy()
    frame = tk.Frame(root)
    
    # letters frequency #
    frame_freq = tk.Frame(frame)

    tk.Label(frame_freq, text="Letters frequency:").grid(row=0, column=0, columnspan=2)
    
    lb_freq = tk.Listbox(frame_freq)
    lb_freq.grid(row=1, column=0)
    
    scroll_freq = tk.Scrollbar(frame_freq, command=lb_freq.yview)
    scroll_freq.grid(row=1, column=1, sticky='ns')
    lb_freq.configure(yscrollcommand=scroll_freq.set)
    
    tk.Button(frame_freq, text="Update", command=lambda: analyse(lb_freq=lb_freq)).grid(row=2, column=0, columnspan=2)
    
    frame_freq.grid(row=0, column=0, columnspan=2)
    
    # key #
    lbl_key = tk.Label(frame, text="Key:")
    lbl_key.grid(row=1, column=0)
    
    entry_key = tk.Entry(frame)
    entry_key.grid(row=1, column=1)
    
    tk.Button(frame, text="Encrypt", command=lambda: crypt(crypto.SUBSTITUTION, entry_key, -1)).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="Decrypt", command=lambda: crypt(crypto.SUBSTITUTION, entry_key, 1)).grid(row=3, column=0, columnspan=2)
    
    frame.grid(row=0, column=1, sticky='ns')


def setup_vigenere():
    global frame
    frame.destroy()
    frame = tk.Frame(root)
    
    # key length #
    frame_pw_len = tk.Frame(frame)
    
    tk.Label(frame_pw_len, text="Potential key length:").grid(row=0, column=0, columnspan=2)
    
    lb_pw_len = tk.Listbox(frame_pw_len)
    lb_pw_len.grid(row=1, column=0)
    
    scroll_pw_len = tk.Scrollbar(frame_pw_len, command=lb_pw_len.yview)
    scroll_pw_len.grid(row=1, column=1, sticky='ns')
    lb_pw_len.configure(yscrollcommand=scroll_pw_len.set)
    
    tk.Button(frame_pw_len, text="Update", command=lambda: analyse(lb_pw_len=lb_pw_len)).grid(row=2, column=0, columnspan=2)
    
    frame_pw_len.grid(row=0, column=0, columnspan=2)
    
    # key #
    lbl_key = tk.Label(frame, text="Key:")
    lbl_key.grid(row=1, column=0)
    
    entry_key = tk.Entry(frame)
    entry_key.grid(row=1, column=1)
    
    tk.Button(frame, text="Encrypt", command=lambda: crypt(crypto.VIGENERE, entry_key, -1)).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="Decrypt", command=lambda: crypt(crypto.VIGENERE, entry_key, 1)).grid(row=3, column=0, columnspan=2)
    
    frame.grid(row=0, column=1, sticky='ns')


def analyse(lbl_IC=None, lb_freq=None, lb_pw_len=None):
    line = wdgt_txt.get(1.0, tk.END)
    if len(line) <= 1: return
    
    pw_len_dict = crypto.pw_length(line, 2, 13)
    text = line_to_text(line)
    IC = crypto.get_IC(text)
    freq_dict = crypto.count_letters(text)
    
    if lbl_IC:
        lbl_IC.configure(text="IC: " + str(round(IC, 3)))
    
    if lb_freq:
        lb_freq.delete(0,tk.END)
        for i, key in enumerate(freq_dict):
            lb_freq.insert(i, str(key) + ": " + str(freq_dict[key]))
    
    if lb_pw_len:
        lb_pw_len.delete(0,tk.END)
        for i, key in enumerate(pw_len_dict):
            lb_pw_len.insert(i, str(key) + ": " + str(round(pw_len_dict[key], 3)))


def line_to_text(line):
    return line.split('\n')


def get_help():
    try:
        file = open('README.md')
        txt = "".join(file.readlines())
    except Exception:
        txt = "No help coming for you..."
    
    wdgt_txt2.insert(1.0, txt)


def menu():
    wdgt_mb = tk.Menu(root)

    wdgt_mb.add_command(label="Open text", command=import_text)

    mb_type = tk.Menu(wdgt_mb, tearoff=0, bg=color_bg, fg=color_fg)
    wdgt_mb.add_cascade(label="Type", menu=mb_type)

    mb_type.add_command(label="Analyse", command=setup_analyse)
    mb_type.add_separator()
    mb_type.add_command(label="ROT", command=setup_rot)
    mb_type.add_command(label="Substitution", command=setup_substitution)
    mb_type.add_command(label="Vigenere", command=setup_vigenere)

    wdgt_mb.add_command(label="Help", command=get_help)
    
    wdgt_mb.add_command(label="Exit", command=lambda: root.quit())
    return wdgt_mb


def main():
    global root, wdgt_txt, wdgt_txt2
    
    settings()
    
    root = tk.Tk()

    wdgt_txt = tk.Text(root, bg=color_bg, fg=color_fg, insertbackground=color_fg)
    wdgt_txt.grid(row=0, column=0, sticky='ns')

    setup_analyse()

    wdgt_txt2 = tk.Text(root, bg=color_bg, fg=color_fg, insertbackground=color_fg)
    wdgt_txt2.grid(row=0, column=2, sticky='ns')

    root.title("Crypto")
    root.resizable(False, False)
    root.config(menu=menu(), bg=color_bg)
    root.mainloop()

if __name__ == '__main__': main()
