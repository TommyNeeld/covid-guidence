from celery import Celery
from celery.utils.log import get_task_logger
from config import settings

logger = get_task_logger(__name__)


celery_app = Celery('tasks', broker=f'pyamqp://guest@{settings.celery_host}//')


@celery_app.task
def add(x, y):
    res = x + y
    logger.info("Adding %s + %s, res: %s" % (x, y, res))
    return res
