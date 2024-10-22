import nuke

def arnold_splitout():

    nodeSel = [n for n in nuke.allNodes() if n['selected'].value() == True]
    if nodeSel:
        if len(nodeSel) >1:
            nuke.message('Please select only the node you want to split out.')
        if len(nodeSel) == 1:
            node = nuke.selectedNode()
    else:
        nuke.message('Too many nodes selected, please select one.')

    node = nuke.selectedNode()
    channels = node.channels()
    xposoffset = 150
    yposoffset = 75

    #list layers and sort alphabetically
    layers = list( set([c.split('.')[0] for c in channels]) )
    layers = sorted(layers, key=str.lower)

    print(layers)

    #reset mergecount
    mergecount = 0;

    #create Top Dot and fetch position
    topdot = nuke.createNode("Dot")
    dotXpos = topdot.xpos()
    dotYpos = topdot.ypos()

    #create copy dot
    copydot = nuke.createNode("Dot")
    copydot.setXYpos((int(dotXpos-xposoffset)), dotYpos)

    #For each layer containing RGBA do this
    for i in layers:
        if "RGBA" in i:

            mergecount = mergecount + 1;

            #If This is the first layer
            if mergecount<2:
                global mergeXpos
                global mergeYpos
                global shuffleNode
                shuffleNode = nuke.nodes.Shuffle( label = "[value in]", inputs= [topdot])
                shuffleNode['in'].setValue(i)
                mergeXpos = shuffleNode.xpos()
                mergeYpos = shuffleNode.ypos()

            #If this is the second layer
            if mergecount==2:
                topdot = nuke.nodes.Dot(inputs= [topdot])
                topdot.setXYpos(int(dotXpos+((mergecount-1)*xposoffset)), dotYpos)

                currentmerge = nuke.nodes.Merge2(operation="plus")
                currentmerge.setInput(0,shuffleNode)

                shuffleNode = nuke.nodes.Shuffle( label = "[value in]", inputs= [topdot])
                shuffleNode['in'].setValue(i)

                bottomdot = nuke.nodes.Dot(inputs = [shuffleNode])
                #bottomdot['ypos'].setValue(mergeYpos+(yposoffset*mergecount)+40)
                bottomdot.setXYpos(int(dotXpos+((mergecount-1)*xposoffset)), (dotYpos+yposoffset*2))
                print("This is first dot ypos")
                print(bottomdot.ypos())

                currentmerge.setInput(1,bottomdot)
                currentmerge.setXYpos(mergeXpos, (bottomdot.ypos()-4))
                print(currentmerge.ypos())


            #If this is the third layer
            if mergecount>2:
                topdot = nuke.nodes.Dot(inputs= [topdot])
                topdot.setXYpos(int(dotXpos+((mergecount-1)*xposoffset)), dotYpos)

                shuffleNode = nuke.nodes.Shuffle( label = "[value in]", inputs= [topdot])
                shuffleNode['in'].setValue(i)

                bottomdot = nuke.nodes.Dot(inputs = [shuffleNode])
                print("This is orig")
                print(bottomdot.ypos())
                bottomdot['ypos'].setValue(mergeYpos+(yposoffset*mergecount)+4)
                print("This is modified")
                print(bottomdot.ypos())

                newmerge = nuke.nodes.Merge2(operation="plus")
                newmerge.setInput(1,bottomdot)
                newmerge.setInput(0,currentmerge)

                currentmerge = newmerge
                currentmerge.setXYpos(mergeXpos, (mergeYpos+(yposoffset*mergecount)))


    copylowerdot = nuke.createNode("Dot")
    copylowerdot.setXYpos(copydot.xpos(),(mergeYpos+(yposoffset*(mergecount+1))))

    #setup copy
    copy = nuke.nodes.Copy(inputs = [currentmerge, copylowerdot], from0="rgba.alpha", to0="rgba.alpha")
    copy.setXYpos(mergeXpos, (mergeYpos+(yposoffset*(mergecount+1)-10)))

    print(copylowerdot.ypos())
    print(copy.ypos())

