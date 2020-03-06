#!/usr/bin/python3
import threading
import time
class MultiThreading:

    def __init__(self):
        self.thread = None
        self.started = True
    def threaded_program(self):
        while self.started:
            print("running")
            print(time.asctime())
            time.sleep(1)
    def run(self):
        self.thread = threading.Thread(target=self.threaded_program, args=())
        self.thread.start()
    def stop(self):
        self.started = False
        self.thread.join()

app = MultiThreading()
app.run()
for i in range(10):
    print(i)
time.sleep(10)
app.stop()