import re

class Codec:
    def encode(self, strs):
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        return re.findall(r'\d+#(.+?)(?=\d+#|$)', s)
        
codec = Codec()
print(codec.decode(codec.encode(['hello','dad'])))