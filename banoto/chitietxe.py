# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chitietxe.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chitiet_xe(object):
    def setupUi(self, chitiet_xe):
        chitiet_xe.setObjectName("chitiet_xe")
        chitiet_xe.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(chitiet_xe)
        self.centralwidget.setObjectName("centralwidget")
        self.hinh = QtWidgets.QLabel(self.centralwidget)
        self.hinh.setGeometry(QtCore.QRect(400, 30, 361, 261))
        self.hinh.setFrameShape(QtWidgets.QFrame.Box)
        self.hinh.setText("")
        self.hinh.setObjectName("hinh")
        self.txt_masp = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_masp.setGeometry(QtCore.QRect(130, 30, 161, 31))
        self.txt_masp.setObjectName("txt_masp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 31))
        self.label_2.setObjectName("label_2")
        self.txt_nsx = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nsx.setGeometry(QtCore.QRect(130, 90, 161, 31))
        self.txt_nsx.setObjectName("txt_nsx")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 101, 31))
        self.label_3.setObjectName("label_3")
        self.txt_tensp = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_tensp.setGeometry(QtCore.QRect(130, 150, 161, 31))
        self.txt_tensp.setObjectName("txt_tensp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 101, 31))
        self.label_4.setObjectName("label_4")
        self.txt_namsx = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_namsx.setGeometry(QtCore.QRect(130, 210, 161, 31))
        self.txt_namsx.setObjectName("txt_namsx")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 330, 101, 31))
        self.label_5.setObjectName("label_5")
        self.txt_mau = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_mau.setGeometry(QtCore.QRect(130, 330, 161, 31))
        self.txt_mau.setObjectName("txt_mau")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.label_7.setObjectName("label_7")
        self.txt_gianhap = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_gianhap.setGeometry(QtCore.QRect(130, 270, 161, 31))
        self.txt_gianhap.setObjectName("txt_gianhap")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 390, 101, 31))
        self.label_6.setObjectName("label_6")
        self.txt_giamgia = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_giamgia.setGeometry(QtCore.QRect(130, 450, 161, 31))
        self.txt_giamgia.setObjectName("txt_giamgia")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(10, 450, 101, 31))
        self.label_34.setObjectName("label_34")
        self.txt_giaban = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_giaban.setGeometry(QtCore.QRect(130, 390, 161, 31))
        self.txt_giaban.setObjectName("txt_giaban")
        self.txt_sl = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sl.setGeometry(QtCore.QRect(130, 510, 161, 31))
        self.txt_sl.setObjectName("txt_sl")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(10, 510, 101, 31))
        self.label_17.setObjectName("label_17")
        self.cbb_anhxe = QtWidgets.QComboBox(self.centralwidget)
        self.cbb_anhxe.setGeometry(QtCore.QRect(400, 310, 361, 22))
        self.cbb_anhxe.setObjectName("cbb_anhxe")
        self.btn_layanh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_layanh.setGeometry(QtCore.QRect(400, 360, 361, 28))
        self.btn_layanh.setObjectName("btn_layanh")
        self.btn_themsp_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_themsp_2.setGeometry(QtCore.QRect(400, 400, 93, 31))
        self.btn_themsp_2.setObjectName("btn_themsp_2")
        self.btn_suasp_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_suasp_2.setGeometry(QtCore.QRect(400, 440, 93, 31))
        self.btn_suasp_2.setObjectName("btn_suasp_2")
        self.btn_xoasp_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_xoasp_2.setGeometry(QtCore.QRect(400, 480, 93, 31))
        self.btn_xoasp_2.setObjectName("btn_xoasp_2")
        self.btn_luusp_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_luusp_2.setGeometry(QtCore.QRect(400, 520, 93, 31))
        self.btn_luusp_2.setObjectName("btn_luusp_2")
        self.btn_dathang = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dathang.setGeometry(QtCore.QRect(540, 400, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dathang.setFont(font)
        self.btn_dathang.setObjectName("btn_dathang")
        chitiet_xe.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(chitiet_xe)
        self.statusbar.setObjectName("statusbar")
        chitiet_xe.setStatusBar(self.statusbar)

        self.retranslateUi(chitiet_xe)
        QtCore.QMetaObject.connectSlotsByName(chitiet_xe)

    def retranslateUi(self, chitiet_xe):
        _translate = QtCore.QCoreApplication.translate
        chitiet_xe.setWindowTitle(_translate("chitiet_xe", "Chi tiết xe"))
        self.label.setText(_translate("chitiet_xe", "Mã sản phẩm"))
        self.label_2.setText(_translate("chitiet_xe", "Nhà sản xuất"))
        self.label_3.setText(_translate("chitiet_xe", "Tên"))
        self.label_4.setText(_translate("chitiet_xe", "Năm sản xuất"))
        self.label_5.setText(_translate("chitiet_xe", "Phân loại"))
        self.label_7.setText(_translate("chitiet_xe", "Giá nhập"))
        self.label_6.setText(_translate("chitiet_xe", "Giá bán"))
        self.label_34.setText(_translate("chitiet_xe", "Giảm giá(%)"))
        self.label_17.setText(_translate("chitiet_xe", "Số lượng"))
        self.btn_layanh.setText(_translate("chitiet_xe", "Lấy file ảnh"))
        self.btn_themsp_2.setText(_translate("chitiet_xe", "Làm mới"))
        self.btn_suasp_2.setText(_translate("chitiet_xe", "Sửa"))
        self.btn_xoasp_2.setText(_translate("chitiet_xe", "Xóa"))
        self.btn_luusp_2.setText(_translate("chitiet_xe", "Thêm"))
        self.btn_dathang.setText(_translate("chitiet_xe", "Đặt hàng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chitiet_xe = QtWidgets.QMainWindow()
    ui = Ui_chitiet_xe()
    ui.setupUi(chitiet_xe)
    chitiet_xe.show()
    sys.exit(app.exec_())
