import random
from django.shortcuts import render
from .models import Welcome


def index(request):
    """ A view to return the index page """

    sentences = list(Welcome.objects.all())
    sentence = random.choice(sentences)
    template = 'home/index.html'
    context = {
        "sentence": sentence,
    }
    return render(request, template, context)
