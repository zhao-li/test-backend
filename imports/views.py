"""Defines views"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ImportTransactions(APIView):
    """API endpoints for Imports"""

    def post(self, request):
        """This action handles receiving a file posted by a client"""
        account_id = request.POST['account_id']
        file = request.FILES['attachment']
        raw_data_string = request.FILES['attachment'].read().decode('UTF-8')

        transactions_string = TransactionExtractor(raw_data_string).extract()
        transactions = TransactionParser(transactions_string).parse()
        #[saved, duplicates] = save transactions
        return Response(
            duplicates,
            status=status.HTTP_202_ACCEPTED,
        )

