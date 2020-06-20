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
    return reader;

def CreateVisualizationFromListOfActors(ListOfActors, Animate):
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
    #print(InputData.GetOutput())
    # create a BoundingBox using 
    # vtkOutlineFilter 
    # vtkPolyDataMapper
    # vtkActor 
    
    #BBox_poly = vtk.vtkPolyData()
    #BBox_poly.SetPoints(bbox_points)
    
    #outlineDimTmp=InputData.GetDimensions()
   # img = vtk.vtkXMLImageDataWriter()
   # img.SetFileName(InputData)
    
    outline = vtk.vtkOutlineFilter()
    outline.SetInputConnection(InputData.GetOutputPort())
        
    outline_mapper = vtk.vtkPolyDataMapper()
    outline_mapper.SetInputConnection(outline.GetOutputPort())
   
    outActor= vtk.vtkActor()    
    outActor.SetMapper(outline_mapper)
    outActor.GetProperty().SetColor(0,128,0)
    outActor.GetProperty().SetLineWidth(3)
    #print("task1")
    return outActor
  
def task2(InputData):
    #create a contour using contourFilter
    contours = vtk.vtkContourFilter()
    contours.SetInputConnection(InputData.GetOutputPort())
    #contours.GenerateValues(12, 500, 1150)
    #contours.Set
    contours.SetValue(0, 73)
    
    contMapper = vtk.vtkPolyDataMapper()
    contMapper.SetInputConnection(contours.GetOutputPort())
    #contMapper.SetScalarRange(0.0, 1.2)
    contMapper.ScalarVisibilityOff()
    
    bonesActor = vtk.vtkActor()
    # <Insert Code>
    bonesActor.SetMapper(contMapper)
    bonesActor.GetProperty().SetColor(255,255,0)
    #return the actor
    return bonesActor
    
def task3(InputData):
    #create a contour using contourFilter
    # <Insert Code>
    contours = vtk.vtkContourFilter()
    contours.SetInputConnection(InputData.GetOutputPort())
    #contours.GenerateValues(12, 500, 1150)
    #contours.Set
    contours.SetValue(0, 60)
    
    contMapper = vtk.vtkPolyDataMapper()
    contMapper.SetInputConnection(contours.GetOutputPort())
    #contMapper.SetScalarRange(0.0, 1.2)
    contMapper.ScalarVisibilityOff()
    #contMapper.set
    
    skinActor = vtk.vtkActor()
    # <Insert Code>
    skinActor.SetMapper(contMapper)
    skinActor.GetProperty().SetColor(255,0,0)
    skinActor.GetProperty().SetOpacity(0.5)
    #skinActor.GetProperty.Set
    #return the actor
    return skinActor

'''
def bonusTask(data):
    
    return actor
'''


#Defining the Main Function 
def main(argv):    
    # define input variables
    helpstr="""IntroVtkPython.py -i <InputFilename> [optional -b <ShowBoundingBox>] [optional -b <Animate>]"""
    # parse command line
    InputFilename="head.vti"
    #print(InputFilename)
    ShowBBoxInStr = None
    Animate = None
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
    #AnimateActor = bonusTask(data)
    # disable the visibility of the BboxActor when 
    # the boundingbox shall not be shown   
    
    #adding the actors to A List Of Actors    
    ListOfActors = []
    if ShowBBoxInStr!=None:
        ListOfActors.append(BboxActor)        
    ListOfActors.append(BonesActor)
    ListOfActors.append(SkinActor)
   
    # create visualization and interaction 
    CreateVisualizationFromListOfActors(ListOfActors, Animate)

#Entry point
if __name__ == "__main__":
    main(sys.argv[1:])

    