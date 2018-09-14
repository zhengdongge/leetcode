class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans = {}
        reans = []
        for domain in cpdomains:
            times, url = domain.split(' ')
            urls = url.split('.')
            for i in range(len(urls)):
                if '.'.join(urls[i:]) not in ans:
                    ans['.'.join(urls[i:])] = int(times)
                else:
                    ans['.'.join(urls[i:])] += int(times)

        for u, t in ans.items():
            reans.append(str(t) + ' ' + u)
        return reans

t = Solution()
print(t.subdomainVisits(["9001 discuss.leetcode.com"]))
