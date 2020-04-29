from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from django.core.mail import send_mail


@task(name="email_sender_task")

def sendemail(subject, message, to_id):
    from_id = "no-reply@mogamboproject.com"
    email = send_mail(
        subject,
        message,
        from_id,
        [to_id],
        fail_silently=False)
    return email


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)
