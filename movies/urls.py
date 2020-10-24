from django.urls import path
from django.contrib.flatpages import views as flatpage_views

from . import views


urlpatterns = [
    path('', views.MoviesView.as_view(), name='home'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('category/<str:slug>', views.FilterCategoryView.as_view(), name='category'),
    path('search/', views.Search.as_view(), name='search'),
    path('about-us/', flatpage_views.flatpage, {'url': '/about-us/'}, name='about'),
    path('contacts/', flatpage_views.flatpage, {'url': '/contacts/'}, name='contacts'),
    path('add-rating', views.AddStarRating.as_view(), name='add_rating'),
    path('json-filter/', views.JsonFilterMoviesViews.as_view(), name='json_filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]
