"""
Luiz Guilherme R Lins - 28/12/2023
Essa classe tem o proposito de realizar o "display" da tela, mostrar as peças o tablueiro e receber as informações (input) do usuário
"""

from plistlib import InvalidFileException


class GameState():
    def __init__(self):
        self.board =[
            ["xh", "eh", "eh", "ap", "ap", "ap", "ap", "ap", "eh", "eh", "xh"],
            ["eh", "eh", "eh", "eh", "eh", "ap", "eh", "eh", "eh", "eh", "eh"],
            ["eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh"],
            ["ap", "eh", "eh", "eh", "eh", "dp", "eh", "eh", "eh", "eh", "ap"],
            ["ap", "eh", "eh", "eh", "dp", "dp", "dp", "eh", "eh", "eh", "ap"],
            ["ap", "ap", "eh", "dp", "dp", "tk", "dp", "dp", "eh", "ap", "ap"],
            ["ap", "eh", "eh", "eh", "dp", "dp", "dp", "eh", "eh", "eh", "ap"],
            ["ap", "eh", "eh", "eh", "eh", "dp", "eh", "eh", "eh", "eh", "ap"],
            ["eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh"],
            ["eh", "eh", "eh", "eh", "eh", "ap", "eh", "eh", "eh", "eh", "eh"],
            ["xh", "eh", "eh", "ap", "ap", "ap", "ap", "ap", "eh", "eh", "xh"]]
        
        self.defenseToMove = True
        self.moveLog = []
    
    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "eh"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.defenseToMove = not self.defenseToMove
    
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()  
            self.board[move.startRow][move.startCol]   = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
        




class Move():
    logRow = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "11": 10}
    rowToLog = {v: k for k, v in logRow.items()}
    logCol = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10}
    colToLog = {v: k for k, v in logCol.items()}

    def __init__(self,startSq,endSq,board):
       

        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]        

        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def getHnefataflNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)

    def getRankFile(self,r,c):
        return self.colToLog[c] + self.rowToLog[r]






        
