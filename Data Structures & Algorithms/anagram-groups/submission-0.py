class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        finalList = []
        for i, word in enumerate(strs):
            sortedWord = "".join(sorted(word))
            if sortedWord in hashMap:
                hashMap[sortedWord].append(strs[i])
            else:
                hashMap[sortedWord] = [strs[i]]
        
        for key in hashMap.keys():
            finalList.append(hashMap[key])
        return finalList
            
            
        

            

        