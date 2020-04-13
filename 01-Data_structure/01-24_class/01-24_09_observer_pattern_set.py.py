# -*- coding: utf-8 -*- 
class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == "__main__":
    pub = Publisher()

    jiny = Subscriber("지니")
    fairy = Subscriber("요정")
    coder = Subscriber("코더")

    pub.register(jiny)
    pub.register(fairy)
    pub.register(coder)

    pub.dispatch("출근")
    pub.unregister(coder)
    pub.dispatch("퇴근")