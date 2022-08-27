#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fnmatch import translate
import os
import locale
import subprocess
import byebye_ui
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.QtCore import (
    pyqtSignal, pyqtSlot, Qt, QEvent,
    QTranslator, QCoreApplication)


class ByeBye(QDialog):
    lblimg_cancel_clicked = pyqtSignal()
    lblimg_switchuser_clicked = pyqtSignal()
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

        self._translate = QCoreApplication.translate
        self._byebye_translator = QTranslator()
        self._qtbasetranslator = QTranslator()

        self._locale = locale.getdefaultlocale()[0]
        self.change_language()

        self.connect_connections()
        self.install_event_filters()

    def change_language(self):
        """Change language depends of system locale."""
        if self._locale == "ru_RU":
            self._byebye_translator.load(":/lang/Translations/qtbase_ru.qm")
            self._byebye_translator.load(":/lang/Translations/byebye_ru.qm")
            QApplication.installTranslator(self._byebye_translator)

        else:
            self._byebye_translator.load(":/lang/Translations/qtbase_en.qm")
            self._byebye_translator.load(":/lang/Translations/byebye_en.qm")

        QApplication.installTranslator(self._qtbasetranslator)

    def changeEvent(self, e):
        """Retranslate the app when called event LanguageChange."""
        if e.type() == QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        else:
            QWidget.changeEvent(self, e)

    def connect_connections(self):
        """Connect connections."""
        self.lblimg_cancel_clicked.connect(self.cancel_clicked)
        self.lblimg_switchuser_clicked.connect(self.switchuser_clicked)
        self.lblimg_logout_clicked.connect(self.logout_clicked)
        self.lblimg_reboot_clicked.connect(self.reboot_clicked)
        self.lblimg_shutdown_clicked.connect(self.shutdown_clicked)
        self.lblimg_suspend_clicked.connect(self.suspend_clicked)
        self.lblimg_hibernate_clicked.connect(self.hibernate_clicked)
        self.lblimg_lock_clicked.connect(self.lock_clicked)

    def install_event_filters(self):
        """Install my event filters."""
        self.ui.lblimg_cancel.installEventFilter(self)
        self.ui.lblimg_switchuser.installEventFilter(self)
        self.ui.lblimg_logout.installEventFilter(self)
        self.ui.lblimg_reboot.installEventFilter(self)
        self.ui.lblimg_shutdown.installEventFilter(self)
        self.ui.lblimg_suspend.installEventFilter(self)
        self.ui.lblimg_hibernate.installEventFilter(self)
        self.ui.lblimg_lock.installEventFilter(self)

    @pyqtSlot()
    def cancel_clicked(self):
        """Cancel."""
        self.close()

    @pyqtSlot()
    def logout_clicked(self):
        """Logout."""
        id = subprocess.check_output(["pgrep", "qtile"]).decode(
            "utf-8").strip().splitlines()[0]
        os.system(f"kill -15 {id}")

    @pyqtSlot()
    def switchuser_clicked(self):
        """Switch User."""
        os.system("dm-tool switch-to-greeter")
        self.close()

    @pyqtSlot()
    def reboot_clicked(self):
        """Reboot."""
        os.system("systemctl reboot")

    @pyqtSlot()
    def shutdown_clicked(self):
        """Shutdown."""
        os.system("systemctl poweroff")

    @pyqtSlot()
    def suspend_clicked(self):
        """Suspend."""
        os.system("systemctl suspend")
        self.close()

    @pyqtSlot()
    def hibernate_clicked(self):
        """Hibernate."""
        os.system("systemctl hibernate")
        self.close()

    @pyqtSlot()
    def lock_clicked(self):
        """Lock."""
        os.system("$HOME/.myScripts/system_exit/lock.sh")
        # os.system("i3lock")
        # os.system("slock")
        self.close()

    def eventFilter(self, obj, e):
        """
        My events for lblimg_... .
        :param obj:
        :param e:
        :return QtWidgets.QWidget.eventFilter(self, obj, e):
        """
        if obj == self.ui.lblimg_cancel:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_cancel_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_switchuser:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_switchuser_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_logout:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_logout_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_reboot:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_reboot_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_shutdown:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_shutdown_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_suspend:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_suspend_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_hibernate:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_hibernate_clicked.emit()
                    return True
        elif obj == self.ui.lblimg_lock:
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.lblimg_lock_clicked.emit()
                    return True
        # pass the event on to the parent class.
        return QDialog.eventFilter(self, obj, e)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    byebye = ByeBye()
    byebye.show()
    sys.exit(app.exec_())
