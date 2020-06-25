#!/usr/bin/env python
# This script has been tested with Python 3.7.7 and VTK 8.2.0
from builtins import str
from builtins import range
import vtk 
from functions import *
import numpy as np

# ---- Cell Orientation -------
#                0
#      0 ---------------- 1
#      |                  |
#    3 |                  |  1
#      |                  |
#      2 ---------------- 3
#                 2
#------------------------------------


def main():
  isoValue = 50
  cases    = createCases()
  renList  = createRenderers()
  pts      = createPoints()
  window   = vtk.vtkRenderWindow()


  for i in range(0,len(cases)):
    #determine case and add an text actor to this renderer
    caseNumber=determineCase(cases[i],isoValue)
    text=vtk.vtkTextActor()
    text.SetInput("Case "+str(caseNumber))
    text.GetProperty().SetColor(0,0,0)
    renList[i].AddActor(text)

    #create spheres for the points and colorize by caseNumber
    createSpheresForPoints(renList[i],pts,caseNumber)

    #create edges between the points 
    createCellLinesForPoints(renList[i],pts)

    #find the edges that are intersected
    intEdges=getEdgeIdsForIntersection(caseNumber)

    #find the intersection point on intersected edges
    interP=computeIntersectionPoints(intEdges,pts,cases[i],isoValue)



    #create the edges between intersection points
    for ip in range(0,len(interP)//2):
      q=ip*2
      addIntersectionLine(renList[i],interP[q],interP[1+q])

    #add this renderer to the renderWindow
    window.AddRenderer(renList[i])



  #Create Interactor
  interactor = vtk.vtkRenderWindowInteractor()
  interactor.SetRenderWindow(window)
  interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
  interactor.Initialize()
  interactor.Start()

# ###################################################################
# Execution 
# ###################################################################
if __name__ == '__main__':
    main()