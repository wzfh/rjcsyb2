import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        # self.__win()
        # self.tk_tabs_lxv6vvyf = self.__tk_tabs_lxv6vvyf(self)
        # self.tk_label_frame_lxv6zvcb = self.__tk_label_frame_lxv6zvcb( self.tk_tabs_lxv6vvyf_0)
        # self.tk_button_lxv773zl = self.__tk_button_lxv773zl( self.tk_label_frame_lxv6zvcb)
        # self.tk_input_lxv77ls0 = self.__tk_input_lxv77ls0( self.tk_label_frame_lxv6zvcb)
        # self.tk_label_lxv78gxm = self.__tk_label_lxv78gxm( self.tk_label_frame_lxv6zvcb)
        # self.tk_input_lxv78ycf = self.__tk_input_lxv78ycf( self.tk_label_frame_lxv6zvcb)
        # self.tk_label_lxv79yme = self.__tk_label_lxv79yme( self.tk_label_frame_lxv6zvcb)
        # self.tk_button_lxv7avzl = self.__tk_button_lxv7avzl( self.tk_label_frame_lxv6zvcb)
        # self.tk_label_frame_lxv73o6w = self.__tk_label_frame_lxv73o6w( self.tk_tabs_lxv6vvyf_0)
        # self.tk_select_box_lxv7ckxd = self.__tk_select_box_lxv7ckxd( self.tk_label_frame_lxv73o6w)
        # self.tk_button_lxv7h04h = self.__tk_button_lxv7h04h( self.tk_label_frame_lxv73o6w)
        # self.tk_radio_button_lxv7hoep = self.__tk_radio_button_lxv7hoep( self.tk_label_frame_lxv73o6w)
        # self.tk_radio_button_lxv7jm59 = self.__tk_radio_button_lxv7jm59( self.tk_label_frame_lxv73o6w)
        # self.tk_label_frame_lxv74afu = self.__tk_label_frame_lxv74afu( self.tk_tabs_lxv6vvyf_0)
        # self.tk_text_lxy5okbn = self.__tk_text_lxy5okbn(self.tk_label_frame_lxv74afu)
        # self.tk_label_frame_lxv754so = self.__tk_label_frame_lxv754so( self.tk_tabs_lxv6vvyf_0)
        # self.tk_text_lxy5p1aw = self.__tk_text_lxy5p1aw(self.tk_label_frame_lxv754so)
        self.__win()
        self.tk_tabs_lxv6vvyf = self.__tk_tabs_lxv6vvyf(self)
        self.tk_label_frame_lxv6zvcb = self.__tk_label_frame_lxv6zvcb(self.tk_tabs_lxv6vvyf_0)
        self.tk_button_lxv773zl = self.__tk_button_lxv773zl(self.tk_label_frame_lxv6zvcb)
        self.tk_input_lxv77ls0 = self.__tk_input_lxv77ls0(self.tk_label_frame_lxv6zvcb)
        self.tk_label_lxv78gxm = self.__tk_label_lxv78gxm(self.tk_label_frame_lxv6zvcb)
        self.tk_input_lxv78ycf = self.__tk_input_lxv78ycf(self.tk_label_frame_lxv6zvcb)
        self.tk_label_lxv79yme = self.__tk_label_lxv79yme(self.tk_label_frame_lxv6zvcb)
        self.tk_button_lxv7avzl = self.__tk_button_lxv7avzl(self.tk_label_frame_lxv6zvcb)
        self.tk_label_frame_lxv73o6w = self.__tk_label_frame_lxv73o6w(self.tk_tabs_lxv6vvyf_0)
        self.tk_select_box_lxv7ckxd = self.__tk_select_box_lxv7ckxd(self.tk_label_frame_lxv73o6w)
        self.tk_button_lxv7h04h = self.__tk_button_lxv7h04h(self.tk_label_frame_lxv73o6w)
        self.tk_radio_button_lxv7hoep = self.__tk_radio_button_lxv7hoep(self.tk_label_frame_lxv73o6w)

        self.tk_frame_lxygtwgi = self.__tk_frame_lxygtwgi(self.tk_label_frame_lxv73o6w)

        self.tk_frame_lxygtwgi1 = self.__tk_frame_lxygtwgi1(self.tk_label_frame_lxv73o6w)
        self.tk_frame_lxygtwgi2 = self.__tk_frame_lxygtwgi2(self.tk_label_frame_lxv73o6w)
        self.tk_frame_lxygtwgi3 = self.__tk_frame_lxygtwgi3(self.tk_label_frame_lxv73o6w)

        # self.tk_input_lxygvyfs = self.__tk_input_lxygvyfs(self.tk_frame_lxygtwgi)
        # self.tk_label_lxygw3p7 = self.__tk_label_lxygw3p7(self.tk_frame_lxygtwgi)
        self.tk_input_lxygvyfs = self.__tk_input_lxygvyfs(self.tk_label_frame_lxv73o6w)
        self.tk_label_lxygw3p7 = self.__tk_label_lxygw3p7(self.tk_label_frame_lxv73o6w)
        self.tk_input_lxygxlii = self.__tk_input_lxygxlii(self.tk_frame_lxygtwgi)
        self.tk_label_lxygxul8 = self.__tk_label_lxygxul8(self.tk_frame_lxygtwgi)
        self.tk_label_lxygxxix = self.__tk_label_lxygxxix(self.tk_frame_lxygtwgi)
        self.tk_input_lxygxzvc = self.__tk_input_lxygxzvc(self.tk_frame_lxygtwgi)
        self.tk_button_lxyh2e7d = self.__tk_button_lxyh2e7d(self.tk_frame_lxygtwgi)
        self.tk_button_lxyh2v5m = self.__tk_button_lxyh2v5m(self.tk_frame_lxygtwgi)
        self.tk_label_frame_lxv74afu = self.__tk_label_frame_lxv74afu(self.tk_tabs_lxv6vvyf_0)
        self.tk_text_lxy5okbn = self.__tk_text_lxy5okbn(self.tk_label_frame_lxv74afu)
        self.tk_label_frame_lxv754so = self.__tk_label_frame_lxv754so(self.tk_tabs_lxv6vvyf_0)
        self.tk_text_lxy5p1aw = self.__tk_text_lxy5p1aw(self.tk_label_frame_lxv754so)

        # 报警列表窗口
        # self.tk_frame_alarm = self.__tk_frame_alarm(self.tk_frame_lxygtwgi1)
        self.tk_select_box_ly703s7u = self.__tk_select_box_ly703s7u(self.tk_frame_lxygtwgi1)
        self.tk_radio_button_ly5jbxmi = self.__tk_radio_button_ly5jbxmi(self.tk_frame_lxygtwgi2)
        self.tk_radio_button_ly5jcr04 = self.__tk_radio_button_ly5jcr04(self.tk_frame_lxygtwgi2)
        self.tk_label_ly5jgd2g = self.__tk_label_ly5jgd2g(self.tk_frame_lxygtwgi2)

        self.tk_select_box_ly8bh0v7 = self.__tk_select_box_ly8bh0v7(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf5 = self.__tk_label_frame_ly8bjuf5(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf51 = self.__tk_label_frame_ly8bjuf51(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf52 = self.__tk_label_frame_ly8bjuf52(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf53 = self.__tk_label_frame_ly8bjuf53(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf54 = self.__tk_label_frame_ly8bjuf54(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf55 = self.__tk_label_frame_ly8bjuf55(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf56 = self.__tk_label_frame_ly8bjuf56(self.tk_frame_lxygtwgi3)
        self.tk_label_frame_ly8bjuf57 = self.__tk_label_frame_ly8bjuf57(self.tk_frame_lxygtwgi3)
        self.tk_list_box_ly8dvqzm = self.__tk_list_box_ly8dvqzm(self.tk_label_frame_ly8bjuf5)
        self.tk_label_ly8e38bn = self.__tk_label_ly8e38bn(self.tk_label_frame_ly8bjuf52)
        self.tk_input_ly8e3a89 = self.__tk_input_ly8e3a89(self.tk_label_frame_ly8bjuf52)
        self.tk_label_ly8e3cat = self.__tk_label_ly8e3cat(self.tk_label_frame_ly8bjuf52)
        self.tk_input_ly8e3fi2 = self.__tk_input_ly8e3fi2(self.tk_label_frame_ly8bjuf52)
        self.tk_label_ly8e3hqy = self.__tk_label_ly8e3hqy(self.tk_label_frame_ly8bjuf52)
        self.tk_input_ly8e3k2t = self.__tk_input_ly8e3k2t(self.tk_label_frame_ly8bjuf52)
        self.tk_label_ly8eipx9 = self.__tk_label_ly8eipx9(self.tk_label_frame_ly8bjuf53)
        self.tk_input_ly8ejpej = self.__tk_input_ly8ejpej(self.tk_label_frame_ly8bjuf53)
        self.tk_label_ly8eqf7j = self.__tk_label_ly8eqf7j(self.tk_label_frame_ly8bjuf53)
        self.tk_input_ly8eqi9n = self.__tk_input_ly8eqi9n(self.tk_label_frame_ly8bjuf53)
        self.tk_radio_button_ly8eqpg3 = self.__tk_radio_button_ly8eqpg3(self.tk_label_frame_ly8bjuf53)
        self.tk_radio_button_ly8eqtwa = self.__tk_radio_button_ly8eqtwa(self.tk_label_frame_ly8bjuf53)
        self.tk_list_box_ly8fp6ua = self.__tk_list_box_ly8fp6ua(self.tk_label_frame_ly8bjuf54)
        # self.tk_radio_button_ly8fxr28 = self.__tk_radio_button_ly8fxr28(self.tk_label_frame_ly8bjuf55)
        # self.tk_radio_button_ly8fxteh = self.__tk_radio_button_ly8fxteh(self.tk_label_frame_ly8bjuf55)
        self.tk_select_box_ly8g0lmi = self.__tk_select_box_ly8g0lmi(self.tk_label_frame_ly8bjuf55)
        self.tk_label_ly8g392k = self.__tk_label_ly8g392k(self.tk_label_frame_ly8bjuf55)
        self.tk_input_ly8g3cus = self.__tk_input_ly8g3cus(self.tk_label_frame_ly8bjuf55)
        self.tk_input_ly8g3ox7 = self.__tk_input_ly8g3ox7(self.tk_label_frame_ly8bjuf55)
        self.tk_label_ly8g3upt = self.__tk_label_ly8g3upt(self.tk_label_frame_ly8bjuf55)
        self.tk_select_box_ly8g0lmi1 = self.__tk_select_box_ly8g0lmi1(self.tk_label_frame_ly8bjuf56)
        self.tk_label_ly8g392k1 = self.__tk_label_ly8g392k1(self.tk_label_frame_ly8bjuf56)
        self.tk_input_ly8g3cus1 = self.__tk_input_ly8g3cus1(self.tk_label_frame_ly8bjuf56)
        self.tk_input_ly8g3ox71 = self.__tk_input_ly8g3ox71(self.tk_label_frame_ly8bjuf56)
        self.tk_label_ly8g3upt1 = self.__tk_label_ly8g3upt1(self.tk_label_frame_ly8bjuf56)
        self.tk_input_ly8g3ox72 = self.__tk_input_ly8g3ox72(self.tk_label_frame_ly8bjuf56)
        self.tk_label_ly8g3upt2 = self.__tk_label_ly8g3upt2(self.tk_label_frame_ly8bjuf56)

    def __win(self):
        self.title("studentcard")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_tabs_lxv6vvyf(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_lxv6vvyf_0 = self.__tk_frame_lxv6vvyf_0(frame)
        frame.add(self.tk_tabs_lxv6vvyf_0, text="学生证tcp发送")
        self.tk_tabs_lxv6vvyf_1 = self.__tk_frame_lxv6vvyf_1(frame)
        frame.add(self.tk_tabs_lxv6vvyf_1, text="服务器操作")
        self.tk_tabs_lxv6vvyf_2 = self.__tk_frame_lxv6vvyf_2(frame)
        frame.add(self.tk_tabs_lxv6vvyf_2, text="平台操作")
        frame.place(x=0, y=4, width=600, height=496)
        return frame

    def __tk_frame_lxv6vvyf_0(self, parent):
        frame = Frame(parent)
        # frame.place(x=0, y=4, width=600, height=496)
        return frame

    def __tk_frame_lxv6vvyf_1(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=4, width=600, height=496)
        return frame

    def __tk_frame_lxv6vvyf_2(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=4, width=600, height=496)
        return frame

    def __tk_label_frame_lxv6zvcb(self, parent):
        frame = LabelFrame(parent, text="服务器连接", )
        frame.place(x=0, y=0, width=200, height=181)
        return frame

    def __tk_button_lxv773zl(self, parent):
        btn = Button(parent, text="连接", takefocus=False, )
        btn.place(x=10, y=120, width=50, height=30)
        return btn

    def __tk_input_lxv77ls0(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "47.113.121.87")
        ipt.place(x=56, y=0, width=141, height=31)
        return ipt

    def __tk_label_lxv78gxm(self, parent):
        label = Label(parent, text="服务器ip", anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_lxv78ycf(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "7999")
        ipt.place(x=56, y=50, width=142, height=31)
        return ipt

    def __tk_label_lxv79yme(self, parent):
        label = Label(parent, text="端口", anchor="center", )
        label.place(x=0, y=50, width=50, height=30)
        return label

    def __tk_button_lxv7avzl(self, parent):
        btn = Button(parent, text="断开", takefocus=False, state="disabled")
        btn.place(x=126, y=119, width=50, height=30)
        return btn

    def __tk_label_frame_lxv73o6w(self, parent):
        frame = LabelFrame(parent, text="发送数据", )
        frame.place(x=0, y=184, width=200, height=286)
        return frame

    def __tk_select_box_lxv7ckxd(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("定位数据", "报警数据", "自定义文本", "其他")
        cb.set("定位数据")
        cb.place(x=0, y=10, width=150, height=30)
        return cb

    def __tk_button_lxv7h04h(self, parent):
        btn = Button(parent, text="发送", takefocus=False, )
        btn.place(x=148, y=236, width=50, height=30)
        return btn

    def __tk_radio_button_lxv7hoep(self, parent):
        rb = Radiobutton(parent, text="是否先发送登录数据", )
        rb.place(x=0, y=236, width=140, height=30)
        return rb

    # def __tk_frame_lxygtwgi(self, parent):
    #     frame = Frame(parent, )
    #     frame.place(x=0, y=40, width=199, height=191)
    #     return frame
    def __tk_frame_lxygtwgi(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=73, width=192, height=158)
        return frame

    def __tk_frame_lxygtwgi1(self, parent):
        frame = Frame(parent, )
        # frame.place(x=0, y=73, width=192, height=158)
        return frame

    def __tk_frame_lxygtwgi2(self, parent):
        frame = Frame(parent, )
        # frame.place(x=0, y=40, width=199, height=191)
        return frame

    def __tk_frame_lxygtwgi3(self, parent):
        frame = Frame(parent, )
        # frame.place(x=0, y=40, width=199, height=191)
        return frame

    def __tk_input_lxygvyfs(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "123456789012345")
        ipt.place(x=64, y=40, width=127, height=30)
        return ipt

    def __tk_label_lxygw3p7(self, parent):
        label = Label(parent, text="IMEI", anchor="center", )
        # label.place(x=0, y=0, width=50, height=30)
        label.place(x=0, y=40, width=50, height=30)
        return label

    def __tk_input_lxygxlii(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "114.106906")
        ipt.place(x=63, y=12, width=127, height=30)
        return ipt

    def __tk_label_lxygxul8(self, parent):
        label = Label(parent, text="经度", anchor="center", )
        # label.place(x=0, y=40, width=50, height=30)
        label.place(x=0, y=12, width=50, height=30)
        return label

    def __tk_label_lxygxxix(self, parent):
        label = Label(parent, text="纬度", anchor="center", )
        label.place(x=0, y=56, width=50, height=30)
        return label

    def __tk_input_lxygxzvc(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "22.468459")
        ipt.place(x=64, y=56, width=127, height=30)
        return ipt

    def __tk_button_lxyh2e7d(self, parent):
        btn = Button(parent, text="随机经纬度", takefocus=False, )
        btn.place(x=0, y=120, width=80, height=30)
        return btn

    def __tk_button_lxyh2v5m(self, parent):
        btn = Button(parent, text="wifi数据", takefocus=False, )
        btn.place(x=110, y=120, width=80, height=30)
        return btn

    def __tk_label_frame_lxv74afu(self, parent):
        frame = LabelFrame(parent, text="数据接收及提示窗口", )
        frame.place(x=218, y=0, width=379, height=179)
        return frame

    def __tk_text_lxy5okbn(self, parent):
        text = Text(parent)
        text.place(x=0, y=0, width=376, height=155)
        return text

    def __tk_label_frame_lxv754so(self, parent):
        frame = LabelFrame(parent, text="数据发送窗口", )
        frame.place(x=214, y=180, width=381, height=284)
        return frame

    def __tk_text_lxy5p1aw(self, parent):
        text = Text(parent)
        text.place(x=3, y=1, width=378, height=271)
        # text.insert('insert', "可以输入或修改文本。\n")
        return text

    def __tk_select_box_ly703s7u(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("sos报警", "开机", "关机", "缺电", "自动关机", "心跳")
        cb.set("sos报警")
        cb.place(x=19, y=20, width=150, height=30)
        return cb

    def __tk_radio_button_ly5jbxmi(self, parent):
        rb = Radiobutton(parent, text="是否替换当时最新时间", )
        rb.place(x=1, y=6, width=173, height=30)
        return rb

    def __tk_radio_button_ly5jcr04(self, parent):
        rb = Radiobutton(parent, text="是否替换IMEI", )
        rb.place(x=0, y=41, width=174, height=30)
        return rb

    def __tk_label_ly5jgd2g(self, parent):
        label = Label(parent, text="请在输入框中输入数据", anchor="center", )
        label.place(x=11, y=109, width=160, height=30)
        return label

    def __tk_select_box_ly8bh0v7(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = (
            "设备模式上报", "设备登录", "健康参数上报", "通话记录上报", "到家提醒", "亲情号码报警", "上报答题结果",
            "跳绳数据上报", "获取跳绳蓝牙mac地址", "蓝牙信标上传")
        cb.set("设备模式上报")
        cb.place(x=0, y=0, width=190, height=30)
        return cb

    def __tk_label_frame_ly8bjuf5(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf51(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf52(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf53(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf54(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf55(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf56(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_label_frame_ly8bjuf57(self, parent):
        frame = LabelFrame(parent, text="参数选择区", )
        # frame.place(x=0, y=30, width=188, height=123)
        return frame

    def __tk_list_box_ly8dvqzm(self, parent):
        lb = Listbox(parent)

        lb.insert(END, "平衡模式")

        lb.insert(END, "实时模式")

        lb.insert(END, "待机模式")

        lb.place(x=0, y=0, width=188, height=104)
        return lb

    def __tk_label_ly8e38bn(self, parent):
        label = Label(parent, text="心率", anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_ly8e3a89(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "95")
        ipt.place(x=80, y=0, width=100, height=30)
        return ipt

    def __tk_label_ly8e3cat(self, parent):
        label = Label(parent, text="血氧", anchor="center", )
        label.place(x=0, y=35, width=50, height=30)
        return label

    def __tk_input_ly8e3fi2(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "95")
        ipt.place(x=80, y=35, width=100, height=30)
        return ipt

    def __tk_label_ly8e3hqy(self, parent):
        label = Label(parent, text="体温", anchor="center", )
        label.place(x=0, y=70, width=50, height=30)
        return label

    def __tk_input_ly8e3k2t(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, "36.8")
        ipt.place(x=80, y=70, width=100, height=30)
        return ipt

    def __tk_label_ly8eipx9(self, parent):
        label = Label(parent, text="手机号", anchor="center", )
        label.place(x=0, y=0, width=50, height=30)
        return label

    def __tk_input_ly8ejpej(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=0, width=100, height=30)
        return ipt

    def __tk_label_ly8eqf7j(self, parent):
        label = Label(parent, text="时长", anchor="center", )
        label.place(x=0, y=40, width=50, height=30)
        return label

    def __tk_input_ly8eqi9n(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=100, height=30)
        return ipt

    def __tk_radio_button_ly8eqpg3(self, parent):
        rb = Radiobutton(parent, text="呼出", )
        rb.place(x=0, y=75, width=80, height=30)
        return rb

    def __tk_radio_button_ly8eqtwa(self, parent):
        rb = Radiobutton(parent, text="呼入", )
        rb.place(x=100, y=75, width=80, height=30)
        return rb

    def __tk_list_box_ly8fp6ua(self, parent):
        lb = Listbox(parent)

        lb.insert(END, "到家")

        lb.insert(END, "离家")

        lb.insert(END, "到校")

        lb.insert(END, "离校")

        lb.place(x=0, y=0, width=188, height=104)
        return lb

    # def __tk_radio_button_ly8fxr28(self, parent):
    #     rb = Radiobutton(parent, text="进入", )
    #     rb.place(x=0, y=0, width=50, height=30)
    #     return rb
    #
    # def __tk_radio_button_ly8fxteh(self, parent):
    #     rb = Radiobutton(parent, text="退出", )
    #     rb.place(x=56, y=0, width=50, height=30)
    #     return rb

    def __tk_select_box_ly8g0lmi(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("单选", "判断", "Tkinter 多选")
        cb.set("单选")
        cb.place(x=0, y=0, width=180, height=30)
        return cb

    def __tk_label_ly8g392k(self, parent):
        label = Label(parent, text="题目序号", anchor="center", )
        label.place(x=0, y=40, width=50, height=30)
        return label

    def __tk_input_ly8g3cus(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=100, height=30)
        return ipt

    def __tk_input_ly8g3ox7(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=75, width=100, height=30)
        return ipt

    def __tk_label_ly8g3upt(self, parent):
        label = Label(parent, text="答案", anchor="center", )
        label.place(x=0, y=75, width=50, height=30)
        return label

    def __tk_select_box_ly8g0lmi1(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("自由跳模式", "倒计时跳模式")
        cb.set("自由跳模式")
        cb.place(x=0, y=0, width=180, height=30)
        return cb

    def __tk_label_ly8g392k1(self, parent):
        label = Label(parent, text="跳绳时长(s)", anchor="center", )
        label.place(x=0, y=40, width=50, height=30)
        return label

    def __tk_input_ly8g3cus1(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=100, height=30)
        return ipt

    def __tk_input_ly8g3ox71(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=75, width=100, height=30)
        return ipt

    def __tk_label_ly8g3upt1(self, parent):
        label = Label(parent, text="跳绳次数", anchor="center", )
        label.place(x=0, y=75, width=50, height=30)
        return label

    def __tk_input_ly8g3ox72(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=0, y=35, width=174, height=65)
        return ipt

    def __tk_label_ly8g3upt2(self, parent):
        label = Label(parent, text="mac地址", anchor="center", )
        label.place(x=0, y=0, width=174, height=30)
        return label


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_lxv773zl.bind('<Button>', self.ctl.connect)
        self.tk_button_lxv7avzl.bind('<Button>', self.ctl.disconnect)
        self.tk_button_lxv7h04h.bind('<Button>', self.ctl.send)
        self.tk_select_box_lxv7ckxd.bind('<<ComboboxSelected>>', self.ctl.change_page)
        self.tk_button_lxyh2e7d.bind('<Button>', self.ctl.random_gps)
        self.tk_button_lxyh2v5m.bind('<Button>', self.ctl.wifi_data)
        self.tk_select_box_ly8bh0v7.bind('<<ComboboxSelected>>', self.ctl.change_page1)


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
