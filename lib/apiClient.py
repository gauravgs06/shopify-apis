import requests
import time
import queue
import json

from dataclasses import dataclass, field


@dataclass(order=True)
class RequestTask:
    url: str = field(compare=False)
    headers: dict = field(default=None, compare=False)
    payload: dict = field(default=None, compare=False)
    params: dict = field(default=None, compare=False)
    method: str = field(default="GET", compare=False)
    priority: int = 2

    def run(self, func=None) -> requests.Response:
        if func != None:
            response = func(self)
        else:
            response = requests.request(method=self.method, url=self.url,
                                        headers=self.headers, data=None if self.payload == None else json.dumps(self.payload), params=self.params)
        return response


class SyncAPIClient:
    __apiClient = None
    __taskList: queue.Queue = queue.PriorityQueue()
    __waitTime: int = 0.51

    @classmethod
    def getApiClient(cls):
        if cls.__apiClient == None:
            cls.__apiClient = SyncAPIClient()
        return cls.__apiClient

    @classmethod
    def setTimeDelay(cls, waitTime=0.51):
        cls.__waitTime = waitTime

    def createTask(self, task) -> requests.Response:
        self.__class__.__taskList.put(task)

    def runAdhocTask(self, task, waitTime=0.51):
        response = task.run()
        time.sleep(waitTime)
        return response

    def start(self, func=None):
        while not self.__class__.__taskList.empty():
            try:
                result = self.__class__.__taskList.get().run(func)
                time.sleep(self.__class__.__waitTime)
                yield result
            except queue.Empty as e:
                print("Queue Empty:", e)
            except Exception as e:
                print("Error:", e)

    def completeTask(self):
        self.__class__.__taskList.task_done()

    def isTaskListEmpty(self):
        return self.__class__.__taskList.empty()
