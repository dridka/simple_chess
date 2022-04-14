from colorama import Back, Style

dark_background = Back.MAGENTA
normal_style = Style.RESET_ALL

chessboard = [["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
              ["♙"]*8,
              [" "]*8,
              [" "]*8,
              [" "]*8,
              [" "]*8,
              ["♟"]*8,
              ["♜", "♞", "♝", "♚", "♛", "♝", "♞", "♜"]]

# print whole chessboard
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print(chessboard[i][j], end="")
        else:
            print(dark_background + chessboard[i][j] + normal_style, end="")
    print("")
