# write your code here

def finished(state):

    if "_" in state:
        return "Game not finished"
    else:
        return "finished"


def impossible(state):

    count_o = 0
    count_x = 0

    for i in state:
        if i == 'O':
            count_o += 1
        elif i == 'X':
            count_x += 1

    if abs(count_o - count_x) > 1:
        return "impossible"
    else:
        return "possible"


def victory(state):

    line = state[::]
    test = line.replace('X', '1')
    test = test.replace('O', '0')
    win_set = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    win_x = 0
    win_o = 0

    for win in win_set:
        score = 0
        for pos in win:
            if test[pos] != "_":
                score += int(test[pos])
            else:
                score += 5
        if score == 3:
            win_x = 1
        elif score == 0:
            win_o += 1

    if win_x + win_o == 0:
        return "draw"
    elif win_x == 1 and win_o == 0:
        return "X"
    elif win_o == 1 and win_x == 0:
        return "O"
    else:
        return "impossible"


def string_line(line):

    return "| {} {} {} |".format(line[0], line[1], line[2])



def outcome(state):

    # print("outcome")

    if impossible(state) == "impossible" or victory(state) == "impossible":
        print("Impossible")
    elif victory(state) == "X":
        print("X wins")
    elif victory(state) == "O":
        print("O wins")
    elif victory(state) == "draw" and finished(state) == "finished":
        print("Draw")
    elif victory(state) == "draw" and finished(state) == "Game not finished":
        print("Game not finished")


def get_cell(state):

    x, y = input("Enter the coordinates:").split()

    print(x, y)

    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        return "error"

    board = ["1", "2", "3"]

    if x not in board or y not in board:
        print("Coordinates should be from 1 to 3!")
        return "error"

    cells = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    cell = cells[int(x)-1][int(y)-1]

    if state[cell] != "_":
        print("This cell is occupied! Choose another one!")
        return "error"

    return cell


def update_state(state, cell, player):

    if player:
        mark = "X"
    else:
        mark = "O"

    state_list = list(state)

    state_list[cell] = mark

    state = ''.join(state_list)

    return state


def draw_game(state):

    line_1 = state[:3].replace("_", " ")
    line_2 = state[3:6].replace("_", " ")
    line_3 = state[6:].replace("_", " ")

    print("-" * 9)
    print(string_line(line_1))
    print(string_line(line_2))
    print(string_line(line_3))
    print("-" * 9)


def main():

    # state = input("Enter cells:")
    state = "_________"

    draw_game(state)

    #cell = get_cell(state)

    player = True

    while any([finished(state) == "Game not finished"]):
    #while cell == "error":

        cell = get_cell(state)

        if not str(cell).isdigit():
            continue

        state = update_state(state, cell, player)

        draw_game(state)

        if victory(state) == "X" or victory(state) == "O":
            print("{} wins".format(victory(state)))
            break
        else:
            print("Draw")
        player = not player



main()
