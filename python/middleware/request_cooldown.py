from time import sleep


class RequestCooldownMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0

    def __call__(self, request):
        self.request_count += 1

        if self.request_count > 5:
            sleep(2)
            self.request_count = 0

        response = self.get_response(request)

        return response
