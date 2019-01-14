from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Todo


def index(request):
    todo_list = Todo.objects.order_by('-updated_at')[:5]
    template = loader.get_template('todo/index.html')
    context = {
        'todo_list': todo_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        template = loader.get_template('todo/detail.html')
        context = {
            'todo': todo,
        }
        return HttpResponse(template.render(context, request))
    except Exception as e:
        context = {
            'msg': 'Error.'
        }
        return HttpResponse(template.render(context, request))
