
import math
scores = [3, 5, 2, 9, 0, 7, 0, 0]
treeDepth = int(math.log2(len(scores)))


def minimax(depth, index, maxTurn, scores, targetDepth, counter):
    if depth == targetDepth:
        counter[0] += 1
        return scores[index]

    if maxTurn:
        left = minimax(depth + 1, index * 2, False,
                       scores, targetDepth, counter)
        right = minimax(depth + 1, index * 2 + 1, False,
                        scores, targetDepth, counter)
        return max(left, right)

    else:
        left = minimax(depth + 1, index * 2, True,
                       scores, targetDepth, counter)
        right = minimax(depth + 1, index * 2 + 1, True,
                        scores, targetDepth, counter)
        return min(left, right)

def alphabeta(depth, index, maxTurn, scores, targetDepth,
              alpha, beta, counter):
    if depth == targetDepth:
        counter[0] += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')

        for i in range(2):
            child = alphabeta(
                depth + 1, index * 2 + i, False,
                scores, targetDepth, alpha, beta, counter
            )
            value = max(value, child)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for i in range(2):
            child = alphabeta(
                depth + 1, index * 2 + i, True,
                scores, targetDepth, alpha, beta, counter
            )
            value = min(value, child)
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value

minimax_counter = [0]
minimax_value = minimax(
    0, 0, True, scores, treeDepth, minimax_counter
)

print("Minimax Value:", minimax_value)
print("Minimax Leaves Evaluated:", minimax_counter[0])


alphabeta_counter = [0]
alphabeta_value = alphabeta(
    0, 0, True, scores, treeDepth,
    float('-inf'), float('inf'), alphabeta_counter
)

print("Alpha-Beta Value:", alphabeta_value)
print("Alpha-Beta Leaves Evaluated:", alphabeta_counter[0])
