# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chitietxe1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chitiet_xe1(object):
    def setupUi(self, chitiet_xe1):
        chitiet_xe1.setObjectName("chitiet_xe1")
        chitiet_xe1.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(chitiet_xe1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 101, 31))
        self.label_6.setObjectName("label_6")
        self.txt_namsx = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_namsx.setGeometry(QtCore.QRect(140, 200, 161, 31))
        self.txt_namsx.setReadOnly(True)
        self.txt_namsx.setObjectName("txt_namsx")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 101, 31))
        self.label_5.setObjectName("label_5")
        self.txt_mau = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_mau.setGeometry(QtCore.QRect(140, 320, 161, 31))
        self.txt_mau.setReadOnly(True)
        self.txt_mau.setObjectName("txt_mau")
        self.txt_giamgia = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_giamgia.setGeometry(QtCore.QRect(140, 440, 161, 31))
        self.txt_giamgia.setReadOnly(True)
        self.txt_giamgia.setObjectName("txt_giamgia")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.label.setObjectName("label")
        self.txt_giaban = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_giaban.setGeometry(QtCore.QRect(140, 380, 161, 31))
        self.txt_giaban.setReadOnly(True)
        self.txt_giaban.setObjectName("txt_giaban")
        self.hinh = QtWidgets.QLabel(self.centralwidget)
        self.hinh.setGeometry(QtCore.QRect(410, 20, 361, 261))
        self.hinh.setFrameShape(QtWidgets.QFrame.Box)
        self.hinh.setText("")
        self.hinh.setObjectName("hinh")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.label_2.setObjectName("label_2")
        self.txt_nsx = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nsx.setGeometry(QtCore.QRect(140, 80, 161, 31))
        self.txt_nsx.setReadOnly(True)
        self.txt_nsx.setObjectName("txt_nsx")
        self.txt_tensp = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_tensp.setGeometry(QtCore.QRect(140, 140, 161, 31))
        self.txt_tensp.setReadOnly(True)
        self.txt_tensp.setObjectName("txt_tensp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 101, 31))
        self.label_4.setObjectName("label_4")
        self.cbb_anhxe = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_anhxe.setGeometry(QtCore.QRect(410, 300, 361, 22))
        self.cbb_anhxe.setObjectName("cbb_anhxe")
        self.btn_dathang = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dathang.setGeometry(QtCore.QRect(480, 510, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dathang.setFont(font)
        self.btn_dathang.setObjectName("btn_dathang")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(20, 440, 101, 31))
        self.label_34.setObjectName("label_34")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 500, 101, 31))
        self.label_17.setObjectName("label_17")
        self.txt_gianhap = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_gianhap.setGeometry(QtCore.QRect(140, 260, 161, 31))
        self.txt_gianhap.setReadOnly(True)
        self.txt_gianhap.setObjectName("txt_gianhap")
        self.txt_masp = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_masp.setGeometry(QtCore.QRect(140, 20, 161, 31))
        self.txt_masp.setReadOnly(True)
        self.txt_masp.setObjectName("txt_masp")
        self.txt_sl = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sl.setGeometry(QtCore.QRect(140, 500, 161, 31))
        self.txt_sl.setReadOnly(True)
        self.txt_sl.setObjectName("txt_sl")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 101, 31))
        self.label_7.setObjectName("label_7")
        self.cbb_nv = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_nv.setGeometry(QtCore.QRect(410, 410, 361, 41))
        self.cbb_nv.setObjectName("cbb_nv")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 360, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        chitiet_xe1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(chitiet_xe1)
        self.statusbar.setObjectName("statusbar")
        chitiet_xe1.setStatusBar(self.statusbar)

        self.retranslateUi(chitiet_xe1)
        QtCore.QMetaObject.connectSlotsByName(chitiet_xe1)

    def retranslateUi(self, chitiet_xe1):
        _translate = QtCore.QCoreApplication.translate
        chitiet_xe1.setWindowTitle(_translate("chitiet_xe1", "Chi tiết xe"))
        self.label_6.setText(_translate("chitiet_xe1", "Giá bán"))
        self.label_5.setText(_translate("chitiet_xe1", "Phân loại"))
        self.label.setText(_translate("chitiet_xe1", "Mã sản phẩm"))
        self.label_2.setText(_translate("chitiet_xe1", "Nhà sản xuất"))
        self.label_3.setText(_translate("chitiet_xe1", "Tên"))
        self.label_4.setText(_translate("chitiet_xe1", "Năm sản xuất"))
        self.btn_dathang.setText(_translate("chitiet_xe1", "Đặt hàng"))
        self.label_34.setText(_translate("chitiet_xe1", "Giảm giá(%)"))
        self.label_17.setText(_translate("chitiet_xe1", "Số lượng"))
        self.label_7.setText(_translate("chitiet_xe1", "Giá nhập"))
        self.label_8.setText(_translate("chitiet_xe1", "Chọn nhân viên tư vấn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chitiet_xe1 = QtWidgets.QMainWindow()
    ui = Ui_chitiet_xe1()
    ui.setupUi(chitiet_xe1)
    chitiet_xe1.show()
    sys.exit(app.exec_())
