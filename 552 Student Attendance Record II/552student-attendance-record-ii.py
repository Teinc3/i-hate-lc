class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 1_000_000_000 + 7
        # States to store:
        # Absent 0 days possibilities, absent 1 day possibilities
        # Last day not late, last 2 days not late
        state = {
            "a0l0": 1,
            "a1l0": 0,
            "a0l1": 0,
            "a1l1": 0,
            "a0l2": 0,
            "a1l2": 0
        }

        # State transitions:
        # a0l0 -> a0l0 (P), a0l1 (L), a1l0 (A)
        # a1l0 -> a1l0 (P), a1l1 (L). No further absences allowed
        # a0l1 -> a0l0 (P), a0l2 (L), a1l0 (A)
        # a1l1 -> a1l0 (P), a1l2 (L). No further absences allowed
        # a0l2 -> a0l0 (P), a1l0 (A). No further lates allowed
        # a1l2 -> a1l0 (P). No further lates or absences allowed.
        # Therefore:
        # a0l0 receives from a0l0, a0l1, a0l2
        # a1l0 receives from a0l0, a1l0, a0l1, a1l1, a0l2, a1l2
        # a0l1 receives from a0l0
        # a1l1 receives from a1l0
        # a0l2 receives from a0l1
        # a1l2 receives from a1l1

        for _ in range(n):
            a0l0, a1l0, a0l1, a1l1, a0l2, a1l2 = state.values()
            state = {
                "a0l0": (a0l0 + a0l1 + a0l2) % mod,
                "a1l0": (a0l0 + a1l0 + a0l1 + a1l1 + a0l2 + a1l2) % mod,
                "a0l1": a0l0,
                "a1l1": a1l0,
                "a0l2": a0l1,
                "a1l2": a1l1
            }

        return sum(s % mod for s in state.values()) % mod
