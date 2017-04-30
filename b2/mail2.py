#coding=utf-8



import object2
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import basename
import exceptions2
import object2
import system2

system2.reload_utf8()

__ALL__ = ["mail"]

SERVER_DICT = object2.StaticDict({"126.com":"smtp.126.com"})



def mail( user , pass_wd  ,title , content , tos , server = None,port = 25, files = None , html = False ,encoding = None):
    if isinstance(tos , basestring):
        tos = [tos]
    user , suffix = user.split("@")
    server = SERVER_DICT.get(suffix) if server is None else server
    exceptions2.judge_str(server)
    exceptions2.judge_type(tos , (list , tuple))
    content_type = "plain" if html is False else "html"
    encoding = "utf-8" if encoding is None else encoding
    mail_object = MIMEMultipart()
    if not isinstance(title,unicode):
        title = unicode(title)
    mail_object["Subject"] = title
    mail_object["From"] = "{user}<{user}@{suffix}>".format(user = user , suffix = suffix)
    mail_object["To"] = ";".join(tos)
    mail_object.attach(MIMEText(content, _subtype = content_type , _charset = encoding))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            mail_object.attach(part)
    service = smtplib.SMTP(server , port)
    service.login(user , pass_wd)
    service.sendmail("{user}@{suffix}".format(user = user , suffix = suffix ) , tos , mail_object.as_string())

