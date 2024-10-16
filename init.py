import nuke
def extend_plugin_path():
    paths = ["python",
             "gizmos",
             "Utilities/pixelfudger3",
             "utilities/stamps",
             "utilities/NukeSurvivalToolkit"
            ]
    for path in paths:
        nuke.pluginAddPath(path)

extend_plugin_path()
