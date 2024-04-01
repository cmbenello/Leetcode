class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        
        current_dict = self.trie
        _end = 0
        for letter in word:
            if letter not in current_dict:
                current_dict[letter] = {}
            current_dict = current_dict[letter]
        
        current_dict[_end] = _end
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot             character '.' to represent any letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch == '.':
                        for x in node:
                            if x != 0 and search_in_node(word[i + 1:], node[x]):
                                return True

                    # If no nodes lead to answer
                    # or the current character != '.'
                    return False

                # If the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return 0 in node

        return search_in_node(word, self.trie)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)