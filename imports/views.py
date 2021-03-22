"""Defines views"""
from rest_framework.views import APIView
from rest_framework.response import Response


class ImportTransactions(APIView):
    """API endpoints for Imports"""
    def post(self, request):
        print(request.FILES['attachment'])
        print(request.POST['account_id'])
        for chunk in request.FILES['attachment'].chunks():
            print(chunk)
            print('===')
        return Response()

