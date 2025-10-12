#include <Python.h>

PyMODINIT_FUNC
PyInit_contracts(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("64f9d080262e6bf77878__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3____utils___contracts");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "64f9d080262e6bf77878__mypyc.init_faster_web3____utils___contracts");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_contracts(); }
