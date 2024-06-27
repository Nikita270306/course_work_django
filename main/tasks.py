from celery import shared_task


@shared_task(name='send_message')
def send_message(mailing_id):
    from django_coursework.main.models import Mailing
    from django_coursework.main.services.services import finish_task, delete_task, send_mailing
    mailing = Mailing.objects.get(pk=mailing_id)
    if finish_task(mailing):
        delete_task(mailing)
        return
    return send_mailing(mailing)