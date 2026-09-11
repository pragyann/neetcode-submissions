class TimeMap:

    def __init__(self):
        self.map = {}

        # {
        #   "alice": [["worried", 2], ["sad", 3], ["happy", 4], ["angry", 6]],
        #   target = 5 
        #   "alice": [['happy', 1]], target 2
        # }

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        
        self.map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        data_list = self.map[key]

        l, r = 0, len(data_list) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2
            m_val = data_list[m]

            if m_val[1] <= timestamp: 
                # if the mid val was set in past, 
                # update the res 
                res = m_val[0]

                if timestamp ==  m_val[1]:
                    break
                
                # look on the right side to see if we can find a past data
                # more closer to the target timestamp
                l = m + 1

            else:
                # if we ended up in a future timestamp,
                # look on the left side (go more in past)
                r = m - 1

        return res


        
