from gi.repository import Gtk

def exit(win):
    Gtk.main_quit()

def handle_click_on_ok_button(b):
    print 'ok clic'

b = Gtk.Builder()
b.add_from_file('test.glade')

b.connect_signals({
    'on_ok_button_clicked': handle_click_on_ok_button
})



w = b.get_object('window1')
#w = Gtk.Window()



w.show_all()
w.connect('destroy', exit)

Gtk.main()
