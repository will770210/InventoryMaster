from datetime import time, datetime, timedelta, timezone

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from store.models import *
from inventory.models import *

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

# @register_job(scheduler, "interval", seconds=300, replace_existing=True)
# def test_job():
#     print("I'm a test job!")


@register_job(scheduler, "cron", year='*', month='*', day='*', hour='1', minute='0')
def check_safe_inventory():
    print("Execute check_safe_inventory job!")
    stores = Store.objects.filter(enable=True)

    now_date = datetime.now().date()

    check_safe_inventory_days = 3  # 計算前n天庫存使用量

    start_date = datetime.combine((now_date - timedelta(days=check_safe_inventory_days + 1)), datetime.min.time(),
                                  tzinfo=timezone.utc)

    end_date = datetime.combine((now_date - timedelta(days=1)), datetime.max.time(), tzinfo=timezone.utc)

    for store in stores:

        inventories = Inventory.objects.filter(store=store)

        for inventory in inventories:
            rule = Safety_Inventory_Rule.objects.filter(inventory=inventory).first()
            histories = Inventory_History.objects.filter(created_at__range=[start_date, end_date], inventory=inventory,
                                                         action_type='OUT')
            inventory_sum_qty = 0
            for history in histories:
                inventory_sum_qty = inventory_sum_qty + (history.previous_amount - history.current_amount)

            inventory_avg_qty = (inventory_sum_qty/check_safe_inventory_days)

            inventory.safety_inventory_amount = rule.safety_days * inventory_avg_qty  # save safety_inventory_amount

            if inventory.amount < inventory.safety_inventory_amount:
                inventory.is_less_safety_inventory = True

            inventory.save()

register_events(scheduler)

scheduler.start()
print("Scheduler started!")