from PySide2.QtQml import qmlRegisterType, QQmlExtensionPlugin


class PluginRegistry:
    """Utility class for loading qml types"""

    def __init__(self, plugins=None, template_path=None):
        self.plugins = []
        for p in plugins:
            qmlRegisterType(
                p, 
                p.verbose_name, 
                p.version.major, 
                p.version.minor, 
                p.service_name
            )
            self.plugins.append(plugins)

    @classmethod
    def from_path(paths):
        """Give a dotted path list will auto-discover plugins"""
        raise NotImplementedError