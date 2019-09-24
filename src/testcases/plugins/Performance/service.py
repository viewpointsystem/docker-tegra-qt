
import os 
from PySide2.QtCore import Property, Signal, Slot, QObject 



class PerformanceService(QObject):     
    def __init__(self, parent=None):         
        super().__init__(parent)     
        
    @Slot(int)     
    def setPerformance(self, mode):         
        raise NotImplemntedError

