from abc import ABC


class IRateLimitHelper(ABC):
    def helper(self, limiter, client_id, message_type):
        pass
