class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # PHASE 1: create one empty adjacency-set slot for every unique character
        # across all words (a character can appear in many words, but only needs one slot)
        adj = {c: set() for w in words for c in w}

         # PHASE 2: compare each pair of ADJACENT words to find ordering rules.
        # find the first position where the two words differ -> that tells us
        # "this character comes before that character" (add it as an edge).
        # if no difference is found and the first word is LONGER than the second,
        # that's an invalid prefix order (longer word can't come before its own prefix).
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            #if w1 is a prefix of w2
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # PHASE 3: post-order DFS with cycle detection.
        # visit[c] = True means "c is currently being explored, still on this path"
        # (not finished yet) -- landing on a True node again means a CYCLE (invalid).
        # once c's successors are all safely explored, mark visit[c] = False
        # (done, safe) and append c to res -- appending happens AFTER exploring
        # neighbors, which is what makes this post-order.
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)

        # PHASE 4: run DFS from every character (in case the graph has
        # multiple disconnected pieces). if any DFS call finds a cycle,
        # the whole ordering is impossible -> return "".
        # otherwise, reverse res (since post-order builds it backwards)
        # and join it into the final alphabet-order string.
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
