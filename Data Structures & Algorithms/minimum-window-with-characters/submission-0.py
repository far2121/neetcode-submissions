class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = start = 0
        missing = len(t)
        ans = ""

        for right in range(len(s)):
            c = s[right]
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            else:
                need[c] = -1

            while missing == 0:
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return ans