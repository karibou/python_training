"""little GTK / Glade exercise

"Send Mail" button should only be sensitive when mail addresses
are valid.
"""

import gtk
import sys

def quit(window, event):
    """callback connected to 'delete-event' on main window"""
    print "Bye"
    sys.exit(0)

def address_entry_changed(entry, send_button):
    """callback connected to 'changed' signal on address_entry"""
    content = entry.get_text()
    # emails are separated with ';'
    email_list = [email.strip() for email in content.split(';')]
    for email in email_list:
        if not is_mail_valid(email):
            send_button.set_sensitive(False)
            return
    send_button.set_sensitive(True)

def do_send_mail(button, textview, address_entry, subject_entry):
    """callback called when 'clicked' signal is emitted on 'send button'"""
    textbuffer = textview.get_buffer()
    start, end = textbuffer.get_bounds()
    text = textbuffer.get_text(start, end)
    print "*" * 10, "Sending Mail", "*" * 10
    print "To : ", address_entry.get_text().split(';')
    print "Subject : ", subject_entry.get_text()
    print "Content :\n", text
    print "*" * 34

## Should be imported from other module written during the training session
import re
# This pattern is just a test one
VALID_MAIL_RGX = re.compile(r"[a-zA-Z\d_][a-zA-Z\d._-]*@[a-zA-Z\d_][a-zA-Z\d_-]*\.[a-z]{2,3}$")
def is_mail_valid(email):
    """returns True if email is valid"""
    return VALID_MAIL_RGX.match(email) is not None

def run():
    builder = gtk.Builder()
    builder.add_from_file('sendemail_ui.glade')
    send_button = builder.get_object('sendmail_button')
    textview = builder.get_object('body_textview')
    address_entry = builder.get_object('address_entry')
    subject_entry = builder.get_object('subject_entry')
    builder.connect_signals({
        'on_main_delete_event' : quit,
        'on_address_entry_changed' : (address_entry_changed, send_button),
        'on_send_clicked' : (do_send_mail, textview, address_entry, subject_entry),
        })
    gtk.main()


if __name__ == '__main__':
    run()
