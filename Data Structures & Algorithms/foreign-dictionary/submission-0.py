class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        lettersAfter = {}
        for word in words:
            for char in word:
                lettersAfter[char] = set()
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            updated = False
            for j in range(min(len(word1), len(word2))):
                if word2[j] != word1[j]:
                    lettersAfter[word1[j]].add(word2[j])
                    updated = True
                    break
            if updated == False and len(word1) > len(word2):
                return ""
        
        valueCount = {}
        for key in lettersAfter:
            valueCount[key] = 0
        for key in lettersAfter:
            for letter in lettersAfter[key]:
                valueCount[letter] += 1
        starting = set()
        for letter in valueCount:
            if valueCount[letter] == 0:
                starting.add(letter)
        output = ""
        while starting:
            nextLetter = starting.pop()
            output = output + nextLetter
            for letter in lettersAfter[nextLetter]:
                valueCount[letter] -= 1
                if valueCount[letter] == 0:
                    starting.add(letter)
        return output if len(output) == len(lettersAfter) else ""

