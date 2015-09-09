# coding: utf-8
from django.dispatch import receiver, Signal
from django.db.models import signals
from lawsuits.models import Lawsuit
from django.conf import settings
from lawsuits.utils import EmailMessage
from django.core import serializers

@receiver(signals.post_save, sender=Lawsuit, dispatch_uid="lawsuit-registered")
def lawsuit_registered(sender, instance, **kwargs):
    try:
        lawsuit = sender.objects.get(id=instance.id)

        # printa o email
        print 'Subject: Processo numero %s foi gerado' % lawsuit.number
        print 'Message: O processo numero %s foi criado para o usuario %s' % (lawsuit.number, lawsuit.user.username)
        print 'To: ffreitasalves@gmail.com'
        print 'From: techgui3@gmail.com'


        # Configurei um SMTP no settings.
        emails = []
        emails.append('ffreitasalves@gmail.com')
        _from = settings.DEFAULT_FROM_EMAIL
        #_from = 'guilherme.marques@cargobr.com'
        subject = 'emails/create_alert_subject.txt'
        template = 'emails/create_alert.txt'
        to = emails
        context = {'lawsuit': lawsuit}
        message = EmailMessage(to=to,
                               subject=subject,
                               template=template,
                               context=context,
                               reply_to=_from,
                               )

        try:
            print 'send'
            message.send()
        except Exception as e:
            print e
    except sender.DoesNotExist:
        return