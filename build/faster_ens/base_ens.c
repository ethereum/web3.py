#include <Python.h>

PyMODINIT_FUNC
PyInit_base_ens(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("c0256778788a14b22fea__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_ens___base_ens");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "c0256778788a14b22fea__mypyc.init_faster_ens___base_ens");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_base_ens(); }
