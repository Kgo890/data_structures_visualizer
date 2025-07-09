from backend.schemas.hash_map_schema import KeyValuePair


class HashMap:
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for character in key:
            sum += ord(character)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False

        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            index = (index + 1) % len(self.hashmap)
            if not first_iteration and index == original_index:
                first_iteration = False
        raise Exception("sorry, key not found")

    def delete(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                self.hashmap[index] = None
                return
            index = (index + 1) % len(self.hashmap)
            if not first_iteration and index == original_index:
                break
            first_iteration = False

        raise Exception("Key not found")

    def items(self):
        result = []
        for item in self.hashmap:
            if item is None:
                result.append(None)
            else:
                result.append(KeyValuePair(key=item[0], value=item[1]))
        return result

    def reset(self):
        self.hashmap = [None for _ in range(len(self.hashmap))]
