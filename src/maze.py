import random


class Maze:
    def __init__(self, x: int, y: int, generationMethod: str):
        # self._mazeWalls
        # False - free, True - wall 
        self._x = x
        self._y = y
        self._mazeWalls = [[True for _ in range(y + 1)] for _ in range(x + 1)]

        match generationMethod:
            case 'binTree':
                self.binTreeMazeGenerate()
            case 'sidewinder':
                self.sidewinderMazeGenerate()
            case _:
                raise ValueError('This method is unavailable. Use these: "binTree", "sidewinder"')
    
    def __getitem__(self, key):
        return self._mazeWalls[key]

    def __setitem__(self, key, val: int):
        self._mazeWalls[key] = val
         
    def __str__(self):
        s = ''
        for i in range(self._x + 1):
            for j in range(self._y + 1):
                if self[i][j]:
                    s += '#'
                else:
                    s += ' '
            s += '\n'
        
        return s

    def getSize():
        return (self._x, self._y)

    def binTreeMazeGenerate(self):
        for i in range(self._x + 1):
            for j in range(self._y + 1):
                if i == 0 and j == self._y:
                    continue
                elif i == 0 and j < self._y:
                    self[i][j + 1] = False
                elif j == self._y and i > 0:
                    self[i - 1][j] = False
                else:
                    if random.randint(0, 1):
                        self[i - 1][j] = False
                    else:
                        self[i][j + 1] = False
    
    def sidewinderMazeGenerate(self):
        for j in range(self._y + 1):
            self[0][j] = False
        for i in range(1, self._x + 1):
            curGroup = [0]
            for j in range(self._y + 1):
                if random.randint(0, 9) < 5:
                    self._mazeWalls[i][j] = False   
                    curGroup.append(j)                
                else:
                    self._mazeWalls[i - 1][random.choices(curGroup)[0]] = False
                    curGroup.clear()
                    curGroup.append(j + 1)
                

def main():
    print('binTree')
    print(Maze(40, 160, 'binTree')) 
    print('sidewinder')
    print(Maze(40, 160, 'sidewinder')) 
    print('binTree')

if __name__ == '__main__':
    main()
























