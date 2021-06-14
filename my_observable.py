class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None
    def attach(self, subscriber): # attach a new subscriber
        self.__subscribers.append(subscriber)
    def detach(self):
        self.__subscribers.pop()
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers] # show all the current subscribers
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    def addNews(self, news):
        self.__latestNews = news
    def getNews(self):
        return 'News: {}'.format(self.__latestNews)

class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews() )

class PrintSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews() )

class MediaSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    def update(self):
        print(type(self).__name__, self.publisher.getNews() )


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    # iterate over the collection of subscribers, notifying each
    for Subscriber in [MediaSubscriber, PrintSubscriber, EmailSubscriber]:
        Subscriber(news_publisher)
        print('\nSubscribers: {}'.format( news_publisher.subscribers() ))
        news_publisher. addNews('something newsworthy happened')
        news_publisher.notifySubscribers()