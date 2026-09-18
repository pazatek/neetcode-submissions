class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '-' + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '-':
                j += 1
            length = int(s[i:j])
            decodedStrings.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decodedStrings 
