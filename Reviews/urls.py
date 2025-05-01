from django.urls import path

from Reviews.views import *

app_name = "Reviews"

urlpatterns = [
    path("all/",all_reviews,name="all"),
    path("<int:review_id>/",current_review,name="cur_review_page")
]