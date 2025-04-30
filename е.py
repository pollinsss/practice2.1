def combination_sum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, target - candidates[i], path + [candidates[i]])

    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result

candidates1 = [2, 5, 7, 1, 3]
target1 = 5
print(combination_sum2(candidates1, target1))

