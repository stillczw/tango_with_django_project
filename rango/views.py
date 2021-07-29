from django.shortcuts import render

from django.http import HttpResponse

# include a hyperlink to other pages by using <a></a>
def index(request):
    # return HttpResponse("Rango says hey there partner! <a href=\"/rango/about/\">About</a>")

    # Construct a dictionary
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page. <a href=\"/rango/\">Index</a>")

    # context_dict = {}
    return render(request, 'rango/about.html', context=None)