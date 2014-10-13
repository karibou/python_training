#include <Python.h>

/*
 * if you want to compile by hand on a linux/unix platform (though usually using
 * setup.py will do the job):
 *
 * gcc -fPIC -I/usr/include/python2.X -shared c_api_fact.c -o cfact.so -lpython2.X
 */

static PyObject * wrap_fact(PyObject *self, PyObject *args) {

  long res, n;
  if(!PyArg_ParseTuple(args, "l", &n)) {
      /* no need to setup the exception, PyArg_ParseTuple has already done it
       */
      PyErr_SetString(PyExc_TypeError, "I need an integer !");
      return NULL;
  }
  for(res = 1; n > 0; --n) {
     res *= n ;
  }

  return Py_BuildValue("l", res);

}

static PyMethodDef CFACT_METHODS[] = {
  {"fact", wrap_fact, METH_VARARGS, "C implementation of a factoriel functionC"},
  {NULL,   NULL}        /* Sentinel */
};


void initcfact(void)
{
  (void) Py_InitModule("cfact", CFACT_METHODS);
}


