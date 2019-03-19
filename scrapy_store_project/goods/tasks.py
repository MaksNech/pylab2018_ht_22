from celery.task import task
from celery.utils.log import get_task_logger

from .models import Bag

logger = get_task_logger(__name__)


@task(
    name="save_goods_to_db"
)
def save_goods_to_db(items_list):
    print("*" * 20)
    print("*" * 20)
    print('IN TASK '*5)
    print("*" * 20)
    print("*" * 20)

    # for item in items_list:
        # bag = Bag(
        #     title=item['title'],
        #     brand=item['brand'],
        #     image=item['image'],
        #     price=item['price'],
        #     size=item['size'],
        #     description=item['description']
        # )
        # bag.save()
        # print("*" * 20)
        # print("*" * 20)
        # print(item)
        # print(item['brand'])
        # print(item['image'])
        # print(item['price'])
        # print(item['size'])
        # print(item['description'])
        # print("*" * 20)
        # print("*" * 20)
