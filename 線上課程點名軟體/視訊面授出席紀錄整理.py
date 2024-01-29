import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Nou import Record_mac as rec
from Nou import Integrate_mac as inter


def record():
    rec.process()


def integrate():
    inter.process()


root = ttk.Window(themename='flatly', title='視訊面授出席紀錄整理')
root.resizable(width=0, height=0)

record_btn = ttk.Button(root, text='出席紀錄彙整csv2xlsx', bootstyle=(PRIMARY, OUTLINE), command=record).pack(side=LEFT, padx=10, pady=15)
integrate_btn = ttk.Button(root, text='        出席紀錄統整        ', bootstyle=(PRIMARY, OUTLINE), command=integrate).pack(side=LEFT, padx=10, pady=15)

root.mainloop()

themes = ['flatly', 'sandstone']