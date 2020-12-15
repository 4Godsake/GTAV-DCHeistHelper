import tkinter as tk  # 导入tkinter模块

window = tk.Tk()  # 主窗口
window.title('my window')  # 窗口标题
window.geometry('200x300')  # 窗口尺寸

### 这里是窗口的内容###

var = tk.StringVar()    # 文字变量储存器
var.set('等待启动')

label_status = tk.Label(window, textvariable=var, bg='blue', font=('Arial', 12), width=15, height=2)
label_status.pack()

on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit            # on_hit为全局变量
    if on_hit == False:      # 从 False 状态变成 True 状态
        on_hit = True
        var.set('已启动')   # 设置标签的文字为 'you hit me'
        label_status.config(bg='green')     #更改label的背景颜色，也可以更改其他选项
    else:                    # 从 True 状态变成 False 状态
        on_hit = False
        var.set('已停止')          # 设置 文字为空
        label_status.config(bg='red')
b = tk.Button(window, text='启动/停止', width=15, height=2, command=hit_me)
b.pack()

#选择器部分
var_selected = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='请选择模式')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var_selected.get())  # var.get()即获取到变量 var 的值

r1 = tk.Radiobutton(window, text='F5', variable=var_selected, value='F5', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='F6', variable=var_selected, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='F7', variable=var_selected, value='C', command=print_selection)
r3.pack()

r1.select()




window.mainloop()
