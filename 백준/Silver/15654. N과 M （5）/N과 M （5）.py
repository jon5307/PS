def bfs(N, M, l, nums):
    if len(l) == M:
        # for i in l:
        #     print(nums[i - 1], end=" ")
        # print()
        print(*l, sep=" ")
        return
    if len(l) == 0:
        for i in nums:
            new_num = nums[:]
            new_num.remove(i)
            bfs(N, M, [i], new_num)
        return
    for i in nums:
        new_num = nums[:]
        new_num.remove(i)
        bfs(N, M, l + [i], new_num)


if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    bfs(N, M, [], nums)
