class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1 
        
        import heapq
        maxHeap = []
        
        for key,value in hashMap.items():
            heapq.heappush(maxHeap,(-value,key))

        finalList = []

        for _ in range(k):
            item = heapq.heappop(maxHeap)[1]
            finalList.append(item)
        return finalList





       

        
       

        