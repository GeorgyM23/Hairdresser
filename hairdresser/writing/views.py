# coding=utf-8
from django.shortcuts import render, redirect
from .forms import RecordsForm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version


def sending_email():
    server = 'smtp.gmail.com'
    user = 'georgymihalyants23@gmail.com'
    password = 'Goha_2005'

    recipients = next(RecordsForm.Meta.it)
    sender = 'georgymihalyants23@gmail.com'
    subject = "Задравствуйте"
    html = '<html> <p>Георгий вы записанны к прихмахеру на <b>04:03:2022 в 14:00</b></p></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Goldene Schere <' + sender + '>'
    msg['To'] = ','.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText('plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


def last(request):
    return render(request, 'writing/last.html')


def writing_home(request):
    error = ''
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid():
            form.save()
            sending_email()
            return redirect('last')
        else:
            error = 'Форма была неверной'

    form = RecordsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'writing/writing_home.html', data)
