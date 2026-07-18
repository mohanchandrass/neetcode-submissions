class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False
        

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            
            node = node.children[ch]
        
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self

        def dfs(i,node):
            if i == len(word):
                return node.end
            if word[i] == ".":
                for child in node.children:
                    if dfs(i+1,node.children[child]):
                        return True
                return False
                    
                    
            if word[i] not in node.children:
                return False
           
            return dfs(i+1,node.children[word[i]])

        result = dfs(0,node)
        return result

