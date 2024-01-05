from time import time
import time as ti

class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill_time = time()

    def refill(self):
        current_time = time()
        time_elapsed = current_time - self.last_refill_time
        tokens_to_add = time_elapsed * self.refill_rate

        if tokens_to_add > 1:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_time = current_time
 
    def allow_request(self):
        self.refill()

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

class APIHandler:
    def __init__(self):
        self.rate_limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1)

    def process_request(self):
        if self.rate_limiter.allow_request():
            print("Request processed successfully.")
        else:
            print("Request rate limit exceeded. Please try again later.")

# Example Usage
api_handler = APIHandler()

# Simulate processing requests
for _ in range(10):
    ti.sleep(0)
    api_handler.process_request()
