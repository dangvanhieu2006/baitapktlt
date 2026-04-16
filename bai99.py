import tkinter as tk
import random

A, B = [], []

def tao_ma_tran():
    global A, B
    n = int(entry_n.get())
    A = [[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
    hien(A, "Ma trận A")
    hien(B, "Ma trận B")

def hien(M, ten):
    kq.insert(tk.END, ten + ":\n")
    for row in M:
        kq.insert(tk.END, str(row) + "\n")
    kq.insert(tk.END, "\n")

def tong():
    n = len(A)
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
    hien(C, "Tổng A+B")

def tich():
    n = len(A)
    C = [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    hien(C, "Tích A*B")

# GUI
root = tk.Tk()
root.title("Ma trận")

tk.Label(root, text="n").grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

tk.Button(root, text="Tạo ma trận", command=tao_ma_tran).grid(row=1, columnspan=2)
tk.Button(root, text="Tính tổng", command=tong).grid(row=2, columnspan=2)
tk.Button(root, text="Tính tích", command=tich).grid(row=3, columnspan=2)

kq = tk.Text(root, height=20, width=40)
kq.grid(row=4, columnspan=2)

root.mainloop()
