from django.core.exceptions import PermissionDenied


class FilterIpAddress:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        denied_ips = []
        ip = request.META.get('REMOTE_ADDR')
        if ip in denied_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response
