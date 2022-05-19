from django.core.exceptions import PermissionDenied
import datetime

class FilterIPMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        request_date = datetime.date.today()
        request_time = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
        with open('request_file.txt', 'a') as request_file:
            request_file.write(', '.join([str(request_date), str(request_time), str(request.method), str(request.get_raw_uri())]))
            request_file.write('\n')

        resource = self.get_response(request)
        return resource
