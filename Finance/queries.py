from django.db.models import F, Sum, Count, Case, When, Value
from .models import *


def query_0():
    q = Employee.objects.all()
    return q


def query_1():
    q = Payslip.objects.filter(payment=None).annotate(total=F('base') + F('tax') + F('insurance') + F('overtime')).aggregate(total_dept=Sum('total'))
    return q


def query_2(x):
    q = Salary.objects.filter(overtime__gte=x).aggregate(total_overtime=Sum('payslip__overtime'))
    return q


def query_3():
    q = Payment.objects.aggregate(total=Sum('amount'))
    return q


def query_4(x):
    q = Employee.objects.filter(id=x).aggregate(total_hours=Sum('employeeprojectrelation__hours'))
    return q


def query_5(x):
    q = Employee.objects.annotate(total_payment=Sum('salary__payslip__payment__amount')).filter(total_payment__gt=x)
    return q


def query_6():
    q = Employee.objects.annotate(total_hours=Sum('employeeprojectrelation__hours')).order_by('-total_hours','account__first_name').first()
    return q


def query_7():
    q = Department.objects.annotate(total=Sum('employee__salary__payslip__payment',default=0)).order_by('-total','name').first()
    return q

def query_8():
    q = Department.objects.filter(project__estimated_end_time__lte=F('project__end_time')).annotate(count=Count('project')).order_by('-count','name').first()
    return q


def query_9(x):
    q = Employee.objects.filter(attendance__in_time__lt=x).annotate(count=Count('pk')).order_by('-count','account__first_name').first()
    return q


def query_10():
    q = Employee.objects.filter(project__isnull=True).aggregate(total=Count('pk'))
    return q


