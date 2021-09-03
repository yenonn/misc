from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.queue1 = deque()
        self.dict1 = {}
        self.lrulist = []

    def put(self, key, value):
        print(f"put operation - {key}")
        if len(self.queue1) < self.cap:
            self.queue1.append(key)
            self.dict1[key] = value
        else:
            removekey = self.queue1.popleft()
            self.queue1.append(key)
            self.dict1[key] = value
        self._update_lru()

    def get(self, key):
        print(f"get operation {key}")
        if key in self.dict1.keys():
            self.queue1.append(key)
            self.queue1.popleft()
        self._update_lru()

    def _update_lru(self):
        self.lrulist = [(k, self.dict1.get(k)) for k in list(self.queue1)]
        self.print()

    def print(self):
        print(self.lrulist)

    def items(self):
        return self.lrulist


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put("key1", 1)
    lru.put("key2", 2)
    lru.put("key3", 3)
    lru.get("key1")
    lru.put("key4", 4)
    lru.put("key5", 5)
    lru.get("key4")
    lru.put("key6", 6)
    lru.put("key7", 7)
    lru.get("key7")
    lru.put("key8", 8)
    lru.put("key9", 9)
    for l in lru.items():
        print(f" --> {l}")
