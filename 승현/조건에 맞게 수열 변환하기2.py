def solution(arr):
    answer = 0
    x = 0
    
    while (True):
        now_arr = []
        for i in range(0, len(arr)):
            now_arr.append(arr[i])

        # print(now_arr)
        for j in range(0, len(arr)):
            if arr[j] >= 50 and arr[j] % 2 == 0:
                arr[j] = arr[j] // 2
            elif arr[j] < 50 and arr[j] % 2 == 1:
                arr[j] = (arr[j] * 2) + 1
        
        # print(now_arr)
        # print(arr)
        # print(x)
        cnt = 0
        for i in range(0, len(arr)):
            if now_arr[i] == arr[i]:
                cnt = cnt + 1
                
        if cnt == len(arr):
            answer = x
            return answer
        
        x = x + 1

# print(solution([1, 2, 3, 100, 99, 98]))