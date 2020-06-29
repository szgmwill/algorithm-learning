class Tier(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startWith(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True 

if __name__ == "__main__":
    tier = Tier()
    tier.insert('apple')
    search = tier.search('ape')
    startWith = tier.startWith('app')
    print('=======================search:', search)
    print('=======================startWith:', startWith)
