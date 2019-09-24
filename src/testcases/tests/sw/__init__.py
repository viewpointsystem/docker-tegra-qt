from PySide2.QtQml import qmlRegisterType, QQmlExtensionPlugin
  
from .dbus import DbusService

qmlRegisterType(DbusService, "Dbus", 1, 0, "DbusService")
