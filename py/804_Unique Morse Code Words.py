class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morsewords = []
        for word in words:
            morsestring = ''
            for letter in word:
                morsestring += morse[ord(letter)-97]
            morsewords.append(morsestring)
        new_morsewords = []
        for ele in morsewords:
            if ele not in new_morsewords:
                new_morsewords.append(ele)
        return len(new_morsewords)

    print(uniqueMorseRepresentations(['a']))