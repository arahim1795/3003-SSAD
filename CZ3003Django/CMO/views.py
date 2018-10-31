from django.http import HttpResponse
from .models import Operator

# Create your views here.

def index(request):
    all_operators = Operator.objects.all()
    html = ''
    for operator in all_operators:
        url = '/CMO/' + str(operator.operator_id) + '/'
        html += '<a href="' + url + '">' + operator.operator_name + '</a><br>'
    return HttpResponse(html)


def detail(request, operator_id):
    return HttpResponse("<h2>Details for Operator id: " + str(operator_id) + "</h2>")