import tkinter as tk
from datetime import datetime, timedelta

def tinh():
    d = int(entry_d.get())
    m = int(entry_m.get())
    y = int(entry_y.get())
    
    ngay = datetime(y, m, d)
    
    ngay_sau = ngay + timedelta(days=1)
    ngay_truoc = ngay - timedelta(days=1)
    
    kq.config(text=f"Ngày sau: {ngay_sau.strftime('%d/%m/%Y')}\n"
                   f"Ngày trước: {ngay_truoc.strftime('%d/%m/%Y')}")

# GUI
root = tk.Tk()
root.title("Tính ngày")

tk.Label(root, text="Ngày").grid(row=0, column=0)
tk.Label(root, text="Tháng").grid(row=1, column=0)
tk.Label(root, text="Năm").grid(row=2, column=0)

entry_d = tk.Entry(root)
entry_m = tk.Entry(root)
entry_y = tk.Entry(root)

entry_d.grid(row=0, column=1)
entry_m.grid(row=1, column=1)
entry_y.grid(row=2, column=1)

tk.Button(root, text="Tính", command=tinh).grid(row=3, columnspan=2)

kq = tk.Label(root, text="")
kq.grid(row=4, columnspan=2)

root.mainloop()
