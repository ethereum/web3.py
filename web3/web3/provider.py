from six.moves.queue import Queue
import threading

class Provider(object):

    def __init__(self):
        self.requests = Queue()
        self.responses = {}

        self.request_thread = threading.Thread(target=self.process_requests)
        self.request_thread.daemon = True
        self.request_thread.start()

    def process_requests(self):
        while True:
            request = self.requests.get()

            try:
                response = self._make_request(request)
            except Exception as e:
                response = e

            self.responses[request["messageId"]] = response

    def _make_request(self, request):
        raise NotImplementedError("Providers must implement this method")