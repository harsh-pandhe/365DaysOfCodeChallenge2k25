from collections import deque


def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i + 1 :]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, steps + 1))

    return 0


begin = "hit"
end = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = word_ladder(begin, end, wordList)
print("Shortest transformation length:", result)
