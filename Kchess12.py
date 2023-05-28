class Move:
    def __init__(self, start:tuple, end:tuple, piece):
        self.sx = start[0]
        self.sy = start[1]
        self.ex = end[0]
        self.ey = end[1]
        self.start = start
        self.end = end
        self.piece = piece
    def __repr__(self):
        return f"{self.start} -> {self.end}"

class Player:
    def __init__(self, pitch):
        self.hand = []
        self.pitch = pitch
        self.defaultKingPosition = (3-int((pitch+1)/2*3), 1)
        self.pieces = []


class Piece:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.pieceName = ''
    def setPos(self, pos:tuple):
        self.x = pos[0]
        self.y = pos[1]
    def getAbleMove(self, x, y):
        _x = x
        _y = y
        moves = []
        for i in range(len(_x)):
            if self.x+_x[i] < 0 or self.x+_x[i] > 3 or self.y+_y[i] < 0 or self.y+_y[i] > 2:
                continue
            m = Move((self.x, self.y), (self.x+_x[i], self.y+_y[i]), self)
            moves.append(m)
        return moves
    def goMove(self, move:Move):
        if self.x != move.sx or self.y != move.sy:
            return False
        self.x = move.ex
        self.y = move.ey

        
        return [move.ex, move.ey]
    
    def __repr__(self):
        return self.pieceName
    
    def catched(self, attacker:Player):
        self.x = -1
        self.y = -1
        attacker.hand.append(self)


class Board:
    def __init__(self, pitch=0):
        self.pst = (0,0)
        self.plt = (3,2)
        self.pitch = pitch
    def boardInitialize(self, positivePlayer: Player, negativePlayer:Player):

        positive_piece = [
            King(positivePlayer),
            Sang(positivePlayer),
            Jang(positivePlayer),
            Ja(positivePlayer)
        ]

        negative_piece = [
            King(negativePlayer),
            Sang(negativePlayer),
            Jang(negativePlayer),
            Ja(negativePlayer)
        ]
        dp = positivePlayer.defaultKingPosition
        positive_piece[0].setPos(dp)
        positive_piece[1].setPos((dp[0], dp[1]-1))
        positive_piece[2].setPos((dp[0], dp[1]+1))
        positive_piece[3].setPos((dp[0]+1, dp[1]))

        dp = negativePlayer.defaultKingPosition
        negative_piece[0].setPos(dp)
        negative_piece[1].setPos((dp[0], dp[1]+1))
        negative_piece[2].setPos((dp[0], dp[1]-1))
        negative_piece[3].setPos((dp[0]-1, dp[1]))
        self.pieces = sum([positive_piece, negative_piece], [])

    def getBoard(self):
        board = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        for piece in self.pieces:
            board[piece.y][piece.x] = piece
        
        return board
    
    def getSquare(self, x,y):
        return self.getBoard()[y][x]



        
class King(Piece):
    def __init__(self, player):
        self.player = player
        self.pieceName = '왕'
    def ableMove(self):
        _x = [-1, 0, 1, 1, 1, 0, -1, -1]
        _y = [1, 1, 1, 0, -1 , -1, -1, 0]
        return self.getAbleMove(_x,  _y)
    
    
class Sang(Piece):
    def __init__(self, player):
        self.player = player
        self.pieceName = '상'
    def ableMove(self):
        _x = [-1, 1, 1, -1]
        _y = [1, 1, -1, -1]
        return self.getAbleMove(_x,  _y)
class Jang(Piece):
    def __init__(self, player):
        self.player = player
        self.pieceName = '장'
    def ableMove(self):
        _x = [0,1, 0, -1]
        _y = [1, 0, -1, 0]
        return self.getAbleMove(_x,  _y)
class Ja(Piece):
    def __init__(self, player: Player):
        self.player = player
        self.pieceName = '자'
    def ableMove(self):
        _x = [0, 1, 1, 1, 0, -1]
        _y = [1, 1, 0, -1, -1, 0]
        if self.pieceName == '자':
            _x = [self.player.pitch * 1]
            _y = [0]
        
        return self.getAbleMove(_x,  _y)
    def goMove(self, move: Move):
        if self.x != move.sx or self.y != move.sy:
            return False
        self.x = move.ex
        self.y = move.ey
        if 3 - self.defaultKingPosition == self.x:
            self.pieceName = '후'
        return [move.ex, move.ey]

if __name__ == '__main__':
    blue = Player(1)
    red = Player(-1)

    board = Board()
    board.boardInitialize(blue, red)

    

    



    




        

    
