from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")


# # Kết nối tới db
# conn = sqlite3.connect('QuanLySV.db')
# c = conn.cursor()
#
# # Tao bang de luu tru
# c.execute('''
#     CREATE TABLE students(
#         id_student INTEGER PRIMARY KEY AUTOINCREMENT,
#         last_name text,
#         first_name text,
#         id_class text,
#         year text,
#         AVG integer
#     )
# '''
# )

def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('QuanLySV.db')
    c = conn.cursor()

    # Lấy dữ liệu đã nhập
    id_student_value = id_student.get()
    lastname_value = l_name.get()
    name_value = f_name.get()
    id_class_value = id_class.get()
    year_value = year.get()
    AVG_value = avg.get()

    # Thực hiện câu lệnh để thêm
    c.execute('''
            INSERT INTO 
            students (id_student, last_name, first_name, id_class, year, AVG)
            VALUES 
            (:id_student, :last_name, :first_name, :id_class,:year, :AVG)
        ''', {
        'id_student': id_student_value,
        'last_name': lastname_value,
        'first_name': name_value,
        'id_class': id_class_value,
        'year': year_value,
        'AVG': AVG_value,
    }
              )
    conn.commit()
    conn.close()

    # Reset form
    id_student.delete(0, END)
    l_name.delete(0, END)
    f_name.delete(0, END)
    id_class.delete(0, END)
    year.delete(0, END)
    avg.delete(0, END)

    # Hien thi lai du lieu
    truy_van()

def xoa():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('QuanLySV.db')
    c = conn.cursor()
    c.execute('''DELETE FROM
                            students 
                          WHERE id_student=:id_student''',
              {'id_student': delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    # Hiên thi thong bao
    messagebox.showinfo("Thông báo", "Đã xóa!")
    # Hiển thị lại dữ liệu
    truy_van()

def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('QuanLySV.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3]))

    # Ngat ket noi
    conn.close()
def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('QuanLySV.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM students WHERE id_student=:id_student", {'id_student':record_id})
    records = c.fetchall()

    global id_student_editor, l_name_editor, f_name_editor, id_class_editor, year_editor, avg_editor

    id_student_editor = Entry(editor, width=30)
    id_student_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=2, column=1)
    id_class_editor = Entry(editor, width=30)
    id_class_editor.grid(row=3, column=1)
    year_editor = Entry(editor, width=30)
    year_editor.grid(row=4, column=1)
    avg_editor = Entry(editor, width=30)
    avg_editor.grid(row=5, column=1)


    id_student_label = Label(editor, text="Mã sinh viên")
    id_student_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Họ")
    l_name_label.grid(row=1, column=0)
    f_name_label = Label(editor, text="Tên")
    f_name_label.grid(row=2, column=0)
    id_class_label = Label(editor, text="Mã lớp")
    id_class_label.grid(row=3, column=0)
    year_label = Label(editor, text="Năm nhập học")
    year_label.grid(row=4, column=0)
    avg_label = Label(editor, text="Điểm trung bình")
    avg_label.grid(row=5, column=0)

    for record in records:
        id_student_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        f_name_editor.insert(0, record[2])
        id_class_editor.insert(0, record[3])
        year_editor.insert(0, record[4])
        avg_editor.insert(0, record[5])

    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhap)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
def cap_nhap():
    conn = sqlite3.connect('QuanLySV.db')
    c = conn.cursor()
    record_id = id_student_editor.get()

    # Thực hiện câu lệnh UPDATE
    c.execute("""UPDATE students SET
            last_name = :last,
            first_name = :first,
            id_class = :id_class,
            year = :year,
            AVG = :avg
            WHERE id_student = :id_student""",
              {
                  'last': l_name_editor.get(),
                  'first': f_name_editor.get(),
                  'id_class': id_class_editor.get(),
                  'year': year_editor.get(),
                  'avg': avg_editor.get(),
                  'id_student': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    truy_van()


# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
id_student = Entry(input_frame, width=30)
id_student.grid(row=0, column=1, pady=(10, 0))
l_name = Entry(input_frame, width=30)
l_name.grid(row=1, column=1)
f_name = Entry(input_frame, width=30)
f_name.grid(row=2, column=1, padx=20) #pady=(10, 0))
id_class = Entry(input_frame, width=30)
id_class.grid(row=3, column=1)
year = Entry(input_frame, width=30)
year.grid(row=4, column=1)
avg = Entry(input_frame, width=30)
avg.grid(row=5, column=1)

# Các nhãn
id_student_label = Label(input_frame, text="Mã sinh viên")
id_student_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(input_frame, text="Họ")
l_name_label.grid(row=1, column=0) #pady=(10, 0))
f_name_label = Label(input_frame, text="Tên")
f_name_label.grid(row=2, column=0)
id_class_label = Label(input_frame, text="Mã lớp")
id_class_label.grid(row=3, column=0)
year_label = Label(input_frame, text="Năm nhập học")
year_label.grid(row=4, column=0)
avg_label = Label(input_frame, text="Điểm trung bình")
avg_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID Student", "Họ", "Tên")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
for column in columns:
    tree.column(column, anchor=CENTER) # This will center text in rows
    tree.heading(column, text=column)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()