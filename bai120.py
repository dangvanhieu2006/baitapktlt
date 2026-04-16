import tkinter as tk

def chen():
    s1 = entry_s1.get()
    s2 = entry_s2.get()
    k = int(entry_k.get())
    
    if 0 <= k <= len(s1):
        kq.config(text="Kết quả: " + s1[:k] + s2 + s1[k:])
    else:
        kq.config(text="k không hợp lệ")

# GUI
root = tk.Tk()
root.title("Chèn chuỗi")

tk.Label(root, text="Chuỗi 1").grid(row=0, column=0)
tk.Label(root, text="Chuỗi 2").grid(row=1, column=0)
tk.Label(root, text="k").grid(row=2, column=0)

entry_s1 = tk.Entry(root, width=30)
entry_s2 = tk.Entry(root, width=30)
entry_k = tk.Entry(root)

entry_s1.grid(row=0, column=1)
entry_s2.grid(row=1, column=1)
entry_k.grid(row=2, column=1)

tk.Button(root, text="Chèn", command=chen).grid(row=3, columnspan=2)

kq = tk.Label(root, text="")
kq.grid(row=4, columnspan=2)

root.mainloop()
