#include "Python.h"

static PyObject* maFunction(PyObject *self, PyObject *args){
    long res = 0;
    return Py_BuildValue("l", res);
}

static PyMethodDef MESFONCTIONS[] = {
    {"fonc", maFunction, METH_VARARGS, "ma premiere fonction c"},
    {NULL, NULL}
};

void initmodc(void) {
    Py_InitModule("modc", MESFONCTIONS);
}
