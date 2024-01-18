from time import time,sleep

class APIRateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.count = 0
        self.last_refill_time = time()

    def refill(self):
        self.curr_time = time()
        time_elapsed = self.curr_time - self.last_refill_time
        tokens_to_add = time_elapsed*self.refill_rate
        if tokens_to_add>0:
            self.count = min(self.capacity, self.count+tokens_to_add)
            self.last_refill_time = self.curr_time

    def allow_req(self):
        self.refill()
        if self.count < self.capacity:
            self.count+=1
            return True
        return False

        

class APIHandler:
    def __init__(self):
        self.rate_limiter = APIRateLimiter(capacity=5, refill_rate=2)
    
    def process_request(self):
        if self.rate_limiter.allow_req():
            print("YES")
        else:
            print("Failed")

A = APIHandler()
for i in range(20):
    A.process_request()
    sleep(0.25)