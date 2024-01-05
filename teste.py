
matriz =   [["xh", "eh", "eh", "ap", "ap", "ap", "ap", "ap", "eh", "eh", "xh"],
            ["eh", "eh", "eh", "eh", "eh", "ap", "eh", "eh", "eh", "eh", "eh"],
            ["eh", "eh", "eh", "ap", "eh", "eh", "eh", "eh", "eh", "eh", "eh"],
            ["ap", "eh", "eh", "eh", "eh", "dp", "eh", "eh", "eh", "eh", "ap"],
            ["ap", "eh", "eh", "eh", "dp", "dp", "dp", "eh", "eh", "eh", "ap"],
            ["ap", "ap", "eh", "dp", "dp", "tk", "dp", "dp", "eh", "ap", "ap"],
            ["ap", "eh", "eh", "eh", "dp", "dp", "dp", "eh", "eh", "eh", "ap"],
            ["ap", "eh", "eh", "eh", "eh", "dp", "eh", "eh", "eh", "eh", "ap"],
            ["eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh", "eh"],
            ["eh", "eh", "eh", "eh", "eh", "ap", "eh", "eh", "eh", "eh", "eh"],
            ["xh", "eh", "eh", "ap", "ap", "ap", "ap", "ap", "eh", "eh", "xh"]]


def mov(r_inicial,c_inicial,r_final,c_final,matriz):
        moves = []
        #Para esquerda
        if(c_inicial>c_final):
            while c_inicial >= c_final and c_inicial >= 0:
                if(matriz[r_inicial][c_inicial-1]=="eh"):
                    moves.append((r_inicial,c_inicial-1))
                    c_inicial = c_inicial-1
                else:
                    break
        #Para direita
        if(c_inicial<c_final):
            while c_inicial <= c_final and c_inicial <=10:
                if(matriz[r_inicial][c_inicial+1]=="eh"):
                    moves.append((r_inicial,c_inicial+1))
                    c_inicial = c_inicial+1
                else:
                    break

        #Para cima
        if(r_inicial>r_final):
            while r_inicial>=r_final and r_final>=0:
                if(matriz[r_inicial-1][c_inicial]=="eh"):
                    moves.append((r_inicial-1,c_inicial))
                    r_inicial = r_inicial-1
                else:
                    break
        #Para Baixo
        if(r_inicial<r_final):
            while r_inicial<=r_final and r_final>=0:
                if(matriz[r_inicial+1][c_inicial]=="eh"):
                    moves.append((r_inicial+1,c_inicial))
                    r_inicial = r_inicial+1
                else:
                    break;

        return moves




a= mov(5,3,9,3,matriz)
for i in a:
    print(i)

if((9,3) in a):
    print("Ok")
else:
    print()






