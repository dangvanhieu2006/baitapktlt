import tkinter as tk
from tkinter import messagebox

# Hàm đệ quy tính tổng và đếm số âm
def neg_helper(arr, n):
    if n == 0:
        return (0, 0)  # (sum, count)

    s, c = neg_helper(arr, n - 1)

    if arr[n - 1] < 0:
        return (s + arr[n - 1], c + 1)
    return (s, c)

# Hàm tính trung bình số âm
def neg_average(arr):
    s, c = neg_helper(arr, len(arr))
    if c == 0:
        return 0
    return s / c

# Xử lý khi bấm nút
def calculate():
    try:
        input_str = entry.get()
        arr = list(map(int, input_str.split()))

        result = neg_average(arr)
        result_label.config(text=f"Trung bình số âm: {result}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên, cách nhau bởi dấu cách")

# GUI
root = tk.Tk()
root.title("Tính trung bình số âm (Đệ quy)")
root.geometry("400x200")

label = tk.Label(root, text="Nhập mảng số nguyên (cách nhau bằng dấu cách):")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn = tk.Button(root, text="Tính", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(root, text="Trung bình số âm: ")
result_label.pack(pady=5)

root.mainloop()
