from time import time, sleep

class LeakyBucketRateLimiter:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.tokens = 0
        self.leak_rate = leak_rate
        self.last_leak_time = time()

    def leak_tokens(self):
        current_time = time()
        time_elapsed = current_time - self.last_leak_time
        tokens_to_leak = time_elapsed * self.leak_rate

        if tokens_to_leak > 1:
            self.tokens = max(0, self.tokens - tokens_to_leak)
            self.last_leak_time = current_time

    def allow_request(self):
        self.leak_tokens()

        if self.tokens < self.capacity:
            self.tokens += 1
            return True
        else:
            return False

class APIHandler:
    def __init__(self):
        self.rate_limiter = LeakyBucketRateLimiter(capacity=5, leak_rate=1)

    def process_request(self):
        if self.rate_limiter.allow_request():
            print("Request processed successfully.")
        else:
            print("Request rate limit exceeded. Please try again later.")
            # Simulate a delay or handle the request in some way
            # sleep(1)

# Example Usage
api_handler = APIHandler()

# Simulate processing requests
for _ in range(10):
    sleep(0.1)
    api_handler.process_request()
