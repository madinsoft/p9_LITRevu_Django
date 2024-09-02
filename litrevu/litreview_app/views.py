from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from litreview_app.models import Review, Ticket

"""def homepage(request):
    return render(request, 'litreview_app/homepage.html')"""

def registration(request):
    return render(request, 'litreview_app/registration.html')

@login_required
def flow(request):
    reviews = Review.objects.all()
    return render(request, 'litreview_app/flow.html', {'reviews': reviews})

@login_required
def ticket_create(request):
    return render(request, 'litreview_app/ticket_create.html')

@login_required
def review_create(request):
    return render(request, 'litreview_app/review_create.html')

@login_required
def review_ticket_create(request):
    return render(request, 'litreview_app/review_ticket_create.html')

@login_required
def your_posts(request):
    return render(request, 'litreview_app/your_posts.html')

@login_required
def review_update(request):
    return render(request, 'litreview_app/review_update.html')

@login_required
def ticket_update(request):
    return render(request, 'litreview_app/ticket_update.html')

@login_required
def subscriptions(request):
    return render(request, 'litreview_app/subscriptions.html')

def user_update(request):
    return render(request, 'litreview_app/user_update.html')

