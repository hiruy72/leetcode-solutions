from collections import deque

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        max_val = max(nums)
        
        # 1. Fast Sieve to identify primes
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
        
        # 2. Map primes to indices of their multiples
        # prime_to_indices[p] = [list of indices j where nums[j] % p == 0]
        prime_to_indices = {}
        
        # Pre-calculating multiples for all numbers in nums
        # Optimization: Only care about primes that actually appear in nums
        # or are factors of numbers in nums.
        for i, val in enumerate(nums):
            # Find all prime factors of val to populate the map
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    if is_prime[d]:
                        if d not in prime_to_indices: prime_to_indices[d] = []
                        prime_to_indices[d].append(i)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                if is_prime[temp]:
                    if temp not in prime_to_indices: prime_to_indices[temp] = []
                    prime_to_indices[temp].append(i)

        # 3. BFS
        queue = deque([(0, 0)]) # (current_index, distance)
        visited_indices = {0}
        visited_primes = set()
        
        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # --- Adjacent Steps ---
            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            # --- Prime Teleportation ---
            val = nums[curr_idx]
            if is_prime[val] and val not in visited_primes:
                visited_primes.add(val)
                if val in prime_to_indices:
                    for target_idx in prime_to_indices[val]:
                        if target_idx not in visited_indices:
                            visited_indices.add(target_idx)
                            queue.append((target_idx, dist + 1))
                            
        return -1