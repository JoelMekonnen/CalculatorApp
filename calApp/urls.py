from django.urls import path, include
from .views import SignUpView, homepage, HistoryPage, ShowHistory, userUpdate
urlpatterns = [
    path('register', SignUpView.as_view(), name="register"),
    path('', HistoryPage.as_view(), name='save'),
    path('history/', ShowHistory.as_view(), name='history'),
    path('update/<int:pk>/', userUpdate.as_view(), name='update'),
]