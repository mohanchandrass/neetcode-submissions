class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string+=str(len(word))
            encoded_string+='#'
            encoded_string+=word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i<len(s):
            length = ''
            while s[i]!='#':
                length+=s[i]
                i+=1
            i+=1
            strs =''
            end = i+int(length)
            while i!=end:
                strs+=s[i]
                i+=1
            decoded_strs.append(strs)


            
        return decoded_strs