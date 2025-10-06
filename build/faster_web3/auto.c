#include <Python.h>

PyMODINIT_FUNC
PyInit_auto(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("a5a22c221938b4ca5e7a__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3___auto");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "a5a22c221938b4ca5e7a__mypyc.init_faster_web3___auto");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_auto(); }
