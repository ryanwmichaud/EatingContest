
import random
#import getch
class Cell:
  "cell class for making cells"
  def __init__(self,x,y):
    'create new cells'
    self.alive1=False
    self.alive2=False
    self.last1=False
    self.last2=False
    self.x=x
    self.y=y
    self.start=0
    self.end=0
    self.food=False
    self.freeze=False
  def update(self,cells,direction):
#p1 and p2 move

    if (self.x==board.p1x and self.y==board.p1y)==True:
      self.alive1=True
    else:
      self.alive1=False
      
    if   (self.x==board.p2x and self.y==board.p2y)==True:
      self.alive2=True
    else:
      self.alive2=False

    
    

    
#if p1 cursor on food
    if self.x==board.p1x and self.y==board.p1y and self.food == True:
      #swallow
      self.food=False
      #new random food 
      board.cells[random.randrange(board.width)][random.randrange(board.height)].food=True
      board.draw(canvas,True)
      board.r1+=32
      board.g1-=32
      
#if p2 cursor on food
    if self.x==board.p2x and self.y==board.p2y and self.food == True:
      #swallow
      self.food=False
      #new random food 
      board.cells[random.randrange(board.width)][random.randrange(board.height)].food=True
      board.draw(canvas,True)
      board.r2+=32
      board.g2-=32
#if p1 cursor on freeze
    if self.x==board.p1x and self.y==board.p1y and self.freeze == True:
      #swallow
      self.freeze=False
      #new random freeze
      board.cells[random.randrange(board.width)][random.randrange(board.height)].freeze=True
      board.draw(canvas,True)
      #freeze opponent
      board.p2frozen=True
      print("\nplayer 2 is frozen!")
      #start freeze timer. really just save the time of freezing so we can unfreeze x moves later
      board.starttimer=board.moves
      
#if p2 cursor on freeze
    if self.x==board.p2x and self.y==board.p2y and self.freeze == True:
      #swallow
      self.freeze=False
      #new random freeze
      board.cells[random.randrange(board.width)][random.randrange(board.height)].freeze=True
      board.draw(canvas,True)
      #freeze opponent
      board.p1frozen=True
      print("\nplayer 1 is frozen!")
      #start freeze timer. really just save the time of freezing so we can unfreeze x moves later
      board.starttimer=board.moves

      
      

 
  def __str__(self):
    return "x=" + str(self.x) + ", y=" + str(self.y)


class Board:
  "does the stuff"
  def __init__ (self,width,height):
    "make the board"
    self.sizesq=30
    self.width=width
    self.height=height
    self.cells = []
    self.addcells(self.cells,self.width,self.height)
    self.starttimer=0
    self.endtimer=0
    self.p2x=3*self.width//4
    self.p1y=self.height//2
    self.p1x=self.width//4
    self.p2y=self.height//2
    self.moves=0
    self.d1='d'
    self.d2='l'
    self.r1=0
    self.g1=255
    self.b1=0
    self.r2=0
    self.g2=255
    self.b2=0
    self.p1frozen=False
    self.p2frozen=False

  def addcells(self,cells,width,height) : 
    for x in range(width):
      cells.append([])
      for y in range(height):
        cells[x].append(Cell(x, y))

  def initialize(self,setup):

    self.cells[random.randrange(self.width)][random.randrange(self.height)].food = True
    self.cells[random.randrange(self.width)][random.randrange(self.height)].food = True
    self.cells[random.randrange(self.width)][random.randrange(self.height)].food = True  
    self.cells[random.randrange(self.width)][random.randrange(self.height)].freeze = True     
    
    self.cells[self.p1x][self.p1y].alive1 = True
    self.cells[self.p2x][self.p2y].alive2 = True
   

  def update(self,direction):
    
    cellsfromboard=self.cells
    if board.p1frozen==False and board.p2frozen==False:
  #move cursor
      # if direction=='':
      #   if self.d == 'a':
      #     board.p1x=(board.p1x-1)%board.width
      #   elif self.d == 'd':
      #     board.p1x=(board.p1x+1)%board.width
      #   elif self.d == 'w':
      #     board.p1y=(board.p1y-1)%board.height
      #   elif self.d == 's':
      #     board.p1y=(board.p1y+1)%board.height
    
      if direction == 'a':
        self.d='a'
        board.p1x=(board.p1x-1)%board.width
      elif direction == 'd':
        self.d='d'
        board.p1x=(board.p1x+1)%board.width
      elif direction == 'w':
        self.d='w'
        board.p1y=(board.p1y-1)%board.height
      elif direction == 's':
        board.p1y=(board.p1y+1)%board.height
        self.d='s'

      elif direction == 'j':
        self.d2='j'
        board.p2x=(board.p2x-1)%board.width
      elif direction == 'l':
        self.d2='l'
        board.p2x=(board.p2x+1)%board.width
      elif direction == 'i':
        self.d2='i'
        board.p2y=(board.p2y-1)%board.height
      elif direction == 'k':
        board.p2y=(board.p2y+1)%board.height
        self.d2='k'
    elif board.p1frozen==False and board.p2frozen==True:
      if direction == 'a':
        self.d='a'
        board.p1x=(board.p1x-1)%board.width
      elif direction == 'd':
        self.d='d'
        board.p1x=(board.p1x+1)%board.width
      elif direction == 'w':
        self.d='w'
        board.p1y=(board.p1y-1)%board.height
      elif direction == 's':
        board.p1y=(board.p1y+1)%board.height
        self.d='s'
    elif board.p1frozen==True and board.p2frozen==False:  
      if direction == 'j':
        self.d2='j'
        board.p2x=(board.p2x-1)%board.width
      elif direction == 'l':
        self.d2='l'
        board.p2x=(board.p2x+1)%board.width
      elif direction == 'i':
        self.d2='i'
        board.p2y=(board.p2y-1)%board.height
      elif direction == 'k':
        board.p2y=(board.p2y+1)%board.height
        self.d2='k'
    else: 
      #nothing
      pass
  
  
    
    

#alive to last for p1 and p2
    for i in range(self.width):
      for cell in self.cells[i]:
        cell.last1 = cell.alive1

    for i in range(self.width):
      for cell in self.cells[i]:
        cell.last2 = cell.alive2
        

#update all
    for i in range (self.width):
      for cell in self.cells[i]:
        cell.update(cellsfromboard,direction)

#increment moves
    self.moves+=1
  #time to unfreeze?
    if board.p2frozen==True:
      endsat=board.starttimer+30
      remaining=endsat-board.moves
      #print("current move: ",board.moves,remaining," moves left til unstick at ", endsat)
      print(remaining)
      if board.moves>board.starttimer+30:
        board.p2frozen=False
  #time to unfreeze?
    elif board.p1frozen==True:
      endsat=board.starttimer+30
      remaining=endsat-board.moves
      #print("current move: ",board.moves,remaining," moves left til unstick at ", endsat)
      print(remaining)
      if board.moves>board.starttimer+30:
        board.p1frozen=False
    


  def draw(self, canvas, force):
    
    
    if force == True:
      for i in range(self.width):
        for cell in self.cells[i]:
          
          
          if cell.alive1==True:
            canvas.setFillColor(self.r1, self.g1, self.b1)
          elif cell.alive2==True:
            canvas.setFillColor(self.r2, self.g2, self.b2)
          elif cell.freeze==True:
            canvas.setFillColor(0, 100, 200)
          elif cell.food==True:
            canvas.setFillColor(255, 255, 255)
          else:
            canvas.setFillColor(0,0,0)
         
          canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    else: 
      
      for i in range(self.width):
        for cell in self.cells[i]:
#if change
          if cell.alive2 != cell.last2 or cell.alive1 !=cell.last1:
#if change to alive, red   if change to dead, white
            if cell.alive1 == True:
              canvas.setFillColor(self.r1, self.g1, self.b1)
            elif cell.alive2==True:
              canvas.setFillColor(self.r2, self.g2, self.b2)
            elif cell.freeze==True:
              canvas.setFillColor(0, 100, 200)
            elif cell.food==True:
              canvas.setFillColor(255, 255, 255)

            else:
              canvas.setFillColor(0,0,0)
            canvas.drawRectFill(cell.x*self.sizesq,cell.y*self.sizesq,
          self.sizesq,self.sizesq)
    canvas.display()
    

    



board=Board(20,20)
import picture
canvas = picture.Picture(800,600)




def main():
  import time
  setup = 1
  board.initialize(setup)
  board.draw(canvas,True)
  time.sleep(1)
  
  input("\nWelcome to Eating Contest!\n---------------------------\nRULES:\n-player 1 moves with the WASD keys\n-player 2 moves with the IJKL keys\n-eet dots and turn red to WIN\n-eat the blue dots to freeze your opponent \n-buttonmash to get unfrozen quickly!\n   --press enter to begin--")
  


  while 1 == 1:
    #direction = getch.getch()
    direction = input();

    if direction.upper() == 'S' or  direction.upper() == 'W' or direction.upper() == 'A' or direction.upper() == 'D' or direction.upper() == 'J'or  direction.upper() == 'K'or  direction.upper() == 'L'or  direction.upper() == 'I':
    
      board.update(direction)
      board.draw(canvas,False)
      
    
    
    #time.sleep(0.1)
    
    
    
main()