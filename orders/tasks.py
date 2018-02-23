from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou successfully placed an order, order id is {}'.format(order.first_name ,order_id)
    mail_sent = send_mail(subject, message,
                          '271380178@qq.com',
                          [order.email])
    return mail_sent
