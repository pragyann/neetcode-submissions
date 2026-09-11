class TimeMap:

    def __init__(self):
        self.map = {}

        # {
        #   "alice": [["worried", 2], ["sad", 3], ["happy", 4], ["angry", 6]]
        #   target = 5 
        # [['happy', 1]], target 2
        # }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = []
        
        self.map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        data_list = self.map[key]

        l, r = 0, len(data_list) - 1

        res = None

        while l <= r:
            m = (l + r) // 2
            m_val = data_list[m]

            if m_val[1] <= timestamp:
                if not res or m_val[1] > res[1]:
                    res = m_val

                if timestamp ==  m_val[1]:
                    break
                
                l = m + 1

            else:
                r = m - 1

        return res[0] if res else "" 


        
