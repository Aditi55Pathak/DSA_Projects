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
    def __init__(self,id):
        self.id=id
        self.current_floor=0
        self.direction=1 # Choose 1 for up , -1 for down according to you need
        self.queueRequest=[]  # Priority queue for floor request

    def add_request(self, request):
        heapq.heappush(self.queueRequest, (request.floornumber, request))
