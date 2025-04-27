# runtime: O(n x log(n))
# space: O(n)

from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:        
        ret = 0
        
        x_map = defaultdict(list)
        for b in buildings:
            cur_x = b[0]
            cur_y = b[1]
            x_map[cur_x].append(cur_y)
            
        y_map = defaultdict(list)
        for b in buildings:
            cur_x = b[0]
            cur_y = b[1]
            y_map[cur_y].append(cur_x)

        for x in x_map:
            tmp = sorted(x_map[x])
            s = {}
            for i, y in enumerate(tmp):
                s[y] = i
            x_map[x] = s
        for y in y_map:
            tmp = sorted(y_map[y])
            s = {}
            for i, x in enumerate(tmp):
                s[x] = i            
            y_map[y] = s
        
        for b in buildings:
            cur_x = b[0]
            cur_y = b[1]

            l = x_map[cur_x]
            ind = l[cur_y]
            if ind == 0 or ind == len(l)-1:
                continue

            l = y_map[cur_y]
            ind = l[cur_x]
            if ind == 0 or ind == len(l)-1:
                continue
            
            ret += 1            
                            
        return ret


# the following solution takes too long
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        ret = 0
        for i, b1 in enumerate(buildings):
            up_direction = False
            down_direction = False
            left_direction = False
            right_direction = False
            
            for j, b2 in enumerate(buildings):
                if i == j:
                    continue

                delta_x = b1[0] - b2[0]
                delta_y = b1[1] - b2[1]
                
                if delta_x > 0 and delta_y == 0:
                    right_direction = True
                elif delta_x < 0 and delta_y == 0:
                    left_direction = True
                elif delta_x == 0 and delta_y > 0:
                    up_direction = True
                elif delta_x == 0 and delta_y < 0:
                    down_direction = True
                
                if up_direction and down_direction and left_direction and right_direction:
                    ret += 1
                    break

        return ret

