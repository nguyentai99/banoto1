import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidgetItem
from login import Ui_MainWindow
import pyodbc
from quanly import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from chitietxe import Ui_chitiet_xe
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.btn_login.clicked.connect(self.login)
        self.DRIVER_NAME = 'SQL SERVER'
        self.SERVER_NAME = 'TRUNG\\SQLEXPRESS'
        self.DATABASE_NAME = 'banxe1'
        self.db_config = f"""
                        DRIVER={{{self.DRIVER_NAME}}};
                        SERVER={self.SERVER_NAME};
                        DATABASE={self.DATABASE_NAME};
                        Trust_Connection=yes;
                        """

    def login(self):
        self.username = self.uic.txt_tk.text()
        self.password = self.uic.txt_mk.text()

        try:
            connection = pyodbc.connect(self.db_config)

            with connection.cursor() as cursor:
                # Thực hiện truy vấn SQL để kiểm tra tài khoản và lấy dữ liệu
                sql = "SELECT * FROM Accounts WHERE username=? AND password=?"
                cursor.execute(sql, (self.username, self.password))
                result = cursor.fetchone()
                self.role = result[7]
                print(self.role)
                if result:
                    # Đăng nhập thành công, hiển thị thông tin tài khoản

                    self.quanly()
                else:
                    # Đăng nhập thất bại
                    QMessageBox.warning(self.main_win, "Login Failed", "Invalid username or password")

        except pyodbc.Error as err:
            print(f"Lỗi: {err}")
    def quanly(self):
        self.mh_new = QtWidgets.QMainWindow()
        self.ui1 = Ui_Form()
        self.ui1.setupUi(self.mh_new)
        self.mh_new.show()
        self.main_win.close()

        connection = pyodbc.connect(self.db_config)


        with connection.cursor() as cursor:
            sql = "SELECT * FROM Cars"
            cursor.execute(sql)
            result = cursor.fetchall()
            self.ui1.tb_dssp.setRowCount(0)
            self.ui1.tb_dssp.setRowCount(len(result))
            self.ui1.tb_dssp.setColumnCount(9)
            self.ui1.tb_dssp.setColumnWidth(0, 5)
            self.ui1.tb_dssp.setColumnWidth(6, 5)
            column_names = ["Mã SP", "Hãng", "Loại", "Năm sản xuất", "Phân loại", "Gía bán", "Số lượng", "Giá nhập",
                            "Giảm giá"]
            self.ui1.tb_dssp.setHorizontalHeaderLabels(column_names)
            for row_num, row_data in enumerate(result):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui1.tb_dssp.setItem(row_num, col_num, item)
            self.ui1.tb_dssp.itemSelectionChanged.connect(self.chitietsp)

            sql1 = "SELECT * FROM accounts"
            cursor.execute(sql1)
            result1 = cursor.fetchall()
            self.ui1.tb_dsnv.setRowCount(0)
            self.ui1.tb_dsnv.setRowCount(len(result1))
            self.ui1.tb_dsnv.setColumnCount(9)
            self.ui1.tb_dsnv.setColumnWidth(0, 5)
            column_names1 = ["Mã NV", "Họ", "Tên", "Email", "Số điện thoại", "Tên đăng nhập", "Mật khẩu", "Chức vụ",
                            "Địa chỉ"]
            self.ui1.tb_dsnv.setHorizontalHeaderLabels(column_names1)
            for row_num, row_data in enumerate(result1):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui1.tb_dsnv.setItem(row_num, col_num, item)

            self.ui1.tb_dsnv.itemSelectionChanged.connect(self.row_selected1)
            sql2 = "SELECT * FROM orders"
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            self.ui1.tb_dshoadon.setRowCount(len(result2))
            self.ui1.tb_dshoadon.setColumnCount(7)
            column_names2 = ["Mã HĐ", "Mã KH", "Mã SP", "Ngày", "Thành tiền", "Mã NV", "Hình thức TT"]
            self.ui1.tb_dshoadon.setHorizontalHeaderLabels(column_names2)
            for row_num, row_data in enumerate(result2):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui1.tb_dshoadon.setItem(row_num, col_num, item)
            # Lấy thời gian hiện tại
            sql_kh = "SELECT * FROM Customers"
            cursor.execute(sql_kh)
            result6 = cursor.fetchall()
            self.ui1.tb_kh.setRowCount(0)
            self.ui1.tb_kh.setRowCount(len(result6))
            self.ui1.tb_kh.setColumnCount(5)
            column_names = ["Mã KH", "Tên KH", "Email", "Phone", "Địa chỉ"]
            self.ui1.tb_kh.setHorizontalHeaderLabels(column_names)
            for row_num, row_data in enumerate(result6):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui1.tb_kh.setItem(row_num, col_num, item)
            self.ui1.tb_dssp.itemSelectionChanged.connect(self.chitietsp)
            current_datetime = QDateTime.currentDateTime()
            # Đặt giá trị của QDateTimeEdit thành thời gian hiện tại
            self.ui1.date_hoadon.setDateTime(current_datetime)
            self.ui1.tb_dshoadon.itemSelectionChanged.connect(self.row_selected2)
            self.ui1.btn_themnv.clicked.connect(self.themnv)
            self.ui1.btn_luunv.clicked.connect(self.updatesnv)
            self.ui1.btn_xoanv.clicked.connect(self.xoanv)
            self.ui1.btn_suanv.clicked.connect(self.suanv)
            self.ui1.btn_luhd.clicked.connect(self.themhd)
            self.ui1.txt_suahd.clicked.connect(self.suahd)
            self.ui1.txt_xoahd.clicked.connect(self.xoahd)
            self.ui1.txt_themhd.clicked.connect(self.lammoi)
            self.ui1.btn_thanhtien.clicked.connect(self.tinhtien)
            self.ui1.txt_inhd.clicked.connect(self.xuathd)




    def tinhtien(self):
        connection = pyodbc.connect(self.db_config)
        masp = self.ui1.txt_masp_2.text()
        with connection.cursor() as cursor:
            sql = "SELECT model, price, giamgia from cars where carid = ?"
            cursor.execute(sql,(masp,))
            result = cursor.fetchone()
            self.ui1.txt_tensp_2.setText(str(result[0]))
            self.ui1.txt_dongia.setText(str(result[1]))
            self.ui1.txt_giamgia_2.setText(str(2))
            thanhtien = float(self.ui1.txt_dongia.text()) - float(self.ui1.txt_dongia.text()) * float(
            self.ui1.txt_giamgia_2.text()) / 100
        self.ui1.txt_thanhtien.setText(str(thanhtien))

    def chitietsp(self):
        connection = pyodbc.connect(self.db_config)
        self.mh_chitietxe = QtWidgets.QMainWindow()
        self.ui2 = Ui_chitiet_xe()
        self.ui2.setupUi(self.mh_chitietxe)
        self.mh_chitietxe.show()
        self.ui2.btn_luusp_2.clicked.connect(self.updates)
        self.ui2.btn_themsp_2.clicked.connect(self.themsp)
        self.ui2.btn_xoasp_2.clicked.connect(self.xoasp)
        self.ui2.btn_suasp_2.clicked.connect(self.suasp)
        selected_items = self.ui1.tb_dssp.selectedItems()
        if len(selected_items) > 0:
            # Lấy số dòng được chọn
            selected_row = selected_items[0].row()
            # Lấy dữ liệu từ hàng được chọn
            row_data = []
            for col in range(self.ui1.tb_dssp.columnCount()):
                item = self.ui1.tb_dssp.item(selected_row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")  # Hoặc thêm giá trị mặc định khi ô trống
            self.masp = row_data[0]
            with connection.cursor() as cursor:
                sql = "Select linkanh FROM Cars WHERE CarID = ?"
                cursor.execute(sql, (self.masp,))
                result = cursor.fetchone()
            print(result[0])
            self.link = result[0]
            self.load_images(self.link)
            # Đặt giá trị cho các ô văn bản
            self.ui2.txt_masp.setText(row_data[0])
            self.ui2.txt_nsx.setText(row_data[1])
            self.ui2.txt_tensp.setText(row_data[2])
            self.ui2.txt_namsx.setText(row_data[3])
            self.ui2.txt_mau.setText(row_data[4])
            self.ui2.txt_gianhap.setText(row_data[7])
            self.ui2.txt_giaban.setText(row_data[5])
            self.ui2.txt_sl.setText(row_data[6])
            self.ui2.txt_giamgia.setText(row_data[8])
            self.ui2.btn_layanh.clicked.connect(self.select_folder)
            self.ui2.cbb_anhxe.currentIndexChanged.connect(self.show_selected_image)
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self.mh_chitietxe, "Chọn thư mục", "./")
        # Hiển thị đường dẫn thư mục đã chọn
        if folder_path:
            self.folder_path1 = folder_path
            print(folder_path)
            # Tải danh sách ảnh vào ComboBox
            self.load_images(folder_path)
    def load_images(self, folder_path):
        # Kiểm tra xem thư mục tồn tại không
        if not os.path.exists(folder_path):
            print("Thư mục không tồn tại.")
            return
        # Lấy danh sách tên tệp ảnh từ thư mục
        image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        # Xóa danh sách ảnh cũ trong ComboBox
        self.ui2.cbb_anhxe.clear()
        # Thêm tên các tệp ảnh vào ComboBox
        self.ui2.cbb_anhxe.addItems(image_files)
    def show_selected_image(self, index):
        # Lấy tên tệp ảnh được chọn
        selected_image = self.ui2.cbb_anhxe.currentText()
        # Tạo đường dẫn đầy đủ đến tệp ảnh
        folder_path = self.link
        image_path = os.path.join(folder_path, selected_image)
        if not os.path.exists(image_path):
            print("Tệp ảnh không tồn tại.")
            return
        # Tải ảnh và hiển thị trong QLabel
        pixmap = QPixmap(image_path)
        self.ui2.hinh.setPixmap(pixmap.scaled(361, 261))  # Scale ảnh cho phù hợp với kích thước QLabel
    def row_selected1(self):
        selected_items = self.ui1.tb_dsnv.selectedItems()
        if len(selected_items) > 0:
            # Lấy số dòng được chọn
            selected_row = selected_items[0].row()
            # Lấy dữ liệu từ hàng được chọn
            row_data = []
            for col in range(self.ui1.tb_dsnv.columnCount()):
                item = self.ui1.tb_dsnv.item(selected_row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")  # Hoặc thêm giá trị mặc định khi ô trống
            # Kiểm tra số lượng cột và số lượng phần tử trong row_data
            if len(row_data) >= 9:  # Cần ít nhất 9 cột
                # Đặt giá trị cho các ô văn bản
                self.ui1.txt_manv.setText(row_data[0])
                self.ui1.txt_fname.setText(row_data[1])
                self.ui1.txt_lname.setText(row_data[2])
                self.ui1.txt_email.setText(row_data[3])
                self.ui1.txt_sdt.setText(row_data[4])
                self.ui1.txt_tendn.setText(row_data[5])
                self.ui1.txt_pass.setText(row_data[6])
                # self.ui1.cbb_idnv.setText(row_data[7])  # Kiểm tra xem ComboBox có được sử dụng đúng không
                self.ui1.txt_dc.setText(row_data[8])
                cbb_value = row_data[7]
                # Sử dụng giá trị để thiết lập cho QComboBox
                index = self.ui1.cbb_idnv.findText(cbb_value)
                if index != -1:
                    self.ui1.cbb_idnv.setCurrentIndex(index)
                else:
                    print(f"Lỗi: Giá trị '{cbb_value}' không tồn tại trong QComboBox.")
            else:
                print("Lỗi: Số lượng cột không đúng.")
    def row_selected2(self):
        selected_items = self.ui1.tb_dshoadon.selectedItems()
        if len(selected_items) > 0:
            # Lấy số dòng được chọn
            selected_row = selected_items[0].row()
            # Lấy dữ liệu từ hàng được chọn
            row_data = []
            for col in range(self.ui1.tb_dsnv.columnCount()):
                item = self.ui1.tb_dshoadon.item(selected_row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")  # Hoặc thêm giá trị mặc định khi ô trống

            # Kiểm tra số lượng cột và số lượng phần tử trong row_data
            if len(row_data) >= 7:  # Cần ít nhất 7 cột
                # Đặt giá trị cho các ô văn bản
                self.ui1.txt_mahd.setText(row_data[0])
                self.ui1.txt_makh.setText(row_data[1])
                self.ui1.txt_masp_2.setText(row_data[2])
                self.ui1.txt_manv_2.setText(row_data[5])
                self.ui1.txt_thanhtien.setText(row_data[4])
                self.date_time = str(row_data[3])
            else:
                print("Lỗi: Số lượng cột không đúng.")
        idsp = self.ui1.txt_masp_2.text()
        idnv = self.ui1.txt_manv_2.text()
        idkh = self.ui1.txt_makh.text()
        # print(idsp)
        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cars where carid = ?"
            cursor.execute(sql, (idsp,))
            result = cursor.fetchone()
            print(result)
            self.ui1.txt_tensp_2.setText(str(result[2]))
            self.ui1.txt_dongia.setText(str(result[5]))
            self.ui1.txt_giamgia_2.setText(str(result[8]))
            sql2 = "SELECT lastname,firstname from accounts where salespersonid = ? "
            cursor.execute(sql2,(idnv,))
            result2 = cursor.fetchone()
            print(result2)
            self.ui1.txt_tennv.setText(str(result2[0]+ " " + result2[1]))
            sql3 = "SELECT firstname, address, phone, email from customers where customerid = ?"
            cursor.execute(sql3,(idkh,))
            result3 = cursor.fetchone()
            print(result3)
            self.ui1.txt_tenkh.setText(str(result3[0]))
            self.ui1.txt_dckh.setText(str(result3[1]))
            self.ui1.txt_dtkh.setText(str(result3[2]))
            self.ui1.txt_emailkh.setText(str(result3[3]))
            print(self.date_time)
            datetime_obj = datetime.strptime(self.date_time, '%Y-%m-%d %H:%M:%S')
            # Tách ngày và giờ
            date = datetime_obj.date()
            time = datetime_obj.time()
            self.ui1.date_hoadon.setDate(date)
            self.ui1.date_hoadon.setTime(time)
    def themsp(self):
        self.ui2.txt_masp.clear()
        self.ui2.txt_nsx.clear()
        self.ui2.txt_tensp.clear()
        self.ui2.txt_namsx.clear()
        self.ui2.txt_mau.clear()
        self.ui2.txt_gianhap.clear()
        self.ui2.txt_giaban.clear()
        self.ui2.txt_sl.clear()
        self.ui2.txt_giamgia.clear()
    def themnv(self):
        self.ui1.txt_manv.clear()
        self.ui1.txt_lname.clear()
        self.ui1.txt_fname.clear()
        self.ui1.txt_email.clear()
        self.ui1.txt_sdt.clear()
        self.ui1.txt_tendn.clear()
        self.ui1.txt_pass.clear()
        self.ui1.txt_dc.clear()

    def updates(self):
        make = self.ui2.txt_nsx.text()
        model = self.ui2.txt_tensp.text()
        namsx = int(self.ui2.txt_namsx.text())
        mau = self.ui2.txt_mau.text()
        giaban = float(self.ui2.txt_giaban.text())
        sl = int(self.ui2.txt_sl.text())
        gianhap = float(self.ui2.txt_gianhap.text())
        giamgia = float(self.ui2.txt_giamgia.text())
        idsp = self.ui2.txt_masp.text()
        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Kiểm tra trùng id trước khi thêm mới
                sql_check_id = "SELECT Carid FROM cars WHERE carid = ?"
                cursor.execute(sql_check_id, (idsp,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # Nếu id đã tồn tại, hiển thị thông báo và không thêm mới
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID đã tồn tại. Vui lòng chọn ID khác.")
                else:
                    # Thêm mới sản phẩm vào cơ sở dữ liệu
                    sql_insert = "INSERT INTO cars (carid,make, model, year, classify, price, availability, gianhap, giamgia ,linkanh) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    cursor.execute(sql_insert, (idsp, make, model, namsx, mau, giaban, sl, gianhap, giamgia, self.folder_path1))
                    connection.commit()
                    print("Đã thêm mới sản phẩm.")

                    # Cập nhật danh sách sản phẩm sau khi thêm mới
                    new_product_info = (idsp, make, model, namsx, mau, giaban, sl, gianhap, giamgia)
                    # Lấy số dòng hiện tại của QTableWidget
                    row_position = self.ui1.tb_dssp.rowCount()

                    # Thêm một dòng mới vào QTableWidget
                    self.ui1.tb_dssp.insertRow(row_position)

                    # Đặt giá trị cho các ô trong dòng mới
                    for column, value in enumerate(new_product_info):
                        item = QTableWidgetItem(str(value))
                        self.ui1.tb_dssp.setItem(row_position, column, item)


            except Exception as e:
                # Xử lý nếu có lỗi khi thêm mới
                print(f"Lỗi khi thêm mới sản phẩm: {e}")


    def xoasp(self):
        # Get the CarID you want to delete from the user input or any other source
        id_to_delete = self.ui2.txt_masp.text()

        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Check if the CarID exists before deleting
                sql_check_id = "SELECT CarID FROM cars WHERE CarID = ?"
                cursor.execute(sql_check_id, (id_to_delete,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # CarID exists, proceed with the delete operation
                    sql_delete = "DELETE FROM cars WHERE CarID = ?"
                    cursor.execute(sql_delete, (id_to_delete,))
                    connection.commit()

                    # Remove the row from the QTableWidget
                    selected_row = self.ui1.tb_dssp.currentRow()
                    if selected_row >= 0:
                        self.ui1.tb_dssp.removeRow(selected_row)

                    print("Đã xóa sản phẩm.")
                else:
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID không tồn tại. Vui lòng kiểm tra lại.")

            except Exception as e:
                # Handle errors
                print(f"Lỗi khi xóa sản phẩm: {e}")


    def suasp(self):
        # Get the values to update from the user input or any other source
        id_to_update = self.ui2.txt_masp.text()

        make = self.ui2.txt_nsx.text()
        model = self.ui2.txt_tensp.text()
        namsx = int(self.ui2.txt_namsx.text())
        mau = self.ui2.txt_mau.text()
        giaban = float(self.ui2.txt_giaban.text())
        sl = int(self.ui2.txt_sl.text())
        gianhap = float(self.ui2.txt_gianhap.text())
        giamgia = int(self.ui2.txt_giamgia.text())


        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Check if the CarID exists before updating
                sql_check_id = "SELECT CarID FROM cars WHERE CarID = ?"
                cursor.execute(sql_check_id, (id_to_update,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # CarID exists, proceed with the update operation
                    sql_update = "UPDATE cars SET make=?, model=?, year=?, classify=?, price=?, availability=?, gianhap=?, giamgia=? WHERE CarID=?"
                    cursor.execute(sql_update, (make, model, namsx, mau, giaban, sl, gianhap, giamgia, id_to_update))
                    connection.commit()

                    # Update the data in the QTableWidget
                    selected_row = self.ui1.tb_dssp.currentRow()
                    if selected_row >= 0:
                        for col, value in enumerate(
                                [id_to_update, make, model, namsx, mau, giaban, sl, gianhap, giamgia]):
                            item = QTableWidgetItem(str(value))
                            self.ui1.tb_dssp.setItem(selected_row, col, item)

                    print("Đã cập nhật sản phẩm.")
                else:
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID không tồn tại. Vui lòng kiểm tra lại.")

            except Exception as e:
                # Handle errors
                print(f"Lỗi khi cập nhật sản phẩm: {e}")

    def suanv(self):
        # Get the values to update from the user input or any other source
        id_to_update = self.ui1.txt_manv.text()

        fname = self.ui1.txt_fname.text()
        lname = self.ui1.txt_lname.text()
        email = self.ui1.txt_email.text()
        phone = self.ui1.txt_sdt.text()
        username = self.ui1.txt_tendn.text()
        password = self.ui1.txt_pass.text()
        # role_id = self.ui1.cbb_idnv.text()
        dc = self.ui1.txt_dc.text()
        role = self.ui1.cbb_idnv.currentText()


        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Check if the CarID exists before updating
                sql_check_id = "SELECT salespersonid FROM accounts WHERE salespersonid = ?"
                cursor.execute(sql_check_id, (id_to_update,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # CarID exists, proceed with the update operation
                    sql_update = "UPDATE accounts SET firstname=?, lastname=?, email=?, phone=?, username=?, password=?, address=?  WHERE salespersonid=?"
                    cursor.execute(sql_update, (fname, lname, email, phone, username, password, dc, id_to_update))
                    connection.commit()

                    # Update the data in the QTableWidget
                    selected_row = self.ui1.tb_dsnv.currentRow()
                    if selected_row >= 0:
                        for col, value in enumerate(
                                [id_to_update, fname, lname, email, phone, username, password, role, dc]):
                            item = QTableWidgetItem(str(value))
                            self.ui1.tb_dsnv.setItem(selected_row, col, item)

                    print("Đã cập nhật nhân viên.")
                else:
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID không tồn tại. Vui lòng kiểm tra lại.")

            except Exception as e:
                # Handle errors
                print(f"Lỗi khi cập nhật nhân viên: {e}")


    def updatesnv(self):
        idnv = self.ui1.txt_manv.text()
        fname = self.ui1.txt_fname.text()
        lname = self.ui1.txt_lname.text()
        email = self.ui1.txt_email.text()
        sdt = self.ui1.txt_sdt.text()
        username = self.ui1.txt_tendn.text()
        password = self.ui1.txt_pass.text()
        role = self.ui1.cbb_idnv.currentText()
        dc = self.ui1.txt_dc.text()

        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Kiểm tra trùng id trước khi thêm mới
                sql_check_id = "SELECT salespersonid FROM accounts WHERE salespersonid = ?"
                cursor.execute(sql_check_id, (idnv,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # Nếu id đã tồn tại, hiển thị thông báo và không thêm mới
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID đã tồn tại. Vui lòng chọn ID khác.")
                else:
                    # Thêm mới sản phẩm vào cơ sở dữ liệu
                    sql_insert = "INSERT INTO accounts (salespersonid, firstname, lastname, email, phone, username, password,role_id, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    cursor.execute(sql_insert, (idnv, fname, lname, email, sdt, username, password,role, dc))
                    connection.commit()
                    print("Đã thêm mới nhân viên.")

                    # Cập nhật danh sách sản phẩm sau khi thêm mới
                    new_product_info = (idnv, fname, lname, email, sdt, username, password,role, dc)
                    # Lấy số dòng hiện tại của QTableWidget
                    row_position = self.ui1.tb_dsnv.rowCount()

                    # Thêm một dòng mới vào QTableWidget
                    self.ui1.tb_dsnv.insertRow(row_position)

                    # Đặt giá trị cho các ô trong dòng mới
                    for column, value in enumerate(new_product_info):
                        item = QTableWidgetItem(str(value))
                        self.ui1.tb_dsnv.setItem(row_position, column, item)


            except Exception as e:
                # Xử lý nếu có lỗi khi thêm mới
                print(f"Lỗi khi thêm mới nhân viên: {e}")


    def xoanv(self):
        # Get the CarID you want to delete from the user input or any other source
        id_to_delete = self.ui1.txt_manv.text()

        connection = pyodbc.connect(self.db_config)
        with connection.cursor() as cursor:
            try:
                # Check if the CarID exists before deleting
                sql_check_id = "SELECT salespersonid FROM accounts WHERE salespersonid = ?"
                cursor.execute(sql_check_id, (id_to_delete,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # CarID exists, proceed with the delete operation
                    sql_delete = "DELETE FROM accounts WHERE salespersonid = ?"
                    cursor.execute(sql_delete, (id_to_delete,))
                    connection.commit()

                    # Remove the row from the QTableWidget
                    selected_row = self.ui1.tb_dsnv.currentRow()
                    if selected_row >= 0:
                        self.ui1.tb_dsnv.removeRow(selected_row)

                    print("Đã xóa nhân viên.")
                else:
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID không tồn tại. Vui lòng kiểm tra lại.")

            except Exception as e:
                # Handle errors
                print(f"Lỗi khi xóa nhân viên: {e}")

    def themhd(self):
        mahd = self.ui1.txt_mahd.text()
        manv = self.ui1.txt_manv_2.text()
        tennv = self.ui1.txt_tennv.text()
        makh = self.ui1.txt_makh.text()
        tenkh = self.ui1.txt_tenkh.text()
        diachi = self.ui1.txt_dckh.text()
        dt = self.ui1.txt_dtkh.text()
        masp = self.ui1.txt_masp_2.text()
        tensp = self.ui1.txt_tensp_2.text()
        dongia = float(self.ui1.txt_dongia.text())
        giamgia = float(self.ui1.txt_giamgia_2.text())
        thanhtien = float(self.ui1.txt_thanhtien.text())
        emailkh = self.ui1.txt_emailkh.text()
        ngay_gio_qdatetime = self.ui1.date_hoadon.dateTime()

        # Chuyển đổi QDateTime thành chuỗi ngày và giờ theo định dạng yyyy-MM-dd HH:mm:ss
        ngay_gio = ngay_gio_qdatetime.toString('yyyy-MM-dd HH:mm:ss')

        print(ngay_gio)
        connection = pyodbc.connect(self.db_config)

        with connection.cursor() as cursor:
            try:

                # Kiểm tra trùng id trước khi thêm mới
                sql_check_id = "SELECT orderid FROM orders WHERE orderid = ?"
                cursor.execute(sql_check_id, (mahd,))
                existing_id = cursor.fetchone()
                sql_check_id_kh = "SELECT customerid from customers where customerid = ?"
                cursor.execute(sql_check_id_kh, (makh,))
                result = cursor.fetchone()

                if existing_id:
                    # Nếu id đã tồn tại, hiển thị thông báo và không thêm mới
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID đã tồn tại. Vui lòng chọn ID khác.")
                else:
                    sql_1 = "SELECT Availability From Cars WHERE carid = ?"
                    cursor.execute(sql_1,(masp))
                    re1 = cursor.fetchone()
                    sl = float(re1[0])
                    sl1 = sl -1
                    sql2 = "UPDATE Cars SET Availability = ? WHERE carid = ?"
                    cursor.execute(sql2,(sl1,masp))
                    connection.commit()
                    print(sl1)
                    if result:
                        sql_insert1 = "insert into orders(orderid, customerid, carid, totalamount, salespersonid, orderdate) values(?, ?, ?, ?, ?, ?)"
                        cursor.execute(sql_insert1, (mahd, makh, masp, thanhtien, manv, ngay_gio))

                        connection.commit()
                    else:
                        # Thêm mới sản phẩm vào cơ sở dữ liệu
                        sql_insert = "INSERT INTO customers VALUES (?, ?, ?, ?, ?)"
                        cursor.execute(sql_insert, (makh, tenkh, emailkh, dt, diachi))
                        connection.commit()

                        sql_insert1 = "insert into orders(orderid, customerid, carid, totalamount, salespersonid, orderdate) values(?, ?, ?, ?, ?, ?)"
                        cursor.execute(sql_insert1, (mahd, makh, masp, thanhtien, manv, ngay_gio))
                        connection.commit()

                    # Cập nhật danh sách sản phẩm sau khi thêm mới
                    new_product_info = (mahd, makh, masp, ngay_gio, thanhtien, manv, "")
                    # Lấy số dòng hiện tại của QTableWidget
                    row_position = self.ui1.tb_dshoadon.rowCount()

                    # Thêm một dòng mới vào QTableWidget
                    self.ui1.tb_dshoadon.insertRow(row_position)

                    # Đặt giá trị cho các ô trong dòng mới
                    for column, value in enumerate(new_product_info):
                        item = QTableWidgetItem(str(value))
                        self.ui1.tb_dshoadon.setItem(row_position, column, item)


            except Exception as e:
                # Xử lý nếu có lỗi khi thêm mới
                print(f"Lỗi khi thêm mới hóa đơn: {e}")
    def suahd(self):
        mahd = self.ui1.txt_mahd.text()
        manv = self.ui1.txt_manv_2.text()
        tennv = self.ui1.txt_tennv.text()
        makh = self.ui1.txt_makh.text()
        tenkh = self.ui1.txt_tenkh.text()
        diachi = self.ui1.txt_dckh.text()
        dt = self.ui1.txt_dtkh.text()
        masp = self.ui1.txt_masp_2.text()
        tensp = self.ui1.txt_tensp_2.text()
        dongia = float(self.ui1.txt_dongia.text())
        giamgia = float(self.ui1.txt_giamgia_2.text())
        thanhtien = float(self.ui1.txt_thanhtien.text())
        emailkh = self.ui1.txt_emailkh.text()
        connection = pyodbc.connect(self.db_config)

        with connection.cursor() as cursor:
            try:

                # Kiểm tra trùng id trước khi sửa
                sql_check_id = "SELECT orderid FROM orders WHERE orderid = ?"
                cursor.execute(sql_check_id, (mahd,))
                existing_id = cursor.fetchone()

                if not existing_id:
                    # Nếu id đã tồn tại, hiển thị thông báo và không thêm mới
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID khong tồn tại. Vui lòng chọn ID khác.")
                else:
                    # Thêm mới sản phẩm vào cơ sở dữ liệu
                    sql_insert = "UPDATE customers SET firstname = ?, email = ?, phone = ?, address = ? where customerid = ?"
                    cursor.execute(sql_insert, (tenkh, emailkh, dt, diachi, makh))
                    connection.commit()

                    sql_insert1 = "UPDATE orders SET customerid = ?, carid = ?, totalamount = ? where orderid = ?"
                    cursor.execute(sql_insert1, (makh, masp, thanhtien, mahd))
                    connection.commit()
                    selected_row = self.ui1.tb_dshoadon.currentRow()
                    if selected_row >= 0:
                        for col, value in enumerate(
                                [mahd, makh, masp, "", thanhtien, manv, ""]):
                            item = QTableWidgetItem(str(value))
                            self.ui1.tb_dshoadon.setItem(selected_row, col, item)


            except Exception as e:
                # Xử lý nếu có lỗi khi thêm mới
                print(f"Lỗi khi thêm mới hóa đơn: {e}")


    def xoahd(self):
        mahd = self.ui1.txt_mahd.text()
        makh = self.ui1.txt_makh.text()
        connection = pyodbc.connect(self.db_config)

        with connection.cursor() as cursor:
            try:
                # Kiểm tra trùng id trước khi sửa
                sql_check_id = "SELECT orderid FROM orders WHERE orderid = ?"
                cursor.execute(sql_check_id, (mahd,))
                existing_id = cursor.fetchone()

                if existing_id:
                    # Xóa hóa đơn từ cơ sở dữ liệu
                    sql_delete = """
                        DELETE orders
                        FROM orders
                        WHERE orderid = ?
                    """
                    cursor.execute(sql_delete, (mahd,))
                    connection.commit()

                    # Xóa dòng tương ứng trong danh sách
                    selected_row = self.ui1.tb_dshoadon.currentRow()
                    if selected_row >= 0:
                        self.ui1.tb_dshoadon.removeRow(selected_row)
                    print("Đã xóa hóa đơn.")
                else:
                    # Nếu id không tồn tại, hiển thị thông báo cảnh báo
                    QMessageBox.warning(self.mh_new, "Lỗi", "ID không tồn tại. Vui lòng chọn ID khác.")
            except Exception as e:
                # Xử lý nếu có lỗi khi xóa hóa đơn
                print(f"Lỗi khi xóa hóa đơn: {e}")


    def lammoi(self):
        self.ui1.txt_makh.clear()
        self.ui1.txt_tenkh.clear()
        self.ui1.txt_dckh.clear()
        self.ui1.txt_dtkh.clear()
        self.ui1.txt_emailkh.clear()
        self.ui1.txt_tensp_2.clear()
        self.ui1.txt_dongia.clear()
        self.ui1.txt_giamgia_2.clear()
        self.ui1.txt_thanhtien.clear()
        self.ui1.txt_masp_2.clear()
        current_datetime = QDateTime.currentDateTime()

        # Đặt giá trị của QDateTimeEdit thành thời gian hiện tại
        self.ui1.date_hoadon.setDateTime(current_datetime)
        connection = pyodbc.connect(self.db_config)
        tennv = self.uic.txt_tk.text()
        print(tennv)
        with connection.cursor() as cursor:
            try:
                sql = "SELECT salespersonid, firstname, lastname from accounts where username = ?"
                cursor.execute(sql, (tennv,))
                result = cursor.fetchone()
                self.ui1.txt_manv_2.setText(str(result[0]))
                self.ui1.txt_tennv.setText(str(result[1] + ' ' + result[2]))
                sql1 = "SELECT MAX(orderid) from Orders"
                cursor.execute(sql1)
                result1 = cursor.fetchone()
                mahd = int(result1[0])
                mahd_new = mahd+1
                self.ui1.txt_mahd.setText(str(mahd_new))
                sql2 = "SELECT MAX(customerid) FROM Customers"
                cursor.execute(sql2)
                result2 = cursor.fetchone()
                makh = int(result2[0])
                makh_new = makh +1
                self.ui1.txt_makh.setText(str(makh_new))
            except Exception as e:
                # Xử lý nếu có lỗi khi xóa hóa đơn
                print(f"Lỗi khi làm mới hóa đơn: {e}")

    def xuathd(self):
        mahd = self.ui1.txt_mahd.text()
        manv = self.ui1.txt_manv_2.text()
        tennv = self.ui1.txt_tennv.text()
        makh = self.ui1.txt_makh.text()
        tenkh = self.ui1.txt_tenkh.text()
        diachi = self.ui1.txt_dckh.text()
        dt = self.ui1.txt_dtkh.text()
        masp = self.ui1.txt_masp_2.text()
        tensp = self.ui1.txt_tensp_2.text()
        dongia = str(self.ui1.txt_dongia.text())
        giamgia = str(self.ui1.txt_giamgia_2.text())
        thanhtien = str(self.ui1.txt_thanhtien.text())
        emailkh = self.ui1.txt_emailkh.text()
        ngay_gio_qdatetime = self.ui1.date_hoadon.dateTime()
        ngay_gio = ngay_gio_qdatetime.toString('yyyy-MM-dd HH:mm:ss')
        # Tạo một trang mới với kích thước trang chữ cái
        data = {
            'mahd': mahd,
            'manv': manv,
            'tennv': tennv,
            'masp': masp,
            'tensp': tensp,
            'dongia': dongia,
            'giamgia': giamgia,
            'thanhtien': thanhtien,
            'ngay': ngay_gio
        }
        doc = SimpleDocTemplate('invoic1e.pdf', pagesize=letter)

        # Tạo một stylesheet để sử dụng cho các đoạn văn bản trong hóa đơn
        styles = getSampleStyleSheet()
        normal_style = ParagraphStyle(name='Normal', fontName='Helvetica')
        # Tạo danh sách các nội dung cho hóa đơn
        content = []

        # Thêm các thông tin từ dữ liệu hóa đơn vào nội dung
        content.append(Paragraph("Hóa đơn", styles["Title"]))
        content.append(Paragraph("Ngày : {}".format(data['ngay']), normal_style))
        content.append(Paragraph("Tên nhân viên: {}".format(data['tennv']), normal_style))
        content.append(Paragraph("Tên sản phẩm: {}".format(data['tensp']), normal_style))
        content.append(Paragraph("Gía sản phẩm: {}VND".format(data['dongia']), normal_style))
        content.append(Paragraph("Giảm giá: {}%".format(data['giamgia']), normal_style))
        content.append(Paragraph("Thành tiền: {}VND".format(data['thanhtien']), normal_style))

        # Thêm các thông tin khác tùy theo nhu cầu

        # Thêm nội dung vào tài liệu
        doc.build(content)




    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
