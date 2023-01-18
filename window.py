import space
import arcade

class Window(arcade.Window):
    def __init__(self, width, height, rowCount, colCount) -> None:
        self.board = [[space.space(row, col, width/colCount, height/rowCount) for row in range(rowCount)] for col in range(colCount)]
        super().__init__(width, height, "Minesweeper") #type: ignore
        self.xscl = width/colCount
        self.yScl = height/rowCount
        self.closedSet = []
        for col in self.board:
            for cell in col:
                cell.populateData(self.board)
    
    def on_draw(self) -> None:
        arcade.start_render()
        for col in self.board:
            for cell in col:
                cell.on_draw()
        arcade.finish_render()
        
    def on_update(self, delta_time: float) -> None:
        pass
    
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        print("Reveal" if button == 1 else "Flag")
        idxX, idxY = int(x // self.xscl), int(y // self.yScl)
        
        if button == 1:
            queue = []
            queue.append(self.board[idxY][idxX])
            cell = queue.pop(0)
            if not (cell.isRevealed or cell in self.closedSet):
                cell.reveal()
                self.closedSet.append(cell)
                if cell.bombedNeighbors == 0:
                    queue.extend(cell.neighbors)
            while len(queue) > 0:
                cell = queue.pop(0)
                if cell.isRevealed or cell in self.closedSet:
                    continue
                if cell.isBomb == False:
                    cell.reveal()
                self.closedSet.append(cell)
                if cell.bombedNeighbors == 0:
                    queue.extend(cell.neighbors)
        elif button == 4:
            self.board[idxY][idxX].isFlagged = not self.board[idxY][idxX].isFlagged
            
        