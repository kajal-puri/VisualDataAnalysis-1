#!/usr/bin/env python
# This script has been tested with Python 3.7.7 and VTK 8.2.0
# ################################################################
# Import Packages
# ################################################################
from builtins import range
import vtk
import sys
import getopt
from functions import *


# ################################################################
# Start of the main 
# ################################################################
def main(argv):
     # define input variables
    helpstr="""isoLones.py -i <InputFilename> -v <IsoValue>"""
    # parse command line
    InputFilename=None
    isovalue=0
    
    # debuging setting
    #InputFilename="../fullhead15.png"
    #isovalue=float(700)
    try:
        opts, args = getopt.getopt(argv,"i:v:")
    except getopt.GetoptError:
       print(helpstr)
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpstr)
            sys.exit()
        elif opt == "-i":
            InputFilename = arg
        elif opt == "-v":
            isovalue=float(arg)
    if InputFilename==None:
        print(helpstr)
        sys.exit(2)

    #Load the image data Set
    reader =vtk.vtkPNGReader();
    reader.SetFileName(InputFilename);
    reader.Update();

    data = reader.GetOutput();
    # Create Marching Squares	
    print('Marching Squares(Isovalue:',isovalue,') under construction, Please Wait! ... ');
    intersectionPoints=[]
    computeLineSegments(data,intersectionPoints,isovalue)
    linesActor=drawLines(intersectionPoints)
    
    imageMapper = vtk.vtkDataSetMapper();
    imageMapper.AddInputConnection(reader.GetOutputPort());
    imageMapper.SetScalarRange(0, 10000);
    imageActor = vtk.vtkActor();
    imageActor.SetMapper(imageMapper);

    #// Create a window + renderer
    renderer =  vtk.vtkRenderer();
    renderWindow = vtk.vtkRenderWindow();
    renderWindow.AddRenderer(renderer);
    renderWindowInteractor = vtk.vtkRenderWindowInteractor();
    renderWindowInteractor.SetRenderWindow(renderWindow);
    renderWindowInteractor.SetInteractorStyle(vtk.vtkInteractorStyleImage());

    renderer.AddActor(imageActor);
    renderer.AddActor(linesActor);

    renderWindow.Render();
    renderWindowInteractor.Start();


def drawLines(linesegs):
  numPts=len(linesegs)
  print("numberOfPoints=",numPts)
  actor=vtk.vtkActor()
  pts=vtk.vtkPoints()
 
  
  for i in range (0,numPts):
    apoint=linesegs[i]
    bpoint=np.append(apoint,0)
    pts.InsertNextPoint(bpoint);

  lines = vtk.vtkCellArray();
  lineSource = vtk.vtkLine();
  for j in range(0,numPts,2): 
    lineSource.GetPointIds().SetId(0,j);
    lineSource.GetPointIds().SetId(1,j+1);
    lines.InsertNextCell(lineSource);

  linesPolyData = vtk.vtkPolyData();
  linesPolyData.SetPoints(pts);
  linesPolyData.SetLines(lines);

  linesMapper = vtk.vtkPolyDataMapper();
  linesMapper.SetInputData(linesPolyData)
  actor.SetMapper(linesMapper);
  return actor
  


# ###################################################################
# Execution 
# ###################################################################
if __name__ == '__main__':
    main(sys.argv[1:])