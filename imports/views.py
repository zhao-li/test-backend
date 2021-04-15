"""Defines views"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from trading_accounts.models import TradingAccount
from .services.transactions_extractor import TransactionsExtractor
from .services.transactions_transformer import TransactionsTransformer
from .services.transactions_loader import TransactionsLoader


class ImportTransactions(APIView):
    """API endpoints for Imports"""

    def post(self, request):
        """This action handles receiving a file posted by a client"""
        account = TradingAccount.objects.get(pk=request.POST['account_id'])
        raw_data_string = request.FILES['attachment'].read().decode('UTF-8')

        transactions_string = TransactionsExtractor(raw_data_string).extract()
        transactions = TransactionsTransformer(transactions_string).parse()
        [loaded, duplicates, not_loaded] = \
            TransactionsLoader(account, transactions).load()
        return Response(
            {
                "loaded": len(loaded),
                "duplicates": len(duplicates),
                "not_loaded": len(not_loaded),
            },
            status=status.HTTP_202_ACCEPTED,
        )

