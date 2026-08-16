# Processing Script Reload

A minimal QGIS 4 plugin with one command: **Refresh**.

The command calls the QGIS Processing Scripts provider's public
`refreshAlgorithms()` API. It rescans the default and configured custom script
folders, then updates the Processing Toolbox.

## Install for development

Link this repository into the active QGIS 4 profile's plugin directory:

```sh
ln -s /Users/guilhem/dev/projects/github/qgis_processing_script_reload \
  "$HOME/Library/Application Support/QGIS/QGIS4/profiles/default/python/plugins/qgis_processing_script_reload"
```

Then enable **Processing Script Reload** in **Plugins > Manage and Install
Plugins**.

## Use

Choose **Plugins > Processing Script Reload > Refresh**, or use its Refresh
toolbar button. Close and reopen an existing Processing algorithm dialog to see
updated parameters.

If a script cannot be imported, QGIS reports the details under **Log Messages >
Processing**. Other valid scripts are still loaded.
