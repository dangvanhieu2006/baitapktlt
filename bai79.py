import tkinter as tk
import random

arr = []

def tao_mang():
    global arr
    n = int(entry_n.get())
    arr = [random.randint(-100, 100) for _ in range(n)]
    hien_thi()

def hien_thi():
    kq.delete("1.0", tk.END)
    kq.insert(tk.END, "Mảng: " + str(arr) + "\n")

def gan_x():
    x = int(entry_x.get())
    gan = min(arr, key=lambda a: abs(a - x))
    kq.insert(tk.END, f"Gần {x} nhất: {gan}\n")

def chen_1():
    global arr
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr.insert(i+1, 1)
            i += 1
        i += 1
    hien_thi()

# GUI
root = tk.Tk()
root.title("Xử lý mảng")

tk.Label(root, text="n").grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Button(root, text="Tạo mảng", command=tao_mang).grid(row=1, columnspan=2)

tk.Label(root, text="x").grid(row=2, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=2, column=1)

tk.Button(root, text="Tìm gần x", command=gan_x).grid(row=3, columnspan=2)
tk.Button(root, text="Chèn 1 sau số âm", command=chen_1).grid(row=4, columnspan=2)

kq = tk.Text(root, height=10, width=40)
kq.grid(row=5, columnspan=2)

root.mainloop()
