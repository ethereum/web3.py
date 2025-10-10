#include <Python.h>

PyMODINIT_FUNC
PyInit_type_conversion(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("d3a4f7a67f1084c42c9b__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3____utils___type_conversion");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "d3a4f7a67f1084c42c9b__mypyc.init_faster_web3____utils___type_conversion");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_type_conversion(); }
