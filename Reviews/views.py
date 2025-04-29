from django.shortcuts import get_object_or_404, render

from Reviews.models import Review

# Create your views here.


def all_reviews(request):
    return render(request,"Reviews/all_reviews.html")



def current_review(request,review_id):
    review = get_object_or_404(Review, id=review_id)
    context = {
        'review': review,
    }
    
    return render(request,"Reviews/current_review.html",context=context)
