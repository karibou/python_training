import gtk

def exit(win):
    print 'ici', win
    gtk.main_quit()

w = gtk.Window()
w.connect('destroy', exit)
vb = gtk.HBox()
w.add(vb)



b = gtk.Button('ok')
l = gtk.Label('toto')
vb.add(b)
vb.add(l)


w.show_all()


gtk.main()
