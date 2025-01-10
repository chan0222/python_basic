def count_change(board,x,y,start_color):
    changes = 0
    for i in range(8):
        for j in range(8):
            expect_color = 'w' if (i +j) % 2 == 0 else "B"
            if start_color == 'B':
                expect_color = 'B' if (i + j) % 2 == 2 else "W"
            if board[x + i][y+j] != expect_color:
                changes += 1
    return changes    
