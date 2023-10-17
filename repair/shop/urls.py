from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('news/', views.news),
    path('news/news_show/<int:id>', views.news_show, name='news_show'),
    path('about/', views.about),
    path('policy/', views.policy),
    path('vacancies/', views.vacancies),
    path('coupons/', views.coupons),
    path('faq/', views.faq),
    path('<int:id>', views.usluga_detail,
         name='usluga_detail'),
    path("create/", views.usluga_create),
    path("edit/<int:id>/", views.usluga_edit),
    path("delete/<int:id>/", views.usluga_delete),
    path('reviews/', views.review, name='reviews'),

    path('', views.usluga_list, name='usluga_list'),
    path('<str:usluga_genre_name>/', views.usluga_list,
         name='usluga_list_by_genre'),
]
