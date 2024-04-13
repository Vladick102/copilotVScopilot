def smaller(nums):
    # Create a list of distinct elements in nums, sorted in ascending order
    sorted_nums = sorted(set(nums))

    # Create a map from each element in nums to its position in sorted_nums
    num_to_pos = {num: i + 1 for i, num in enumerate(sorted_nums)}

    # Create a Binary Indexed Tree with an extra 0 at the beginning
    bit = [0] * (len(sorted_nums) + 1)

    # Function to compute the prefix sum up to a given position in the BIT
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Function to add a value to a given position in the BIT
    def update(i):
        while i < len(bit):
            bit[i] += 1
            i += i & -i

    # Compute the result
    res = []
    for num in reversed(nums):
        pos = num_to_pos[num]
        res.append(query(pos - 1))
        update(pos)
    res.reverse()

    return res
