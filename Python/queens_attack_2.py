# Queen's Attack 2
# Determine how many squares a queen at a given position can attack and return it

import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Sets the max moves to the distance to the board's edge.
    It then loops through all obstacles to find out if one is in the path of the queen.
    If so, max moves are updates to reflect the obstacle.
    """
    
    diag_1 = min(r_q - 1, c_q - 1)
    diag_2 = min(n - r_q, n - c_q)
    diag_3 = min(n - r_q, c_q - 1)
    diag_4 = min(r_q - 1, n - c_q)

    vert_1 = c_q - 1
    vert_2 = n - c_q

    horiz_1 = r_q - 1
    horiz_2 = n - r_q

    for obstacle in obstacles:
        if r_q > obstacle[0] and c_q > obstacle[1] and r_q - obstacle[0] == c_q - obstacle[1]:
            diag_1 = min(diag_1, r_q - obstacle[0] - 1)

        if obstacle[0] > r_q and obstacle[1] > c_q and  obstacle[0] - r_q == obstacle[1] - c_q:
            diag_2 = min(diag_2, obstacle[0] - r_q - 1)

        if obstacle[0] > r_q and c_q > obstacle[1] and  obstacle[0] - r_q == c_q - obstacle[1]:
            diag_3 = min(diag_3, obstacle[0] - r_q - 1)

        if r_q > obstacle[0] and obstacle[1] > c_q and r_q - obstacle[0] == obstacle[1] - c_q:
            diag_4 = min(diag_4, r_q - obstacle[0] - 1)

        if r_q == obstacle[0] and obstacle[1] < c_q:
            vert_1 = min(vert_1, c_q - obstacle[1] - 1)

        if r_q == obstacle[0] and obstacle[1] > c_q:
            vert_2 = min(vert_2, obstacle[1] - c_q - 1)

        if c_q == obstacle[1] and obstacle[0] < r_q:
            horiz_1 = min(horiz_1, r_q - obstacle[0] - 1)

        if c_q == obstacle[1] and obstacle[0] > r_q:
            horiz_2 = min(horiz_2, obstacle[0] - r_q - 1)
        
    return diag_1 + diag_2 + diag_3 + diag_4 + vert_1 + vert_2 + horiz_1 + horiz_2


def queensAttackFirstAttempt(n, k, r_q, c_q, obstacles):
    """
    First attempt at a solution. Works wonderfully, but times out on large boards due to the number of possible moves.
    """

    move_count = 0

    # setup possible moves list, starting up and going clockwise
    possible_moves = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

    # loop through possible moves list
    for move in possible_moves:

        # loop through length of board
        for unit in range(1, n):

            new_position = [r_q + (unit * move[0]), c_q + (unit * move[1])]
            if new_position in obstacles or new_position[0] not in range(1, n + 1) or new_position[1] not in range(1, n + 1):
                break

            move_count += 1
    
    return move_count
        

if __name__ == "__main__":
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + "\n")