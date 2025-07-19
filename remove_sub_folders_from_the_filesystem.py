from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tries = {}
        ret = []
        folder.sort()
        for i, path in enumerate(folder): 
            dirs = path.split("/")[1:]
            tmp = tries
            unique = True if i == 0 else False
            for dir in dirs: 
                if dir not in tmp: 
                    if len(tmp) > 0:
                        unique = True
                    if unique:
                        tmp[dir] = {}
                    else: 
                        break
                tmp = tmp[dir]
            if unique: 
                ret.append(path)
        return ret
    
if __name__ == "__main__": 
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    # folder = ["/a","/a/b/c","/a/b/d"]
    folder = ["/a/b/c","/a/b/d","/a"]
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    ret = Solution().removeSubfolders(folder)
    print(ret)