import heapq
def solution(n, works):
    answer = 0
    
    heap = []
    for i in works :
        heapq.heappush(heap, -i)
        
    for i in range(n) :
        pop = heapq.heappop(heap)
        if pop == 0 : # 모든 작업 끝 
            heapq.heappush(heap, 0)
            break
        value = pop + 1
        heapq.heappush(heap, value)

    for i in range(len(heap)) :
        answer += heap[i]**2
    return answer