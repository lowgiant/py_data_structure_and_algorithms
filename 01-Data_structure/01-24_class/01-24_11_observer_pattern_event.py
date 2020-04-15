# -*- coding: utf-8 -*- 
class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, "update")
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


if __name__ == "__main__":
    pub = Publisher(["점심", "퇴근"])

    jiny = Subscriber("지니")
    fairy = Subscriber("요정")
    coder = Subscriber("코더")

    pub.register("점심", fairy)
    pub.register("퇴근", fairy)
    pub.register("퇴근", coder)
    pub.register("점심", jiny)

    pub.dispatch("점심", "점심시간 입니다.")
    pub.dispatch("퇴근", "저녁시간 입니다.")

