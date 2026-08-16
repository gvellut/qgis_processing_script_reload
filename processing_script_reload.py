from qgis.core import Qgis, QgsApplication, QgsMessageLog
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtGui import QAction


class ProcessingScriptReloadPlugin:
    MENU_NAME = "&Processing Script Reload"
    LOG_NAME = "Processing Script Reload"

    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def tr(self, text):
        return QCoreApplication.translate("ProcessingScriptReloadPlugin", text)

    def initGui(self):
        self.action = QAction(
            QgsApplication.getThemeIcon("/mActionRefresh.svg"),
            self.tr("Refresh"),
            self.iface.mainWindow(),
        )
        self.action.setObjectName("processingScriptReloadRefreshAction")
        self.action.setToolTip(self.tr("Refresh Processing scripts"))
        self.action.triggered.connect(self.refresh)

        self.iface.addPluginToMenu(self.MENU_NAME, self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        if self.action is None:
            return

        self.iface.removePluginMenu(self.MENU_NAME, self.action)
        self.iface.removeToolBarIcon(self.action)
        self.action.deleteLater()
        self.action = None

    def refresh(self):
        provider = QgsApplication.processingRegistry().providerById("script")
        if provider is None:
            self._show_message(
                self.tr("The Processing Scripts provider is not available."),
                Qgis.MessageLevel.Critical,
            )
            return

        try:
            provider.refreshAlgorithms()
        except Exception as error:
            message = self.tr("Could not refresh Processing scripts: {error}").format(
                error=error
            )
            QgsMessageLog.logMessage(
                message,
                self.LOG_NAME,
                Qgis.MessageLevel.Critical,
            )
            self._show_message(message, Qgis.MessageLevel.Critical)
            return

        count = len(provider.algorithms())
        message = self.tr("Loaded {count} Processing script(s).").format(count=count)
        QgsMessageLog.logMessage(
            message,
            self.LOG_NAME,
            Qgis.MessageLevel.Success,
        )
        self._show_message(message, Qgis.MessageLevel.Success)

    def _show_message(self, message, level):
        self.iface.messageBar().pushMessage(
            self.tr("Processing scripts"),
            message,
            level=level,
            duration=5,
        )
