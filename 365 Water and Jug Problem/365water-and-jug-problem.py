class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Possible states:
        # 1. jug1 -> jug2
        # - tf = jug2_full - jug2 if jug2_full - jug2 < jug1 else jug1
        # - jug2 = jug2 + tf
        # - jug1 = jug1 - tf
        # 2. jug = jug_full
        # 3. jug = 0

        initial_state = (0, 0)
        states_map = {(0, 0)}

        def searchPossibleStates(state):
            # deconstruct tuple
            jug1, jug2 = state

            # First search if this state solves the problem
            if jug1 + jug2 == target:
                return True

            # No? Then try all possibilities
            for trial in range(6):
                new_jug1, new_jug2 = jug1, jug2

                # Case 1
                if trial == 0: # Tf from jug1 to jug2
                    tf = y - jug2 if y - jug2 < jug1 else jug1
                    new_jug1 = jug1 - tf
                    new_jug2 = jug2 + tf
                if trial == 1: # tf from jug2 to jug1
                    tf = x - jug1 if x - jug1 < jug2 else jug2
                    new_jug1 = jug1 + tf
                    new_jug2 = jug2 - tf
                
                # Case 2
                elif trial == 2:
                    new_jug1 = x
                elif trial == 3:
                    new_jug2 = y

                # Case 3
                elif trial == 4:
                    new_jug1 = 0
                elif trial == 5:
                    new_jug2 = 0
                
                new_state = (new_jug1, new_jug2)
                if new_state not in states_map:
                    states_map.add(new_state)
                    res = searchPossibleStates(new_state)
                    if res == True:
                        return res
                    states_map.remove(new_state)

                else:
                    continue
            
            return False

        return searchPossibleStates(initial_state)
