import inspect

def help(obj):
    print 'class', obj.__class__.__name__, 'defined in', obj.__class__.__module__
    if obj.__doc__:
        print 'description:', obj.__doc__
    objdict = getattr(obj, '__dict__', {}) # some objects have no dict (eg dict class)
    if objdict:
        print 'instance attributes:'
        for name, val in sorted(obj.__dict__.iteritems()):
            print '  %s: %r' % (name, val)
    callables, attrs = [], []
    for name in dir(obj):
        if name in objdict:
            continue
        val = getattr(obj, name)
        if callable(val):
            callables.append( (name, val) )
        else:
            attrs.append( (name, val) )
    if attrs:
        print 'other attributes:'
        for name, val in sorted(attrs):
            print '  %s: %r' % (name, val)
    if callables:
        print 'callables:'
        for name, val in sorted(callables):
            try:
                args, vararg, kwarg, default = inspect.getargspec(val)
            except TypeError:
                continue
            argstrings = args[:-len(default)]
            for arg, default in zip(args[-len(default):], default):
                argstrings.append('%s=%r' % (arg, default))
            if vararg:
                argstrings.append('*'+vararg)
            if kwarg:
                argstrings.append('**'+kwarg)
            print '  %s(%s): %s' % (name, ','.join(argstrings), val.__doc__ or u'')

if __name__ == '__main__':
    import sys
    print '-'*80
    help(sys.modules[__name__])
    print '-'*80
    help(help)
    print '-'*80
    help(dict)
    print '-'*80
    help({})
