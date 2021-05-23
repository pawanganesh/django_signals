from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Order


@receiver(m2m_changed, sender=Order.cars.through)
def m2m_changed_cars_order(sender, instance, action, **kwargs):
    total = 0
    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        print('running')
        print(action)
        for car in instance.cars.all():
            total += 1
            total_price += car.price
        instance.total = total
        instance.total_price = total_price
        instance.save()
