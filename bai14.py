import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def next_day():
    try:
        d = int(entry_day.get())
        m = int(entry_month.get())
        y = int(entry_year.get())

        current_date = datetime(y, m, d)
        next_date = current_date + timedelta(days=1)

        result_var.set(f"Ngày tiếp theo: {next_date.day}/{next_date.month}/{next_date.year}")
    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")

def prev_day():
    try:
        d = int(entry_day.get())
        m = int(entry_month.get())
        y = int(entry_year.get())

        current_date = datetime(y, m, d)
        prev_date = current_date - timedelta(days=1)

        result_var.set(f"Ngày trước đó: {prev_date.day}/{prev_date.month}/{prev_date.year}")
    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tính ngày tiếp theo / trước đó")
root.geometry("350x250")

# Nhãn và ô nhập
tk.Label(root, text="Ngày").pack()
entry_day = tk.Entry(root)
entry_day.pack()

tk.Label(root, text="Tháng").pack()
entry_month = tk.Entry(root)
entry_month.pack()

tk.Label(root, text="Năm").pack()
entry_year = tk.Entry(root)
entry_year.pack()

# Nút bấm
tk.Button(root, text="Ngày tiếp theo", command=next_day).pack(pady=5)
tk.Button(root, text="Ngày trước đó", command=prev_day).pack(pady=5)

# Kết quả
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").pack(pady=10)

# Chạy chương trình
root.mainloop()
