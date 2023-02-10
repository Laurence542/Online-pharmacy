from django.conf.urls.static import static
from django.conf import settings
from . import views
from.views import about
from.views import feature
from.views import searchBar

from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/',about, name = "about"),
    path('feature/',feature, name = "feature"),
    path('search/',searchBar, name = 'search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
