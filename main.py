print()
def sum(a,b,c):
    return a+b+c

def printBoard(xState,zState):
    one='X' if xState[6] else ('O' if zState[6] else 1)
    two='X' if xState[7] else ('O' if zState[7] else 2)
    three='X' if xState[8] else ('O' if zState[8] else 3)
    four='X' if xState[3] else ('O' if zState[3] else 4)
    five='X' if xState[4] else ('O' if zState[4] else 5)
    six='X' if xState[5] else ('O' if zState[5] else 6)
    seven='X' if xState[0] else ('O' if zState[0] else 7)
    eight='X' if xState[1] else ('O' if zState[1] else 8)
    nine='X' if xState[2] else ('O' if zState[2] else 9)
    # nine='X' if xState[8] else ('O' if zState[8] else 8)
    print(f" {seven} | {eight} | {nine} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print(f"---|---|---")
    print(f" {one} | {two} | {three} ")

def checkWin(xState,zState,player1,player2):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[6,7,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xState[win[0]],xState[win[1]],xState[win[2]])==3:
            print(f"{player1} won the match!")
            return 1
        if sum(zState[win[0]],zState[win[1]],zState[win[2]])==3:
            print(f"{player2} won the match!")
            return 0
    return -1

numberChange={7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}

if __name__=="__main__":
    player1=input("Enter Player 1's name : ")
    player2=input("Enter Player 2's name : ")
    print()
    xState=[0,0,0,0,0,0,0,0,0]
    zState=[0,0,0,0,0,0,0,0,0]
    turn=1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")  
    print()
    printBoard(xState,zState)  
    while True:
        if turn == 1:
            print(f"{player1}'s Chance, put X")
            value=int(input("Please enter a value : "))
            print()
            xState[numberChange[value]]=1
        else:
            print(f"{player2}'s Chance, put O")
            value=int(input("Please enter a value : "))
            print()
            zState[numberChange[value]]=1
        printBoard(xState,zState)
        if checkWin(xState,zState,player1,player2)!=-1:
            break
        turn=1-turn
print("Match Over!")