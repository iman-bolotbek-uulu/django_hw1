from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import models


# Create your views here.
def index(request):
    question_list = models.Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'index.html',context)


def detail(request, id):
    question = get_object_or_404(models.Question,id=id)
    context = {
        'question': question,
    }
    return render(request,'detail.html',context)


def result(request, id):
    question = get_object_or_404(models.Question, id=id)
    context = {
        'question': question,
    }
    return render(request, 'result.html', context)


def vote(request, id):
    question = get_object_or_404(models.Question, id=id)
    select_choice = request.POST.get('choice')
    choice = get_object_or_404(models.Choice,id=select_choice,question=question)
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('result',args=(question.id,)))


def item(request):
    item = models.Item.objects.all()
    context = {
        'item': item
    }
    return render(request, 'list_item.html', context)


def detail_item(request, id):
    items = get_object_or_404(models.Item, id=id)
    context = {
        'items': items
    }
    return render(request, 'detail_item.html', context)