import gevent


sleep = gevent.sleep
spawn = gevent.spawn


class Timeout(gevent.Timeout):
    def check(self):
        pass
