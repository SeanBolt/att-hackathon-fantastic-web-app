from django.conf.urls import url
from django.conf.urls.static import static
from visualize import views

urlpatterns = [
    url(r'^$', views.indexPageView.as_view()),
]
