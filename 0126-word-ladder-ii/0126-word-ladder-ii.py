from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        # Helper function to perform depth-first search to find paths
        def dfs(path: List[str], current_word: str):
            if current_word == begin_word:
                # Reverse the path since we are moving from endWord to beginWord
                ans.append(path[::-1])
                return
            # Iterate over all predecessors and continue building the path
            for precursor_word in predecessors[current_word]:
                path.append(precursor_word)
                dfs(path, precursor_word)  # Recursive DFS call
                path.pop()  # Remove the last word to backtrack

        ans = []  # List to store all the shortest transformation sequences
        words = set(word_list)  # Convert the word list to a set for O(1) look-ups
      
        # Early exit if end word is not in the word list
        if end_word not in words:
            return ans
      
        words.discard(begin_word)  # Remove the begin word from the set of words
        distance_from_begin = {begin_word: 0}  # Dictionary to store distance of words from beginWord
        predecessors = defaultdict(set)  # Dictionary to store predecessors of each word
      
        # Initialize queue for BFS
        queue = deque([begin_word])
        found = False
        step = 0  # Number of steps taken

        # Perform BFS until the queue is empty or the end word is found
        while queue and not found:
            step += 1
            for _ in range(len(queue)):
                current_word = queue.popleft()
                word_chars = list(current_word)

                # Try changing each character in the current word
                for char_index in range(len(word_chars)):
                    original_char = word_chars[char_index]

                    # Try all possible transformations by changing the character to 'a' to 'z'
                    for letter in range(26):
                        word_chars[char_index] = chr(ord('a') + letter)
                        new_word = ''.join(word_chars)

                        # Skip words that are not one step away
                        if distance_from_begin.get(new_word, 0) == step:
                            predecessors[new_word].add(current_word)

                        # If the new word is in the words set, it is a valid transformation
                        if new_word in words:
                            # Add the current word as a predecessor of the new word
                            predecessors[new_word].add(current_word)
                            words.discard(new_word)  # Mark the new word as visited
                            queue.append(new_word)  # Add the new word to the queue

                            # Set the distance for the new word
                            distance_from_begin[new_word] = step

                            # If the end word is reached, mark that we found a transformation
                            if end_word == new_word:
                                found = True
                    # Restore the original character at the index
                    word_chars[char_index] = original_char

        # If a transformation was found, reconstruct paths using DFS
        if found:
            dfs([end_word], end_word)  # Initial call to dfs to start path reconstruction

        return ans  # Return the list of all shortest transformation sequences