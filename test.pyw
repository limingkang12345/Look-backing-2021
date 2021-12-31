from tkinter import *
labels=['2021.1.1--新的一年开始了','2021.2.12--春节到！','2021.1.7--五上期末考试','2021.1.22--散学典礼，寒假开始','2021.2.26--新学期开始，见到郑老师','2021.5.15--天问一号着陆火星','2021.5.22--双星陨坠，举国哀痛','2021.7.1--中国共产党成立一百周年；五下期末考试','2021.9.1--六上开始，岳老师回归；迎来新同学','2021.9.25--孟晚舟回国','2021.11.11--双十一狂欢','2021.12.31--《如果微某公司倒闭了》完稿']
counter = 0
def run_counter(obj):
    def counting():
        global counter
        obj.config(text=labels[counter])
        if counter == 11:
            counter = 0
        else:
            counter += 1
        obj.after(1000,counting)
    counting()
root = Tk()
root.title("LMK")
label = Label(root,text='回望2021',font='楷体 60 normal italic',fg='red')
label.pack()
run_counter(label)
root.mainloop()
