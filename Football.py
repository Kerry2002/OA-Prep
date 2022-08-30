


def counts(teamA, teamB):
    answer = []
    teamA.sort()
    for score in teamB:
        low, high = 0, len(teamA) - 1
        while low <= high:
            mid = (low + high) // 2
            if teamA[mid] > score:
                high = mid - 1
            else:
                low = mid + 1
        answer.append(low)

    return answer
    # note
if __name__ == "__main__":
    t1 = [1,4,2,4]
    t2 = [3,5]
    print(counts(t1,t2))