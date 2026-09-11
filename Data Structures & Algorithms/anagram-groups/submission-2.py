
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        character_index_map = self.get_character_index_map()
        grouped_map = {} 

        for string in strs:
            freq_list = [0 for i in range(26)]

            for character in string:
                char_index = character_index_map[character]
                freq_list[char_index] = freq_list[char_index] + 1

            freq_tuple = tuple(freq_list)
            anagrams_list = grouped_map.get(freq_tuple) if grouped_map.get(freq_tuple) != None else []

            anagrams_list.append(string)

            grouped_map[freq_tuple] = anagrams_list

            print(grouped_map)

        return list(grouped_map.values())

    def get_character_index_map(self):
        initial_ascii = 97;
        char_index_map = {}

        for i in range(26):
            character_ascii = initial_ascii + i
            character = chr(character_ascii)
            char_index_map[character] = i

        return char_index_map;


    


            

            



