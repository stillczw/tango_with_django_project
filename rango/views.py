from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category
from rango.models import Page


# include a hyperlink to other pages by using <a></a>
def index(request):
    # return HttpResponse("Rango says hey there partner! <a href=\"/rango/about/\">About</a>")

    # the first 5 objects in descending order of likes
    category_list = Category.objects.order_by('-likes')[:5]

    # the top five most viewed pages
    page_list = Page.objects.order_by('-views')[:5]

    # Construct a dictionary
#   context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    # Return a rendered response
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # return HttpResponse("Rango says here is the about page. <a href=\"/rango/\">Index</a>")

    # context_dict = {}
    return render(request, 'rango/about.html', context=None)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
