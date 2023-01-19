import random
import arcade
import arcade.color
import time

from typing import List


class space:
    def __init__(self, x, y, width, height, percentChance=0.1):
        self.isBomb = random.random() < percentChance
        self.x = x * width
        self.y = y * height
        self.rawX = x
        self.rawY = y 
        self.width = width
        self.height = height
        self.isFlagged = False
        self.isRevealed = False
        self.neighbors = []
    def populateData(self, board):
        self.bombedNeighbors = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if any([self.rawX + j < 0, self.rawY + i < 0]):
                    continue
                try:
                    self.neighbors.append(board[self.rawY + i][self.rawX + j])
                    if(board[self.rawY + i][self.rawX + j].isBomb):
                        self.bombedNeighbors += 1
                except IndexError:
                    continue
    def reveal(self):
        self.isRevealed = True
        if(self.isBomb == True):
            print("You Lose")
            
        
    
    def on_draw(self):
        if self.isRevealed:
            if self.isBomb:
                arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.RED)
                arcade.draw_xywh_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK)
                print("You hit a bomb")
                time.sleep(2)
                exit()
            else:
                arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.WHITE)
                arcade.draw_xywh_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK)
                arcade.Text(str(self.bombedNeighbors) if self.bombedNeighbors != 0 else "", self.x + self.width/4, self.y + self.height/2, arcade.color.BLACK, 12).draw()
        else:
                arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.GRAY)
                arcade.draw_xywh_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK)
        if self.isFlagged:
            arcade.draw_xywh_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.YELLOW)
            arcade.draw_xywh_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK)
    def __repr__(self) -> str:
        return f"space({self.x}, {self.y}, {self.width}, {self.height}, {self.isBomb})\n"
