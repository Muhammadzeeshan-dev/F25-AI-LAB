import math
def minimax(depth, index, maxTurn, scores, target, counter):
    if depth == target:
        counter[0] += 1
        return scores[index]
    left = minimax(depth + 1, index * 2, not maxTurn,
                   scores, target, counter)
    right = minimax(depth + 1, index * 2 + 1, not maxTurn,
                    scores, target, counter)
    if maxTurn:
        return max(left, right)
    return min(left, right)

def alphabeta(depth, index, maxTurn, scores, target,
              alpha, beta, counter):
    if depth == target:
        counter[0] += 1
        return scores[index]
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(
                depth + 1, index * 2 + i, False,
                scores, target, alpha, beta, counter
            ))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(
                depth + 1, index * 2 + i, True,
                scores, target, alpha, beta, counter
            ))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
original = [3, 5, 2, 9, 0, 7, 0, 0]
reordered = [3, 5, 2, 9, 0, 0, 0, 7]

for name, scores in [
    ("Original Order", original),
    ("Reordered Branches", reordered)
]:
    depth = int(math.log2(len(scores)))

    m_count = [0]
    a_count = [0]

    m_value = minimax(0, 0, True, scores, depth, m_count)
    a_value = alphabeta(
        0, 0, True, scores, depth,
        float('-inf'), float('inf'), a_count
    )
    print("\n" + name)
    print("Minimax Value:", m_value)
    print("Minimax Leaves:", m_count[0])
    print("Alpha-Beta Value:", a_value)
    print("Alpha-Beta Leaves:", a_count[0])
