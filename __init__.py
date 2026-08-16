"""QGIS entry point for the Processing Script Reload plugin."""


def classFactory(iface):
    from .processing_script_reload import ProcessingScriptReloadPlugin

    return ProcessingScriptReloadPlugin(iface)
