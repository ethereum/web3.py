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
#include "__native_211de080822a4a868b8f.h"
#include "__native_internal_211de080822a4a868b8f.h"

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
    cpy_r_r5 = CPyStatics[106]; /* ('Any', 'Collection', 'Dict', 'Final', 'Optional', 'Tuple',
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
    cpy_r_r15 = CPyStatics[109]; /* (('faster_eth_utils', 'faster_eth_utils',
                                     'faster_eth_utils'),
                                    ('faster_eth_utils.toolz', 'faster_eth_utils',
                                     'faster_eth_utils')) */
    cpy_r_r16 = CPyStatic_datatypes___globals;
    cpy_r_r17 = CPyStatics[25]; /* 'faster_web3/_utils/datatypes.py' */
    cpy_r_r18 = CPyStatics[26]; /* '<module>' */
    cpy_r_r19 = CPyImport_ImportMany(cpy_r_r15, cpy_r_r12, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r14);
    if (!cpy_r_r19) goto CPyL37;
    cpy_r_r20 = CPyStatics[110]; /* ('mypyc_attr',) */
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
    cpy_r_r24 = CPyStatics[111]; /* ('Web3AttributeError',) */
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
    cpy_r_r95 = CPyStatics[112]; /* ('native_class',) */
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
    cpy_r_r0 = CPyStatics[113]; /* ('__version__',) */
    cpy_r_r1 = CPyStatics[114]; /* ('web3_version',) */
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
    cpy_r_r5 = CPyStatics[115]; /* ('Final',) */
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
    cpy_r_r5 = CPyStatics[116]; /* ('Sequence',) */
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
    cpy_r_r9 = CPyStatics[117]; /* ('InsufficientData', 'Web3ValueError') */
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
    cpy_r_r31 = CPyStatics[118]; /* ('hexstr',) */
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
    cpy_r_r54 = CPyStatics[118]; /* ('hexstr',) */
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
    cpy_r_r6 = CPyStatics[118]; /* ('hexstr',) */
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
    cpy_r_r5 = CPyStatics[119]; /* ('Final', 'Union') */
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
    cpy_r_r14 = CPyStatics[120]; /* (('faster_eth_utils', 'faster_eth_utils',
                                     'faster_eth_utils'),) */
    cpy_r_r15 = CPyStatic_type_conversion___globals;
    cpy_r_r16 = CPyStatics[62]; /* 'faster_web3/_utils/type_conversion.py' */
    cpy_r_r17 = CPyStatics[26]; /* '<module>' */
    cpy_r_r18 = CPyImport_ImportMany(cpy_r_r14, cpy_r_r11, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r13);
    if (!cpy_r_r18) goto CPyL12;
    cpy_r_r19 = CPyStatics[121]; /* ('HexStr',) */
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
    cpy_r_r23 = CPyStatics[122]; /* ('Web3ValueError',) */
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
    cpy_r_r5 = CPyStatics[123]; /* ('Any', 'Iterable', 'Mapping', 'Set', 'Union') */
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
    cpy_r_r9 = CPyStatics[124]; /* ('TxData', 'TxParams') */
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

static int
caching___SimpleCache_init(PyObject *self, PyObject *args, PyObject *kwds)
{
    return 0;
}
static Py_ssize_t CPyDunder___len__caching___SimpleCache(PyObject *self) {
    CPyTagged retval = CPyDef_caching___SimpleCache_____len__(self);
    if (retval == CPY_INT_TAG) {
        return -1;
    }
    Py_ssize_t val = CPyTagged_AsSsize_t(retval);
    CPyTagged_DECREF(retval);
    if (PyErr_Occurred()) return -1;
    return val;
}
static PyMappingMethods caching___SimpleCache_as_mapping = {
    .mp_length = CPyDunder___len__caching___SimpleCache,
};
static int CPyDunder___contains__caching___SimpleCache(PyObject *self, PyObject *obj_item) {
    PyObject *arg_item;
    if (likely(PyUnicode_Check(obj_item)))
        arg_item = obj_item;
    else {
        CPy_TypeError("str", obj_item); 
        return -1;
    }
    char val = CPyDef_caching___SimpleCache_____contains__(self, arg_item);
    if (val == 2) {
        return -1;
    }
    return val;
}
static PySequenceMethods caching___SimpleCache_as_sequence = {
    .sq_contains = CPyDunder___contains__caching___SimpleCache,
};
PyObject *CPyDef_caching_____mypyc__SimpleCache_setup(PyObject *cpy_r_type);
PyObject *CPyDef_caching___SimpleCache(CPyTagged cpy_r_size);

static PyObject *
caching___SimpleCache_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    if (type != CPyType_caching___SimpleCache) {
        PyErr_SetString(PyExc_TypeError, "interpreted classes cannot inherit from compiled");
        return NULL;
    }
    PyObject *self = CPyDef_caching_____mypyc__SimpleCache_setup((PyObject*)type);
    if (self == NULL)
        return NULL;
    PyObject *ret = CPyPy_caching___SimpleCache_____init__(self, args, kwds);
    if (ret == NULL)
        return NULL;
    return self;
}

static int
caching___SimpleCache_traverse(faster_web3___utils___caching___SimpleCacheObject *self, visitproc visit, void *arg)
{
    if (CPyTagged_CheckLong(self->__size)) {
        Py_VISIT(CPyTagged_LongAsObject(self->__size));
    }
    Py_VISIT(self->__data);
    PyObject_VisitManagedDict((PyObject *)self, visit, arg);
    return 0;
}

static int
caching___SimpleCache_clear(faster_web3___utils___caching___SimpleCacheObject *self)
{
    if (CPyTagged_CheckLong(self->__size)) {
        CPyTagged __tmp = self->__size;
        self->__size = CPY_INT_TAG;
        Py_XDECREF(CPyTagged_LongAsObject(__tmp));
    }
    Py_CLEAR(self->__data);
    PyObject_ClearManagedDict((PyObject *)self);
    return 0;
}

static void
caching___SimpleCache_dealloc(faster_web3___utils___caching___SimpleCacheObject *self)
{
    PyObject_GC_UnTrack(self);
    CPy_TRASHCAN_BEGIN(self, caching___SimpleCache_dealloc)
    caching___SimpleCache_clear(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
    CPy_TRASHCAN_END(self)
}

static CPyVTableItem caching___SimpleCache_vtable[11];
static bool
CPyDef_caching___SimpleCache_trait_vtable_setup(void)
{
    CPyVTableItem caching___SimpleCache_vtable_scratch[] = {
        (CPyVTableItem)CPyDef_caching___SimpleCache_____init__,
        (CPyVTableItem)CPyDef_caching___SimpleCache_____contains__,
        (CPyVTableItem)CPyDef_caching___SimpleCache_____len__,
        (CPyVTableItem)CPyDef_caching___SimpleCache___cache,
        (CPyVTableItem)CPyDef_caching___SimpleCache___get_cache_entry,
        (CPyVTableItem)CPyDef_caching___SimpleCache___clear,
        (CPyVTableItem)CPyDef_caching___SimpleCache___items,
        (CPyVTableItem)CPyDef_caching___SimpleCache___pop,
        (CPyVTableItem)CPyDef_caching___SimpleCache___popitem,
        (CPyVTableItem)CPyDef_caching___SimpleCache___is_full,
        (CPyVTableItem)CPyDef_caching___SimpleCache___async_await_and_popitem,
    };
    memcpy(caching___SimpleCache_vtable, caching___SimpleCache_vtable_scratch, sizeof(caching___SimpleCache_vtable));
    return 1;
}

static PyObject *
caching___SimpleCache_get__size(faster_web3___utils___caching___SimpleCacheObject *self, void *closure);
static int
caching___SimpleCache_set__size(faster_web3___utils___caching___SimpleCacheObject *self, PyObject *value, void *closure);
static PyObject *
caching___SimpleCache_get__data(faster_web3___utils___caching___SimpleCacheObject *self, void *closure);
static int
caching___SimpleCache_set__data(faster_web3___utils___caching___SimpleCacheObject *self, PyObject *value, void *closure);

static PyGetSetDef caching___SimpleCache_getseters[] = {
    {"_size",
     (getter)caching___SimpleCache_get__size, (setter)caching___SimpleCache_set__size,
     NULL, NULL},
    {"_data",
     (getter)caching___SimpleCache_get__data, (setter)caching___SimpleCache_set__data,
     NULL, NULL},
    {"__dict__", PyObject_GenericGetDict, PyObject_GenericSetDict},
    {NULL}  /* Sentinel */
};

static PyMethodDef caching___SimpleCache_methods[] = {
    {"__init__",
     (PyCFunction)CPyPy_caching___SimpleCache_____init__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__init__($self, size=100)\n--\n\n")},
    {"__contains__",
     (PyCFunction)CPyPy_caching___SimpleCache_____contains__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__contains__($self, key, /)\n--\n\n")},
    {"__len__",
     (PyCFunction)CPyPy_caching___SimpleCache_____len__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__len__($self, /)\n--\n\n")},
    {"cache",
     (PyCFunction)CPyPy_caching___SimpleCache___cache,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("cache($self, key, value)\n--\n\n")},
    {"get_cache_entry",
     (PyCFunction)CPyPy_caching___SimpleCache___get_cache_entry,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("get_cache_entry($self, key)\n--\n\n")},
    {"clear",
     (PyCFunction)CPyPy_caching___SimpleCache___clear,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("clear($self)\n--\n\n")},
    {"items",
     (PyCFunction)CPyPy_caching___SimpleCache___items,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("items($self)\n--\n\n")},
    {"pop",
     (PyCFunction)CPyPy_caching___SimpleCache___pop,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("pop($self, key)\n--\n\n")},
    {"popitem",
     (PyCFunction)CPyPy_caching___SimpleCache___popitem,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("popitem($self, last=True)\n--\n\n")},
    {"is_full",
     (PyCFunction)CPyPy_caching___SimpleCache___is_full,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("is_full($self)\n--\n\n")},
    {"async_await_and_popitem",
     (PyCFunction)CPyPy_caching___SimpleCache___async_await_and_popitem,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("async_await_and_popitem($self, last=True, timeout=10.0, /)\n--\n\n")},
    {"__setstate__", (PyCFunction)CPyPickle_SetState, METH_O, NULL},
    {"__getstate__", (PyCFunction)CPyPickle_GetState, METH_NOARGS, NULL},
    {NULL}  /* Sentinel */
};

static PyTypeObject CPyType_caching___SimpleCache_template_ = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "SimpleCache",
    .tp_new = caching___SimpleCache_new,
    .tp_dealloc = (destructor)caching___SimpleCache_dealloc,
    .tp_traverse = (traverseproc)caching___SimpleCache_traverse,
    .tp_clear = (inquiry)caching___SimpleCache_clear,
    .tp_getset = caching___SimpleCache_getseters,
    .tp_methods = caching___SimpleCache_methods,
    .tp_init = caching___SimpleCache_init,
    .tp_as_mapping = &caching___SimpleCache_as_mapping,
    .tp_as_sequence = &caching___SimpleCache_as_sequence,
    .tp_basicsize = sizeof(faster_web3___utils___caching___SimpleCacheObject),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_MANAGED_DICT,
    .tp_doc = PyDoc_STR("SimpleCache(size=100)\n--\n\n"),
};
static PyTypeObject *CPyType_caching___SimpleCache_template = &CPyType_caching___SimpleCache_template_;

PyObject *CPyDef_caching_____mypyc__SimpleCache_setup(PyObject *cpy_r_type)
{
    PyTypeObject *type = (PyTypeObject*)cpy_r_type;
    faster_web3___utils___caching___SimpleCacheObject *self;
    self = (faster_web3___utils___caching___SimpleCacheObject *)type->tp_alloc(type, 0);
    if (self == NULL)
        return NULL;
    self->vtable = caching___SimpleCache_vtable;
    self->__size = CPY_INT_TAG;
    return (PyObject *)self;
}

PyObject *CPyDef_caching___SimpleCache(CPyTagged cpy_r_size)
{
    PyObject *self = CPyDef_caching_____mypyc__SimpleCache_setup((PyObject *)CPyType_caching___SimpleCache);
    if (self == NULL)
        return NULL;
    char res = CPyDef_caching___SimpleCache_____init__(self, cpy_r_size);
    if (res == 2) {
        Py_DECREF(self);
        return NULL;
    }
    return self;
}

static PyObject *
caching___SimpleCache_get__size(faster_web3___utils___caching___SimpleCacheObject *self, void *closure)
{
    if (unlikely(self->__size == CPY_INT_TAG)) {
        PyErr_SetString(PyExc_AttributeError,
            "attribute '_size' of 'SimpleCache' undefined");
        return NULL;
    }
    CPyTagged_INCREF(self->__size);
    PyObject *retval = CPyTagged_StealAsObject(self->__size);
    return retval;
}

static int
caching___SimpleCache_set__size(faster_web3___utils___caching___SimpleCacheObject *self, PyObject *value, void *closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_AttributeError,
            "'SimpleCache' object attribute '_size' cannot be deleted");
        return -1;
    }
    if (self->__size != CPY_INT_TAG) {
        CPyTagged_DECREF(self->__size);
    }
    CPyTagged tmp;
    if (likely(PyLong_Check(value)))
        tmp = CPyTagged_FromObject(value);
    else {
        CPy_TypeError("int", value); return -1;
    }
    CPyTagged_INCREF(tmp);
    self->__size = tmp;
    return 0;
}

static PyObject *
caching___SimpleCache_get__data(faster_web3___utils___caching___SimpleCacheObject *self, void *closure)
{
    if (unlikely(self->__data == NULL)) {
        PyErr_SetString(PyExc_AttributeError,
            "attribute '_data' of 'SimpleCache' undefined");
        return NULL;
    }
    CPy_INCREF(self->__data);
    PyObject *retval = self->__data;
    return retval;
}

static int
caching___SimpleCache_set__data(faster_web3___utils___caching___SimpleCacheObject *self, PyObject *value, void *closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_AttributeError,
            "'SimpleCache' object attribute '_data' cannot be deleted");
        return -1;
    }
    if (self->__data != NULL) {
        CPy_DECREF(self->__data);
    }
    PyObject *tmp;
    if (likely(PyDict_Check(value)))
        tmp = value;
    else {
        CPy_TypeError("dict", value); 
        tmp = NULL;
    }
    if (!tmp)
        return -1;
    CPy_INCREF(tmp);
    self->__data = tmp;
    return 0;
}

static PyAsyncMethods caching___async_await_and_popitem_SimpleCache_gen_as_async = {
    .am_await = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____await__,
};
PyObject *CPyDef_caching_____mypyc__async_await_and_popitem_SimpleCache_gen_setup(PyObject *cpy_r_type);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen(void);

static PyObject *
caching___async_await_and_popitem_SimpleCache_gen_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    if (type != CPyType_caching___async_await_and_popitem_SimpleCache_gen) {
        PyErr_SetString(PyExc_TypeError, "interpreted classes cannot inherit from compiled");
        return NULL;
    }
    PyObject *self = CPyDef_caching_____mypyc__async_await_and_popitem_SimpleCache_gen_setup((PyObject*)type);
    if (self == NULL)
        return NULL;
    return self;
}

static int
caching___async_await_and_popitem_SimpleCache_gen_traverse(faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *self, visitproc visit, void *arg)
{
    Py_VISIT(self->___mypyc_generator_attribute__self);
    Py_VISIT(self->___mypyc_temp__0);
    Py_VISIT(self->___mypyc_temp__1.f0);
    Py_VISIT(self->___mypyc_temp__1.f1);
    Py_VISIT(self->___mypyc_temp__1.f2);
    Py_VISIT(self->___mypyc_temp__2.f0);
    Py_VISIT(self->___mypyc_temp__2.f1);
    Py_VISIT(self->___mypyc_temp__2.f2);
    Py_VISIT(self->___mypyc_temp__3);
    Py_VISIT(self->___mypyc_temp__4.f0);
    Py_VISIT(self->___mypyc_temp__4.f1);
    Py_VISIT(self->___mypyc_temp__4.f2);
    return 0;
}

static int
caching___async_await_and_popitem_SimpleCache_gen_clear(faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *self)
{
    Py_CLEAR(self->___mypyc_generator_attribute__self);
    Py_CLEAR(self->___mypyc_temp__0);
    Py_CLEAR(self->___mypyc_temp__1.f0);
    Py_CLEAR(self->___mypyc_temp__1.f1);
    Py_CLEAR(self->___mypyc_temp__1.f2);
    Py_CLEAR(self->___mypyc_temp__2.f0);
    Py_CLEAR(self->___mypyc_temp__2.f1);
    Py_CLEAR(self->___mypyc_temp__2.f2);
    Py_CLEAR(self->___mypyc_temp__3);
    Py_CLEAR(self->___mypyc_temp__4.f0);
    Py_CLEAR(self->___mypyc_temp__4.f1);
    Py_CLEAR(self->___mypyc_temp__4.f2);
    return 0;
}

static void
caching___async_await_and_popitem_SimpleCache_gen_dealloc(faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *self)
{
    PyObject_GC_UnTrack(self);
    if (caching___async_await_and_popitem_SimpleCache_gen_free_instance == NULL) {
        caching___async_await_and_popitem_SimpleCache_gen_free_instance = self;
        self->bitmap = 0;
        Py_CLEAR(self->___mypyc_generator_attribute__self);
        self->___mypyc_generator_attribute__last = 2;
        self->___mypyc_generator_attribute__timeout = -113.0;
        self->___mypyc_next_label__ = -113;
        self->___mypyc_generator_attribute__start = -113.0;
        self->___mypyc_generator_attribute__end_time = -113.0;
        Py_CLEAR(self->___mypyc_temp__0);
        Py_CLEAR(self->___mypyc_temp__1.f0);
        Py_CLEAR(self->___mypyc_temp__1.f1);
        Py_CLEAR(self->___mypyc_temp__1.f2);
        Py_CLEAR(self->___mypyc_temp__2.f0);
        Py_CLEAR(self->___mypyc_temp__2.f1);
        Py_CLEAR(self->___mypyc_temp__2.f2);
        self->___mypyc_generator_attribute__now = -113.0;
        Py_CLEAR(self->___mypyc_temp__3);
        Py_CLEAR(self->___mypyc_temp__4.f0);
        Py_CLEAR(self->___mypyc_temp__4.f1);
        Py_CLEAR(self->___mypyc_temp__4.f2);
        return;
    }
    CPy_TRASHCAN_BEGIN(self, caching___async_await_and_popitem_SimpleCache_gen_dealloc)
    caching___async_await_and_popitem_SimpleCache_gen_clear(self);
    Py_TYPE(self)->tp_free((PyObject *)self);
    CPy_TRASHCAN_END(self)
}

static CPyVTableItem caching___async_await_and_popitem_SimpleCache_gen_vtable[7];
static bool
CPyDef_caching___async_await_and_popitem_SimpleCache_gen_trait_vtable_setup(void)
{
    CPyVTableItem caching___async_await_and_popitem_SimpleCache_gen_vtable_scratch[] = {
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____next__,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen___send,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____iter__,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen___throw,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen___close,
        (CPyVTableItem)CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____await__,
    };
    memcpy(caching___async_await_and_popitem_SimpleCache_gen_vtable, caching___async_await_and_popitem_SimpleCache_gen_vtable_scratch, sizeof(caching___async_await_and_popitem_SimpleCache_gen_vtable));
    return 1;
}

static PyMethodDef caching___async_await_and_popitem_SimpleCache_gen_methods[] = {
    {"__next__",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____next__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__next__()\n--\n\n")},
    {"send",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen___send,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("send($arg)\n--\n\n")},
    {"__iter__",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____iter__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__iter__()\n--\n\n")},
    {"throw",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen___throw,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR(NULL)},
    {"close",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen___close,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("close()\n--\n\n")},
    {"__await__",
     (PyCFunction)CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____await__,
     METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("__await__()\n--\n\n")},
    {"__setstate__", (PyCFunction)CPyPickle_SetState, METH_O, NULL},
    {"__getstate__", (PyCFunction)CPyPickle_GetState, METH_NOARGS, NULL},
    {NULL}  /* Sentinel */
};

static PyTypeObject CPyType_caching___async_await_and_popitem_SimpleCache_gen_template_ = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "async_await_and_popitem_SimpleCache_gen",
    .tp_new = caching___async_await_and_popitem_SimpleCache_gen_new,
    .tp_dealloc = (destructor)caching___async_await_and_popitem_SimpleCache_gen_dealloc,
    .tp_traverse = (traverseproc)caching___async_await_and_popitem_SimpleCache_gen_traverse,
    .tp_clear = (inquiry)caching___async_await_and_popitem_SimpleCache_gen_clear,
    .tp_methods = caching___async_await_and_popitem_SimpleCache_gen_methods,
    .tp_iter = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____iter__,
    .tp_iternext = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____next__,
    .tp_as_async = &caching___async_await_and_popitem_SimpleCache_gen_as_async,
    .tp_basicsize = sizeof(faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
    .tp_doc = PyDoc_STR("async_await_and_popitem_SimpleCache_gen()\n--\n\n"),
};
static PyTypeObject *CPyType_caching___async_await_and_popitem_SimpleCache_gen_template = &CPyType_caching___async_await_and_popitem_SimpleCache_gen_template_;

PyObject *CPyDef_caching_____mypyc__async_await_and_popitem_SimpleCache_gen_setup(PyObject *cpy_r_type)
{
    PyTypeObject *type = (PyTypeObject*)cpy_r_type;
    faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *self;
    if (caching___async_await_and_popitem_SimpleCache_gen_free_instance != NULL) {
        self = caching___async_await_and_popitem_SimpleCache_gen_free_instance;
        caching___async_await_and_popitem_SimpleCache_gen_free_instance = NULL;
        Py_SET_REFCNT(self, 1);
        PyObject_GC_Track(self);
        return (PyObject *)self;
    }
    self = (faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)type->tp_alloc(type, 0);
    if (self == NULL)
        return NULL;
    self->vtable = caching___async_await_and_popitem_SimpleCache_gen_vtable;
    self->bitmap = 0;
    self->___mypyc_generator_attribute__last = 2;
    self->___mypyc_generator_attribute__timeout = -113.0;
    self->___mypyc_next_label__ = -113;
    self->___mypyc_generator_attribute__start = -113.0;
    self->___mypyc_generator_attribute__end_time = -113.0;
    self->___mypyc_temp__1 = (tuple_T3OOO) { NULL, NULL, NULL };
    self->___mypyc_temp__2 = (tuple_T3OOO) { NULL, NULL, NULL };
    self->___mypyc_generator_attribute__now = -113.0;
    self->___mypyc_temp__4 = (tuple_T3OOO) { NULL, NULL, NULL };
    return (PyObject *)self;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen(void)
{
    PyObject *self = CPyDef_caching_____mypyc__async_await_and_popitem_SimpleCache_gen_setup((PyObject *)CPyType_caching___async_await_and_popitem_SimpleCache_gen);
    if (self == NULL)
        return NULL;
    return self;
}

static PyMethodDef cachingmodule_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3___utils___caching(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3___utils___caching__internal, "__name__");
    CPyStatic_caching___globals = PyModule_GetDict(CPyModule_faster_web3___utils___caching__internal);
    if (unlikely(CPyStatic_caching___globals == NULL))
        goto fail;
    CPyType_caching___async_await_and_popitem_SimpleCache_gen = (PyTypeObject *)CPyType_FromTemplate((PyObject *)CPyType_caching___async_await_and_popitem_SimpleCache_gen_template, NULL, modname);
    if (unlikely(!CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef_caching_____top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3___utils___caching__internal);
    Py_CLEAR(modname);
    CPy_XDECREF(CPyStatic_caching___RequestCacheValidationThreshold___FINALIZED);
    CPyStatic_caching___RequestCacheValidationThreshold___FINALIZED = NULL;
    CPy_XDECREF(CPyStatic_caching___RequestCacheValidationThreshold___SAFE);
    CPyStatic_caching___RequestCacheValidationThreshold___SAFE = NULL;
    Py_CLEAR(CPyType_caching___RequestCacheValidationThreshold);
    Py_CLEAR(CPyType_caching___SimpleCache);
    Py_CLEAR(CPyType_caching___async_await_and_popitem_SimpleCache_gen);
    return -1;
}
static struct PyModuleDef cachingmodule = {
    PyModuleDef_HEAD_INIT,
    "faster_web3.utils.caching",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    cachingmodule_methods,
    NULL,
};

PyObject *CPyInit_faster_web3___utils___caching(void)
{
    if (CPyModule_faster_web3___utils___caching__internal) {
        Py_INCREF(CPyModule_faster_web3___utils___caching__internal);
        return CPyModule_faster_web3___utils___caching__internal;
    }
    CPyModule_faster_web3___utils___caching__internal = PyModule_Create(&cachingmodule);
    if (unlikely(CPyModule_faster_web3___utils___caching__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3___utils___caching(CPyModule_faster_web3___utils___caching__internal) != 0)
        goto fail;
    return CPyModule_faster_web3___utils___caching__internal;
    fail:
    return NULL;
}

char CPyDef_caching___SimpleCache_____init__(PyObject *cpy_r_self, CPyTagged cpy_r_size) {
    char cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    char cpy_r_r6;
    char cpy_r_r7;
    if (cpy_r_size != CPY_INT_TAG) goto CPyL9;
    cpy_r_size = 200;
CPyL2: ;
    if (((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__size != CPY_INT_TAG) {
        CPyTagged_DECREF(((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__size);
    }
    ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__size = cpy_r_size;
    cpy_r_r0 = 1;
    if (unlikely(!cpy_r_r0)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "__init__", 34, CPyStatic_caching___globals);
        goto CPyL8;
    }
    cpy_r_r1 = CPyStatic_caching___globals;
    cpy_r_r2 = CPyStatics[74]; /* 'OrderedDict' */
    cpy_r_r3 = CPyDict_GetItem(cpy_r_r1, cpy_r_r2);
    if (unlikely(cpy_r_r3 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "__init__", 35, CPyStatic_caching___globals);
        goto CPyL8;
    }
    cpy_r_r4 = PyObject_Vectorcall(cpy_r_r3, 0, 0, 0);
    CPy_DECREF(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "__init__", 35, CPyStatic_caching___globals);
        goto CPyL8;
    }
    if (likely(PyDict_Check(cpy_r_r4)))
        cpy_r_r5 = cpy_r_r4;
    else {
        CPy_TypeErrorTraceback("faster_web3/utils/caching.py", "__init__", 35, CPyStatic_caching___globals, "dict", cpy_r_r4);
        goto CPyL8;
    }
    if (((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data);
    }
    ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data = cpy_r_r5;
    cpy_r_r6 = 1;
    if (unlikely(!cpy_r_r6)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "__init__", 35, CPyStatic_caching___globals);
        goto CPyL8;
    }
    return 1;
CPyL8: ;
    cpy_r_r7 = 2;
    return cpy_r_r7;
CPyL9: ;
    CPyTagged_INCREF(cpy_r_size);
    goto CPyL2;
}

PyObject *CPyPy_caching___SimpleCache_____init__(PyObject *self, PyObject *args, PyObject *kw) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"size", 0};
    PyObject *obj_size = NULL;
    if (!CPyArg_ParseTupleAndKeywords(args, kw, "|O", "__init__", kwlist, &obj_size)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    CPyTagged arg_size;
    if (obj_size == NULL) {
        arg_size = CPY_INT_TAG;
    } else if (likely(PyLong_Check(obj_size)))
        arg_size = CPyTagged_BorrowFromObject(obj_size);
    else {
        CPy_TypeError("int", obj_size); goto fail;
    }
    char retval = CPyDef_caching___SimpleCache_____init__(arg_self, arg_size);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = Py_None;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__init__", 33, CPyStatic_caching___globals);
    return NULL;
}

char CPyDef_caching___SimpleCache_____contains__(PyObject *cpy_r_self, PyObject *cpy_r_key) {
    PyObject *cpy_r_r0;
    int32_t cpy_r_r1;
    char cpy_r_r2;
    char cpy_r_r3;
    char cpy_r_r4;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "__contains__", "SimpleCache", "_data", 38, CPyStatic_caching___globals);
        goto CPyL3;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = PyDict_Contains(cpy_r_r0, cpy_r_key);
    CPy_DECREF(cpy_r_r0);
    cpy_r_r2 = cpy_r_r1 >= 0;
    if (unlikely(!cpy_r_r2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "__contains__", 38, CPyStatic_caching___globals);
        goto CPyL3;
    }
    cpy_r_r3 = cpy_r_r1;
    return cpy_r_r3;
CPyL3: ;
    cpy_r_r4 = 2;
    return cpy_r_r4;
}

PyObject *CPyPy_caching___SimpleCache_____contains__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"key", 0};
    static CPyArg_Parser parser = {"O:__contains__", kwlist, 0};
    PyObject *obj_key;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_key)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    PyObject *arg_key;
    if (likely(PyUnicode_Check(obj_key)))
        arg_key = obj_key;
    else {
        CPy_TypeError("str", obj_key); 
        goto fail;
    }
    char retval = CPyDef_caching___SimpleCache_____contains__(arg_self, arg_key);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__contains__", 37, CPyStatic_caching___globals);
    return NULL;
}

CPyTagged CPyDef_caching___SimpleCache_____len__(PyObject *cpy_r_self) {
    PyObject *cpy_r_r0;
    int64_t cpy_r_r1;
    CPyTagged cpy_r_r2;
    CPyTagged cpy_r_r3;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "__len__", "SimpleCache", "_data", 41, CPyStatic_caching___globals);
        goto CPyL2;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = PyDict_Size(cpy_r_r0);
    CPy_DECREF(cpy_r_r0);
    cpy_r_r2 = cpy_r_r1 << 1;
    return cpy_r_r2;
CPyL2: ;
    cpy_r_r3 = CPY_INT_TAG;
    return cpy_r_r3;
}

PyObject *CPyPy_caching___SimpleCache_____len__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":__len__", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    CPyTagged retval = CPyDef_caching___SimpleCache_____len__(arg_self);
    if (retval == CPY_INT_TAG) {
        return NULL;
    }
    PyObject *retbox = CPyTagged_StealAsObject(retval);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__len__", 40, CPyStatic_caching___globals);
    return NULL;
}

tuple_T2OO CPyDef_caching___SimpleCache___cache(PyObject *cpy_r_self, PyObject *cpy_r_key, PyObject *cpy_r_value) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    int32_t cpy_r_r2;
    char cpy_r_r3;
    char cpy_r_r4;
    char cpy_r_r5;
    PyObject *cpy_r_r6;
    int64_t cpy_r_r7;
    CPyTagged cpy_r_r8;
    CPyTagged cpy_r_r9;
    int64_t cpy_r_r10;
    char cpy_r_r11;
    int64_t cpy_r_r12;
    char cpy_r_r13;
    char cpy_r_r14;
    char cpy_r_r15;
    char cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject **cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject *cpy_r_r23;
    tuple_T2OO cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject *cpy_r_r28;
    int32_t cpy_r_r29;
    char cpy_r_r30;
    PyObject *cpy_r_r31;
    int32_t cpy_r_r32;
    char cpy_r_r33;
    int64_t cpy_r_r34;
    CPyTagged cpy_r_r35;
    char cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    tuple_T2OO cpy_r_r39;
    tuple_T2OO cpy_r_r40;
    cpy_r_r0 = PyDict_New();
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 44, CPyStatic_caching___globals);
        goto CPyL20;
    }
    cpy_r_r1 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r1 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "cache", "SimpleCache", "_data", 49, CPyStatic_caching___globals);
        goto CPyL21;
    }
    CPy_INCREF(cpy_r_r1);
CPyL2: ;
    cpy_r_r2 = PyDict_Contains(cpy_r_r1, cpy_r_key);
    CPy_DECREF(cpy_r_r1);
    cpy_r_r3 = cpy_r_r2 >= 0;
    if (unlikely(!cpy_r_r3)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 49, CPyStatic_caching___globals);
        goto CPyL21;
    }
    cpy_r_r4 = cpy_r_r2;
    cpy_r_r5 = cpy_r_r4 ^ 1;
    if (!cpy_r_r5) goto CPyL14;
CPyL4: ;
    cpy_r_r6 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r6 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "cache", "SimpleCache", "_data", 50, CPyStatic_caching___globals);
        goto CPyL21;
    }
    CPy_INCREF(cpy_r_r6);
CPyL5: ;
    cpy_r_r7 = PyDict_Size(cpy_r_r6);
    CPy_DECREF(cpy_r_r6);
    cpy_r_r8 = cpy_r_r7 << 1;
    cpy_r_r9 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__size;
    if (unlikely(cpy_r_r9 == CPY_INT_TAG)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "cache", "SimpleCache", "_size", 50, CPyStatic_caching___globals);
        goto CPyL21;
    }
CPyL6: ;
    cpy_r_r10 = cpy_r_r8 & 1;
    cpy_r_r11 = cpy_r_r10 != 0;
    if (cpy_r_r11) goto CPyL8;
    cpy_r_r12 = cpy_r_r9 & 1;
    cpy_r_r13 = cpy_r_r12 != 0;
    if (!cpy_r_r13) goto CPyL9;
CPyL8: ;
    cpy_r_r14 = CPyTagged_IsLt_(cpy_r_r8, cpy_r_r9);
    cpy_r_r15 = cpy_r_r14 ^ 1;
    if (cpy_r_r15) {
        goto CPyL10;
    } else
        goto CPyL14;
CPyL9: ;
    cpy_r_r16 = (Py_ssize_t)cpy_r_r8 >= (Py_ssize_t)cpy_r_r9;
    if (!cpy_r_r16) goto CPyL14;
CPyL10: ;
    cpy_r_r17 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r17 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "cache", "SimpleCache", "_data", 51, CPyStatic_caching___globals);
        goto CPyL21;
    }
    CPy_INCREF(cpy_r_r17);
CPyL11: ;
    cpy_r_r18 = CPyStatics[75]; /* 'popitem' */
    cpy_r_r19 = 0 ? Py_True : Py_False;
    PyObject *cpy_r_r20[2] = {cpy_r_r17, cpy_r_r19};
    cpy_r_r21 = (PyObject **)&cpy_r_r20;
    cpy_r_r22 = CPyStatics[125]; /* ('last',) */
    cpy_r_r23 = PyObject_VectorcallMethod(cpy_r_r18, cpy_r_r21, 9223372036854775809ULL, cpy_r_r22);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 51, CPyStatic_caching___globals);
        goto CPyL22;
    }
    CPy_DECREF(cpy_r_r17);
    PyObject *__tmp15;
    if (unlikely(!(PyTuple_Check(cpy_r_r23) && PyTuple_GET_SIZE(cpy_r_r23) == 2))) {
        __tmp15 = NULL;
        goto __LL16;
    }
    if (likely(PyUnicode_Check(PyTuple_GET_ITEM(cpy_r_r23, 0))))
        __tmp15 = PyTuple_GET_ITEM(cpy_r_r23, 0);
    else {
        __tmp15 = NULL;
    }
    if (__tmp15 == NULL) goto __LL16;
    __tmp15 = PyTuple_GET_ITEM(cpy_r_r23, 1);
    if (__tmp15 == NULL) goto __LL16;
    __tmp15 = cpy_r_r23;
__LL16: ;
    if (unlikely(__tmp15 == NULL)) {
        CPy_TypeError("tuple[str, object]", cpy_r_r23); cpy_r_r24 = (tuple_T2OO) { NULL, NULL };
    } else {
        PyObject *__tmp17 = PyTuple_GET_ITEM(cpy_r_r23, 0);
        CPy_INCREF(__tmp17);
        PyObject *__tmp18;
        if (likely(PyUnicode_Check(__tmp17)))
            __tmp18 = __tmp17;
        else {
            CPy_TypeError("str", __tmp17); 
            __tmp18 = NULL;
        }
        cpy_r_r24.f0 = __tmp18;
        PyObject *__tmp19 = PyTuple_GET_ITEM(cpy_r_r23, 1);
        CPy_INCREF(__tmp19);
        PyObject *__tmp20;
        __tmp20 = __tmp19;
        cpy_r_r24.f1 = __tmp20;
    }
    CPy_DECREF(cpy_r_r23);
    if (unlikely(cpy_r_r24.f0 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 51, CPyStatic_caching___globals);
        goto CPyL21;
    }
    cpy_r_r25 = cpy_r_r24.f0;
    cpy_r_r26 = cpy_r_r24.f1;
    cpy_r_r27 = cpy_r_r25;
    cpy_r_r28 = cpy_r_r26;
    cpy_r_r29 = CPyDict_SetItem(cpy_r_r0, cpy_r_r27, cpy_r_r28);
    CPy_DECREF(cpy_r_r27);
    CPy_DECREF(cpy_r_r28);
    cpy_r_r30 = cpy_r_r29 >= 0;
    if (unlikely(!cpy_r_r30)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 52, CPyStatic_caching___globals);
        goto CPyL21;
    } else
        goto CPyL4;
CPyL14: ;
    cpy_r_r31 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r31 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "cache", "SimpleCache", "_data", 53, CPyStatic_caching___globals);
        goto CPyL21;
    }
    CPy_INCREF(cpy_r_r31);
CPyL15: ;
    cpy_r_r32 = CPyDict_SetItem(cpy_r_r31, cpy_r_key, cpy_r_value);
    CPy_DECREF(cpy_r_r31);
    cpy_r_r33 = cpy_r_r32 >= 0;
    if (unlikely(!cpy_r_r33)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 53, CPyStatic_caching___globals);
        goto CPyL21;
    }
    cpy_r_r34 = PyDict_Size(cpy_r_r0);
    cpy_r_r35 = cpy_r_r34 << 1;
    cpy_r_r36 = cpy_r_r35 != 0;
    if (!cpy_r_r36) goto CPyL23;
    cpy_r_r37 = cpy_r_r0;
    goto CPyL19;
CPyL18: ;
    cpy_r_r38 = Py_None;
    cpy_r_r37 = cpy_r_r38;
CPyL19: ;
    CPy_INCREF(cpy_r_value);
    cpy_r_r39.f0 = cpy_r_value;
    cpy_r_r39.f1 = cpy_r_r37;
    return cpy_r_r39;
CPyL20: ;
    tuple_T2OO __tmp21 = { NULL, NULL };
    cpy_r_r40 = __tmp21;
    return cpy_r_r40;
CPyL21: ;
    CPy_DecRef(cpy_r_r0);
    goto CPyL20;
CPyL22: ;
    CPy_DecRef(cpy_r_r0);
    CPy_DecRef(cpy_r_r17);
    goto CPyL20;
CPyL23: ;
    CPy_DECREF(cpy_r_r0);
    goto CPyL18;
}

PyObject *CPyPy_caching___SimpleCache___cache(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"key", "value", 0};
    static CPyArg_Parser parser = {"OO:cache", kwlist, 0};
    PyObject *obj_key;
    PyObject *obj_value;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_key, &obj_value)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    PyObject *arg_key;
    if (likely(PyUnicode_Check(obj_key)))
        arg_key = obj_key;
    else {
        CPy_TypeError("str", obj_key); 
        goto fail;
    }
    PyObject *arg_value = obj_value;
    tuple_T2OO retval = CPyDef_caching___SimpleCache___cache(arg_self, arg_key, arg_value);
    if (retval.f0 == NULL) {
        return NULL;
    }
    PyObject *retbox = PyTuple_New(2);
    if (unlikely(retbox == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp22 = retval.f0;
    PyTuple_SET_ITEM(retbox, 0, __tmp22);
    PyObject *__tmp23 = retval.f1;
    PyTuple_SET_ITEM(retbox, 1, __tmp23);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "cache", 43, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___SimpleCache___get_cache_entry(PyObject *cpy_r_self, PyObject *cpy_r_key) {
    PyObject *cpy_r_r0;
    int32_t cpy_r_r1;
    char cpy_r_r2;
    char cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "get_cache_entry", "SimpleCache", "_data", 60, CPyStatic_caching___globals);
        goto CPyL8;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = PyDict_Contains(cpy_r_r0, cpy_r_key);
    CPy_DECREF(cpy_r_r0);
    cpy_r_r2 = cpy_r_r1 >= 0;
    if (unlikely(!cpy_r_r2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "get_cache_entry", 60, CPyStatic_caching___globals);
        goto CPyL8;
    }
    cpy_r_r3 = cpy_r_r1;
    if (!cpy_r_r3) goto CPyL6;
    cpy_r_r4 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "get_cache_entry", "SimpleCache", "_data", 60, CPyStatic_caching___globals);
        goto CPyL8;
    }
    CPy_INCREF(cpy_r_r4);
CPyL4: ;
    cpy_r_r5 = CPyDict_GetItem(cpy_r_r4, cpy_r_key);
    CPy_DECREF(cpy_r_r4);
    if (unlikely(cpy_r_r5 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "get_cache_entry", 60, CPyStatic_caching___globals);
        goto CPyL8;
    }
    cpy_r_r6 = cpy_r_r5;
    goto CPyL7;
CPyL6: ;
    cpy_r_r7 = Py_None;
    cpy_r_r6 = cpy_r_r7;
CPyL7: ;
    return cpy_r_r6;
CPyL8: ;
    cpy_r_r8 = NULL;
    return cpy_r_r8;
}

PyObject *CPyPy_caching___SimpleCache___get_cache_entry(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"key", 0};
    static CPyArg_Parser parser = {"O:get_cache_entry", kwlist, 0};
    PyObject *obj_key;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_key)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    PyObject *arg_key;
    if (likely(PyUnicode_Check(obj_key)))
        arg_key = obj_key;
    else {
        CPy_TypeError("str", obj_key); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___SimpleCache___get_cache_entry(arg_self, arg_key);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "get_cache_entry", 59, CPyStatic_caching___globals);
    return NULL;
}

char CPyDef_caching___SimpleCache___clear(PyObject *cpy_r_self) {
    PyObject *cpy_r_r0;
    char cpy_r_r1;
    char cpy_r_r2;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "clear", "SimpleCache", "_data", 63, CPyStatic_caching___globals);
        goto CPyL3;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = CPyDict_Clear(cpy_r_r0);
    CPy_DECREF(cpy_r_r0);
    if (unlikely(!cpy_r_r1)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "clear", 63, CPyStatic_caching___globals);
        goto CPyL3;
    }
    return 1;
CPyL3: ;
    cpy_r_r2 = 2;
    return cpy_r_r2;
}

PyObject *CPyPy_caching___SimpleCache___clear(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":clear", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    char retval = CPyDef_caching___SimpleCache___clear(arg_self);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = Py_None;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "clear", 62, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___SimpleCache___items(PyObject *cpy_r_self) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "items", "SimpleCache", "_data", 66, CPyStatic_caching___globals);
        goto CPyL3;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = CPyDict_Items(cpy_r_r0);
    CPy_DECREF(cpy_r_r0);
    if (unlikely(cpy_r_r1 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "items", 66, CPyStatic_caching___globals);
        goto CPyL3;
    }
    return cpy_r_r1;
CPyL3: ;
    cpy_r_r2 = NULL;
    return cpy_r_r2;
}

PyObject *CPyPy_caching___SimpleCache___items(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":items", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___SimpleCache___items(arg_self);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "items", 65, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___SimpleCache___pop(PyObject *cpy_r_self, PyObject *cpy_r_key) {
    PyObject *cpy_r_r0;
    int32_t cpy_r_r1;
    char cpy_r_r2;
    char cpy_r_r3;
    char cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject **cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "pop", "SimpleCache", "_data", 69, CPyStatic_caching___globals);
        goto CPyL7;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = PyDict_Contains(cpy_r_r0, cpy_r_key);
    CPy_DECREF(cpy_r_r0);
    cpy_r_r2 = cpy_r_r1 >= 0;
    if (unlikely(!cpy_r_r2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "pop", 69, CPyStatic_caching___globals);
        goto CPyL7;
    }
    cpy_r_r3 = cpy_r_r1;
    cpy_r_r4 = cpy_r_r3 ^ 1;
    if (!cpy_r_r4) goto CPyL4;
    cpy_r_r5 = Py_None;
    return cpy_r_r5;
CPyL4: ;
    cpy_r_r6 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r6 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "pop", "SimpleCache", "_data", 72, CPyStatic_caching___globals);
        goto CPyL7;
    }
    CPy_INCREF(cpy_r_r6);
CPyL5: ;
    cpy_r_r7 = CPyStatics[77]; /* 'pop' */
    PyObject *cpy_r_r8[2] = {cpy_r_r6, cpy_r_key};
    cpy_r_r9 = (PyObject **)&cpy_r_r8;
    cpy_r_r10 = PyObject_VectorcallMethod(cpy_r_r7, cpy_r_r9, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r10 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "pop", 72, CPyStatic_caching___globals);
        goto CPyL8;
    }
    CPy_DECREF(cpy_r_r6);
    return cpy_r_r10;
CPyL7: ;
    cpy_r_r11 = NULL;
    return cpy_r_r11;
CPyL8: ;
    CPy_DecRef(cpy_r_r6);
    goto CPyL7;
}

PyObject *CPyPy_caching___SimpleCache___pop(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"key", 0};
    static CPyArg_Parser parser = {"O:pop", kwlist, 0};
    PyObject *obj_key;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_key)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    PyObject *arg_key;
    if (likely(PyUnicode_Check(obj_key)))
        arg_key = obj_key;
    else {
        CPy_TypeError("str", obj_key); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___SimpleCache___pop(arg_self, arg_key);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "pop", 68, CPyStatic_caching___globals);
    return NULL;
}

tuple_T2OO CPyDef_caching___SimpleCache___popitem(PyObject *cpy_r_self, char cpy_r_last) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject **cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    tuple_T2OO cpy_r_r7;
    tuple_T2OO cpy_r_r8;
    if (cpy_r_last != 2) goto CPyL2;
    cpy_r_last = 1;
CPyL2: ;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "popitem", "SimpleCache", "_data", 75, CPyStatic_caching___globals);
        goto CPyL6;
    }
    CPy_INCREF(cpy_r_r0);
CPyL3: ;
    cpy_r_r1 = CPyStatics[75]; /* 'popitem' */
    cpy_r_r2 = cpy_r_last ? Py_True : Py_False;
    PyObject *cpy_r_r3[2] = {cpy_r_r0, cpy_r_r2};
    cpy_r_r4 = (PyObject **)&cpy_r_r3;
    cpy_r_r5 = CPyStatics[125]; /* ('last',) */
    cpy_r_r6 = PyObject_VectorcallMethod(cpy_r_r1, cpy_r_r4, 9223372036854775809ULL, cpy_r_r5);
    if (unlikely(cpy_r_r6 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "popitem", 75, CPyStatic_caching___globals);
        goto CPyL7;
    }
    CPy_DECREF(cpy_r_r0);
    PyObject *__tmp24;
    if (unlikely(!(PyTuple_Check(cpy_r_r6) && PyTuple_GET_SIZE(cpy_r_r6) == 2))) {
        __tmp24 = NULL;
        goto __LL25;
    }
    if (likely(PyUnicode_Check(PyTuple_GET_ITEM(cpy_r_r6, 0))))
        __tmp24 = PyTuple_GET_ITEM(cpy_r_r6, 0);
    else {
        __tmp24 = NULL;
    }
    if (__tmp24 == NULL) goto __LL25;
    __tmp24 = PyTuple_GET_ITEM(cpy_r_r6, 1);
    if (__tmp24 == NULL) goto __LL25;
    __tmp24 = cpy_r_r6;
__LL25: ;
    if (unlikely(__tmp24 == NULL)) {
        CPy_TypeError("tuple[str, object]", cpy_r_r6); cpy_r_r7 = (tuple_T2OO) { NULL, NULL };
    } else {
        PyObject *__tmp26 = PyTuple_GET_ITEM(cpy_r_r6, 0);
        CPy_INCREF(__tmp26);
        PyObject *__tmp27;
        if (likely(PyUnicode_Check(__tmp26)))
            __tmp27 = __tmp26;
        else {
            CPy_TypeError("str", __tmp26); 
            __tmp27 = NULL;
        }
        cpy_r_r7.f0 = __tmp27;
        PyObject *__tmp28 = PyTuple_GET_ITEM(cpy_r_r6, 1);
        CPy_INCREF(__tmp28);
        PyObject *__tmp29;
        __tmp29 = __tmp28;
        cpy_r_r7.f1 = __tmp29;
    }
    CPy_DECREF(cpy_r_r6);
    if (unlikely(cpy_r_r7.f0 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "popitem", 75, CPyStatic_caching___globals);
        goto CPyL6;
    }
    return cpy_r_r7;
CPyL6: ;
    tuple_T2OO __tmp30 = { NULL, NULL };
    cpy_r_r8 = __tmp30;
    return cpy_r_r8;
CPyL7: ;
    CPy_DecRef(cpy_r_r0);
    goto CPyL6;
}

PyObject *CPyPy_caching___SimpleCache___popitem(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"last", 0};
    static CPyArg_Parser parser = {"|O:popitem", kwlist, 0};
    PyObject *obj_last = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_last)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    char arg_last;
    if (obj_last == NULL) {
        arg_last = 2;
    } else if (unlikely(!PyBool_Check(obj_last))) {
        CPy_TypeError("bool", obj_last); goto fail;
    } else
        arg_last = obj_last == Py_True;
    tuple_T2OO retval = CPyDef_caching___SimpleCache___popitem(arg_self, arg_last);
    if (retval.f0 == NULL) {
        return NULL;
    }
    PyObject *retbox = PyTuple_New(2);
    if (unlikely(retbox == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp31 = retval.f0;
    PyTuple_SET_ITEM(retbox, 0, __tmp31);
    PyObject *__tmp32 = retval.f1;
    PyTuple_SET_ITEM(retbox, 1, __tmp32);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "popitem", 74, CPyStatic_caching___globals);
    return NULL;
}

char CPyDef_caching___SimpleCache___is_full(PyObject *cpy_r_self) {
    PyObject *cpy_r_r0;
    int64_t cpy_r_r1;
    CPyTagged cpy_r_r2;
    CPyTagged cpy_r_r3;
    int64_t cpy_r_r4;
    char cpy_r_r5;
    int64_t cpy_r_r6;
    char cpy_r_r7;
    char cpy_r_r8;
    char cpy_r_r9;
    char cpy_r_r10;
    char cpy_r_r11;
    char cpy_r_r12;
    cpy_r_r0 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__data;
    if (unlikely(cpy_r_r0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "is_full", "SimpleCache", "_data", 78, CPyStatic_caching___globals);
        goto CPyL7;
    }
    CPy_INCREF(cpy_r_r0);
CPyL1: ;
    cpy_r_r1 = PyDict_Size(cpy_r_r0);
    CPy_DECREF(cpy_r_r0);
    cpy_r_r2 = cpy_r_r1 << 1;
    cpy_r_r3 = ((faster_web3___utils___caching___SimpleCacheObject *)cpy_r_self)->__size;
    if (unlikely(cpy_r_r3 == CPY_INT_TAG)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "is_full", "SimpleCache", "_size", 78, CPyStatic_caching___globals);
        goto CPyL7;
    }
CPyL2: ;
    cpy_r_r4 = cpy_r_r2 & 1;
    cpy_r_r5 = cpy_r_r4 != 0;
    if (cpy_r_r5) goto CPyL4;
    cpy_r_r6 = cpy_r_r3 & 1;
    cpy_r_r7 = cpy_r_r6 != 0;
    if (!cpy_r_r7) goto CPyL5;
CPyL4: ;
    cpy_r_r8 = CPyTagged_IsLt_(cpy_r_r2, cpy_r_r3);
    cpy_r_r9 = cpy_r_r8 ^ 1;
    cpy_r_r10 = cpy_r_r9;
    goto CPyL6;
CPyL5: ;
    cpy_r_r11 = (Py_ssize_t)cpy_r_r2 >= (Py_ssize_t)cpy_r_r3;
    cpy_r_r10 = cpy_r_r11;
CPyL6: ;
    return cpy_r_r10;
CPyL7: ;
    cpy_r_r12 = 2;
    return cpy_r_r12;
}

PyObject *CPyPy_caching___SimpleCache___is_full(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":is_full", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    char retval = CPyDef_caching___SimpleCache___is_full(arg_self);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = retval ? Py_True : Py_False;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "is_full", 77, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg, PyObject **cpy_r_stop_iter_ptr) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    int32_t cpy_r_r4;
    PyObject *cpy_r_r5;
    char cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    double cpy_r_r11;
    char cpy_r_r12;
    char cpy_r_r13;
    PyObject *cpy_r_r14;
    double cpy_r_r15;
    char cpy_r_r16;
    double cpy_r_r17;
    char cpy_r_r18;
    PyObject *cpy_r_r19;
    double cpy_r_r20;
    char cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject *cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject **cpy_r_r28;
    PyObject *cpy_r_r29;
    PyObject *cpy_r_r30;
    char cpy_r_r31;
    PyObject *cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    char cpy_r_r37;
    PyObject *cpy_r_r38;
    char cpy_r_r39;
    PyObject *cpy_r_r40;
    char cpy_r_r41;
    tuple_T3OOO cpy_r_r42;
    char cpy_r_r43;
    PyObject **cpy_r_r44;
    PyObject *cpy_r_r45;
    char cpy_r_r46;
    tuple_T3OOO cpy_r_r47;
    tuple_T3OOO cpy_r_r48;
    tuple_T3OOO cpy_r_r49;
    char cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    char cpy_r_r55;
    tuple_T2OO cpy_r_r56;
    PyObject *cpy_r_r57;
    char cpy_r_r58;
    tuple_T3OOO cpy_r_r59;
    char cpy_r_r60;
    PyObject *cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    char cpy_r_r64;
    PyObject *cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject *cpy_r_r68;
    double cpy_r_r69;
    char cpy_r_r70;
    char cpy_r_r71;
    PyObject *cpy_r_r72;
    double cpy_r_r73;
    char cpy_r_r74;
    double cpy_r_r75;
    char cpy_r_r76;
    PyObject *cpy_r_r77;
    char cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
    PyObject *cpy_r_r81;
    PyObject *cpy_r_r82;
    PyObject *cpy_r_r83;
    PyObject **cpy_r_r85;
    PyObject *cpy_r_r86;
    double cpy_r_r87;
    char cpy_r_r88;
    double cpy_r_r89;
    char cpy_r_r90;
    PyObject *cpy_r_r91;
    double cpy_r_r92;
    char cpy_r_r93;
    PyObject *cpy_r_r94;
    double cpy_r_r95;
    PyObject *cpy_r_r96;
    PyObject *cpy_r_r97;
    PyObject *cpy_r_r98;
    PyObject *cpy_r_r99;
    PyObject **cpy_r_r101;
    PyObject *cpy_r_r102;
    PyObject *cpy_r_r103;
    char cpy_r_r104;
    PyObject *cpy_r_r105;
    PyObject *cpy_r_r106;
    PyObject *cpy_r_r107;
    PyObject *cpy_r_r108;
    PyObject *cpy_r_r109;
    char cpy_r_r110;
    PyObject *cpy_r_r111;
    char cpy_r_r112;
    PyObject *cpy_r_r113;
    char cpy_r_r114;
    tuple_T3OOO cpy_r_r115;
    char cpy_r_r116;
    PyObject **cpy_r_r117;
    PyObject *cpy_r_r118;
    char cpy_r_r119;
    tuple_T3OOO cpy_r_r120;
    tuple_T3OOO cpy_r_r121;
    tuple_T3OOO cpy_r_r122;
    char cpy_r_r123;
    PyObject *cpy_r_r124;
    PyObject *cpy_r_r125;
    PyObject *cpy_r_r126;
    tuple_T3OOO cpy_r_r127;
    tuple_T3OOO cpy_r_r128;
    char cpy_r_r129;
    PyObject *cpy_r_r130;
    char cpy_r_r131;
    char cpy_r_r132;
    char cpy_r_r133;
    char cpy_r_r134;
    char cpy_r_r135;
    PyObject *cpy_r_r136;
    cpy_r_r0 = NULL;
    cpy_r_r1 = cpy_r_r0;
    cpy_r_r2 = NULL;
    cpy_r_r3 = cpy_r_r2;
    cpy_r_r4 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_next_label__;
    goto CPyL119;
CPyL1: ;
    cpy_r_r5 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r6 = cpy_r_type != cpy_r_r5;
    if (!cpy_r_r6) goto CPyL4;
    CPyErr_SetObjectAndTraceback(cpy_r_type, cpy_r_value, cpy_r_traceback);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_Unreachable();
CPyL4: ;
    cpy_r_r7 = CPyModule_time;
    cpy_r_r8 = CPyStatics[78]; /* 'time' */
    cpy_r_r9 = CPyObject_GetAttr(cpy_r_r7, cpy_r_r8);
    if (unlikely(cpy_r_r9 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 85, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r10 = PyObject_Vectorcall(cpy_r_r9, 0, 0, 0);
    CPy_DECREF(cpy_r_r9);
    if (unlikely(cpy_r_r10 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 85, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r11 = PyFloat_AsDouble(cpy_r_r10);
    if (cpy_r_r11 == -1.0 && PyErr_Occurred()) {
        CPy_TypeError("float", cpy_r_r10); cpy_r_r11 = -113.0;
    }
    CPy_DECREF(cpy_r_r10);
    cpy_r_r12 = cpy_r_r11 == -113.0;
    if (unlikely(cpy_r_r12)) goto CPyL8;
CPyL7: ;
    if (unlikely(cpy_r_r11 == -113.0)) {
        ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap |= 2;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__start = cpy_r_r11;
    cpy_r_r13 = 1;
    if (unlikely(!cpy_r_r13)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 85, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL9;
CPyL8: ;
    cpy_r_r14 = PyErr_Occurred();
    if (unlikely(cpy_r_r14 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 85, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL7;
CPyL9: ;
    cpy_r_r15 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__start;
    if (unlikely(cpy_r_r15 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 2)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'start' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r16 = cpy_r_r15 == -113.0;
    if (unlikely(cpy_r_r16)) goto CPyL11;
CPyL10: ;
    cpy_r_r17 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__timeout;
    if (unlikely(cpy_r_r17 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 1)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'timeout' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r18 = cpy_r_r17 == -113.0;
    if (unlikely(cpy_r_r18)) {
        goto CPyL13;
    } else
        goto CPyL12;
CPyL11: ;
    cpy_r_r19 = PyErr_Occurred();
    if (unlikely(cpy_r_r19 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 86, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL10;
CPyL12: ;
    cpy_r_r20 = cpy_r_r15 + cpy_r_r17;
    if (unlikely(cpy_r_r20 == -113.0)) {
        ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap |= 4;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__end_time = cpy_r_r20;
    cpy_r_r21 = 1;
    if (unlikely(!cpy_r_r21)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 86, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL14;
CPyL13: ;
    cpy_r_r22 = PyErr_Occurred();
    if (unlikely(cpy_r_r22 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 86, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL12;
CPyL14: ;
    if (!1) goto CPyL114;
    cpy_r_r23 = CPyModule_asyncio;
    cpy_r_r24 = CPyStatics[79]; /* 'sleep' */
    cpy_r_r25 = CPyObject_GetAttr(cpy_r_r23, cpy_r_r24);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r26 = CPyStatics[105]; /* 0 */
    PyObject *cpy_r_r27[1] = {cpy_r_r26};
    cpy_r_r28 = (PyObject **)&cpy_r_r27;
    cpy_r_r29 = PyObject_Vectorcall(cpy_r_r25, cpy_r_r28, 1, 0);
    CPy_DECREF(cpy_r_r25);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r30 = CPy_GetCoro(cpy_r_r29);
    CPy_DECREF(cpy_r_r29);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    }
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0 = cpy_r_r30;
    cpy_r_r31 = 1;
    if (unlikely(!cpy_r_r31)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", -1, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r32 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0;
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__0", -1, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_INCREF(cpy_r_r32);
CPyL20: ;
    cpy_r_r33 = CPyIter_Next(cpy_r_r32);
    CPy_DECREF(cpy_r_r32);
    if (cpy_r_r33 != NULL) goto CPyL23;
    cpy_r_r34 = CPy_FetchStopIterationValue();
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r35 = cpy_r_r34;
    CPy_DECREF(cpy_r_r35);
    cpy_r_r36 = NULL;
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0 = cpy_r_r36;
    cpy_r_r37 = 1;
    if (unlikely(!cpy_r_r37)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    } else
        goto CPyL45;
CPyL23: ;
    cpy_r_r38 = cpy_r_r33;
CPyL24: ;
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_next_label__ = 1;
    return cpy_r_r38;
CPyL25: ;
    cpy_r_r40 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r41 = cpy_r_type != cpy_r_r40;
    if (!cpy_r_r41) goto CPyL125;
    CPyErr_SetObjectAndTraceback(cpy_r_type, cpy_r_value, cpy_r_traceback);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL29;
    } else
        goto CPyL126;
CPyL27: ;
    CPy_Unreachable();
CPyL28: ;
    CPy_INCREF(cpy_r_arg);
    goto CPyL40;
CPyL29: ;
    cpy_r_r42 = CPy_CatchError();
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1.f0 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1.f0);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1.f1);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1.f2);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1 = cpy_r_r42;
    cpy_r_r43 = 1;
    if (unlikely(!cpy_r_r43)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", -1, CPyStatic_caching___globals);
        goto CPyL127;
    }
    cpy_r_r44 = (PyObject **)&cpy_r_r1;
    cpy_r_r45 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0;
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__0", -1, CPyStatic_caching___globals);
        goto CPyL127;
    }
    CPy_INCREF(cpy_r_r45);
CPyL31: ;
    cpy_r_r46 = CPy_YieldFromErrorHandle(cpy_r_r45, cpy_r_r44);
    CPy_DecRef(cpy_r_r45);
    if (unlikely(cpy_r_r46 == 2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL127;
    }
    if (cpy_r_r46) goto CPyL35;
    cpy_r_r38 = cpy_r_r1;
    cpy_r_r47 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1;
    if (unlikely(cpy_r_r47.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__1", -1, CPyStatic_caching___globals);
        goto CPyL128;
    }
    CPy_INCREF(cpy_r_r47.f0);
    CPy_INCREF(cpy_r_r47.f1);
    CPy_INCREF(cpy_r_r47.f2);
CPyL34: ;
    CPy_RestoreExcInfo(cpy_r_r47);
    CPy_DecRef(cpy_r_r47.f0);
    CPy_DecRef(cpy_r_r47.f1);
    CPy_DecRef(cpy_r_r47.f2);
    goto CPyL24;
CPyL35: ;
    cpy_r_r35 = cpy_r_r1;
    CPy_DecRef(cpy_r_r35);
    cpy_r_r48 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1;
    if (unlikely(cpy_r_r48.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__1", -1, CPyStatic_caching___globals);
        goto CPyL37;
    }
    CPy_INCREF(cpy_r_r48.f0);
    CPy_INCREF(cpy_r_r48.f1);
    CPy_INCREF(cpy_r_r48.f2);
CPyL36: ;
    CPy_RestoreExcInfo(cpy_r_r48);
    CPy_DecRef(cpy_r_r48.f0);
    CPy_DecRef(cpy_r_r48.f1);
    CPy_DecRef(cpy_r_r48.f2);
    goto CPyL45;
CPyL37: ;
    cpy_r_r49 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__1;
    if (unlikely(cpy_r_r49.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__1", -1, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_INCREF(cpy_r_r49.f0);
    CPy_INCREF(cpy_r_r49.f1);
    CPy_INCREF(cpy_r_r49.f2);
CPyL38: ;
    CPy_RestoreExcInfo(cpy_r_r49);
    CPy_DecRef(cpy_r_r49.f0);
    CPy_DecRef(cpy_r_r49.f1);
    CPy_DecRef(cpy_r_r49.f2);
    cpy_r_r50 = CPy_KeepPropagating();
    if (!cpy_r_r50) goto CPyL124;
    CPy_Unreachable();
CPyL40: ;
    cpy_r_r51 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__0;
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__0", -1, CPyStatic_caching___globals);
        goto CPyL129;
    }
    CPy_INCREF(cpy_r_r51);
CPyL41: ;
    cpy_r_r52 = CPyIter_Send(cpy_r_r51, cpy_r_arg);
    CPy_DECREF(cpy_r_r51);
    CPy_DECREF(cpy_r_arg);
    if (cpy_r_r52 == NULL) goto CPyL43;
    cpy_r_r38 = cpy_r_r52;
    goto CPyL24;
CPyL43: ;
    cpy_r_r53 = CPy_FetchStopIterationValue();
    if (unlikely(cpy_r_r53 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 88, CPyStatic_caching___globals);
        goto CPyL124;
    }
    cpy_r_r35 = cpy_r_r53;
    CPy_DECREF(cpy_r_r35);
CPyL45: ;
    cpy_r_r54 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__self;
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "self", 90, CPyStatic_caching___globals);
        goto CPyL53;
    }
    CPy_INCREF_NO_IMM(cpy_r_r54);
CPyL46: ;
    cpy_r_r55 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__last;
    if (unlikely(cpy_r_r55 == 2)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "last", 90, CPyStatic_caching___globals);
        goto CPyL130;
    }
CPyL47: ;
    cpy_r_r56 = CPyDef_caching___SimpleCache___popitem(cpy_r_r54, cpy_r_r55);
    CPy_DECREF_NO_IMM(cpy_r_r54);
    if (unlikely(cpy_r_r56.f0 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 90, CPyStatic_caching___globals);
        goto CPyL53;
    }
    cpy_r_r57 = PyTuple_New(2);
    if (unlikely(cpy_r_r57 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp33 = cpy_r_r56.f0;
    PyTuple_SET_ITEM(cpy_r_r57, 0, __tmp33);
    PyObject *__tmp34 = cpy_r_r56.f1;
    PyTuple_SET_ITEM(cpy_r_r57, 1, __tmp34);
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_next_label__ = -1;
    if (cpy_r_stop_iter_ptr != NULL) goto CPyL52;
    CPyGen_SetStopIterationValue(cpy_r_r57);
    CPy_DECREF(cpy_r_r57);
    if (!0) goto CPyL124;
    CPy_Unreachable();
CPyL52: ;
    *(PyObject * *)cpy_r_stop_iter_ptr = cpy_r_r57;
    return 0;
CPyL53: ;
    cpy_r_r59 = CPy_CatchError();
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2.f0 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2.f0);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2.f1);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2.f2);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2 = cpy_r_r59;
    cpy_r_r60 = 1;
    if (unlikely(!cpy_r_r60)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", -1, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r61 = CPyModule_builtins;
    cpy_r_r62 = CPyStatics[80]; /* 'KeyError' */
    cpy_r_r63 = CPyObject_GetAttr(cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 91, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r64 = CPy_ExceptionMatches(cpy_r_r63);
    CPy_DecRef(cpy_r_r63);
    if (!cpy_r_r64) goto CPyL107;
    cpy_r_r65 = CPyModule_time;
    cpy_r_r66 = CPyStatics[78]; /* 'time' */
    cpy_r_r67 = CPyObject_GetAttr(cpy_r_r65, cpy_r_r66);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 92, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r68 = PyObject_Vectorcall(cpy_r_r67, 0, 0, 0);
    CPy_DecRef(cpy_r_r67);
    if (unlikely(cpy_r_r68 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 92, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r69 = PyFloat_AsDouble(cpy_r_r68);
    if (cpy_r_r69 == -1.0 && PyErr_Occurred()) {
        CPy_TypeError("float", cpy_r_r68); cpy_r_r69 = -113.0;
    }
    CPy_DecRef(cpy_r_r68);
    cpy_r_r70 = cpy_r_r69 == -113.0;
    if (unlikely(cpy_r_r70)) goto CPyL60;
CPyL59: ;
    if (unlikely(cpy_r_r69 == -113.0)) {
        ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap |= 8;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__now = cpy_r_r69;
    cpy_r_r71 = 1;
    if (unlikely(!cpy_r_r71)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 92, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL61;
CPyL60: ;
    cpy_r_r72 = PyErr_Occurred();
    if (unlikely(cpy_r_r72 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 92, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL59;
CPyL61: ;
    cpy_r_r73 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__now;
    if (unlikely(cpy_r_r73 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 8)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'now' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r74 = cpy_r_r73 == -113.0;
    if (unlikely(cpy_r_r74)) goto CPyL63;
CPyL62: ;
    cpy_r_r75 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__end_time;
    if (unlikely(cpy_r_r75 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 4)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'end_time' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r76 = cpy_r_r75 == -113.0;
    if (unlikely(cpy_r_r76)) {
        goto CPyL65;
    } else
        goto CPyL64;
CPyL63: ;
    cpy_r_r77 = PyErr_Occurred();
    if (unlikely(cpy_r_r77 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 93, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL62;
CPyL64: ;
    cpy_r_r78 = cpy_r_r73 >= cpy_r_r75;
    if (cpy_r_r78) {
        goto CPyL66;
    } else
        goto CPyL70;
CPyL65: ;
    cpy_r_r79 = PyErr_Occurred();
    if (unlikely(cpy_r_r79 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 93, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL64;
CPyL66: ;
    cpy_r_r80 = CPyStatics[81]; /* 'Timeout waiting for item to be available' */
    cpy_r_r81 = CPyModule_asyncio;
    cpy_r_r82 = CPyStatics[82]; /* 'TimeoutError' */
    cpy_r_r83 = CPyObject_GetAttr(cpy_r_r81, cpy_r_r82);
    if (unlikely(cpy_r_r83 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 94, CPyStatic_caching___globals);
        goto CPyL111;
    }
    PyObject *cpy_r_r84[1] = {cpy_r_r80};
    cpy_r_r85 = (PyObject **)&cpy_r_r84;
    cpy_r_r86 = PyObject_Vectorcall(cpy_r_r83, cpy_r_r85, 1, 0);
    CPy_DecRef(cpy_r_r83);
    if (unlikely(cpy_r_r86 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 94, CPyStatic_caching___globals);
        goto CPyL111;
    }
    CPy_Raise(cpy_r_r86);
    CPy_DecRef(cpy_r_r86);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 94, CPyStatic_caching___globals);
        goto CPyL111;
    }
    CPy_Unreachable();
CPyL70: ;
    cpy_r_r87 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__end_time;
    if (unlikely(cpy_r_r87 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 4)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'end_time' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r88 = cpy_r_r87 == -113.0;
    if (unlikely(cpy_r_r88)) goto CPyL72;
CPyL71: ;
    cpy_r_r89 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_generator_attribute__now;
    if (unlikely(cpy_r_r89 == -113.0) && !(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->bitmap & 8)) {
        PyErr_SetString(PyExc_AttributeError, "attribute 'now' of 'async_await_and_popitem_SimpleCache_gen' undefined");
    }
    cpy_r_r90 = cpy_r_r89 == -113.0;
    if (unlikely(cpy_r_r90)) {
        goto CPyL74;
    } else
        goto CPyL73;
CPyL72: ;
    cpy_r_r91 = PyErr_Occurred();
    if (unlikely(cpy_r_r91 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL71;
CPyL73: ;
    cpy_r_r92 = cpy_r_r87 - cpy_r_r89;
    cpy_r_r93 = cpy_r_r92 < 0.1;
    if (cpy_r_r93) {
        goto CPyL75;
    } else
        goto CPyL76;
CPyL74: ;
    cpy_r_r94 = PyErr_Occurred();
    if (unlikely(cpy_r_r94 != NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL73;
CPyL75: ;
    cpy_r_r95 = cpy_r_r92;
    goto CPyL77;
CPyL76: ;
    cpy_r_r95 = 0.1;
CPyL77: ;
    cpy_r_r96 = CPyModule_asyncio;
    cpy_r_r97 = CPyStatics[79]; /* 'sleep' */
    cpy_r_r98 = CPyObject_GetAttr(cpy_r_r96, cpy_r_r97);
    if (unlikely(cpy_r_r98 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r99 = PyFloat_FromDouble(cpy_r_r95);
    PyObject *cpy_r_r100[1] = {cpy_r_r99};
    cpy_r_r101 = (PyObject **)&cpy_r_r100;
    cpy_r_r102 = PyObject_Vectorcall(cpy_r_r98, cpy_r_r101, 1, 0);
    CPy_DecRef(cpy_r_r98);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL131;
    }
    CPy_DecRef(cpy_r_r99);
    cpy_r_r103 = CPy_GetCoro(cpy_r_r102);
    CPy_DecRef(cpy_r_r102);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    }
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3 = cpy_r_r103;
    cpy_r_r104 = 1;
    if (unlikely(!cpy_r_r104)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", -1, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r105 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3;
    if (unlikely(cpy_r_r105 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__3", -1, CPyStatic_caching___globals);
        goto CPyL111;
    }
    CPy_INCREF(cpy_r_r105);
CPyL82: ;
    cpy_r_r106 = CPyIter_Next(cpy_r_r105);
    CPy_DecRef(cpy_r_r105);
    if (cpy_r_r106 != NULL) goto CPyL85;
    cpy_r_r107 = CPy_FetchStopIterationValue();
    if (unlikely(cpy_r_r107 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r108 = cpy_r_r107;
    CPy_DecRef(cpy_r_r108);
    cpy_r_r109 = NULL;
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3 = cpy_r_r109;
    cpy_r_r110 = 1;
    if (unlikely(!cpy_r_r110)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    } else
        goto CPyL109;
CPyL85: ;
    cpy_r_r111 = cpy_r_r106;
CPyL86: ;
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_next_label__ = 2;
    return cpy_r_r111;
CPyL87: ;
    cpy_r_r113 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r114 = cpy_r_type != cpy_r_r113;
    if (!cpy_r_r114) goto CPyL132;
    CPyErr_SetObjectAndTraceback(cpy_r_type, cpy_r_value, cpy_r_traceback);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL91;
    } else
        goto CPyL133;
CPyL89: ;
    CPy_Unreachable();
CPyL90: ;
    CPy_INCREF(cpy_r_arg);
    goto CPyL102;
CPyL91: ;
    cpy_r_r115 = CPy_CatchError();
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4.f0 != NULL) {
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4.f0);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4.f1);
        CPy_DECREF(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4.f2);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4 = cpy_r_r115;
    cpy_r_r116 = 1;
    if (unlikely(!cpy_r_r116)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", -1, CPyStatic_caching___globals);
        goto CPyL134;
    }
    cpy_r_r117 = (PyObject **)&cpy_r_r3;
    cpy_r_r118 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3;
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__3", -1, CPyStatic_caching___globals);
        goto CPyL134;
    }
    CPy_INCREF(cpy_r_r118);
CPyL93: ;
    cpy_r_r119 = CPy_YieldFromErrorHandle(cpy_r_r118, cpy_r_r117);
    CPy_DecRef(cpy_r_r118);
    if (unlikely(cpy_r_r119 == 2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL134;
    }
    if (cpy_r_r119) goto CPyL97;
    cpy_r_r111 = cpy_r_r3;
    cpy_r_r120 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4;
    if (unlikely(cpy_r_r120.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__4", -1, CPyStatic_caching___globals);
        goto CPyL135;
    }
    CPy_INCREF(cpy_r_r120.f0);
    CPy_INCREF(cpy_r_r120.f1);
    CPy_INCREF(cpy_r_r120.f2);
CPyL96: ;
    CPy_RestoreExcInfo(cpy_r_r120);
    CPy_DecRef(cpy_r_r120.f0);
    CPy_DecRef(cpy_r_r120.f1);
    CPy_DecRef(cpy_r_r120.f2);
    goto CPyL86;
CPyL97: ;
    cpy_r_r108 = cpy_r_r3;
    CPy_DecRef(cpy_r_r108);
    cpy_r_r121 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4;
    if (unlikely(cpy_r_r121.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__4", -1, CPyStatic_caching___globals);
        goto CPyL99;
    }
    CPy_INCREF(cpy_r_r121.f0);
    CPy_INCREF(cpy_r_r121.f1);
    CPy_INCREF(cpy_r_r121.f2);
CPyL98: ;
    CPy_RestoreExcInfo(cpy_r_r121);
    CPy_DecRef(cpy_r_r121.f0);
    CPy_DecRef(cpy_r_r121.f1);
    CPy_DecRef(cpy_r_r121.f2);
    goto CPyL109;
CPyL99: ;
    cpy_r_r122 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__4;
    if (unlikely(cpy_r_r122.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__4", -1, CPyStatic_caching___globals);
        goto CPyL111;
    }
    CPy_INCREF(cpy_r_r122.f0);
    CPy_INCREF(cpy_r_r122.f1);
    CPy_INCREF(cpy_r_r122.f2);
CPyL100: ;
    CPy_RestoreExcInfo(cpy_r_r122);
    CPy_DecRef(cpy_r_r122.f0);
    CPy_DecRef(cpy_r_r122.f1);
    CPy_DecRef(cpy_r_r122.f2);
    cpy_r_r123 = CPy_KeepPropagating();
    if (!cpy_r_r123) goto CPyL111;
    CPy_Unreachable();
CPyL102: ;
    cpy_r_r124 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__3;
    if (unlikely(cpy_r_r124 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__3", -1, CPyStatic_caching___globals);
        goto CPyL136;
    }
    CPy_INCREF(cpy_r_r124);
CPyL103: ;
    cpy_r_r125 = CPyIter_Send(cpy_r_r124, cpy_r_arg);
    CPy_DECREF(cpy_r_r124);
    CPy_DECREF(cpy_r_arg);
    if (cpy_r_r125 == NULL) goto CPyL105;
    cpy_r_r111 = cpy_r_r125;
    goto CPyL86;
CPyL105: ;
    cpy_r_r126 = CPy_FetchStopIterationValue();
    if (unlikely(cpy_r_r126 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 97, CPyStatic_caching___globals);
        goto CPyL111;
    }
    cpy_r_r108 = cpy_r_r126;
    CPy_DECREF(cpy_r_r108);
    goto CPyL109;
CPyL107: ;
    CPy_Reraise();
    if (!0) goto CPyL111;
    CPy_Unreachable();
CPyL109: ;
    cpy_r_r127 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2;
    if (unlikely(cpy_r_r127.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__2", -1, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_INCREF(cpy_r_r127.f0);
    CPy_INCREF(cpy_r_r127.f1);
    CPy_INCREF(cpy_r_r127.f2);
CPyL110: ;
    CPy_RestoreExcInfo(cpy_r_r127);
    CPy_DECREF(cpy_r_r127.f0);
    CPy_DECREF(cpy_r_r127.f1);
    CPy_DECREF(cpy_r_r127.f2);
    goto CPyL14;
CPyL111: ;
    cpy_r_r128 = ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_temp__2;
    if (unlikely(cpy_r_r128.f0 == NULL)) {
        CPy_AttributeError("faster_web3/utils/caching.py", "async_await_and_popitem", "async_await_and_popitem_SimpleCache_gen", "__mypyc_temp__2", -1, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_INCREF(cpy_r_r128.f0);
    CPy_INCREF(cpy_r_r128.f1);
    CPy_INCREF(cpy_r_r128.f2);
CPyL112: ;
    CPy_RestoreExcInfo(cpy_r_r128);
    CPy_DecRef(cpy_r_r128.f0);
    CPy_DecRef(cpy_r_r128.f1);
    CPy_DecRef(cpy_r_r128.f2);
    cpy_r_r129 = CPy_KeepPropagating();
    if (!cpy_r_r129) goto CPyL124;
    CPy_Unreachable();
CPyL114: ;
    cpy_r_r130 = Py_None;
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r___mypyc_self__)->___mypyc_next_label__ = -1;
    if (cpy_r_stop_iter_ptr != NULL) goto CPyL118;
    CPyGen_SetStopIterationValue(cpy_r_r130);
    if (!0) goto CPyL124;
    CPy_Unreachable();
CPyL118: ;
    *(PyObject * *)cpy_r_stop_iter_ptr = cpy_r_r130;
    return 0;
CPyL119: ;
    cpy_r_r132 = cpy_r_r4 == 0;
    if (cpy_r_r132) goto CPyL137;
    cpy_r_r133 = cpy_r_r4 == 1;
    if (cpy_r_r133) {
        goto CPyL138;
    } else
        goto CPyL139;
CPyL121: ;
    cpy_r_r134 = cpy_r_r4 == 2;
    if (cpy_r_r134) {
        goto CPyL87;
    } else
        goto CPyL140;
CPyL122: ;
    PyErr_SetNone(PyExc_StopIteration);
    cpy_r_r135 = 0;
    if (unlikely(!cpy_r_r135)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL124;
    }
    CPy_Unreachable();
CPyL124: ;
    cpy_r_r136 = NULL;
    return cpy_r_r136;
CPyL125: ;
    CPy_XDECREF(cpy_r_r1);
    goto CPyL28;
CPyL126: ;
    CPy_XDECREF(cpy_r_r1);
    goto CPyL27;
CPyL127: ;
    CPy_XDecRef(cpy_r_r1);
    goto CPyL37;
CPyL128: ;
    CPy_DecRef(cpy_r_r38);
    goto CPyL37;
CPyL129: ;
    CPy_DecRef(cpy_r_arg);
    goto CPyL124;
CPyL130: ;
    CPy_DecRef(cpy_r_r54);
    goto CPyL53;
CPyL131: ;
    CPy_DecRef(cpy_r_r99);
    goto CPyL111;
CPyL132: ;
    CPy_XDECREF(cpy_r_r3);
    goto CPyL90;
CPyL133: ;
    CPy_XDECREF(cpy_r_r3);
    goto CPyL89;
CPyL134: ;
    CPy_XDecRef(cpy_r_r3);
    goto CPyL99;
CPyL135: ;
    CPy_DecRef(cpy_r_r111);
    goto CPyL99;
CPyL136: ;
    CPy_DecRef(cpy_r_arg);
    goto CPyL111;
CPyL137: ;
    CPy_XDECREF(cpy_r_r1);
    CPy_XDECREF(cpy_r_r3);
    goto CPyL1;
CPyL138: ;
    CPy_XDECREF(cpy_r_r3);
    goto CPyL25;
CPyL139: ;
    CPy_XDECREF(cpy_r_r1);
    goto CPyL121;
CPyL140: ;
    CPy_XDECREF(cpy_r_r3);
    goto CPyL122;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____next__(PyObject *cpy_r___mypyc_self__) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    cpy_r_r0 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r1 = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__(cpy_r___mypyc_self__, cpy_r_r0, cpy_r_r0, cpy_r_r0, cpy_r_r0, 0);
    if (cpy_r_r1 == NULL) goto CPyL2;
    return cpy_r_r1;
CPyL2: ;
    cpy_r_r2 = NULL;
    return cpy_r_r2;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____next__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":__next__", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____next__(arg___mypyc_self__);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__next__", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___send(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    cpy_r_r0 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r1 = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__(cpy_r___mypyc_self__, cpy_r_r0, cpy_r_r0, cpy_r_r0, cpy_r_arg, 0);
    if (cpy_r_r1 == NULL) goto CPyL2;
    return cpy_r_r1;
CPyL2: ;
    cpy_r_r2 = NULL;
    return cpy_r_r2;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___send(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"arg", 0};
    static CPyArg_Parser parser = {"O:send", kwlist, 0};
    PyObject *obj_arg;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_arg)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *arg_arg = obj_arg;
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen___send(arg___mypyc_self__, arg_arg);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "send", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____iter__(PyObject *cpy_r___mypyc_self__) {
    CPy_INCREF_NO_IMM(cpy_r___mypyc_self__);
    return cpy_r___mypyc_self__;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____iter__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":__iter__", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____iter__(arg___mypyc_self__);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__iter__", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___throw(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    cpy_r_r0 = (PyObject *)&_Py_NoneStruct;
    if (cpy_r_value != NULL) goto CPyL7;
    CPy_INCREF(cpy_r_r0);
    cpy_r_value = cpy_r_r0;
CPyL2: ;
    if (cpy_r_traceback != NULL) goto CPyL8;
    CPy_INCREF(cpy_r_r0);
    cpy_r_traceback = cpy_r_r0;
CPyL4: ;
    cpy_r_r1 = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__(cpy_r___mypyc_self__, cpy_r_type, cpy_r_value, cpy_r_traceback, cpy_r_r0, 0);
    CPy_DECREF(cpy_r_value);
    CPy_DECREF(cpy_r_traceback);
    if (cpy_r_r1 == NULL) goto CPyL6;
    return cpy_r_r1;
CPyL6: ;
    cpy_r_r2 = NULL;
    return cpy_r_r2;
CPyL7: ;
    CPy_INCREF(cpy_r_value);
    goto CPyL2;
CPyL8: ;
    CPy_INCREF(cpy_r_traceback);
    goto CPyL4;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___throw(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {"type", "value", "traceback", 0};
    static CPyArg_Parser parser = {"O|OO:throw", kwlist, 0};
    PyObject *obj_type;
    PyObject *obj_value = NULL;
    PyObject *obj_traceback = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_type, &obj_value, &obj_traceback)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *arg_type = obj_type;
    PyObject *arg_value;
    if (obj_value == NULL) {
        arg_value = NULL;
    } else {
        arg_value = obj_value; 
    }
    PyObject *arg_traceback;
    if (obj_traceback == NULL) {
        arg_traceback = NULL;
    } else {
        arg_traceback = obj_traceback; 
    }
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen___throw(arg___mypyc_self__, arg_type, arg_value, arg_traceback);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "throw", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___close(PyObject *cpy_r___mypyc_self__) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    tuple_T3OOO cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    tuple_T2OO cpy_r_r10;
    PyObject *cpy_r_r11;
    char cpy_r_r12;
    PyObject *cpy_r_r13;
    char cpy_r_r14;
    PyObject *cpy_r_r15;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = CPyStatics[83]; /* 'GeneratorExit' */
    cpy_r_r2 = CPyObject_GetAttr(cpy_r_r0, cpy_r_r1);
    if (cpy_r_r2 == NULL) goto CPyL3;
    cpy_r_r3 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r4 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r5 = CPyDef_caching___async_await_and_popitem_SimpleCache_gen___throw(cpy_r___mypyc_self__, cpy_r_r2, cpy_r_r3, cpy_r_r4);
    if (cpy_r_r5 != NULL) goto CPyL11;
CPyL3: ;
    cpy_r_r6 = CPy_CatchError();
    cpy_r_r7 = CPyModule_builtins;
    cpy_r_r8 = CPyStatics[84]; /* 'StopIteration' */
    cpy_r_r9 = CPyObject_GetAttr(cpy_r_r7, cpy_r_r8);
    if (cpy_r_r9 == NULL) goto CPyL12;
    cpy_r_r10.f0 = cpy_r_r2;
    cpy_r_r10.f1 = cpy_r_r9;
    cpy_r_r11 = PyTuple_New(2);
    if (unlikely(cpy_r_r11 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp35 = cpy_r_r10.f0;
    PyTuple_SET_ITEM(cpy_r_r11, 0, __tmp35);
    PyObject *__tmp36 = cpy_r_r10.f1;
    PyTuple_SET_ITEM(cpy_r_r11, 1, __tmp36);
    cpy_r_r12 = CPy_ExceptionMatches(cpy_r_r11);
    CPy_DECREF(cpy_r_r11);
    if (!cpy_r_r12) goto CPyL13;
    CPy_RestoreExcInfo(cpy_r_r6);
    CPy_DECREF(cpy_r_r6.f0);
    CPy_DECREF(cpy_r_r6.f1);
    CPy_DECREF(cpy_r_r6.f2);
    cpy_r_r13 = (PyObject *)&_Py_NoneStruct;
    CPy_INCREF(cpy_r_r13);
    return cpy_r_r13;
CPyL6: ;
    CPy_Reraise();
    if (!0) goto CPyL10;
    CPy_Unreachable();
CPyL8: ;
    PyErr_SetString(PyExc_RuntimeError, "generator ignored GeneratorExit");
    cpy_r_r14 = 0;
    if (!cpy_r_r14) goto CPyL10;
    CPy_Unreachable();
CPyL10: ;
    cpy_r_r15 = NULL;
    return cpy_r_r15;
CPyL11: ;
    CPy_DECREF(cpy_r_r2);
    CPy_DECREF(cpy_r_r5);
    goto CPyL8;
CPyL12: ;
    CPy_DECREF(cpy_r_r2);
    CPy_DECREF(cpy_r_r6.f0);
    CPy_DECREF(cpy_r_r6.f1);
    CPy_DECREF(cpy_r_r6.f2);
    goto CPyL10;
CPyL13: ;
    CPy_DECREF(cpy_r_r6.f0);
    CPy_DECREF(cpy_r_r6.f1);
    CPy_DECREF(cpy_r_r6.f2);
    goto CPyL6;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___close(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":close", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen___close(arg___mypyc_self__);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "close", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____await__(PyObject *cpy_r___mypyc_self__) {
    CPy_INCREF_NO_IMM(cpy_r___mypyc_self__);
    return cpy_r___mypyc_self__;
}

PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____await__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj___mypyc_self__ = self;
    static const char * const kwlist[] = {0};
    static CPyArg_Parser parser = {":__await__", kwlist, 0};
    if (!CPyArg_ParseStackAndKeywordsNoArgs(args, nargs, kwnames, &parser)) {
        return NULL;
    }
    PyObject *arg___mypyc_self__;
    if (likely(Py_TYPE(obj___mypyc_self__) == CPyType_caching___async_await_and_popitem_SimpleCache_gen))
        arg___mypyc_self__ = obj___mypyc_self__;
    else {
        CPy_TypeError("faster_web3.utils.caching.async_await_and_popitem_SimpleCache_gen", obj___mypyc_self__); 
        goto fail;
    }
    PyObject *retval = CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____await__(arg___mypyc_self__);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "__await__", -1, CPyStatic_caching___globals);
    return NULL;
}

PyObject *CPyDef_caching___SimpleCache___async_await_and_popitem(PyObject *cpy_r_self, char cpy_r_last, double cpy_r_timeout, uint32_t cpy_r___bitmap) {
    uint32_t cpy_r_r0;
    char cpy_r_r1;
    PyObject *cpy_r_r2;
    char cpy_r_r3;
    char cpy_r_r4;
    char cpy_r_r5;
    char cpy_r_r6;
    PyObject *cpy_r_r7;
    if (cpy_r_last != 2) goto CPyL2;
    cpy_r_last = 1;
CPyL2: ;
    cpy_r_r0 = cpy_r___bitmap & 1;
    cpy_r_r1 = cpy_r_r0 == 0;
    if (!cpy_r_r1) goto CPyL4;
    cpy_r_timeout = 10.0;
CPyL4: ;
    cpy_r_r2 = CPyDef_caching___async_await_and_popitem_SimpleCache_gen();
    if (unlikely(cpy_r_r2 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL9;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_next_label__ = 0;
    CPy_INCREF_NO_IMM(cpy_r_self);
    if (((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_generator_attribute__self != NULL) {
        CPy_DECREF_NO_IMM(((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_generator_attribute__self);
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_generator_attribute__self = cpy_r_self;
    cpy_r_r4 = 1;
    if (unlikely(!cpy_r_r4)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL10;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_generator_attribute__last = cpy_r_last;
    cpy_r_r5 = 1;
    if (unlikely(!cpy_r_r5)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL10;
    }
    if (unlikely(cpy_r_timeout == -113.0)) {
        ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->bitmap |= 1;
    }
    ((faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *)cpy_r_r2)->___mypyc_generator_attribute__timeout = cpy_r_timeout;
    cpy_r_r6 = 1;
    if (unlikely(!cpy_r_r6)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
        goto CPyL10;
    }
    return cpy_r_r2;
CPyL9: ;
    cpy_r_r7 = NULL;
    return cpy_r_r7;
CPyL10: ;
    CPy_DecRef(cpy_r_r2);
    goto CPyL9;
}

PyObject *CPyPy_caching___SimpleCache___async_await_and_popitem(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    PyObject *obj_self = self;
    static const char * const kwlist[] = {"last", "timeout", 0};
    static CPyArg_Parser parser = {"|OO:async_await_and_popitem", kwlist, 0};
    PyObject *obj_last = NULL;
    PyObject *obj_timeout = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_last, &obj_timeout)) {
        return NULL;
    }
    uint32_t __bitmap = 0;
    PyObject *arg_self;
    if (likely(Py_TYPE(obj_self) == CPyType_caching___SimpleCache))
        arg_self = obj_self;
    else {
        CPy_TypeError("faster_web3.utils.caching.SimpleCache", obj_self); 
        goto fail;
    }
    char arg_last;
    if (obj_last == NULL) {
        arg_last = 2;
    } else if (unlikely(!PyBool_Check(obj_last))) {
        CPy_TypeError("bool", obj_last); goto fail;
    } else
        arg_last = obj_last == Py_True;
    double arg_timeout = -113.0;
    if (obj_timeout != NULL) {
        __bitmap |= 1 << 0;
        arg_timeout = PyFloat_AsDouble(obj_timeout);
        if (arg_timeout == -1.0 && PyErr_Occurred()) {
            CPy_TypeError("float", obj_timeout); goto fail;
        }
    }
    PyObject *retval = CPyDef_caching___SimpleCache___async_await_and_popitem(arg_self, arg_last, arg_timeout, __bitmap);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/utils/caching.py", "async_await_and_popitem", 82, CPyStatic_caching___globals);
    return NULL;
}

char CPyDef_caching_____top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject **cpy_r_r5;
    void *cpy_r_r7;
    void *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    PyObject *cpy_r_r13;
    char cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    PyObject **cpy_r_r23;
    void *cpy_r_r25;
    void *cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject *cpy_r_r29;
    PyObject *cpy_r_r30;
    PyObject *cpy_r_r31;
    char cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    PyObject *cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject **cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    int32_t cpy_r_r46;
    char cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    char cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject *cpy_r_r57;
    PyObject *cpy_r_r58;
    PyObject **cpy_r_r60;
    PyObject *cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    PyObject *cpy_r_r64;
    PyObject *cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    int32_t cpy_r_r68;
    char cpy_r_r69;
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
    PyObject *cpy_r_r86;
    PyObject *cpy_r_r87;
    int32_t cpy_r_r88;
    char cpy_r_r89;
    PyObject *cpy_r_r90;
    PyObject *cpy_r_r91;
    int32_t cpy_r_r92;
    char cpy_r_r93;
    PyObject **cpy_r_r95;
    PyObject *cpy_r_r96;
    PyObject *cpy_r_r97;
    PyObject *cpy_r_r98;
    PyObject *cpy_r_r99;
    PyObject **cpy_r_r101;
    PyObject *cpy_r_r102;
    PyObject *cpy_r_r103;
    PyObject *cpy_r_r104;
    int32_t cpy_r_r105;
    char cpy_r_r106;
    PyObject *cpy_r_r107;
    PyObject *cpy_r_r108;
    PyObject *cpy_r_r109;
    PyObject *cpy_r_r110;
    PyObject *cpy_r_r111;
    PyObject *cpy_r_r112;
    PyObject *cpy_r_r113;
    PyObject *cpy_r_r114;
    PyObject *cpy_r_r115;
    PyObject *cpy_r_r116;
    PyObject *cpy_r_r117;
    PyObject *cpy_r_r118;
    PyObject *cpy_r_r119;
    PyObject *cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    char cpy_r_r123;
    PyObject *cpy_r_r124;
    PyObject *cpy_r_r125;
    PyObject *cpy_r_r126;
    PyObject *cpy_r_r127;
    PyObject *cpy_r_r128;
    int32_t cpy_r_r129;
    char cpy_r_r130;
    PyObject *cpy_r_r131;
    PyObject *cpy_r_r132;
    int32_t cpy_r_r133;
    char cpy_r_r134;
    char cpy_r_r135;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[14]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", -1, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = (PyObject **)&CPyModule_asyncio;
    PyObject **cpy_r_r6[1] = {cpy_r_r5};
    cpy_r_r7 = (void *)&cpy_r_r6;
    int64_t cpy_r_r8[1] = {1};
    cpy_r_r9 = (void *)&cpy_r_r8;
    cpy_r_r10 = CPyStatics[127]; /* (('asyncio', 'asyncio', 'asyncio'),) */
    cpy_r_r11 = CPyStatic_caching___globals;
    cpy_r_r12 = CPyStatics[86]; /* 'faster_web3/utils/caching.py' */
    cpy_r_r13 = CPyStatics[26]; /* '<module>' */
    cpy_r_r14 = CPyImport_ImportMany(cpy_r_r10, cpy_r_r7, cpy_r_r11, cpy_r_r12, cpy_r_r13, cpy_r_r9);
    if (!cpy_r_r14) goto CPyL45;
    cpy_r_r15 = CPyStatics[128]; /* ('OrderedDict',) */
    cpy_r_r16 = CPyStatics[87]; /* 'collections' */
    cpy_r_r17 = CPyStatic_caching___globals;
    cpy_r_r18 = CPyImport_ImportFromMany(cpy_r_r16, cpy_r_r15, cpy_r_r15, cpy_r_r17);
    if (unlikely(cpy_r_r18 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 2, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyModule_collections = cpy_r_r18;
    CPy_INCREF(CPyModule_collections);
    CPy_DECREF(cpy_r_r18);
    cpy_r_r19 = CPyStatics[129]; /* ('Enum',) */
    cpy_r_r20 = CPyStatics[89]; /* 'enum' */
    cpy_r_r21 = CPyStatic_caching___globals;
    cpy_r_r22 = CPyImport_ImportFromMany(cpy_r_r20, cpy_r_r19, cpy_r_r19, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 5, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyModule_enum = cpy_r_r22;
    CPy_INCREF(CPyModule_enum);
    CPy_DECREF(cpy_r_r22);
    cpy_r_r23 = (PyObject **)&CPyModule_time;
    PyObject **cpy_r_r24[1] = {cpy_r_r23};
    cpy_r_r25 = (void *)&cpy_r_r24;
    int64_t cpy_r_r26[1] = {8};
    cpy_r_r27 = (void *)&cpy_r_r26;
    cpy_r_r28 = CPyStatics[131]; /* (('time', 'time', 'time'),) */
    cpy_r_r29 = CPyStatic_caching___globals;
    cpy_r_r30 = CPyStatics[86]; /* 'faster_web3/utils/caching.py' */
    cpy_r_r31 = CPyStatics[26]; /* '<module>' */
    cpy_r_r32 = CPyImport_ImportMany(cpy_r_r28, cpy_r_r25, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r27);
    if (!cpy_r_r32) goto CPyL45;
    cpy_r_r33 = CPyStatics[132]; /* ('Any', 'Dict', 'Final', 'Generic', 'List', 'Optional',
                                    'Tuple', 'TypeVar', 'final') */
    cpy_r_r34 = CPyStatics[22]; /* 'typing' */
    cpy_r_r35 = CPyStatic_caching___globals;
    cpy_r_r36 = CPyImport_ImportFromMany(cpy_r_r34, cpy_r_r33, cpy_r_r33, cpy_r_r35);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 9, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyModule_typing = cpy_r_r36;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r36);
    cpy_r_r37 = CPyStatics[94]; /* 'T' */
    cpy_r_r38 = CPyStatic_caching___globals;
    cpy_r_r39 = CPyStatics[92]; /* 'TypeVar' */
    cpy_r_r40 = CPyDict_GetItem(cpy_r_r38, cpy_r_r39);
    if (unlikely(cpy_r_r40 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 22, CPyStatic_caching___globals);
        goto CPyL45;
    }
    PyObject *cpy_r_r41[1] = {cpy_r_r37};
    cpy_r_r42 = (PyObject **)&cpy_r_r41;
    cpy_r_r43 = PyObject_Vectorcall(cpy_r_r40, cpy_r_r42, 1, 0);
    CPy_DECREF(cpy_r_r40);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 22, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r44 = CPyStatic_caching___globals;
    cpy_r_r45 = CPyStatics[94]; /* 'T' */
    cpy_r_r46 = CPyDict_SetItem(cpy_r_r44, cpy_r_r45, cpy_r_r43);
    CPy_DECREF(cpy_r_r43);
    cpy_r_r47 = cpy_r_r46 >= 0;
    if (unlikely(!cpy_r_r47)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 22, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r48 = CPyModule_enum;
    cpy_r_r49 = CPyStatics[88]; /* 'Enum' */
    cpy_r_r50 = CPyObject_GetAttr(cpy_r_r48, cpy_r_r49);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r51 = PyTuple_Pack(1, cpy_r_r50);
    CPy_DECREF(cpy_r_r50);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r52 = (PyObject *)&PyType_Type;
    cpy_r_r53 = CPy_CalculateMetaclass(cpy_r_r52, cpy_r_r51);
    if (unlikely(cpy_r_r53 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL46;
    }
    cpy_r_r54 = CPyStatics[33]; /* '__prepare__' */
    cpy_r_r55 = PyObject_HasAttr(cpy_r_r53, cpy_r_r54);
    if (!cpy_r_r55) goto CPyL19;
    cpy_r_r56 = CPyStatics[95]; /* 'RequestCacheValidationThreshold' */
    cpy_r_r57 = CPyStatics[33]; /* '__prepare__' */
    cpy_r_r58 = CPyObject_GetAttr(cpy_r_r53, cpy_r_r57);
    if (unlikely(cpy_r_r58 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL46;
    }
    PyObject *cpy_r_r59[2] = {cpy_r_r56, cpy_r_r51};
    cpy_r_r60 = (PyObject **)&cpy_r_r59;
    cpy_r_r61 = PyObject_Vectorcall(cpy_r_r58, cpy_r_r60, 2, 0);
    CPy_DECREF(cpy_r_r58);
    if (unlikely(cpy_r_r61 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL46;
    }
    if (likely(PyDict_Check(cpy_r_r61)))
        cpy_r_r62 = cpy_r_r61;
    else {
        CPy_TypeErrorTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals, "dict", cpy_r_r61);
        goto CPyL46;
    }
    cpy_r_r63 = cpy_r_r62;
    goto CPyL21;
CPyL19: ;
    cpy_r_r64 = PyDict_New();
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL46;
    }
    cpy_r_r63 = cpy_r_r64;
CPyL21: ;
    cpy_r_r65 = PyDict_New();
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL47;
    }
    cpy_r_r66 = (PyObject *)&PyUnicode_Type;
    cpy_r_r67 = CPyStatics[96]; /* 'FINALIZED' */
    cpy_r_r68 = PyDict_SetItem(cpy_r_r65, cpy_r_r67, cpy_r_r66);
    cpy_r_r69 = cpy_r_r68 >= 0;
    if (unlikely(!cpy_r_r69)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 27, CPyStatic_caching___globals);
        goto CPyL48;
    }
    cpy_r_r70 = CPyStatics[97]; /* 'finalized' */
    cpy_r_r71 = CPyStatics[96]; /* 'FINALIZED' */
    cpy_r_r72 = CPyDict_SetItem(cpy_r_r63, cpy_r_r71, cpy_r_r70);
    cpy_r_r73 = cpy_r_r72 >= 0;
    if (unlikely(!cpy_r_r73)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 27, CPyStatic_caching___globals);
        goto CPyL48;
    }
    cpy_r_r74 = (PyObject *)&PyUnicode_Type;
    cpy_r_r75 = CPyStatics[98]; /* 'SAFE' */
    cpy_r_r76 = PyDict_SetItem(cpy_r_r65, cpy_r_r75, cpy_r_r74);
    cpy_r_r77 = cpy_r_r76 >= 0;
    if (unlikely(!cpy_r_r77)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 28, CPyStatic_caching___globals);
        goto CPyL48;
    }
    cpy_r_r78 = CPyStatics[99]; /* 'safe' */
    cpy_r_r79 = CPyStatics[98]; /* 'SAFE' */
    cpy_r_r80 = CPyDict_SetItem(cpy_r_r63, cpy_r_r79, cpy_r_r78);
    cpy_r_r81 = cpy_r_r80 >= 0;
    if (unlikely(!cpy_r_r81)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 28, CPyStatic_caching___globals);
        goto CPyL48;
    }
    cpy_r_r82 = CPyStatics[95]; /* 'RequestCacheValidationThreshold' */
    cpy_r_r83 = CPyStatics[36]; /* '__annotations__' */
    cpy_r_r84 = CPyDict_SetItem(cpy_r_r63, cpy_r_r83, cpy_r_r65);
    CPy_DECREF(cpy_r_r65);
    cpy_r_r85 = cpy_r_r84 >= 0;
    if (unlikely(!cpy_r_r85)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL47;
    }
    cpy_r_r86 = CPyStatics[37]; /* 'mypyc filler docstring' */
    cpy_r_r87 = CPyStatics[38]; /* '__doc__' */
    cpy_r_r88 = CPyDict_SetItem(cpy_r_r63, cpy_r_r87, cpy_r_r86);
    cpy_r_r89 = cpy_r_r88 >= 0;
    if (unlikely(!cpy_r_r89)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL47;
    }
    cpy_r_r90 = CPyStatics[100]; /* 'faster_web3.utils.caching' */
    cpy_r_r91 = CPyStatics[40]; /* '__module__' */
    cpy_r_r92 = CPyDict_SetItem(cpy_r_r63, cpy_r_r91, cpy_r_r90);
    cpy_r_r93 = cpy_r_r92 >= 0;
    if (unlikely(!cpy_r_r93)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL47;
    }
    PyObject *cpy_r_r94[3] = {cpy_r_r82, cpy_r_r51, cpy_r_r63};
    cpy_r_r95 = (PyObject **)&cpy_r_r94;
    cpy_r_r96 = PyObject_Vectorcall(cpy_r_r53, cpy_r_r95, 3, 0);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL47;
    }
    CPy_DECREF(cpy_r_r51);
    CPy_DECREF(cpy_r_r63);
    cpy_r_r97 = CPyStatic_caching___globals;
    cpy_r_r98 = CPyStatics[93]; /* 'final' */
    cpy_r_r99 = CPyDict_GetItem(cpy_r_r97, cpy_r_r98);
    if (unlikely(cpy_r_r99 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 25, CPyStatic_caching___globals);
        goto CPyL49;
    }
    PyObject *cpy_r_r100[1] = {cpy_r_r96};
    cpy_r_r101 = (PyObject **)&cpy_r_r100;
    cpy_r_r102 = PyObject_Vectorcall(cpy_r_r99, cpy_r_r101, 1, 0);
    CPy_DECREF(cpy_r_r99);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL49;
    }
    CPy_DECREF(cpy_r_r96);
    CPyType_caching___RequestCacheValidationThreshold = (PyTypeObject *)cpy_r_r102;
    CPy_INCREF(CPyType_caching___RequestCacheValidationThreshold);
    cpy_r_r103 = CPyStatic_caching___globals;
    cpy_r_r104 = CPyStatics[95]; /* 'RequestCacheValidationThreshold' */
    cpy_r_r105 = PyDict_SetItem(cpy_r_r103, cpy_r_r104, cpy_r_r102);
    CPy_DECREF(cpy_r_r102);
    cpy_r_r106 = cpy_r_r105 >= 0;
    if (unlikely(!cpy_r_r106)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r107 = (PyObject *)CPyType_caching___RequestCacheValidationThreshold;
    cpy_r_r108 = CPyStatics[96]; /* 'FINALIZED' */
    cpy_r_r109 = CPyObject_GetAttr(cpy_r_r107, cpy_r_r108);
    if (unlikely(cpy_r_r109 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyStatic_caching___RequestCacheValidationThreshold___FINALIZED = cpy_r_r109;
    CPy_INCREF(CPyStatic_caching___RequestCacheValidationThreshold___FINALIZED);
    CPy_DECREF(cpy_r_r109);
    cpy_r_r110 = CPyStatics[98]; /* 'SAFE' */
    cpy_r_r111 = CPyObject_GetAttr(cpy_r_r107, cpy_r_r110);
    if (unlikely(cpy_r_r111 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 26, CPyStatic_caching___globals);
        goto CPyL45;
    }
    CPyStatic_caching___RequestCacheValidationThreshold___SAFE = cpy_r_r111;
    CPy_INCREF(CPyStatic_caching___RequestCacheValidationThreshold___SAFE);
    CPy_DECREF(cpy_r_r111);
    cpy_r_r112 = CPyStatic_caching___globals;
    cpy_r_r113 = CPyStatics[90]; /* 'Generic' */
    cpy_r_r114 = CPyDict_GetItem(cpy_r_r112, cpy_r_r113);
    if (unlikely(cpy_r_r114 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r115 = CPyStatic_caching___globals;
    cpy_r_r116 = CPyStatics[94]; /* 'T' */
    cpy_r_r117 = CPyDict_GetItem(cpy_r_r115, cpy_r_r116);
    if (unlikely(cpy_r_r117 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL50;
    }
    cpy_r_r118 = PyObject_GetItem(cpy_r_r114, cpy_r_r117);
    CPy_DECREF(cpy_r_r114);
    CPy_DECREF(cpy_r_r117);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r119 = PyTuple_Pack(1, cpy_r_r118);
    CPy_DECREF(cpy_r_r118);
    if (unlikely(cpy_r_r119 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r120 = CPyStatics[100]; /* 'faster_web3.utils.caching' */
    cpy_r_r121 = (PyObject *)CPyType_caching___SimpleCache_template;
    cpy_r_r122 = CPyType_FromTemplate(cpy_r_r121, cpy_r_r119, cpy_r_r120);
    CPy_DECREF(cpy_r_r119);
    if (unlikely(cpy_r_r122 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL45;
    }
    cpy_r_r123 = CPyDef_caching___SimpleCache_trait_vtable_setup();
    if (unlikely(cpy_r_r123 == 2)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", -1, CPyStatic_caching___globals);
        goto CPyL51;
    }
    cpy_r_r124 = CPyStatics[101]; /* '__mypyc_attrs__' */
    cpy_r_r125 = CPyStatics[102]; /* '_size' */
    cpy_r_r126 = CPyStatics[103]; /* '_data' */
    cpy_r_r127 = CPyStatics[11]; /* '__dict__' */
    cpy_r_r128 = PyTuple_Pack(3, cpy_r_r125, cpy_r_r126, cpy_r_r127);
    if (unlikely(cpy_r_r128 == NULL)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL51;
    }
    cpy_r_r129 = PyObject_SetAttr(cpy_r_r122, cpy_r_r124, cpy_r_r128);
    CPy_DECREF(cpy_r_r128);
    cpy_r_r130 = cpy_r_r129 >= 0;
    if (unlikely(!cpy_r_r130)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL51;
    }
    CPyType_caching___SimpleCache = (PyTypeObject *)cpy_r_r122;
    CPy_INCREF(CPyType_caching___SimpleCache);
    cpy_r_r131 = CPyStatic_caching___globals;
    cpy_r_r132 = CPyStatics[104]; /* 'SimpleCache' */
    cpy_r_r133 = PyDict_SetItem(cpy_r_r131, cpy_r_r132, cpy_r_r122);
    CPy_DECREF(cpy_r_r122);
    cpy_r_r134 = cpy_r_r133 >= 0;
    if (unlikely(!cpy_r_r134)) {
        CPy_AddTraceback("faster_web3/utils/caching.py", "<module>", 32, CPyStatic_caching___globals);
        goto CPyL45;
    }
    return 1;
CPyL45: ;
    cpy_r_r135 = 2;
    return cpy_r_r135;
CPyL46: ;
    CPy_DecRef(cpy_r_r51);
    goto CPyL45;
CPyL47: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r63);
    goto CPyL45;
CPyL48: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r63);
    CPy_DecRef(cpy_r_r65);
    goto CPyL45;
CPyL49: ;
    CPy_DecRef(cpy_r_r96);
    goto CPyL45;
CPyL50: ;
    CPy_DecRef(cpy_r_r114);
    goto CPyL45;
CPyL51: ;
    CPy_DecRef(cpy_r_r122);
    goto CPyL45;
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
    CPyModule_faster_web3___utils___caching = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_asyncio = Py_None;
    CPyModule_collections = Py_None;
    CPyModule_enum = Py_None;
    CPyModule_time = Py_None;
    CPyModule_typing = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[133];
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
    "\b\bTxParams\021faster_web3.types\vOrderedDict\apopitem\004last\003pop\004time\005sleep",
    "\003\bKeyError(Timeout waiting for item to be available\fTimeoutError",
    "\004\rGeneratorExit\rStopIteration\aasyncio\034faster_web3/utils/caching.py",
    "\b\vcollections\004Enum\004enum\aGeneric\004List\aTypeVar\005final\001T",
    "\005\037RequestCacheValidationThreshold\tFINALIZED\tfinalized\004SAFE\004safe",
    "\005\031faster_web3.utils.caching\017__mypyc_attrs__\005_size\005_data\vSimpleCache",
    "",
};
const char * const CPyLit_Bytes[] = {
    "",
};
const char * const CPyLit_Int[] = {
    "\0010",
    "",
};
const double CPyLit_Float[] = {0};
const double CPyLit_Complex[] = {0};
const int CPyLit_Tuple[] = {
    27, 7, 15, 16, 17, 18, 19, 20, 21, 3, 23, 23, 23, 3, 24, 23, 23, 2,
    107, 108, 1, 27, 1, 8, 1, 41, 1, 42, 1, 43, 1, 18, 1, 56, 2, 53, 55,
    1, 59, 2, 18, 61, 1, 107, 1, 63, 1, 55, 5, 15, 68, 69, 70, 61, 2, 71,
    72, 1, 76, 3, 85, 85, 85, 1, 126, 1, 74, 1, 88, 3, 78, 78, 78, 1, 130,
    9, 15, 17, 18, 90, 91, 19, 20, 92, 93
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
CPyModule *CPyModule_faster_web3___utils___caching__internal = NULL;
CPyModule *CPyModule_faster_web3___utils___caching;
PyObject *CPyStatic_caching___globals;
CPyModule *CPyModule_asyncio;
CPyModule *CPyModule_collections;
CPyModule *CPyModule_enum;
CPyModule *CPyModule_time;
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
PyObject *CPyStatic_caching___RequestCacheValidationThreshold___FINALIZED = NULL;
PyObject *CPyStatic_caching___RequestCacheValidationThreshold___SAFE = NULL;
PyTypeObject *CPyType_caching___RequestCacheValidationThreshold;
PyTypeObject *CPyType_caching___SimpleCache;
PyObject *CPyDef_caching___SimpleCache(CPyTagged cpy_r_size);
PyTypeObject *CPyType_caching___async_await_and_popitem_SimpleCache_gen;
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen(void);
CPyThreadLocal faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject *caching___async_await_and_popitem_SimpleCache_gen_free_instance;
char CPyDef_caching___SimpleCache_____init__(PyObject *cpy_r_self, CPyTagged cpy_r_size);
PyObject *CPyPy_caching___SimpleCache_____init__(PyObject *self, PyObject *args, PyObject *kw);
char CPyDef_caching___SimpleCache_____contains__(PyObject *cpy_r_self, PyObject *cpy_r_key);
PyObject *CPyPy_caching___SimpleCache_____contains__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
CPyTagged CPyDef_caching___SimpleCache_____len__(PyObject *cpy_r_self);
PyObject *CPyPy_caching___SimpleCache_____len__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
tuple_T2OO CPyDef_caching___SimpleCache___cache(PyObject *cpy_r_self, PyObject *cpy_r_key, PyObject *cpy_r_value);
PyObject *CPyPy_caching___SimpleCache___cache(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___SimpleCache___get_cache_entry(PyObject *cpy_r_self, PyObject *cpy_r_key);
PyObject *CPyPy_caching___SimpleCache___get_cache_entry(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_caching___SimpleCache___clear(PyObject *cpy_r_self);
PyObject *CPyPy_caching___SimpleCache___clear(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___SimpleCache___items(PyObject *cpy_r_self);
PyObject *CPyPy_caching___SimpleCache___items(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___SimpleCache___pop(PyObject *cpy_r_self, PyObject *cpy_r_key);
PyObject *CPyPy_caching___SimpleCache___pop(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
tuple_T2OO CPyDef_caching___SimpleCache___popitem(PyObject *cpy_r_self, char cpy_r_last);
PyObject *CPyPy_caching___SimpleCache___popitem(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_caching___SimpleCache___is_full(PyObject *cpy_r_self);
PyObject *CPyPy_caching___SimpleCache___is_full(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____mypyc_generator_helper__(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback, PyObject *cpy_r_arg, PyObject **cpy_r_stop_iter_ptr);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____next__(PyObject *cpy_r___mypyc_self__);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____next__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___send(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_arg);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___send(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____iter__(PyObject *cpy_r___mypyc_self__);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____iter__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___throw(PyObject *cpy_r___mypyc_self__, PyObject *cpy_r_type, PyObject *cpy_r_value, PyObject *cpy_r_traceback);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___throw(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen___close(PyObject *cpy_r___mypyc_self__);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen___close(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___async_await_and_popitem_SimpleCache_gen_____await__(PyObject *cpy_r___mypyc_self__);
PyObject *CPyPy_caching___async_await_and_popitem_SimpleCache_gen_____await__(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_caching___SimpleCache___async_await_and_popitem(PyObject *cpy_r_self, char cpy_r_last, double cpy_r_timeout, uint32_t cpy_r___bitmap);
PyObject *CPyPy_caching___SimpleCache___async_await_and_popitem(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_caching_____top_level__(void);

static int exec_211de080822a4a868b8f__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___datatypes(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___datatypes, "211de080822a4a868b8f__mypyc.init_faster_web3____utils___datatypes", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___datatypes", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___http(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___http, "211de080822a4a868b8f__mypyc.init_faster_web3____utils___http", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___http", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___math(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___math, "211de080822a4a868b8f__mypyc.init_faster_web3____utils___math", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___math", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___type_conversion(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___type_conversion, "211de080822a4a868b8f__mypyc.init_faster_web3____utils___type_conversion", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___type_conversion", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3____utils___utility_methods(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___utility_methods, "211de080822a4a868b8f__mypyc.init_faster_web3____utils___utility_methods", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___utility_methods", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    extern PyObject *CPyInit_faster_web3___utils___caching(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3___utils___caching, "211de080822a4a868b8f__mypyc.init_faster_web3___utils___caching", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3___utils___caching", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_211de080822a4a868b8f__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "211de080822a4a868b8f__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_211de080822a4a868b8f__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_211de080822a4a868b8f__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_211de080822a4a868b8f__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
