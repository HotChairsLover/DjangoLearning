import datetime


class UserLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        method = request.method
        path = request.path
        time = datetime.datetime.now()
        text = f"IP:{ip};METHOD:{method};PATH:{path};TIME:{time}\n"
        with open("logs.txt", "a") as logs:
            logs.write(text)

        response = self.get_response(request)
        return response
