from django.db import models
from django.db.models import ForiegnKey, PositiveIntegerField
from django.db.models import Count, Sum
from django.contrib.auth.admin import User
from django.db.models import Q
from django.db.models.functions import Coalesce


class Transaction(models.Model):
    CHARGE = 1
    BUY = 2
    TRANSFER = 3

    TRANSACTION_TYPE = (
        (CHARGE, "Charge"),
        (BUY, "Buy"),
        (TRANSFER, "Transfer")
    )

    user = models.ForeignKey(User, related_name='transactions', on_delete=models.RESTRICT)
    transaction_type = models.PositiveIntegerField(choices=TRANSACTION_TYPE)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"

    @classmethod
    def get_report(cls):
        positive_trans = Sum(
            'transactions__amount',
            filter=Q(transactions__transaction_type=1)
        )
        negative_trans = Sum(
            'transaction__amount',
            filter=Q(transactions__transaction_type__in=[2, 3])
        )
        users = User.objects.all().annotate(
            transactions_count=Count('transactions__id'),
            balance=Coalesce(positive_trans, 0) - Coalesce(negative_trans, 0)
        )
        return users

    @classmethod
    def get_total_balance(cls):
        queryset = cls.get_report()
        return queryset.aggregate(Sum('balance'))


class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name='balance_records', on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.balance} - {self.created_time} "

    @classmethod
    def record_user_balance(cls, user):
        positive_transactions = Sum('amount', filter=Q(transaction_type=1))
        negative_transactions = Sum('amount', filter=Q(transaction_type__in=[2, 3]))

        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0)
        )

        instance = cls.objects.create(user=user, balance=user_balance['balance'])
        return instance

    @classmethod
    def record_all_users_balance(cls):
        for user in User.objects.all():
            record = cls.record_user_balance(user)
            print(record)
