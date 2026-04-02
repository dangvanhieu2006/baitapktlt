import tkinter as tk

def hien_bang_cuu_chuong():
    text.delete("1.0", tk.END)  # xóa nội dung cũ
    
    for i in range(2, 10):
        text.insert(tk.END, f"Bảng cửu chương {i}:\n")
        for j in range(1, 11):
            text.insert(tk.END, f"{i} x {j} = {i*j}\n")
        text.insert(tk.END, "\n")

# Tạo cửa sổ
root = tk.Tk()
root.title("Bảng cửu chương 2-9")
root.geometry("400x400")

# Nút bấm
btn = tk.Button(root, text="Hiển thị bảng cửu chương", command=hien_bang_cuu_chuong)
btn.pack(pady=10)

# Vùng hiển thị kết quả
text = tk.Text(root, width=40, height=20)
text.pack()

# Chạy chương trình
root.mainloop()
