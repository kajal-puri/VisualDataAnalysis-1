#!/usr/bin/env python
# This script has been tested with Python 3.7.7 and VTK 8.2.0
# ################################################################
# Import Packages
# ################################################################
import vtk
import sys
import getopt
import math

chart = None 

class vtkTimerCallback():
    def __init__(self):
        self.timer_count = 0
        self.timeStamp=0
 
    def execute(self,obj,event):
        
        numP=chart.GetNumberOfPlots()
        global bBox;
        self.timer_count += 1
       
       
        # Execution for the first Animation
        if self.timer_count<=100:
            numP=chart.GetNumberOfPlots()
            translation=0.03

            val1=boxB.GetRow(0).GetValue(0).ToFloat();
            val2=boxB.GetRow(0).GetValue(1).ToFloat();
            val3=boxB.GetRow(1).GetValue(0).ToFloat();
            val4=boxB.GetRow(1).GetValue(1).ToFloat();
            val5=boxB.GetRow(2).GetValue(0).ToFloat();
            val6=boxB.GetRow(2).GetValue(1).ToFloat();
            val7=boxB.GetRow(3).GetValue(0).ToFloat();
            val8=boxB.GetRow(3).GetValue(1).ToFloat();
            
            boxB.SetValue(0, 0, val1+translation)
            boxB.SetValue(0, 1, val2)
            boxB.SetValue(1, 0, val3+translation)
            boxB.SetValue(1, 1, val4)
            boxB.SetValue(2, 0, val5+translation)
            boxB.SetValue(2, 1, val6)
            boxB.SetValue(3, 0, val7+translation)
            boxB.SetValue(3, 1, val8)
            
            line2 = chart.AddPlot(vtk.vtkChart.LINE)
            line2.SetInputData(boxB, 0, 1)
            line2.SetColor(255, 0, 0, 255)
            line2.SetWidth(3.0)
            line2.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line2.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
            
            
            line3 = chart.AddPlot(vtk.vtkChart.LINE)
            line3.SetInputData(boxA, 0, 1)
            line3.SetColor(0, 0, 0, 255)
            line3.SetWidth(3.0)
            line3.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line3.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
            
            #call the convolution Function Drawer
            
            convolutionDrawerBoxBox(boxB.GetRow(3).GetValue(0).ToFloat()-0.5,
                                    self.timer_count-1)
            for i in range(0,numP-1):
                chart.RemovePlot(1)
            
        # clearing the Plot when reached the end
        if self.timer_count==110:

            #reset the plotter 
            for i in range(0,numP-1):
                chart.RemovePlot(1)

            # reset the convolution box 
            boxB.SetValue(0, 0, -2.5)
            boxB.SetValue(0, 1, 0.0)
            boxB.SetValue(1, 0, -2.5)
            boxB.SetValue(1, 1, 1)
            boxB.SetValue(2, 0, -1.5)
            boxB.SetValue(2, 1, 1.0)
            boxB.SetValue(3, 0, -1.5)
            boxB.SetValue(3, 1, 0)
            
            line2 = chart.AddPlot(vtk.vtkChart.LINE)
            line2.SetInputData(boxB, 0, 1)
            line2.SetColor(255, 0, 0, 255)
            line2.SetWidth(3.0)
            line2.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line2.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
            
            boxA.SetValue(0, 0, 0)
            boxA.SetValue(0, 1, 0)
            boxA.SetValue(1, 0, 1)
            boxA.SetValue(1, 1, 1)
            boxA.SetValue(2, 0, 2)
            boxA.SetValue(2, 1, 0)
            boxA.SetValue(3, 0, 2)
            boxA.SetValue(3, 1, 0)
            
            line3 = chart.AddPlot(vtk.vtkChart.LINE)
            line3.SetInputData(boxA, 0, 1)
            line3.SetColor(0, 0, 255, 255)
            line3.SetWidth(3.0)
            line3.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line3.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
            
      
        # Now draw the new Function
        if self.timer_count>110 and self.timer_count<240:
            translation=0.03
            #get number of plots
            numP=chart.GetNumberOfPlots()
            val1=boxB.GetRow(0).GetValue(0).ToFloat();
            val2=boxB.GetRow(0).GetValue(1).ToFloat();
            val3=boxB.GetRow(1).GetValue(0).ToFloat();
            val4=boxB.GetRow(1).GetValue(1).ToFloat();
            val5=boxB.GetRow(2).GetValue(0).ToFloat();
            val6=boxB.GetRow(2).GetValue(1).ToFloat();
            val7=boxB.GetRow(3).GetValue(0).ToFloat();
            val8=boxB.GetRow(3).GetValue(1).ToFloat();
            
            boxB.SetValue(0, 0, val1+translation)
            boxB.SetValue(0, 1, val2)
            boxB.SetValue(1, 0, val3+translation)
            boxB.SetValue(1, 1, val4)
            boxB.SetValue(2, 0, val5+translation)
            boxB.SetValue(2, 1, val6)
            boxB.SetValue(3, 0, val7+translation)
            boxB.SetValue(3, 1, val8)
            
            line2 = chart.AddPlot(vtk.vtkChart.LINE)
            line2.SetInputData(boxB, 0, 1)
            line2.SetColor(255, 0, 0, 255)
            line2.SetWidth(3.0)
            line2.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line2.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
            
            boxA.SetValue(0, 0, -1.0)
            boxA.SetValue(0, 1, 0)
            boxA.SetValue(1, 0, 0)
            boxA.SetValue(1, 1, 1)
            boxA.SetValue(2, 0, 1.0)
            boxA.SetValue(2, 1, 0)
            boxA.SetValue(3, 0, 1.0)
            boxA.SetValue(3, 1, 0)
            
            line3 = chart.AddPlot(vtk.vtkChart.LINE)
            line3.SetInputData(boxA, 0, 1)
            line3.SetColor(0, 0, 255, 255)
            line3.SetWidth(3.0)
            line3.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
            line3.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)

            convolutionDrawerBoxTriangle(boxB.GetRow(3).GetValue(0).ToFloat()-0.5,
                                         self.timeStamp)
            self.timeStamp+=1
             #reset the plotter 
            for i in range(0,numP-1):
                chart.RemovePlot(1)

def computeAreaBoxTriangle(xpos):
    # evaluates the integral for shift value xpos
    y=0
    # <insert your code here>
    return y
            
def convolutionDrawerBoxTriangle(xval,timestamp):
    boxD.SetNumberOfRows(timestamp+1)
    boxD.SetValue(timestamp, 0, xval)
    boxD.SetValue(timestamp, 1, computeAreaBoxTriangle(xval))
    # we render points here 
    points = chart.AddPlot(vtk.vtkChart.LINE)
    points.SetInputData(boxD, 0, 1)
    points.SetColor(0, 255, 0, 255)
    points.SetWidth(3.0)

def computeAreaBoxBox(xpos):
    # evaluates the integral for shift value xpos
    y=0
    # <insert your code here>
    return y

def convolutionDrawerBoxBox(xval,timestamp):
    boxD.SetNumberOfRows(timestamp+1)
    boxD.SetValue(timestamp, 0, xval)
    boxD.SetValue(timestamp, 1, computeAreaBoxBox(xval))
    # we render points here 
    points = chart.AddPlot(vtk.vtkChart.LINE)
    points.SetInputData(boxD, 0, 1)
    points.SetColor(50, 50, 255, 255)
    points.SetWidth(3.0)

#Defining the Main Function 
def main(argv):    
    view=vtk.vtkContextView()
    view.GetRenderer().SetBackground(1.0,1.0,1.0)
    view.GetRenderWindow().SetSize(1000,400)
    
    global chart 
    chart= vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(False)
    chart.AutoAxesOn()
    chart.SetForceAxesToBounds(False)
    table = vtk.vtkTable()
     
    arrX = vtk.vtkFloatArray()
    arrX.SetName('X Axis')
     
    arrC = vtk.vtkFloatArray()
    arrC.SetName('Y Axis')
     
  
     
    table.AddColumn(arrX)
    table.AddColumn(arrC)
  
    
    table.SetNumberOfRows(2)
    table.SetValue(0, 0, -2.5)
    table.SetValue(0, 1, 0)
    
    table.SetValue(1, 0, 2.5)
    table.SetValue(1, 1, 1.4)
    
    
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, 1)
    points.SetColor(0, 0, 0, 255)
    points.SetWidth(1.0)
    points.SetMarkerStyle(vtk.vtkPlotPoints.CROSS)
    
# define the stationary (gray) box
    global boxA
    boxA= vtk.vtkTable()
    boxAx= vtk.vtkFloatArray()
    boxAx.SetName('X Axis')
    
    boxAy= vtk.vtkFloatArray()
    boxAy.SetName('Y Axis')
    
    boxA.AddColumn(boxAx)
    boxA.AddColumn(boxAy)
    
    boxA.SetNumberOfRows(4)
    boxA.SetValue(0, 0, -0.5)
    boxA.SetValue(0, 1, 0.0)

    boxA.SetValue(1, 0, -0.5)
    boxA.SetValue(1, 1, 1)
    
    boxA.SetValue(2, 0, 0.5)
    boxA.SetValue(2, 1, 1.0)
    boxA.SetValue(3, 0, 0.5)
    boxA.SetValue(3, 1, 0)

    
    line0 = chart.AddPlot(vtk.vtkChart.LINE)
    line0.SetInputData(boxA, 0, 1)
    line0.SetColor(50, 50, 50, 255)
    line0.SetWidth(3.0)
    line0.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
    line0.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
    
# define the moving (red) box
    global boxB
    boxB= vtk.vtkTable()
    boxBx= vtk.vtkFloatArray()
    boxBx.SetName('X Axis')
    
    boxBy= vtk.vtkFloatArray()
    boxBy.SetName('Y Axis')
           
    boxB.AddColumn(boxBx)
    boxB.AddColumn(boxBy)
    
    boxB.SetNumberOfRows(4)
    boxB.SetValue(0, 0, -2.0)
    boxB.SetValue(0, 1, 0.0)

    boxB.SetValue(1, 0, -2.0)
    boxB.SetValue(1, 1, 1)
    
    boxB.SetValue(2, 0, -1.0)
    boxB.SetValue(2, 1, 1.0)
    boxB.SetValue(3, 0, -1.0)
    boxB.SetValue(3, 1, 0)

    line1 = chart.AddPlot(vtk.vtkChart.LINE)
    line1.SetInputData(boxB, 0, 1)
    line1.SetColor(255, 0, 0, 255)
    line1.SetWidth(3.0)
    line1.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
    line1.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)

    
    global boxC
    boxC= vtk.vtkTable()
    boxCx= vtk.vtkFloatArray()
    boxCx.SetName('X Axis')
    boxCy= vtk.vtkFloatArray()
    boxCy.SetName('Y Axis')
    boxC.SetNumberOfRows(3)
    boxC.AddColumn(boxCx)
    boxC.AddColumn(boxCy)
    boxC.SetNumberOfRows(3)
      
    boxC.SetValue(0, 0, 0)
    boxC.SetValue(0, 1, 0)     
    boxC.SetValue(1, 0, 0)
    boxC.SetValue(1, 1, 0)
    boxC.SetValue(2, 0, 0)
    boxC.SetValue(2, 1, 0)
     
    
    line0 = chart.AddPlot(vtk.vtkChart.LINE)
    line0.SetInputData(boxC, 0, 1)
    line0.SetColor(50, 50, 255, 255)
    line0.SetWidth(3.0)
    line0.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
    line0.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
        

    global boxD
    boxD= vtk.vtkTable()
    boxDx= vtk.vtkFloatArray()
    boxDx.SetName('X Axis')
    boxDy= vtk.vtkFloatArray()
    boxDy.SetName('Y Axis')
    boxD.AddColumn(boxDx)
    boxD.AddColumn(boxDy)
    boxD.SetNumberOfRows(130)
     
    line3 = chart.AddPlot(vtk.vtkChart.LINE)
    line3.SetInputData(boxD, 0, 1)
    line3.SetColor(50, 255, 0, 255)
    line3.SetWidth(3.0)
    line3.GetPen().SetLineType(vtk.vtkPen.SOLID_LINE)
    line3.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)
    
    #create timerCallBack
    cb = vtkTimerCallback()
    view.GetRenderWindow().SetMultiSamples(0)
    view.GetInteractor().Initialize()
    view.GetInteractor().AddObserver('TimerEvent', cb.execute)    
    timerId = view.GetInteractor().CreateRepeatingTimer(20);
    view.GetInteractor().Start()

boxA=None
boxB=None
boxC=None
boxD=None

#Entry point
if __name__ == "__main__":
    main(sys.argv[1:])

    
