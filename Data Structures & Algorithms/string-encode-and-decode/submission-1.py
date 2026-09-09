
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        delimitor = "@" #will help to tell whetre the string starts

        for word in strs:
            length = len(word)
            encoded_string += str(length) + delimitor + word
        return encoded_string    

        # ["cat", "helloworld"]
        #encoder() -> 3@cat10@helloworld

    def decode(self, s: str) -> List[str]:
        delimitor = "@" 
        decoded_list = []
        
        idx = 0

        while(idx < len(s)):
            del_idx = idx

            #del idx shoudl look out for delimitor 
            while(s[del_idx] != delimitor):
                del_idx += 1
            
            word_len = int(s[idx:del_idx])
            idx = del_idx + 1
            word = s[idx:idx + word_len]
            decoded_list.append(word)
            idx = idx + word_len
        return decoded_list    





                


