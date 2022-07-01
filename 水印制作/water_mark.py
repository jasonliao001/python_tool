from watermarker.marker import add_mark
import tkinter as tk
import tkinter.filedialog as filedialog
import numpy as np
import time


def isNaNo(sth):
    '''
    NaN、None或者空字符串返回True，其他情况返回False
    '''
    if not sth:
        return True
    if isinstance(sth, float):
        if np.isnan(sth):
            return True
    return False
# 方法
class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("图片加水印")
        # 路径变量
        self.img_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.watermark_text = tk.StringVar()
        # 布局
        self.frame = tk.Frame(self)
        self.frame.pack(padx=10, pady=10)
        # 第一行
        # 标签
        self.lbl_file = tk.Label(self.frame, text="需要处理图片位置")
        self.lbl_file.grid(row=0, column=0)
        # 输入框布局
        self.txt_file = tk.Entry(self.frame, width=60, textvariable=self.img_path)
        self.txt_file.grid(row=0, column=1, sticky=tk.W)
        # button形式以及布局
        self.btn_file = tk.Button(self.frame, text="选择", command=self.sel_img_file)
        self.btn_file.grid(row=0, column=1, sticky=tk.E)
        # 第二行
        self.lbl_file_1 = tk.Label(self.frame, text="图片输出位置")
        self.lbl_file_1.grid(row=1, column=0)
        self.txt_file_1 = tk.Entry(self.frame, width=60, textvariable=self.output_path)
        self.txt_file_1.grid(row=1, column=1, sticky=tk.W)
        self.btn_file_1 = tk.Button(self.frame, text="选择", command=self.sel_output_path)
        self.btn_file_1.grid(row=1, column=1, sticky=tk.E)
        # 第3行
        self.lbl_txt_2 = tk.Label(self.frame, text="水印文字")
        self.lbl_txt_2.grid(row=2, column=0)
        self.txt_file_2 = tk.Entry(self.frame,width=60, textvariable=self.watermark_text)
        self.txt_file_2.grid(row=2, column=1,sticky=tk.W)
        # 第4行
        self.lbl_txt_3 = tk.Label(self.frame, text="提示")
        self.lbl_txt_3.grid(row=3, column=0)
        self.txt_exract = tk.Text(self.frame)
        self.txt_exract.grid(row=3, column=1)

        # 第5行
        self.btn_extract = tk.Button(self.frame, text="开始处理", command=self.extract_text)
        self.btn_extract.grid(row=4, column=1, sticky=tk.W + tk.E)

    def sel_img_file(self):
        self.txt_exract.delete(1.0, tk.END)
        self.txt_exract.insert(tk.END, "")
        self.img_path.set(filedialog.askopenfilename(title="选择图片", initialdir="."))
    def sel_output_path(self):
        self.txt_exract.delete(1.0, tk.END)
        self.txt_exract.insert(tk.END, "")
        self.output_path.set(filedialog.askdirectory(title="选择输出位置", initialdir="."))
    def clear_text(self):
        self.txt_exract.delete(1.0, tk.END)
        self.txt_exract.insert(tk.END,"")
        time.sleep(2)

    def extract_text(self):
        self.clear_text()
        img_path = self.img_path.get()
        output_path = self.output_path.get()
        watermark_text = self.watermark_text.get()
        if isNaNo(img_path) or isNaNo(output_path) or isNaNo(watermark_text):
            self.txt_exract.delete(1.0, tk.END)
            self.txt_exract.insert(tk.END, "'需要处理图片位置不能为空'&'图片输出位置不能为空'&'水印文字不能为空'")
        else:
            try:
                add_mark(file=self.img_path.get(), out=self.output_path.get(), size=24,color="#ff0000",opacity=0.3,mark=self.watermark_text.get(), space=60)
                self.txt_exract.delete(1.0, tk.END)
                self.txt_exract.insert(tk.END, f"文件成功保存在{output_path}")
            except Exception as e:
                self.txt_exract.delete(1.0, tk.END)
                self.txt_exract.insert(tk.END, e)
#
# if __name__ == "__main__":
#     app = Application()
#     app.mainloop()