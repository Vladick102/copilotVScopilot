import heapq

def hamming(n):
    # Initialize the priority queue with the first Hamming number (1)
    pq = [1]
    seen = set([1])  # To avoid duplicates

    # Generate the next n-1 Hamming numbers
    for _ in range(n - 1):
        current_hamming = heapq.heappop(pq)  # Get the smallest Hamming number
        i, j, k = current_hamming // 2, current_hamming // 3, current_hamming // 5

        # Generate the next Hamming numbers by multiplying with 2, 3, and 5
        for factor in [2, 3, 5]:
            next_hamming = factor * current_hamming
            if next_hamming not in seen:
                seen.add(next_hamming)
                heapq.heappush(pq, next_hamming)

    return heapq.heappop(pq)