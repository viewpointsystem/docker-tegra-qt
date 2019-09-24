
from PySide2 import QtWidgets
from PySide2 import QtGui


# quickfix monkeypatch QtGui for quamash
def monkeypatch_qt():
    QtGui.QApplication = QtWidgets.QApplication