from django.urls import path
from .views import news_list, news_detail , home_page_view , contact_us , about_us , page_404, EditView

urlpatterns = [
    path('' , home_page_view, name='home_page_view'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail'),
    path('news/<slug>/edit/', EditView.as_view(), name='news_edit'),

    path('contact-us/', contact_us, name='contact_us'),
    path('about/', about_us, name='about_us'),
    path('page_404/', page_404, name='page_404'),

]