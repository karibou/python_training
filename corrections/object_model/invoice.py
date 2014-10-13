# -*- coding: iso-8859-1 -*-
# Exercice cours Python
# Copyright (c) 2002-2012 Logilab, SA
#
#
# The goal of this exercise is first to deduce the interface of the classes
# InvoiceItem, Nails and Planks.
# So read the existing code and try and deduce most of the interface.
# The second part of the exercise consists in implementing those interfaces
# to transform this skeleton of a program into a fully functional program.
# You will write the code for InvoiceItem, Nails and Planks.

import time

nail_price = [10, 15, 18]

def NailPrice(date):
    """Return the price of a kg of nails depending on the date"""
    q,r=divmod(date,len(nail_price))
    return nail_price[int(r)]

class Invoice(object):
    """The Invoice class defines a model of invoice system.
    The lines of an invoice are appended to the invoice using the
    Append method"""
    def __init__(self, client, date=None):
        """The constructor of the class. will take the name of the
        client and the invoice's date as parameter. By default if no
        date is provided it will use today's date."""
        self.client = client
        if not date:
            self.date = time.time()
        else:
            self.date = date
        self.items=[]

    def __len__(self):
        """return the number of lines of the invoice"""
        return len(self.items)

    def __getitem__(self,i):
        """Returns the ith line of invoice."""
        return self.items[i]

    def __setitem__(self,i,v):
        """Forbid the modification of the invoice."""
        raise AttributeError

    def get_date(self):
        """Returns the date of the invoice."""
        return self.date

    def append_item(self,item):
        """Append a line of invoice at the end of the invoice."""
        self.items.append(item)

    def display(self):
        """Prints the invoice."""
        client =  "Attn: %s" % self.client
        datestr =  "The %s" % time.strftime("%x",time.localtime(self.date))
        lg_entete = max(len(client),len(datestr))
        print
        print client
        print datestr
        print "-"*lg_entete
        print
        invoice_total = 0
        # see the chapter about strings to understand the following
        print "%10s %29s\t%5s\t%6s %3s\t%8s" %("Date","Label","Qty","UPrice", "Uni", "Total")
        print "-"*80
        for i in self.items:
            q = i.get_quantity()
            pu = i.unit_price()
            u = i.unit()
            total = i.total_price()
            titre = i.description()
            d = i.get_date()
            date = time.strftime("%x",time.localtime(d))
            # see the chapter about strings to understand the following
            print "%10s %29s\t%5.0f\t%6.2f %3s\t%8.2f" % (date, titre, q, pu, u, total)
            invoice_total += total
        print "-"*80
        print "%65s%15.2f" % ("Total", invoice_total)
        print


class InvoiceItem(object):
    """A line of invoice. This is a base class.
    The derived classes should implement the methods of this interface."""
    def __init__(self, date, titre):
        """Construct a line of invoice. Caller must provide the label
        and date"""
        if not date:
            date=time.time()
        self.titre=titre
        self.date=date

    def description(self):
        """Returns the label of the line."""
        return self.titre

    def get_quantity(self):
        """Return the quantity of products."""
        raise NotImplementedError

    def unit_price(self):
        """Return the unit price of the product."""
        raise NotImplementedError

    def unit(self):
        """Return the unit type (kg,cm,m,pound...) of the product."""
        raise NotImplementedError

    def total_price(self):
        """Return the total price of this line."""
        return self.get_quantity()*self.unit_price()

    def get_date(self):
        """Return the date of purchase of this product."""
        return self.date


class Nails(InvoiceItem):
    """Implementation of InvoiceItem for a bag of nails"""
    def __init__(self,q=1,date=None):
        InvoiceItem.__init__(self,date,"Bag of 12 nails")
        self.quantite=q
        self.unite = "pce"
        self.poids = 0.01 # it weighs 0.01 kg

    def unit_price(self):
        #calls NailPrice to get the price of the bag at the time of purchase
        return NailPrice(self.date)*self.poids

    def get_quantity(self):
        return self.quantite

    def unit(self):
        return self.unite

class Planks(InvoiceItem):
    """Implementation of InvoiceItem for a wooden plank"""
    def __init__(self,q=1,date=None):
        InvoiceItem.__init__(self,date,"Wooden Plank")
        self.quantite = q
        self.unite = "m²"

    def get_quantity(self):
        return self.quantite

    def unit(self):
        return self.unite

    def unit_price(self):
        return 34.5

def main():
    """The main function: create an invoice, and print it."""
    fact = Invoice("Felix the fakir")
    clous = Nails(10000)
    fact.append_item(clous)
    planches = Planks(2)
    fact.append_item(planches)
    fact.display()


if __name__ == "__main__":
    # this code is excuted if and only if the script was invoked
    # from the command line
    main()
