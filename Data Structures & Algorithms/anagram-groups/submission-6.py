class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list) # tuple([has_table]): [strs]

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            freq_map[tuple(count)].append(s)
        
        return list(freq_map.values())
        