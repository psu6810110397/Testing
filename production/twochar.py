def alternate(s):

    unique_chars = list(set(s))
    max_len = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]

            filtered = [c for c in s if c == char1 or c == char2]

            is_alternating = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    is_alternating = False
                    break

            if is_alternating:
                max_len = max(max_len, len(filtered))

    return max_len
