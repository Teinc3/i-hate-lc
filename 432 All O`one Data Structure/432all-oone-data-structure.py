class KeyNode:
    def __init__(self, key: int, freq: int):
        self.key = key
        self.freq = freq
        self.lkey = self.rkey = None

class FreqNode:
    def __init__(self, freq: int):
        self.freq = freq
        self.lfreq = self.rfreq = None
        self.khead = self.ktail = dummy = KeyNode("", freq)
        dummy.lkey = dummy.rkey = dummy

class AllOne:
    def __init__(self):
        self.keys = {}
        self.freqs = {}
        self.fhead = self.ftail = dummy = FreqNode(-1)
        dummy.lfreq = dummy.rfreq = dummy

    def inc(self, key: str) -> None:
        old_freq = None
        if key not in self.keys:
            node = self.keys[key] = KeyNode(key, 1)
        else:
            node = self.keys[key]
            old_freq = node.freq
            node.freq += 1
        
        self._update_freq(node, old_freq)

    def dec(self, key: str) -> None:
        old_freq = None
        if key not in self.keys:
            return
        else:
            node = self.keys[key]
            old_freq = node.freq
            node.freq -= 1
        
        self._update_freq(node, old_freq)
    
    def _update_freq(self, node: KeyNode, old_freq: int | None):
        # 1. sever the node from its old frequency node
        old_f_node = None
        wiped_old_f_node = False
        if old_freq:
            old_f_node = self.freqs[old_freq]
            if node.lkey is node.rkey: # only key in this freqnode
                # Wipe the freqnode reference from the freq DLL
                old_f_node.lfreq.rfreq = old_f_node.rfreq
                old_f_node.rfreq.lfreq = old_f_node.lfreq
                self.freqs.pop(old_freq)
                wiped_old_f_node = True
            else: # Simply detatch our keynode from the existing freqnode
                node.lkey.rkey = node.rkey
                node.rkey.lkey = node.lkey
        
        new_f_node = None
        if old_f_node: # N -> N+1 / N-1
            if node.freq == 0: # 1 -> 0
                self.keys.pop(node.key)
            elif old_f_node.rfreq.freq == node.freq: # existing N+1 fnode
                new_f_node = old_f_node.rfreq
            elif old_f_node.lfreq.freq == node.freq: # existing N-1 fnode
                new_f_node = old_f_node.lfreq
            else: # The N+1/N-1 node doesn't exist
                inc = not old_freq or node.freq > old_freq
                # Create a new f node, and insert it in between.
                new_f_node = FreqNode(node.freq)
                if inc: # N+1
                    if wiped_old_f_node:
                        new_f_node.lfreq = old_f_node.lfreq
                        new_f_node.rfreq = old_f_node.rfreq
                        old_f_node.lfreq.rfreq = new_f_node
                        old_f_node.rfreq.lfreq = new_f_node
                    else:
                        new_f_node.lfreq = old_f_node
                        new_f_node.rfreq = old_f_node.rfreq
                        old_f_node.rfreq.lfreq = new_f_node
                        old_f_node.rfreq = new_f_node
                else: # N-1
                    if wiped_old_f_node:
                        new_f_node.lfreq = old_f_node.lfreq
                        new_f_node.rfreq = old_f_node.rfreq
                        old_f_node.lfreq.rfreq = new_f_node
                        old_f_node.rfreq.lfreq = new_f_node
                    else:
                        new_f_node.rfreq = old_f_node
                        new_f_node.lfreq = old_f_node.lfreq
                        old_f_node.lfreq.rfreq = new_f_node
                        old_f_node.lfreq = new_f_node
        else:
            # 0 -> 1
            if self.fhead.rfreq.freq == node.freq:
                new_f_node = self.fhead.rfreq
            else:
                # Create the new freq node for 1 and insert right next to head.
                new_f_node = FreqNode(node.freq)
                new_f_node.lfreq = self.fhead
                new_f_node.rfreq = self.fhead.rfreq
                self.fhead.rfreq = new_f_node.rfreq.lfreq = new_f_node

        # And finally insert the node into the new freq node.
        if new_f_node:
            node.lkey = new_f_node.ktail.lkey
            node.rkey = new_f_node.ktail
            node.lkey.rkey = node.rkey.lkey = node

            if node.freq not in self.freqs:
                self.freqs[node.freq] = new_f_node

    def getMaxKey(self) -> str:
        if self.fhead.rfreq is self.ftail:
            return ""
        return self.ftail.lfreq.ktail.lkey.key

    def getMinKey(self) -> str:
        if self.fhead.rfreq is self.ftail:
            return ""
        return self.fhead.rfreq.ktail.lkey.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()