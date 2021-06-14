from abc import ABC, abstractmethod
from random import randrange
# from typing import List

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass
    @abstractmethod
    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass
    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass

class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    _state = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """
    _observers = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    def attach(self, observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    """
    The subscription management methods.
    """
    def notify(self):
        """
        Trigger an update in each subscriber.
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    def some_business_logic(self):
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject: Subject):
        """
        Receive update from subject.
        """
        pass

"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""

class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to 'lower than three' event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to 'zero or exceeds two' event")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject):
        if subject._state >= 8:
            print("ConcreteObserverC: Reacted to 'exceeds seven' event")

if __name__ == "__main__":
    # The client code.
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    # subject.detach(observer_a) # comment this out
    observer_c = ConcreteObserverC()
    subject.attach(observer_c)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.some_business_logic()