def otoyExport():
    import os
    import time
    node = hou.pwd()
    geo = node.geometry()
    
    fPath = hou.hipFile.path()
    fName = len(hou.hipFile.basename())*-1
    fComp = fPath[:fName]
    
        
    
    #data = zzz
    dirTest = os.path.exists(fComp+"/render/")
    if dirTest < 1:
        os.mkdir(fComp+"/render/")
    
    startF = node.parm("startFrame").evalAsInt()
    
    endF = node.parm("endFrame").evalAsInt()
    #startF = 1
    #endF = 200
    frame_range = range(startF,endF)
    #num_tasks=range(1,24)

    with hou.InterruptableOperation("otoyExport",open_interrupt_dialog=True) as operation:
        for frame in frame_range:
            hou.setFrame(frame)
            f = open(fComp+"render/cacheLight"+"_"+str(format(hou.intFrame(),'04'))+".txt", 'w')
            point = geo.points()
            
            for p in point:
                #print p
                a=p.floatListAttribValue("test")
                for d in a:
                    #print d
                    ptComp = str(d)
                    f.write(ptComp)
                    f.write(" ")
                    
            percent = (float(frame)-float(startF))/float(len(frame_range))
            operation.updateProgress(percent)
