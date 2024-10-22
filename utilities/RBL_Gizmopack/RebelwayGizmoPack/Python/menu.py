import arnold_splitout


toolbar = nuke.menu("Nuke")
rebelPython = toolbar.addMenu("Rebelway Tools")
rebelPython.addCommand('Arnold Splitout', 'arnold_splitout.arnold_splitout(), "Alt+s"')
