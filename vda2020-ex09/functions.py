import vtk
import numpy as np


def determineCase(cellvalues,iso):
  """ 
    Computes the CaseNumber based on the binary state of the cell values
    eg cell=[17,10,20,10] and isovalue is 15
    Test of cell is greater equal than isovalue
    boolvalues=[true,false,true,false]
    translates bool values into Bits
    BitValues=1010
    Translates BitValues into int
    caseNumber=10
    ---- Cell Orientation -------
    0 -- 1
    |    |
    2 -- 3
  Args: 
    cellvalues(list)= list of the cellvalues 
    iso(float)      = iso value for contour
    
    
  Returns: 
   Computed Case number
  """
  caseNumber=0
  #<INSERT CODE>
    #</INSERT CODE>
  return caseNumber

def createCaseEdgeTable():
  """ Create a Case Edge Table
      An entry in caseEdgeTable[x] is a list of 
      edges(ids) that will be intersected by the case x 
      for ambiguous cases an entry is a list of list eg caseTable[x]=[[a,b,c,d],[e,f,g,h]]
      It also tells you how the intersection points will be connected
      for the case [[a,b,c,d],[e,f,g,h]] intersection lines are introduced between
      a-b and c-d if subcase is 0 
      e-f and g-h if subcase is 1 
      
  ---- Cell Orientation -------
           0
      0 ------ 1
    3 |        |  1
      2 ------ 3
          2
  Returns the created table list
  """
  empty=[]
  caseEdgeTable=[empty]*16
  caseEdgeTable[ 0]=[]          # No Intersection
  
  # Case 1 means that the value at cell id 3 is greater than isoValue
  # therefore the intersection is on the edges 1 and 2 
  caseEdgeTable[ 1]=[1,2]       # Intersection on Edge 1 and on Edge 2 
  
  #<INSERT CODE>
  #</INSERT CODE>
  
  return caseEdgeTable


def findIntersectionPoint(p1,p2,c1,c2,isoValue):
  """  Returns the Intersection Point Based on c1 ,c2 and isoValue
       The intersection Point is on a line between p1 and p2 
  Args: 
        p1(numpy array) = point on a cell edge
        p2(numpy array) = point on a cell edge
        c1(float)       = cell value on p1 (scalar value)
        c2(float)       = cell value on p2 (scalar value)
        isoValue(float) = iso value for contour
  Returns:
      An intersection point that lies on the edge between p1, and p2 
  """
  intersection=p1
  #<INSERT CODE>
  #</INSERT CODE>
  return intersection

def identifySubcase(pts):
  """ identifies the subcase for the asymptotic decider
      
  Args: pts(List) = list of 4 2D points (intersection points)

  Returns: subcase index to be used with case table
  
  """
  subcase=0;
  # define subcases for the Asymptotoc Decider
  #<INSERT CODE>
  #</INSERT CODE>
  return subcase

  
def asymptoticDecider(pts,edgeCase):
  """ Input are the four intersection points.
      
      the subcase tells us how to connect the points.
    
    Args :
      pts(numpy array) : intersection points
      edgeCase (list of list): list of list for different ambiguous cases (interseting edges)
        
      Based on the subcase you have to select one of list in edgeCase

     Returns: reordered Points so that p0-p1 and p2-p3 are the two intersection lines for this subcase
 
  """
  #HINT: 1] find the subcase for the ambiguous case 
  #      2] based on the subcase extact the correct value form the edgeCaseTable
  #      3] create the line Points (reoder the points)
        
  newOrder=[];
  #<INSERT CODE>
  #</INSERT CODE>
  return newOrder;


def computeIntersectionPoints(intersectingEdges,pts,cellValues,isoValue):
  """ Returns the intersection Points for the given intersecting Edge list
  
    Args: intersectionEdge (List or List(List) ) = list or list of list for intersecting edges
                                                   based in the case number
  
  
    pts (numpy array) = location of the corner points of the cell
    cellValues (list )= scalar values of the cell
    isoValue (float or int)= isoValue for contour
  """
  intersectionPoints=[]
  if len(intersectingEdges)==0:
    return intersectionPoints
  # find out if you need the asymptotic decider
  ambiguousCase=False    
  if type(intersectingEdges[0])==type([]):
    ambiguousCase=True
    
  # if  ambiguousCase==True you need first to find the intersection points
  # for any of the given list from intersecting edges
  # and then call the asymptoticDecider with the intersectionPoints and intersectingEdges
    
  # to find the intersection points use the already implemented function 'findIntersectionPointsOnEdges()'
 
  #<INSERT CODE>
  #</INSERT CODE>
  return intersectionPoints;




  
#------ function for the second part of the exercise  
def computeLineSegments(data,intersectionPoints,isovalue):
  """ Computes intersections points for a cell 
      (based on the evaluated case) 
      and adds the points to 'intersectionPoints'
  Args: data(vtkImageData)       = image data
        
        intersectionPoints(list) = list of all intersection points
                                   an intersection line is defined by 2 points
        
        isovalue(float or int)   = value for iso contour 
        
  Returns: Nothing, result values are stored in 'intersectionPoints'
  """
  #<INSERT CODE>

  #</INSERT CODE>


#---------------------------------------------------------------------
# You do not have to change anything below this line
#---------------------------------------------------------------------
def createPointIdsOnEdge():
  edges=[]
  edges.append([0,1])
  edges.append([1,3])
  edges.append([2,3])
  edges.append([0,2])
  return edges
#---------------------------------------------------------------------
def createCellLinesForPoints(renderer,pts):
  """ Adds Edges to the renderer detemined by the given points
  
  Args: 
    renderer(vtkRenderer) = the renderer
    pts (numpy array)     = array of the 2d points
  """
  pd1=pts[0,:]
  pd2=pts[1,:]
  pd3=pts[3,:]
  pd4=pts[2,:]
  
  p1=np.append(pd1,0)
  p2=np.append(pd2,0)
  p3=np.append(pd3,0)
  p4=np.append(pd4,0)

  pts=vtk.vtkPoints()
  pts.InsertNextPoint(p1)
  pts.InsertNextPoint(p2)
  pts.InsertNextPoint(p3)
  pts.InsertNextPoint(p4)
  polyData=vtk.vtkPolyData()
  polyData.SetPoints(pts)
  # create lines 
  lin1=vtk.vtkLine()
  lin1.GetPointIds().SetId(0,0)
  lin1.GetPointIds().SetId(1,1)
  lin2=vtk.vtkLine()
  lin2.GetPointIds().SetId(0,1)
  lin2.GetPointIds().SetId(1,2)

  lin3=vtk.vtkLine()
  lin3.GetPointIds().SetId(0,2)
  lin3.GetPointIds().SetId(1,3)
  
  lin4=vtk.vtkLine()
  lin4.GetPointIds().SetId(0,3)
  lin4.GetPointIds().SetId(1,0)
  
  lines=vtk.vtkCellArray()
  lines.InsertNextCell(lin1)
  lines.InsertNextCell(lin2)
  lines.InsertNextCell(lin3)
  lines.InsertNextCell(lin4)
  polyData.SetLines(lines)
  mapper=vtk.vtkPolyDataMapper()
  mapper.SetInputData(polyData)
  mapper.Update()
  actor=vtk.vtkActor()
  actor.SetMapper(mapper)
  renderer.AddActor(actor)
#---------------------------------------------------------------------
def createRenderers():
  ymax=2
  xmax=8
  bgColor=(0.5,0.5,0.5)
  bgColor2=(0.6,0.6,0.6)
  # Setting up the viewport pyramid
  index=0;
  renderers=[]
  for y in range(1,-1,-1):
      yvalMin=y*1.0/ymax
      yvalMax=(y+1)*1.0/ymax
      index=index+1
      for x in range(0,xmax):
          xwidth=1.0/xmax
          xvalMin=(xwidth)*x
          xvalMax=xvalMin+xwidth;
          #init renderer and set its viewport and color
          ren= vtk.vtkRenderer();
          ren.SetViewport(xvalMin, yvalMin, xvalMax,yvalMax)
          if (index%2)==0:
            ren.SetBackground(bgColor);
          else:
            ren.SetBackground(bgColor2);
          # add to our list
          renderers.append(ren);
          index=index+1
  return renderers

#--------------------------------------------------------------------
def addIntersectionLine(renderer,p1,p2):
  p1=np.append(p1,0)
  p2=np.append(p2,0)
  pts=vtk.vtkPoints()
  pts.InsertNextPoint(p1)
  pts.InsertNextPoint(p2)
  polyData=vtk.vtkPolyData()
  polyData.SetPoints(pts)
  # create lines 
  lin1=vtk.vtkLine()
  lin1.GetPointIds().SetId(0,0)
  lin1.GetPointIds().SetId(1,1)
  
  lines=vtk.vtkCellArray()
  lines.InsertNextCell(lin1)
  polyData.SetLines(lines)
  mapper=vtk.vtkPolyDataMapper()
  mapper.SetInputData(polyData)
  mapper.Update()
  actor=vtk.vtkActor()
  actor.SetMapper(mapper)
  actor.GetProperty().SetColor(0.5,1.0,1.0)
  renderer.AddActor(actor)
#--------------------------------------------------------------------
def addColoredSphere(ren,pnt,color):
  """ Adds a Colored Sphere to the Renderer
  
  Args: renderer(vtkRenderer)  = the Renderer
        point (numpy array)    = location of 2d point
        color2 (list)          = list of rgb color values (range [0..1])
        
  """
  sphere=vtk.vtkSphereSource()
  center3d=np.append(pnt,0)
  sphere.SetCenter(center3d)
  sphere.SetRadius(0.05)
  map=vtk.vtkPolyDataMapper()
  map.SetInputData(sphere.GetOutput())
  map.Update()
  act=vtk.vtkActor()
  act.SetMapper(map)
  act.GetProperty().SetColor(color[0],color[1],color[2])
  ren.AddActor(act)
#--------------------------------------------------------------------
def createPoints():
  """ Creates Points for CellTests
  Returns : numpy array of 2d points
  """
  pts=np.array([ [0,1],[1,1], [0,0],  [1,0]])
  return pts
#--------------------------------------------------------------------
def createCases():
  c00=[60,12,15,20] # single
  c01=[10,60,15,20] # single
  c02=[10,12,60,20] # single
  c03=[10,12,15,60] # single
  c04=[10,60,60,60] # single
  c05=[60,12,60,60] # single
  c06=[60,60,15,60] # single 
  c07=[60,60,60,20] # single 

  c08=[10,12,60,60] # double adjacent 
  c09=[60,60,15,20] # double adjacent 
  c10=[10,60,15,60] # double adjacent
  c11=[60,12,60,20] # double adjacent 

  c12=[10,60,60,20] # double Opposite
  c13=[60,12,15,60] # double Opposite
  c14=[60,60,60,60] # no crossing
  c15=[10,12,15,20] # no crossing

  allCases=[]
  allCases.append(c00)
  allCases.append(c01)
  allCases.append(c02)
  allCases.append(c03)
  allCases.append(c04)
  allCases.append(c05)
  allCases.append(c06)
  allCases.append(c07)
  allCases.append(c08)
  allCases.append(c09)
  allCases.append(c10)
  allCases.append(c11)
  allCases.append(c12)
  allCases.append(c13)
  allCases.append(c14)
  allCases.append(c15)
  return allCases
  
  #--- Drawing Functions 
def createSpheresForPoints(renderer,points,caseNumber):
  """ Adds Speheres to renderer at the location of the points
      Colorizes them by the caseNumber
      
  Args: renderer(vtkRenderer) = the renderer
        points(numpy array)   = an array of 2d points (where to draw the spheres)
        caseNumber(int)       = specifies the coloring (use binary representation)
                                of the case number 0=color1, 1=color2
    
  """
  color1=[0.0,0.0,1.0]
  color2=[1.0,0.0,0.0]
  binaryCase=format(caseNumber, '04b')
  
  for i in range(0,len(points)):
    if (binaryCase[i]=='0'):
      addColoredSphere(renderer,points[i],color1)
    else:
      addColoredSphere(renderer,points[i],color2)
  

# i dont think they should have to implement this,
# its just a line that returns an entry in the case table
def getEdgeIdsForIntersection(caseNumber):
  """ 
  Return the ids of edges that will be interesected
    
    Args:
      caseNumber(int)= number of the case
    
    Returns:
      the edgeIds that will be intersected in this case
      the intersectedEdges for each case are stored in 
      the list caseEdgeTable
      Returning item is an entrie in the list caseEdgeTable 
      at the position caseNumber
  """
  return caseEdgeTable[caseNumber]

# not sure if to let them implement this or not 
def findIntersectionPointsOnEdges(edgeList,points,cellValues,isoValue):
  intersectionPoints=[]
  for i in range(0,len(edgeList)):
      ids=PointIDsOnEdge[edgeList[i]]
      p1=points[ids[0]]
      p2=points[ids[1]]
      c1=cellValues[ids[0]]
      c2=cellValues[ids[1]]
      ip1=findIntersectionPoint(p1,p2,c1,c2,isoValue)
      intersectionPoints.append(ip1)
  return intersectionPoints



#defining the point ids for an edge
PointIDsOnEdge = createPointIdsOnEdge()
caseEdgeTable  = createCaseEdgeTable()