
from winreg import QueryValue
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, "index.html", context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "details.html", context)


def result(request , question_id):
    response = 'result %s'
    return HttpResponse(response %question_id)


def vote(request , question_id):
    response = "vote %s"
    return HttpResponse(response %question_id)
