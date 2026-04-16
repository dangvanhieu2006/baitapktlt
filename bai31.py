import tkinter as tk

def in_bang():
    kq.delete("1.0", tk.END)
    for i in range(2, 10):
        kq.insert(tk.END, f"Bảng {i}:\n")
        for j in range(1, 11):
            kq.insert(tk.END, f"{i} x {j} = {i*j}\n")
        kq.insert(tk.END, "\n")

root = tk.Tk()
root.title("Bảng cửu chương")

tk.Button(root, text="In bảng cửu chương", command=in_bang).pack()

kq = tk.Text(root, height=25, width=30)
kq.pack()

root.mainloop()
