import nuke

nuke.pluginAddPath('./Gizmos')
nuke.pluginAddPath('./Python')

print("Loading Rebelway Toolkit")

#setup menu
toolbar = nuke.toolbar('Nodes')
rebelNode = toolbar.addMenu('Rebelway', 'rebelway.png')

#add gizmos
rebelNode.addCommand('AdvancedGrain', 'nuke.createNode(\"AdvancedGrain\")')
rebelNode.addCommand('BlacksMatch', 'nuke.createNode(\"BlacksMatch\")')
rebelNode.addCommand('bm_CameraShake', 'nuke.createNode(\"bm_CameraShake\")')
rebelNode.addCommand('bm_Despill', 'nuke.createNode(\"bm_Despill\")')
rebelNode.addCommand('bm_OpticalGlow', 'nuke.createNode(\"bm_OpticalGlow\")')
rebelNode.addCommand('ChannelContactSheet', 'nuke.createNode(\"ChannelContactSheet\")')
rebelNode.addCommand('Colour_Smear', 'nuke.createNode(\"Colour_Smear\")')
rebelNode.addCommand('DasGrain', 'nuke.createNode(\"DasGrain\")')
rebelNode.addCommand('DespillMadness', 'nuke.createNode(\"DespillMadness\")')
rebelNode.addCommand('DirectionalBlur', 'nuke.createNode(\"DirectionalBlur\")')
rebelNode.addCommand('expoglow', 'nuke.createNode(\"expoglow\")')
rebelNode.addCommand('fxT_chromaticAberration', 'nuke.createNode(\"fxT_chromaticAberration\")')
rebelNode.addCommand('HeatWave', 'nuke.createNode(\"HeatWave\")')
rebelNode.addCommand('HighPass', 'nuke.createNode(\"HighPass\")')
rebelNode.addCommand('IBKColour_Stack', 'nuke.createNode(\"IBKColour_Stack\")')
rebelNode.addCommand('iBlur', 'nuke.createNode(\"iBlur\")')
rebelNode.addCommand('LensKernelFFT_v01', 'nuke.createNode(\"LensKernelFFT_v01\")')
rebelNode.addCommand('MagicDefocus', 'nuke.createNode("MagicDefocus")')
rebelNode.addCommand('NoiseAdvanced', 'nuke.createNode(\"NoiseAdvanced\")')
rebelNode.addCommand('OpticalZDefocus', 'nuke.createNode(\"OpticalZDefocus\")')
rebelNode.addCommand('P_Matte', 'nuke.createNode(\"P_Matte\")')
rebelNode.addCommand('P_Noise_Advanced', 'nuke.createNode(\"P_Noise_Advanced\")')
rebelNode.addCommand('TrueExponentialBlur', 'nuke.createNode(\"TrueExponentialBlur\")')
rebelNode.addCommand('W_CatsEye', 'nuke.createNode(\"W_CatsEye\")')

print("Rebelway Toolkit Successfully Loaded")
