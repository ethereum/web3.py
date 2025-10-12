#include <Python.h>

PyMODINIT_FUNC
PyInit_gethdev(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("0f6029afddfacd3d5db8__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3___auto___gethdev");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "0f6029afddfacd3d5db8__mypyc.init_faster_web3___auto___gethdev");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_gethdev(); }
