def solve():
    f = open('user.out', 'w')
    for nums in map(loads, stdin):
        idx = len(nums) - 1
        while idx > 0:
            idx_goal = idx
            idx -= 1
            while idx >= 0 and idx + nums[idx] < idx_goal:
                idx -= 1
        print('true' if idx == 0 else 'false', file=f)

solve()
exit() 