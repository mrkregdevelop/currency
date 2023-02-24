from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.models import Rate
from currency.forms import RateForm


# GET (list)
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


# GET (details)
def rates_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'rate': rate
    }

    return render(request, 'rates_details.html', context)


def rates_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()  # save validate, Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rates_create.html', context)


def rates_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()  # save validate, Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        # try:
        #     rate = Rate.objects.get(id=pk)
        # except Rate.DoesNotExist:
        #     raise Http404('Rate does not exist')
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'rates_update.html', context)


def rates_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        context = {
            'rate': rate,
        }
        return render(request, 'rates_delete.html', context)


def test_template(request):
    name = request.GET.get('name')

    context = {
        'username': name
    }

    return render(request, 'test_template.html', context)


def status_code(request):
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
    # create user

    response = HttpResponse(
        'Not Found',
        status=404,
    )
    return response


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def request_methods(request):
    '''
    1. GET - client wants to get data from server (read)
    http:\\localhost:8000\path\?name=John&age=27

    2. POST - client wants push data to server (create)
    http:\\localhost:8000\path\

    name=John&age=27

    3. PUT - client wants update record on server (update) name=John&age=28
    4. PATCH - client wants update record on server partially (partial update) name=John or age=27

    5. DELETE - client wants to delete record on server (delete)

    6. OPTIONS - client wants to know which methods are available

    7. HEAD (GET) - client wants info about (without body)

    HTML - GET, POST

    C - POST
    R - GET (list, details)
    U - PUT\PATCH
    D - DELETE
    '''
    if request.method == 'GET':
        message = 'GET method'
    elif request.method == 'POST':
        message = 'POST method'

    return HttpResponse(message)
