self.str_905_button9 = Button(pane9, text="808普通报警", width=35,
                              command=lambda: self.thread_it(self.baoget))
self.str_905_button9.grid(row=2, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="808粤标报警", width=35,
                              command=lambda: self.thread_it(self.baoget1))
self.str_905_button9.grid(row=3, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="808苏标报警", width=35,
                              command=lambda: self.thread_it(self.baoget2))
self.str_905_button9.grid(row=4, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="905人证不匹配报警", width=35,
                              command=lambda: self.thread_it(self.baoget3))
self.str_905_button9.grid(row=5, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="905绕路报警", width=35,
                              command=lambda: self.thread_it(self.baoget4))
self.str_905_button9.grid(row=6, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="905驾驶员没有从业资格证", width=35,
                              command=lambda: self.thread_it(self.baoget5))
self.str_905_button9.grid(row=7, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="905跨区域营运预警", width=35,
                              command=lambda: self.thread_it(self.baoget6))
self.str_905_button9.grid(row=8, column=1, columnspan=2, sticky=E)
self.str_905_button9 = Button(pane9, text="905车辆未办理网络预约出租车营运证预警", width=35,
                              command=lambda: self.thread_it(self.baoget7))
self.str_905_button9.grid(row=9, column=1, columnspan=2, sticky=E)

self.str_905_button9 = Button(pane9, text="循环报警", width=35,
                              command=lambda: self.thread_it(self.baojhe))
self.str_905_button9.grid(row=10, column=1, columnspan=2, sticky=E)
self.result905_label9 = Label(pane9, text="输出结果：有返回，即发送成功")
self.result905_label9.grid(row=1, column=3, sticky=E)
self.result905_Text9 = Text(pane9, width=85, height=19, relief='solid')
self.result905_Text9.grid(row=2, column=3, rowspan=9, sticky=E)
