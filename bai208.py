import tkinter as tk
from tkinter import messagebox

# ===== Node Linked List =====
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ===== Linked List =====
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def to_list(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def move_last_m_to_front(self, m):
        if not self.head or m == 0:
            return

        # đếm độ dài
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next

        if m >= length:
            return

        # tìm vị trí cắt
        cut_pos = length - m
        temp = self.head

        for _ in range(cut_pos - 1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = self.head
        self.head = new_head

# ===== GUI =====

def process():
    try:
        arr = list(map(int, entry_list.get().split()))
        m = int(entry_m.get())

        ll = LinkedList()
        for x in arr:
            ll.append(x)

        ll.move_last_m_to_front(m)

        result = ll.to_list()
        result_label.config(text="Kết quả: " + " ".join(map(str, result)))
    except:
        messagebox.showerror("Lỗi", "Nhập không hợp lệ")

root = tk.Tk()
root.title("Danh sách liên kết - Đổi m phần tử cuối lên đầu")
root.geometry("500x250")

label1 = tk.Label(root, text="Nhập danh sách (cách nhau bằng dấu cách):")
label1.pack(pady=5)

entry_list = tk.Entry(root, width=50)
entry_list.pack(pady=5)

label2 = tk.Label(root, text="Nhập m:")
label2.pack(pady=5)

entry_m = tk.Entry(root)
entry_m.pack(pady=5)

btn = tk.Button(root, text="Thực hiện", command=process)
btn.pack(pady=10)

result_label = tk.Label(root, text="Kết quả: ")
result_label.p
