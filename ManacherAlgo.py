def manacher(s: str) -> str:
    # Preprocess the string
    T = '#' + '#'.join(s) + '#'
    n = len(T)
    P = [0] * n
    C, R = 0, 0

    #Manacher's algorithm
    for i in range(n):
        mirror = 2 * C - i  # Mirror of i with respect to center C
        if i < R:
            P[i] = min(R - i, P[mirror])

        # Try to expand the palindrome centered at i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Update C and R if the palindrome centered at i expands past R
        if i + P[i] > R:
            C, R = i, i + P[i]

    print(P)
    # Find the maximum value in P
    max_length = max(P)
    center_index = P.index(max_length)

    # Translate back to original string
    start = (center_index - max_length) // 2
    return s[start:start + max_length]

(manacher("ababac"))