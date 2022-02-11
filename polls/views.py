
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
import polls

from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailsView(generic.DetailView):
    model = Question
    template_name = 'details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'result.html'


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


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "result.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=[question.id]))
