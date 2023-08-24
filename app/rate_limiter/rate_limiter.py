import time
from collections import defaultdict
from rate_limiter.rate_limiter_abc import IRateLimiter


class RateLimiter(IRateLimiter):
    def __init__(self, limits):
        self.limits = limits
        self.clients = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    def can_send(self, client_id, message_type):
        current_second = int(time.time())
        total_requests = sum(
            self.clients[client_id][message_type][timestamp]
            for timestamp in range(current_second - 1, current_second + 1)
        )
        limit = self.limits[client_id][message_type]
        return total_requests < limit

    def add_request(self, client_id, message_type):
        current_second = int(time.time())
        self.clients[client_id][message_type][current_second] += 1
