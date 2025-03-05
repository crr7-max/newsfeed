from django.urls import path



from .views import (
    news_list,
    news_detail,
    homePageViews, contactPageWiev
)



urlpatterns = [
    path('',homePageViews,name = 'home_page'),
    path('news/all/', news_list, name = 'all_news_list'),
    path("news/<int:id>/", news_detail, name = "news_detail_page"),
    path('new/contact/',contactPageWiev, name = 'contact')
]
