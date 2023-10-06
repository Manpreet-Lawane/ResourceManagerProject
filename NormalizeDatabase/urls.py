from django.urls import path
from NormalizeDatabase.views import RawDataUploadView, FeedHospitalDataView, FeedHospitalExpensesView, GetExpense, ExpensesGraph

urlpatterns = [
    path('RawDataUpload/', RawDataUploadView.as_view(), name='RawDataUpload'),
    path('FeedHospitalData/', FeedHospitalDataView.as_view(), name='FeedHospitalData'),
    path('FeedHospitalExpenses/', FeedHospitalExpensesView.as_view(), name='FeedHospitalExpensesView'),
    path('GetExpense/', GetExpense.as_view(), name='GetExpense'),
    path('ExpensesGraph/', ExpensesGraph.as_view(), name='ExpensesGraph')
]

