from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Rate


def list_rates(request):
    '''
    MTVU
    V - views
    U - urls
    M - model
    T - template
    '''
    rates = Rate.objects.all()

    context = {
        'rates': rates
    }

    return render(request, 'rates_list.html', context)


def test_template(request):
    name = request.GET.get('name')

    context = {
        'username': name
    }

    return render(request, 'test_template.html', context)


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
