from django.shortcuts import render
from .models import Crafts


def all_crafts(request):
    """ A view to show all crafts, including sorting and search queries """

    crafts = Crafts.objects.all()

    context = {
        'crafts': crafts,
    }

    return render(request, 'crafts/crafts.html', context)
