from ..queues import get_remaining_queues, print_queue_status
from rate_limiter.rate_limit_helper_abc import IRateLimitHelper


class RateLimitHelper(IRateLimitHelper):
    def helper(self, limiter, client_id, message_type):
        if limiter.can_send(client_id, message_type):
            limiter.add_request(client_id, message_type)
            print(f"Sent message for Client {client_id} - {message_type}")
        else:
            remaining_queues = get_remaining_queues(client_id, message_type)
            rate_limit_used = False
            for queue in remaining_queues:
                if limiter.can_send(client_id, queue):
                    print(
                        f"Using rate limit from {queue} for Client {client_id} - {message_type}"
                    )
                    limiter.add_request(client_id, queue)
                    rate_limit_used = True
                    break
            if not rate_limit_used:
                print(f"Rate limit reached for Client {client_id} - {message_type}")

        print_queue_status(limiter, client_id)
