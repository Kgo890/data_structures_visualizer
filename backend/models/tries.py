class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i: j + 1])
        return matches

    def advanced_find_matches(self, document, variations):
        continuous_substrings = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in level:
                    level = level[ch]

                elif ch in variations and variations[ch] in level:
                    level = level[variations[ch]]
                else:
                    break

                if self.end_symbol in level:
                    continuous_substrings.add(document[i:j + 1])

        return continuous_substrings

    def delete(self, word):
        def _delete(current, word, index):
            if index == len(word):
                if self.end_symbol not in current:
                    return False  # word doesn't exist
                del current[self.end_symbol]
                return len(current) == 0  # delete this node if it's now empty

            char = word[index]
            if char not in current:
                return False  # word doesn't exist

            should_delete_child = _delete(current[char], word, index + 1)

            if should_delete_child:
                del current[char]
                return len(current) == 0 and self.end_symbol not in current

            return False

        _delete(self.root, word, 0)

    def items(self):
        results = []

        def dfs(node, path):
            for char, child in node.items():
                if char == self.end_symbol:
                    results.append("".join(path))
                else:
                    dfs(child, path + [char])

        dfs(self.root, [])
        return results

    def search(self, word):
        current = self.root
        for character in word:
            if character in current:
                current = current[character]
            else:
                return False
        if self.end_symbol in current:
            return True
        else:
            return False

    def prefix_search(self,prefix):
        current_level = self.root
        for character in prefix:
            if character in current_level:
                current_level = current_level[character]
            else:
                return False
        return True

    def reset(self):
        self.root = {}
