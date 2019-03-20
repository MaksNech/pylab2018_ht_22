import requests
import tempfile
from celery.task import task
from django.core import files
from celery.utils.log import get_task_logger

from .models import Bag

logger = get_task_logger(__name__)


@task(
    name="save_goods_to_db"
)
def save_goods_to_db(items_list):

    for item in items_list:
        bag = Bag(
            title=item['title'],
            brand=item['brand'],
            image=item['image'],
            price=item['price'],
            size=item['size'],
            description=item['description']
        )

        request = requests.get(item['image'], stream=True)
        if request.status_code != requests.codes.ok:
            continue
        file_name = item['image'].split('/')[-1]
        lf = tempfile.NamedTemporaryFile()
        for block in request.iter_content(1024 * 8):
            if not block:
                break
            lf.write(block)

        bag.image.save(file_name, files.File(lf))

        bag.save()
