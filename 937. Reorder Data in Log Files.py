# 字符串的处理与重载
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig = []
        let = []
        d = collections.defaultdict(list)
        for i in range(len(logs)):
            if logs[i].split()[1].isdigit():
                dig.append(logs[i])
            else:
                let.append(logs[i])
        let.sort(key = lambda x: x.split()[0])   
        let.sort(key = lambda x: x.split()[1:])   
        return (let + dig)