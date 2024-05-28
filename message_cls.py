from typing import List, Callable

class MessageBroker:

    def __init__(self):
        self.subscribers: List[Callable] = []

    def subscribe(self, subscriber: Callable):
        self.subscribers.append(subscriber)

    async def send_all(self, message: str):
        if self.subscribers:
            last_subscriber = self.subscribers[-1]
            await last_subscriber(message)



message_broker = MessageBroker()

