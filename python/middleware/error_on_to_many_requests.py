from django.core.exceptions import PermissionDenied
import datetime


class ErrorOnToManyRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_count = 0
        self.time = datetime.datetime.now()

    def __call__(self, request):
        self.request_count += 1
        if self.request_count > 10 and (self.time - datetime.datetime.now()) < datetime.timedelta(seconds=10):
            self.time = datetime.datetime.now()
            self.request_count = 0
            raise PermissionDenied

        response = self.get_response(request)
        return response
