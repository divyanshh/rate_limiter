from abc import ABC


class IRateLimiter(ABC):
    def can_send(self, client_id, message_type):
        pass

    def add_request(self, client_id, message_type):
        pass
