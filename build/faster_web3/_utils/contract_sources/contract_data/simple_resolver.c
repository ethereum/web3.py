#include <Python.h>

PyMODINIT_FUNC
PyInit_simple_resolver(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("faster_web3._utils.contract_sources.contract_data.simple_resolver__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_web3____utils___contract_sources___contract_data___simple_resolver");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "faster_web3._utils.contract_sources.contract_data.simple_resolver__mypyc.init_faster_web3____utils___contract_sources___contract_data___simple_resolver");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_simple_resolver(); }
