from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_craft(request):
    """ Add a craft to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CraftForm(request.POST, request.FILES)
        
        if form.is_valid():
            craft = form.save()
            messages.success(request, 'Successfully added craft!')
            return redirect(reverse('craft_detail', args=[craft.id]))

        else:
            messages.error(request, 'Failed to add craft. Please ensure the form is valid.')

    else:
        form = CraftForm()

    template = 'crafts/add_craft.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_craft(request, craft_id):
    """ Edit a craft in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    craft = get_object_or_404(Crafts, pk=craft_id)
    if request.method == 'POST':
        form = CraftForm(request.POST, request.FILES, instance=craft)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated craft!')
            return redirect(reverse('craft_detail', args=[craft.id]))
        else:
            messages.error(request, 'Failed to update craft. Please ensure the form is valid.')
    else:
        form = CraftForm(instance=craft)
        messages.info(request, f'You are editing {craft.name}')

    template = 'crafts/edit_craft.html'
    context = {
        'form': form,
        'craft': craft,
    }

    return render(request, template, context)


@login_required
def delete_craft(request, craft_id):
    """ Delete a craft from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    craft = get_object_or_404(Crafts, pk=craft_id)
    craft.delete()
    messages.success(request, 'Craft deleted!')
    return redirect(reverse('crafts'))
