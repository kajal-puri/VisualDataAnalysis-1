# ################################################################
# Import Packages
# ################################################################
import vtk
import sys
import getopt

def ReadInputFile(InputFilename):
    # read the image
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(InputFilename)
    reader.Update()
    return reader.GetOutput();

def CreateVisualizationFromListOfActors(ListOfActors):
    #create a renderer
    render=vtk.vtkRenderer()
    #Add the Actors to Renderer
    for i in range(0,len(ListOfActors)):
        render.AddActor(ListOfActors[i]);
    #Create Render Window
    window=vtk.vtkRenderWindow()
    window.AddRenderer(render)
    #Create Interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)
    interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
    interactor.Initialize()
    interactor.Start()

def task1(InputData):
    # create a BoundingBox using 
    # vtkOutlineFilter 
    # vtkPolyDataMapper
    # vtkActor 

    # <Insert Code>

    outActor= vtk.vtkActor()
    # <Insert Code> 

    #return the actor
    return outActor
  
def task2(InputData):
    #create a contour using contourFilter
    # <Insert Code>
    
    bonesActor = vtk.vtkActor()
    # <Insert Code>
    
    #return the actor
    return bonesActor
    
def task3(InputData):
    #create a contour using contourFilter
    # <Insert Code>
   
    skinActor = vtk.vtkActor()
    # <Insert Code>
    
    #return the actor
    return skinActor



#Defining the Main Function 
def main(argv):    
    # define input variables
    helpstr="""IntroVtkPython.py -i <InputFilename> [optional -b <ShowBoundingBox>]"""
    # parse command line
    InputFilename=None
    ShowBBoxInStr=None
    ShowBBox=0
    try:
        opts, args = getopt.getopt(argv,"i:b:")
    except getopt.GetoptError:
        print (helpstr)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (helpstr)
            sys.exit()
        elif opt == "-i":
            InputFilename = arg
        elif opt == "-b":
            ShowBBoxInStr = arg

    if InputFilename==None:
        print (helpstr)
        sys.exit(2)
    if ShowBBoxInStr=="true":
        ShowBBox = 1
# ########## Finished Parsing Agruments ##################
    
    # reading the file 
    data=ReadInputFile(InputFilename)
    # execute the tasks
    BboxActor    = task1(data)
    BonesActor   = task2(data)
    SkinActor    = task3(data)
    # disable the visibility of the BboxActor when 
    # the boundingbox shall not be shown 
    # <Insert Code>
    
    #adding the actors to A List Of Actors    
    ListOfActors = []
    ListOfActors.append(BboxActor)
    ListOfActors.append(BonesActor)
    ListOfActors.append(SkinActor)
   
    # create visualization and interaction 
    CreateVisualizationFromListOfActors(ListOfActors)

#Entry point
if __name__ == "__main__":
    main(sys.argv[1:])

    