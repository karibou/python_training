import inspect

def myhelp(command):
    if inspect.ismodule(command):
        cmd_doc = inspect.getdoc(command)
    elif inspect.isclass(command):
        cmd_doc = inspect.getdoc(command)
    elif inspect.isbuiltin(command):
        cmd_doc = inspect.getdoc(command)
        
        print cmd_doc
