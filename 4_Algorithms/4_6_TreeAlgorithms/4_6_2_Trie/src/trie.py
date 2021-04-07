class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.count_leaf = 0
 
 
class Trie:
    def __init__(self):
        self.head = Node(None)
        self.word_count = 0
 
    def insert(self, word):
        curr = self.head
 
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.count_leaf += 1
 
        curr.child['*'] = True
        self.word_count += 1
 
    def count_match(self, word):
        curr = self.head
        match_fail = False
 
        for c in word:
            if c != '?':
                if c not in curr.child:
                    match_fail = True
                    break
                curr = curr.child[c]
            else:
                return curr.count_leaf  # Case1: 와일드카드 매치
 
            if match_fail is True:
                return 0                # Case2: 단어 매치가 없음
 
        return 1                        # Case3: 단어 매치
 
 
def solution(words, queries):
    tries = dict()
    inv_tries = dict()
 
    for word in words:
        word_len = len(word)
 
        if word_len not in tries:
            tries[word_len] = Trie()
            inv_tries[word_len] = Trie()
 
        tries[word_len].insert(word)
        inv_tries[word_len].insert(word[::-1])
 
    answer = list()
    for query in queries:
        query_len = len(query)
        if query_len not in tries:
            answer.append(0)                                             # Case1: 해당 길이의 단어가 없음
        elif query.count('?') == query_len:
            answer.append(tries[query_len].word_count)                   # Case2: 전체 와일드카드
        elif query[0] == '?':
            answer.append(inv_tries[query_len].count_match(query[::-1])) # Case3: 전위 와일드카드
        else:
            answer.append(tries[query_len].count_match(query))           # Case4: 후위 와일드카드 or 단어 매칭
 
    return answer

 
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))