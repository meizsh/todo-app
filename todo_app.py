# todo_app.py

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        """
        初始化 TodoList 应用程序。
        master 是主窗口（root）。
        """
        self.master = master
        master.title("待办事项列表")
        master.geometry("400x400") # 设置窗口初始大小 (宽度x高度)

        # 待办事项列表数据 (内存中)
        self.tasks = []

        # --- UI 组件创建 ---

        # 1. 任务输入框
        self.task_entry = tk.Entry(master, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10) # pack 是一个简单的布局管理器，pady 设置垂直内边距

        # 2. 添加任务按钮
        self.add_button = tk.Button(master, text="添加任务", command=self.add_task, font=("Arial", 10))
        self.add_button.pack(pady=5)

        # 3. 待办事项列表框
        # Listbox 显示项目列表
        self.task_listbox = tk.Listbox(master, width=50, height=15, selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # 4. 删除任务按钮
        self.delete_button = tk.Button(master, text="删除任务", command=self.delete_task, font=("Arial", 10))
        self.delete_button.pack(pady=5)

        # 初始化显示 (如果 tasks 列表中有数据的话)
        self.update_task_listbox()

    def add_task(self):
        """
        从输入框获取任务文本，添加到 tasks 列表，并更新列表框。
        这是“添加任务”按钮的回调函数。
        """
        task_text = self.task_entry.get().strip() # .get() 获取输入框内容, .strip() 移除空白

        if task_text: # 确保输入不为空
            self.tasks.append(task_text)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END) # 清空输入框
        else:
            messagebox.showwarning("警告", "任务不能为空！") # 弹出警告框

    def delete_task(self):
        """
        删除选中的任务。
        这是“删除任务”按钮的回调函数。
        """
        try:
            # curselection() 返回选中的索引元组 (例如 (0,) 表示选中第一个)
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("警告", "请选择要删除的任务！")

    def update_task_listbox(self):
        """
        清空列表框并重新填充 tasks 列表中的所有任务。
        """
        self.task_listbox.delete(0, tk.END) # 清空列表框所有内容
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task) # 在列表框末尾插入任务

# --- 程序主入口 ---
if __name__ == "__main__":
    root = tk.Tk() # 创建主窗口对象
    app = TodoApp(root) # 创建 TodoApp 实例，将主窗口传递给它
    root.mainloop() # 启动 Tkinter 事件循环，让窗口保持显示和响应事件