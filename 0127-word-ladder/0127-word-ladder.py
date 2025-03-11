class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is not in wordList, return 0
        if endWord not in wordList:
            return 0

        # Initialize defaultdict to store neighbors of each word pattern
        nei = collections.defaultdict(list)
        # Append beginWord to wordList
        wordList.append(beginWord)
        # Generate patterns and store neighbors
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        # Initialize set to store visited words and queue for BFS traversal
        visit = set([beginWord])
        q = deque([beginWord])
        # Initialize result to track transformation length
        res = 1
        
        # Perform BFS
        while q:
            # Iterate through words at the current level
            for i in range(len(q)):
                word = q.popleft()
                # If word is equal to endWord, return result
                if word == endWord:
                    return res
                # Generate patterns and explore neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            # Increment result for next level
            res += 1
        # If endWord not found, return 0
        return 0