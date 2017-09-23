from django.conf.urls import url
from django.conf.urls.static import static
from visualize import views

urlpatterns = [
    url(r'^$', views.indexPageView.as_view()),
    url(r'^upload$', views.send_data),
    url(r'^fetch$', views.fetch_data),
    url(r'^scores$', views.scoresPageView.as_view())
]