from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        parent = list(range(len(source)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: build connected components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 2: group indices by root
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 3: calculate mismatch
        res = 0
        for indices in groups.values():
            count = Counter()
            
            for i in indices:
                count[source[i]] += 1
                count[target[i]] -= 1
            
            # unmatched values
            res += sum(v for v in count.values() if v > 0)

        return res
        