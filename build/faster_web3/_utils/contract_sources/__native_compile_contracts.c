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
#include "__native_compile_contracts.h"
#include "__native_internal_compile_contracts.h"
static PyMethodDef module_methods[] = {
    {"_compile_dot_sol_files", (PyCFunction)CPyPy__compile_dot_sol_files, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("_compile_dot_sol_files(dot_sol_filename)\n--\n\n") /* docstring */},
    {"_get_compiled_contract_data", (PyCFunction)CPyPy__get_compiled_contract_data, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("_get_compiled_contract_data(sol_file_output, dot_sol_filename, contract_name=None)\n--\n\n") /* docstring */},
    {"compile_files", (PyCFunction)CPyPy_compile_files, METH_FASTCALL | METH_KEYWORDS, PyDoc_STR("compile_files(file_list)\n--\n\n") /* docstring */},
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___compile_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.compile_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___compile_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___compile_contracts(CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal;
    fail:
    return NULL;
}

PyObject *CPyDef__compile_dot_sol_files(PyObject *cpy_r_dot_sol_filename) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    PyObject *cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject *cpy_r_r5;
    CPyPtr cpy_r_r6;
    CPyPtr cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    CPyPtr cpy_r_r12;
    CPyPtr cpy_r_r13;
    CPyPtr cpy_r_r14;
    CPyPtr cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject **cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject *cpy_r_r21;
    PyObject *cpy_r_r22;
    cpy_r_r0 = CPyStatic_globals;
    cpy_r_r1 = CPyStatics[3]; /* 'solcx' */
    cpy_r_r2 = CPyDict_GetItem(cpy_r_r0, cpy_r_r1);
    if (unlikely(cpy_r_r2 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 87, CPyStatic_globals);
        goto CPyL7;
    }
    cpy_r_r3 = CPyStatics[4]; /* './' */
    cpy_r_r4 = CPyStr_Build(2, cpy_r_r3, cpy_r_dot_sol_filename);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 88, CPyStatic_globals);
        goto CPyL8;
    }
    cpy_r_r5 = PyList_New(1);
    if (unlikely(cpy_r_r5 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 88, CPyStatic_globals);
        goto CPyL9;
    }
    cpy_r_r6 = (CPyPtr)&((PyListObject *)cpy_r_r5)->ob_item;
    cpy_r_r7 = *(CPyPtr *)cpy_r_r6;
    *(PyObject * *)cpy_r_r7 = cpy_r_r4;
    cpy_r_r8 = CPyStatics[5]; /* 'abi' */
    cpy_r_r9 = CPyStatics[6]; /* 'bin' */
    cpy_r_r10 = CPyStatics[7]; /* 'bin-runtime' */
    cpy_r_r11 = PyList_New(3);
    if (unlikely(cpy_r_r11 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 89, CPyStatic_globals);
        goto CPyL10;
    }
    cpy_r_r12 = (CPyPtr)&((PyListObject *)cpy_r_r11)->ob_item;
    cpy_r_r13 = *(CPyPtr *)cpy_r_r12;
    CPy_INCREF(cpy_r_r8);
    *(PyObject * *)cpy_r_r13 = cpy_r_r8;
    CPy_INCREF(cpy_r_r9);
    cpy_r_r14 = cpy_r_r13 + 8;
    *(PyObject * *)cpy_r_r14 = cpy_r_r9;
    CPy_INCREF(cpy_r_r10);
    cpy_r_r15 = cpy_r_r13 + 16;
    *(PyObject * *)cpy_r_r15 = cpy_r_r10;
    cpy_r_r16 = CPyStatics[8]; /* 'compile_files' */
    PyObject *cpy_r_r17[3] = {cpy_r_r2, cpy_r_r5, cpy_r_r11};
    cpy_r_r18 = (PyObject **)&cpy_r_r17;
    cpy_r_r19 = CPyStatics[101]; /* ('output_values',) */
    cpy_r_r20 = PyObject_VectorcallMethod(cpy_r_r16, cpy_r_r18, 9223372036854775810ULL, cpy_r_r19);
    if (unlikely(cpy_r_r20 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 87, CPyStatic_globals);
        goto CPyL11;
    }
    CPy_DECREF(cpy_r_r2);
    CPy_DECREF_NO_IMM(cpy_r_r5);
    CPy_DECREF_NO_IMM(cpy_r_r11);
    if (likely(PyDict_Check(cpy_r_r20)))
        cpy_r_r21 = cpy_r_r20;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 91, CPyStatic_globals, "dict", cpy_r_r20);
        goto CPyL7;
    }
    return cpy_r_r21;
CPyL7: ;
    cpy_r_r22 = NULL;
    return cpy_r_r22;
CPyL8: ;
    CPy_DecRef(cpy_r_r2);
    goto CPyL7;
CPyL9: ;
    CPy_DecRef(cpy_r_r2);
    CPy_DecRef(cpy_r_r4);
    goto CPyL7;
CPyL10: ;
    CPy_DecRef(cpy_r_r2);
    CPy_DecRef(cpy_r_r5);
    goto CPyL7;
CPyL11: ;
    CPy_DecRef(cpy_r_r2);
    CPy_DecRef(cpy_r_r5);
    CPy_DecRef(cpy_r_r11);
    goto CPyL7;
}

PyObject *CPyPy__compile_dot_sol_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"dot_sol_filename", 0};
    static CPyArg_Parser parser = {"O:_compile_dot_sol_files", kwlist, 0};
    PyObject *obj_dot_sol_filename;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_dot_sol_filename)) {
        return NULL;
    }
    PyObject *arg_dot_sol_filename;
    if (likely(PyUnicode_Check(obj_dot_sol_filename)))
        arg_dot_sol_filename = obj_dot_sol_filename;
    else {
        CPy_TypeError("str", obj_dot_sol_filename); 
        goto fail;
    }
    PyObject *retval = CPyDef__compile_dot_sol_files(arg_dot_sol_filename);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_compile_dot_sol_files", 86, CPyStatic_globals);
    return NULL;
}

PyObject *CPyDef__get_compiled_contract_data(PyObject *cpy_r_sol_file_output, PyObject *cpy_r_dot_sol_filename, PyObject *cpy_r_contract_name) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    char cpy_r_r4;
    PyObject *cpy_r_r5;
    PyObject *cpy_r_r6;
    PyObject *cpy_r_r7;
    PyObject *cpy_r_r8;
    PyObject *cpy_r_contract_data;
    CPyTagged cpy_r_r9;
    int64_t cpy_r_r10;
    PyObject *cpy_r_r11;
    tuple_T3CIO cpy_r_r12;
    CPyTagged cpy_r_r13;
    char cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    int32_t cpy_r_r20;
    char cpy_r_r21;
    char cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject *cpy_r_r24;
    char cpy_r_r25;
    char cpy_r_r26;
    PyObject *cpy_r_r27;
    char cpy_r_r28;
    PyObject *cpy_r_r29;
    int64_t cpy_r_r30;
    CPyTagged cpy_r_r31;
    char cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    PyObject **cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    PyObject *cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    int32_t cpy_r_r50;
    char cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject *cpy_r_r57;
    PyObject *cpy_r_r58;
    PyObject *cpy_r_r59;
    int32_t cpy_r_r60;
    char cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    if (cpy_r_contract_name != NULL) goto CPyL43;
    cpy_r_r0 = Py_None;
    cpy_r_contract_name = cpy_r_r0;
CPyL2: ;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_contract_name != cpy_r_r1;
    if (!cpy_r_r2) goto CPyL44;
    CPy_INCREF(cpy_r_contract_name);
    if (likely(cpy_r_contract_name != Py_None))
        cpy_r_r3 = cpy_r_contract_name;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 97, CPyStatic_globals, "str", cpy_r_contract_name);
        goto CPyL45;
    }
    cpy_r_r4 = CPyStr_IsTrue(cpy_r_r3);
    CPy_DECREF(cpy_r_r3);
    if (cpy_r_r4) {
        goto CPyL7;
    } else
        goto CPyL44;
CPyL5: ;
    cpy_r_r5 = CPyStatics[10]; /* '.sol' */
    cpy_r_r6 = CPyStatics[11]; /* '' */
    cpy_r_r7 = PyUnicode_Replace(cpy_r_dot_sol_filename, cpy_r_r5, cpy_r_r6, -1);
    if (unlikely(cpy_r_r7 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 100, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_contract_name = cpy_r_r7;
CPyL7: ;
    cpy_r_r8 = Py_None;
    cpy_r_contract_data = cpy_r_r8;
    cpy_r_r9 = 0;
    cpy_r_r10 = PyDict_Size(cpy_r_sol_file_output);
    cpy_r_r11 = CPyDict_GetKeysIter(cpy_r_sol_file_output);
    if (unlikely(cpy_r_r11 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 103, CPyStatic_globals);
        goto CPyL46;
    }
CPyL8: ;
    cpy_r_r12 = CPyDict_NextKey(cpy_r_r11, cpy_r_r9);
    cpy_r_r13 = cpy_r_r12.f1;
    cpy_r_r9 = cpy_r_r13;
    cpy_r_r14 = cpy_r_r12.f0;
    if (!cpy_r_r14) goto CPyL47;
    cpy_r_r15 = cpy_r_r12.f2;
    CPy_INCREF(cpy_r_r15);
    CPy_DECREF(cpy_r_r12.f2);
    if (likely(PyUnicode_Check(cpy_r_r15)))
        cpy_r_r16 = cpy_r_r15;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 103, CPyStatic_globals, "str", cpy_r_r15);
        goto CPyL48;
    }
    cpy_r_r17 = CPyStatics[12]; /* ':' */
    CPy_INCREF(cpy_r_contract_name);
    if (likely(cpy_r_contract_name != Py_None))
        cpy_r_r18 = cpy_r_contract_name;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 104, CPyStatic_globals, "str", cpy_r_contract_name);
        goto CPyL49;
    }
    cpy_r_r19 = CPyStr_Build(2, cpy_r_r17, cpy_r_r18);
    CPy_DECREF(cpy_r_r18);
    if (unlikely(cpy_r_r19 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 104, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r20 = PyUnicode_Contains(cpy_r_r16, cpy_r_r19);
    CPy_DECREF(cpy_r_r19);
    cpy_r_r21 = cpy_r_r20 >= 0;
    if (unlikely(!cpy_r_r21)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 104, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r22 = cpy_r_r20;
    if (cpy_r_r22) {
        goto CPyL50;
    } else
        goto CPyL51;
CPyL14: ;
    cpy_r_r23 = CPyDict_GetItem(cpy_r_sol_file_output, cpy_r_r16);
    CPy_DECREF(cpy_r_r16);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 105, CPyStatic_globals);
        goto CPyL52;
    }
    if (likely(PyDict_Check(cpy_r_r23)))
        cpy_r_r24 = cpy_r_r23;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 105, CPyStatic_globals, "dict", cpy_r_r23);
        goto CPyL52;
    }
    cpy_r_contract_data = cpy_r_r24;
CPyL17: ;
    cpy_r_r25 = CPyDict_CheckSize(cpy_r_sol_file_output, cpy_r_r10);
    if (unlikely(!cpy_r_r25)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 103, CPyStatic_globals);
        goto CPyL48;
    } else
        goto CPyL8;
CPyL18: ;
    cpy_r_r26 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r26)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 103, CPyStatic_globals);
        goto CPyL46;
    }
    cpy_r_r27 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r28 = cpy_r_contract_data != cpy_r_r27;
    if (!cpy_r_r28) goto CPyL53;
    CPy_INCREF(cpy_r_contract_data);
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r29 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 102, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL46;
    }
    cpy_r_r30 = PyDict_Size(cpy_r_r29);
    CPy_DECREF(cpy_r_r29);
    cpy_r_r31 = cpy_r_r30 << 1;
    cpy_r_r32 = cpy_r_r31 != 0;
    if (cpy_r_r32) {
        goto CPyL54;
    } else
        goto CPyL53;
CPyL22: ;
    cpy_r_r33 = CPyStatics[13]; /* 'Could not find compiled data for contract: ' */
    if (likely(cpy_r_contract_name != Py_None))
        cpy_r_r34 = cpy_r_contract_name;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 107, CPyStatic_globals, "str", cpy_r_contract_name);
        goto CPyL42;
    }
    cpy_r_r35 = CPyStr_Build(2, cpy_r_r33, cpy_r_r34);
    CPy_DECREF(cpy_r_r34);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 107, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r36 = CPyModule_builtins;
    cpy_r_r37 = CPyStatics[14]; /* 'Exception' */
    cpy_r_r38 = CPyObject_GetAttr(cpy_r_r36, cpy_r_r37);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 107, CPyStatic_globals);
        goto CPyL55;
    }
    PyObject *cpy_r_r39[1] = {cpy_r_r35};
    cpy_r_r40 = (PyObject **)&cpy_r_r39;
    cpy_r_r41 = PyObject_Vectorcall(cpy_r_r38, cpy_r_r40, 1, 0);
    CPy_DECREF(cpy_r_r38);
    if (unlikely(cpy_r_r41 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 107, CPyStatic_globals);
        goto CPyL55;
    }
    CPy_DECREF(cpy_r_r35);
    CPy_Raise(cpy_r_r41);
    CPy_DECREF(cpy_r_r41);
    if (unlikely(!0)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 107, CPyStatic_globals);
        goto CPyL42;
    }
    CPy_Unreachable();
CPyL28: ;
    cpy_r_r42 = CPyStatics[15]; /* '0x' */
    CPy_INCREF(cpy_r_contract_data);
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r43 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL56;
    }
    cpy_r_r44 = CPyStatics[6]; /* 'bin' */
    cpy_r_r45 = CPyDict_GetItem(cpy_r_r43, cpy_r_r44);
    CPy_DECREF(cpy_r_r43);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals);
        goto CPyL56;
    }
    if (likely(PyUnicode_Check(cpy_r_r45)))
        cpy_r_r46 = cpy_r_r45;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals, "str", cpy_r_r45);
        goto CPyL56;
    }
    cpy_r_r47 = CPyStr_Build(2, cpy_r_r42, cpy_r_r46);
    CPy_DECREF(cpy_r_r46);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals);
        goto CPyL56;
    }
    CPy_INCREF(cpy_r_contract_data);
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r48 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL57;
    }
    cpy_r_r49 = CPyStatics[6]; /* 'bin' */
    cpy_r_r50 = CPyDict_SetItem(cpy_r_r48, cpy_r_r49, cpy_r_r47);
    CPy_DECREF(cpy_r_r48);
    CPy_DECREF(cpy_r_r47);
    cpy_r_r51 = cpy_r_r50 >= 0;
    if (unlikely(!cpy_r_r51)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 109, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r52 = CPyStatics[15]; /* '0x' */
    CPy_INCREF(cpy_r_contract_data);
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r53 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL56;
    }
    cpy_r_r54 = CPyStatics[7]; /* 'bin-runtime' */
    cpy_r_r55 = CPyDict_GetItem(cpy_r_r53, cpy_r_r54);
    CPy_DECREF(cpy_r_r53);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals);
        goto CPyL56;
    }
    if (likely(PyUnicode_Check(cpy_r_r55)))
        cpy_r_r56 = cpy_r_r55;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals, "str", cpy_r_r55);
        goto CPyL56;
    }
    cpy_r_r57 = CPyStr_Build(2, cpy_r_r52, cpy_r_r56);
    CPy_DECREF(cpy_r_r56);
    if (unlikely(cpy_r_r57 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals);
        goto CPyL56;
    }
    CPy_INCREF(cpy_r_contract_data);
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r58 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL58;
    }
    cpy_r_r59 = CPyStatics[7]; /* 'bin-runtime' */
    cpy_r_r60 = CPyDict_SetItem(cpy_r_r58, cpy_r_r59, cpy_r_r57);
    CPy_DECREF(cpy_r_r58);
    CPy_DECREF(cpy_r_r57);
    cpy_r_r61 = cpy_r_r60 >= 0;
    if (unlikely(!cpy_r_r61)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 110, CPyStatic_globals);
        goto CPyL56;
    }
    if (likely(cpy_r_contract_data != Py_None))
        cpy_r_r62 = cpy_r_contract_data;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 112, CPyStatic_globals, "dict", cpy_r_contract_data);
        goto CPyL42;
    }
    return cpy_r_r62;
CPyL42: ;
    cpy_r_r63 = NULL;
    return cpy_r_r63;
CPyL43: ;
    CPy_INCREF(cpy_r_contract_name);
    goto CPyL2;
CPyL44: ;
    CPy_DECREF(cpy_r_contract_name);
    goto CPyL5;
CPyL45: ;
    CPy_DecRef(cpy_r_contract_name);
    goto CPyL42;
CPyL46: ;
    CPy_DecRef(cpy_r_contract_name);
    CPy_DecRef(cpy_r_contract_data);
    goto CPyL42;
CPyL47: ;
    CPy_DECREF(cpy_r_r11);
    CPy_DECREF(cpy_r_r12.f2);
    goto CPyL18;
CPyL48: ;
    CPy_DecRef(cpy_r_contract_name);
    CPy_DecRef(cpy_r_contract_data);
    CPy_DecRef(cpy_r_r11);
    goto CPyL42;
CPyL49: ;
    CPy_DecRef(cpy_r_contract_name);
    CPy_DecRef(cpy_r_contract_data);
    CPy_DecRef(cpy_r_r11);
    CPy_DecRef(cpy_r_r16);
    goto CPyL42;
CPyL50: ;
    CPy_DECREF(cpy_r_contract_data);
    goto CPyL14;
CPyL51: ;
    CPy_DECREF(cpy_r_r16);
    goto CPyL17;
CPyL52: ;
    CPy_DecRef(cpy_r_contract_name);
    CPy_DecRef(cpy_r_r11);
    goto CPyL42;
CPyL53: ;
    CPy_DECREF(cpy_r_contract_data);
    goto CPyL22;
CPyL54: ;
    CPy_DECREF(cpy_r_contract_name);
    goto CPyL28;
CPyL55: ;
    CPy_DecRef(cpy_r_r35);
    goto CPyL42;
CPyL56: ;
    CPy_DecRef(cpy_r_contract_data);
    goto CPyL42;
CPyL57: ;
    CPy_DecRef(cpy_r_contract_data);
    CPy_DecRef(cpy_r_r47);
    goto CPyL42;
CPyL58: ;
    CPy_DecRef(cpy_r_contract_data);
    CPy_DecRef(cpy_r_r57);
    goto CPyL42;
}

PyObject *CPyPy__get_compiled_contract_data(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"sol_file_output", "dot_sol_filename", "contract_name", 0};
    static CPyArg_Parser parser = {"OO|O:_get_compiled_contract_data", kwlist, 0};
    PyObject *obj_sol_file_output;
    PyObject *obj_dot_sol_filename;
    PyObject *obj_contract_name = NULL;
    if (!CPyArg_ParseStackAndKeywordsSimple(args, nargs, kwnames, &parser, &obj_sol_file_output, &obj_dot_sol_filename, &obj_contract_name)) {
        return NULL;
    }
    PyObject *arg_sol_file_output;
    if (likely(PyDict_Check(obj_sol_file_output)))
        arg_sol_file_output = obj_sol_file_output;
    else {
        CPy_TypeError("dict", obj_sol_file_output); 
        goto fail;
    }
    PyObject *arg_dot_sol_filename;
    if (likely(PyUnicode_Check(obj_dot_sol_filename)))
        arg_dot_sol_filename = obj_dot_sol_filename;
    else {
        CPy_TypeError("str", obj_dot_sol_filename); 
        goto fail;
    }
    PyObject *arg_contract_name;
    if (obj_contract_name == NULL) {
        arg_contract_name = NULL;
        goto __LL1;
    }
    if (PyUnicode_Check(obj_contract_name))
        arg_contract_name = obj_contract_name;
    else {
        arg_contract_name = NULL;
    }
    if (arg_contract_name != NULL) goto __LL1;
    if (obj_contract_name == Py_None)
        arg_contract_name = obj_contract_name;
    else {
        arg_contract_name = NULL;
    }
    if (arg_contract_name != NULL) goto __LL1;
    CPy_TypeError("str or None", obj_contract_name); 
    goto fail;
__LL1: ;
    PyObject *retval = CPyDef__get_compiled_contract_data(arg_sol_file_output, arg_dot_sol_filename, arg_contract_name);
    return retval;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "_get_compiled_contract_data", 94, CPyStatic_globals);
    return NULL;
}

char CPyDef_compile_files(PyObject *cpy_r_file_list) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_dot_sol_file;
    int64_t cpy_r_r1;
    CPyPtr cpy_r_r2;
    int64_t cpy_r_r3;
    char cpy_r_r4;
    CPyPtr cpy_r_r5;
    CPyPtr cpy_r_r6;
    int64_t cpy_r_r7;
    CPyPtr cpy_r_r8;
    PyObject *cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    PyObject *cpy_r_r13;
    PyObject *cpy_r_r14;
    PyObject *cpy_r_r15;
    PyObject *cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject **cpy_r_r22;
    PyObject *cpy_r_r23;
    PyObject *cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject **cpy_r_r29;
    PyObject *cpy_r_r30;
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject **cpy_r_r37;
    PyObject *cpy_r_r38;
    char cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject **cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    tuple_T3OOO cpy_r_r45;
    tuple_T3OOO cpy_r_r46;
    PyObject *cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject **cpy_r_r51;
    PyObject *cpy_r_r52;
    int32_t cpy_r_r53;
    char cpy_r_r54;
    char cpy_r_r55;
    char cpy_r_r56;
    tuple_T3OOO cpy_r_r57;
    tuple_T3OOO cpy_r_r58;
    tuple_T3OOO cpy_r_r59;
    PyObject *cpy_r_r60;
    PyObject **cpy_r_r62;
    PyObject *cpy_r_r63;
    char cpy_r_r64;
    PyObject *cpy_r_r65;
    int64_t cpy_r_r66;
    char cpy_r_r67;
    CPyPtr cpy_r_r68;
    int64_t cpy_r_r69;
    char cpy_r_r70;
    char cpy_r_r71;
    CPyPtr cpy_r_r72;
    CPyPtr cpy_r_r73;
    int64_t cpy_r_r74;
    CPyPtr cpy_r_r75;
    PyObject *cpy_r_r76;
    PyObject *cpy_r_r77;
    char cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
    PyObject *cpy_r_r81;
    CPyPtr cpy_r_r82;
    CPyPtr cpy_r_r83;
    CPyPtr cpy_r_r84;
    int64_t cpy_r_r85;
    CPyPtr cpy_r_r86;
    int64_t cpy_r_r87;
    char cpy_r_r88;
    CPyPtr cpy_r_r89;
    CPyPtr cpy_r_r90;
    int64_t cpy_r_r91;
    CPyPtr cpy_r_r92;
    PyObject *cpy_r_r93;
    PyObject *cpy_r_r94;
    PyObject *cpy_r__;
    PyObject *cpy_r_r95;
    int32_t cpy_r_r96;
    char cpy_r_r97;
    char cpy_r_r98;
    char cpy_r_r99;
    int64_t cpy_r_r100;
    PyObject *cpy_r_r101;
    int32_t cpy_r_r102;
    char cpy_r_r103;
    char cpy_r_r104;
    char cpy_r_r105;
    PyObject *cpy_r_r106;
    CPyTagged cpy_r_r107;
    PyObject *cpy_r_r108;
    int64_t cpy_r_r109;
    char cpy_r_r110;
    CPyTagged cpy_r_r111;
    CPyTagged cpy_r_r112;
    PyObject *cpy_r_r113;
    PyObject *cpy_r_r114;
    PyObject *cpy_r_r115;
    CPyTagged cpy_r_r116;
    CPyTagged cpy_r_r117;
    PyObject *cpy_r_r118;
    PyObject *cpy_r_r119;
    int32_t cpy_r_r120;
    char cpy_r_r121;
    int64_t cpy_r_r122;
    PyObject *cpy_r_r123;
    PyObject *cpy_r_r124;
    PyObject *cpy_r_r125;
    PyObject *cpy_r_r126;
    int32_t cpy_r_r127;
    char cpy_r_r128;
    int64_t cpy_r_r129;
    PyObject *cpy_r_r130;
    PyObject *cpy_r_r131;
    PyObject *cpy_r_r132;
    PyObject *cpy_r_r133;
    CPyTagged cpy_r_r134;
    int64_t cpy_r_r135;
    PyObject *cpy_r_r136;
    tuple_T3CIO cpy_r_r137;
    CPyTagged cpy_r_r138;
    char cpy_r_r139;
    PyObject *cpy_r_r140;
    PyObject *cpy_r_r141;
    PyObject *cpy_r_r142;
    PyObject *cpy_r_r143;
    PyObject *cpy_r_r144;
    PyObject *cpy_r_r145;
    PyObject *cpy_r_r146;
    PyObject *cpy_r_r147;
    PyObject *cpy_r_r148;
    PyObject *cpy_r_r149;
    PyObject **cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    int64_t cpy_r_r154;
    CPyPtr cpy_r_r155;
    int64_t cpy_r_r156;
    char cpy_r_r157;
    CPyPtr cpy_r_r158;
    CPyPtr cpy_r_r159;
    int64_t cpy_r_r160;
    CPyPtr cpy_r_r161;
    PyObject *cpy_r_r162;
    PyObject *cpy_r_i;
    int32_t cpy_r_r163;
    char cpy_r_r164;
    char cpy_r_r165;
    PyObject *cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject **cpy_r_r169;
    PyObject *cpy_r_r170;
    PyObject *cpy_r_r171;
    int32_t cpy_r_r172;
    char cpy_r_r173;
    int64_t cpy_r_r174;
    PyObject *cpy_r_r175;
    PyObject *cpy_r_r176;
    PyObject *cpy_r_r177;
    PyObject *cpy_r_r178;
    PyObject *cpy_r_r179;
    PyObject *cpy_r_r180;
    PyObject *cpy_r_r181;
    PyObject *cpy_r_r182;
    PyObject *cpy_r_r183;
    PyObject *cpy_r_r184;
    PyObject *cpy_r_r185;
    PyObject *cpy_r_r186;
    PyObject *cpy_r_r187;
    PyObject *cpy_r_r188;
    PyObject *cpy_r_r189;
    PyObject **cpy_r_r191;
    PyObject *cpy_r_r192;
    PyObject *cpy_r_r193;
    PyObject *cpy_r_r194;
    PyObject *cpy_r_r195;
    PyObject *cpy_r_r196;
    PyObject **cpy_r_r198;
    PyObject *cpy_r_r199;
    tuple_T3OOO cpy_r_r200;
    PyObject *cpy_r_r201;
    PyObject *cpy_r_r202;
    PyObject *cpy_r_r203;
    char cpy_r_r204;
    char cpy_r_r205;
    PyObject *cpy_r_r206;
    PyObject *cpy_r_r207;
    PyObject *cpy_r_r208;
    PyObject *cpy_r_r209;
    PyObject *cpy_r_r210;
    PyObject **cpy_r_r212;
    PyObject *cpy_r_r213;
    PyObject *cpy_r_r214;
    PyObject *cpy_r_r215;
    PyObject *cpy_r_r216;
    PyObject *cpy_r_r217;
    PyObject *cpy_r_r218;
    PyObject **cpy_r_r220;
    PyObject *cpy_r_r221;
    PyObject *cpy_r_r222;
    PyObject *cpy_r_r223;
    PyObject *cpy_r_r224;
    PyObject *cpy_r_r225;
    PyObject *cpy_r_r226;
    PyObject **cpy_r_r228;
    PyObject *cpy_r_r229;
    char cpy_r_r230;
    PyObject *cpy_r_r231;
    PyObject *cpy_r_r232;
    PyObject *cpy_r_r233;
    PyObject *cpy_r_r234;
    PyObject *cpy_r_r235;
    PyObject *cpy_r_r236;
    PyObject *cpy_r_r237;
    PyObject *cpy_r_r238;
    PyObject *cpy_r_r239;
    PyObject *cpy_r_r240;
    PyObject **cpy_r_r242;
    PyObject *cpy_r_r243;
    PyObject *cpy_r_r244;
    PyObject *cpy_r_r245;
    PyObject *cpy_r_r246;
    PyObject *cpy_r_r247;
    PyObject **cpy_r_r249;
    PyObject *cpy_r_r250;
    PyObject *cpy_r_r251;
    PyObject *cpy_r_r252;
    PyObject *cpy_r_r253;
    PyObject *cpy_r_r254;
    PyObject *cpy_r_r255;
    PyObject *cpy_r_r256;
    PyObject *cpy_r_r257;
    PyObject *cpy_r_r258;
    PyObject **cpy_r_r260;
    PyObject *cpy_r_r261;
    PyObject *cpy_r_r262;
    PyObject *cpy_r_r263;
    PyObject *cpy_r_r264;
    PyObject *cpy_r_r265;
    PyObject *cpy_r_r266;
    PyObject *cpy_r_r267;
    int64_t cpy_r_r268;
    CPyPtr cpy_r_r269;
    int64_t cpy_r_r270;
    char cpy_r_r271;
    CPyPtr cpy_r_r272;
    CPyPtr cpy_r_r273;
    int64_t cpy_r_r274;
    CPyPtr cpy_r_r275;
    PyObject *cpy_r_r276;
    PyObject *cpy_r_r277;
    PyObject *cpy_r_r278;
    PyObject *cpy_r_r279;
    PyObject *cpy_r_r280;
    PyObject *cpy_r_r281;
    PyObject *cpy_r_r282;
    PyObject **cpy_r_r284;
    PyObject *cpy_r_r285;
    PyObject *cpy_r_r286;
    int64_t cpy_r_r287;
    CPyPtr cpy_r_r288;
    int64_t cpy_r_r289;
    char cpy_r_r290;
    CPyPtr cpy_r_r291;
    CPyPtr cpy_r_r292;
    int64_t cpy_r_r293;
    CPyPtr cpy_r_r294;
    PyObject *cpy_r_r295;
    PyObject *cpy_r_i_2;
    int32_t cpy_r_r296;
    char cpy_r_r297;
    char cpy_r_r298;
    PyObject *cpy_r_r299;
    PyObject *cpy_r_r300;
    PyObject **cpy_r_r302;
    PyObject *cpy_r_r303;
    PyObject *cpy_r_r304;
    int32_t cpy_r_r305;
    char cpy_r_r306;
    int64_t cpy_r_r307;
    PyObject *cpy_r_r308;
    PyObject *cpy_r_r309;
    PyObject *cpy_r_r310;
    PyObject *cpy_r_r311;
    PyObject *cpy_r_r312;
    PyObject *cpy_r_r313;
    PyObject *cpy_r_contract_source;
    int64_t cpy_r_r314;
    char cpy_r_r315;
    CPyTagged cpy_r_r316;
    char cpy_r_r317;
    PyObject *cpy_r_r318;
    PyObject *cpy_r_r319;
    PyObject *cpy_r_r320;
    PyObject *cpy_r_r321;
    PyObject *cpy_r_r322;
    PyObject **cpy_r_r324;
    PyObject *cpy_r_r325;
    PyObject *cpy_r_r326;
    PyObject *cpy_r_r327;
    PyObject *cpy_r_r328;
    PyObject *cpy_r_r329;
    PyObject *cpy_r_r330;
    PyObject *cpy_r_r331;
    PyObject *cpy_r_r332;
    PyObject **cpy_r_r334;
    PyObject *cpy_r_r335;
    PyObject *cpy_r_r336;
    PyObject *cpy_r_r337;
    PyObject *cpy_r_r338;
    PyObject *cpy_r_r339;
    PyObject *cpy_r_r340;
    PyObject *cpy_r_r341;
    PyObject *cpy_r_r342;
    PyObject **cpy_r_r344;
    PyObject *cpy_r_r345;
    PyObject *cpy_r_r346;
    PyObject *cpy_r_r347;
    PyObject *cpy_r_r348;
    PyObject *cpy_r_r349;
    PyObject *cpy_r_r350;
    PyObject *cpy_r_r351;
    PyObject *cpy_r_r352;
    PyObject **cpy_r_r354;
    PyObject *cpy_r_r355;
    PyObject *cpy_r_r356;
    PyObject *cpy_r_r357;
    PyObject *cpy_r_r358;
    PyObject **cpy_r_r360;
    PyObject *cpy_r_r361;
    PyObject *cpy_r_r362;
    PyObject *cpy_r_r363;
    PyObject *cpy_r_r364;
    PyObject *cpy_r_r365;
    PyObject **cpy_r_r367;
    PyObject *cpy_r_r368;
    PyObject *cpy_r_r369;
    PyObject *cpy_r_r370;
    PyObject *cpy_r_r371;
    PyObject *cpy_r_r372;
    PyObject **cpy_r_r374;
    PyObject *cpy_r_r375;
    PyObject *cpy_r_r376;
    PyObject *cpy_r_r377;
    PyObject *cpy_r_r378;
    PyObject *cpy_r_r379;
    PyObject **cpy_r_r381;
    PyObject *cpy_r_r382;
    PyObject *cpy_r_r383;
    PyObject *cpy_r_r384;
    PyObject **cpy_r_r386;
    PyObject *cpy_r_r387;
    int64_t cpy_r_r388;
    tuple_T3OOO cpy_r_r389;
    tuple_T3OOO cpy_r_r390;
    PyObject *cpy_r_r391;
    PyObject *cpy_r_r392;
    PyObject *cpy_r_r393;
    PyObject **cpy_r_r395;
    PyObject *cpy_r_r396;
    int32_t cpy_r_r397;
    char cpy_r_r398;
    char cpy_r_r399;
    char cpy_r_r400;
    tuple_T3OOO cpy_r_r401;
    tuple_T3OOO cpy_r_r402;
    tuple_T3OOO cpy_r_r403;
    PyObject *cpy_r_r404;
    PyObject **cpy_r_r406;
    PyObject *cpy_r_r407;
    char cpy_r_r408;
    char cpy_r_r409;
    char cpy_r_r410;
    char cpy_r_r411;
    cpy_r_r0 = NULL;
    cpy_r_dot_sol_file = cpy_r_r0;
    cpy_r_r1 = 0;
CPyL1: ;
    cpy_r_r2 = (CPyPtr)&((PyVarObject *)cpy_r_file_list)->ob_size;
    cpy_r_r3 = *(int64_t *)cpy_r_r2;
    cpy_r_r4 = cpy_r_r1 < cpy_r_r3;
    if (!cpy_r_r4) goto CPyL207;
    cpy_r_r5 = (CPyPtr)&((PyListObject *)cpy_r_file_list)->ob_item;
    cpy_r_r6 = *(CPyPtr *)cpy_r_r5;
    cpy_r_r7 = cpy_r_r1 * 8;
    cpy_r_r8 = cpy_r_r6 + cpy_r_r7;
    cpy_r_r9 = *(PyObject * *)cpy_r_r8;
    CPy_INCREF(cpy_r_r9);
    if (likely(PyUnicode_Check(cpy_r_r9)))
        cpy_r_r10 = cpy_r_r9;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 119, CPyStatic_globals, "str", cpy_r_r9);
        goto CPyL208;
    }
    cpy_r_r11 = CPyModule_os;
    cpy_r_r12 = CPyStatics[16]; /* 'getcwd' */
    cpy_r_r13 = CPyObject_GetAttr(cpy_r_r11, cpy_r_r12);
    if (unlikely(cpy_r_r13 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL209;
    }
    cpy_r_r14 = PyObject_Vectorcall(cpy_r_r13, 0, 0, 0);
    CPy_DECREF(cpy_r_r13);
    if (unlikely(cpy_r_r14 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL209;
    }
    if (likely(PyUnicode_Check(cpy_r_r14)))
        cpy_r_r15 = cpy_r_r14;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals, "str", cpy_r_r14);
        goto CPyL209;
    }
    cpy_r_r16 = CPyModule_os;
    cpy_r_r17 = CPyStatics[17]; /* 'path' */
    cpy_r_r18 = CPyObject_GetAttr(cpy_r_r16, cpy_r_r17);
    if (unlikely(cpy_r_r18 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL210;
    }
    cpy_r_r19 = CPyStatics[18]; /* 'join' */
    cpy_r_r20 = CPyObject_GetAttr(cpy_r_r18, cpy_r_r19);
    CPy_DECREF(cpy_r_r18);
    if (unlikely(cpy_r_r20 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL210;
    }
    PyObject *cpy_r_r21[2] = {cpy_r_r15, cpy_r_r10};
    cpy_r_r22 = (PyObject **)&cpy_r_r21;
    cpy_r_r23 = PyObject_Vectorcall(cpy_r_r20, cpy_r_r22, 2, 0);
    CPy_DECREF(cpy_r_r20);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL210;
    }
    CPy_DECREF(cpy_r_r15);
    if (likely(PyUnicode_Check(cpy_r_r23)))
        cpy_r_r24 = cpy_r_r23;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals, "str", cpy_r_r23);
        goto CPyL209;
    }
    cpy_r_r25 = CPyModule_builtins;
    cpy_r_r26 = CPyStatics[19]; /* 'open' */
    cpy_r_r27 = CPyObject_GetAttr(cpy_r_r25, cpy_r_r26);
    if (unlikely(cpy_r_r27 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL211;
    }
    PyObject *cpy_r_r28[1] = {cpy_r_r24};
    cpy_r_r29 = (PyObject **)&cpy_r_r28;
    cpy_r_r30 = PyObject_Vectorcall(cpy_r_r27, cpy_r_r29, 1, 0);
    CPy_DECREF(cpy_r_r27);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL211;
    }
    CPy_DECREF(cpy_r_r24);
    cpy_r_r31 = CPy_TYPE(cpy_r_r30);
    cpy_r_r32 = CPyStatics[20]; /* '__exit__' */
    cpy_r_r33 = CPyObject_GetAttr(cpy_r_r31, cpy_r_r32);
    if (unlikely(cpy_r_r33 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL212;
    }
    cpy_r_r34 = CPyStatics[21]; /* '__enter__' */
    cpy_r_r35 = CPyObject_GetAttr(cpy_r_r31, cpy_r_r34);
    CPy_DECREF(cpy_r_r31);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL213;
    }
    PyObject *cpy_r_r36[1] = {cpy_r_r30};
    cpy_r_r37 = (PyObject **)&cpy_r_r36;
    cpy_r_r38 = PyObject_Vectorcall(cpy_r_r35, cpy_r_r37, 1, 0);
    CPy_DECREF(cpy_r_r35);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL213;
    }
    cpy_r_r39 = 1;
    cpy_r_r40 = CPyStatics[22]; /* 'readlines' */
    PyObject *cpy_r_r41[1] = {cpy_r_r38};
    cpy_r_r42 = (PyObject **)&cpy_r_r41;
    cpy_r_r43 = PyObject_VectorcallMethod(cpy_r_r40, cpy_r_r42, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 121, CPyStatic_globals);
        goto CPyL214;
    }
    CPy_DECREF(cpy_r_r38);
    if (likely(PyList_Check(cpy_r_r43)))
        cpy_r_r44 = cpy_r_r43;
    else {
        CPy_TypeError("list", cpy_r_r43); 
        cpy_r_r44 = NULL;
    }
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 121, CPyStatic_globals);
        goto CPyL19;
    } else
        goto CPyL215;
CPyL18: ;
    cpy_r_dot_sol_file = cpy_r_r44;
    goto CPyL27;
CPyL19: ;
    cpy_r_r45 = CPy_CatchError();
    cpy_r_r39 = 0;
    cpy_r_r46 = CPy_GetExcInfo();
    cpy_r_r47 = cpy_r_r46.f0;
    CPy_INCREF(cpy_r_r47);
    cpy_r_r48 = cpy_r_r46.f1;
    CPy_INCREF(cpy_r_r48);
    cpy_r_r49 = cpy_r_r46.f2;
    CPy_INCREF(cpy_r_r49);
    CPy_DecRef(cpy_r_r46.f0);
    CPy_DecRef(cpy_r_r46.f1);
    CPy_DecRef(cpy_r_r46.f2);
    PyObject *cpy_r_r50[4] = {cpy_r_r30, cpy_r_r47, cpy_r_r48, cpy_r_r49};
    cpy_r_r51 = (PyObject **)&cpy_r_r50;
    cpy_r_r52 = PyObject_Vectorcall(cpy_r_r33, cpy_r_r51, 4, 0);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL216;
    }
    CPy_DecRef(cpy_r_r47);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r49);
    cpy_r_r53 = PyObject_IsTrue(cpy_r_r52);
    CPy_DecRef(cpy_r_r52);
    cpy_r_r54 = cpy_r_r53 >= 0;
    if (unlikely(!cpy_r_r54)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r55 = cpy_r_r53;
    if (cpy_r_r55) goto CPyL24;
    CPy_Reraise();
    if (!0) {
        goto CPyL25;
    } else
        goto CPyL217;
CPyL23: ;
    CPy_Unreachable();
CPyL24: ;
    CPy_RestoreExcInfo(cpy_r_r45);
    CPy_DecRef(cpy_r_r45.f0);
    CPy_DecRef(cpy_r_r45.f1);
    CPy_DecRef(cpy_r_r45.f2);
    goto CPyL27;
CPyL25: ;
    CPy_RestoreExcInfo(cpy_r_r45);
    CPy_DecRef(cpy_r_r45.f0);
    CPy_DecRef(cpy_r_r45.f1);
    CPy_DecRef(cpy_r_r45.f2);
    cpy_r_r56 = CPy_KeepPropagating();
    if (!cpy_r_r56) {
        goto CPyL28;
    } else
        goto CPyL218;
CPyL26: ;
    CPy_Unreachable();
CPyL27: ;
    tuple_T3OOO __tmp2 = { NULL, NULL, NULL };
    cpy_r_r57 = __tmp2;
    cpy_r_r58 = cpy_r_r57;
    goto CPyL29;
CPyL28: ;
    cpy_r_r59 = CPy_CatchError();
    cpy_r_r58 = cpy_r_r59;
CPyL29: ;
    if (!cpy_r_r39) goto CPyL219;
    cpy_r_r60 = (PyObject *)&_Py_NoneStruct;
    PyObject *cpy_r_r61[4] = {cpy_r_r30, cpy_r_r60, cpy_r_r60, cpy_r_r60};
    cpy_r_r62 = (PyObject **)&cpy_r_r61;
    cpy_r_r63 = PyObject_Vectorcall(cpy_r_r33, cpy_r_r62, 4, 0);
    CPy_DECREF(cpy_r_r33);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 120, CPyStatic_globals);
        goto CPyL220;
    } else
        goto CPyL221;
CPyL31: ;
    CPy_DECREF(cpy_r_r30);
CPyL32: ;
    if (cpy_r_r58.f0 == NULL) {
        goto CPyL39;
    } else
        goto CPyL222;
CPyL33: ;
    CPy_Reraise();
    if (!0) {
        goto CPyL35;
    } else
        goto CPyL223;
CPyL34: ;
    CPy_Unreachable();
CPyL35: ;
    if (cpy_r_r58.f0 == NULL) goto CPyL37;
    CPy_RestoreExcInfo(cpy_r_r58);
    CPy_XDECREF(cpy_r_r58.f0);
    CPy_XDECREF(cpy_r_r58.f1);
    CPy_XDECREF(cpy_r_r58.f2);
CPyL37: ;
    cpy_r_r64 = CPy_KeepPropagating();
    if (!cpy_r_r64) goto CPyL206;
    CPy_Unreachable();
CPyL39: ;
    cpy_r_r65 = PyList_New(0);
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 123, CPyStatic_globals);
        goto CPyL209;
    }
    cpy_r_r66 = 0;
CPyL41: ;
    if (cpy_r_dot_sol_file == NULL) {
        goto CPyL224;
    } else
        goto CPyL44;
CPyL42: ;
    PyErr_SetString(PyExc_UnboundLocalError, "local variable \"dot_sol_file\" referenced before assignment");
    cpy_r_r67 = 0;
    if (unlikely(!cpy_r_r67)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", -1, CPyStatic_globals);
        goto CPyL206;
    }
    CPy_Unreachable();
CPyL44: ;
    cpy_r_r68 = (CPyPtr)&((PyVarObject *)cpy_r_dot_sol_file)->ob_size;
    cpy_r_r69 = *(int64_t *)cpy_r_r68;
    cpy_r_r70 = cpy_r_r66 < cpy_r_r69;
    if (!cpy_r_r70) goto CPyL70;
    if (cpy_r_dot_sol_file == NULL) {
        goto CPyL225;
    } else
        goto CPyL48;
CPyL46: ;
    PyErr_SetString(PyExc_UnboundLocalError, "local variable \"dot_sol_file\" referenced before assignment");
    cpy_r_r71 = 0;
    if (unlikely(!cpy_r_r71)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", -1, CPyStatic_globals);
        goto CPyL206;
    }
    CPy_Unreachable();
CPyL48: ;
    cpy_r_r72 = (CPyPtr)&((PyListObject *)cpy_r_dot_sol_file)->ob_item;
    cpy_r_r73 = *(CPyPtr *)cpy_r_r72;
    cpy_r_r74 = cpy_r_r66 * 8;
    cpy_r_r75 = cpy_r_r73 + cpy_r_r74;
    cpy_r_r76 = *(PyObject * *)cpy_r_r75;
    CPy_INCREF(cpy_r_r76);
    if (likely(PyUnicode_Check(cpy_r_r76)))
        cpy_r_r77 = cpy_r_r76;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 125, CPyStatic_globals, "str", cpy_r_r76);
        goto CPyL226;
    }
    cpy_r_r78 = 1;
    cpy_r_r79 = CPyStatics[23]; /* 'contract' */
    cpy_r_r80 = CPyStatics[24]; /* '{' */
    cpy_r_r81 = PyList_New(2);
    if (unlikely(cpy_r_r81 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 126, CPyStatic_globals);
        goto CPyL227;
    }
    cpy_r_r82 = (CPyPtr)&((PyListObject *)cpy_r_r81)->ob_item;
    cpy_r_r83 = *(CPyPtr *)cpy_r_r82;
    CPy_INCREF(cpy_r_r79);
    *(PyObject * *)cpy_r_r83 = cpy_r_r79;
    CPy_INCREF(cpy_r_r80);
    cpy_r_r84 = cpy_r_r83 + 8;
    *(PyObject * *)cpy_r_r84 = cpy_r_r80;
    cpy_r_r85 = 0;
CPyL51: ;
    cpy_r_r86 = (CPyPtr)&((PyVarObject *)cpy_r_r81)->ob_size;
    cpy_r_r87 = *(int64_t *)cpy_r_r86;
    cpy_r_r88 = cpy_r_r85 < cpy_r_r87;
    if (!cpy_r_r88) goto CPyL228;
    cpy_r_r89 = (CPyPtr)&((PyListObject *)cpy_r_r81)->ob_item;
    cpy_r_r90 = *(CPyPtr *)cpy_r_r89;
    cpy_r_r91 = cpy_r_r85 * 8;
    cpy_r_r92 = cpy_r_r90 + cpy_r_r91;
    cpy_r_r93 = *(PyObject * *)cpy_r_r92;
    CPy_INCREF(cpy_r_r93);
    if (likely(PyUnicode_Check(cpy_r_r93)))
        cpy_r_r94 = cpy_r_r93;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 126, CPyStatic_globals, "str", cpy_r_r93);
        goto CPyL229;
    }
    cpy_r__ = cpy_r_r94;
    if (likely(PyUnicode_Check(cpy_r__)))
        cpy_r_r95 = cpy_r__;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 126, CPyStatic_globals, "str", cpy_r__);
        goto CPyL229;
    }
    cpy_r_r96 = PyUnicode_Contains(cpy_r_r77, cpy_r_r95);
    CPy_DECREF(cpy_r_r95);
    cpy_r_r97 = cpy_r_r96 >= 0;
    if (unlikely(!cpy_r_r97)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 126, CPyStatic_globals);
        goto CPyL229;
    }
    cpy_r_r98 = cpy_r_r96;
    cpy_r_r99 = cpy_r_r98 ^ 1;
    if (cpy_r_r99) {
        goto CPyL230;
    } else
        goto CPyL57;
CPyL56: ;
    cpy_r_r78 = 0;
    goto CPyL58;
CPyL57: ;
    cpy_r_r100 = cpy_r_r85 + 1;
    cpy_r_r85 = cpy_r_r100;
    goto CPyL51;
CPyL58: ;
    if (!cpy_r_r78) goto CPyL231;
    cpy_r_r101 = CPyStatics[25]; /* 'abstract' */
    cpy_r_r102 = PyUnicode_Contains(cpy_r_r77, cpy_r_r101);
    cpy_r_r103 = cpy_r_r102 >= 0;
    if (unlikely(!cpy_r_r103)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 126, CPyStatic_globals);
        goto CPyL227;
    }
    cpy_r_r104 = cpy_r_r102;
    cpy_r_r105 = cpy_r_r104 ^ 1;
    if (!cpy_r_r105) goto CPyL231;
    cpy_r_r106 = CPyStatics[26]; /* 'contract ' */
    cpy_r_r107 = CPyStr_Find(cpy_r_r77, cpy_r_r106, 0, 1);
    if (unlikely(cpy_r_r107 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 127, CPyStatic_globals);
        goto CPyL227;
    }
    cpy_r_r108 = CPyStatics[26]; /* 'contract ' */
    cpy_r_r109 = CPyStr_Size_size_t(cpy_r_r108);
    cpy_r_r110 = cpy_r_r109 >= 0;
    if (unlikely(!cpy_r_r110)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 127, CPyStatic_globals);
        goto CPyL232;
    }
    cpy_r_r111 = cpy_r_r109 << 1;
    cpy_r_r112 = CPyTagged_Add(cpy_r_r107, cpy_r_r111);
    CPyTagged_DECREF(cpy_r_r107);
    cpy_r_r113 = CPyStr_GetSlice(cpy_r_r77, cpy_r_r112, 9223372036854775806LL);
    if (unlikely(cpy_r_r113 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 128, CPyStatic_globals);
        goto CPyL233;
    }
    if (likely(PyUnicode_Check(cpy_r_r113)))
        cpy_r_r114 = cpy_r_r113;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 128, CPyStatic_globals, "str", cpy_r_r113);
        goto CPyL233;
    }
    cpy_r_r115 = CPyStatics[27]; /* ' ' */
    cpy_r_r116 = CPyStr_Find(cpy_r_r114, cpy_r_r115, 0, 1);
    CPy_DECREF(cpy_r_r114);
    if (unlikely(cpy_r_r116 == CPY_INT_TAG)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 128, CPyStatic_globals);
        goto CPyL233;
    }
    cpy_r_r117 = CPyTagged_Add(cpy_r_r116, cpy_r_r112);
    CPyTagged_DECREF(cpy_r_r116);
    cpy_r_r118 = CPyStr_GetSlice(cpy_r_r77, cpy_r_r112, cpy_r_r117);
    CPy_DECREF(cpy_r_r77);
    CPyTagged_DECREF(cpy_r_r112);
    CPyTagged_DECREF(cpy_r_r117);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 129, CPyStatic_globals);
        goto CPyL226;
    }
    if (likely(PyUnicode_Check(cpy_r_r118)))
        cpy_r_r119 = cpy_r_r118;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 129, CPyStatic_globals, "str", cpy_r_r118);
        goto CPyL226;
    }
    cpy_r_r120 = PyList_Append(cpy_r_r65, cpy_r_r119);
    CPy_DECREF(cpy_r_r119);
    cpy_r_r121 = cpy_r_r120 >= 0;
    if (unlikely(!cpy_r_r121)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 130, CPyStatic_globals);
        goto CPyL226;
    }
CPyL69: ;
    cpy_r_r122 = cpy_r_r66 + 1;
    cpy_r_r66 = cpy_r_r122;
    goto CPyL41;
CPyL70: ;
    cpy_r_r123 = CPyStatic_globals;
    cpy_r_r124 = CPyStatics[28]; /* 'contracts_in_file' */
    cpy_r_r125 = CPyDict_GetItem(cpy_r_r123, cpy_r_r124);
    if (unlikely(cpy_r_r125 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 132, CPyStatic_globals);
        goto CPyL226;
    }
    if (likely(PyDict_Check(cpy_r_r125)))
        cpy_r_r126 = cpy_r_r125;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 132, CPyStatic_globals, "dict", cpy_r_r125);
        goto CPyL226;
    }
    cpy_r_r127 = CPyDict_SetItem(cpy_r_r126, cpy_r_r10, cpy_r_r65);
    CPy_DECREF(cpy_r_r126);
    CPy_DECREF(cpy_r_r10);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    cpy_r_r128 = cpy_r_r127 >= 0;
    if (unlikely(!cpy_r_r128)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 132, CPyStatic_globals);
        goto CPyL208;
    }
    cpy_r_r129 = cpy_r_r1 + 1;
    cpy_r_r1 = cpy_r_r129;
    goto CPyL1;
CPyL74: ;
    cpy_r_r130 = CPyStatic_globals;
    cpy_r_r131 = CPyStatics[28]; /* 'contracts_in_file' */
    cpy_r_r132 = CPyDict_GetItem(cpy_r_r130, cpy_r_r131);
    if (unlikely(cpy_r_r132 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals);
        goto CPyL206;
    }
    if (likely(PyDict_Check(cpy_r_r132)))
        cpy_r_r133 = cpy_r_r132;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals, "dict", cpy_r_r132);
        goto CPyL206;
    }
    cpy_r_r134 = 0;
    cpy_r_r135 = PyDict_Size(cpy_r_r133);
    cpy_r_r136 = CPyDict_GetKeysIter(cpy_r_r133);
    if (unlikely(cpy_r_r136 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals);
        goto CPyL234;
    }
CPyL77: ;
    cpy_r_r137 = CPyDict_NextKey(cpy_r_r136, cpy_r_r134);
    cpy_r_r138 = cpy_r_r137.f1;
    cpy_r_r134 = cpy_r_r138;
    cpy_r_r139 = cpy_r_r137.f0;
    if (!cpy_r_r139) goto CPyL235;
    cpy_r_r140 = cpy_r_r137.f2;
    CPy_INCREF(cpy_r_r140);
    CPy_DECREF(cpy_r_r137.f2);
    if (likely(PyUnicode_Check(cpy_r_r140)))
        cpy_r_r141 = cpy_r_r140;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals, "str", cpy_r_r140);
        goto CPyL236;
    }
    cpy_r_r142 = CPyStatics[10]; /* '.sol' */
    cpy_r_r143 = CPyStatics[11]; /* '' */
    cpy_r_r144 = PyUnicode_Replace(cpy_r_r141, cpy_r_r142, cpy_r_r143, -1);
    if (unlikely(cpy_r_r144 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 135, CPyStatic_globals);
        goto CPyL237;
    }
    cpy_r_r145 = PyList_New(0);
    if (unlikely(cpy_r_r145 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 136, CPyStatic_globals);
        goto CPyL238;
    }
    cpy_r_r146 = CPyStatics[29]; /* '([A-Z][a-z]*)' */
    cpy_r_r147 = CPyModule_re;
    cpy_r_r148 = CPyStatics[30]; /* 'split' */
    cpy_r_r149 = CPyObject_GetAttr(cpy_r_r147, cpy_r_r148);
    if (unlikely(cpy_r_r149 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 137, CPyStatic_globals);
        goto CPyL239;
    }
    PyObject *cpy_r_r150[2] = {cpy_r_r146, cpy_r_r144};
    cpy_r_r151 = (PyObject **)&cpy_r_r150;
    cpy_r_r152 = PyObject_Vectorcall(cpy_r_r149, cpy_r_r151, 2, 0);
    CPy_DECREF(cpy_r_r149);
    if (unlikely(cpy_r_r152 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 137, CPyStatic_globals);
        goto CPyL239;
    }
    CPy_DECREF(cpy_r_r144);
    if (likely(PyList_Check(cpy_r_r152)))
        cpy_r_r153 = cpy_r_r152;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 137, CPyStatic_globals, "list", cpy_r_r152);
        goto CPyL240;
    }
    cpy_r_r154 = 0;
CPyL85: ;
    cpy_r_r155 = (CPyPtr)&((PyVarObject *)cpy_r_r153)->ob_size;
    cpy_r_r156 = *(int64_t *)cpy_r_r155;
    cpy_r_r157 = cpy_r_r154 < cpy_r_r156;
    if (!cpy_r_r157) goto CPyL241;
    cpy_r_r158 = (CPyPtr)&((PyListObject *)cpy_r_r153)->ob_item;
    cpy_r_r159 = *(CPyPtr *)cpy_r_r158;
    cpy_r_r160 = cpy_r_r154 * 8;
    cpy_r_r161 = cpy_r_r159 + cpy_r_r160;
    cpy_r_r162 = *(PyObject * *)cpy_r_r161;
    CPy_INCREF(cpy_r_r162);
    cpy_r_i = cpy_r_r162;
    cpy_r_r163 = PyObject_IsTrue(cpy_r_i);
    cpy_r_r164 = cpy_r_r163 >= 0;
    if (unlikely(!cpy_r_r164)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 137, CPyStatic_globals);
        goto CPyL242;
    }
    cpy_r_r165 = cpy_r_r163;
    if (!cpy_r_r165) goto CPyL243;
    cpy_r_r166 = cpy_r_i;
    cpy_r_r167 = CPyStatics[31]; /* 'lower' */
    PyObject *cpy_r_r168[1] = {cpy_r_r166};
    cpy_r_r169 = (PyObject **)&cpy_r_r168;
    cpy_r_r170 = PyObject_VectorcallMethod(cpy_r_r167, cpy_r_r169, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r170 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 137, CPyStatic_globals);
        goto CPyL244;
    }
    CPy_DECREF(cpy_r_r166);
    cpy_r_r171 = cpy_r_r170;
    cpy_r_r172 = PyList_Append(cpy_r_r145, cpy_r_r171);
    CPy_DECREF(cpy_r_r171);
    cpy_r_r173 = cpy_r_r172 >= 0;
    if (unlikely(!cpy_r_r173)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 136, CPyStatic_globals);
        goto CPyL245;
    }
CPyL91: ;
    cpy_r_r174 = cpy_r_r154 + 1;
    cpy_r_r154 = cpy_r_r174;
    goto CPyL85;
CPyL92: ;
    cpy_r_r175 = CPyStatics[32]; /* '_' */
    cpy_r_r176 = PyUnicode_Join(cpy_r_r175, cpy_r_r145);
    CPy_DECREF_NO_IMM(cpy_r_r145);
    if (unlikely(cpy_r_r176 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 139, CPyStatic_globals);
        goto CPyL237;
    }
    cpy_r_r177 = CPyStatics[33]; /* '.py' */
    cpy_r_r178 = CPyStr_Build(2, cpy_r_r176, cpy_r_r177);
    CPy_DECREF(cpy_r_r176);
    if (unlikely(cpy_r_r178 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 139, CPyStatic_globals);
        goto CPyL237;
    }
    cpy_r_r179 = CPyModule_os;
    cpy_r_r180 = CPyStatics[16]; /* 'getcwd' */
    cpy_r_r181 = CPyObject_GetAttr(cpy_r_r179, cpy_r_r180);
    if (unlikely(cpy_r_r181 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals);
        goto CPyL246;
    }
    cpy_r_r182 = PyObject_Vectorcall(cpy_r_r181, 0, 0, 0);
    CPy_DECREF(cpy_r_r181);
    if (unlikely(cpy_r_r182 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals);
        goto CPyL246;
    }
    if (likely(PyUnicode_Check(cpy_r_r182)))
        cpy_r_r183 = cpy_r_r182;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals, "str", cpy_r_r182);
        goto CPyL246;
    }
    cpy_r_r184 = CPyStatics[34]; /* 'contract_data' */
    cpy_r_r185 = CPyModule_os;
    cpy_r_r186 = CPyStatics[17]; /* 'path' */
    cpy_r_r187 = CPyObject_GetAttr(cpy_r_r185, cpy_r_r186);
    if (unlikely(cpy_r_r187 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals);
        goto CPyL247;
    }
    cpy_r_r188 = CPyStatics[18]; /* 'join' */
    cpy_r_r189 = CPyObject_GetAttr(cpy_r_r187, cpy_r_r188);
    CPy_DECREF(cpy_r_r187);
    if (unlikely(cpy_r_r189 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals);
        goto CPyL247;
    }
    PyObject *cpy_r_r190[3] = {cpy_r_r183, cpy_r_r184, cpy_r_r178};
    cpy_r_r191 = (PyObject **)&cpy_r_r190;
    cpy_r_r192 = PyObject_Vectorcall(cpy_r_r189, cpy_r_r191, 3, 0);
    CPy_DECREF(cpy_r_r189);
    if (unlikely(cpy_r_r192 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals);
        goto CPyL247;
    }
    CPy_DECREF(cpy_r_r183);
    CPy_DECREF(cpy_r_r178);
    if (likely(PyUnicode_Check(cpy_r_r192)))
        cpy_r_r193 = cpy_r_r192;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 140, CPyStatic_globals, "str", cpy_r_r192);
        goto CPyL237;
    }
    cpy_r_r194 = CPyModule_os;
    cpy_r_r195 = CPyStatics[35]; /* 'remove' */
    cpy_r_r196 = CPyObject_GetAttr(cpy_r_r194, cpy_r_r195);
    if (unlikely(cpy_r_r196 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 143, CPyStatic_globals);
        goto CPyL104;
    }
    PyObject *cpy_r_r197[1] = {cpy_r_r193};
    cpy_r_r198 = (PyObject **)&cpy_r_r197;
    cpy_r_r199 = PyObject_Vectorcall(cpy_r_r196, cpy_r_r198, 1, 0);
    CPy_DECREF(cpy_r_r196);
    if (unlikely(cpy_r_r199 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 143, CPyStatic_globals);
    } else
        goto CPyL248;
CPyL104: ;
    cpy_r_r200 = CPy_CatchError();
    cpy_r_r201 = CPyModule_builtins;
    cpy_r_r202 = CPyStatics[36]; /* 'FileNotFoundError' */
    cpy_r_r203 = CPyObject_GetAttr(cpy_r_r201, cpy_r_r202);
    if (unlikely(cpy_r_r203 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 144, CPyStatic_globals);
        goto CPyL249;
    }
    cpy_r_r204 = CPy_ExceptionMatches(cpy_r_r203);
    CPy_DecRef(cpy_r_r203);
    if (cpy_r_r204) {
        goto CPyL108;
    } else
        goto CPyL250;
CPyL106: ;
    CPy_Reraise();
    if (!0) {
        goto CPyL109;
    } else
        goto CPyL251;
CPyL107: ;
    CPy_Unreachable();
CPyL108: ;
    CPy_RestoreExcInfo(cpy_r_r200);
    CPy_DecRef(cpy_r_r200.f0);
    CPy_DecRef(cpy_r_r200.f1);
    CPy_DecRef(cpy_r_r200.f2);
    goto CPyL111;
CPyL109: ;
    CPy_RestoreExcInfo(cpy_r_r200);
    CPy_DecRef(cpy_r_r200.f0);
    CPy_DecRef(cpy_r_r200.f1);
    CPy_DecRef(cpy_r_r200.f2);
    cpy_r_r205 = CPy_KeepPropagating();
    if (!cpy_r_r205) goto CPyL206;
    CPy_Unreachable();
CPyL111: ;
    cpy_r_r206 = CPyStatics[37]; /* 'compiling ' */
    cpy_r_r207 = CPyStr_Build(2, cpy_r_r206, cpy_r_r141);
    if (unlikely(cpy_r_r207 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 146, CPyStatic_globals);
        goto CPyL252;
    }
    cpy_r_r208 = CPyModule_builtins;
    cpy_r_r209 = CPyStatics[38]; /* 'print' */
    cpy_r_r210 = CPyObject_GetAttr(cpy_r_r208, cpy_r_r209);
    if (unlikely(cpy_r_r210 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 146, CPyStatic_globals);
        goto CPyL253;
    }
    PyObject *cpy_r_r211[1] = {cpy_r_r207};
    cpy_r_r212 = (PyObject **)&cpy_r_r211;
    cpy_r_r213 = PyObject_Vectorcall(cpy_r_r210, cpy_r_r212, 1, 0);
    CPy_DECREF(cpy_r_r210);
    if (unlikely(cpy_r_r213 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 146, CPyStatic_globals);
        goto CPyL253;
    } else
        goto CPyL254;
CPyL114: ;
    CPy_DECREF(cpy_r_r207);
    cpy_r_r214 = CPyDef__compile_dot_sol_files(cpy_r_r141);
    if (unlikely(cpy_r_r214 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 147, CPyStatic_globals);
        goto CPyL252;
    }
    cpy_r_r215 = CPyStatics[39]; /* 'w' */
    cpy_r_r216 = CPyModule_builtins;
    cpy_r_r217 = CPyStatics[19]; /* 'open' */
    cpy_r_r218 = CPyObject_GetAttr(cpy_r_r216, cpy_r_r217);
    if (unlikely(cpy_r_r218 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL255;
    }
    PyObject *cpy_r_r219[2] = {cpy_r_r193, cpy_r_r215};
    cpy_r_r220 = (PyObject **)&cpy_r_r219;
    cpy_r_r221 = PyObject_Vectorcall(cpy_r_r218, cpy_r_r220, 2, 0);
    CPy_DECREF(cpy_r_r218);
    if (unlikely(cpy_r_r221 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL255;
    }
    CPy_DECREF(cpy_r_r193);
    cpy_r_r222 = CPy_TYPE(cpy_r_r221);
    cpy_r_r223 = CPyStatics[20]; /* '__exit__' */
    cpy_r_r224 = CPyObject_GetAttr(cpy_r_r222, cpy_r_r223);
    if (unlikely(cpy_r_r224 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL256;
    }
    cpy_r_r225 = CPyStatics[21]; /* '__enter__' */
    cpy_r_r226 = CPyObject_GetAttr(cpy_r_r222, cpy_r_r225);
    CPy_DECREF(cpy_r_r222);
    if (unlikely(cpy_r_r226 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL257;
    }
    PyObject *cpy_r_r227[1] = {cpy_r_r221};
    cpy_r_r228 = (PyObject **)&cpy_r_r227;
    cpy_r_r229 = PyObject_Vectorcall(cpy_r_r226, cpy_r_r228, 1, 0);
    CPy_DECREF(cpy_r_r226);
    if (unlikely(cpy_r_r229 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL257;
    }
    cpy_r_r230 = 1;
    cpy_r_r231 = CPyStatics[40]; /* '"""\nGenerated by `' */
    cpy_r_r232 = CPyStatic_globals;
    cpy_r_r233 = CPyStatics[41]; /* '__file__' */
    cpy_r_r234 = CPyDict_GetItem(cpy_r_r232, cpy_r_r233);
    if (unlikely(cpy_r_r234 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL258;
    }
    if (likely(PyUnicode_Check(cpy_r_r234)))
        cpy_r_r235 = cpy_r_r234;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals, "str", cpy_r_r234);
        goto CPyL258;
    }
    cpy_r_r236 = CPyModule_os;
    cpy_r_r237 = CPyStatics[17]; /* 'path' */
    cpy_r_r238 = CPyObject_GetAttr(cpy_r_r236, cpy_r_r237);
    if (unlikely(cpy_r_r238 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL259;
    }
    cpy_r_r239 = CPyStatics[42]; /* 'basename' */
    cpy_r_r240 = CPyObject_GetAttr(cpy_r_r238, cpy_r_r239);
    CPy_DECREF(cpy_r_r238);
    if (unlikely(cpy_r_r240 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL259;
    }
    PyObject *cpy_r_r241[1] = {cpy_r_r235};
    cpy_r_r242 = (PyObject **)&cpy_r_r241;
    cpy_r_r243 = PyObject_Vectorcall(cpy_r_r240, cpy_r_r242, 1, 0);
    CPy_DECREF(cpy_r_r240);
    if (unlikely(cpy_r_r243 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL259;
    }
    CPy_DECREF(cpy_r_r235);
    if (likely(PyUnicode_Check(cpy_r_r243)))
        cpy_r_r244 = cpy_r_r243;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals, "str", cpy_r_r243);
        goto CPyL258;
    }
    cpy_r_r245 = CPyStatics[43]; /* '` script.\n' */
    cpy_r_r246 = CPyStr_Build(3, cpy_r_r231, cpy_r_r244, cpy_r_r245);
    CPy_DECREF(cpy_r_r244);
    if (unlikely(cpy_r_r246 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL258;
    }
    cpy_r_r247 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r248[2] = {cpy_r_r229, cpy_r_r246};
    cpy_r_r249 = (PyObject **)&cpy_r_r248;
    cpy_r_r250 = PyObject_VectorcallMethod(cpy_r_r247, cpy_r_r249, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r250 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 149, CPyStatic_globals);
        goto CPyL260;
    } else
        goto CPyL261;
CPyL129: ;
    CPy_DECREF(cpy_r_r246);
    cpy_r_r251 = CPyStatics[45]; /* 'Compiled with Solidity v' */
    cpy_r_r252 = CPyStatic_globals;
    cpy_r_r253 = CPyStatics[46]; /* 'solidity_version' */
    cpy_r_r254 = CPyDict_GetItem(cpy_r_r252, cpy_r_r253);
    if (unlikely(cpy_r_r254 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 150, CPyStatic_globals);
        goto CPyL258;
    }
    cpy_r_r255 = PyObject_Str(cpy_r_r254);
    CPy_DECREF(cpy_r_r254);
    if (unlikely(cpy_r_r255 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 150, CPyStatic_globals);
        goto CPyL258;
    }
    cpy_r_r256 = CPyStatics[47]; /* '.\n"""\n\n' */
    cpy_r_r257 = CPyStr_Build(3, cpy_r_r251, cpy_r_r255, cpy_r_r256);
    CPy_DECREF(cpy_r_r255);
    if (unlikely(cpy_r_r257 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 150, CPyStatic_globals);
        goto CPyL258;
    }
    cpy_r_r258 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r259[2] = {cpy_r_r229, cpy_r_r257};
    cpy_r_r260 = (PyObject **)&cpy_r_r259;
    cpy_r_r261 = PyObject_VectorcallMethod(cpy_r_r258, cpy_r_r260, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r261 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 150, CPyStatic_globals);
        goto CPyL262;
    } else
        goto CPyL263;
CPyL133: ;
    CPy_DECREF(cpy_r_r257);
    cpy_r_r262 = CPyStatic_globals;
    cpy_r_r263 = CPyStatics[28]; /* 'contracts_in_file' */
    cpy_r_r264 = CPyDict_GetItem(cpy_r_r262, cpy_r_r263);
    if (unlikely(cpy_r_r264 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 152, CPyStatic_globals);
        goto CPyL258;
    }
    if (likely(PyDict_Check(cpy_r_r264)))
        cpy_r_r265 = cpy_r_r264;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 152, CPyStatic_globals, "dict", cpy_r_r264);
        goto CPyL258;
    }
    cpy_r_r266 = CPyDict_GetItem(cpy_r_r265, cpy_r_r141);
    CPy_DECREF(cpy_r_r265);
    if (unlikely(cpy_r_r266 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 152, CPyStatic_globals);
        goto CPyL258;
    }
    if (likely(PyList_Check(cpy_r_r266)))
        cpy_r_r267 = cpy_r_r266;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 152, CPyStatic_globals, "list", cpy_r_r266);
        goto CPyL258;
    }
    cpy_r_r268 = 0;
CPyL138: ;
    cpy_r_r269 = (CPyPtr)&((PyVarObject *)cpy_r_r267)->ob_size;
    cpy_r_r270 = *(int64_t *)cpy_r_r269;
    cpy_r_r271 = cpy_r_r268 < cpy_r_r270;
    if (!cpy_r_r271) goto CPyL264;
    cpy_r_r272 = (CPyPtr)&((PyListObject *)cpy_r_r267)->ob_item;
    cpy_r_r273 = *(CPyPtr *)cpy_r_r272;
    cpy_r_r274 = cpy_r_r268 * 8;
    cpy_r_r275 = cpy_r_r273 + cpy_r_r274;
    cpy_r_r276 = *(PyObject * *)cpy_r_r275;
    CPy_INCREF(cpy_r_r276);
    if (likely(PyUnicode_Check(cpy_r_r276)))
        cpy_r_r277 = cpy_r_r276;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 152, CPyStatic_globals, "str", cpy_r_r276);
        goto CPyL265;
    }
    cpy_r_r278 = PyList_New(0);
    if (unlikely(cpy_r_r278 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 153, CPyStatic_globals);
        goto CPyL266;
    }
    cpy_r_r279 = CPyStatics[48]; /* '([A-Z0-9][a-z0-9]*)' */
    cpy_r_r280 = CPyModule_re;
    cpy_r_r281 = CPyStatics[30]; /* 'split' */
    cpy_r_r282 = CPyObject_GetAttr(cpy_r_r280, cpy_r_r281);
    if (unlikely(cpy_r_r282 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 154, CPyStatic_globals);
        goto CPyL267;
    }
    PyObject *cpy_r_r283[2] = {cpy_r_r279, cpy_r_r277};
    cpy_r_r284 = (PyObject **)&cpy_r_r283;
    cpy_r_r285 = PyObject_Vectorcall(cpy_r_r282, cpy_r_r284, 2, 0);
    CPy_DECREF(cpy_r_r282);
    if (unlikely(cpy_r_r285 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 154, CPyStatic_globals);
        goto CPyL267;
    }
    if (likely(PyList_Check(cpy_r_r285)))
        cpy_r_r286 = cpy_r_r285;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 154, CPyStatic_globals, "list", cpy_r_r285);
        goto CPyL267;
    }
    cpy_r_r287 = 0;
CPyL145: ;
    cpy_r_r288 = (CPyPtr)&((PyVarObject *)cpy_r_r286)->ob_size;
    cpy_r_r289 = *(int64_t *)cpy_r_r288;
    cpy_r_r290 = cpy_r_r287 < cpy_r_r289;
    if (!cpy_r_r290) goto CPyL268;
    cpy_r_r291 = (CPyPtr)&((PyListObject *)cpy_r_r286)->ob_item;
    cpy_r_r292 = *(CPyPtr *)cpy_r_r291;
    cpy_r_r293 = cpy_r_r287 * 8;
    cpy_r_r294 = cpy_r_r292 + cpy_r_r293;
    cpy_r_r295 = *(PyObject * *)cpy_r_r294;
    CPy_INCREF(cpy_r_r295);
    cpy_r_i_2 = cpy_r_r295;
    cpy_r_r296 = PyObject_IsTrue(cpy_r_i_2);
    cpy_r_r297 = cpy_r_r296 >= 0;
    if (unlikely(!cpy_r_r297)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 154, CPyStatic_globals);
        goto CPyL269;
    }
    cpy_r_r298 = cpy_r_r296;
    if (!cpy_r_r298) goto CPyL270;
    cpy_r_r299 = cpy_r_i_2;
    cpy_r_r300 = CPyStatics[49]; /* 'upper' */
    PyObject *cpy_r_r301[1] = {cpy_r_r299};
    cpy_r_r302 = (PyObject **)&cpy_r_r301;
    cpy_r_r303 = PyObject_VectorcallMethod(cpy_r_r300, cpy_r_r302, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r303 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 154, CPyStatic_globals);
        goto CPyL271;
    }
    CPy_DECREF(cpy_r_r299);
    cpy_r_r304 = cpy_r_r303;
    cpy_r_r305 = PyList_Append(cpy_r_r278, cpy_r_r304);
    CPy_DECREF(cpy_r_r304);
    cpy_r_r306 = cpy_r_r305 >= 0;
    if (unlikely(!cpy_r_r306)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 153, CPyStatic_globals);
        goto CPyL272;
    }
CPyL151: ;
    cpy_r_r307 = cpy_r_r287 + 1;
    cpy_r_r287 = cpy_r_r307;
    goto CPyL145;
CPyL152: ;
    cpy_r_r308 = CPyStatics[32]; /* '_' */
    cpy_r_r309 = PyUnicode_Join(cpy_r_r308, cpy_r_r278);
    CPy_DECREF_NO_IMM(cpy_r_r278);
    if (unlikely(cpy_r_r309 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 156, CPyStatic_globals);
        goto CPyL266;
    }
    cpy_r_r310 = CPyDef__get_compiled_contract_data(cpy_r_r214, cpy_r_r141, cpy_r_r277);
    if (unlikely(cpy_r_r310 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 158, CPyStatic_globals);
        goto CPyL273;
    }
    cpy_r_r311 = CPyStatics[50]; /* '# source: web3/_utils/contract_sources/' */
    cpy_r_r312 = CPyStatics[12]; /* ':' */
    cpy_r_r313 = CPyStr_Build(4, cpy_r_r311, cpy_r_r141, cpy_r_r312, cpy_r_r277);
    CPy_DECREF(cpy_r_r277);
    if (unlikely(cpy_r_r313 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 163, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_contract_source = cpy_r_r313;
    cpy_r_r314 = CPyStr_Size_size_t(cpy_r_contract_source);
    cpy_r_r315 = cpy_r_r314 >= 0;
    if (unlikely(!cpy_r_r315)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 165, CPyStatic_globals);
        goto CPyL275;
    }
    cpy_r_r316 = cpy_r_r314 << 1;
    cpy_r_r317 = (Py_ssize_t)cpy_r_r316 > (Py_ssize_t)176;
    if (!cpy_r_r317) goto CPyL159;
    cpy_r_r318 = CPyStatics[51]; /* '  # noqa: E501' */
    cpy_r_r319 = CPyStr_Append(cpy_r_contract_source, cpy_r_r318);
    if (unlikely(cpy_r_r319 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 166, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_contract_source = cpy_r_r319;
CPyL159: ;
    cpy_r_r320 = CPyStatics[52]; /* '\n' */
    cpy_r_r321 = CPyStr_Build(2, cpy_r_contract_source, cpy_r_r320);
    CPy_DECREF(cpy_r_contract_source);
    if (unlikely(cpy_r_r321 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 168, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_r322 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r323[2] = {cpy_r_r229, cpy_r_r321};
    cpy_r_r324 = (PyObject **)&cpy_r_r323;
    cpy_r_r325 = PyObject_VectorcallMethod(cpy_r_r322, cpy_r_r324, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r325 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 168, CPyStatic_globals);
        goto CPyL276;
    } else
        goto CPyL277;
CPyL161: ;
    CPy_DECREF(cpy_r_r321);
    cpy_r_r326 = CPyStatics[53]; /* '_BYTECODE = "' */
    cpy_r_r327 = CPyStatics[6]; /* 'bin' */
    cpy_r_r328 = CPyDict_GetItem(cpy_r_r310, cpy_r_r327);
    if (unlikely(cpy_r_r328 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 170, CPyStatic_globals);
        goto CPyL274;
    }
    if (likely(PyUnicode_Check(cpy_r_r328)))
        cpy_r_r329 = cpy_r_r328;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 170, CPyStatic_globals, "str", cpy_r_r328);
        goto CPyL274;
    }
    cpy_r_r330 = CPyStatics[54]; /* '"  # noqa: E501\n' */
    cpy_r_r331 = CPyStr_Build(4, cpy_r_r309, cpy_r_r326, cpy_r_r329, cpy_r_r330);
    CPy_DECREF(cpy_r_r329);
    if (unlikely(cpy_r_r331 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 170, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_r332 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r333[2] = {cpy_r_r229, cpy_r_r331};
    cpy_r_r334 = (PyObject **)&cpy_r_r333;
    cpy_r_r335 = PyObject_VectorcallMethod(cpy_r_r332, cpy_r_r334, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r335 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 169, CPyStatic_globals);
        goto CPyL278;
    } else
        goto CPyL279;
CPyL165: ;
    CPy_DECREF(cpy_r_r331);
    cpy_r_r336 = CPyStatics[55]; /* '_RUNTIME = "' */
    cpy_r_r337 = CPyStatics[7]; /* 'bin-runtime' */
    cpy_r_r338 = CPyDict_GetItem(cpy_r_r310, cpy_r_r337);
    if (unlikely(cpy_r_r338 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 173, CPyStatic_globals);
        goto CPyL274;
    }
    if (likely(PyUnicode_Check(cpy_r_r338)))
        cpy_r_r339 = cpy_r_r338;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 173, CPyStatic_globals, "str", cpy_r_r338);
        goto CPyL274;
    }
    cpy_r_r340 = CPyStatics[54]; /* '"  # noqa: E501\n' */
    cpy_r_r341 = CPyStr_Build(4, cpy_r_r309, cpy_r_r336, cpy_r_r339, cpy_r_r340);
    CPy_DECREF(cpy_r_r339);
    if (unlikely(cpy_r_r341 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 173, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_r342 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r343[2] = {cpy_r_r229, cpy_r_r341};
    cpy_r_r344 = (PyObject **)&cpy_r_r343;
    cpy_r_r345 = PyObject_VectorcallMethod(cpy_r_r342, cpy_r_r344, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r345 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 172, CPyStatic_globals);
        goto CPyL280;
    } else
        goto CPyL281;
CPyL169: ;
    CPy_DECREF(cpy_r_r341);
    cpy_r_r346 = CPyStatics[56]; /* '_ABI = ' */
    cpy_r_r347 = CPyStatics[5]; /* 'abi' */
    cpy_r_r348 = CPyDict_GetItem(cpy_r_r310, cpy_r_r347);
    CPy_DECREF(cpy_r_r310);
    if (unlikely(cpy_r_r348 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 175, CPyStatic_globals);
        goto CPyL282;
    }
    if (likely(PyUnicode_Check(cpy_r_r348)))
        cpy_r_r349 = cpy_r_r348;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 175, CPyStatic_globals, "str", cpy_r_r348);
        goto CPyL282;
    }
    cpy_r_r350 = CPyStatics[52]; /* '\n' */
    cpy_r_r351 = CPyStr_Build(4, cpy_r_r309, cpy_r_r346, cpy_r_r349, cpy_r_r350);
    CPy_DECREF(cpy_r_r349);
    if (unlikely(cpy_r_r351 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 175, CPyStatic_globals);
        goto CPyL282;
    }
    cpy_r_r352 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r353[2] = {cpy_r_r229, cpy_r_r351};
    cpy_r_r354 = (PyObject **)&cpy_r_r353;
    cpy_r_r355 = PyObject_VectorcallMethod(cpy_r_r352, cpy_r_r354, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r355 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 175, CPyStatic_globals);
        goto CPyL283;
    } else
        goto CPyL284;
CPyL173: ;
    CPy_DECREF(cpy_r_r351);
    cpy_r_r356 = CPyStatics[57]; /* '_DATA = {\n' */
    cpy_r_r357 = PyUnicode_Concat(cpy_r_r309, cpy_r_r356);
    if (unlikely(cpy_r_r357 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 176, CPyStatic_globals);
        goto CPyL282;
    }
    cpy_r_r358 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r359[2] = {cpy_r_r229, cpy_r_r357};
    cpy_r_r360 = (PyObject **)&cpy_r_r359;
    cpy_r_r361 = PyObject_VectorcallMethod(cpy_r_r358, cpy_r_r360, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r361 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 176, CPyStatic_globals);
        goto CPyL285;
    } else
        goto CPyL286;
CPyL175: ;
    CPy_DECREF(cpy_r_r357);
    cpy_r_r362 = CPyStatics[58]; /* '    "bytecode": ' */
    cpy_r_r363 = CPyStatics[59]; /* '_BYTECODE,\n' */
    cpy_r_r364 = CPyStr_Build(3, cpy_r_r362, cpy_r_r309, cpy_r_r363);
    if (unlikely(cpy_r_r364 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 177, CPyStatic_globals);
        goto CPyL282;
    }
    cpy_r_r365 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r366[2] = {cpy_r_r229, cpy_r_r364};
    cpy_r_r367 = (PyObject **)&cpy_r_r366;
    cpy_r_r368 = PyObject_VectorcallMethod(cpy_r_r365, cpy_r_r367, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r368 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 177, CPyStatic_globals);
        goto CPyL287;
    } else
        goto CPyL288;
CPyL177: ;
    CPy_DECREF(cpy_r_r364);
    cpy_r_r369 = CPyStatics[60]; /* '    "bytecode_runtime": ' */
    cpy_r_r370 = CPyStatics[61]; /* '_RUNTIME,\n' */
    cpy_r_r371 = CPyStr_Build(3, cpy_r_r369, cpy_r_r309, cpy_r_r370);
    if (unlikely(cpy_r_r371 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 178, CPyStatic_globals);
        goto CPyL282;
    }
    cpy_r_r372 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r373[2] = {cpy_r_r229, cpy_r_r371};
    cpy_r_r374 = (PyObject **)&cpy_r_r373;
    cpy_r_r375 = PyObject_VectorcallMethod(cpy_r_r372, cpy_r_r374, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r375 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 178, CPyStatic_globals);
        goto CPyL289;
    } else
        goto CPyL290;
CPyL179: ;
    CPy_DECREF(cpy_r_r371);
    cpy_r_r376 = CPyStatics[62]; /* '    "abi": ' */
    cpy_r_r377 = CPyStatics[63]; /* '_ABI,\n' */
    cpy_r_r378 = CPyStr_Build(3, cpy_r_r376, cpy_r_r309, cpy_r_r377);
    CPy_DECREF(cpy_r_r309);
    if (unlikely(cpy_r_r378 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 179, CPyStatic_globals);
        goto CPyL265;
    }
    cpy_r_r379 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r380[2] = {cpy_r_r229, cpy_r_r378};
    cpy_r_r381 = (PyObject **)&cpy_r_r380;
    cpy_r_r382 = PyObject_VectorcallMethod(cpy_r_r379, cpy_r_r381, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r382 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 179, CPyStatic_globals);
        goto CPyL291;
    } else
        goto CPyL292;
CPyL181: ;
    CPy_DECREF(cpy_r_r378);
    cpy_r_r383 = CPyStatics[64]; /* '}\n\n\n' */
    cpy_r_r384 = CPyStatics[44]; /* 'write' */
    PyObject *cpy_r_r385[2] = {cpy_r_r229, cpy_r_r383};
    cpy_r_r386 = (PyObject **)&cpy_r_r385;
    cpy_r_r387 = PyObject_VectorcallMethod(cpy_r_r384, cpy_r_r386, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r387 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 180, CPyStatic_globals);
        goto CPyL265;
    } else
        goto CPyL293;
CPyL182: ;
    cpy_r_r388 = cpy_r_r268 + 1;
    cpy_r_r268 = cpy_r_r388;
    goto CPyL138;
CPyL183: ;
    cpy_r_r389 = CPy_CatchError();
    cpy_r_r230 = 0;
    cpy_r_r390 = CPy_GetExcInfo();
    cpy_r_r391 = cpy_r_r390.f0;
    CPy_INCREF(cpy_r_r391);
    cpy_r_r392 = cpy_r_r390.f1;
    CPy_INCREF(cpy_r_r392);
    cpy_r_r393 = cpy_r_r390.f2;
    CPy_INCREF(cpy_r_r393);
    CPy_DecRef(cpy_r_r390.f0);
    CPy_DecRef(cpy_r_r390.f1);
    CPy_DecRef(cpy_r_r390.f2);
    PyObject *cpy_r_r394[4] = {cpy_r_r221, cpy_r_r391, cpy_r_r392, cpy_r_r393};
    cpy_r_r395 = (PyObject **)&cpy_r_r394;
    cpy_r_r396 = PyObject_Vectorcall(cpy_r_r224, cpy_r_r395, 4, 0);
    if (unlikely(cpy_r_r396 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL294;
    }
    CPy_DecRef(cpy_r_r391);
    CPy_DecRef(cpy_r_r392);
    CPy_DecRef(cpy_r_r393);
    cpy_r_r397 = PyObject_IsTrue(cpy_r_r396);
    CPy_DecRef(cpy_r_r396);
    cpy_r_r398 = cpy_r_r397 >= 0;
    if (unlikely(!cpy_r_r398)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL189;
    }
    cpy_r_r399 = cpy_r_r397;
    if (cpy_r_r399) goto CPyL188;
    CPy_Reraise();
    if (!0) {
        goto CPyL189;
    } else
        goto CPyL295;
CPyL187: ;
    CPy_Unreachable();
CPyL188: ;
    CPy_RestoreExcInfo(cpy_r_r389);
    CPy_DecRef(cpy_r_r389.f0);
    CPy_DecRef(cpy_r_r389.f1);
    CPy_DecRef(cpy_r_r389.f2);
    goto CPyL191;
CPyL189: ;
    CPy_RestoreExcInfo(cpy_r_r389);
    CPy_DecRef(cpy_r_r389.f0);
    CPy_DecRef(cpy_r_r389.f1);
    CPy_DecRef(cpy_r_r389.f2);
    cpy_r_r400 = CPy_KeepPropagating();
    if (!cpy_r_r400) {
        goto CPyL192;
    } else
        goto CPyL296;
CPyL190: ;
    CPy_Unreachable();
CPyL191: ;
    tuple_T3OOO __tmp3 = { NULL, NULL, NULL };
    cpy_r_r401 = __tmp3;
    cpy_r_r402 = cpy_r_r401;
    goto CPyL193;
CPyL192: ;
    cpy_r_r403 = CPy_CatchError();
    cpy_r_r402 = cpy_r_r403;
CPyL193: ;
    if (!cpy_r_r230) goto CPyL297;
    cpy_r_r404 = (PyObject *)&_Py_NoneStruct;
    PyObject *cpy_r_r405[4] = {cpy_r_r221, cpy_r_r404, cpy_r_r404, cpy_r_r404};
    cpy_r_r406 = (PyObject **)&cpy_r_r405;
    cpy_r_r407 = PyObject_Vectorcall(cpy_r_r224, cpy_r_r406, 4, 0);
    CPy_DECREF(cpy_r_r224);
    if (unlikely(cpy_r_r407 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 148, CPyStatic_globals);
        goto CPyL298;
    } else
        goto CPyL299;
CPyL195: ;
    CPy_DECREF(cpy_r_r221);
CPyL196: ;
    if (cpy_r_r402.f0 == NULL) {
        goto CPyL203;
    } else
        goto CPyL300;
CPyL197: ;
    CPy_Reraise();
    if (!0) {
        goto CPyL199;
    } else
        goto CPyL301;
CPyL198: ;
    CPy_Unreachable();
CPyL199: ;
    if (cpy_r_r402.f0 == NULL) goto CPyL201;
    CPy_RestoreExcInfo(cpy_r_r402);
    CPy_XDECREF(cpy_r_r402.f0);
    CPy_XDECREF(cpy_r_r402.f1);
    CPy_XDECREF(cpy_r_r402.f2);
CPyL201: ;
    cpy_r_r408 = CPy_KeepPropagating();
    if (!cpy_r_r408) goto CPyL206;
    CPy_Unreachable();
CPyL203: ;
    cpy_r_r409 = CPyDict_CheckSize(cpy_r_r133, cpy_r_r135);
    if (unlikely(!cpy_r_r409)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals);
        goto CPyL236;
    } else
        goto CPyL77;
CPyL204: ;
    cpy_r_r410 = CPy_NoErrOccurred();
    if (unlikely(!cpy_r_r410)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 134, CPyStatic_globals);
        goto CPyL206;
    }
    return 1;
CPyL206: ;
    cpy_r_r411 = 2;
    return cpy_r_r411;
CPyL207: ;
    CPy_XDECREF_NO_IMM(cpy_r_dot_sol_file);
    goto CPyL74;
CPyL208: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    goto CPyL206;
CPyL209: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    goto CPyL206;
CPyL210: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r15);
    goto CPyL206;
CPyL211: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r24);
    goto CPyL206;
CPyL212: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r31);
    goto CPyL206;
CPyL213: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r33);
    goto CPyL206;
CPyL214: ;
    CPy_DecRef(cpy_r_r38);
    goto CPyL19;
CPyL215: ;
    CPy_XDECREF_NO_IMM(cpy_r_dot_sol_file);
    goto CPyL18;
CPyL216: ;
    CPy_DecRef(cpy_r_r47);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r49);
    goto CPyL25;
CPyL217: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r33);
    CPy_DecRef(cpy_r_r45.f0);
    CPy_DecRef(cpy_r_r45.f1);
    CPy_DecRef(cpy_r_r45.f2);
    goto CPyL23;
CPyL218: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r33);
    goto CPyL26;
CPyL219: ;
    CPy_DECREF(cpy_r_r30);
    CPy_DECREF(cpy_r_r33);
    goto CPyL32;
CPyL220: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r30);
    goto CPyL35;
CPyL221: ;
    CPy_DECREF(cpy_r_r63);
    goto CPyL31;
CPyL222: ;
    CPy_XDECREF_NO_IMM(cpy_r_dot_sol_file);
    CPy_DECREF(cpy_r_r10);
    goto CPyL33;
CPyL223: ;
    CPy_XDECREF(cpy_r_r58.f0);
    CPy_XDECREF(cpy_r_r58.f1);
    CPy_XDECREF(cpy_r_r58.f2);
    goto CPyL34;
CPyL224: ;
    CPy_DECREF(cpy_r_r10);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    goto CPyL42;
CPyL225: ;
    CPy_DECREF(cpy_r_r10);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    goto CPyL46;
CPyL226: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r65);
    goto CPyL206;
CPyL227: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r77);
    goto CPyL206;
CPyL228: ;
    CPy_DECREF_NO_IMM(cpy_r_r81);
    goto CPyL58;
CPyL229: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r77);
    CPy_DecRef(cpy_r_r81);
    goto CPyL206;
CPyL230: ;
    CPy_DECREF_NO_IMM(cpy_r_r81);
    goto CPyL56;
CPyL231: ;
    CPy_DECREF(cpy_r_r77);
    goto CPyL69;
CPyL232: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r77);
    CPyTagged_DecRef(cpy_r_r107);
    goto CPyL206;
CPyL233: ;
    CPy_XDecRef(cpy_r_dot_sol_file);
    CPy_DecRef(cpy_r_r10);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r77);
    CPyTagged_DecRef(cpy_r_r112);
    goto CPyL206;
CPyL234: ;
    CPy_DecRef(cpy_r_r133);
    goto CPyL206;
CPyL235: ;
    CPy_DECREF(cpy_r_r133);
    CPy_DECREF(cpy_r_r136);
    CPy_DECREF(cpy_r_r137.f2);
    goto CPyL204;
CPyL236: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    goto CPyL206;
CPyL237: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    goto CPyL206;
CPyL238: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r144);
    goto CPyL206;
CPyL239: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r144);
    CPy_DecRef(cpy_r_r145);
    goto CPyL206;
CPyL240: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r145);
    goto CPyL206;
CPyL241: ;
    CPy_DECREF_NO_IMM(cpy_r_r153);
    goto CPyL92;
CPyL242: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r145);
    CPy_DecRef(cpy_r_r153);
    CPy_DecRef(cpy_r_i);
    goto CPyL206;
CPyL243: ;
    CPy_DECREF(cpy_r_i);
    goto CPyL91;
CPyL244: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r145);
    CPy_DecRef(cpy_r_r153);
    CPy_DecRef(cpy_r_r166);
    goto CPyL206;
CPyL245: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r145);
    CPy_DecRef(cpy_r_r153);
    goto CPyL206;
CPyL246: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r178);
    goto CPyL206;
CPyL247: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r178);
    CPy_DecRef(cpy_r_r183);
    goto CPyL206;
CPyL248: ;
    CPy_DECREF(cpy_r_r199);
    goto CPyL111;
CPyL249: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r193);
    goto CPyL109;
CPyL250: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r193);
    goto CPyL106;
CPyL251: ;
    CPy_DecRef(cpy_r_r200.f0);
    CPy_DecRef(cpy_r_r200.f1);
    CPy_DecRef(cpy_r_r200.f2);
    goto CPyL107;
CPyL252: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r193);
    goto CPyL206;
CPyL253: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r207);
    goto CPyL206;
CPyL254: ;
    CPy_DECREF(cpy_r_r213);
    goto CPyL114;
CPyL255: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r214);
    goto CPyL206;
CPyL256: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r221);
    CPy_DecRef(cpy_r_r222);
    goto CPyL206;
CPyL257: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r221);
    CPy_DecRef(cpy_r_r224);
    goto CPyL206;
CPyL258: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    goto CPyL183;
CPyL259: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r235);
    goto CPyL183;
CPyL260: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r246);
    goto CPyL183;
CPyL261: ;
    CPy_DECREF(cpy_r_r250);
    goto CPyL129;
CPyL262: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r257);
    goto CPyL183;
CPyL263: ;
    CPy_DECREF(cpy_r_r261);
    goto CPyL133;
CPyL264: ;
    CPy_DECREF(cpy_r_r141);
    CPy_DECREF(cpy_r_r214);
    CPy_DECREF(cpy_r_r229);
    CPy_DECREF_NO_IMM(cpy_r_r267);
    goto CPyL191;
CPyL265: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    goto CPyL183;
CPyL266: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    goto CPyL183;
CPyL267: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    CPy_DecRef(cpy_r_r278);
    goto CPyL183;
CPyL268: ;
    CPy_DECREF_NO_IMM(cpy_r_r286);
    goto CPyL152;
CPyL269: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    CPy_DecRef(cpy_r_r278);
    CPy_DecRef(cpy_r_r286);
    CPy_DecRef(cpy_r_i_2);
    goto CPyL183;
CPyL270: ;
    CPy_DECREF(cpy_r_i_2);
    goto CPyL151;
CPyL271: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    CPy_DecRef(cpy_r_r278);
    CPy_DecRef(cpy_r_r286);
    CPy_DecRef(cpy_r_r299);
    goto CPyL183;
CPyL272: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    CPy_DecRef(cpy_r_r278);
    CPy_DecRef(cpy_r_r286);
    goto CPyL183;
CPyL273: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r277);
    CPy_DecRef(cpy_r_r309);
    goto CPyL183;
CPyL274: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r310);
    goto CPyL183;
CPyL275: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r310);
    CPy_DecRef(cpy_r_contract_source);
    goto CPyL183;
CPyL276: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r310);
    CPy_DecRef(cpy_r_r321);
    goto CPyL183;
CPyL277: ;
    CPy_DECREF(cpy_r_r325);
    goto CPyL161;
CPyL278: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r310);
    CPy_DecRef(cpy_r_r331);
    goto CPyL183;
CPyL279: ;
    CPy_DECREF(cpy_r_r335);
    goto CPyL165;
CPyL280: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r310);
    CPy_DecRef(cpy_r_r341);
    goto CPyL183;
CPyL281: ;
    CPy_DECREF(cpy_r_r345);
    goto CPyL169;
CPyL282: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    goto CPyL183;
CPyL283: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r351);
    goto CPyL183;
CPyL284: ;
    CPy_DECREF(cpy_r_r355);
    goto CPyL173;
CPyL285: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r357);
    goto CPyL183;
CPyL286: ;
    CPy_DECREF(cpy_r_r361);
    goto CPyL175;
CPyL287: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r364);
    goto CPyL183;
CPyL288: ;
    CPy_DECREF(cpy_r_r368);
    goto CPyL177;
CPyL289: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r309);
    CPy_DecRef(cpy_r_r371);
    goto CPyL183;
CPyL290: ;
    CPy_DECREF(cpy_r_r375);
    goto CPyL179;
CPyL291: ;
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r214);
    CPy_DecRef(cpy_r_r229);
    CPy_DecRef(cpy_r_r267);
    CPy_DecRef(cpy_r_r378);
    goto CPyL183;
CPyL292: ;
    CPy_DECREF(cpy_r_r382);
    goto CPyL181;
CPyL293: ;
    CPy_DECREF(cpy_r_r387);
    goto CPyL182;
CPyL294: ;
    CPy_DecRef(cpy_r_r391);
    CPy_DecRef(cpy_r_r392);
    CPy_DecRef(cpy_r_r393);
    goto CPyL189;
CPyL295: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r221);
    CPy_DecRef(cpy_r_r224);
    CPy_DecRef(cpy_r_r389.f0);
    CPy_DecRef(cpy_r_r389.f1);
    CPy_DecRef(cpy_r_r389.f2);
    goto CPyL187;
CPyL296: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r221);
    CPy_DecRef(cpy_r_r224);
    goto CPyL190;
CPyL297: ;
    CPy_DECREF(cpy_r_r221);
    CPy_DECREF(cpy_r_r224);
    goto CPyL196;
CPyL298: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r221);
    goto CPyL199;
CPyL299: ;
    CPy_DECREF(cpy_r_r407);
    goto CPyL195;
CPyL300: ;
    CPy_DECREF(cpy_r_r133);
    CPy_DECREF(cpy_r_r136);
    goto CPyL197;
CPyL301: ;
    CPy_XDECREF(cpy_r_r402.f0);
    CPy_XDECREF(cpy_r_r402.f1);
    CPy_XDECREF(cpy_r_r402.f2);
    goto CPyL198;
}

PyObject *CPyPy_compile_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames) {
    static const char * const kwlist[] = {"file_list", 0};
    static CPyArg_Parser parser = {"O:compile_files", kwlist, 0};
    PyObject *obj_file_list;
    if (!CPyArg_ParseStackAndKeywordsOneArg(args, nargs, kwnames, &parser, &obj_file_list)) {
        return NULL;
    }
    PyObject *arg_file_list;
    if (likely(PyList_Check(obj_file_list)))
        arg_file_list = obj_file_list;
    else {
        CPy_TypeError("list", obj_file_list); 
        goto fail;
    }
    char retval = CPyDef_compile_files(arg_file_list);
    if (retval == 2) {
        return NULL;
    }
    PyObject *retbox = Py_None;
    CPy_INCREF(retbox);
    return retbox;
fail: ;
    CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "compile_files", 118, CPyStatic_globals);
    return NULL;
}

char CPyDef___top_level__(void) {
    PyObject *cpy_r_r0;
    PyObject *cpy_r_r1;
    char cpy_r_r2;
    PyObject *cpy_r_r3;
    PyObject *cpy_r_r4;
    PyObject **cpy_r_r5;
    PyObject **cpy_r_r6;
    PyObject **cpy_r_r7;
    void *cpy_r_r9;
    void *cpy_r_r11;
    PyObject *cpy_r_r12;
    PyObject *cpy_r_r13;
    PyObject *cpy_r_r14;
    PyObject *cpy_r_r15;
    char cpy_r_r16;
    PyObject *cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    PyObject **cpy_r_r21;
    void *cpy_r_r23;
    void *cpy_r_r25;
    PyObject *cpy_r_r26;
    PyObject *cpy_r_r27;
    PyObject *cpy_r_r28;
    PyObject *cpy_r_r29;
    char cpy_r_r30;
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    PyObject *cpy_r_r33;
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    int32_t cpy_r_r37;
    char cpy_r_r38;
    PyObject *cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject **cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject **cpy_r_r58;
    PyObject *cpy_r_r59;
    PyObject *cpy_r_r60;
    PyObject *cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    PyObject *cpy_r_r64;
    PyObject **cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject *cpy_r_r68;
    PyObject *cpy_r_r69;
    int32_t cpy_r_r70;
    char cpy_r_r71;
    PyObject *cpy_r_r72;
    PyObject *cpy_r_r73;
    PyObject *cpy_r_r74;
    PyObject *cpy_r_r75;
    PyObject **cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
    PyObject *cpy_r_r81;
    PyObject *cpy_r_r82;
    int32_t cpy_r_r83;
    char cpy_r_r84;
    PyObject *cpy_r_r85;
    PyObject *cpy_r_r86;
    PyObject *cpy_r_r87;
    PyObject *cpy_r_r88;
    PyObject *cpy_r_r89;
    PyObject *cpy_r_r90;
    PyObject *cpy_r_r91;
    int32_t cpy_r_r92;
    char cpy_r_r93;
    PyObject *cpy_r_r94;
    PyObject *cpy_r_r95;
    PyObject *cpy_r_r96;
    int32_t cpy_r_r97;
    char cpy_r_r98;
    char cpy_r_r99;
    PyObject *cpy_r_r100;
    PyObject *cpy_r_r101;
    PyObject *cpy_r_r102;
    PyObject *cpy_r_r103;
    PyObject *cpy_r_r104;
    PyObject *cpy_r_r105;
    PyObject *cpy_r_r106;
    PyObject *cpy_r_r107;
    PyObject *cpy_r_r108;
    int32_t cpy_r_r109;
    char cpy_r_r110;
    PyObject *cpy_r_r111;
    PyObject *cpy_r_r112;
    PyObject *cpy_r_r113;
    PyObject *cpy_r_r114;
    PyObject *cpy_r_r115;
    PyObject *cpy_r_r116;
    PyObject *cpy_r_r117;
    PyObject **cpy_r_r119;
    PyObject *cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    PyObject *cpy_r_r124;
    PyObject *cpy_r_r125;
    PyObject *cpy_r_r126;
    PyObject *cpy_r_r127;
    PyObject **cpy_r_r129;
    PyObject *cpy_r_r130;
    PyObject *cpy_r_r131;
    PyObject *cpy_r_r132;
    PyObject *cpy_r_r133;
    PyObject *cpy_r_r134;
    PyObject *cpy_r_r135;
    PyObject *cpy_r_r136;
    PyObject *cpy_r_r137;
    PyObject *cpy_r_r138;
    PyObject *cpy_r_r139;
    PyObject **cpy_r_r141;
    PyObject *cpy_r_r142;
    PyObject *cpy_r_r143;
    int64_t cpy_r_r144;
    CPyPtr cpy_r_r145;
    int64_t cpy_r_r146;
    char cpy_r_r147;
    CPyPtr cpy_r_r148;
    CPyPtr cpy_r_r149;
    int64_t cpy_r_r150;
    CPyPtr cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
    int32_t cpy_r_r155;
    char cpy_r_r156;
    int32_t cpy_r_r157;
    char cpy_r_r158;
    int64_t cpy_r_r159;
    PyObject *cpy_r_r160;
    PyObject *cpy_r_r161;
    int32_t cpy_r_r162;
    char cpy_r_r163;
    PyObject *cpy_r_r164;
    PyObject *cpy_r_r165;
    PyObject *cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject *cpy_r_r168;
    PyObject *cpy_r_r169;
    PyObject *cpy_r_r170;
    int32_t cpy_r_r171;
    char cpy_r_r172;
    PyObject *cpy_r_r173;
    PyObject *cpy_r_r174;
    PyObject *cpy_r_r175;
    int32_t cpy_r_r176;
    char cpy_r_r177;
    char cpy_r_r178;
    PyObject *cpy_r_r179;
    PyObject *cpy_r_r180;
    PyObject *cpy_r_r181;
    PyObject *cpy_r_r182;
    CPyPtr cpy_r_r183;
    CPyPtr cpy_r_r184;
    PyObject *cpy_r_r185;
    PyObject *cpy_r_r186;
    PyObject *cpy_r_r187;
    PyObject *cpy_r_r188;
    PyObject *cpy_r_r189;
    PyObject *cpy_r_r190;
    PyObject *cpy_r_r191;
    int32_t cpy_r_r192;
    char cpy_r_r193;
    PyObject *cpy_r_r194;
    PyObject *cpy_r_r195;
    PyObject *cpy_r_r196;
    int32_t cpy_r_r197;
    char cpy_r_r198;
    PyObject *cpy_r_r199;
    PyObject *cpy_r_r200;
    PyObject *cpy_r_r201;
    PyObject *cpy_r_r202;
    char cpy_r_r203;
    PyObject *cpy_r_r204;
    PyObject *cpy_r_r205;
    PyObject *cpy_r_r206;
    PyObject *cpy_r_r207;
    PyObject *cpy_r_r208;
    PyObject *cpy_r_r209;
    PyObject *cpy_r_r210;
    PyObject *cpy_r_r211;
    PyObject *cpy_r_r212;
    PyObject *cpy_r_r213;
    PyObject **cpy_r_r215;
    PyObject *cpy_r_r216;
    char cpy_r_r217;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[65]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL77;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = (PyObject **)&CPyModule_argparse;
    cpy_r_r6 = (PyObject **)&CPyModule_os;
    cpy_r_r7 = (PyObject **)&CPyModule_re;
    PyObject **cpy_r_r8[3] = {cpy_r_r5, cpy_r_r6, cpy_r_r7};
    cpy_r_r9 = (void *)&cpy_r_r8;
    int64_t cpy_r_r10[3] = {45, 46, 47};
    cpy_r_r11 = (void *)&cpy_r_r10;
    cpy_r_r12 = CPyStatics[105]; /* (('argparse', 'argparse', 'argparse'), ('os', 'os', 'os'),
                                    ('re', 're', 're')) */
    cpy_r_r13 = CPyStatic_globals;
    cpy_r_r14 = CPyStatics[69]; /* 'faster_web3/_utils/contract_sources/compile_contracts.py' */
    cpy_r_r15 = CPyStatics[70]; /* '<module>' */
    cpy_r_r16 = CPyImport_ImportMany(cpy_r_r12, cpy_r_r9, cpy_r_r13, cpy_r_r14, cpy_r_r15, cpy_r_r11);
    if (!cpy_r_r16) goto CPyL77;
    cpy_r_r17 = CPyStatics[106]; /* ('Any', 'Dict', 'List', 'Optional') */
    cpy_r_r18 = CPyStatics[75]; /* 'typing' */
    cpy_r_r19 = CPyStatic_globals;
    cpy_r_r20 = CPyImport_ImportFromMany(cpy_r_r18, cpy_r_r17, cpy_r_r17, cpy_r_r19);
    if (unlikely(cpy_r_r20 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 48, CPyStatic_globals);
        goto CPyL77;
    }
    CPyModule_typing = cpy_r_r20;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r20);
    cpy_r_r21 = (PyObject **)&CPyModule_solcx;
    PyObject **cpy_r_r22[1] = {cpy_r_r21};
    cpy_r_r23 = (void *)&cpy_r_r22;
    int64_t cpy_r_r24[1] = {55};
    cpy_r_r25 = (void *)&cpy_r_r24;
    cpy_r_r26 = CPyStatics[108]; /* (('solcx', 'solcx', 'solcx'),) */
    cpy_r_r27 = CPyStatic_globals;
    cpy_r_r28 = CPyStatics[69]; /* 'faster_web3/_utils/contract_sources/compile_contracts.py' */
    cpy_r_r29 = CPyStatics[70]; /* '<module>' */
    cpy_r_r30 = CPyImport_ImportMany(cpy_r_r26, cpy_r_r23, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r25);
    if (!cpy_r_r30) goto CPyL77;
    cpy_r_r31 = CPyModule_argparse;
    cpy_r_r32 = CPyStatics[76]; /* 'ArgumentParser' */
    cpy_r_r33 = CPyObject_GetAttr(cpy_r_r31, cpy_r_r32);
    if (unlikely(cpy_r_r33 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r34 = PyObject_Vectorcall(cpy_r_r33, 0, 0, 0);
    CPy_DECREF(cpy_r_r33);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r35 = CPyStatic_globals;
    cpy_r_r36 = CPyStatics[77]; /* 'arg_parser' */
    cpy_r_r37 = CPyDict_SetItem(cpy_r_r35, cpy_r_r36, cpy_r_r34);
    CPy_DECREF(cpy_r_r34);
    cpy_r_r38 = cpy_r_r37 >= 0;
    if (unlikely(!cpy_r_r38)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r39 = CPyStatic_globals;
    cpy_r_r40 = CPyStatics[77]; /* 'arg_parser' */
    cpy_r_r41 = CPyDict_GetItem(cpy_r_r39, cpy_r_r40);
    if (unlikely(cpy_r_r41 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 58, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r42 = CPyStatics[78]; /* '-v' */
    cpy_r_r43 = CPyStatics[79]; /* '--version' */
    cpy_r_r44 = CPyStatics[80]; /* 'Solidity version for compiling contracts.' */
    cpy_r_r45 = CPyStatics[81]; /* 'add_argument' */
    PyObject *cpy_r_r46[4] = {cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44};
    cpy_r_r47 = (PyObject **)&cpy_r_r46;
    cpy_r_r48 = CPyStatics[109]; /* ('help',) */
    cpy_r_r49 = PyObject_VectorcallMethod(cpy_r_r45, cpy_r_r47, 9223372036854775811ULL, cpy_r_r48);
    if (unlikely(cpy_r_r49 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 58, CPyStatic_globals);
        goto CPyL78;
    } else
        goto CPyL79;
CPyL11: ;
    CPy_DECREF(cpy_r_r41);
    cpy_r_r50 = CPyStatic_globals;
    cpy_r_r51 = CPyStatics[77]; /* 'arg_parser' */
    cpy_r_r52 = CPyDict_GetItem(cpy_r_r50, cpy_r_r51);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 61, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r53 = CPyStatics[83]; /* '-f' */
    cpy_r_r54 = CPyStatics[84]; /* '--filename' */
    cpy_r_r55 = CPyStatics[85]; /* ('(optional) The filename if only one file is to be '
                                   'compiled - otherwise all .sol files will be compiled at '
                                   'once.') */
    cpy_r_r56 = CPyStatics[81]; /* 'add_argument' */
    PyObject *cpy_r_r57[4] = {cpy_r_r52, cpy_r_r53, cpy_r_r54, cpy_r_r55};
    cpy_r_r58 = (PyObject **)&cpy_r_r57;
    cpy_r_r59 = CPyStatics[109]; /* ('help',) */
    cpy_r_r60 = PyObject_VectorcallMethod(cpy_r_r56, cpy_r_r58, 9223372036854775811ULL, cpy_r_r59);
    if (unlikely(cpy_r_r60 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 61, CPyStatic_globals);
        goto CPyL80;
    } else
        goto CPyL81;
CPyL13: ;
    CPy_DECREF(cpy_r_r52);
    cpy_r_r61 = CPyStatic_globals;
    cpy_r_r62 = CPyStatics[77]; /* 'arg_parser' */
    cpy_r_r63 = CPyDict_GetItem(cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 67, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r64 = CPyStatics[86]; /* 'parse_args' */
    PyObject *cpy_r_r65[1] = {cpy_r_r63};
    cpy_r_r66 = (PyObject **)&cpy_r_r65;
    cpy_r_r67 = PyObject_VectorcallMethod(cpy_r_r64, cpy_r_r66, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 67, CPyStatic_globals);
        goto CPyL82;
    }
    CPy_DECREF(cpy_r_r63);
    cpy_r_r68 = CPyStatic_globals;
    cpy_r_r69 = CPyStatics[87]; /* 'user_args' */
    cpy_r_r70 = CPyDict_SetItem(cpy_r_r68, cpy_r_r69, cpy_r_r67);
    CPy_DECREF(cpy_r_r67);
    cpy_r_r71 = cpy_r_r70 >= 0;
    if (unlikely(!cpy_r_r71)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 67, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r72 = CPyStatic_globals;
    cpy_r_r73 = CPyStatics[3]; /* 'solcx' */
    cpy_r_r74 = CPyDict_GetItem(cpy_r_r72, cpy_r_r73);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 69, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r75 = CPyStatics[88]; /* 'get_compilable_solc_versions' */
    PyObject *cpy_r_r76[1] = {cpy_r_r74};
    cpy_r_r77 = (PyObject **)&cpy_r_r76;
    cpy_r_r78 = PyObject_VectorcallMethod(cpy_r_r75, cpy_r_r77, 9223372036854775809ULL, 0);
    if (unlikely(cpy_r_r78 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 69, CPyStatic_globals);
        goto CPyL83;
    }
    CPy_DECREF(cpy_r_r74);
    cpy_r_r79 = CPySequence_Sort(cpy_r_r78);
    CPy_DECREF(cpy_r_r78);
    if (unlikely(cpy_r_r79 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 69, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r80 = CPyList_GetItemShort(cpy_r_r79, -2);
    CPy_DECREF_NO_IMM(cpy_r_r79);
    if (unlikely(cpy_r_r80 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 69, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r81 = CPyStatic_globals;
    cpy_r_r82 = CPyStatics[89]; /* 'LATEST_AVAILABLE_SOLIDITY_VERSION' */
    cpy_r_r83 = CPyDict_SetItem(cpy_r_r81, cpy_r_r82, cpy_r_r80);
    CPy_DECREF(cpy_r_r80);
    cpy_r_r84 = cpy_r_r83 >= 0;
    if (unlikely(!cpy_r_r84)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 69, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r85 = CPyStatic_globals;
    cpy_r_r86 = CPyStatics[87]; /* 'user_args' */
    cpy_r_r87 = CPyDict_GetItem(cpy_r_r85, cpy_r_r86);
    if (unlikely(cpy_r_r87 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 71, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r88 = CPyStatics[90]; /* 'version' */
    cpy_r_r89 = CPyObject_GetAttr(cpy_r_r87, cpy_r_r88);
    CPy_DECREF(cpy_r_r87);
    if (unlikely(cpy_r_r89 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 71, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r90 = CPyStatic_globals;
    cpy_r_r91 = CPyStatics[91]; /* 'user_sol_version' */
    cpy_r_r92 = CPyDict_SetItem(cpy_r_r90, cpy_r_r91, cpy_r_r89);
    CPy_DECREF(cpy_r_r89);
    cpy_r_r93 = cpy_r_r92 >= 0;
    if (unlikely(!cpy_r_r93)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 71, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r94 = CPyStatic_globals;
    cpy_r_r95 = CPyStatics[91]; /* 'user_sol_version' */
    cpy_r_r96 = CPyDict_GetItem(cpy_r_r94, cpy_r_r95);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 74, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r97 = PyObject_IsTrue(cpy_r_r96);
    CPy_DECREF(cpy_r_r96);
    cpy_r_r98 = cpy_r_r97 >= 0;
    if (unlikely(!cpy_r_r98)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 74, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r99 = cpy_r_r97;
    if (!cpy_r_r99) goto CPyL29;
    cpy_r_r100 = CPyStatic_globals;
    cpy_r_r101 = CPyStatics[91]; /* 'user_sol_version' */
    cpy_r_r102 = CPyDict_GetItem(cpy_r_r100, cpy_r_r101);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 74, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r103 = cpy_r_r102;
    goto CPyL31;
CPyL29: ;
    cpy_r_r104 = CPyStatic_globals;
    cpy_r_r105 = CPyStatics[89]; /* 'LATEST_AVAILABLE_SOLIDITY_VERSION' */
    cpy_r_r106 = CPyDict_GetItem(cpy_r_r104, cpy_r_r105);
    if (unlikely(cpy_r_r106 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 74, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r103 = cpy_r_r106;
CPyL31: ;
    cpy_r_r107 = CPyStatic_globals;
    cpy_r_r108 = CPyStatics[46]; /* 'solidity_version' */
    cpy_r_r109 = CPyDict_SetItem(cpy_r_r107, cpy_r_r108, cpy_r_r103);
    CPy_DECREF(cpy_r_r103);
    cpy_r_r110 = cpy_r_r109 >= 0;
    if (unlikely(!cpy_r_r110)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 74, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r111 = CPyStatic_globals;
    cpy_r_r112 = CPyStatics[3]; /* 'solcx' */
    cpy_r_r113 = CPyDict_GetItem(cpy_r_r111, cpy_r_r112);
    if (unlikely(cpy_r_r113 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r114 = CPyStatic_globals;
    cpy_r_r115 = CPyStatics[46]; /* 'solidity_version' */
    cpy_r_r116 = CPyDict_GetItem(cpy_r_r114, cpy_r_r115);
    if (unlikely(cpy_r_r116 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL84;
    }
    cpy_r_r117 = CPyStatics[92]; /* 'install_solc' */
    PyObject *cpy_r_r118[2] = {cpy_r_r113, cpy_r_r116};
    cpy_r_r119 = (PyObject **)&cpy_r_r118;
    cpy_r_r120 = PyObject_VectorcallMethod(cpy_r_r117, cpy_r_r119, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r120 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL85;
    } else
        goto CPyL86;
CPyL35: ;
    CPy_DECREF(cpy_r_r113);
    CPy_DECREF(cpy_r_r116);
    cpy_r_r121 = CPyStatic_globals;
    cpy_r_r122 = CPyStatics[3]; /* 'solcx' */
    cpy_r_r123 = CPyDict_GetItem(cpy_r_r121, cpy_r_r122);
    if (unlikely(cpy_r_r123 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 77, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r124 = CPyStatic_globals;
    cpy_r_r125 = CPyStatics[46]; /* 'solidity_version' */
    cpy_r_r126 = CPyDict_GetItem(cpy_r_r124, cpy_r_r125);
    if (unlikely(cpy_r_r126 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 77, CPyStatic_globals);
        goto CPyL87;
    }
    cpy_r_r127 = CPyStatics[93]; /* 'set_solc_version' */
    PyObject *cpy_r_r128[2] = {cpy_r_r123, cpy_r_r126};
    cpy_r_r129 = (PyObject **)&cpy_r_r128;
    cpy_r_r130 = PyObject_VectorcallMethod(cpy_r_r127, cpy_r_r129, 9223372036854775810ULL, 0);
    if (unlikely(cpy_r_r130 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 77, CPyStatic_globals);
        goto CPyL88;
    } else
        goto CPyL89;
CPyL38: ;
    CPy_DECREF(cpy_r_r123);
    CPy_DECREF(cpy_r_r126);
    cpy_r_r131 = PyList_New(0);
    if (unlikely(cpy_r_r131 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r132 = CPyModule_os;
    cpy_r_r133 = CPyStatics[16]; /* 'getcwd' */
    cpy_r_r134 = CPyObject_GetAttr(cpy_r_r132, cpy_r_r133);
    if (unlikely(cpy_r_r134 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL90;
    }
    cpy_r_r135 = PyObject_Vectorcall(cpy_r_r134, 0, 0, 0);
    CPy_DECREF(cpy_r_r134);
    if (unlikely(cpy_r_r135 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL90;
    }
    if (likely(PyUnicode_Check(cpy_r_r135)))
        cpy_r_r136 = cpy_r_r135;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals, "str", cpy_r_r135);
        goto CPyL90;
    }
    cpy_r_r137 = CPyModule_os;
    cpy_r_r138 = CPyStatics[94]; /* 'listdir' */
    cpy_r_r139 = CPyObject_GetAttr(cpy_r_r137, cpy_r_r138);
    if (unlikely(cpy_r_r139 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL91;
    }
    PyObject *cpy_r_r140[1] = {cpy_r_r136};
    cpy_r_r141 = (PyObject **)&cpy_r_r140;
    cpy_r_r142 = PyObject_Vectorcall(cpy_r_r139, cpy_r_r141, 1, 0);
    CPy_DECREF(cpy_r_r139);
    if (unlikely(cpy_r_r142 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL91;
    }
    CPy_DECREF(cpy_r_r136);
    if (likely(PyList_Check(cpy_r_r142)))
        cpy_r_r143 = cpy_r_r142;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals, "list", cpy_r_r142);
        goto CPyL90;
    }
    cpy_r_r144 = 0;
CPyL46: ;
    cpy_r_r145 = (CPyPtr)&((PyVarObject *)cpy_r_r143)->ob_size;
    cpy_r_r146 = *(int64_t *)cpy_r_r145;
    cpy_r_r147 = cpy_r_r144 < cpy_r_r146;
    if (!cpy_r_r147) goto CPyL92;
    cpy_r_r148 = (CPyPtr)&((PyListObject *)cpy_r_r143)->ob_item;
    cpy_r_r149 = *(CPyPtr *)cpy_r_r148;
    cpy_r_r150 = cpy_r_r144 * 8;
    cpy_r_r151 = cpy_r_r149 + cpy_r_r150;
    cpy_r_r152 = *(PyObject * *)cpy_r_r151;
    CPy_INCREF(cpy_r_r152);
    if (likely(PyUnicode_Check(cpy_r_r152)))
        cpy_r_r153 = cpy_r_r152;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals, "str", cpy_r_r152);
        goto CPyL93;
    }
    cpy_r_r154 = CPyStatics[10]; /* '.sol' */
    cpy_r_r155 = CPyStr_Endswith(cpy_r_r153, cpy_r_r154);
    cpy_r_r156 = cpy_r_r155;
    if (!cpy_r_r156) goto CPyL94;
    cpy_r_r157 = PyList_Append(cpy_r_r131, cpy_r_r153);
    CPy_DECREF(cpy_r_r153);
    cpy_r_r158 = cpy_r_r157 >= 0;
    if (unlikely(!cpy_r_r158)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL93;
    }
CPyL50: ;
    cpy_r_r159 = cpy_r_r144 + 1;
    cpy_r_r144 = cpy_r_r159;
    goto CPyL46;
CPyL51: ;
    cpy_r_r160 = CPyStatic_globals;
    cpy_r_r161 = CPyStatics[95]; /* 'all_dot_sol_files' */
    cpy_r_r162 = CPyDict_SetItem(cpy_r_r160, cpy_r_r161, cpy_r_r131);
    CPy_DECREF_NO_IMM(cpy_r_r131);
    cpy_r_r163 = cpy_r_r162 >= 0;
    if (unlikely(!cpy_r_r163)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r164 = CPyStatic_globals;
    cpy_r_r165 = CPyStatics[87]; /* 'user_args' */
    cpy_r_r166 = CPyDict_GetItem(cpy_r_r164, cpy_r_r165);
    if (unlikely(cpy_r_r166 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 82, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r167 = CPyStatics[96]; /* 'filename' */
    cpy_r_r168 = CPyObject_GetAttr(cpy_r_r166, cpy_r_r167);
    CPy_DECREF(cpy_r_r166);
    if (unlikely(cpy_r_r168 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 82, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r169 = CPyStatic_globals;
    cpy_r_r170 = CPyStatics[97]; /* 'user_filename' */
    cpy_r_r171 = CPyDict_SetItem(cpy_r_r169, cpy_r_r170, cpy_r_r168);
    CPy_DECREF(cpy_r_r168);
    cpy_r_r172 = cpy_r_r171 >= 0;
    if (unlikely(!cpy_r_r172)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 82, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r173 = CPyStatic_globals;
    cpy_r_r174 = CPyStatics[97]; /* 'user_filename' */
    cpy_r_r175 = CPyDict_GetItem(cpy_r_r173, cpy_r_r174);
    if (unlikely(cpy_r_r175 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r176 = PyObject_IsTrue(cpy_r_r175);
    CPy_DECREF(cpy_r_r175);
    cpy_r_r177 = cpy_r_r176 >= 0;
    if (unlikely(!cpy_r_r177)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r178 = cpy_r_r176;
    if (!cpy_r_r178) goto CPyL61;
    cpy_r_r179 = CPyStatic_globals;
    cpy_r_r180 = CPyStatics[97]; /* 'user_filename' */
    cpy_r_r181 = CPyDict_GetItem(cpy_r_r179, cpy_r_r180);
    if (unlikely(cpy_r_r181 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r182 = PyList_New(1);
    if (unlikely(cpy_r_r182 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL95;
    }
    cpy_r_r183 = (CPyPtr)&((PyListObject *)cpy_r_r182)->ob_item;
    cpy_r_r184 = *(CPyPtr *)cpy_r_r183;
    *(PyObject * *)cpy_r_r184 = cpy_r_r181;
    cpy_r_r185 = cpy_r_r182;
    goto CPyL64;
CPyL61: ;
    cpy_r_r186 = CPyStatic_globals;
    cpy_r_r187 = CPyStatics[95]; /* 'all_dot_sol_files' */
    cpy_r_r188 = CPyDict_GetItem(cpy_r_r186, cpy_r_r187);
    if (unlikely(cpy_r_r188 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL77;
    }
    if (likely(PyList_Check(cpy_r_r188)))
        cpy_r_r189 = cpy_r_r188;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals, "list", cpy_r_r188);
        goto CPyL77;
    }
    cpy_r_r185 = cpy_r_r189;
CPyL64: ;
    cpy_r_r190 = CPyStatic_globals;
    cpy_r_r191 = CPyStatics[98]; /* 'files_to_compile' */
    cpy_r_r192 = CPyDict_SetItem(cpy_r_r190, cpy_r_r191, cpy_r_r185);
    CPy_DECREF_NO_IMM(cpy_r_r185);
    cpy_r_r193 = cpy_r_r192 >= 0;
    if (unlikely(!cpy_r_r193)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 83, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r194 = PyDict_New();
    if (unlikely(cpy_r_r194 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 115, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r195 = CPyStatic_globals;
    cpy_r_r196 = CPyStatics[28]; /* 'contracts_in_file' */
    cpy_r_r197 = CPyDict_SetItem(cpy_r_r195, cpy_r_r196, cpy_r_r194);
    CPy_DECREF(cpy_r_r194);
    cpy_r_r198 = cpy_r_r197 >= 0;
    if (unlikely(!cpy_r_r198)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 115, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r199 = CPyStatic_globals;
    cpy_r_r200 = CPyStatics[98]; /* 'files_to_compile' */
    cpy_r_r201 = CPyDict_GetItem(cpy_r_r199, cpy_r_r200);
    if (unlikely(cpy_r_r201 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 183, CPyStatic_globals);
        goto CPyL77;
    }
    if (likely(PyList_Check(cpy_r_r201)))
        cpy_r_r202 = cpy_r_r201;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 183, CPyStatic_globals, "list", cpy_r_r201);
        goto CPyL77;
    }
    cpy_r_r203 = CPyDef_compile_files(cpy_r_r202);
    CPy_DECREF_NO_IMM(cpy_r_r202);
    if (unlikely(cpy_r_r203 == 2)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 183, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r204 = CPyStatics[99]; /* 'black ' */
    cpy_r_r205 = CPyModule_os;
    cpy_r_r206 = CPyStatics[16]; /* 'getcwd' */
    cpy_r_r207 = CPyObject_GetAttr(cpy_r_r205, cpy_r_r206);
    if (unlikely(cpy_r_r207 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r208 = PyObject_Vectorcall(cpy_r_r207, 0, 0, 0);
    CPy_DECREF(cpy_r_r207);
    if (unlikely(cpy_r_r208 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals);
        goto CPyL77;
    }
    if (likely(PyUnicode_Check(cpy_r_r208)))
        cpy_r_r209 = cpy_r_r208;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals, "str", cpy_r_r208);
        goto CPyL77;
    }
    cpy_r_r210 = CPyStr_Build(2, cpy_r_r204, cpy_r_r209);
    CPy_DECREF(cpy_r_r209);
    if (unlikely(cpy_r_r210 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r211 = CPyModule_os;
    cpy_r_r212 = CPyStatics[100]; /* 'system' */
    cpy_r_r213 = CPyObject_GetAttr(cpy_r_r211, cpy_r_r212);
    if (unlikely(cpy_r_r213 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals);
        goto CPyL96;
    }
    PyObject *cpy_r_r214[1] = {cpy_r_r210};
    cpy_r_r215 = (PyObject **)&cpy_r_r214;
    cpy_r_r216 = PyObject_Vectorcall(cpy_r_r213, cpy_r_r215, 1, 0);
    CPy_DECREF(cpy_r_r213);
    if (unlikely(cpy_r_r216 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/compile_contracts.py", "<module>", 184, CPyStatic_globals);
        goto CPyL96;
    } else
        goto CPyL97;
CPyL76: ;
    CPy_DECREF(cpy_r_r210);
    return 1;
CPyL77: ;
    cpy_r_r217 = 2;
    return cpy_r_r217;
CPyL78: ;
    CPy_DecRef(cpy_r_r41);
    goto CPyL77;
CPyL79: ;
    CPy_DECREF(cpy_r_r49);
    goto CPyL11;
CPyL80: ;
    CPy_DecRef(cpy_r_r52);
    goto CPyL77;
CPyL81: ;
    CPy_DECREF(cpy_r_r60);
    goto CPyL13;
CPyL82: ;
    CPy_DecRef(cpy_r_r63);
    goto CPyL77;
CPyL83: ;
    CPy_DecRef(cpy_r_r74);
    goto CPyL77;
CPyL84: ;
    CPy_DecRef(cpy_r_r113);
    goto CPyL77;
CPyL85: ;
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r116);
    goto CPyL77;
CPyL86: ;
    CPy_DECREF(cpy_r_r120);
    goto CPyL35;
CPyL87: ;
    CPy_DecRef(cpy_r_r123);
    goto CPyL77;
CPyL88: ;
    CPy_DecRef(cpy_r_r123);
    CPy_DecRef(cpy_r_r126);
    goto CPyL77;
CPyL89: ;
    CPy_DECREF(cpy_r_r130);
    goto CPyL38;
CPyL90: ;
    CPy_DecRef(cpy_r_r131);
    goto CPyL77;
CPyL91: ;
    CPy_DecRef(cpy_r_r131);
    CPy_DecRef(cpy_r_r136);
    goto CPyL77;
CPyL92: ;
    CPy_DECREF_NO_IMM(cpy_r_r143);
    goto CPyL51;
CPyL93: ;
    CPy_DecRef(cpy_r_r131);
    CPy_DecRef(cpy_r_r143);
    goto CPyL77;
CPyL94: ;
    CPy_DECREF(cpy_r_r153);
    goto CPyL50;
CPyL95: ;
    CPy_DecRef(cpy_r_r181);
    goto CPyL77;
CPyL96: ;
    CPy_DecRef(cpy_r_r210);
    goto CPyL77;
CPyL97: ;
    CPy_DECREF(cpy_r_r216);
    goto CPyL76;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___compile_contracts = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_argparse = Py_None;
    CPyModule_os = Py_None;
    CPyModule_re = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_solcx = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[110];
const char * const CPyLit_Str[] = {
    "\n\005solcx\002./\003abi\003bin\vbin-runtime\rcompile_files\routput_values\004.sol\000\001:",
    "\005+Could not find compiled data for contract: \tException\0020x\006getcwd\004path",
    "\t\004join\004open\b__exit__\t__enter__\treadlines\bcontract\001{\babstract\tcontract ",
    "\b\001 \021contracts_in_file\r([A-Z][a-z]*)\005split\005lower\001_\003.py\rcontract_data",
    "\006\006remove\021FileNotFoundError\ncompiling \005print\001w\022\"\"\"\nGenerated by `",
    "\005\b__file__\bbasename\n` script.\n\005write\030Compiled with Solidity v",
    "\004\020solidity_version\a.\n\"\"\"\n\n\023([A-Z0-9][a-z0-9]*)\005upper",
    "\003\'# source: web3/_utils/contract_sources/\016  # noqa: E501\001\n",
    "\005\r_BYTECODE = \"\020\"  # noqa: E501\n\f_RUNTIME = \"\a_ABI = \n_DATA = {\n",
    "\004\020    \"bytecode\": \v_BYTECODE,\n\030    \"bytecode_runtime\": \n_RUNTIME,\n",
    "\a\v    \"abi\": \006_ABI,\n\004}\n\n\n\bbuiltins\bargparse\002os\002re",
    "\0038faster_web3/_utils/contract_sources/compile_contracts.py\b<module>\003Any",
    "\b\004Dict\004List\bOptional\006typing\016ArgumentParser\narg_parser\002-v\t--version",
    "\004)Solidity version for compiling contracts.\fadd_argument\004help\002-f",
    "\001\n--filename",
    "\001o(optional) The filename if only one file is to be compiled - otherwise all .sol files will be compiled at once.",
    "\003\nparse_args\tuser_args\034get_compilable_solc_versions",
    "\003!LATEST_AVAILABLE_SOLIDITY_VERSION\aversion\020user_sol_version",
    "\005\finstall_solc\020set_solc_version\alistdir\021all_dot_sol_files\bfilename",
    "\004\ruser_filename\020files_to_compile\006black \006system",
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
    9, 1, 9, 3, 66, 66, 66, 3, 67, 67, 67, 3, 68, 68, 68, 3, 102, 103,
    104, 4, 71, 72, 73, 74, 3, 3, 3, 3, 1, 107, 1, 82
};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___compile_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
CPyModule *CPyModule_argparse;
CPyModule *CPyModule_os;
CPyModule *CPyModule_re;
CPyModule *CPyModule_typing;
CPyModule *CPyModule_solcx;
PyObject *CPyDef__compile_dot_sol_files(PyObject *cpy_r_dot_sol_filename);
PyObject *CPyPy__compile_dot_sol_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
PyObject *CPyDef__get_compiled_contract_data(PyObject *cpy_r_sol_file_output, PyObject *cpy_r_dot_sol_filename, PyObject *cpy_r_contract_name);
PyObject *CPyPy__get_compiled_contract_data(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef_compile_files(PyObject *cpy_r_file_list);
PyObject *CPyPy_compile_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
char CPyDef___top_level__(void);

static int exec_compile_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___compile_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___compile_contracts, "faster_web3._utils.contract_sources.compile_contracts__mypyc.init_faster_web3____utils___contract_sources___compile_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___compile_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_compile_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.compile_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_compile_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_compile_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_compile_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
