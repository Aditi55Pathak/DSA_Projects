# Elevator system based on priority queue

import heapq
import time


#  First create the request class here
class RequestHere:
    def __init__(self, floornumber, timestamp):
        self.floornumber = floornumber
        self.timestamp = timestamp


#  Create the elevator class here
class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.direction = 1  # Choose 1 for up , -1 for down according to you need
        self.queueRequest = []  # Priority queue for floor request

    def add_request(self, request):
        heapq.heappush(self.queueRequest, (request.floornumber, request))

    def process_requests(self):
        while self.queueRequest:
            _, request = heapq.heappop(self.queueRequest)
            self.move_to_floor(request.floornumber)
            print(f"Elevator {self.id} arrived at floor {request.floornumber}")

    def move_to_floor(self, floor_number):
        while self.current_floor != floor_number:
            self.current_floor += self.direction
            time.sleep(1)  # Simulate movement time
            print(f"Elevator {self.id} moving to floor {self.current_floor}")


def main():
    elevators = [Elevator(1), Elevator(2)]

    # Example: Add some requests to the elevators' queues
    elevators[0].add_request(RequestHere(5, time.time()))
    elevators[0].add_request(RequestHere(2, time.time() + 5))
    elevators[1].add_request(RequestHere(8, time.time() + 10))
    elevators[1].add_request(RequestHere(1, time.time() + 15))

    # Process requests for each elevator
    for elevator in elevators:
        elevator.process_requests()


if __name__ == "__main__":
    main()
