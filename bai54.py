import tkinter as tk

def gt(n):
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return kq

def tinh():
    n = int(entry_n.get())
    k = int(entry_k.get())
    
    Cnk = gt(n) // (gt(k) * gt(n-k))
    Cn_nk = gt(n) // (gt(n-k) * gt(k))
    
    kq.config(text=f"C(n,k) = {Cnk}\nC(n,n-k) = {Cn_nk}\n"
                   + ("Đúng" if Cnk == Cn_nk else "Sai"))

root = tk.Tk()
root.title("Tổ hợp")

tk.Label(root, text="n").grid(row=0, column=0)
tk.Label(root, text="k").grid(row=1, column=0)

entry_n = tk.Entry(root)
entry_k = tk.Entry(root)

entry_n.grid(row=0, column=1)
entry_k.grid(row=1, column=1)

tk.Button(root, text="Tính", command=tinh).grid(row=2, columnspan=2)

kq = tk.Label(root, text="")
kq.grid(row=3, columnspan=2)

root.mainloop()
