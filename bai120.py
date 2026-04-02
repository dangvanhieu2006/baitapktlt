import tkinter as tk
from tkinter import messagebox

def chen_chuoi():
    try:
        s1 = entry_s1.get()
        s2 = entry_s2.get()
        k = int(entry_k.get())

        # kiểm tra độ dài
        if len(s1) > 80 or len(s2) > 80:
            messagebox.showerror("Lỗi", "Chuỗi tối đa 80 ký tự!")
            return

        # kiểm tra k
        if k < 0 or k > len(s1):
            messagebox.showerror("Lỗi", "k không hợp lệ!")
            return

        # chèn chuỗi
        result = s1[:k] + s2 + s1[k:]

        label_kq.config(text="Kết quả: " + result)

    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")

# Giao diện
root = tk.Tk()
root.title("Chèn chuỗi")
root.geometry("450x250")

tk.Label(root, text="Chuỗi 1:").pack()
entry_s1 = tk.Entry(root, width=50)
entry_s1.pack()

tk.Label(root, text="Chuỗi 2:").pack()
entry_s2 = tk.Entry(root, width=50)
entry_s2.pack()

tk.Label(root, text="Vị trí k:").pack()
entry_k = tk.Entry(root)
entry_k.pack()

tk.Button(root, text="Chèn chuỗi", command=chen_chuoi).pack(pady=10)

label_kq = tk.Label(root, text="", fg="blue", wraplength=400)
label_kq.pack()

root.mainloop()
