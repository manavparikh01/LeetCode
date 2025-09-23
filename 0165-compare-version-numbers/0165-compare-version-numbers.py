class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        lv1 = len(v1)
        lv2 = len(v2)
        for i in range(min(lv1, lv2)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            
        print(lv1, lv2)
        if lv1 < lv2:
            for i in range(lv1, lv2):
                if int(v2[i]) > 0:
                    return -1
        if lv1 > lv2:
            for i in range(lv2, lv1):
                if int(v1[i]) > 0:
                    return 1
        
        return 0