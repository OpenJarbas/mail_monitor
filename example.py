from mail_monitor import EmailMonitor

"""
enable less secure apps https://myaccount.google.com/lesssecureapps
enable imap  https://mail.google.com/mail/u/1/?tab=mm#settings/fwdandpop
"""
mail = ""
password = ""

m = EmailMonitor(mail, password, time_between_checks=5)


def new_email(mail):
    print(mail)


m.on_new_email = new_email

# optionally run in background
# m.setDaemon(True)

m.start()
