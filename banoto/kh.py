# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kh.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Khachhang(object):
    def setupUi(self, Khachhang):
        Khachhang.setObjectName("Khachhang")
        Khachhang.resize(1044, 673)
        self.tab_kh = QtWidgets.QTabWidget(Khachhang)
        self.tab_kh.setGeometry(QtCore.QRect(0, 0, 1041, 641))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab_kh.setFont(font)
        self.tab_kh.setObjectName("tab_kh")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tb_dssp = QtWidgets.QTableWidget(self.tab)
        self.tb_dssp.setGeometry(QtCore.QRect(0, 0, 1041, 611))
        self.tb_dssp.setObjectName("tb_dssp")
        self.tb_dssp.setColumnCount(0)
        self.tb_dssp.setRowCount(0)
        self.tab_kh.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.tb_donhang = QtWidgets.QTableWidget(self.widget)
        self.tb_donhang.setGeometry(QtCore.QRect(0, 120, 1031, 291))
        self.tb_donhang.setObjectName("tb_donhang")
        self.tb_donhang.setColumnCount(0)
        self.tb_donhang.setRowCount(0)
        self.tab_kh.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.txt_tenkh = QtWidgets.QLineEdit(self.tab_2)
        self.txt_tenkh.setGeometry(QtCore.QRect(440, 30, 301, 41))
        self.txt_tenkh.setObjectName("txt_tenkh")
        self.txt_dckh = QtWidgets.QLineEdit(self.tab_2)
        self.txt_dckh.setGeometry(QtCore.QRect(440, 90, 301, 41))
        self.txt_dckh.setObjectName("txt_dckh")
        self.txt_sdtkh = QtWidgets.QLineEdit(self.tab_2)
        self.txt_sdtkh.setGeometry(QtCore.QRect(440, 150, 301, 41))
        self.txt_sdtkh.setObjectName("txt_sdtkh")
        self.txt_emailkh = QtWidgets.QLineEdit(self.tab_2)
        self.txt_emailkh.setGeometry(QtCore.QRect(440, 210, 301, 41))
        self.txt_emailkh.setObjectName("txt_emailkh")
        self.txt_uname = QtWidgets.QLineEdit(self.tab_2)
        self.txt_uname.setGeometry(QtCore.QRect(440, 270, 301, 41))
        self.txt_uname.setObjectName("txt_uname")
        self.txt_pass = QtWidgets.QLineEdit(self.tab_2)
        self.txt_pass.setGeometry(QtCore.QRect(440, 330, 301, 41))
        self.txt_pass.setObjectName("txt_pass")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(220, 30, 171, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 171, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(220, 150, 171, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(220, 210, 171, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(220, 270, 171, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(220, 330, 171, 41))
        self.label_6.setObjectName("label_6")
        self.btn_luutt = QtWidgets.QPushButton(self.tab_2)
        self.btn_luutt.setGeometry(QtCore.QRect(612, 400, 131, 41))
        self.btn_luutt.setObjectName("btn_luutt")
        self.tab_kh.addTab(self.tab_2, "")

        self.retranslateUi(Khachhang)
        self.tab_kh.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Khachhang)

    def retranslateUi(self, Khachhang):
        _translate = QtCore.QCoreApplication.translate
        Khachhang.setWindowTitle(_translate("Khachhang", "Form"))
        self.tab_kh.setTabText(self.tab_kh.indexOf(self.tab), _translate("Khachhang", "Sản phẩm"))
        self.tab_kh.setTabText(self.tab_kh.indexOf(self.widget), _translate("Khachhang", "Đơn hàng"))
        self.label.setText(_translate("Khachhang", "Họ và tên"))
        self.label_2.setText(_translate("Khachhang", "Địa chỉ"))
        self.label_3.setText(_translate("Khachhang", "Số điện thoại"))
        self.label_4.setText(_translate("Khachhang", "Email"))
        self.label_5.setText(_translate("Khachhang", "Tên đăng nhập"))
        self.label_6.setText(_translate("Khachhang", "Mật khẩu"))
        self.btn_luutt.setText(_translate("Khachhang", "Lưu thông tin"))
        self.tab_kh.setTabText(self.tab_kh.indexOf(self.tab_2), _translate("Khachhang", "Cá nhân"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Khachhang = QtWidgets.QWidget()
    ui = Ui_Khachhang()
    ui.setupUi(Khachhang)
    Khachhang.show()
    sys.exit(app.exec_())
