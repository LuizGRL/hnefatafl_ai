import pygame as p
import HnefataflEngine
WIDTH = HEIGHT = 660 #qualquer numero divisivel por 22 pode ser usado
DIMENSION = 11
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}

def loadImages():
    # Carrega as imagens
    dp_image = p.image.load('Imagens/defense.png')
    ap_image = p.image.load('Imagens/attack.png')
    tk_image = p.image.load('Imagens/king.png')

    # Redimensiona as imagens para SQ_SIZE
    IMAGES['dp'] = (p.transform.scale(dp_image, (SQ_SIZE, SQ_SIZE)), p.Rect(0, 0, SQ_SIZE, SQ_SIZE))
    IMAGES['ap'] = (p.transform.scale(ap_image, (SQ_SIZE, SQ_SIZE)), p.Rect(0, 0, SQ_SIZE, SQ_SIZE))
    IMAGES['tk'] = (p.transform.scale(tk_image, (SQ_SIZE, SQ_SIZE)), p.Rect(0, 0, SQ_SIZE, SQ_SIZE))



def main():
    p.init()
    WHITE = p.Color("white")
    screen = p.display.set_mode((660,660))
    clock = p.time.Clock()
    screen.fill(WHITE)
    gs = HnefataflEngine.GameState()
    loadImages()
    running = True
    sqSelected= ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks = [] #essa logica vai limpar a escolha caso o usuário selecione a mesma casa     
                else:
                    sqSelected = (row, col)
                
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2:
                    startRow, startCol = playerClicks[0]
                    if gs.board[startRow][startCol]=="eh":
                        pass
                    else:
                        move = HnefataflEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                        gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []

        DrawGameState(screen,gs)

        clock.tick(MAX_FPS)
        p.display.flip()

def DrawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)

def drawBoard(screen):
    colors = [p.Color("#653210"),p.Color("#4b250c")]
    edge_color = p.Color("#201409")
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            if (r == 0 and c == 0) or (r == DIMENSION - 1 and c == DIMENSION - 1) or (r == 0 and c == DIMENSION - 1) or (r == DIMENSION - 1 and c == 0):
                color = edge_color
            else:
                color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            p.draw.rect(screen, p.Color("black"), p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)  # 1 é a espessura da borda

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "eh" and piece != "xh":
                image_info = IMAGES.get(piece)  # Use .get() para evitar KeyError
                if image_info:
                    # Verifique se image_info é uma tupla antes de desempacotar
                    if isinstance(image_info, tuple) and len(image_info) == 2:
                        surface, rect = image_info
                        screen.blit(surface, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    else:
                        print(f"Entrada inválida para a peça {piece} em IMAGES.")
                else:
                    print(f"Imagem para a peça {piece} não encontrada em IMAGES.")




main()
