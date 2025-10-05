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
#include "__native_type_conversion.h"
#include "__native_internal_type_conversion.h"
static PyMethodDef module_methods[] = {
    {"to_hex_if_bytes", (PyCFunction)CPyPy_to_hex_if_bytes, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("to_hex_if_bytes(val)\n--\n\n") /* docstring */},
    {"to_bytes_if_hex", (PyCFunction)CPyPy_to_bytes_if_hex, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("to_bytes_if_hex(val)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___type_conversion(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___type_conversion__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___type_conversion__internal);
    if (unlikely(CPyStatic_globals == NULL))
        goto fail;
    if (CPyGlobalsInit() < 0)
        goto fail;
    char result = CPyDef___top_level__();
    if (result == 2)
        goto fail;
    Py_DECREF(modname);
    return 0;
    fail:
    Py_CLEAR(CPyModule_faster_web3____utils___type_conversion__internal);
    Py_CLEAR(modname);
    CPy_XDECREF(CPyStatic_to_bytes);
    CPyStatic_to_bytes = NULL;
    CPy_XDECREF(CPyStatic_to_hex);
    CPyStatic_to_hex = NULL;
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.type_conversion",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___type_conversion(void)
{
    if (CPyModule_faster_web3____utils___type_conversion__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___type_conversion__internal);
        return CPyModule_faster_web3____utils___type_conversion__internal;
    }
    CPyModule_faster_web3____utils___type_conversion__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___type_conversion__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___type_conversion(CPyModule_faster_web3____utils___type_conversion__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___type_conversion__internal;
    fail:
    return NULL;
}

PyObject *CPyDef_to_hex_if_bytes(PyObject *cpy_r_val) {
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
    char cpy_r_r50;
    PyObject **cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    cpy_r_r0 = PyUnicode_Check(cpy_r_val);
    if (!cpy_r_r0) goto CPyL19;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r1 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 26, CPyStatic_globals, "str", cpy_r_val);
        goto CPyL34;
    }
    cpy_r_r2 = CPyStatics[3]; /* '0x' */
    cpy_r_r3 = CPyStr_Startswith(cpy_r_r1, cpy_r_r2);
    CPy_DECREF(cpy_r_r1);
    cpy_r_r4 = cpy_r_r3;
    if (cpy_r_r4) goto CPyL12;
    cpy_r_r5 = CPyStatics[4]; /* '' */
    cpy_r_r6 = CPyStatics[5]; /* 'Expected a hex string. Got: ' */
    cpy_r_r7 = CPyStatics[6]; /* '{!r:{}}' */
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r8 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals, "str", cpy_r_val);
        goto CPyL34;
    }
    cpy_r_r9 = CPyStatics[4]; /* '' */
    cpy_r_r10 = CPyStatics[7]; /* 'format' */
    PyObject *cpy_r_r11[3] = {cpy_r_r7, cpy_r_r8, cpy_r_r9};
    cpy_r_r12 = (PyObject **)&cpy_r_r11;
    cpy_r_r13 = PyObject_VectorcallMethod(cpy_r_r10, cpy_r_r12, 9223372036854775811ULL, 0);
    if (unlikely(cpy_r_r13 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL35;
    }
    CPy_DECREF(cpy_r_r8);
    if (likely(PyUnicode_Check(cpy_r_r13)))
        cpy_r_r14 = cpy_r_r13;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals, "str", cpy_r_r13);
        goto CPyL34;
    }
    cpy_r_r15 = PyList_New(2);
    if (unlikely(cpy_r_r15 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL36;
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
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r20 = CPyStatic_globals;
    cpy_r_r21 = CPyStatics[8]; /* 'Web3ValueError' */
    cpy_r_r22 = CPyDict_GetItem(cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL37;
    }
    PyObject *cpy_r_r23[1] = {cpy_r_r19};
    cpy_r_r24 = (PyObject **)&cpy_r_r23;
    cpy_r_r25 = PyObject_Vectorcall(cpy_r_r22, cpy_r_r24, 1, 0);
    CPy_DECREF(cpy_r_r22);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL37;
    }
    CPy_DECREF(cpy_r_r19);
    CPy_Raise(cpy_r_r25);
    CPy_DECREF(cpy_r_r25);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 27, CPyStatic_globals);
        goto CPyL34;
    }
    CPy_Unreachable();
CPyL12: ;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r26 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_globals, "str", cpy_r_val);
        goto CPyL34;
    }
    cpy_r_r27 = CPyStatic_to_hex;
    if (unlikely(cpy_r_r27 == NULL)) {
        goto CPyL38;
    } else
        goto CPyL16;
CPyL14: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r28 = 0;
    if (unlikely(!cpy_r_r28)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_globals);
        goto CPyL34;
    }
    CPy_Unreachable();
CPyL16: ;
    PyObject *cpy_r_r29[1] = {cpy_r_r26};
    cpy_r_r30 = (PyObject **)&cpy_r_r29;
    cpy_r_r31 = CPyStatics[23]; /* ('hexstr',) */
    cpy_r_r32 = PyObject_Vectorcall(cpy_r_r27, cpy_r_r30, 0, cpy_r_r31);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_globals);
        goto CPyL39;
    }
    CPy_DECREF(cpy_r_r26);
    if (likely(PyUnicode_Check(cpy_r_r32)))
        cpy_r_r33 = cpy_r_r32;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 28, CPyStatic_globals, "str", cpy_r_r32);
        goto CPyL34;
    }
    return cpy_r_r33;
CPyL19: ;
    cpy_r_r34 = (PyObject *)&PyBytes_Type;
    cpy_r_r35 = CPyModule_builtins;
    cpy_r_r36 = CPyStatics[10]; /* 'bytearray' */
    cpy_r_r37 = CPyObject_GetAttr(cpy_r_r35, cpy_r_r36);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    CPy_INCREF(cpy_r_r34);
    cpy_r_r38.f0 = cpy_r_r34;
    cpy_r_r38.f1 = cpy_r_r37;
    cpy_r_r39 = PyTuple_New(2);
    if (unlikely(cpy_r_r39 == NULL))
        CPyError_OutOfMemory();
    PyObject *__tmp1 = cpy_r_r38.f0;
    PyTuple_SET_ITEM(cpy_r_r39, 0, __tmp1);
    PyObject *__tmp2 = cpy_r_r38.f1;
    PyTuple_SET_ITEM(cpy_r_r39, 1, __tmp2);
    cpy_r_r40 = PyObject_IsInstance(cpy_r_val, cpy_r_r39);
    CPy_DECREF(cpy_r_r39);
    cpy_r_r41 = cpy_r_r40 >= 0;
    if (unlikely(!cpy_r_r41)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r42 = cpy_r_r40;
    if (!cpy_r_r42) goto CPyL27;
    cpy_r_r43 = CPyStatic_to_hex;
    if (likely(cpy_r_r43 != NULL)) goto CPyL25;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r44 = 0;
    if (unlikely(!cpy_r_r44)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    CPy_Unreachable();
CPyL25: ;
    PyObject *cpy_r_r45[1] = {cpy_r_val};
    cpy_r_r46 = (PyObject **)&cpy_r_r45;
    cpy_r_r47 = PyObject_Vectorcall(cpy_r_r43, cpy_r_r46, 1, 0);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r48 = cpy_r_r47;
    goto CPyL32;
CPyL27: ;
    cpy_r_r49 = CPyStatic_to_hex;
    if (likely(cpy_r_r49 != NULL)) goto CPyL30;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_hex\" was not set");
    cpy_r_r50 = 0;
    if (unlikely(!cpy_r_r50)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    CPy_Unreachable();
CPyL30: ;
    PyObject *cpy_r_r51[1] = {cpy_r_val};
    cpy_r_r52 = (PyObject **)&cpy_r_r51;
    cpy_r_r53 = CPyStatics[23]; /* ('hexstr',) */
    cpy_r_r54 = PyObject_Vectorcall(cpy_r_r49, cpy_r_r52, 0, cpy_r_r53);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r48 = cpy_r_r54;
CPyL32: ;
    if (likely(PyUnicode_Check(cpy_r_r48)))
        cpy_r_r55 = cpy_r_r48;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 30, CPyStatic_globals, "str", cpy_r_r48);
        goto CPyL34;
    }
    return cpy_r_r55;
CPyL34: ;
    cpy_r_r56 = NULL;
    return cpy_r_r56;
CPyL35: ;
    CPy_DecRef(cpy_r_r8);
    goto CPyL34;
CPyL36: ;
    CPy_DecRef(cpy_r_r14);
    goto CPyL34;
CPyL37: ;
    CPy_DecRef(cpy_r_r19);
    goto CPyL34;
CPyL38: ;
    CPy_DecRef(cpy_r_r26);
    goto CPyL14;
CPyL39: ;
    CPy_DecRef(cpy_r_r26);
    goto CPyL34;
}

PyObject *CPyPy_to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
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
    if (arg_val != NULL) goto __LL3;
    if (PyBytes_Check(obj_val) || PyByteArray_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL3;
    arg_val = obj_val;
    if (arg_val != NULL) goto __LL3;
    CPy_TypeError("union[str, bytes, object]", obj_val); 
    goto fail;
__LL3: ;
    PyObject *retval = CPyDef_to_hex_if_bytes(arg_val);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_hex_if_bytes", 20, CPyStatic_globals);
    return NULL;
}

PyObject *CPyDef_to_bytes_if_hex(PyObject *cpy_r_val) {
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
    cpy_r_r0 = PyUnicode_Check(cpy_r_val);
    if (!cpy_r_r0) goto CPyL7;
    CPy_INCREF(cpy_r_val);
    if (likely(PyUnicode_Check(cpy_r_val)))
        cpy_r_r1 = cpy_r_val;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_globals, "str", cpy_r_val);
        goto CPyL10;
    }
    cpy_r_r2 = CPyStatic_to_bytes;
    if (unlikely(cpy_r_r2 == NULL)) {
        goto CPyL11;
    } else
        goto CPyL5;
CPyL3: ;
    PyErr_SetString(PyExc_NameError, "value for final name \"to_bytes\" was not set");
    cpy_r_r3 = 0;
    if (unlikely(!cpy_r_r3)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_globals);
        goto CPyL10;
    }
    CPy_Unreachable();
CPyL5: ;
    PyObject *cpy_r_r4[1] = {cpy_r_r1};
    cpy_r_r5 = (PyObject **)&cpy_r_r4;
    cpy_r_r6 = CPyStatics[23]; /* ('hexstr',) */
    cpy_r_r7 = PyObject_Vectorcall(cpy_r_r2, cpy_r_r5, 0, cpy_r_r6);
    if (unlikely(cpy_r_r7 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_globals);
        goto CPyL12;
    }
    CPy_DECREF(cpy_r_r1);
    cpy_r_r8 = cpy_r_r7;
    goto CPyL8;
CPyL7: ;
    CPy_INCREF(cpy_r_val);
    cpy_r_r8 = cpy_r_val;
CPyL8: ;
    if (likely(PyBytes_Check(cpy_r_r8) || PyByteArray_Check(cpy_r_r8)))
        cpy_r_r9 = cpy_r_r8;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 38, CPyStatic_globals, "bytes", cpy_r_r8);
        goto CPyL10;
    }
    return cpy_r_r9;
CPyL10: ;
    cpy_r_r10 = NULL;
    return cpy_r_r10;
CPyL11: ;
    CPy_DecRef(cpy_r_r1);
    goto CPyL3;
CPyL12: ;
    CPy_DecRef(cpy_r_r1);
    goto CPyL10;
}

PyObject *CPyPy_to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
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
    if (arg_val != NULL) goto __LL4;
    if (PyBytes_Check(obj_val) || PyByteArray_Check(obj_val))
        arg_val = obj_val;
    else {
        arg_val = NULL;
    }
    if (arg_val != NULL) goto __LL4;
    arg_val = obj_val;
    if (arg_val != NULL) goto __LL4;
    CPy_TypeError("union[str, bytes, object]", obj_val); 
    goto fail;
__LL4: ;
    PyObject *retval = CPyDef_to_bytes_if_hex(arg_val);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "to_bytes_if_hex", 33, CPyStatic_globals);
    return NULL;
}

char CPyDef___top_level__(void) {
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
    PyObject *cpy_r_r32;
    PyObject *cpy_r_r33;
    int32_t cpy_r_r34;
    char cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    PyObject *cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    int32_t cpy_r_r43;
    char cpy_r_r44;
    char cpy_r_r45;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[11]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", -1, CPyStatic_globals);
        goto CPyL14;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[24]; /* ('Final', 'Union') */
    cpy_r_r6 = CPyStatics[14]; /* 'typing' */
    cpy_r_r7 = CPyStatic_globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 1, CPyStatic_globals);
        goto CPyL14;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = (PyObject **)&CPyModule_eth_utils;
    PyObject **cpy_r_r10[1] = {cpy_r_r9};
    cpy_r_r11 = (void *)&cpy_r_r10;
    int64_t cpy_r_r12[1] = {6};
    cpy_r_r13 = (void *)&cpy_r_r12;
    cpy_r_r14 = CPyStatics[26]; /* (('eth_utils', 'eth_utils', 'eth_utils'),) */
    cpy_r_r15 = CPyStatic_globals;
    cpy_r_r16 = CPyStatics[16]; /* 'faster_web3/_utils/type_conversion.py' */
    cpy_r_r17 = CPyStatics[17]; /* '<module>' */
    cpy_r_r18 = CPyImport_ImportMany(cpy_r_r14, cpy_r_r11, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r13);
    if (!cpy_r_r18) goto CPyL14;
    cpy_r_r19 = CPyStatics[27]; /* ('HexStr',) */
    cpy_r_r20 = CPyStatics[19]; /* 'eth_typing' */
    cpy_r_r21 = CPyStatic_globals;
    cpy_r_r22 = CPyImport_ImportFromMany(cpy_r_r20, cpy_r_r19, cpy_r_r19, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 7, CPyStatic_globals);
        goto CPyL14;
    }
    CPyModule_eth_typing = cpy_r_r22;
    CPy_INCREF(CPyModule_eth_typing);
    CPy_DECREF(cpy_r_r22);
    cpy_r_r23 = CPyStatics[28]; /* ('Web3ValueError',) */
    cpy_r_r24 = CPyStatics[20]; /* 'faster_web3.exceptions' */
    cpy_r_r25 = CPyStatic_globals;
    cpy_r_r26 = CPyImport_ImportFromMany(cpy_r_r24, cpy_r_r23, cpy_r_r23, cpy_r_r25);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 11, CPyStatic_globals);
        goto CPyL14;
    }
    CPyModule_faster_web3___exceptions = cpy_r_r26;
    CPy_INCREF(CPyModule_faster_web3___exceptions);
    CPy_DECREF(cpy_r_r26);
    cpy_r_r27 = CPyStatic_globals;
    cpy_r_r28 = CPyStatics[15]; /* 'eth_utils' */
    cpy_r_r29 = CPyDict_GetItem(cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 16, CPyStatic_globals);
        goto CPyL14;
    }
    cpy_r_r30 = CPyStatics[21]; /* 'to_bytes' */
    cpy_r_r31 = CPyObject_GetAttr(cpy_r_r29, cpy_r_r30);
    CPy_DECREF(cpy_r_r29);
    if (unlikely(cpy_r_r31 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 16, CPyStatic_globals);
        goto CPyL14;
    }
    CPyStatic_to_bytes = cpy_r_r31;
    CPy_INCREF(CPyStatic_to_bytes);
    cpy_r_r32 = CPyStatic_globals;
    cpy_r_r33 = CPyStatics[21]; /* 'to_bytes' */
    cpy_r_r34 = CPyDict_SetItem(cpy_r_r32, cpy_r_r33, cpy_r_r31);
    CPy_DECREF(cpy_r_r31);
    cpy_r_r35 = cpy_r_r34 >= 0;
    if (unlikely(!cpy_r_r35)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 16, CPyStatic_globals);
        goto CPyL14;
    }
    cpy_r_r36 = CPyStatic_globals;
    cpy_r_r37 = CPyStatics[15]; /* 'eth_utils' */
    cpy_r_r38 = CPyDict_GetItem(cpy_r_r36, cpy_r_r37);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 17, CPyStatic_globals);
        goto CPyL14;
    }
    cpy_r_r39 = CPyStatics[22]; /* 'to_hex' */
    cpy_r_r40 = CPyObject_GetAttr(cpy_r_r38, cpy_r_r39);
    CPy_DECREF(cpy_r_r38);
    if (unlikely(cpy_r_r40 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 17, CPyStatic_globals);
        goto CPyL14;
    }
    CPyStatic_to_hex = cpy_r_r40;
    CPy_INCREF(CPyStatic_to_hex);
    cpy_r_r41 = CPyStatic_globals;
    cpy_r_r42 = CPyStatics[22]; /* 'to_hex' */
    cpy_r_r43 = CPyDict_SetItem(cpy_r_r41, cpy_r_r42, cpy_r_r40);
    CPy_DECREF(cpy_r_r40);
    cpy_r_r44 = cpy_r_r43 >= 0;
    if (unlikely(!cpy_r_r44)) {
        CPy_AddTraceback("faster_web3/_utils/type_conversion.py", "<module>", 17, CPyStatic_globals);
        goto CPyL14;
    }
    return 1;
CPyL14: ;
    cpy_r_r45 = 2;
    return cpy_r_r45;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___type_conversion = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_eth_utils = Py_None;
    CPyModule_eth_typing = Py_None;
    CPyModule_faster_web3___exceptions = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[29];
const char * const CPyLit_Str[] = {
    "\a\0020x\000\034Expected a hex string. Got: \a{!r:{}}\006format\016Web3ValueError\006hexstr",
    "\006\tbytearray\bbuiltins\005Final\005Union\006typing\teth_utils",
    "\004%faster_web3/_utils/type_conversion.py\b<module>\006HexStr\neth_typing",
    "\003\026faster_web3.exceptions\bto_bytes\006to_hex",
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
const int CPyLit_Tuple[] = {6, 1, 9, 2, 12, 13, 3, 15, 15, 15, 1, 25, 1, 18, 1, 8};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___type_conversion__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___type_conversion;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
CPyModule *CPyModule_typing;
CPyModule *CPyModule_eth_utils;
CPyModule *CPyModule_eth_typing;
CPyModule *CPyModule_faster_web3___exceptions;
PyObject *CPyStatic_to_bytes = NULL;
PyObject *CPyStatic_to_hex = NULL;
PyObject *CPyDef_to_hex_if_bytes(PyObject *cpy_r_val);
PyObject *CPyPy_to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef_to_bytes_if_hex(PyObject *cpy_r_val);
PyObject *CPyPy_to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef___top_level__(void);

static int exec_type_conversion__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___type_conversion(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___type_conversion, "faster_web3._utils.type_conversion__mypyc.init_faster_web3____utils___type_conversion", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___type_conversion", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_type_conversion__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.type_conversion__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_type_conversion__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_type_conversion__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_type_conversion__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
