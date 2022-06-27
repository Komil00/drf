from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from .models import Loan
from .serializers import LoanSerializer


class LoanListView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]