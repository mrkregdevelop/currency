from time import time


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)

        end = time()

        print(f'Total time: {end - start}')
        # RequestResponseLog.objects.create(path=..., method=..., time=...)

        return response
