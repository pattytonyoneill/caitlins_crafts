from django.shortcuts import render, get_object_or_404
from .models import Crafts


def all_crafts(request):
    """ A view to show all crafts, including sorting and search queries """

    crafts = Crafts.objects.all()

    context = {
        'crafts': crafts,
    }

    return render(request, 'crafts/crafts.html', context)


def craft_detail(request, craft_id):
    """ A view to show individual craft details """

    craft = get_object_or_404(Crafts, pk=craft_id)

    context = {
        'craft': craft,
    }

    return render(request, 'crafts/craft_detail.html', context)
