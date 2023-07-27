from Card import Card
import global_variable as glv

from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import threading

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        glv._init()
        glv.set("aa","aa2")
        glv.set("aa", "aa1")
        self.master = master
        self.pack()
        # label参数数组
        self.label_text_list=["请输入网址：","请输入表格路径:","请输入驱动路径:"]
        self.label_name_list=[]
        self.entry_name_list=[]
        self.createWidget()

    def createWidget(self):
        # 手动输入区文本
        self.label_01 = Label(self, text="手动输入区", width=10, height=0, bg="blue", fg="white", font=("黑体", 20))
        self.label_01.grid(row=0, column=0, padx=0, pady=20, columnspan=3)

        # 输入提示文本框及输入框
        for i in range(0,len(self.label_text_list)):
            self.label_name = Label(self, text=self.label_text_list[i], width=15, height=1, bg="blue", fg="white", font=("黑体", 15))
            self.label_name.grid(row=i+1, column=0, padx=0, pady=5)
            self.label_name_list.append(self.label_name)

            self.entry_name = Entry(self, width=45, relief=SUNKEN, borderwidth=3)
            self.entry_name.grid(row=i+1, column=1, padx=0, pady=5)
            self.entry_name_list.append(self.entry_name)

        # 选择表格路径按钮
        self.excel_file_btn = Button(self, text="..", width=0, height=0, font=("黑体", 10), state=NORMAL, command=lambda:self.btn_click("excelfile"))
        self.excel_file_btn.grid(row=2, column=2, padx=0, pady=0)
        # 选择驱动路径按钮
        self.driver_file_btn = Button(self, text="..", width=0, height=0, font=("黑体", 10), state=NORMAL,command=lambda: self.btn_click("driver_file"))
        self.driver_file_btn.grid(row=3, column=2, padx=0, pady=0)

        # 选择功能区文本
        self.label_01 = Label(self, text="请选择功能", width=10, height=0, bg="blue", fg="white", font=("黑体", 20))
        self.label_01.grid(row=6, column=0, padx=0, pady=20, columnspan=3)

        # 单选按钮容器
        self.Radio_Frame = Frame(self,bg="blue")
        self.Radio_Frame.grid(row=7, column=0, padx=0, pady=0, columnspan=3)
        # 单选按钮选择变量
        self.rbman_var= IntVar()
        self.rbman_var.set(0)
        glv.set("rbman_var",self.rbman_var)
        # 单选按钮(variable=var，value的值会赋给var,从而判断选择了哪个单选按钮)
        self.rbman = Radiobutton(self.Radio_Frame,text="绑卡",variable=self.rbman_var,value=0,font=("黑体", 13))
        self.rbman.pack(side=LEFT)
        self.rbman = Radiobutton(self.Radio_Frame,text="改名",variable=self.rbman_var,value=1,font=("黑体", 13))
        self.rbman.pack(side=LEFT)
        self.rbman = Radiobutton(self.Radio_Frame, text="爬取用户数据入库", variable=self.rbman_var, value=2, font=("黑体", 13))
        self.rbman.pack(side=LEFT)

        # 开始执行按钮，按钮normal为按钮正常状态DISABLED为不能按状态
        self.start_btn= Button(self, text="开始执行", width=10, height=2, font=("黑体", 15), state=NORMAL,command=lambda:self.btn_click("start"))
        self.start_btn.grid(row=8, column=0, padx=0, pady=10, columnspan=3)
        glv.set("start_btn", self.start_btn)

        # 显示日志滑动文本框(全局变量)
        self.text=scrolledtext.ScrolledText(self,width=75, height=23, bg="blue",fg="white", font=("黑体", 10))
        self.text.grid(row=9, column=0, padx=0, pady=10, columnspan=3)
        glv.set("scrolledtext", self.text)
    def btn_click(self,str):
        # 根据字符串判断触发哪个事件
        if str=="excelfile":
            root2 = Tk()
            root2.withdraw()
            filePath = filedialog.askopenfilename()
            self.entry_name_list[1].insert(END, filePath)
            # 要销毁文件夹窗口，不然会后台持续运行
            root2.destroy()
        elif str == "driver_file":
            root3 = Tk()
            root3.withdraw()
            filePath2 = filedialog.askopenfilename()
            self.entry_name_list[2].insert(END, filePath2)
            # 要销毁文件夹窗口，不然会后台持续运行
            root3.destroy()
        elif str=="start":
            # 开始后开始按钮显示不可点击状态
            # self.start_btn['state'] = DISABLED
            # 点击按钮执行
            card = Card(self.entry_name_list[1].get(), self.entry_name_list[2].get())
            # 开启一条线程来进行开始操作，target中的方法card.start_task不能加括号，否则会出错
            cardStart_thread = threading.Thread(target=card.start_task, args=(self.entry_name_list[0].get(),),daemon=True)
            cardStart_thread.start()



if __name__ == "__main__":
    root = Tk()
    root.geometry("600x700+150+50")
    root.title("facebook")
    alp = Application(master=root)
    root.mainloop()


