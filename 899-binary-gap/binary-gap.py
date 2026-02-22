class Solution:
    def binaryGap(self, n: int) -> int:
        # Convert n to binary string and remove '0b' prefix
        binary = bin(n)[2:]
        
        max_gap = 0
        last_position = -1
        
        for i, digit in enumerate(binary):
            if digit == '1':
                if last_position != -1:
                    # Calculate distance from the previous '1'
                    max_gap = max(max_gap, i - last_position)
                # Update the position of the most recent '1'
                last_position = i
                
        return max_gap