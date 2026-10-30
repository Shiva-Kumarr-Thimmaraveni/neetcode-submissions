class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+ "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        f = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            lengthOfWord = int(s[i:j])
            word = s[j+1:j+1+lengthOfWord]
            f.append(word)
            i = j+1+lengthOfWord
            
        return f


        
        

                

                
                

        
                


            


        
        

    
        


