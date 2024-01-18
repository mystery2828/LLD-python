import time

class RateLimiter:
    def __init__(self, requests_per_second):
        self.requests_per_second = requests_per_second
        self.interval = 1 / requests_per_second
        self.last_request_time = 0

    def allow_request(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_request_time

        if elapsed_time >= self.interval:
            self.last_request_time = current_time
            return True
        else:
            return False

class APIHandler:
    def __init__(self):
        self.rate_limiter = RateLimiter(requests_per_second=5)

    def process_request(self):
        if self.rate_limiter.allow_request():
            print("Request processed successfully.")
        else:
            print("Request rate limit exceeded. Please try again later.")

# Example Usage
api_handler = APIHandler()

# Simulate processing requests
for _ in range(10):
    time.sleep(0.15)
    api_handler.process_request()
