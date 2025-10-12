#include <Python.h>

PyMODINIT_FUNC
PyInit_method_formatters(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("95165774e50df86d685c__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3____utils___method_formatters");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "95165774e50df86d685c__mypyc.init_faster_web3____utils___method_formatters");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_method_formatters(); }
