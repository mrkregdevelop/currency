from django.http import HttpResponse

from currency.models import Rate


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, '
                      f'source: {rate.source}, created: {rate.created} <br>')

    return HttpResponse(str(result))


def status_code(request):
    # create user

    response = HttpResponse(
        'Not Found',
        status=404,
    )
    return response


'''
1xx - informational response
2xx - success
200 - OK
201 - Created
202 - Accepted
204 - No Content
3xx - redirect
301 - Moved Permanently
302 - Found (Previously "Moved temporarily")
4xx - client errors
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
405 - Method Not Allowed
5xx - server errors (code errors)
500 - Internal Server Error (python)
'''
