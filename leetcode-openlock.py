def openLock(self, deadends: List[str], target: str) -> int:
        # BFS
        queue = ['0000']
        visited = set()
        visited.add('0000')
        deadset = set(deadends)
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur in deadset:
                    continue             # 如果cur是死亡数字，则不选这条路径
                if cur == target:
                    return step          # 如果cur = target，则找到目标，返回step
                # 将当前cur元素的所有邻近元素加入队列和visited
                for i in range(4):
                    up = self.up(cur, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.down(cur, i)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            step += 1
        return -1

def up(self, s:str, i:int) -> str:
    """将字符串s的第i个元素向上拨动一位，并返回拨动后的字符串"""
    s_list = list(s)
    if s_list[i] == '9':
        s_list[i] = '0'
    else:
        s_list[i] = str(int(s_list[i])+1)
    return "".join(s_list)

def down(self, s:str, i:int) -> str:
    """将字符串s的第i个元素向下拨动一位，并返回拨动后的字符串"""
    s_list = list(s)
    if s_list[i] == '0':
        s_list[i] = '9'
    else:
        s_list[i] = str(int(s_list[i])-1)
    return "".join(s_list)


import queue as Queue
class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:

        # minmum trials
        depth = 0
        visited = set() # store all processed strings, to avoid duplicates

        dead_set = set(deadends)

        # BFS
        queue = Queue.Queue() # store all needed process strings
        # init by putting the first strings
        queue.put('0000')
        visited.add('0000')

        # loop queue
        while not queue.empty():
            
            cur_depth_len = queue.qsize()
            print(f'cur_depth_len is {cur_depth_len}')
            for cur_try_idx in range(cur_depth_len):
                cur_val = queue.get()
               
                # if match the deadend, means no need to try next steps!!!
                if cur_val in dead_set:
                    continue

                # if matched, return current trials
                if cur_val == target:
                    return depth

                # expandation
                for i in range(0, 4):
                    # try one time rotate up
                    up = self._plus_one(cur_val, i)
                    # try one time rotate down
                    down = self._minus_one(cur_val, i)

                    if not up in visited:
                        visited.add(up)
                        queue.put(up)
                    
                    if not down in visited:
                        visited.add(down)
                        queue.put(down)
            else:
                # increase steps
                depth+=1

        # not matched at all
        return -1

    # func for Plus+
    # def _plus_one(self, cur_str: str, index: int) -> str:
        
    #     list_int = list(map(lambda x: int(x), list(cur_str)))

    #     if list_int[index] == 9:
    #         list_int[index] = 0
    #     else:
    #         list_int[index]+=1
        
    #     return ''.join([str(i) for i in list_int])

    def _plus_one(self, cur_str: str, index: int) -> str:
        list_str = list(cur_str)
        if list_str[index] == '9':
            list_str[index] = '0'
        else:
            list_str[index] = str(int(list_str[index]) + 1)
        return ''.join(list_str)

    # func for Minus-
    def _minus_one(self, cur_str: str, index: int) -> str:
        list_str = list(cur_str)
        if list_str[index] == '0':
            list_str[index] = '9'
        else:
            idx_int = int(list_str[index])
            idx_int += 1
            list_str[index] = str(idx_int)
        
        return ''.join(list_str)