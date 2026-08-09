class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            current_node = trie
            for char in word:
                current_node = current_node.setdefault(char, {})
            current_node['end'] = word

        m, n = len(board), len(board[0])
        res = []
        
        def search(i, j, node):
            char = board[j][i]
            if char not in node:
                return
            node = node[char]
            if 'end' in node:
                res.append(node.pop('end'))

            board[j][i] = "-"

            for x_o, y_o in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = x_o + i, y_o + j
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                search(x, y, node)

            board[j][i] = char
            # Wipe this node, if the children nodes are wiped
            for key in list(node.keys()):
                if not node[key]:
                    node.pop(key)

        for j, row in enumerate(board):
            for i in range(len(row)): 
                search(i, j, trie)

        return res
