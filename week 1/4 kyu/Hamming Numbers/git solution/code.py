import heapq


def hamming(n):
    h = [1]
    seen = {1}
    for _ in range(n):
        val = heapq.heappop(h)
        for mult in [2, 3, 5]:
            m = val * mult
            if m not in seen:
                seen.add(m)
                heapq.heappush(h, m)
    return val
