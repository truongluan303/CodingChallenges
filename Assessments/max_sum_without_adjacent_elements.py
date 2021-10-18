
def max_sum_without_adj(nums: list[int]) -> int:

    include = 0
    exclude = 0

    for num in nums:
        
        current = max(include, exclude)

        include = exclude + num
        exclude = current

    return max(include, exclude)