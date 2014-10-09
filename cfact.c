#include "Python.h"

unsigned long fact(unsigned long value) {

    if ( value == 1 ) {
        return 1;
        } else {
        return value * fact(value - 1);
    }
}

static PyObject* Factorielle(PyObject *self, PyObject *args){
    unsigned long result = 0;
    int ok;
    char *s; int size;
    unsigned long value = 0;

    ok = PyArg_ParseTuple(args, "k", &value);

    result = fact(value);

    return Py_BuildValue("k", result);
}



static PyMethodDef MESFONCTIONS[]= {
    {"cfact", Factorielle, METH_VARARGS, "Factorielle en C"},
    {NULL, NULL}
};

void initcfact(void) {
    Py_InitModule("cfact", MESFONCTIONS);
    }
