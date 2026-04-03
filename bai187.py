import tkinter as tk
from tkinter import filedialog, messagebox

LINES_PER_PAGE = 25

class FileViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiển thị file theo trang")
        self.root.geometry("600x400")

        self.text = tk.Text(root, width=80, height=25)
        self.text.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        self.open_btn = tk.Button(self.btn_frame, text="Mở file", command=self.open_file)
        self.open_btn.pack(side="left", padx=5)

        self.next_btn = tk.Button(self.btn_frame, text="Tiếp (Enter)", command=self.next_page, state="disabled")
        self.next_btn.pack(side="left", padx=5)

        self.lines = []
        self.index = 0

        self.root.bind('<Return>', lambda event: self.next_page())

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.lines = f.readlines()
            self.index = 0
            self.text.delete(1.0, tk.END)
            self.next_btn.config(state="normal")
            self.next_page()
        except:
            messagebox.showerror("Lỗi", "Không đọc được file")

    def next_page(self):
        if self.index >= len(self.lines):
            messagebox.showinfo("Thông báo", "Đã hết nội dung file")
            return

        self.text.delete(1.0, tk.END)

        for _ in range(LINES_PER_PAGE):
            if self.index < len(self.lines):
                self.text.insert(tk.END, self.lines[self.index])
                self.index += 1
            else:
                break

# chạy app
root = tk.Tk()
app = FileViewer(root)
root.mainloop()
