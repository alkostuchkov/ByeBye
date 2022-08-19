#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import byebye_ui
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class ByeBye(QDialog):
    lblimg_cancel_clicked = pyqtSignal()
    lblimg_logout_clicked = pyqtSignal()
    lblimg_reboot_clicked = pyqtSignal()
    lblimg_shutdown_clicked = pyqtSignal()
    lblimg_suspend_clicked = pyqtSignal()
    lblimg_hibernate_clicked = pyqtSignal()
    lblimg_lock_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.ui = byebye_ui.Ui_dlg_byebye()
        self.ui.setupUi(self)

        self.connect_connections()
        self.install_event_filters()

    def connect_connections(self):
        """Connect connections."""
        self.lblimg_cancel_clicked.connect(self.cancel_clicked)
        self.lblimg_logout_clicked.connect(self.logout_clicked)
        self.lblimg_reboot_clicked.connect(self.reboot_clicked)
        self.lblimg_shutdown_clicked.connect(self.shutdown_clicked)
        self.lblimg_suspend_clicked.connect(self.suspend_clicked)
        self.lblimg_hibernate_clicked.connect(self.hibernate_clicked)
        self.lblimg_lock_clicked.connect(self.lock_clicked)

    def install_event_filters(self):
        """Install my event filters."""
        self.ui.lblimg_cancel.installEventFilter(self)
        self.ui.lblimg_logout.installEventFilter(self)
        self.ui.lblimg_reboot.installEventFilter(self)
        self.ui.lblimg_shutdown.installEventFilter(self)
        self.ui.lblimg_suspend.installEventFilter(self)
        self.ui.lblimg_hibernate.installEventFilter(self)
        self.ui.lblimg_lock.installEventFilter(self)

    @pyqtSlot()
    def cancel_clicked(self):
        pass

    @pyqtSlot()
    def logout_clicked(self):
        pass

    @pyqtSlot()
    def reboot_clicked(self):
        pass

    @pyqtSlot()
    def shutdown_clicked(self):
        pass

    @pyqtSlot()
    def suspend_clicked(self):
        pass

    @pyqtSlot()
    def hibernate_clicked(self):
        pass

    @pyqtSlot()
    def lock_clicked(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    byebye = ByeBye()
    byebye.show()
    sys.exit(app.exec_())
