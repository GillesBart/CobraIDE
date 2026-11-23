"""
This module contains the tab bar used in the splittable tab widget.
"""
from pyqode.qt import QtWidgets, QtCore
from pyqode.core.api import DelayJobRunner


class TabBar(QtWidgets.QTabBar):
    """
    Tab bar specialized to allow the user to close a tab using mouse middle
    click. Also exposes a double clicked signal.
    """
    double_clicked = QtCore.Signal()

    def __init__(self, parent):
        QtWidgets.QTabBar.__init__(self, parent)
        self.setTabsClosable(True)
        self._timer = DelayJobRunner(delay=1)

    def mousePressEvent(self, event):
        QtWidgets.QTabBar.mousePressEvent(self, event)
        if event.button() == QtCore.Qt.MiddleButton:
            tab = self.tabAt(event.pos())
            self._timer.request_job(
                self.parentWidget().tabCloseRequested.emit, tab)

    def mouseDoubleClickEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton:
            return
        index = self.tabAt(event.pos())
        if index < 0:
            # endroit libre de la barre d'onglets
            self.double_clicked.emit()
            return
        # double-clic sur un onglet : fermeture (avec la demande
        # d'enregistrement habituelle si le document est modifié). Différée
        # comme pour le clic du milieu : la fermeture peut détruire la barre
        # qui est en train de traiter l'événement.
        tab_widget = self.parentWidget()
        widget = tab_widget.widget(index)

        def close_tab():
            i = tab_widget.indexOf(widget)
            if i >= 0:
                tab_widget.tabCloseRequested.emit(i)
        QtCore.QTimer.singleShot(0, close_tab)
