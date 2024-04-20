class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= i & -i
        return sum


def smaller(nums):
    rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
    fenwick = FenwickTree(len(nums))
    for x in reversed(nums):
        res.append(fenwick.query(rank[x] - 1))
        fenwick.update(rank[x], 1)
    return res[::-1]
