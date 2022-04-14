"""Defines views"""
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from trading_accounts.models import TradingAccount
from .models import Transaction
from .serializers import TransactionSerializer
from .services.extractor import Extractor
from .services.transformer import Transformer
from .services.loader import Loader
from .services.validator import Validator


# pylint:disable=too-many-ancestors
class TransactionViewSet(viewsets.ModelViewSet):
    """API endpoints for Transaction"""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # pylint: disable=no-self-use
    @action(methods=['post'], detail=False)
    def batch_upload(self, request):
        """
        Action to batch create transactions via file upload
        """
        account = TradingAccount.objects.get(pk=request.POST['account_id'])

        filepointer = request.FILES['file']
        validator = Validator(filepointer)
        if validator.validity():
            # Reset File Pointer to Beginning of File
            # remove when there is a way to make a copy and use independent
            # filepointers
            beginning_of_file_position = 0
            filepointer.seek(beginning_of_file_position)
            # :end Reset File Pointer to Beginning of File
            raw_data_string = filepointer.read().decode('UTF-8')

            transactions_string = Extractor(raw_data_string).extract()
            transactions = Transformer(transactions_string).parse()
            [loaded, duplicates, not_loaded] = \
                Loader(account, transactions).load()
            result = {
                "loaded": len(loaded),
                "duplicates": len(duplicates),
                "not_loaded": len(not_loaded),
            }
            response_code = status.HTTP_202_ACCEPTED
        else:
            result = {
                "loaded": 0,
                "duplicates": 0,
                "not_loaded": 0,
            }
            response_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return Response(
            result,
            response_code
        )

