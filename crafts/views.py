from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Crafts, Category
from .forms import CraftForm


def all_crafts(request):
    """ A view to show all crafts, including sorting and search queries """

    crafts = Crafts.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                crafts = crafts.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            crafts = crafts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            crafts = crafts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('crafts'))
     
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            crafts = crafts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'crafts': crafts,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'crafts/crafts.html', context)


def craft_detail(request, craft_id):
    """ A view to show individual craft details """

    craft = get_object_or_404(Crafts, pk=craft_id)

    context = {
        'craft': craft,
    }

    return render(request, 'crafts/craft_detail.html', context)


def add_craft(request):
    """ Add a craft to the store """
    if request.method == 'POST':
        form = CraftForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added craft!')
            return redirect(reverse('add_craft'))

        else:
            messages.error(request, 'Failed to add craft. Please ensure the form is valid.')

    else:
        form = CraftForm()

    template = 'crafts/add_craft.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
