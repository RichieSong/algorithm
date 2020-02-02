# coding:utf-8
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        示例:

        输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
        输出:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        """
        map = {}
        ret = []
        for m in strs:
            tmp = ''.join(sorted(m))
            if tmp not in map:
                map[tmp] = [m]
            else:
                map[tmp].append(m)
        for k, v in map.items():
            ret.append(v)
        return ret
    def groupAnagrams1(self, strs):
        """
        模块
        :param strs:
        :return:
        """
        from collections import defaultdict
        dic = defaultdict(list)
        for s in strs:
            dic["".join(sorted(s))].append(s)
        return list(dic.values())

if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
    print(s.groupAnagrams1(strs))
