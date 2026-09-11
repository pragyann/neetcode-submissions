class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.get_freq_map_of_string(s)
        t_map = self.get_freq_map_of_string(t)

        if len(s_map) != len(t_map):
            return False

        for s_key in s_map.keys():
            t_val = t_map.get(s_key)

            if not t_val:
                return False;

            if t_val != s_map.get(s_key):
                return False;

        return True;

    def get_freq_map_of_string(self, string: str):
        freq_map = {}

        for character in string:
            character_freq = freq_map.get(character) if freq_map.get(character) else 0
            freq_map[character] = character_freq + 1

        return freq_map

            