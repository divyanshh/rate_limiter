import time
import random
from rate_limiter.rate_limiter import RateLimiter
from rate_limiter.rate_limiter_abc import IRateLimiter
from client_rates import client_rates
from app.rate_limiter.rate_limit_helper import RateLimitHelper
from app.rate_limiter.rate_limit_helper_abc import IRateLimitHelper


def simulate(limiter: IRateLimiter, rate_limit_helper: IRateLimitHelper):
    end_time = time.time() + 300  # Simulate for 5 minutes
    while time.time() < end_time:
        client_id = random.choice(list(client_rates.keys()))
        message_type = random.choice(["Non sessional", "Sessional receive", "Sessional send"])
        rate_limit_helper.helper(limiter, client_id, message_type)
        time.sleep(0)  # Simulate a fraction of a second


if __name__ == "__main__":
    # Switchable algos, if we want to switch our rate limiting algo, we just need to make a swith here
    limiter = RateLimiter(client_rates)
    rate_limit_helper = RateLimitHelper()
    simulate(limiter, rate_limit_helper)
