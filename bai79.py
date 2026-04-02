import tkinter as tk
from tkinter import messagebox
import random

arr = []

# a. Tạo mảng
def tao_mang():
    global arr
    try:
        n = int(entry_n.get())
        arr = [random.randint(-100, 100) for _ in range(n)]
        label_arr.config(text="Mảng: " + str(arr))
        label_kq.config(text="")
    except:
        messagebox.showerror("Lỗi", "Nhập n hợp lệ!")

# b. Tìm phần tử gần x nhất
def tim_gan_x():
    try:
        x = int(entry_x.get())
        if not arr:
            messagebox.showerror("Lỗi", "Chưa tạo mảng!")
            return

        gan_nhat = arr[0]
        for i in arr:
            if abs(i - x) < abs(gan_nhat - x):
                gan_nhat = i

        label_kq.config(text=f"Phần tử gần {x} nhất là: {gan_nhat}")
    except:
        messagebox.showerror("Lỗi", "Nhập x hợp lệ!")

# c. Chèn 1 sau phần tử âm
def chen_1():
    global arr
    if not arr:
        messagebox.showerror("Lỗi", "Chưa tạo mảng!")
        return

    new_arr = []
    for i in arr:
        new_arr.append(i)
        if i < 0:
            new_arr.append(1)

    arr = new_arr
    label_arr.config(text="Mảng sau khi chèn: " + str(arr))
    label_kq.config(text="Đã chèn 1 sau các số âm")

# Giao diện
root = tk.Tk()
root.title("Xử lý mảng")
root.geometry("450x350")

tk.Label(root, text="Nhập số phần tử n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo mảng", command=tao_mang).pack(pady=5)

label_arr = tk.Label(root, text="", wraplength=400, fg="blue")
label_arr.pack(pady=5)

tk.Label(root, text="Nhập x:").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Button(root, text="Tìm phần tử gần x", command=tim_gan_x).pack(pady=5)

tk.Button(root, text="Chèn 1 sau số âm", command=chen_1).pack(pady=5)

label_kq = tk.Label(root, text="", fg="green")
label_kq.pack(pady=10)

root.mainloop()
