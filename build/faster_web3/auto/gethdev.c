#include <Python.h>

PyMODINIT_FUNC
PyInit_gethdev(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("a75ef894e9249d4405a1__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3___auto___gethdev");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "a75ef894e9249d4405a1__mypyc.init_faster_web3___auto___gethdev");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_gethdev(); }
