import tkinter as tk
from tkinter import messagebox
import math

EPS = 5e-4

# ===== ĐỆ QUY SIN, COS =====

def sin_rec(x):
    if abs(x) < 0.1:  # ngưỡng nhỏ
        return x - (x**3)/6
    # giảm góc
    y = x / 3
    s = sin_rec(y)
    c = cos_rec(y)
    return (4*(c**2) - 1) * s


def cos_rec(x):
    if abs(x) < 0.1:
        return 1 - (x**2)/2
    y = x / 3
    s = sin_rec(y)
    c = cos_rec(y)
    return (1 - 4*(s**2)) * c

# ===== XỬ LÝ NÚT =====

def calculate():
    try:
        x = float(entry.get())

        s = sin_rec(x)
        c = cos_rec(x)

        s_true = math.sin(x)
        c_true = math.cos(x)

        result_label.config(
            text=(f"sin(x) ≈ {s:.6f} | math.sin = {s_true:.6f}\n"
                  f"cos(x) ≈ {c:.6f} | math.cos = {c_true:.6f}")
        )
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số thực hợp lệ")

# ===== GUI =====
root = tk.Tk()
root.title("Tính sin(x), cos(x) - Đệ quy")
root.geometry("420x220")

label = tk.Label(root, text="Nhập x (radian):")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

btn = tk.Button(root, text="Tính", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(root, text="Kết quả sẽ hiển thị ở đây", justify="left")
result_label.pack(pady=10)

root.mainloop()
