import tkinter as tk
from tkinter import messagebox

def add_binary(a, b):
    result = ""
    carry = 0

    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))

    for i in range(len(a)-1, -1, -1):
        total = carry
        total += 1 if a[i] == '1' else 0
        total += 1 if b[i] == '1' else 0

        result = str(total % 2) + result
        carry = total // 2

    if carry:
        result = '1' + result

    return result


def calculate():
    bin1 = entry1.get()
    bin2 = entry2.get()

    if not all(c in '01' for c in bin1 + bin2):
        messagebox.showerror("Error", "Chỉ được nhập số nhị phân (0 hoặc 1)")
        return

    result = add_binary(bin1, bin2)
    result_label.config(text="Kết quả: " + result)


# GUI
root = tk.Tk()
root.title("Cộng nhị phân")
root.geometry("350x200")

label1 = tk.Label(root, text="Số nhị phân 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Số nhị phân 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

btn = tk.Button(root, text="Cộng", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(root, text="Kết quả: ")
result_label.pack()

root.mainloop()
