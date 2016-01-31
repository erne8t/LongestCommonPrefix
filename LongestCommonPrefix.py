class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for item in strs:
            if len(item)>len(prefix): prefix = item

        # every str will be compared to this prefix to find mutual maximum prefix
        for item in strs:
            x = len(item)
            prefix = prefix[:x]
            while prefix!=item[:x]:
                x -= 1
                prefix = prefix[:x]
        return prefix
