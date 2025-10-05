#include "init.c"
#include "getargs.c"
#include "getargsfast.c"
#include "int_ops.c"
#include "float_ops.c"
#include "str_ops.c"
#include "bytes_ops.c"
#include "list_ops.c"
#include "dict_ops.c"
#include "set_ops.c"
#include "tuple_ops.c"
#include "exc_ops.c"
#include "misc_ops.c"
#include "generic_ops.c"
#include "pythonsupport.c"
#include "__native_e60543e00a47358a5fd8.h"
#include "__native_internal_e60543e00a47358a5fd8.h"

static PyObject *CPyDunder___get__datatypes_____init___3_PropertyCheckingFactory_obj(PyObject *self, PyObject *instance, PyObject *owner) {
    instance = instance ? instance : Py_None;
    return CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(self, instance, owner);
}
PyObject *CPyDef_datatypes_____mypyc___3__init___3_PropertyCheckingFactory_obj_setup(PyObject *cpy_r_type);
PyObject *CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj(void);

static PyObject *
datatypes_____init___3_PropertyCheckingFactory_obj_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    if (type != CPyType_datatypes_____init___3_PropertyCheckingFactory_obj) {
        PyErr_SetString(PyExc_TypeError, "interpreted classes cannot inherit from compiled");
        return NULL;
    }
    PyObject *self = CPyDef_datatypes_____mypyc___3__init___3_PropertyCheckingFactory_obj_setup((PyObject*)type);
    if (self == NULL)
        return NULL;
    return self;
}

static int
datatypes_____init___3_PropertyCheckingFactory_obj_traverse(faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *self, visitproc visit, void *arg)
{
    return 0;
}

static int
datatypes_____init___3_PropertyCheckingFactory_obj_clear(faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *self)
{
    return 0;
}

static void
datatypes_____init___3_PropertyCheckingFactory_obj_dealloc(faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *self)
{
    PyObject_GC_UnTrack(self);
    if (datatypes_____init___3_PropertyCheckingFactory_obj_free_instance == NULL) {
        datatypes_____init___3_PropertyCheckingFactory_obj_free_instance = self;
        return;
    }
    CPy_TRASHCAN_BEGIN(self, datatypes_____init___3_PropertyCheckingFactory_obj_dealloc)
    datatypes_____init___3_PropertyCheckingFactory_obj_clear(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
    CPy_TRASHCAN_END(self)
}

static CPyVTableItem datatypes_____init___3_PropertyCheckingFactory_obj_vtable[2];
static bool
CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_trait_vtable_setup(void)
{
    CPyVTableItem datatypes_____init___3_PropertyCheckingFactory_obj_vtable_scratch[] = {
        (CPyVTableItem)CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____call__,
        (CPyVTableItem)CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____get__,
    };
    memcpy(datatypes_____init___3_PropertyCheckingFactory_obj_vtable, datatypes_____init___3_PropertyCheckingFactory_obj_vtable_scratch, sizeof(datatypes_____init___3_PropertyCheckingFactory_obj_vtable));
    return 1;
}

static PyMethodDef datatypes_____init___3_PropertyCheckingFactory_obj_methods[] = {
    {"__call__",
     (PyCFunction)CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____call__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__call__($cls, name, bases, namespace, **kwargs)\n--\n\n")},
    {"__get__",
     (PyCFunction)CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____get__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__get__($instance, owner)\n--\n\n")},
    {"__setstate__", (PyCFunction)CPyPickle_SetState, METH_O, NULL},
    {"__getstate__", (PyCFunction)CPyPickle_GetState, METH_NOARGS, NULL},
    {NULL}  /* Sentinel */
};

static PyTypeObject CPyType_datatypes_____init___3_PropertyCheckingFactory_obj_template_ = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "__init___PropertyCheckingFactory_obj",
    .tp_new = datatypes_____init___3_PropertyCheckingFactory_obj_new,
    .tp_dealloc = (destructor)datatypes_____init___3_PropertyCheckingFactory_obj_dealloc,
    .tp_traverse = (traverseproc)datatypes_____init___3_PropertyCheckingFactory_obj_traverse,
    .tp_clear = (inquiry)datatypes_____init___3_PropertyCheckingFactory_obj_clear,
    .tp_methods = datatypes_____init___3_PropertyCheckingFactory_obj_methods,
    .tp_call = PyVectorcall_Call,
    .tp_descr_get = CPyDunder___get__datatypes_____init___3_PropertyCheckingFactory_obj,
    .tp_basicsize = sizeof(faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject),
    .tp_vectorcall_offset = offsetof(faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject, vectorcall),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC | _Py_TPFLAGS_HAVE_VECTORCALL,
    .tp_doc = PyDoc_STR("__init___PropertyCheckingFactory_obj()\n--\n\n"),
};
static PyTypeObject *CPyType_datatypes_____init___3_PropertyCheckingFactory_obj_template = &CPyType_datatypes_____init___3_PropertyCheckingFactory_obj_template_;

PyObject *CPyDef_datatypes_____mypyc___3__init___3_PropertyCheckingFactory_obj_setup(PyObject *cpy_r_type)
{
    PyTypeObject *type = (PyTypeObject*)cpy_r_type;
    faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *self;
    if (datatypes_____init___3_PropertyCheckingFactory_obj_free_instance != NULL) {
        self = datatypes_____init___3_PropertyCheckingFactory_obj_free_instance;
        datatypes_____init___3_PropertyCheckingFactory_obj_free_instance = NULL;
        Py_SET_REFCNT(self, 1);
        PyObject_GC_Track(self);
        return (PyObject *)self;
    }
    self = (faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *)type->tp_alloc(type, 0);
    if (self == NULL)
        return NULL;
    self->vtable = datatypes_____init___3_PropertyCheckingFactory_obj_vtable;
    self->vectorcall = CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____call__;
    return (PyObject *)self;
}

PyObject *CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj(void)
{
    PyObject *self = CPyDef_datatypes_____mypyc___3__init___3_PropertyCheckingFactory_obj_setup((PyObject *)CPyType_datatypes_____init___3_PropertyCheckingFactory_obj);
    if (self == NULL)
        return NULL;
    return self;
}


static PyObject *CPyDunder___get__datatypes_____new___3_PropertyCheckingFactory_obj(PyObject *self, PyObject *instance, PyObject *owner) {
    instance = instance ? instance : Py_None;
    return CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(self, instance, owner);
}
PyObject *CPyDef_datatypes_____mypyc___3__new___3_PropertyCheckingFactory_obj_setup(PyObject *cpy_r_type);
PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj(void);

static PyObject *
datatypes_____new___3_PropertyCheckingFactory_obj_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    if (type != CPyType_datatypes_____new___3_PropertyCheckingFactory_obj) {
        PyErr_SetString(PyExc_TypeError, "interpreted classes cannot inherit from compiled");
        return NULL;
    }
    PyObject *self = CPyDef_datatypes_____mypyc___3__new___3_PropertyCheckingFactory_obj_setup((PyObject*)type);
    if (self == NULL)
        return NULL;
    return self;
}

static int
datatypes_____new___3_PropertyCheckingFactory_obj_traverse(faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *self, visitproc visit, void *arg)
{
    return 0;
}

static int
datatypes_____new___3_PropertyCheckingFactory_obj_clear(faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *self)
{
    return 0;
}

static void
datatypes_____new___3_PropertyCheckingFactory_obj_dealloc(faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *self)
{
    PyObject_GC_UnTrack(self);
    if (datatypes_____new___3_PropertyCheckingFactory_obj_free_instance == NULL) {
        datatypes_____new___3_PropertyCheckingFactory_obj_free_instance = self;
        return;
    }
    CPy_TRASHCAN_BEGIN(self, datatypes_____new___3_PropertyCheckingFactory_obj_dealloc)
    datatypes_____new___3_PropertyCheckingFactory_obj_clear(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
    CPy_TRASHCAN_END(self)
}

static CPyVTableItem datatypes_____new___3_PropertyCheckingFactory_obj_vtable[2];
static bool
CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_trait_vtable_setup(void)
{
    CPyVTableItem datatypes_____new___3_PropertyCheckingFactory_obj_vtable_scratch[] = {
        (CPyVTableItem)CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____call__,
        (CPyVTableItem)CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____get__,
    };
    memcpy(datatypes_____new___3_PropertyCheckingFactory_obj_vtable, datatypes_____new___3_PropertyCheckingFactory_obj_vtable_scratch, sizeof(datatypes_____new___3_PropertyCheckingFactory_obj_vtable));
    return 1;
}

static PyMethodDef datatypes_____new___3_PropertyCheckingFactory_obj_methods[] = {
    {"__call__",
     (PyCFunction)CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____call__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__call__($mcs, name, bases, namespace, normalizers=None)\n--\n\n")},
    {"__get__",
     (PyCFunction)CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____get__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__get__($instance, owner)\n--\n\n")},
    {"__setstate__", (PyCFunction)CPyPickle_SetState, METH_O, NULL},
    {"__getstate__", (PyCFunction)CPyPickle_GetState, METH_NOARGS, NULL},
    {NULL}  /* Sentinel */
};

static PyTypeObject CPyType_datatypes_____new___3_PropertyCheckingFactory_obj_template_ = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "__new___PropertyCheckingFactory_obj",
    .tp_new = datatypes_____new___3_PropertyCheckingFactory_obj_new,
    .tp_dealloc = (destructor)datatypes_____new___3_PropertyCheckingFactory_obj_dealloc,
    .tp_traverse = (traverseproc)datatypes_____new___3_PropertyCheckingFactory_obj_traverse,
    .tp_clear = (inquiry)datatypes_____new___3_PropertyCheckingFactory_obj_clear,
    .tp_methods = datatypes_____new___3_PropertyCheckingFactory_obj_methods,
    .tp_call = PyVectorcall_Call,
    .tp_descr_get = CPyDunder___get__datatypes_____new___3_PropertyCheckingFactory_obj,
    .tp_basicsize = sizeof(faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject),
    .tp_vectorcall_offset = offsetof(faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject, vectorcall),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC | _Py_TPFLAGS_HAVE_VECTORCALL,
    .tp_doc = PyDoc_STR("__new___PropertyCheckingFactory_obj()\n--\n\n"),
};
static PyTypeObject *CPyType_datatypes_____new___3_PropertyCheckingFactory_obj_template = &CPyType_datatypes_____new___3_PropertyCheckingFactory_obj_template_;

PyObject *CPyDef_datatypes_____mypyc___3__new___3_PropertyCheckingFactory_obj_setup(PyObject *cpy_r_type)
{
    PyTypeObject *type = (PyTypeObject*)cpy_r_type;
    faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *self;
    if (datatypes_____new___3_PropertyCheckingFactory_obj_free_instance != NULL) {
        self = datatypes_____new___3_PropertyCheckingFactory_obj_free_instance;
        datatypes_____new___3_PropertyCheckingFactory_obj_free_instance = NULL;
        Py_SET_REFCNT(self, 1);
        PyObject_GC_Track(self);
        return (PyObject *)self;
    }
    self = (faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *)type->tp_alloc(type, 0);
    if (self == NULL)
        return NULL;
    self->vtable = datatypes_____new___3_PropertyCheckingFactory_obj_vtable;
    self->vectorcall = CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____call__;
    return (PyObject *)self;
}

PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj(void)
{
    PyObject *self = CPyDef_datatypes_____mypyc___3__new___3_PropertyCheckingFactory_obj_setup((PyObject *)CPyType_datatypes_____new___3_PropertyCheckingFactory_obj);
    if (self == NULL)
        return NULL;
    return self;
}

static PyMethodDef datatypesmodule_methods[] = {
    {"verify_attr", (PyCFunction)CPyPy_datatypes___verify_attr, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("verify_attr(class_name, key, namespace)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___datatypes(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___datatypes__internal, "__name__");
    CPyStatic_datatypes___globals = PyModule_GetDict(CPyModule_faster_web3____utils___datatypes__internal);
    if (unlikely(CPyStatic_datatypes___globals == NULL))
        goto fail;
    CPyType_datatypes_____init___3_PropertyCheckingFactory_obj = (PyTypeObject *)CPyType_FromTemplate((PyObject *)CPyType_datatypes_____init___3_PropertyCheckingFactory_obj_template, NULL, modname);
    if (unlikely(!CPyType_datatypes_____init___3_PropertyCheckingFactory_obj))
        goto fail;
    CPyType_datatypes_____new___3_PropertyCheckingFactory_obj = (PyTypeObject *)CPyType_FromTemplate((PyObject *)CPyType_datatypes_____new___3_PropertyCheckingFactory_obj_template, NULL, modname);
    if (unlikely(!CPyType_datatypes_____new___3_PropertyCheckingFactory_obj))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_datatypes_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___datatypes__internal);
    Py_CLEAR(modname);
    CPy_XDECREF(CPyStatic_datatypes___apply_formatters_to_dict);
    CPyStatic_datatypes___apply_formatters_to_dict = NULL;
    CPy_XDECREF(CPyStatic_datatypes___concat);
    CPyStatic_datatypes___concat = NULL;
    Py_CLEAR(CPyType_datatypes___PropertyCheckingFactory);
    Py_CLEAR(CPyType_datatypes_____init___3_PropertyCheckingFactory_obj);
    Py_CLEAR(CPyType_datatypes_____new___3_PropertyCheckingFactory_obj);
    return -1;
}
static struct PyModuleDef datatypesmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.datatypes",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    datatypesmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___datatypes(void)
{
    if (CPyModule_faster_web3____utils___datatypes__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___datatypes__internal);
        return CPyModule_faster_web3____utils___datatypes__internal;
    }
    CPyModule_faster_web3____utils___datatypes__internal = PyModule_Create(&datatypesmodule);
    if (unlikely(CPyModule_faster_web3____utils___datatypes__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___datatypes(CPyModule_faster_web3____utils___datatypes__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___datatypes__internal;
    fail:
    return NULL;
}

char CPyDef_datatypes___verify_attr(PyObject *cpy_r_class_name, PyObject *cpy_r_key, PyObject *cpy_r_namespace) {
    int32_t cpy_r_r0;
    char cpy_r_r1;
    char cpy_r_r2;
    char cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    PyObject **cpy_r_r14;
    PyObject *cpy_r_r15;
    char cpy_r_r16;
    cpy_r_r0 = PySequence_Contains(cpy_r_namespace, cpy_r_key);
    cpy_r_r1 = cpy_r_r0 >= 0;
    if (unlikely(!cpy_r_r1)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 27, CPyStatic_datatypes___globals);
        goto CPyL8;
    }
    cpy_r_r2 = cpy_r_r0;
    cpy_r_r3 = cpy_r_r2 ^ 1;
    if (!cpy_r_r3) goto CPyL7;
    cpy_r_r4 = CPyStatics[3]; /* 'Property ' */
    cpy_r_r5 = CPyStatics[4]; /* ' not found on ' */
    cpy_r_r6 = CPyStatics[5]; /* ' class. `' */
    cpy_r_r7 = CPyStatics[6]; /* ('.factory` only accepts keyword arguments which are '
                                 'present on the ') */
    cpy_r_r8 = CPyStatics[7]; /* ' class' */
    cpy_r_r9 = CPyStr_Build(9, cpy_r_r4, cpy_r_key, cpy_r_r5, cpy_r_class_name, cpy_r_r6, cpy_r_class_name, cpy_r_r7, cpy_r_class_name, cpy_r_r8);
    if (unlikely(cpy_r_r9 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 29, CPyStatic_datatypes___globals);
        goto CPyL8;
    }
    cpy_r_r10 = CPyStatic_datatypes___globals;
    cpy_r_r11 = CPyStatics[8]; /* 'Web3AttributeError' */
    cpy_r_r12 = CPyDict_GetItem(cpy_r_r10, cpy_r_r11);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 28, CPyStatic_datatypes___globals);
        goto CPyL9;
    }
    PyObject *cpy_r_r13[1] = {cpy_r_r9};
    cpy_r_r14 = (PyObject **)&cpy_r_r13;
    cpy_r_r15 = PyObject_Vectorcall(cpy_r_r12, cpy_r_r14, 1, 0);
    CPy_DECREF(cpy_r_r12);
    if (unlikely(cpy_r_r15 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 28, CPyStatic_datatypes___globals);
        goto CPyL9;
    }
    CPy_DECREF(cpy_r_r9);
    CPy_Raise(cpy_r_r15);
    CPy_DECREF(cpy_r_r15);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 28, CPyStatic_datatypes___globals);
        goto CPyL8;
    }
    CPy_Unreachable();
CPyL7: ;
    return 1;
CPyL8: ;
    cpy_r_r16 = 2;
    return cpy_r_r16;
CPyL9: ;
    CPy_DecRef(cpy_r_r9);
    goto CPyL8;
}

PyObject *CPyPy_datatypes___verify_attr(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"class_name", "key", "namespace", 0};
    static CPyArg_Parser parser = {"OOO:verify_attr", kwlist, 0};
    PyObject *obj_class_name;
    PyObject *obj_key;
    PyObject *obj_namespace;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_class_name, &obj_key, &obj_namespace)) {
        return NULL;
    }
    PyObject *arg_class_name;
    if (likely(PyUnicode_Check(obj_class_name)))
        arg_class_name = obj_class_name;
    else {
        CPy_TypeError("str", obj_class_name); 
        goto fail;
    }
    PyObject *arg_key;
    if (likely(PyUnicode_Check(obj_key)))
        arg_key = obj_key;
    else {
        CPy_TypeError("str", obj_key); 
        goto fail;
    }
    PyObject *arg_namespace = obj_namespace;
    char retval = CPyDef_datatypes___verify_attr(arg_class_name, arg_key, arg_namespace);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = Py_None;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/datatypes.py", "verify_attr", 26, CPyStatic_datatypes___globals);
    return NULL;
}

PyObject *CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner) {
    PyObject *cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    cpy_r_r0 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r1 = cpy_r_instance == cpy_r_r0;
    if (!cpy_r_r1) goto CPyL2;
    CPy_INCREF(cpy_r___mypyc_self__);
    return cpy_r___mypyc_self__;
CPyL2: ;
    cpy_r_r2 = PyMethod_New(cpy_r___mypyc_self__, cpy_r_instance);
    if (cpy_r_r2 == NULL) goto CPyL4;
    return cpy_r_r2;
CPyL4: ;
    cpy_r_r3 = NULL;
    return cpy_r_r3;
}

PyObject *CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"instance", "owner", 0};
    static CPyArg_Parser parser = {"OO:__get__", kwlist, 0};
    PyObject *obj_instance;
    PyObject *obj_owner;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_instance, &obj_owner)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__ = obj___mypyc_self__;
    PyObject *arg_instance = obj_instance;
    PyObject *arg_owner = obj_owner;
    PyObject *retval = CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(arg___mypyc_self__, arg_instance, arg_owner);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__get__", -1, CPyStatic_datatypes___globals);
    return NULL;
}

char CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____call__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_cls, PyObject *cpy_r_name, PyObject *cpy_r_bases, PyObject *cpy_r_namespace, PyObject *cpy_r_kwargs) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject **cpy_r_r3;
    PyObject *cpy_r_r4;
    char cpy_r_r5;
    cpy_r_r0 = (PyObject *)&PyType_Type;
    cpy_r_r1 = CPyStatics[9]; /* '__init__' */
    PyObject *cpy_r_r2[5] = {cpy_r_r0, cpy_r_cls, cpy_r_name, cpy_r_bases, cpy_r_namespace};
    cpy_r_r3 = (PyObject **)&cpy_r_r2;
    cpy_r_r4 = PyObject_VectorcallMethod(cpy_r_r1, cpy_r_r3, 9223372036854775813ULL, 0);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__init__", 46, CPyStatic_datatypes___globals);
        goto CPyL2;
    } else
        goto CPyL3;
CPyL1: ;
    return 1;
CPyL2: ;
    cpy_r_r5 = 2;
    return cpy_r_r5;
CPyL3: ;
    CPy_DECREF(cpy_r_r4);
    goto CPyL1;
}

PyObject *CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____call__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"cls", "name", "bases", "namespace", 0};
    static CPyArg_Parser parser = {"%OOOO:__call__", kwlist, 0};
    PyObject *obj_cls;
    PyObject *obj_name;
    PyObject *obj_bases;
    PyObject *obj_namespace;
    PyObject *obj_kwargs;
    if (!CPyArg_ParseStackAndKeywords(args, PyVectorcall_NARGS(nargs), kwnames, &parser, NULL, &obj_kwargs, &obj_cls, &obj_name, &obj_bases, &obj_namespace)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__ = obj___mypyc_self__;
    PyObject *arg_cls;
    if (likely(Py_TYPE(obj_cls) == CPyType_datatypes___PropertyCheckingFactory))
        arg_cls = obj_cls;
    else {
        CPy_TypeError("faster_web3._utils.datatypes.PropertyCheckingFactory", obj_cls); 
        goto fail;
    }
    PyObject *arg_name;
    if (likely(PyUnicode_Check(obj_name)))
        arg_name = obj_name;
    else {
        CPy_TypeError("str", obj_name); 
        goto fail;
    }
    PyObject * arg_bases;
    if (likely(PyTuple_Check(obj_bases)))
        arg_bases = obj_bases;
    else {
        CPy_TypeError("tuple", obj_bases); 
        goto fail;
    }
    PyObject *arg_namespace;
    if (likely(PyDict_Check(obj_namespace)))
        arg_namespace = obj_namespace;
    else {
        CPy_TypeError("dict", obj_namespace); 
        goto fail;
    }
    PyObject *arg_kwargs = obj_kwargs;
    char retval = CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____call__(arg___mypyc_self__, arg_cls, arg_name, arg_bases, arg_namespace, arg_kwargs);
    CPy_DECREF(obj_kwargs);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = Py_None;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_DECREF(obj_kwargs);
    CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__init__", 37, CPyStatic_datatypes___globals);
    return NULL;
}

PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner) {
    PyObject *cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    cpy_r_r0 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r1 = cpy_r_instance == cpy_r_r0;
    if (!cpy_r_r1) goto CPyL2;
    CPy_INCREF(cpy_r___mypyc_self__);
    return cpy_r___mypyc_self__;
CPyL2: ;
    cpy_r_r2 = PyMethod_New(cpy_r___mypyc_self__, cpy_r_instance);
    if (cpy_r_r2 == NULL) goto CPyL4;
    return cpy_r_r2;
CPyL4: ;
    cpy_r_r3 = NULL;
    return cpy_r_r3;
}

PyObject *CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"instance", "owner", 0};
    static CPyArg_Parser parser = {"OO:__get__", kwlist, 0};
    PyObject *obj_instance;
    PyObject *obj_owner;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_instance, &obj_owner)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__ = obj___mypyc_self__;
    PyObject *arg_instance = obj_instance;
    PyObject *arg_owner = obj_owner;
    PyObject *retval = CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(arg___mypyc_self__, arg_instance, arg_owner);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__get__", -1, CPyStatic_datatypes___globals);
    return NULL;
}

PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____call__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_mcs, PyObject *cpy_r_name, tuple_T1O cpy_r_bases, PyObject *cpy_r_namespace, PyObject *cpy_r_normalizers) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    int32_t cpy_r_r8;
    char cpy_r_r9;
    char cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    char cpy_r_r13;
    PyObject **cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject **cpy_r_r25;
    PyObject *cpy_r_r26;
    int32_t cpy_r_r27;
    char cpy_r_r28;
    char cpy_r_r29;
    PyObject *cpy_r_r30;
    PyObject *cpy_r_r31;
    char cpy_r_r32;
    PyObject **cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    CPyTagged cpy_r_r37;
    int64_t cpy_r_r38;
    PyObject *cpy_r_r39;
    tuple_T3CIO cpy_r_r40;
    CPyTagged cpy_r_r41;
    char cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    char cpy_r_r45;
    char cpy_r_r46;
    char cpy_r_r47;
    PyObject *cpy_r_r48;
    char cpy_r_r49;
    PyObject *cpy_r_r50;
    int64_t cpy_r_r51;
    CPyTagged cpy_r_r52;
    char cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    char cpy_r_r56;
    PyObject **cpy_r_r58;
    PyObject *cpy_r_r59;
    PyObject *cpy_r_r60;
    PyObject *cpy_r_processed_namespace;
    PyObject *cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    PyObject **cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject *cpy_r_r68;
    if (cpy_r_normalizers != NULL) goto CPyL49;
    cpy_r_r0 = Py_None;
    cpy_r_normalizers = cpy_r_r0;
CPyL2: ;
    cpy_r_r1 = PyList_New(0);
    if (unlikely(cpy_r_r1 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    CPy_INCREF(cpy_r_bases.f0);
    cpy_r_r2 = PyTuple_New(1);
    if (unlikely(cpy_r_r2 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp1 = cpy_r_bases.f0;
    PyTuple_SET_ITEM(cpy_r_r2, 0, __tmp1);
    cpy_r_r3 = PyObject_GetIter(cpy_r_r2);
    CPy_DECREF(cpy_r_r2);
    if (unlikely(cpy_r_r3 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL51;
    }
CPyL4: ;
    cpy_r_r4 = PyIter_Next(cpy_r_r3);
    if (cpy_r_r4 == NULL) goto CPyL52;
    cpy_r_r5 = CPyStatics[10]; /* '__mro__' */
    cpy_r_r6 = CPyObject_GetAttr(cpy_r_r4, cpy_r_r5);
    CPy_DECREF(cpy_r_r4);
    if (unlikely(cpy_r_r6 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL53;
    }
    if (likely(PyTuple_Check(cpy_r_r6)))
        cpy_r_r7 = cpy_r_r6;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals, "tuple", cpy_r_r6);
        goto CPyL53;
    }
    cpy_r_r8 = PyList_Append(cpy_r_r1, cpy_r_r7);
    CPy_DECREF(cpy_r_r7);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL53;
    } else
        goto CPyL4;
CPyL8: ;
    cpy_r_r10 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r10)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL51;
    }
    cpy_r_r11 = PyObject_GetIter(cpy_r_r1);
    CPy_DECREF_NO_IMM(cpy_r_r1);
    if (unlikely(cpy_r_r11 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    cpy_r_r12 = CPyStatic_datatypes___concat;
    if (unlikely(cpy_r_r12 == NULL)) {
        goto CPyL54;
    } else
        goto CPyL13;
CPyL11: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"concat\" was not set");
    cpy_r_r13 = 0;
    if (unlikely(!cpy_r_r13)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL48;
    }
    CPy_Unreachable();
CPyL13: ;
    PyObject *cpy_r_r14[1] = {cpy_r_r11};
    cpy_r_r15 = (PyObject **)&cpy_r_r14;
    cpy_r_r16 = PyObject_Vectorcall(cpy_r_r12, cpy_r_r15, 1, 0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL55;
    }
    CPy_DECREF(cpy_r_r11);
    cpy_r_r17 = PySet_New(cpy_r_r16);
    CPy_DECREF(cpy_r_r16);
    if (unlikely(cpy_r_r17 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 56, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    cpy_r_r18 = PyList_New(0);
    if (unlikely(cpy_r_r18 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL56;
    }
    cpy_r_r19 = PyObject_GetIter(cpy_r_r17);
    CPy_DECREF(cpy_r_r17);
    if (unlikely(cpy_r_r19 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL57;
    }
CPyL17: ;
    cpy_r_r20 = PyIter_Next(cpy_r_r19);
    if (cpy_r_r20 == NULL) goto CPyL58;
    cpy_r_r21 = CPyStatics[11]; /* '__dict__' */
    cpy_r_r22 = CPyObject_GetAttr(cpy_r_r20, cpy_r_r21);
    CPy_DECREF(cpy_r_r20);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL59;
    }
    cpy_r_r23 = CPyStatics[12]; /* 'keys' */
    PyObject *cpy_r_r24[1] = {cpy_r_r22};
    cpy_r_r25 = (PyObject **)&cpy_r_r24;
    cpy_r_r26 = PyObject_VectorcallMethod(cpy_r_r23, cpy_r_r25, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL60;
    }
    CPy_DECREF(cpy_r_r22);
    cpy_r_r27 = PyList_Append(cpy_r_r18, cpy_r_r26);
    CPy_DECREF(cpy_r_r26);
    cpy_r_r28 = cpy_r_r27 >= 0;
    if (unlikely(!cpy_r_r28)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL59;
    } else
        goto CPyL17;
CPyL21: ;
    cpy_r_r29 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r29)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL57;
    }
    cpy_r_r30 = PyObject_GetIter(cpy_r_r18);
    CPy_DECREF_NO_IMM(cpy_r_r18);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    cpy_r_r31 = CPyStatic_datatypes___concat;
    if (unlikely(cpy_r_r31 == NULL)) {
        goto CPyL61;
    } else
        goto CPyL26;
CPyL24: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"concat\" was not set");
    cpy_r_r32 = 0;
    if (unlikely(!cpy_r_r32)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL48;
    }
    CPy_Unreachable();
CPyL26: ;
    PyObject *cpy_r_r33[1] = {cpy_r_r30};
    cpy_r_r34 = (PyObject **)&cpy_r_r33;
    cpy_r_r35 = PyObject_Vectorcall(cpy_r_r31, cpy_r_r34, 1, 0);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL62;
    }
    CPy_DECREF(cpy_r_r30);
    cpy_r_r36 = PySet_New(cpy_r_r35);
    CPy_DECREF(cpy_r_r35);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 57, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    cpy_r_r37 = 0;
    cpy_r_r38 = PyDict_Size(cpy_r_namespace);
    cpy_r_r39 = CPyDict_GetKeysIter(cpy_r_namespace);
    if (unlikely(cpy_r_r39 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 59, CPyStatic_datatypes___globals);
        goto CPyL63;
    }
CPyL29: ;
    cpy_r_r40 = CPyDict_NextKey(cpy_r_r39, cpy_r_r37);
    cpy_r_r41 = cpy_r_r40.f1;
    cpy_r_r37 = cpy_r_r41;
    cpy_r_r42 = cpy_r_r40.f0;
    if (!cpy_r_r42) goto CPyL64;
    cpy_r_r43 = cpy_r_r40.f2;
    CPy_INCREF(cpy_r_r43);
    CPy_DECREF(cpy_r_r40.f2);
    if (likely(PyUnicode_Check(cpy_r_r43)))
        cpy_r_r44 = cpy_r_r43;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 59, CPyStatic_datatypes___globals, "str", cpy_r_r43);
        goto CPyL65;
    }
    cpy_r_r45 = CPyDef_datatypes___verify_attr(cpy_r_name, cpy_r_r44, cpy_r_r36);
    CPy_DECREF(cpy_r_r44);
    if (unlikely(cpy_r_r45 == 2)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 60, CPyStatic_datatypes___globals);
        goto CPyL65;
    }
    cpy_r_r46 = CPyDict_CheckSize(cpy_r_namespace, cpy_r_r38);
    if (unlikely(!cpy_r_r46)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 59, CPyStatic_datatypes___globals);
        goto CPyL65;
    } else
        goto CPyL29;
CPyL33: ;
    cpy_r_r47 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r47)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 59, CPyStatic_datatypes___globals);
        goto CPyL50;
    }
    cpy_r_r48 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r49 = cpy_r_normalizers != cpy_r_r48;
    if (!cpy_r_r49) goto CPyL66;
    CPy_INCREF(cpy_r_normalizers);
    if (likely(cpy_r_normalizers != Py_None))
        cpy_r_r50 = cpy_r_normalizers;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 54, CPyStatic_datatypes___globals, "dict", cpy_r_normalizers);
        goto CPyL50;
    }
    cpy_r_r51 = PyDict_Size(cpy_r_r50);
    CPy_DECREF(cpy_r_r50);
    cpy_r_r52 = cpy_r_r51 << 1;
    cpy_r_r53 = cpy_r_r52 != 0;
    if (!cpy_r_r53) goto CPyL66;
    if (likely(cpy_r_normalizers != Py_None))
        cpy_r_r54 = cpy_r_normalizers;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 64, CPyStatic_datatypes___globals, "dict", cpy_r_normalizers);
        goto CPyL48;
    }
    cpy_r_r55 = CPyStatic_datatypes___apply_formatters_to_dict;
    if (unlikely(cpy_r_r55 == NULL)) {
        goto CPyL67;
    } else
        goto CPyL41;
CPyL39: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"apply_formatters_to_dict\" was not set");
    cpy_r_r56 = 0;
    if (unlikely(!cpy_r_r56)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 63, CPyStatic_datatypes___globals);
        goto CPyL48;
    }
    CPy_Unreachable();
CPyL41: ;
    PyObject *cpy_r_r57[2] = {cpy_r_r54, cpy_r_namespace};
    cpy_r_r58 = (PyObject **)&cpy_r_r57;
    cpy_r_r59 = PyObject_Vectorcall(cpy_r_r55, cpy_r_r58, 2, 0);
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 63, CPyStatic_datatypes___globals);
        goto CPyL68;
    }
    CPy_DECREF(cpy_r_r54);
    if (likely(PyDict_Check(cpy_r_r59)))
        cpy_r_r60 = cpy_r_r59;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 63, CPyStatic_datatypes___globals, "dict", cpy_r_r59);
        goto CPyL48;
    }
    cpy_r_processed_namespace = cpy_r_r60;
    goto CPyL45;
CPyL44: ;
    CPy_INCREF(cpy_r_namespace);
    cpy_r_processed_namespace = cpy_r_namespace;
CPyL45: ;
    cpy_r_r61 = (PyObject *)&PyType_Type;
    cpy_r_r62 = CPyStatics[13]; /* '__new__' */
    CPy_INCREF(cpy_r_bases.f0);
    cpy_r_r63 = PyTuple_New(1);
    if (unlikely(cpy_r_r63 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp2 = cpy_r_bases.f0;
    PyTuple_SET_ITEM(cpy_r_r63, 0, __tmp2);
    PyObject *cpy_r_r64[5] = {
        cpy_r_r61, cpy_r_mcs, cpy_r_name, cpy_r_r63,
        cpy_r_processed_namespace
    };
    cpy_r_r65 = (PyObject **)&cpy_r_r64;
    cpy_r_r66 = PyObject_VectorcallMethod(cpy_r_r62, cpy_r_r65, 9223372036854775813ULL, 0);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 70, CPyStatic_datatypes___globals);
        goto CPyL69;
    }
    CPy_DECREF(cpy_r_r63);
    CPy_DECREF(cpy_r_processed_namespace);
    if (likely(Py_TYPE(cpy_r_r66) == CPyType_datatypes___PropertyCheckingFactory))
        cpy_r_r67 = cpy_r_r66;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "__new__", 70, CPyStatic_datatypes___globals, "faster_web3._utils.datatypes.PropertyCheckingFactory", cpy_r_r66);
        goto CPyL48;
    }
    return cpy_r_r67;
CPyL48: ;
    cpy_r_r68 = NULL;
    return cpy_r_r68;
CPyL49: ;
    CPy_INCREF(cpy_r_normalizers);
    goto CPyL2;
CPyL50: ;
    CPy_DecRef(cpy_r_normalizers);
    goto CPyL48;
CPyL51: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r1);
    goto CPyL48;
CPyL52: ;
    CPy_DECREF(cpy_r_r3);
    goto CPyL8;
CPyL53: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r1);
    CPy_DecRef(cpy_r_r3);
    goto CPyL48;
CPyL54: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r11);
    goto CPyL11;
CPyL55: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r11);
    goto CPyL48;
CPyL56: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r17);
    goto CPyL48;
CPyL57: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r18);
    goto CPyL48;
CPyL58: ;
    CPy_DECREF(cpy_r_r19);
    goto CPyL21;
CPyL59: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r18);
    CPy_DecRef(cpy_r_r19);
    goto CPyL48;
CPyL60: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r18);
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r22);
    goto CPyL48;
CPyL61: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r30);
    goto CPyL24;
CPyL62: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r30);
    goto CPyL48;
CPyL63: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r36);
    goto CPyL48;
CPyL64: ;
    CPy_DECREF(cpy_r_r36);
    CPy_DECREF(cpy_r_r39);
    CPy_DECREF(cpy_r_r40.f2);
    goto CPyL33;
CPyL65: ;
    CPy_DecRef(cpy_r_normalizers);
    CPy_DecRef(cpy_r_r36);
    CPy_DecRef(cpy_r_r39);
    goto CPyL48;
CPyL66: ;
    CPy_DECREF(cpy_r_normalizers);
    goto CPyL44;
CPyL67: ;
    CPy_DecRef(cpy_r_r54);
    goto CPyL39;
CPyL68: ;
    CPy_DecRef(cpy_r_r54);
    goto CPyL48;
CPyL69: ;
    CPy_DecRef(cpy_r_processed_namespace);
    CPy_DecRef(cpy_r_r63);
    goto CPyL48;
}

PyObject *CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____call__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"mcs", "name", "bases", "namespace", "normalizers", 0};
    static CPyArg_Parser parser = {"OOOO|O:__call__", kwlist, 0};
    PyObject *obj_mcs;
    PyObject *obj_name;
    PyObject *obj_bases;
    PyObject *obj_namespace;
    PyObject *obj_normalizers = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, PyVectorcall_NARGS(nargs), kwnames, &parser, &obj_mcs, &obj_name, &obj_bases, &obj_namespace, &obj_normalizers)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__ = obj___mypyc_self__;
    PyObject *arg_mcs = obj_mcs;
    PyObject *arg_name;
    if (likely(PyUnicode_Check(obj_name)))
        arg_name = obj_name;
    else {
        CPy_TypeError("str", obj_name); 
        goto fail;
    }
    tuple_T1O arg_bases;
    PyObject *__tmp3;
    if (unlikely(!(PyTuple_Check(obj_bases) && PyTuple_GET_SIZE(obj_bases) == 1))) {
        __tmp3 = NULL;
        goto __LL4;
    }
    __tmp3 = PyTuple_GET_ITEM(obj_bases, 0);
    if (__tmp3 == NULL) goto __LL4;
    __tmp3 = obj_bases;
__LL4: ;
    if (unlikely(__tmp3 == NULL)) {
        CPy_TypeError("tuple[object]", obj_bases); goto fail;
    } else {
        PyObject *__tmp5 = PyTuple_GET_ITEM(obj_bases, 0);
        PyObject *__tmp6;
        __tmp6 = __tmp5;
        arg_bases.f0 = __tmp6;
    }
    PyObject *arg_namespace;
    if (likely(PyDict_Check(obj_namespace)))
        arg_namespace = obj_namespace;
    else {
        CPy_TypeError("dict", obj_namespace); 
        goto fail;
    }
    PyObject *arg_normalizers;
    if (obj_normalizers == NULL) {
        arg_normalizers = NULL;
        goto __LL7;
    }
    if (PyDict_Check(obj_normalizers))
        arg_normalizers = obj_normalizers;
    else {
        arg_normalizers = NULL;
    }
    if (arg_normalizers != NULL) goto __LL7;
    if (obj_normalizers == Py_None)
        arg_normalizers = obj_normalizers;
    else {
        arg_normalizers = NULL;
    }
    if (arg_normalizers != NULL) goto __LL7;
    CPy_TypeError("dict or None", obj_normalizers); 
    goto fail;
__LL7: ;
    PyObject *retval = CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____call__(arg___mypyc_self__, arg_mcs, arg_name, arg_bases, arg_namespace, arg_normalizers);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/datatypes.py", "__new__", 49, CPyStatic_datatypes___globals);
    return NULL;
}

char CPyDef_datatypes_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject **cpy_r_r9;
    PyObject **cpy_r_r10;
    void *cpy_r_r12;
    void *cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    char cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject *cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject *cpy_r_r29;
    PyObject *cpy_r_r30;
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    int32_t cpy_r_r33;
    char cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    PyObject *cpy_r_r39;
    int32_t cpy_r_r40;
    char cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    PyObject *cpy_r_r47;
    PyObject *cpy_r_r48;
    char cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject **cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject *cpy_r_r57;
    PyObject *cpy_r_r58;
    PyObject *cpy_r_r59;
    PyObject *cpy_r_r60;
    PyObject *cpy_r_r61;
    int32_t cpy_r_r62;
    char cpy_r_r63;
    PyObject *cpy_r_r64;
    PyObject *cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject **cpy_r_r69;
    PyObject *cpy_r_r70;
    PyObject *cpy_r_r71;
    int32_t cpy_r_r72;
    char cpy_r_r73;
    PyObject *cpy_r_r74;
    PyObject *cpy_r_r75;
    int32_t cpy_r_r76;
    char cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    int32_t cpy_r_r80;
    char cpy_r_r81;
    PyObject *cpy_r_r82;
    PyObject *cpy_r_r83;
    int32_t cpy_r_r84;
    char cpy_r_r85;
    PyObject **cpy_r_r87;
    PyObject *cpy_r_r88;
    PyObject *cpy_r_r89;
    PyObject *cpy_r_r90;
    PyObject *cpy_r_r91;
    PyObject *cpy_r_r92;
    PyObject **cpy_r_r94;
    PyObject *cpy_r_r95;
    PyObject *cpy_r_r96;
    PyObject **cpy_r_r98;
    PyObject *cpy_r_r99;
    PyObject *cpy_r_r100;
    PyObject *cpy_r_r101;
    int32_t cpy_r_r102;
    char cpy_r_r103;
    PyObject *cpy_r_r104;
    char cpy_r_r105;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", -1, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[74]; /* ('Any', 'Collection', 'Dict', 'Final', 'Optional', 'Tuple',
                                  'Type') */
    cpy_r_r6 = CPyStatics[22]; /* 'typing' */
    cpy_r_r7 = CPyStatic_datatypes___globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 1, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = (PyObject **)&CPyModule_faster_eth_utils;
    cpy_r_r10 = (PyObject **)&CPyModule_faster_eth_utils___toolz;
    PyObject **cpy_r_r11[2] = {cpy_r_r9, cpy_r_r10};
    cpy_r_r12 = (void *)&cpy_r_r11;
    int64_t cpy_r_r13[2] = {11, 12};
    cpy_r_r14 = (void *)&cpy_r_r13;
    cpy_r_r15 = CPyStatics[77]; /* (('faster_eth_utils', 'faster_eth_utils',
                                    'faster_eth_utils'),
                                   ('faster_eth_utils.toolz', 'faster_eth_utils',
                                    'faster_eth_utils')) */
    cpy_r_r16 = CPyStatic_datatypes___globals;
    cpy_r_r17 = CPyStatics[25]; /* 'faster_web3/_utils/datatypes.py' */
    cpy_r_r18 = CPyStatics[26]; /* '<module>' */
    cpy_r_r19 = CPyImport_ImportMany(cpy_r_r15, cpy_r_r12, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r14);
    if (!cpy_r_r19) goto CPyL37;
    cpy_r_r20 = CPyStatics[78]; /* ('mypyc_attr',) */
    cpy_r_r21 = CPyStatics[28]; /* 'mypy_extensions' */
    cpy_r_r22 = CPyStatic_datatypes___globals;
    cpy_r_r23 = CPyImport_ImportFromMany(cpy_r_r21, cpy_r_r20, cpy_r_r20, cpy_r_r22);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 13, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyModule_mypy_extensions = cpy_r_r23;
    CPy_INCREF(CPyModule_mypy_extensions);
    CPy_DECREF(cpy_r_r23);
    cpy_r_r24 = CPyStatics[79]; /* ('Web3AttributeError',) */
    cpy_r_r25 = CPyStatics[29]; /* 'faster_web3.exceptions' */
    cpy_r_r26 = CPyStatic_datatypes___globals;
    cpy_r_r27 = CPyImport_ImportFromMany(cpy_r_r25, cpy_r_r24, cpy_r_r24, cpy_r_r26);
    if (unlikely(cpy_r_r27 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 17, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyModule_faster_web3___exceptions = cpy_r_r27;
    CPy_INCREF(CPyModule_faster_web3___exceptions);
    CPy_DECREF(cpy_r_r27);
    cpy_r_r28 = CPyModule_faster_eth_utils;
    cpy_r_r29 = CPyStatics[30]; /* 'apply_formatters_to_dict' */
    cpy_r_r30 = CPyObject_GetAttr(cpy_r_r28, cpy_r_r29);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 22, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyStatic_datatypes___apply_formatters_to_dict = cpy_r_r30;
    CPy_INCREF(CPyStatic_datatypes___apply_formatters_to_dict);
    cpy_r_r31 = CPyStatic_datatypes___globals;
    cpy_r_r32 = CPyStatics[30]; /* 'apply_formatters_to_dict' */
    cpy_r_r33 = CPyDict_SetItem(cpy_r_r31, cpy_r_r32, cpy_r_r30);
    CPy_DECREF(cpy_r_r30);
    cpy_r_r34 = cpy_r_r33 >= 0;
    if (unlikely(!cpy_r_r34)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 22, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    cpy_r_r35 = CPyModule_faster_eth_utils___toolz;
    cpy_r_r36 = CPyStatics[31]; /* 'concat' */
    cpy_r_r37 = CPyObject_GetAttr(cpy_r_r35, cpy_r_r36);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 23, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    CPyStatic_datatypes___concat = cpy_r_r37;
    CPy_INCREF(CPyStatic_datatypes___concat);
    cpy_r_r38 = CPyStatic_datatypes___globals;
    cpy_r_r39 = CPyStatics[31]; /* 'concat' */
    cpy_r_r40 = CPyDict_SetItem(cpy_r_r38, cpy_r_r39, cpy_r_r37);
    CPy_DECREF(cpy_r_r37);
    cpy_r_r41 = cpy_r_r40 >= 0;
    if (unlikely(!cpy_r_r41)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 23, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    cpy_r_r42 = CPyModule_builtins;
    cpy_r_r43 = CPyStatics[32]; /* 'type' */
    cpy_r_r44 = CPyObject_GetAttr(cpy_r_r42, cpy_r_r43);
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    cpy_r_r45 = PyTuple_Pack(1, cpy_r_r44);
    CPy_DECREF(cpy_r_r44);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    cpy_r_r46 = (PyObject *)&PyType_Type;
    cpy_r_r47 = CPy_CalculateMetaclass(cpy_r_r46, cpy_r_r45);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL38;
    }
    cpy_r_r48 = CPyStatics[33]; /* '__prepare__' */
    cpy_r_r49 = PyObject_HasAttr(cpy_r_r47, cpy_r_r48);
    if (!cpy_r_r49) goto CPyL19;
    cpy_r_r50 = CPyStatics[34]; /* 'PropertyCheckingFactory' */
    cpy_r_r51 = CPyStatics[33]; /* '__prepare__' */
    cpy_r_r52 = CPyObject_GetAttr(cpy_r_r47, cpy_r_r51);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL38;
    }
    PyObject *cpy_r_r53[2] = {cpy_r_r50, cpy_r_r45};
    cpy_r_r54 = (PyObject **)&cpy_r_r53;
    cpy_r_r55 = PyObject_Vectorcall(cpy_r_r52, cpy_r_r54, 2, 0);
    CPy_DECREF(cpy_r_r52);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL38;
    }
    if (likely(PyDict_Check(cpy_r_r55)))
        cpy_r_r56 = cpy_r_r55;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals, "dict", cpy_r_r55);
        goto CPyL38;
    }
    cpy_r_r57 = cpy_r_r56;
    goto CPyL21;
CPyL19: ;
    cpy_r_r58 = PyDict_New();
    if (unlikely(cpy_r_r58 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL38;
    }
    cpy_r_r57 = cpy_r_r58;
CPyL21: ;
    cpy_r_r59 = PyDict_New();
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL39;
    }
    cpy_r_r60 = CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj();
    if (unlikely(cpy_r_r60 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 37, CPyStatic_datatypes___globals);
        goto CPyL40;
    }
    cpy_r_r61 = CPyStatics[9]; /* '__init__' */
    cpy_r_r62 = CPyDict_SetItem(cpy_r_r57, cpy_r_r61, cpy_r_r60);
    CPy_DECREF_NO_IMM(cpy_r_r60);
    cpy_r_r63 = cpy_r_r62 >= 0;
    if (unlikely(!cpy_r_r63)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 37, CPyStatic_datatypes___globals);
        goto CPyL40;
    }
    cpy_r_r64 = CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj();
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 49, CPyStatic_datatypes___globals);
        goto CPyL40;
    }
    cpy_r_r65 = CPyModule_builtins;
    cpy_r_r66 = CPyStatics[35]; /* 'staticmethod' */
    cpy_r_r67 = CPyObject_GetAttr(cpy_r_r65, cpy_r_r66);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 49, CPyStatic_datatypes___globals);
        goto CPyL41;
    }
    PyObject *cpy_r_r68[1] = {cpy_r_r64};
    cpy_r_r69 = (PyObject **)&cpy_r_r68;
    cpy_r_r70 = PyObject_Vectorcall(cpy_r_r67, cpy_r_r69, 1, 0);
    CPy_DECREF(cpy_r_r67);
    if (unlikely(cpy_r_r70 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 49, CPyStatic_datatypes___globals);
        goto CPyL41;
    }
    CPy_DECREF_NO_IMM(cpy_r_r64);
    cpy_r_r71 = CPyStatics[13]; /* '__new__' */
    cpy_r_r72 = CPyDict_SetItem(cpy_r_r57, cpy_r_r71, cpy_r_r70);
    CPy_DECREF(cpy_r_r70);
    cpy_r_r73 = cpy_r_r72 >= 0;
    if (unlikely(!cpy_r_r73)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 49, CPyStatic_datatypes___globals);
        goto CPyL40;
    }
    cpy_r_r74 = CPyStatics[34]; /* 'PropertyCheckingFactory' */
    cpy_r_r75 = CPyStatics[36]; /* '__annotations__' */
    cpy_r_r76 = CPyDict_SetItem(cpy_r_r57, cpy_r_r75, cpy_r_r59);
    CPy_DECREF(cpy_r_r59);
    cpy_r_r77 = cpy_r_r76 >= 0;
    if (unlikely(!cpy_r_r77)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL39;
    }
    cpy_r_r78 = CPyStatics[37]; /* 'mypyc filler docstring' */
    cpy_r_r79 = CPyStatics[38]; /* '__doc__' */
    cpy_r_r80 = CPyDict_SetItem(cpy_r_r57, cpy_r_r79, cpy_r_r78);
    cpy_r_r81 = cpy_r_r80 >= 0;
    if (unlikely(!cpy_r_r81)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL39;
    }
    cpy_r_r82 = CPyStatics[39]; /* 'faster_web3._utils.datatypes' */
    cpy_r_r83 = CPyStatics[40]; /* '__module__' */
    cpy_r_r84 = CPyDict_SetItem(cpy_r_r57, cpy_r_r83, cpy_r_r82);
    cpy_r_r85 = cpy_r_r84 >= 0;
    if (unlikely(!cpy_r_r85)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL39;
    }
    PyObject *cpy_r_r86[3] = {cpy_r_r74, cpy_r_r45, cpy_r_r57};
    cpy_r_r87 = (PyObject **)&cpy_r_r86;
    cpy_r_r88 = PyObject_Vectorcall(cpy_r_r47, cpy_r_r87, 3, 0);
    if (unlikely(cpy_r_r88 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL39;
    }
    CPy_DECREF(cpy_r_r57);
    CPy_DECREF(cpy_r_r45);
    cpy_r_r89 = CPyStatic_datatypes___globals;
    cpy_r_r90 = CPyStatics[27]; /* 'mypyc_attr' */
    cpy_r_r91 = CPyDict_GetItem(cpy_r_r89, cpy_r_r90);
    if (unlikely(cpy_r_r91 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 35, CPyStatic_datatypes___globals);
        goto CPyL42;
    }
    cpy_r_r92 = 0 ? Py_True : Py_False;
    PyObject *cpy_r_r93[1] = {cpy_r_r92};
    cpy_r_r94 = (PyObject **)&cpy_r_r93;
    cpy_r_r95 = CPyStatics[80]; /* ('native_class',) */
    cpy_r_r96 = PyObject_Vectorcall(cpy_r_r91, cpy_r_r94, 0, cpy_r_r95);
    CPy_DECREF(cpy_r_r91);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 35, CPyStatic_datatypes___globals);
        goto CPyL42;
    }
    PyObject *cpy_r_r97[1] = {cpy_r_r88};
    cpy_r_r98 = (PyObject **)&cpy_r_r97;
    cpy_r_r99 = PyObject_Vectorcall(cpy_r_r96, cpy_r_r98, 1, 0);
    CPy_DECREF(cpy_r_r96);
    if (unlikely(cpy_r_r99 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL42;
    }
    CPy_DECREF(cpy_r_r88);
    CPyType_datatypes___PropertyCheckingFactory = (PyTypeObject *)cpy_r_r99;
    CPy_INCREF(CPyType_datatypes___PropertyCheckingFactory);
    cpy_r_r100 = CPyStatic_datatypes___globals;
    cpy_r_r101 = CPyStatics[34]; /* 'PropertyCheckingFactory' */
    cpy_r_r102 = PyDict_SetItem(cpy_r_r100, cpy_r_r101, cpy_r_r99);
    CPy_DECREF(cpy_r_r99);
    cpy_r_r103 = cpy_r_r102 >= 0;
    if (unlikely(!cpy_r_r103)) {
        CPy_AddTraceback("faster_web3/_utils/datatypes.py", "<module>", 36, CPyStatic_datatypes___globals);
        goto CPyL37;
    }
    cpy_r_r104 = (PyObject *)CPyType_datatypes___PropertyCheckingFactory;
    return 1;
CPyL37: ;
    cpy_r_r105 = 2;
    return cpy_r_r105;
CPyL38: ;
    CPy_DecRef(cpy_r_r45);
    goto CPyL37;
CPyL39: ;
    CPy_DecRef(cpy_r_r45);
    CPy_DecRef(cpy_r_r57);
    goto CPyL37;
CPyL40: ;
    CPy_DecRef(cpy_r_r45);
    CPy_DecRef(cpy_r_r57);
    CPy_DecRef(cpy_r_r59);
    goto CPyL37;
CPyL41: ;
    CPy_DecRef(cpy_r_r45);
    CPy_DecRef(cpy_r_r57);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r64);
    goto CPyL37;
CPyL42: ;
    CPy_DecRef(cpy_r_r88);
    goto CPyL37;
}
static PyMethodDef httpmodule_methods[] = {
    {"construct_user_agent", (PyCFunction)CPyPy_http___construct_user_agent, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("construct_user_agent(module, class_name)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___http(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___http__internal, "__name__");
    CPyStatic_http___globals = PyModule_GetDict(CPyModule_faster_web3____utils___http__internal);
    if (unlikely(CPyStatic_http___globals == NULL))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_http_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___http__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef httpmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.http",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    httpmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___http(void)
{
    if (CPyModule_faster_web3____utils___http__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___http__internal);
        return CPyModule_faster_web3____utils___http__internal;
    }
    CPyModule_faster_web3____utils___http__internal = PyModule_Create(&httpmodule);
    if (unlikely(CPyModule_faster_web3____utils___http__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___http(CPyModule_faster_web3____utils___http__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___http__internal;
    fail:
    return NULL;
}

PyObject *CPyDef_http___construct_user_agent(PyObject *cpy_r_module, PyObject *cpy_r_class_name) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    PyObject *cpy_r_r13;
    cpy_r_r0 = CPyStatics[81]; /* ('__version__',) */
    cpy_r_r1 = CPyStatics[82]; /* ('web3_version',) */
    cpy_r_r2 = CPyStatics[44]; /* 'faster_web3' */
    cpy_r_r3 = CPyStatic_http___globals;
    cpy_r_r4 = CPyImport_ImportFromMany(cpy_r_r2, cpy_r_r0, cpy_r_r1, cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "construct_user_agent", 11, CPyStatic_http___globals);
        goto CPyL5;
    }
    CPyModule_faster_web3 = cpy_r_r4;
    CPy_INCREF(CPyModule_faster_web3);
    CPy_DECREF(cpy_r_r4);
    cpy_r_r5 = CPyStatics[45]; /* 'faster_web3.py/' */
    cpy_r_r6 = CPyStatic_http___globals;
    cpy_r_r7 = CPyStatics[43]; /* 'web3_version' */
    cpy_r_r8 = CPyDict_GetItem(cpy_r_r6, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "construct_user_agent", 15, CPyStatic_http___globals);
        goto CPyL5;
    }
    if (likely(PyUnicode_Check(cpy_r_r8)))
        cpy_r_r9 = cpy_r_r8;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/http.py", "construct_user_agent", 15, CPyStatic_http___globals, "str", cpy_r_r8);
        goto CPyL5;
    }
    cpy_r_r10 = CPyStatics[46]; /* '/' */
    cpy_r_r11 = CPyStatics[47]; /* '.' */
    cpy_r_r12 = CPyStr_Build(6, cpy_r_r5, cpy_r_r9, cpy_r_r10, cpy_r_module, cpy_r_r11, cpy_r_class_name);
    CPy_DECREF(cpy_r_r9);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "construct_user_agent", 15, CPyStatic_http___globals);
        goto CPyL5;
    }
    return cpy_r_r12;
CPyL5: ;
    cpy_r_r13 = NULL;
    return cpy_r_r13;
}

PyObject *CPyPy_http___construct_user_agent(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"module", "class_name", 0};
    static CPyArg_Parser parser = {"OO:construct_user_agent", kwlist, 0};
    PyObject *obj_module;
    PyObject *obj_class_name;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_module, &obj_class_name)) {
        return NULL;
    }
    PyObject *arg_module;
    if (likely(PyUnicode_Check(obj_module)))
        arg_module = obj_module;
    else {
        CPy_TypeError("str", obj_module); 
        goto fail;
    }
    PyObject *arg_class_name;
    if (likely(PyUnicode_Check(obj_class_name)))
        arg_class_name = obj_class_name;
    else {
        CPy_TypeError("str", obj_class_name); 
        goto fail;
    }
    PyObject *retval = CPyDef_http___construct_user_agent(arg_module, arg_class_name);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/http.py", "construct_user_agent", 7, CPyStatic_http___globals);
    return NULL;
}

char CPyDef_http_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    int32_t cpy_r_r12;
    char cpy_r_r13;
    char cpy_r_r14;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "<module>", -1, CPyStatic_http___globals);
        goto CPyL6;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[83]; /* ('Final',) */
    cpy_r_r6 = CPyStatics[22]; /* 'typing' */
    cpy_r_r7 = CPyStatic_http___globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "<module>", 1, CPyStatic_http___globals);
        goto CPyL6;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = CPyStatic_http___globals;
    cpy_r_r10 = CPyStatics[48]; /* 'DEFAULT_HTTP_TIMEOUT' */
    cpy_r_r11 = PyFloat_FromDouble(30.0);
    cpy_r_r12 = CPyDict_SetItem(cpy_r_r9, cpy_r_r10, cpy_r_r11);
    CPy_DECREF(cpy_r_r11);
    cpy_r_r13 = cpy_r_r12 >= 0;
    if (unlikely(!cpy_r_r13)) {
        CPy_AddTraceback("faster_web3/_utils/http.py", "<module>", 4, CPyStatic_http___globals);
        goto CPyL6;
    }
    return 1;
CPyL6: ;
    cpy_r_r14 = 2;
    return cpy_r_r14;
}
static PyMethodDef mathmodule_methods[] = {
    {"percentile", (PyCFunction)CPyPy_math___percentile, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("percentile(values, percentile)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___math(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___math__internal, "__name__");
    CPyStatic_math___globals = PyModule_GetDict(CPyModule_faster_web3____utils___math__internal);
    if (unlikely(CPyStatic_math___globals == NULL))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_math_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___math__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef mathmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.math",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    mathmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___math(void)
{
    if (CPyModule_faster_web3____utils___math__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___math__internal);
        return CPyModule_faster_web3____utils___math__internal;
    }
    CPyModule_faster_web3____utils___math__internal = PyModule_Create(&mathmodule);
    if (unlikely(CPyModule_faster_web3____utils___math__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___math(CPyModule_faster_web3____utils___math__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___math__internal;
    fail:
    return NULL;
}

double CPyDef_math___percentile(PyObject *cpy_r_values, double cpy_r_percentile) {
    int32_t cpy_r_r0;
    char cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject **cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    CPyPtr cpy_r_r13;
    CPyPtr cpy_r_r14;
    CPyPtr cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject **cpy_r_r21;
    PyObject *cpy_r_r22;
    char cpy_r_r23;
    char cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject **cpy_r_r30;
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    CPyTagged cpy_r_r33;
    double cpy_r_r34;
    char cpy_r_r35;
    double cpy_r_r36;
    double cpy_r_r37;
    double cpy_r_r38;
    char cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject *cpy_r_r41;
    CPyTagged cpy_r_r42;
    double cpy_r_r43;
    char cpy_r_r44;
    PyObject *cpy_r_r45;
    double cpy_r_r46;
    double cpy_r_r47;
    char cpy_r_r48;
    char cpy_r_r49;
    char cpy_r_r50;
    char cpy_r_r51;
    double cpy_r_r52;
    double cpy_r_r53;
    double cpy_r_fractional;
    char cpy_r_r54;
    CPyTagged cpy_r_r55;
    PyObject *cpy_r_r56;
    CPyTagged cpy_r_r57;
    double cpy_r_r58;
    char cpy_r_r59;
    PyObject *cpy_r_r60;
    double cpy_r_r61;
    CPyTagged cpy_r_r62;
    PyObject *cpy_r_r63;
    CPyTagged cpy_r_r64;
    CPyTagged cpy_r_r65;
    PyObject *cpy_r_r66;
    CPyTagged cpy_r_r67;
    CPyTagged cpy_r_r68;
    double cpy_r_r69;
    char cpy_r_r70;
    double cpy_r_r71;
    double cpy_r_r72;
    char cpy_r_r73;
    PyObject *cpy_r_r74;
    double cpy_r_r75;
    PyObject *cpy_r_r76;
    double cpy_r_r77;
    cpy_r_r0 = PyObject_IsTrue(cpy_r_values);
    cpy_r_r1 = cpy_r_r0 >= 0;
    if (unlikely(!cpy_r_r1)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 11, CPyStatic_math___globals);
        goto CPyL47;
    }
    cpy_r_r2 = cpy_r_r0;
    if (cpy_r_r2) goto CPyL10;
    cpy_r_r3 = CPyStatics[49]; /* '' */
    cpy_r_r4 = CPyStatics[50]; /* 'Expected a sequence of at least 1 integers, got ' */
    cpy_r_r5 = CPyStatics[51]; /* '{!r:{}}' */
    cpy_r_r6 = CPyStatics[49]; /* '' */
    cpy_r_r7 = CPyStatics[52]; /* 'format' */
    PyObject *cpy_r_r8[3] = {cpy_r_r5, cpy_r_values, cpy_r_r6};
    cpy_r_r9 = (PyObject **)&cpy_r_r8;
    cpy_r_r10 = PyObject_VectorcallMethod(cpy_r_r7, cpy_r_r9, 9223372036854775811ULL, 0);
    if (unlikely(cpy_r_r10 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 15, CPyStatic_math___globals);
        goto CPyL47;
    }
    if (likely(PyUnicode_Check(cpy_r_r10)))
        cpy_r_r11 = cpy_r_r10;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/math.py", "percentile", 15, CPyStatic_math___globals, "str", cpy_r_r10);
        goto CPyL47;
    }
    cpy_r_r12 = PyList_New(2);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 15, CPyStatic_math___globals);
        goto CPyL48;
    }
    cpy_r_r13 = (CPyPtr)&((PyListObject *)cpy_r_r12)->ob_item;
    cpy_r_r14 = *(CPyPtr *)cpy_r_r13;
    CPy_INCREF(cpy_r_r4);
    *(PyObject * *)cpy_r_r14 = cpy_r_r4;
    cpy_r_r15 = cpy_r_r14 + 8;
    *(PyObject * *)cpy_r_r15 = cpy_r_r11;
    cpy_r_r16 = PyUnicode_Join(cpy_r_r3, cpy_r_r12);
    CPy_DECREF_NO_IMM(cpy_r_r12);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 15, CPyStatic_math___globals);
        goto CPyL47;
    }
    cpy_r_r17 = CPyStatic_math___globals;
    cpy_r_r18 = CPyStatics[53]; /* 'InsufficientData' */
    cpy_r_r19 = CPyDict_GetItem(cpy_r_r17, cpy_r_r18);
    if (unlikely(cpy_r_r19 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 14, CPyStatic_math___globals);
        goto CPyL49;
    }
    PyObject *cpy_r_r20[1] = {cpy_r_r16};
    cpy_r_r21 = (PyObject **)&cpy_r_r20;
    cpy_r_r22 = PyObject_Vectorcall(cpy_r_r19, cpy_r_r21, 1, 0);
    CPy_DECREF(cpy_r_r19);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 14, CPyStatic_math___globals);
        goto CPyL49;
    }
    CPy_DECREF(cpy_r_r16);
    CPy_Raise(cpy_r_r22);
    CPy_DECREF(cpy_r_r22);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 14, CPyStatic_math___globals);
        goto CPyL47;
    }
    CPy_Unreachable();
CPyL10: ;
    cpy_r_r23 = cpy_r_percentile < 0.0;
    if (cpy_r_r23) goto CPyL12;
    cpy_r_r24 = cpy_r_percentile > 100.0;
    if (!cpy_r_r24) goto CPyL16;
CPyL12: ;
    cpy_r_r25 = CPyStatics[54]; /* 'percentile must be in the range [0, 100]' */
    cpy_r_r26 = CPyStatic_math___globals;
    cpy_r_r27 = CPyStatics[55]; /* 'Web3ValueError' */
    cpy_r_r28 = CPyDict_GetItem(cpy_r_r26, cpy_r_r27);
    if (unlikely(cpy_r_r28 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 18, CPyStatic_math___globals);
        goto CPyL47;
    }
    PyObject *cpy_r_r29[1] = {cpy_r_r25};
    cpy_r_r30 = (PyObject **)&cpy_r_r29;
    cpy_r_r31 = PyObject_Vectorcall(cpy_r_r28, cpy_r_r30, 1, 0);
    CPy_DECREF(cpy_r_r28);
    if (unlikely(cpy_r_r31 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 18, CPyStatic_math___globals);
        goto CPyL47;
    }
    CPy_Raise(cpy_r_r31);
    CPy_DECREF(cpy_r_r31);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 18, CPyStatic_math___globals);
        goto CPyL47;
    }
    CPy_Unreachable();
CPyL16: ;
    cpy_r_r32 = CPySequence_Sort(cpy_r_values);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 20, CPyStatic_math___globals);
        goto CPyL47;
    }
    cpy_r_r33 = CPyObject_Size(cpy_r_values);
    if (unlikely(cpy_r_r33 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 22, CPyStatic_math___globals);
        goto CPyL50;
    }
    cpy_r_r34 = CPyFloat_FromTagged(cpy_r_r33);
    CPyTagged_DECREF(cpy_r_r33);
    cpy_r_r35 = cpy_r_r34 == -113.0;
    if (unlikely(cpy_r_r35)) goto CPyL20;
CPyL19: ;
    cpy_r_r36 = cpy_r_r34 * cpy_r_percentile;
    cpy_r_r37 = cpy_r_r36 / 100.0;
    cpy_r_r38 = cpy_r_r37 - 1.0;
    cpy_r_r39 = cpy_r_r38 < 0.0;
    if (cpy_r_r39) {
        goto CPyL21;
    } else
        goto CPyL26;
CPyL20: ;
    cpy_r_r40 = PyErr_Occurred();
    if (unlikely(cpy_r_r40 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 22, CPyStatic_math___globals);
        goto CPyL50;
    } else
        goto CPyL19;
CPyL21: ;
    cpy_r_r41 = CPyList_GetItemShort(cpy_r_r32, 0);
    CPy_DECREF_NO_IMM(cpy_r_r32);
    if (unlikely(cpy_r_r41 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 24, CPyStatic_math___globals);
        goto CPyL47;
    }
    if (likely(PyLong_Check(cpy_r_r41)))
        cpy_r_r42 = CPyTagged_FromObject(cpy_r_r41);
    else {
        CPy_TypeError("int", cpy_r_r41); cpy_r_r42 = CPY_INT_TAG;
    }
    CPy_DECREF(cpy_r_r41);
    if (unlikely(cpy_r_r42 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 24, CPyStatic_math___globals);
        goto CPyL47;
    }
    cpy_r_r43 = CPyFloat_FromTagged(cpy_r_r42);
    CPyTagged_DECREF(cpy_r_r42);
    cpy_r_r44 = cpy_r_r43 == -113.0;
    if (unlikely(cpy_r_r44)) goto CPyL25;
CPyL24: ;
    return cpy_r_r43;
CPyL25: ;
    cpy_r_r45 = PyErr_Occurred();
    if (unlikely(cpy_r_r45 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 24, CPyStatic_math___globals);
        goto CPyL47;
    } else
        goto CPyL24;
CPyL26: ;
    cpy_r_r46 = fmod(cpy_r_r38, 1.0);
    cpy_r_r47 = cpy_r_r46;
    cpy_r_r48 = cpy_r_r47 == 0.0;
    if (cpy_r_r48) goto CPyL29;
    cpy_r_r49 = cpy_r_r38 < 0.0;
    cpy_r_r50 = 1.0 < 0.0;
    cpy_r_r51 = cpy_r_r49 == cpy_r_r50;
    if (cpy_r_r51) goto CPyL30;
    cpy_r_r52 = cpy_r_r47 + 1.0;
    cpy_r_r47 = cpy_r_r52;
    goto CPyL30;
CPyL29: ;
    cpy_r_r53 = copysign(0.0, 1.0);
    cpy_r_r47 = cpy_r_r53;
CPyL30: ;
    cpy_r_fractional = cpy_r_r47;
    cpy_r_r54 = cpy_r_fractional == 0.0;
    if (!cpy_r_r54) goto CPyL37;
    cpy_r_r55 = CPyTagged_FromFloat(cpy_r_r38);
    if (unlikely(cpy_r_r55 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 28, CPyStatic_math___globals);
        goto CPyL50;
    }
    cpy_r_r56 = CPyList_GetItem(cpy_r_r32, cpy_r_r55);
    CPy_DECREF_NO_IMM(cpy_r_r32);
    CPyTagged_DECREF(cpy_r_r55);
    if (unlikely(cpy_r_r56 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 28, CPyStatic_math___globals);
        goto CPyL47;
    }
    if (likely(PyLong_Check(cpy_r_r56)))
        cpy_r_r57 = CPyTagged_FromObject(cpy_r_r56);
    else {
        CPy_TypeError("int", cpy_r_r56); cpy_r_r57 = CPY_INT_TAG;
    }
    CPy_DECREF(cpy_r_r56);
    if (unlikely(cpy_r_r57 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 28, CPyStatic_math___globals);
        goto CPyL47;
    }
    cpy_r_r58 = CPyFloat_FromTagged(cpy_r_r57);
    CPyTagged_DECREF(cpy_r_r57);
    cpy_r_r59 = cpy_r_r58 == -113.0;
    if (unlikely(cpy_r_r59)) goto CPyL36;
CPyL35: ;
    return cpy_r_r58;
CPyL36: ;
    cpy_r_r60 = PyErr_Occurred();
    if (unlikely(cpy_r_r60 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 28, CPyStatic_math___globals);
        goto CPyL47;
    } else
        goto CPyL35;
CPyL37: ;
    cpy_r_r61 = cpy_r_r38 - cpy_r_fractional;
    cpy_r_r62 = CPyTagged_FromFloat(cpy_r_r61);
    if (unlikely(cpy_r_r62 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 30, CPyStatic_math___globals);
        goto CPyL50;
    }
    cpy_r_r63 = CPyList_GetItem(cpy_r_r32, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 31, CPyStatic_math___globals);
        goto CPyL51;
    }
    if (likely(PyLong_Check(cpy_r_r63)))
        cpy_r_r64 = CPyTagged_FromObject(cpy_r_r63);
    else {
        CPy_TypeError("int", cpy_r_r63); cpy_r_r64 = CPY_INT_TAG;
    }
    CPy_DECREF(cpy_r_r63);
    if (unlikely(cpy_r_r64 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 31, CPyStatic_math___globals);
        goto CPyL51;
    }
    cpy_r_r65 = CPyTagged_Add(cpy_r_r62, 2);
    CPyTagged_DECREF(cpy_r_r62);
    cpy_r_r66 = CPyList_GetItem(cpy_r_r32, cpy_r_r65);
    CPy_DECREF_NO_IMM(cpy_r_r32);
    CPyTagged_DECREF(cpy_r_r65);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 32, CPyStatic_math___globals);
        goto CPyL52;
    }
    if (likely(PyLong_Check(cpy_r_r66)))
        cpy_r_r67 = CPyTagged_FromObject(cpy_r_r66);
    else {
        CPy_TypeError("int", cpy_r_r66); cpy_r_r67 = CPY_INT_TAG;
    }
    CPy_DECREF(cpy_r_r66);
    if (unlikely(cpy_r_r67 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 32, CPyStatic_math___globals);
        goto CPyL52;
    }
    cpy_r_r68 = CPyTagged_Subtract(cpy_r_r67, cpy_r_r64);
    CPyTagged_DECREF(cpy_r_r67);
    cpy_r_r69 = CPyFloat_FromTagged(cpy_r_r68);
    CPyTagged_DECREF(cpy_r_r68);
    cpy_r_r70 = cpy_r_r69 == -113.0;
    if (unlikely(cpy_r_r70)) goto CPyL44;
CPyL43: ;
    cpy_r_r71 = cpy_r_fractional * cpy_r_r69;
    cpy_r_r72 = CPyFloat_FromTagged(cpy_r_r64);
    CPyTagged_DECREF(cpy_r_r64);
    cpy_r_r73 = cpy_r_r72 == -113.0;
    if (unlikely(cpy_r_r73)) {
        goto CPyL46;
    } else
        goto CPyL45;
CPyL44: ;
    cpy_r_r74 = PyErr_Occurred();
    if (unlikely(cpy_r_r74 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 33, CPyStatic_math___globals);
        goto CPyL52;
    } else
        goto CPyL43;
CPyL45: ;
    cpy_r_r75 = cpy_r_r72 + cpy_r_r71;
    return cpy_r_r75;
CPyL46: ;
    cpy_r_r76 = PyErr_Occurred();
    if (unlikely(cpy_r_r76 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 33, CPyStatic_math___globals);
    } else
        goto CPyL45;
CPyL47: ;
    cpy_r_r77 = -113.0;
    return cpy_r_r77;
CPyL48: ;
    CPy_DecRef(cpy_r_r11);
    goto CPyL47;
CPyL49: ;
    CPy_DecRef(cpy_r_r16);
    goto CPyL47;
CPyL50: ;
    CPy_DecRef(cpy_r_r32);
    goto CPyL47;
CPyL51: ;
    CPy_DecRef(cpy_r_r32);
    CPyTagged_DecRef(cpy_r_r62);
    goto CPyL47;
CPyL52: ;
    CPyTagged_DecRef(cpy_r_r64);
    goto CPyL47;
}

PyObject *CPyPy_math___percentile(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"values", "percentile", 0};
    static CPyArg_Parser parser = {"OO:percentile", kwlist, 0};
    PyObject *obj_values;
    PyObject *obj_percentile;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_values, &obj_percentile)) {
        return NULL;
    }
    PyObject *arg_values = obj_values;
    double arg_percentile;
    arg_percentile = PyFloat_AsDouble(obj_percentile);
    if (arg_percentile == -1.0 && PyErr_Occurred()) {
        CPy_TypeError("float", obj_percentile); goto fail;
    }
    double retval = CPyDef_math___percentile(arg_values, arg_percentile);
    if (retval == -113.0 && PyErr_Occurred()) {
        return NULL;
    }
    PyObject *retbox = PyFloat_FromDouble(retval);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/math.py", "percentile", 11, CPyStatic_math___globals);
    return NULL;
}

char CPyDef_math_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    char cpy_r_r13;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "<module>", -1, CPyStatic_math___globals);
        goto CPyL6;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[84]; /* ('Sequence',) */
    cpy_r_r6 = CPyStatics[22]; /* 'typing' */
    cpy_r_r7 = CPyStatic_math___globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "<module>", 1, CPyStatic_math___globals);
        goto CPyL6;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = CPyStatics[85]; /* ('InsufficientData', 'Web3ValueError') */
    cpy_r_r10 = CPyStatics[29]; /* 'faster_web3.exceptions' */
    cpy_r_r11 = CPyStatic_math___globals;
    cpy_r_r12 = CPyImport_ImportFromMany(cpy_r_r10, cpy_r_r9, cpy_r_r9, cpy_r_r11);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/math.py", "<module>", 5, CPyStatic_math___globals);
        goto CPyL6;
    }
    CPyModule_faster_web3___exceptions = cpy_r_r12;
    CPy_INCREF(CPyModule_faster_web3___exceptions);
    CPy_DECREF(cpy_r_r12);
    return 1;
CPyL6: ;
    cpy_r_r13 = 2;
    return cpy_r_r13;
}
static PyMethodDef type_conversionmodule_methods[] = {
    {"to_hex_if_bytes", (PyCFunction)CPyPy_type_conversion___to_hex_if_bytes, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("to_hex_if_bytes(val)\n--\n\n") /* docstring */},
    {"to_bytes_if_hex", (PyCFunction)CPyPy_type_conversion___to_bytes_if_hex, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("to_bytes_if_hex(val)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___type_conversion(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___type_conversion__internal, "__name__");
    CPyStatic_type_conversion___globals = PyModule_GetDict(CPyModule_faster_web3____utils___type_conversion__internal);
    if (unlikely(CPyStatic_type_conversion___globals == NULL))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_type_conversion_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___type_conversion__internal);
    Py_CLEAR(modname);
    CPy_XDECREF(CPyStatic_type_conversion___to_bytes);
    CPyStatic_type_conversion___to_bytes = NULL;
    CPy_XDECREF(CPyStatic_type_conversion___to_hex);
    CPyStatic_type_conversion___to_hex = NULL;
    return -1;
}
static struct PyModuleDef type_conversionmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.type_conversion",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    type_conversionmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___type_conversion(void)
{
    if (CPyModule_faster_web3____utils___type_conversion__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___type_conversion__internal);
        return CPyModule_faster_web3____utils___type_conversion__internal;
    }
    CPyModule_faster_web3____utils___type_conversion__internal = PyModule_Create(&type_conversionmodule);
    if (unlikely(CPyModule_faster_web3____utils___type_conversion__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___type_conversion(CPyModule_faster_web3____utils___type_conversion__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___type_conversion__internal;
    fail:
    return NULL;
}

PyObject *CPyDef_type_conversion___to_hex_if_bytes(PyObject *cpy_r_val) {
    char cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    int32_t cpy_r_r3;
    char cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject **cpy_r_r12;
    PyObject *cpy_r_r13;
    PyObject *cpy_r_r14;
    PyObject *cpy_r_r15;
    CPyPtr cpy_r_r16;
    CPyPtr cpy_r_r17;
    CPyPtr cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject **cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    char cpy_r_r28;
    PyObject **cpy_r_r30;
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    tuple_T2OO cpy_r_r38;
    PyObject *cpy_r_r39;
    int32_t cpy_r_r40;
    char cpy_r_r41;
    char cpy_r_r42;
    PyObject *cpy_r_r43;
    char cpy_r_r44;
    PyObject **cpy_r_r46;
    PyObject *cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    char cpy_r_r51;
    PyObject **cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject *cpy_r_r57;
    cpy_r_r0 = PyUnicode_Check(cpy_r_val);
    if (!cpy_r_r0) goto CPyL19;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r1 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 26, CPyStatic_type_conversion___globals, "str", cpy_r_val);
        goto CPyL35;
    }
    cpy_r_r2 = CPyStatics[57]; /* '0x' */
    cpy_r_r3 = CPyStr_Startswith(cpy_r_r1, cpy_r_r2);
    CPy_DECREF(cpy_r_r1);
    cpy_r_r4 = cpy_r_r3;
    if (cpy_r_r4) goto CPyL12;
    cpy_r_r5 = CPyStatics[49]; /* '' */
    cpy_r_r6 = CPyStatics[58]; /* 'Expected a hex string. Got: ' */
    cpy_r_r7 = CPyStatics[51]; /* '{!r:{}}' */
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r8 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals, "str", cpy_r_val);
        goto CPyL35;
    }
    cpy_r_r9 = CPyStatics[49]; /* '' */
    cpy_r_r10 = CPyStatics[52]; /* 'format' */
    PyObject *cpy_r_r11[3] = {cpy_r_r7, cpy_r_r8, cpy_r_r9};
    cpy_r_r12 = (PyObject **)&cpy_r_r11;
    cpy_r_r13 = PyObject_VectorcallMethod(cpy_r_r10, cpy_r_r12, 9223372036854775811ULL, 0);
    if (unlikely(cpy_r_r13 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL36;
    }
    CPy_DECREF(cpy_r_r8);
    if (likely(PyUnicode_Check(cpy_r_r13)))
        cpy_r_r14 = cpy_r_r13;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals, "str", cpy_r_r13);
        goto CPyL35;
    }
    cpy_r_r15 = PyList_New(2);
    if (unlikely(cpy_r_r15 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL37;
    }
    cpy_r_r16 = (CPyPtr)&((PyListObject *)cpy_r_r15)->ob_item;
    cpy_r_r17 = *(CPyPtr *)cpy_r_r16;
    CPy_INCREF(cpy_r_r6);
    *(PyObject * *)cpy_r_r17 = cpy_r_r6;
    cpy_r_r18 = cpy_r_r17 + 8;
    *(PyObject * *)cpy_r_r18 = cpy_r_r14;
    cpy_r_r19 = PyUnicode_Join(cpy_r_r5, cpy_r_r15);
    CPy_DECREF_NO_IMM(cpy_r_r15);
    if (unlikely(cpy_r_r19 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    cpy_r_r20 = CPyStatic_type_conversion___globals;
    cpy_r_r21 = CPyStatics[55]; /* 'Web3ValueError' */
    cpy_r_r22 = CPyDict_GetItem(cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL38;
    }
    PyObject *cpy_r_r23[1] = {cpy_r_r19};
    cpy_r_r24 = (PyObject **)&cpy_r_r23;
    cpy_r_r25 = PyObject_Vectorcall(cpy_r_r22, cpy_r_r24, 1, 0);
    CPy_DECREF(cpy_r_r22);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL38;
    }
    CPy_DECREF(cpy_r_r19);
    CPy_Raise(cpy_r_r25);
    CPy_DECREF(cpy_r_r25);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    CPy_Unreachable();
CPyL12: ;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r26 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_type_conversion___globals, "str", cpy_r_val);
        goto CPyL35;
    }
    cpy_r_r27 = CPyStatic_type_conversion___to_hex;
    if (unlikely(cpy_r_r27 == NULL)) {
        goto CPyL39;
    } else
        goto CPyL16;
CPyL14: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r28 = 0;
    if (unlikely(!cpy_r_r28)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    CPy_Unreachable();
CPyL16: ;
    PyObject *cpy_r_r29[1] = {cpy_r_r26};
    cpy_r_r30 = (PyObject **)&cpy_r_r29;
    cpy_r_r31 = CPyStatics[86]; /* ('hexstr',) */
    cpy_r_r32 = PyObject_Vectorcall(cpy_r_r27, cpy_r_r30, 0, cpy_r_r31);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_type_conversion___globals);
        goto CPyL40;
    }
    CPy_DECREF(cpy_r_r26);
    if (likely(PyUnicode_Check(cpy_r_r32)))
        cpy_r_r33 = cpy_r_r32;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_type_conversion___globals, "str", cpy_r_r32);
        goto CPyL35;
    }
    return cpy_r_r33;
CPyL19: ;
    cpy_r_r34 = (PyObject *)&PyBytes_Type;
    cpy_r_r35 = CPyModule_builtins;
    cpy_r_r36 = CPyStatics[60]; /* 'bytearray' */
    cpy_r_r37 = CPyObject_GetAttr(cpy_r_r35, cpy_r_r36);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    CPy_INCREF(cpy_r_r34);
    cpy_r_r38.f0 = cpy_r_r34;
    cpy_r_r38.f1 = cpy_r_r37;
    cpy_r_r39 = PyTuple_New(2);
    if (unlikely(cpy_r_r39 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp8 = cpy_r_r38.f0;
    PyTuple_SET_ITEM(cpy_r_r39, 0, __tmp8);
    PyObject *__tmp9 = cpy_r_r38.f1;
    PyTuple_SET_ITEM(cpy_r_r39, 1, __tmp9);
    cpy_r_r40 = PyObject_IsInstance(cpy_r_val, cpy_r_r39);
    CPy_DECREF(cpy_r_r39);
    cpy_r_r41 = cpy_r_r40 >= 0;
    if (unlikely(!cpy_r_r41)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    cpy_r_r42 = cpy_r_r40;
    if (!cpy_r_r42) goto CPyL28;
    cpy_r_r43 = CPyStatic_type_conversion___to_hex;
    if (likely(cpy_r_r43 != NULL)) goto CPyL25;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r44 = 0;
    if (unlikely(!cpy_r_r44)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    CPy_Unreachable();
CPyL25: ;
    PyObject *cpy_r_r45[1] = {cpy_r_val};
    cpy_r_r46 = (PyObject **)&cpy_r_r45;
    cpy_r_r47 = PyObject_Vectorcall(cpy_r_r43, cpy_r_r46, 1, 0);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    if (likely(PyUnicode_Check(cpy_r_r47)))
        cpy_r_r48 = cpy_r_r47;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals, "str", cpy_r_r47);
        goto CPyL35;
    }
    cpy_r_r49 = cpy_r_r48;
    goto CPyL34;
CPyL28: ;
    cpy_r_r50 = CPyStatic_type_conversion___to_hex;
    if (likely(cpy_r_r50 != NULL)) goto CPyL31;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r51 = 0;
    if (unlikely(!cpy_r_r51)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    CPy_Unreachable();
CPyL31: ;
    PyObject *cpy_r_r52[1] = {cpy_r_val};
    cpy_r_r53 = (PyObject **)&cpy_r_r52;
    cpy_r_r54 = CPyStatics[86]; /* ('hexstr',) */
    cpy_r_r55 = PyObject_Vectorcall(cpy_r_r50, cpy_r_r53, 0, cpy_r_r54);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals);
        goto CPyL35;
    }
    if (likely(PyUnicode_Check(cpy_r_r55)))
        cpy_r_r56 = cpy_r_r55;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_type_conversion___globals, "str", cpy_r_r55);
        goto CPyL35;
    }
    cpy_r_r49 = cpy_r_r56;
CPyL34: ;
    return cpy_r_r49;
CPyL35: ;
    cpy_r_r57 = NULL;
    return cpy_r_r57;
CPyL36: ;
    CPy_DecRef(cpy_r_r8);
    goto CPyL35;
CPyL37: ;
    CPy_DecRef(cpy_r_r14);
    goto CPyL35;
CPyL38: ;
    CPy_DecRef(cpy_r_r19);
    goto CPyL35;
CPyL39: ;
    CPy_DecRef(cpy_r_r26);
    goto CPyL14;
CPyL40: ;
    CPy_DecRef(cpy_r_r26);
    goto CPyL35;
}

PyObject *CPyPy_type_conversion___to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"val", 0};
    static CPyArg_Parser parser = {"O:to_hex_if_bytes", kwlist, 0};
    PyObject *obj_val;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_val)) {
        return NULL;
    }
    PyObject *arg_val;
    if (PyUnicode_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL10;
    if (PyBytes_Check(obj_val) || PyByteArray_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL10;
    arg_val = obj_val;
    if (arg_val != NULL) goto __LL10;
    CPy_TypeError("union[str, bytes, object]", obj_val); 
    goto fail;
__LL10: ;
    PyObject *retval = CPyDef_type_conversion___to_hex_if_bytes(arg_val);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 20, CPyStatic_type_conversion___globals);
    return NULL;
}

PyObject *CPyDef_type_conversion___to_bytes_if_hex(PyObject *cpy_r_val) {
    char cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    char cpy_r_r3;
    PyObject **cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    cpy_r_r0 = PyUnicode_Check(cpy_r_val);
    if (!cpy_r_r0) goto CPyL8;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r1 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_type_conversion___globals, "str", cpy_r_val);
        goto CPyL11;
    }
    cpy_r_r2 = CPyStatic_type_conversion___to_bytes;
    if (unlikely(cpy_r_r2 == NULL)) {
        goto CPyL12;
    } else
        goto CPyL5;
CPyL3: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_bytes\" was not set");
    cpy_r_r3 = 0;
    if (unlikely(!cpy_r_r3)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_type_conversion___globals);
        goto CPyL11;
    }
    CPy_Unreachable();
CPyL5: ;
    PyObject *cpy_r_r4[1] = {cpy_r_r1};
    cpy_r_r5 = (PyObject **)&cpy_r_r4;
    cpy_r_r6 = CPyStatics[86]; /* ('hexstr',) */
    cpy_r_r7 = PyObject_Vectorcall(cpy_r_r2, cpy_r_r5, 0, cpy_r_r6);
    if (unlikely(cpy_r_r7 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_type_conversion___globals);
        goto CPyL13;
    }
    CPy_DECREF(cpy_r_r1);
    if (likely(PyBytes_Check(cpy_r_r7) || PyByteArray_Check(cpy_r_r7)))
        cpy_r_r8 = cpy_r_r7;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_type_conversion___globals, "bytes", cpy_r_r7);
        goto CPyL11;
    }
    cpy_r_r9 = cpy_r_r8;
    goto CPyL9;
CPyL8: ;
    CPy_INCREF(cpy_r_val);
    cpy_r_r9 = cpy_r_val;
CPyL9: ;
    if (likely(PyBytes_Check(cpy_r_r9) || PyByteArray_Check(cpy_r_r9)))
        cpy_r_r10 = cpy_r_r9;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_type_conversion___globals, "bytes", cpy_r_r9);
        goto CPyL11;
    }
    return cpy_r_r10;
CPyL11: ;
    cpy_r_r11 = NULL;
    return cpy_r_r11;
CPyL12: ;
    CPy_DecRef(cpy_r_r1);
    goto CPyL3;
CPyL13: ;
    CPy_DecRef(cpy_r_r1);
    goto CPyL11;
}

PyObject *CPyPy_type_conversion___to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"val", 0};
    static CPyArg_Parser parser = {"O:to_bytes_if_hex", kwlist, 0};
    PyObject *obj_val;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_val)) {
        return NULL;
    }
    PyObject *arg_val;
    if (PyUnicode_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL11;
    if (PyBytes_Check(obj_val) || PyByteArray_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL11;
    arg_val = obj_val;
    if (arg_val != NULL) goto __LL11;
    CPy_TypeError("union[str, bytes, object]", obj_val); 
    goto fail;
__LL11: ;
    PyObject *retval = CPyDef_type_conversion___to_bytes_if_hex(arg_val);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 33, CPyStatic_type_conversion___globals);
    return NULL;
}

char CPyDef_type_conversion_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject **cpy_r_r9;
    void *cpy_r_r11;
    void *cpy_r_r13;
    PyObject *cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    char cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject *cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject *cpy_r_r29;
    PyObject *cpy_r_r30;
    PyObject *cpy_r_r31;
    int32_t cpy_r_r32;
    char cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    int32_t cpy_r_r39;
    char cpy_r_r40;
    char cpy_r_r41;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", -1, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[87]; /* ('Final', 'Union') */
    cpy_r_r6 = CPyStatics[22]; /* 'typing' */
    cpy_r_r7 = CPyStatic_type_conversion___globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 1, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = (PyObject **)&CPyModule_faster_eth_utils;
    PyObject **cpy_r_r10[1] = {cpy_r_r9};
    cpy_r_r11 = (void *)&cpy_r_r10;
    int64_t cpy_r_r12[1] = {6};
    cpy_r_r13 = (void *)&cpy_r_r12;
    cpy_r_r14 = CPyStatics[88]; /* (('faster_eth_utils', 'faster_eth_utils',
                                    'faster_eth_utils'),) */
    cpy_r_r15 = CPyStatic_type_conversion___globals;
    cpy_r_r16 = CPyStatics[62]; /* 'faster_web3/_utils/type_conversion.py' */
    cpy_r_r17 = CPyStatics[26]; /* '<module>' */
    cpy_r_r18 = CPyImport_ImportMany(cpy_r_r14, cpy_r_r11, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r13);
    if (!cpy_r_r18) goto CPyL12;
    cpy_r_r19 = CPyStatics[89]; /* ('HexStr',) */
    cpy_r_r20 = CPyStatics[64]; /* 'eth_typing' */
    cpy_r_r21 = CPyStatic_type_conversion___globals;
    cpy_r_r22 = CPyImport_ImportFromMany(cpy_r_r20, cpy_r_r19, cpy_r_r19, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 7, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyModule_eth_typing = cpy_r_r22;
    CPy_INCREF(CPyModule_eth_typing);
    CPy_DECREF(cpy_r_r22);
    cpy_r_r23 = CPyStatics[90]; /* ('Web3ValueError',) */
    cpy_r_r24 = CPyStatics[29]; /* 'faster_web3.exceptions' */
    cpy_r_r25 = CPyStatic_type_conversion___globals;
    cpy_r_r26 = CPyImport_ImportFromMany(cpy_r_r24, cpy_r_r23, cpy_r_r23, cpy_r_r25);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 11, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyModule_faster_web3___exceptions = cpy_r_r26;
    CPy_INCREF(CPyModule_faster_web3___exceptions);
    CPy_DECREF(cpy_r_r26);
    cpy_r_r27 = CPyModule_faster_eth_utils;
    cpy_r_r28 = CPyStatics[65]; /* 'to_bytes' */
    cpy_r_r29 = CPyObject_GetAttr(cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 16, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyStatic_type_conversion___to_bytes = cpy_r_r29;
    CPy_INCREF(CPyStatic_type_conversion___to_bytes);
    cpy_r_r30 = CPyStatic_type_conversion___globals;
    cpy_r_r31 = CPyStatics[65]; /* 'to_bytes' */
    cpy_r_r32 = CPyDict_SetItem(cpy_r_r30, cpy_r_r31, cpy_r_r29);
    CPy_DECREF(cpy_r_r29);
    cpy_r_r33 = cpy_r_r32 >= 0;
    if (unlikely(!cpy_r_r33)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 16, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    cpy_r_r34 = CPyModule_faster_eth_utils;
    cpy_r_r35 = CPyStatics[66]; /* 'to_hex' */
    cpy_r_r36 = CPyObject_GetAttr(cpy_r_r34, cpy_r_r35);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 17, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    CPyStatic_type_conversion___to_hex = cpy_r_r36;
    CPy_INCREF(CPyStatic_type_conversion___to_hex);
    cpy_r_r37 = CPyStatic_type_conversion___globals;
    cpy_r_r38 = CPyStatics[66]; /* 'to_hex' */
    cpy_r_r39 = CPyDict_SetItem(cpy_r_r37, cpy_r_r38, cpy_r_r36);
    CPy_DECREF(cpy_r_r36);
    cpy_r_r40 = cpy_r_r39 >= 0;
    if (unlikely(!cpy_r_r40)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 17, CPyStatic_type_conversion___globals);
        goto CPyL12;
    }
    return 1;
CPyL12: ;
    cpy_r_r41 = 2;
    return cpy_r_r41;
}
static PyMethodDef utility_methodsmodule_methods[] = {
    {"all_in_dict", (PyCFunction)CPyPy_utility_methods___all_in_dict, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("all_in_dict(values, d)\n--\n\n") /* docstring */},
    {"any_in_dict", (PyCFunction)CPyPy_utility_methods___any_in_dict, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("any_in_dict(values, d)\n--\n\n") /* docstring */},
    {"none_in_dict", (PyCFunction)CPyPy_utility_methods___none_in_dict, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("none_in_dict(values, d)\n--\n\n") /* docstring */},
    {"either_set_is_a_subset", (PyCFunction)CPyPy_utility_methods___either_set_is_a_subset, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("either_set_is_a_subset(set1, set2, percentage=100)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___utility_methods(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___utility_methods__internal, "__name__");
    CPyStatic_utility_methods___globals = PyModule_GetDict(CPyModule_faster_web3____utils___utility_methods__internal);
    if (unlikely(CPyStatic_utility_methods___globals == NULL))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_utility_methods_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___utility_methods__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef utility_methodsmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.utility_methods",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    utility_methodsmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___utility_methods(void)
{
    if (CPyModule_faster_web3____utils___utility_methods__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___utility_methods__internal);
        return CPyModule_faster_web3____utils___utility_methods__internal;
    }
    CPyModule_faster_web3____utils___utility_methods__internal = PyModule_Create(&utility_methodsmodule);
    if (unlikely(CPyModule_faster_web3____utils___utility_methods__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___utility_methods(CPyModule_faster_web3____utils___utility_methods__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___utility_methods__internal;
    fail:
    return NULL;
}

char CPyDef_utility_methods___all_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d) {
    PyObject *cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    int32_t cpy_r_r5;
    char cpy_r_r6;
    char cpy_r_r7;
    char cpy_r_r8;
    char cpy_r_r9;
    char cpy_r_r10;
    cpy_r_r0 = CPyDict_FromAny(cpy_r_d);
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 27, CPyStatic_utility_methods___globals);
        goto CPyL9;
    }
    cpy_r_d = cpy_r_r0;
    cpy_r_r1 = 1;
    cpy_r_r2 = PyObject_GetIter(cpy_r_values);
    if (unlikely(cpy_r_r2 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 28, CPyStatic_utility_methods___globals);
        goto CPyL10;
    }
CPyL2: ;
    cpy_r_r3 = PyIter_Next(cpy_r_r2);
    if (cpy_r_r3 == NULL) goto CPyL11;
    CPy_INCREF(cpy_r_d);
    if (likely(PyDict_Check(cpy_r_d)))
        cpy_r_r4 = cpy_r_d;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 28, CPyStatic_utility_methods___globals, "dict", cpy_r_d);
        goto CPyL12;
    }
    cpy_r_r5 = PyDict_Contains(cpy_r_r4, cpy_r_r3);
    CPy_DECREF(cpy_r_r4);
    CPy_DECREF(cpy_r_r3);
    cpy_r_r6 = cpy_r_r5 >= 0;
    if (unlikely(!cpy_r_r6)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 28, CPyStatic_utility_methods___globals);
        goto CPyL13;
    }
    cpy_r_r7 = cpy_r_r5;
    cpy_r_r8 = cpy_r_r7 ^ 1;
    if (cpy_r_r8) {
        goto CPyL14;
    } else
        goto CPyL2;
CPyL6: ;
    cpy_r_r1 = 0;
    goto CPyL8;
CPyL7: ;
    cpy_r_r9 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 28, CPyStatic_utility_methods___globals);
        goto CPyL9;
    }
CPyL8: ;
    return cpy_r_r1;
CPyL9: ;
    cpy_r_r10 = 2;
    return cpy_r_r10;
CPyL10: ;
    CPy_DecRef(cpy_r_d);
    goto CPyL9;
CPyL11: ;
    CPy_DECREF(cpy_r_d);
    CPy_DECREF(cpy_r_r2);
    goto CPyL7;
CPyL12: ;
    CPy_DecRef(cpy_r_d);
    CPy_DecRef(cpy_r_r2);
    CPy_DecRef(cpy_r_r3);
    goto CPyL9;
CPyL13: ;
    CPy_DecRef(cpy_r_d);
    CPy_DecRef(cpy_r_r2);
    goto CPyL9;
CPyL14: ;
    CPy_DECREF(cpy_r_d);
    CPy_DECREF(cpy_r_r2);
    goto CPyL6;
}

PyObject *CPyPy_utility_methods___all_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"values", "d", 0};
    static CPyArg_Parser parser = {"OO:all_in_dict", kwlist, 0};
    PyObject *obj_values;
    PyObject *obj_d;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_values, &obj_d)) {
        return NULL;
    }
    PyObject *arg_values = obj_values;
    PyObject *arg_d;
    arg_d = obj_d;
    if (arg_d != NULL) goto __LL12;
    if (PyDict_Check(obj_d))
        arg_d = obj_d;
    else {
        arg_d = NULL;
    }
    if (arg_d != NULL) goto __LL12;
    CPy_TypeError("union[object, dict]", obj_d); 
    goto fail;
__LL12: ;
    char retval = CPyDef_utility_methods___all_in_dict(arg_values, arg_d);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "all_in_dict", 15, CPyStatic_utility_methods___globals);
    return NULL;
}

char CPyDef_utility_methods___any_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d) {
    PyObject *cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    int32_t cpy_r_r5;
    char cpy_r_r6;
    char cpy_r_r7;
    char cpy_r_r8;
    char cpy_r_r9;
    cpy_r_r0 = CPyDict_FromAny(cpy_r_d);
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 43, CPyStatic_utility_methods___globals);
        goto CPyL9;
    }
    cpy_r_d = cpy_r_r0;
    cpy_r_r1 = 0;
    cpy_r_r2 = PyObject_GetIter(cpy_r_values);
    if (unlikely(cpy_r_r2 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 44, CPyStatic_utility_methods___globals);
        goto CPyL10;
    }
CPyL2: ;
    cpy_r_r3 = PyIter_Next(cpy_r_r2);
    if (cpy_r_r3 == NULL) goto CPyL11;
    CPy_INCREF(cpy_r_d);
    if (likely(PyDict_Check(cpy_r_d)))
        cpy_r_r4 = cpy_r_d;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 44, CPyStatic_utility_methods___globals, "dict", cpy_r_d);
        goto CPyL12;
    }
    cpy_r_r5 = PyDict_Contains(cpy_r_r4, cpy_r_r3);
    CPy_DECREF(cpy_r_r4);
    CPy_DECREF(cpy_r_r3);
    cpy_r_r6 = cpy_r_r5 >= 0;
    if (unlikely(!cpy_r_r6)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 44, CPyStatic_utility_methods___globals);
        goto CPyL13;
    }
    cpy_r_r7 = cpy_r_r5;
    if (cpy_r_r7) {
        goto CPyL14;
    } else
        goto CPyL2;
CPyL6: ;
    cpy_r_r1 = 1;
    goto CPyL8;
CPyL7: ;
    cpy_r_r8 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r8)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 44, CPyStatic_utility_methods___globals);
        goto CPyL9;
    }
CPyL8: ;
    return cpy_r_r1;
CPyL9: ;
    cpy_r_r9 = 2;
    return cpy_r_r9;
CPyL10: ;
    CPy_DecRef(cpy_r_d);
    goto CPyL9;
CPyL11: ;
    CPy_DECREF(cpy_r_d);
    CPy_DECREF(cpy_r_r2);
    goto CPyL7;
CPyL12: ;
    CPy_DecRef(cpy_r_d);
    CPy_DecRef(cpy_r_r2);
    CPy_DecRef(cpy_r_r3);
    goto CPyL9;
CPyL13: ;
    CPy_DecRef(cpy_r_d);
    CPy_DecRef(cpy_r_r2);
    goto CPyL9;
CPyL14: ;
    CPy_DECREF(cpy_r_d);
    CPy_DECREF(cpy_r_r2);
    goto CPyL6;
}

PyObject *CPyPy_utility_methods___any_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"values", "d", 0};
    static CPyArg_Parser parser = {"OO:any_in_dict", kwlist, 0};
    PyObject *obj_values;
    PyObject *obj_d;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_values, &obj_d)) {
        return NULL;
    }
    PyObject *arg_values = obj_values;
    PyObject *arg_d;
    arg_d = obj_d;
    if (arg_d != NULL) goto __LL13;
    if (PyDict_Check(obj_d))
        arg_d = obj_d;
    else {
        arg_d = NULL;
    }
    if (arg_d != NULL) goto __LL13;
    CPy_TypeError("union[object, dict]", obj_d); 
    goto fail;
__LL13: ;
    char retval = CPyDef_utility_methods___any_in_dict(arg_values, arg_d);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "any_in_dict", 31, CPyStatic_utility_methods___globals);
    return NULL;
}

char CPyDef_utility_methods___none_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d) {
    char cpy_r_r0;
    char cpy_r_r1;
    char cpy_r_r2;
    cpy_r_r0 = CPyDef_utility_methods___any_in_dict(cpy_r_values, cpy_r_d);
    if (unlikely(cpy_r_r0 == 2)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "none_in_dict", 59, CPyStatic_utility_methods___globals);
        goto CPyL2;
    }
    cpy_r_r1 = cpy_r_r0 ^ 1;
    return cpy_r_r1;
CPyL2: ;
    cpy_r_r2 = 2;
    return cpy_r_r2;
}

PyObject *CPyPy_utility_methods___none_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"values", "d", 0};
    static CPyArg_Parser parser = {"OO:none_in_dict", kwlist, 0};
    PyObject *obj_values;
    PyObject *obj_d;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_values, &obj_d)) {
        return NULL;
    }
    PyObject *arg_values = obj_values;
    PyObject *arg_d;
    arg_d = obj_d;
    if (arg_d != NULL) goto __LL14;
    if (PyDict_Check(obj_d))
        arg_d = obj_d;
    else {
        arg_d = NULL;
    }
    if (arg_d != NULL) goto __LL14;
    CPy_TypeError("union[object, dict]", obj_d); 
    goto fail;
__LL14: ;
    char retval = CPyDef_utility_methods___none_in_dict(arg_values, arg_d);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "none_in_dict", 47, CPyStatic_utility_methods___globals);
    return NULL;
}

char CPyDef_utility_methods___either_set_is_a_subset(PyObject *cpy_r_set1, PyObject *cpy_r_set2, CPyTagged cpy_r_percentage) {
    double cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject **cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    CPyPtr cpy_r_r8;
    int64_t cpy_r_r9;
    CPyTagged cpy_r_r10;
    CPyPtr cpy_r_r11;
    int64_t cpy_r_r12;
    CPyTagged cpy_r_r13;
    PyObject *cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    double cpy_r_r17;
    char cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    char cpy_r_r23;
    char cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject **cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject *cpy_r_r29;
    CPyPtr cpy_r_r30;
    int64_t cpy_r_r31;
    CPyTagged cpy_r_r32;
    CPyPtr cpy_r_r33;
    int64_t cpy_r_r34;
    CPyTagged cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    double cpy_r_r39;
    char cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    char cpy_r_r45;
    char cpy_r_r46;
    if (cpy_r_percentage != CPY_INT_TAG) goto CPyL23;
    cpy_r_percentage = 200;
CPyL2: ;
    cpy_r_r0 = CPyTagged_TrueDivide(cpy_r_percentage, 200);
    CPyTagged_DECREF(cpy_r_percentage);
    cpy_r_r1 = cpy_r_r0 == -113.0;
    if (unlikely(cpy_r_r1)) goto CPyL4;
CPyL3: ;
    cpy_r_r2 = CPyStatics[67]; /* 'intersection' */
    PyObject *cpy_r_r3[2] = {cpy_r_set1, cpy_r_set2};
    cpy_r_r4 = (PyObject **)&cpy_r_r3;
    cpy_r_r5 = PyObject_VectorcallMethod(cpy_r_r2, cpy_r_r4, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r5 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL5;
CPyL4: ;
    cpy_r_r6 = PyErr_Occurred();
    if (unlikely(cpy_r_r6 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 79, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL3;
CPyL5: ;
    if (likely(PySet_Check(cpy_r_r5)))
        cpy_r_r7 = cpy_r_r5;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals, "set", cpy_r_r5);
        goto CPyL22;
    }
    cpy_r_r8 = (CPyPtr)&((PySetObject *)cpy_r_r7)->used;
    cpy_r_r9 = *(int64_t *)cpy_r_r8;
    CPy_DECREF(cpy_r_r7);
    cpy_r_r10 = cpy_r_r9 << 1;
    cpy_r_r11 = (CPyPtr)&((PySetObject *)cpy_r_set1)->used;
    cpy_r_r12 = *(int64_t *)cpy_r_r11;
    cpy_r_r13 = cpy_r_r12 << 1;
    cpy_r_r14 = CPyTagged_StealAsObject(cpy_r_r13);
    cpy_r_r15 = PyFloat_FromDouble(cpy_r_r0);
    cpy_r_r16 = PyNumber_Multiply(cpy_r_r14, cpy_r_r15);
    CPy_DECREF(cpy_r_r14);
    CPy_DECREF(cpy_r_r15);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals);
        goto CPyL22;
    }
    cpy_r_r17 = PyFloat_AsDouble(cpy_r_r16);
    if (cpy_r_r17 == -1.0 && PyErr_Occurred()) {
        CPy_TypeError("float", cpy_r_r16); cpy_r_r17 = -113.0;
    }
    CPy_DECREF(cpy_r_r16);
    cpy_r_r18 = cpy_r_r17 == -113.0;
    if (unlikely(cpy_r_r18)) goto CPyL9;
CPyL8: ;
    cpy_r_r19 = CPyTagged_StealAsObject(cpy_r_r10);
    cpy_r_r20 = PyFloat_FromDouble(cpy_r_r17);
    cpy_r_r21 = PyObject_RichCompare(cpy_r_r19, cpy_r_r20, 5);
    CPy_DECREF(cpy_r_r19);
    CPy_DECREF(cpy_r_r20);
    if (unlikely(cpy_r_r21 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL10;
CPyL9: ;
    cpy_r_r22 = PyErr_Occurred();
    if (unlikely(cpy_r_r22 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL8;
CPyL10: ;
    if (unlikely(!PyBool_Check(cpy_r_r21))) {
        CPy_TypeError("bool", cpy_r_r21); cpy_r_r23 = 2;
    } else
        cpy_r_r23 = cpy_r_r21 == Py_True;
    CPy_DECREF(cpy_r_r21);
    if (unlikely(cpy_r_r23 == 2)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 82, CPyStatic_utility_methods___globals);
        goto CPyL22;
    }
    if (!cpy_r_r23) goto CPyL13;
    cpy_r_r24 = cpy_r_r23;
    goto CPyL21;
CPyL13: ;
    cpy_r_r25 = CPyStatics[67]; /* 'intersection' */
    PyObject *cpy_r_r26[2] = {cpy_r_set2, cpy_r_set1};
    cpy_r_r27 = (PyObject **)&cpy_r_r26;
    cpy_r_r28 = PyObject_VectorcallMethod(cpy_r_r25, cpy_r_r27, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r28 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals);
        goto CPyL22;
    }
    if (likely(PySet_Check(cpy_r_r28)))
        cpy_r_r29 = cpy_r_r28;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals, "set", cpy_r_r28);
        goto CPyL22;
    }
    cpy_r_r30 = (CPyPtr)&((PySetObject *)cpy_r_r29)->used;
    cpy_r_r31 = *(int64_t *)cpy_r_r30;
    CPy_DECREF(cpy_r_r29);
    cpy_r_r32 = cpy_r_r31 << 1;
    cpy_r_r33 = (CPyPtr)&((PySetObject *)cpy_r_set2)->used;
    cpy_r_r34 = *(int64_t *)cpy_r_r33;
    cpy_r_r35 = cpy_r_r34 << 1;
    cpy_r_r36 = CPyTagged_StealAsObject(cpy_r_r35);
    cpy_r_r37 = PyFloat_FromDouble(cpy_r_r0);
    cpy_r_r38 = PyNumber_Multiply(cpy_r_r36, cpy_r_r37);
    CPy_DECREF(cpy_r_r36);
    CPy_DECREF(cpy_r_r37);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals);
        goto CPyL22;
    }
    cpy_r_r39 = PyFloat_AsDouble(cpy_r_r38);
    if (cpy_r_r39 == -1.0 && PyErr_Occurred()) {
        CPy_TypeError("float", cpy_r_r38); cpy_r_r39 = -113.0;
    }
    CPy_DECREF(cpy_r_r38);
    cpy_r_r40 = cpy_r_r39 == -113.0;
    if (unlikely(cpy_r_r40)) goto CPyL18;
CPyL17: ;
    cpy_r_r41 = CPyTagged_StealAsObject(cpy_r_r32);
    cpy_r_r42 = PyFloat_FromDouble(cpy_r_r39);
    cpy_r_r43 = PyObject_RichCompare(cpy_r_r41, cpy_r_r42, 5);
    CPy_DECREF(cpy_r_r41);
    CPy_DECREF(cpy_r_r42);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL19;
CPyL18: ;
    cpy_r_r44 = PyErr_Occurred();
    if (unlikely(cpy_r_r44 != NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals);
        goto CPyL22;
    } else
        goto CPyL17;
CPyL19: ;
    if (unlikely(!PyBool_Check(cpy_r_r43))) {
        CPy_TypeError("bool", cpy_r_r43); cpy_r_r45 = 2;
    } else
        cpy_r_r45 = cpy_r_r43 == Py_True;
    CPy_DECREF(cpy_r_r43);
    if (unlikely(cpy_r_r45 == 2)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 83, CPyStatic_utility_methods___globals);
        goto CPyL22;
    }
    cpy_r_r24 = cpy_r_r45;
CPyL21: ;
    return cpy_r_r24;
CPyL22: ;
    cpy_r_r46 = 2;
    return cpy_r_r46;
CPyL23: ;
    CPyTagged_INCREF(cpy_r_percentage);
    goto CPyL2;
}

PyObject *CPyPy_utility_methods___either_set_is_a_subset(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"set1", "set2", "percentage", 0};
    static CPyArg_Parser parser = {"OO|O:either_set_is_a_subset", kwlist, 0};
    PyObject *obj_set1;
    PyObject *obj_set2;
    PyObject *obj_percentage = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_set1, &obj_set2, &obj_percentage)) {
        return NULL;
    }
    PyObject *arg_set1;
    if (likely(PySet_Check(obj_set1)))
        arg_set1 = obj_set1;
    else {
        CPy_TypeError("set", obj_set1); 
        goto fail;
    }
    PyObject *arg_set2;
    if (likely(PySet_Check(obj_set2)))
        arg_set2 = obj_set2;
    else {
        CPy_TypeError("set", obj_set2); 
        goto fail;
    }
    CPyTagged arg_percentage;
    if (obj_percentage == NULL) {
        arg_percentage = CPY_INT_TAG;
    } else if (likely(PyLong_Check(obj_percentage)))
        arg_percentage = CPyTagged_BorrowFromObject(obj_percentage);
    else {
        CPy_TypeError("int", obj_percentage); goto fail;
    }
    char retval = CPyDef_utility_methods___either_set_is_a_subset(arg_set1, arg_set2, arg_percentage);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "either_set_is_a_subset", 62, CPyStatic_utility_methods___globals);
    return NULL;
}

char CPyDef_utility_methods_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    char cpy_r_r13;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "<module>", -1, CPyStatic_utility_methods___globals);
        goto CPyL6;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[91]; /* ('Any', 'Iterable', 'Mapping', 'Set', 'Union') */
    cpy_r_r6 = CPyStatics[22]; /* 'typing' */
    cpy_r_r7 = CPyStatic_utility_methods___globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "<module>", 1, CPyStatic_utility_methods___globals);
        goto CPyL6;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = CPyStatics[92]; /* ('TxData', 'TxParams') */
    cpy_r_r10 = CPyStatics[73]; /* 'faster_web3.types' */
    cpy_r_r11 = CPyStatic_utility_methods___globals;
    cpy_r_r12 = CPyImport_ImportFromMany(cpy_r_r10, cpy_r_r9, cpy_r_r9, cpy_r_r11);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/utility_methods.py", "<module>", 9, CPyStatic_utility_methods___globals);
        goto CPyL6;
    }
    CPyModule_faster_web3___types = cpy_r_r12;
    CPy_INCREF(CPyModule_faster_web3___types);
    CPy_DECREF(cpy_r_r12);
    return 1;
CPyL6: ;
    cpy_r_r13 = 2;
    return cpy_r_r13;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___datatypes = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_faster_eth_utils = Py_None;
    CPyModule_faster_eth_utils___toolz = Py_None;
    CPyModule_mypy_extensions = Py_None;
    CPyModule_faster_web3___exceptions = Py_None;
    CPyModule_faster_web3____utils___http = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_faster_web3 = Py_None;
    CPyModule_faster_web3____utils___math = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_faster_web3___exceptions = Py_None;
    CPyModule_faster_web3____utils___type_conversion = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_faster_eth_utils = Py_None;
    CPyModule_eth_typing = Py_None;
    CPyModule_faster_web3___exceptions = Py_None;
    CPyModule_faster_web3____utils___utility_methods = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_faster_web3___types = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[93];
const char * const CPyLit_Str[] = {
    "\003\tProperty \016 not found on \t class. `",
    "\001B.factory` only accepts keyword arguments which are present on the ",
    "\a\006 class\022Web3AttributeError\b__init__\a__mro__\b__dict__\004keys\a__new__",
    "\t\bbuiltins\003Any\nCollection\004Dict\005Final\bOptional\005Tuple\004Type\006typing",
    "\002\020faster_eth_utils\026faster_eth_utils.toolz",
    "\004\037faster_web3/_utils/datatypes.py\b<module>\nmypyc_attr\017mypy_extensions",
    "\004\026faster_web3.exceptions\030apply_formatters_to_dict\006concat\004type",
    "\004\v__prepare__\027PropertyCheckingFactory\fstaticmethod\017__annotations__",
    "\003\026mypyc filler docstring\a__doc__\034faster_web3._utils.datatypes",
    "\005\n__module__\fnative_class\v__version__\fweb3_version\vfaster_web3",
    "\005\017faster_web3.py/\001/\001.\024DEFAULT_HTTP_TIMEOUT\000",
    "\0030Expected a sequence of at least 1 integers, got \a{!r:{}}\006format",
    "\002\020InsufficientData(percentile must be in the range [0, 100]",
    "\005\016Web3ValueError\bSequence\0020x\034Expected a hex string. Got: \006hexstr",
    "\004\tbytearray\005Union%faster_web3/_utils/type_conversion.py\006HexStr",
    "\b\neth_typing\bto_bytes\006to_hex\fintersection\bIterable\aMapping\003Set\006TxData",
    "\002\bTxParams\021faster_web3.types",
    "",
};
const char * const CPyLit_Bytes[] = {
    "",
};
const char * const CPyLit_Int[] = {
    "",
};
const double CPyLit_Float[] = {0};
const double CPyLit_Complex[] = {0};
const int CPyLit_Tuple[] = {
    19, 7, 15, 16, 17, 18, 19, 20, 21, 3, 23, 23, 23, 3, 24, 23, 23, 2,
    75, 76, 1, 27, 1, 8, 1, 41, 1, 42, 1, 43, 1, 18, 1, 56, 2, 53, 55, 1,
    59, 2, 18, 61, 1, 75, 1, 63, 1, 55, 5, 15, 68, 69, 70, 61, 2, 71, 72
};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___datatypes__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___datatypes;
PyObject *CPyStatic_datatypes___globals;
CPyModule *CPyModule_builtins;
CPyModule *CPyModule_typing;
CPyModule *CPyModule_faster_eth_utils;
CPyModule *CPyModule_faster_eth_utils___toolz;
CPyModule *CPyModule_mypy_extensions;
CPyModule *CPyModule_faster_web3___exceptions;
CPyModule *CPyModule_faster_web3____utils___http__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___http;
PyObject *CPyStatic_http___globals;
CPyModule *CPyModule_faster_web3;
CPyModule *CPyModule_faster_web3____utils___math__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___math;
PyObject *CPyStatic_math___globals;
CPyModule *CPyModule_faster_web3____utils___type_conversion__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___type_conversion;
PyObject *CPyStatic_type_conversion___globals;
CPyModule *CPyModule_eth_typing;
CPyModule *CPyModule_faster_web3____utils___utility_methods__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___utility_methods;
PyObject *CPyStatic_utility_methods___globals;
CPyModule *CPyModule_faster_web3___types;
PyObject *CPyStatic_datatypes___apply_formatters_to_dict = NULL;
PyObject *CPyStatic_datatypes___concat = NULL;
PyTypeObject *CPyType_datatypes___PropertyCheckingFactory;
PyTypeObject *CPyType_datatypes_____init___3_PropertyCheckingFactory_obj;
PyObject *CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj(void);
CPyThreadLocal faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject *datatypes_____init___3_PropertyCheckingFactory_obj_free_instance;
PyTypeObject *CPyType_datatypes_____new___3_PropertyCheckingFactory_obj;
PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj(void);
CPyThreadLocal faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject *datatypes_____new___3_PropertyCheckingFactory_obj_free_instance;
char CPyDef_datatypes___verify_attr(PyObject *cpy_r_class_name, PyObject *cpy_r_key, PyObject *cpy_r_namespace);
PyObject *CPyPy_datatypes___verify_attr(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
PyObject *CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____get__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_datatypes_____init___3_PropertyCheckingFactory_obj_____call__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_cls, PyObject *cpy_r_name, PyObject *cpy_r_bases, PyObject *cpy_r_namespace, PyObject *cpy_r_kwargs);
PyObject *CPyPy_datatypes_____init___3_PropertyCheckingFactory_obj_____call__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_instance, PyObject *cpy_r_owner);
PyObject *CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____get__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_datatypes_____new___3_PropertyCheckingFactory_obj_____call__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_mcs, PyObject *cpy_r_name, tuple_T1O cpy_r_bases, PyObject *cpy_r_namespace, PyObject *cpy_r_normalizers);
PyObject *CPyPy_datatypes_____new___3_PropertyCheckingFactory_obj_____call__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_datatypes_____top_level__(void);
PyObject *CPyDef_http___construct_user_agent(PyObject *cpy_r_module, PyObject *cpy_r_class_name);
PyObject *CPyPy_http___construct_user_agent(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_http_____top_level__(void);
double CPyDef_math___percentile(PyObject *cpy_r_values, double cpy_r_percentile);
PyObject *CPyPy_math___percentile(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_math_____top_level__(void);
PyObject *CPyStatic_type_conversion___to_bytes = NULL;
PyObject *CPyStatic_type_conversion___to_hex = NULL;
PyObject *CPyDef_type_conversion___to_hex_if_bytes(PyObject *cpy_r_val);
PyObject *CPyPy_type_conversion___to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_type_conversion___to_bytes_if_hex(PyObject *cpy_r_val);
PyObject *CPyPy_type_conversion___to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_type_conversion_____top_level__(void);
char CPyDef_utility_methods___all_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d);
PyObject *CPyPy_utility_methods___all_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_utility_methods___any_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d);
PyObject *CPyPy_utility_methods___any_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_utility_methods___none_in_dict(PyObject *cpy_r_values, PyObject *cpy_r_d);
PyObject *CPyPy_utility_methods___none_in_dict(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_utility_methods___either_set_is_a_subset(PyObject *cpy_r_set1, PyObject *cpy_r_set2, CPyTagged cpy_r_percentage);
PyObject *CPyPy_utility_methods___either_set_is_a_subset(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_utility_methods_____top_level__(void);

static int exec_e60543e00a47358a5fd8__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___datatypes(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___datatypes, "e60543e00a47358a5fd8__mypyc.init_faster_web3____utils___datatypes", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___datatypes", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___http(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___http, "e60543e00a47358a5fd8__mypyc.init_faster_web3____utils___http", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___http", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___math(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___math, "e60543e00a47358a5fd8__mypyc.init_faster_web3____utils___math", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___math", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___type_conversion(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___type_conversion, "e60543e00a47358a5fd8__mypyc.init_faster_web3____utils___type_conversion", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___type_conversion", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___utility_methods(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___utility_methods, "e60543e00a47358a5fd8__mypyc.init_faster_web3____utils___utility_methods", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___utility_methods", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_e60543e00a47358a5fd8__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "e60543e00a47358a5fd8__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_e60543e00a47358a5fd8__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_e60543e00a47358a5fd8__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_e60543e00a47358a5fd8__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
