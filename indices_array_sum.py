nums = [2, 7, 11, 15]


def two_sum(nums: int, target: List[int]) -> List[int]:
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return[seen[remaining], i]
        seen[v] = i
    return print(seen[v], seen[i])


target = int(input("Enter a number: "))
two_sum(nums, target)
