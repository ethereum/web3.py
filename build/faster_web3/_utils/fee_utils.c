#include <Python.h>

PyMODINIT_FUNC
PyInit_fee_utils(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("d5b4baa1f9b4011ff1bd__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3____utils___fee_utils");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "d5b4baa1f9b4011ff1bd__mypyc.init_faster_web3____utils___fee_utils");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_fee_utils(); }
