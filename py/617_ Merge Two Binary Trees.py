class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        tr = []
        minlabel = min(len(t1), len(t2))
        for i in range(1, 10):
            if 2**(i-1)-1 > minlabel:
                break
            for j in range(2**(i-1)-1, min(2**i-1, minlabel)):
                if t1[j] == 'null' and t2[j] == 'null':
                    tr.append('null')
                elif t1[j] == 'null':
                    tr.append(t2[j])
                elif t2[j] == 'null':
                    tr.append(t1[j])
                else:
                    tr.append(t1[j]+t2[j])
        if len(t1) > len(t2):
            tr.extend(t1[minlabel:])
        else:
            tr.extend(t2[minlabel:])
        return tr

t = Solution()
print(t.mergeTrees([1,3,2,5], [2,1,3,'null',4,'null',7]))
