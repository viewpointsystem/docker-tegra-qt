#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import os
import logging
import colorlog
import asyncio
import ctypes

import tracemalloc
import linecache
#os.environ["QML2_IMPORT_PATH"] = "plugins"
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
from testcases.utils import monkeypatch_qt
# :from testcases.utils.memory import show_memory
monkeypatch_qt()

from PySide2.QtCore import QObject
from PySide2.QtGui import QGuiApplication,  QTouchDevice, QCursor
from PySide2.QtQml import qmlRegisterType
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtPositioning import *

from quamash import QEventLoop, QThreadExecutor

from testcases.tests.sw import dbus


LOG_LEVEL = os.environ.get("LOG_LEVEL", default="DEBUG")
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "(%(asctime)s) [%(log_color)s%(levelname)s] | %(name)s | %(message)s [%(threadName)-10s]"))

logger = logging.getLogger()

logger.addHandler(handler)
logger.setLevel(LOG_LEVEL)
# remove quamash debug logging as its very 
logging.getLogger("quamash").setLevel(logging.WARNING)

class Application:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)

        self.touchscreens = list(filter(lambda d: d.type() == QTouchDevice.TouchScreen, QTouchDevice.devices()))
        if self.touchscreens:
            logger.info("touchscreens detected, disabling mouse: %s" % self.touchscreens)
            # self.app.setOverrideCursor(QCursor(Qt.BlankCursor))
        else:
            logger.error("No touchscreen detected!")

        self.engine = QQmlApplicationEngine()
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)

    def run(self):
        tracemalloc.start(25)
        self.engine.load("ui/window.qml")
        self.win = self.engine.rootObjects()[0]
        self.win.show() 

        with self.loop: ## context manager calls .close() when loop completes, and releases all resources
            self.loop.run_forever()


if __name__ == "__main__":
    app = Application()
    app.run()