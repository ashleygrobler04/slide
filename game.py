import random, pygame, speech, display, time, math

class Game:
    def __init__(self):
        self.grid=[[1,2,3],[4,5,6],[7,8,'']]
        self.moves=0
        self.x=0
        self.y=0
        self.startTime=0
        self.endTime=0
        self.elapsed=0
    
    def initialize(self):
        random.shuffle(self.grid)
        self.startTime=time.time()
        if self.moves !=0:
            self.moves=0

    def didWin(self):
        won=self.grid==[[1,2,3],[4,5,6],[7,8,'']]
        if won:
            display.display_message('congratulations. you won the game.')
            quit()

    def move(self, direction=0):
        """Move a part in a spessific direction if possible. Use 1 for moving forwards, 2 for moving to the right, 3 for moving backwards and 4 for moving left."""
        temp=0
        if direction==1 and self.y<2:
            if self.grid[self.x][self.y+1]=="":
                temp=self.grid[self.x][self.y]
                self.grid[self.x][self.y+1]=temp
                self.grid[self.x][self.y]=""
                temp=0
                self.moves+=1
        elif direction==2 and self.x<2:
            if self.grid[self.x+1][self.y]=="":
                temp=self.grid[self.x][self.y]
                self.grid[self.x+1][self.y]=temp
                self.grid[self.x][self.y]=""
                temp=0
                self.moves+=1

        elif direction==3 and self.y>0:
            if self.grid[self.x][self.y-1]=="":
                temp=self.grid[self.x][self.y]
                self.grid[self.x][self.y-1]=temp
                self.grid[self.x][self.y]=""
                temp=0
                self.moves+=1

        elif direction==4 and self.x>0:
            if self.grid[self.x-1][self.y]=="":
                temp=self.grid[self.x][self.y]
                self.grid[self.x-1][self.y]=temp
                self.grid[self.x][self.y]=""
                temp=0
                self.moves+=1


    def loop(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and self.y<2:
                    self.y+=1
                    speech.speak(f'{self.grid[self.x][self.y]}')
                elif event.key==pygame.K_DOWN and self.y>0:
                    self.y-=1
                    speech.speak(f'{self.grid[self.x][self.y]}')
                elif event.key==pygame.K_LEFT and self.x>0:
                    self.x-=1
                    speech.speak(f'{self.grid[self.x][self.y]}')
                elif event.key==pygame.K_RIGHT and self.x<2:
                    self.x+=1
                    speech.speak(f'{self.grid[self.x][self.y]}')
                elif event.key==pygame.K_a:
                    self.move(4)
                elif event.key==pygame.K_s:
                    self.move(3)
                elif event.key==pygame.K_d:
                    self.move(2)
                elif event.key==pygame.K_w:
                    self.move(1)
                elif event.key==pygame.K_q:
                    self.endTime=time.time()
                    self.elapsed=self.endTime-self.startTime
                    display.display_message(f'This game lasted for {round(self.elapsed)} seconds and you finished with {self.moves} moves.')
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_m:
                    speech.speak(f'{self.moves} Moves')
