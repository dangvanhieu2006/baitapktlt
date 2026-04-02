import tkinter as tk
from tkinter import messagebox

def giai_thua(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

def to_hop(n, k):
    return giai_thua(n) // (giai_thua(k) * giai_thua(n - k))

def tinh_to_hop():
    try:
        n = int(entry_n.get())
        k = int(entry_k.get())

        c1 = to_hop(n, k)
        c2 = to_hop(n, n - k)

        result.set(f"C({n},{k}) = {c1}\nC({n},{n-k}) = {c2}")

        if c1 == c2:
            check.set("✔ Công thức đúng: C(n,k) = C(n,n-k)")
        else:
            check.set("✘ Công thức sai!")

    except:
        messagebox.showerror("Lỗi", "Nhập sai dữ liệu!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tính tổ hợp C(n,k)")
root.geometry("350x250")

# Nhập n, k
tk.Label(root, text="Nhập n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Label(root, text="Nhập k:").pack()
entry_k = tk.Entry(root)
entry_k.pack()

# Nút tính
tk.Button(root, text="Tính", command=tinh_to_hop).pack(pady=10)

# Hiển thị kết quả
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack()

check = tk.StringVar()
tk.Label(root, textvariable=check, fg="green").pack()

# Chạy
root.mainloop()
