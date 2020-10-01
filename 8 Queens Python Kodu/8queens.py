import math
import random as rnd
import time


class NQueen(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def move(self):
        self.row += 1

    def is_conflict(self, q):
        # Argüman olarak verilen veziri tehdit edip etmediğini kontrol eden metot
        if self.row == q.get_row() or self.column == q.get_column():
            return True
        elif math.fabs(self.column - q.get_column()) == math.fabs(self.row - q.get_row()):
            return True
        return False

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column


def generate_board(n):
    # Rastgele konumlara yerleştirilen vezirlerle tahta oluşturma işlemi
    start_board = []
    for i in range(n):
        start_board.append(NQueen(rnd.randint(0, n - 1), i))
    return start_board


def print_state(n, state):
    # Tahtanın anlık durumunu yazdıran metot
    # Boş kareler için "-" yazdırılıyor
    # Vezir bulunan kareler için ise "Q" yazdırılıyor
    tmp = []
    for i in range(n):
        tmp.append(["-"] * n)
    for i in range(n):
        tmp[state[i].get_row()][state[i].get_column()] = "Q"
    for i in range(n):
        for j in range(n):
            print(tmp[i][j], end="  ")
        print()


def find_heuristic(state):
    heuristic = 0
    k = len(state)
    for i in range(k):
        for j in range(i+1, k):
            if state[i].is_conflict(state[j]):
                heuristic += 1
    return heuristic


def next_board(n, present_board):
    global random_restarts, heu, steps, steps_after_restart
    nxt = [""] * n
    tmp = [""] * n
    present_heu = find_heuristic(present_board)
    best_heu = present_heu

    for i in range(n):
        nxt[i] = NQueen(present_board[i].get_row(), present_board[i].get_column())
        tmp[i] = nxt[i]

    for i in range(n):
        if i > 0:
            tmp[i-1] = NQueen(present_board[i-1].get_row(), present_board[i-1].get_column())
        tmp[i] = NQueen(0, tmp[i].get_column())

        for j in range(n):
            tmp_heu = find_heuristic(tmp)
            if tmp_heu < best_heu:
                best_heu = tmp_heu
                for k in range(n):
                    nxt[k] = NQueen(tmp[k].get_row(), tmp[k].get_column())
            if tmp[i].get_row() != n-1:
                tmp[i].move()

    if best_heu == present_heu:
        random_restarts += 1
        steps_after_restart = 0
        nxt = generate_board(n)
        heu = find_heuristic(nxt)
    else:
        heu = best_heu
    steps += 1
    steps_after_restart += 1
    return nxt


def get_n():
    n = int(input("Enter the number of queens: "))
    while n == 2 or n == 3:
        print("No solution possible for", n, "queens")
        n = get_n()
    return n


def main():
    n = get_n()

    start = time.time()
    print("One of the solutions to", n, "queens using hill climbing with random restart")
    board = generate_board(n)
    present_heu = find_heuristic(board)

    while present_heu != 0:
        board = next_board(n, board)
        present_heu = heu
    end = time.time()

    elapsed = end - start
    print_state(n, board)
    print("Total number of steps climbed:", steps)
    print("Number of random restarts:", random_restarts)
    print("Steps climbed after last restart:", steps_after_restart)
    print("Time elapsed (secs):", format(elapsed, ".4f"))


random_restarts = 0
heu = 0
steps = 0
steps_after_restart = 0
main()
