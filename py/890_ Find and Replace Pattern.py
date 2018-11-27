class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        match = []
        for word in words:
            m1 = {}
            m2 = {}
            matchstatus = 1;
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                else:
                    if m1[w] != p:
                        matchstatus = 0;
                        exit
                if p not in m2:
                    m2[p] = w
                else:
                    if m2[p] != w:
                        matchstatus = 0;
                        exit
            if matchstatus == 1:
                match.append(word)
        return match


t = Solution()
print (t.findAndReplacePattern(["abc","ldd","axx","yus"],"abb"))