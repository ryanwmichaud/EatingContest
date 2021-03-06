import random
import getch
class Cell:
  "cell class for making cells"
  def __init__(self,x,y):
    'create new cells'
    self.alive1=False
    self.last1=False
    self.alive2=False
    self.last2=False
    self.x=x
    self.y=y
    # self.start=0
    # self.end=0
    self.p1act=False
    self.p2act=False
    
  def update(self,cells,direction):
#p1 and p2 move

    if (self.x==board.p1x and self.y==board.p1y)==True:
      self.alive1=True
    else:
      self.alive1=False
      
    # if   (self.x==board.p2x and self.y==board.p2y)==True:
    #   self.alive2=True
    # else:
    #   self.alive2=False
 
  def __str__(self):
    return "x=" + str(self.x) + ", y=" + str(self.y)


class Board:
  "does the stuff"
  def __init__ (self,width,height):
    "make the board"
    self.sizesq=200
    self.width=width
    self.height=height
    self.cells = []
    self.addcells(self.cells,self.width,self.height)
    self.starttimer=0
    self.endtimer=0
    self.p2x=random.randrange(3)
    self.p1y=self.height//2
    self.p1x=self.width//4
    self.p2y=random.randrange(3)
    self.moves=0
    self.block=(0,0)
    self.r1=255
    self.g1=255
    self.b1=255
    self.r2=0
    self.g2=255
    self.b2=0

    #color for when p1 activates
    self.r1a=150
    self.g1a=50
    self.b1a=200
    #color for when p2 activates
    self.r2a=0
    self.g2a=100
    self.b2a=100
    #color for selector
    self.rs=255
    self.gs=255
    self.bs=255
    #color for board
    self.rb=0
    self.gb=0
    self.bb=0
    
    

  def addcells(self,cells,width,height) : 
    for x in range(width):
      cells.append([])
      for y in range(height):
        cells[x].append(Cell(x, y))

  def initialize(self,setup):
    
    
    self.cells[self.p1x][self.p1y].alive1 = True
    # self.cells[self.p2x][self.p2y].alive2 = True
  
  def checkinput(self,direction):
    if direction == 'a':
      board.p1x=(board.p1x-1)%board.width

    elif direction == 'd':
      board.p1x=(board.p1x+1)%board.width
   
    elif direction == 'w':
      board.p1y=(board.p1y-1)%board.height
    
    elif direction == 's':
      board.p1y=(board.p1y+1)%board.height


#draw button pressed    
    elif direction == 'p':
      #if not already
      if (self.cells[self.p1x][self.p1y].p1act==False) and (self.cells[self.p1x][self.p1y].p2act==False):
        
        self.cells[self.p1x][self.p1y].p1act=True
        #incrment/print moves,check for win,compturn , draw(True)
        self.moves+=1
        self.draw(canvas,True)        
        self.checkwincases()
        #print (self.moves)

        self.compturn()
        self.draw(canvas,True)
        self.checkwincases()
      else:
        print("\nalready taken sptuid\n")          

  def update(self,direction):
    
    
    self.checkinput(direction)
   #process input, do it
   #incrment moves compy turn, and check for win

#alive to last for selector
    for i in range(self.width):
      for cell in self.cells[i]:
        cell.last1 = cell.alive1

    # for i in range(self.width):
    #   for cell in self.cells[i]:
    #     cell.last2 = cell.alive2  

#update all
    for i in range (self.width):
      for cell in self.cells[i]:
        cell.update(self.cells,direction)
  
  def checkwincases(self):  
    # self.didP1Win()
    # self.didP2Win()
   
    if self.didP1Win()==True:
      input("\nplayer 1 wins!\npress enter to play again\n")
      self.reset() 
      self.draw(canvas,True)
    elif self.didP2Win() == True:
      input("\nplayer 2 wins!\npress enter to play again\n")
      self.reset() 
      self.draw(canvas,True)
    elif self.moves==9:
      input ("\ntie\npress enter to play again\n")
      self.reset()
      self.draw(canvas,True)


    
  def reset(self):
    #print("resetstart")
    #for all cells
    for i in range(self.width):
      for cell in self.cells[i]:
        # set all to false 
        cell.p1act=False
        cell.p2act=False
        #cell.alive1=False

    self.draw(canvas,True)
    self.didP1Win()==False
    self.didP2Win()==False
    self.moves=0
    main()

  def canBlock(self):
    #loop through every row horiz 
      #if p1act and p1act next and neighther p1 or 2 act next:
        #place in that empty spot 

    #for every space
    for i in range(self.width):
      for j in range (self.height): 
      #if two horiz then one empty
        if self.cells[i%3][j].p1act==True:
          if self.cells[(i+1)%3][j].p1act==True:
            if (self.cells[(i+2)%3][j].p1act==False) and (self.cells[(i+2)%3][j].p2act==False):
              #save the coordinates of the empty, return true
              self.block=(i+2,j)
              return True
#if the next horiz not activ...
#if next vert is activ and next vert empty
          elif self.cells[i][(j+1)%3].p1act==True:
              if (self.cells[i][(j+2)%3].p1act==False) and (self.cells[i][(j+2)%3].p2act==False):
                #save the coordinates of the empty, return true
                self.block=(i,j+2)
                return True
#now diag cases
    #if any of the br three are activ
    for i in range(self.width):
      if (self.cells[(i)%3][(i)%3].p1act==True):
        print("in diag1")
        #if next diag br is activ
        if self.cells[(i+1)%3][(i+1)%3].p1act==True:
          #if next diag br is empty
          if (self.cells[(i+2)%3][(i+2)%3].p1act==False) and (self.cells[(i+2)%3][(i+2)%3].p2act==False):
            #save the empty space coordinates, return true
            self.block=(i+2,i+2)
            return True
    #if any of the bl three are activ
    for i in range(self.width):
      if (self.cells[(self.width-1-i)%3][(i)%3].p1act==True): 
        #if next diag bl is activ
        print("in diag2")
        if self.cells[(i-1)%3][(i+1)%3].p1act==True:
          #if next diag br is empty
          if (self.cells[(i-2)%3][(i+2)%3].p1act==False) and (self.cells[(i-2)%3][(i+2)%3].p2act==False):
            #save the empty space coordinates, return true
            self.block=(i-2,i+2)
            return True

        
        

  def compturn(self):
    #if a fcn called canBlock returns true, select the place to block. else, random thing below
    
    if self.canBlock()==True:
      print("blocked")
      self.cells[self.block[0]%3][self.block[1]%3].p2act=True
    else:
      while (self.cells[self.p2x][self.p2y].p1act==True) or (self.cells[self.p2x][self.p2y].p2act==True):
        self.p2x=random.randrange(3)
        self.p2y=random.randrange(3)
      
      self.cells[self.p2x][self.p2y].p2act=True
    self.moves+=1
    #print (self.moves)
    self.draw(canvas,False)



  def didP1Win(self):

    #vert check
    for i in range(self.width):
      if (self.cells[i][0].p1act==True) and (self.cells[i][1].p1act==True) and (self.cells[i][2].p1act==True):
       # print('vert')
        return True
    #horiz check
    for i in range(self.height):
      if (self.cells[0][i].p1act==True) and (self.cells[1][i].p1act==True) and (self.cells[2][i].p1act==True):
        #print('horiz')
        return True
    i=0
    ii=(self.width-1)
    #diag checks
    if (self.cells[i][i].p1act==True) and (self.cells[i+1][i+1].p1act==True) and (self.cells[i+2][i+2].p1act==True):
        #print ('diag1')
        return True
    if (self.cells[ii][i].p1act==True) and (self.cells[ii-1][i+1].p1act==True) and (self.cells[ii-2][i+2].p1act==True):
        #print ('diag2')
        return True

  def didP2Win(self):
    
    #vert check
    for i in range(self.width):
      if (self.cells[i][0].p2act==True) and (self.cells[i][1].p2act==True) and (self.cells[i][2].p2act==True):
        #print ('evrt')
        return True
    #horiz check
    for i in range(self.height):
      if (self.cells[0][i].p2act==True) and (self.cells[1][i].p2act==True) and (self.cells[2][i].p2act==True):
        #print ('horiz')
        return True
    i=0
    ii=(self.width-1)
    #diag checks
    if (self.cells[i][i].p2act==True) and (self.cells[i+1][i+1].p2act==True) and (self.cells[i+2][i+2].p2act==True):
        #print ('diag1')
        return True
    if (self.cells[ii][i].p2act==True) and (self.cells[ii-1][i+1].p2act==True) and (self.cells[ii-2][i+2].p2act==True):
        #print ('diag2')
        return True
    
      

  def draw(self, canvas, force):
    
    if force == True:
      for i in range(self.width):
        for cell in self.cells[i]:
          
    #if force is True       
          if cell.alive1 == True:
        #if p1 is activated, avg the selector(rs) and p1 color(r1a)
              if cell.p1act ==True:
                canvas.setFillColor((self.rs+self.r1a)//2, (self.gs+self.g1a)//2, (self.bs+self.b1a)//2)
        #if p2 is activated, avg the selector(rs) and p1 color(r2a)
              elif cell.p2act ==True:
                  canvas.setFillColor((self.rs+self.r2a)//2, (self.gs+self.g2a)//2, (self.bs+self.b2a)//2)
        #if neither, avg the selector(rs) and board(rb)
              else: 
                canvas.setFillColor((self.rs+self.rb)//2, (self.gs+self.gb)//2, (self.bs+self.bb)//2)

          # elif cell.alive2==True:
          #   canvas.setFillColor(self.r2, self.g2, self.b2)
          elif cell.p1act==True:
            canvas.setFillColor(self.r1a, self.g1a, self.b1a)
          elif cell.p2act==True:
            canvas.setFillColor(self.r2a, self.g2a, self.b2a)
          else:
            canvas.setFillColor(0,0,0)
         
          canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    #if force is False   
    else: 
      
      for i in range(self.width):
        for cell in self.cells[i]:
#if change
          if cell.alive2 != cell.last2 or cell.alive1 !=cell.last1:
#if selector (alive1), 
            if cell.alive1 == True:
        #if p1 is activated, avg the selector(rs) and p1 color(r1a)
              if cell.p1act ==True:
                canvas.setFillColor((self.rs+self.r1a)//2, (self.gs+self.g1a)//2, (self.bs+self.b1a)//2)
        #if p2 is activated, avg the selector(rs) and p1 color(r2a)
              elif cell.p2act ==True:
                  canvas.setFillColor((self.rs+self.r2a)//2, (self.gs+self.g2a)//2, (self.bs+self.b2a)//2)
        #if neither, avg the selector(rs) and board(rb)
              else: 
                canvas.setFillColor((self.rs+self.rb)//2, (self.gs+self.gb)//2, (self.bs+self.bb)//2)

            # elif cell.alive2==True:
            #   canvas.setFillColor(self.r2, self.g2, self.b2)
            elif cell.p1act==True:
              canvas.setFillColor(self.r1a, self.g1a, self.b1a)
            elif cell.p2act==True:
              canvas.setFillColor(self.r2a, self.g2a, self.b2a)
            else:
              canvas.setFillColor(0,0,0)
            canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    canvas.display()
    

board=Board(3,3)
import picture
canvas = picture.Picture(800,600)


def main():
  import time
  setup = 1
  board.initialize(setup)
  board.draw(canvas,True)
  time.sleep(1)
  

  while 1 == 1:
    direction = getch.getch()

    if direction.upper() == 'S' or  direction.upper() == 'W' or direction.upper() == 'A' or direction.upper() == 'D' or direction.upper() == 'J'or  direction.upper() == 'K'or  direction.upper() == 'L'or  direction.upper() == 'I'or  direction.upper() == 'P':


      
      board.update(direction)
      #checkinput
        #incrment/print moves 
        #check for win   (set True)
        #compturn   
        #draw(True)
      #updatestuff
      board.checkwincases()
      #if win
        #print,reset,draw
      #x2
      #if moves 9, print,reset, draw
      board.draw(canvas,False)
      #draw
      
    
    #time.sleep(0.1)
    
    
    
main()