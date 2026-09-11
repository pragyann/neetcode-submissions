class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            char_arr = [0] * 26

            for c in s:
                char_arr[ord('a') - ord(c)] += 1
            
            anagram_map[tuple(char_arr)].append(s)
        
        return list(anagram_map.values())