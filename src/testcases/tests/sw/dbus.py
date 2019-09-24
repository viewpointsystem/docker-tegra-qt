import logging
import json
import os
import asyncio
from dbus_next.aio import MessageBus
from PySide2.QtCore import Property, Signal, Slot, QObject, QThread, QTimer
from time import sleep

logger = logging.getLogger(__name__)

SYSTEM_DBUS_ADDRESS = "unix:path=/var/run/dbus/system_bus_socket"

with open(os.path.join('/tmp/dbus/cookie')) as f:
    SESSION_DBUS_ADDRESS = f.readline().strip('\n')

DBUS_NAME = "org.testcases.gst"
DBUS_PATH = "/org/testcases/gst"
DBUS_IFACE = "org.testcases.gst.SimplePlayer"

class DbusService(QObject):

    stateChanged = Signal(str)
    addressChanged = Signal(str)
   
    
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self._address = SESSION_DBUS_ADDRESS
        self._player = None
        self._state = None
        asyncio.ensure_future(self._setup())

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address
        self.addressChanged.emit(self._address)
    
    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state
        self.stateChanged.emit(self._state)

    state = Property(str, getState, setState, notify=stateChanged)
    address = Property(str, getAddress, setAddress, notify=addressChanged)

    @Slot()
    def play(self):
           asyncio.ensure_future(self._play())

    @Slot()
    def stop(self):
        raise NotImplementedError

    @Slot()
    def stop(self):
        raise NotImplementedError

    async def _play(self):
        """Plays a test pipeline for 10 seconds"""
        if not self.player:
            self._setup()
        try:
            r = await self.player.call_init()
            logger.debug(r)
            r = await self.player.call_play()
            logger.debug(r)
            sleep(10)
            r = await self.player.call_stop()
            logger.debug(r)
        except Exception as e:
            logger.error(e)

    async def _setup(self):
        """Init the dbus session and gst player"""
        try:
            bus = await MessageBus(bus_address=self._address).connect()
            logger.debug("Trying to setup")
            introspection = await bus.introspect(DBUS_NAME, DBUS_PATH)
            logger.debug("Registered interfaces: %s" % str([i.name for i in introspection.interfaces]))
            proxy_object = bus.get_proxy_object(DBUS_NAME, DBUS_PATH, introspection)
            self.player = proxy_object.get_interface(DBUS_IFACE)
        except Exception as e:
            logger.error(e)
            

    async def _update(self):
        """currently does nothing"""
        introspection = None
        try:
            QTimer.singleShot(1000 * 10, lambda: asyncio.ensure_future(self._update()))

        except Exception as e:
            logger.error(e)

