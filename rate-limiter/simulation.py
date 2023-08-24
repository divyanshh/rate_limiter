import time
import random
from rate_limiter import RateLimiter
from client_rates import client_rates
from queues import get_remaining_queues, print_queue_status

limiter = RateLimiter(client_rates)

def simulate():
    end_time = time.time() + 300  # Simulate for 5 minutes
    while time.time() < end_time:
        client_id = random.choice(list(client_rates.keys()))
        message_type = random.choice(["Non sessional", "Sessional receive", "Sessional send"])

        if limiter.can_send(client_id, message_type):
            limiter.add_request(client_id, message_type)
            print(f"Sent message for Client {client_id} - {message_type}")
        else:
            remaining_queues = get_remaining_queues(client_id, message_type)
            rate_limit_used = False
            for queue in remaining_queues:
                if limiter.can_send(client_id, queue):
                    print(f"Using rate limit from {queue} for Client {client_id} - {message_type}")
                    limiter.add_request(client_id, queue)
                    rate_limit_used = True
                    break
            if not rate_limit_used:
                print(f"Rate limit reached for Client {client_id} - {message_type}")

        print_queue_status(limiter, client_id)
        time.sleep(0)  # Simulate a fraction of a second


if __name__ == "__main__":
    simulate()
