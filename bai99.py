import tkinter as tk
from tkinter import messagebox
import random

A = []
B = []

# Tạo ma trận
def tao_ma_tran():
    global A, B
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError

        A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        B = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

        text.delete("1.0", tk.END)
        text.insert(tk.END, "Ma trận A:\n")
        hien_thi(A)

        text.insert(tk.END, "\nMa trận B:\n")
        hien_thi(B)

    except:
        messagebox.showerror("Lỗi", "Nhập n hợp lệ!")

# Hiển thị ma trận
def hien_thi(M):
    for row in M:
        text.insert(tk.END, " ".join(f"{x:4}" for x in row) + "\n")

# Tính tổng
def tong_ma_tran():
    if not A or not B:
        messagebox.showerror("Lỗi", "Chưa tạo ma trận!")
        return

    n = len(A)
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

    text.insert(tk.END, "\nMa trận tổng (A + B):\n")
    hien_thi(C)

# Tính tích
def tich_ma_tran():
    if not A or not B:
        messagebox.showerror("Lỗi", "Chưa tạo ma trận!")
        return

    n = len(A)
    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    text.insert(tk.END, "\nMa trận tích (A x B):\n")
    hien_thi(C)

# Giao diện
root = tk.Tk()
root.title("Xử lý ma trận")
root.geometry("500x450")

tk.Label(root, text="Nhập cấp n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo ma trận", command=tao_ma_tran).pack(pady=5)
tk.Button(root, text="Tính tổng", command=tong_ma_tran).pack(pady=5)
tk.Button(root, text="Tính tích", command=tich_ma_tran).pack(pady=5)

# Vùng hiển thị
text = tk.Text(root, width=60, height=20)
text.pack(pady=10)

root.mainloop()
