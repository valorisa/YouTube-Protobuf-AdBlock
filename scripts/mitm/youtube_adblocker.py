import re
from mitmproxy import http

class YouTubeAdBlocker:
    def __init__(self):
        self.ad_patterns = [
            re.compile(b'/pagead/'),
            re.compile(b'\xBD\xF8\xE8\xF7\x02', re.DOTALL)  # Signature Protobuf
        ]
    
    def response(self, flow: http.HTTPFlow):
        if any(pattern.search(flow.response.content) for pattern in self.ad_patterns):
            self._modify_protobuf(flow.response.content)
    
    def _modify_protobuf(self, content: bytes) -> bytes:
        modified = bytearray(content)
        index = modified.find(b'\xBD\xF8\xE8\xF7\x02')
        if index != -1:
            modified[index+4] = 0x02  # Modification du field ID
        return bytes(modified)

addons = [YouTubeAdBlocker()]
