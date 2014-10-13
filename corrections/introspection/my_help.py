import inspect

class HelpGenerator(object):
    _indent = 0

    def __call__(self, obj, name=None):
        if inspect.ismodule(obj):
            self.visit_module(obj, name)
        elif inspect.isclass(obj):
            self.visit_class(obj, name)
        elif inspect.ismethod(obj):
            self.visit_method(obj.im_func, name)
        elif inspect.ismethoddescriptor(obj):
            self.visit_methoddescriptor(obj, name)
        elif inspect.isfunction(obj):
            self.visit_function(obj, name)
        else:
            self.visit_default(obj, name)

    def visit_module(self, obj, name):
        myname = name or obj.__name__
        self.display('Module %s' % (myname))
        self.display(obj.__doc__)
        self._indent += 1
        for name in dir(obj):
            member = getattr(obj, name)
            if getattr(member, '__module__', None) != myname:
                continue
            self(member, name)
        print
        self._indent -= 1

    def visit_class(self, obj, name):
        title = 'class %s' % (name or obj.__name__)
        if obj.__bases__:
            title += '(%s):' % ', '.join([parent.__name__ for parent in obj.__bases__])
        else:
            title +=  ':'
        self.display(title)
        self.display(obj.__doc__)
        self._indent += 1
        for name in dir(obj):
            if not name in obj.__dict__:
                continue
            self(getattr(obj, name), name)
        print
        self._indent -= 1

    def visit_method(self, obj, name):
        self.display('method %s%s' % (name or obj.__name__,
                                      inspect.formatargspec(*inspect.getargspec(obj))))
        self.display(obj.__doc__ or '')

    def visit_methoddescriptor(self, obj, name):
        self.display('method %s(...)' % name or obj.__name__)
        self.display(obj.__doc__)

    def visit_function(self, obj, name):
        self.display('function %s%s' % (name or obj.__name__,
                                        inspect.formatargspec(*inspect.getargspec(obj))))
        self.display(obj.__doc__)

    def visit_default(self, obj, name):
        if name:
            self.display('%s = %s' % (name, obj))
        else:
            self.display('%s (%s) is not handled' % (obj, obj.__class__))

    def display(self, msg):
        print '  %s%s' % ('  '*self._indent, msg or '')


def help(obj=None):
    if obj is None:
        print 'type help(obj) to get help on a particular object'
    HelpGenerator()(obj)


if __name__ == '__main__':
    import sys
    print '-'*80
    help(sys.modules[__name__])
    print '-'*80
    help(HelpGenerator)
    print '-'*80
    help(dict)
    print '-'*80
    help({})
