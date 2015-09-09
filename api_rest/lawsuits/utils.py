# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from django.template.loader import render_to_string, select_template
from rest_framework import serializers


def is_number(value):
    if not value.isnumeric():
        raise serializers.ValidationError('Preencha o campo apenas com numeros.')


def parse_mail_template(template, context):
    """From a mail template returns the mail subject and body.

    Template example:

        Subject: Hello {{ user.name }}
        {# blank line #}
        Hello,

        I'm the message body.

    """
    rendered = render_to_string(template, context)
    rendered_lines = rendered.split('\n')
    subject = re.match(r'Subject: (.*)', rendered_lines[0]).group(1).strip()

    body = '\n'.join(rendered_lines[2:])
    body = loader.get_template(body)

    return subject, body


class EmailMessage(object):
    def __init__(self, to, subject, template, context, from_email=None, bcc=[], reply_to=None, attachments=None):
        '''
        If "from" is None, then use settings.DEFAULT_FROM_EMAIL
        '''
        self.to = [to] if not (isinstance(to, list) or isinstance(to, tuple)) else to
        self.bcc = [bcc] if not (isinstance(bcc, list) or isinstance(bcc, tuple)) else bcc
        self.subject = subject
        self.template = template
        self.context = context
        self.from_email = from_email or settings.DEFAULT_FROM_EMAIL
        self.reply_to = reply_to
        self.attachments = [attachments] if not (isinstance(attachments, list) or isinstance(attachments, tuple)) else attachments

    def send(self):
        '''
        Returns True/False
        '''

        try:
            s = loader.get_template(self.subject)
            t = loader.get_template(self.template)
        except Exception as e:
            print e

        headers = {}

        if self.reply_to:
            headers.update({'Reply-To': self.reply_to})

        self.context['settings'] = settings

        subject = s.render(Context(self.context))
        content = t.render(Context(self.context))

        msg = EmailMultiAlternatives(subject, content, self.from_email, self.to, self.bcc, headers=headers)
        msg.attach_alternative(content, getattr(settings, 'EMAIL_MIMETYPE', 'text/plain'))

        if self.attachments[0]:
            for file_doc in self.attachments:
                file_name = file_doc.name
                msg.attach(file_name.split('/')[-1], file_doc.read(), 'application/pdf')
        try:
            msg.send(fail_silently=False)
        except Exception, e:
            print 'Exception: ', e
            return False
        return True
