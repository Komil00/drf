from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response

from .models import Loan
from .serializers import LoanSerializer


class LoanListView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAdminUser]

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = LoanSerializer(queryset, many=True)
    #     return Response(serializer.data)