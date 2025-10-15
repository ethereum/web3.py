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
#include "__native__custom_contract_data.h"
#include "__native_internal__custom_contract_data.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data____custom_contract_data(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data._custom_contract_data",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data____custom_contract_data(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data____custom_contract_data(CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal;
    fail:
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
    PyObject *cpy_r_r34;
    PyObject *cpy_r_r35;
    PyObject *cpy_r_r36;
    PyObject *cpy_r_r37;
    PyObject *cpy_r_r38;
    PyObject *cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    PyObject *cpy_r_r47;
    int32_t cpy_r_r48;
    char cpy_r_r49;
    char cpy_r_r50;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/_custom_contract_data.py", "<module>", -1, CPyStatic_globals);
        goto CPyL6;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* 'LogAnonymous' */
    cpy_r_r6 = CPyStatics[5]; /* 'LogNoArguments' */
    cpy_r_r7 = CPyStatics[6]; /* 'LogSingleArg' */
    cpy_r_r8 = CPyStatics[7]; /* 'LogDoubleArg' */
    cpy_r_r9 = CPyStatics[8]; /* 'LogTripleArg' */
    cpy_r_r10 = CPyStatics[9]; /* 'LogQuadrupleArg' */
    cpy_r_r11 = CPyStatics[10]; /* 'LogSingleAnonymous' */
    cpy_r_r12 = CPyStatics[11]; /* 'LogSingleWithIndex' */
    cpy_r_r13 = CPyStatics[12]; /* 'LogDoubleAnonymous' */
    cpy_r_r14 = CPyStatics[13]; /* 'LogDoubleWithIndex' */
    cpy_r_r15 = CPyStatics[14]; /* 'LogTripleWithIndex' */
    cpy_r_r16 = CPyStatics[15]; /* 'LogQuadrupleWithIndex' */
    cpy_r_r17 = CPyStatics[16]; /* 'LogBytes' */
    cpy_r_r18 = CPyStatics[17]; /* 'LogString' */
    cpy_r_r19 = CPyStatics[18]; /* 'LogDynamicArgs' */
    cpy_r_r20 = CPyStatics[19]; /* 'LogListArgs' */
    cpy_r_r21 = CPyStatics[20]; /* 'LogAddressIndexed' */
    cpy_r_r22 = CPyStatics[21]; /* 'LogAddressNotIndexed' */
    cpy_r_r23 = CPyStatics[22]; /* 'LogStructArgs' */
    cpy_r_r24 = CPyStatics[23]; /* 'LogIndexedAndNotIndexed' */
    cpy_r_r25 = CPyStatics[25]; /* 0 */
    cpy_r_r26 = CPyStatics[26]; /* 1 */
    cpy_r_r27 = CPyStatics[27]; /* 2 */
    cpy_r_r28 = CPyStatics[28]; /* 3 */
    cpy_r_r29 = CPyStatics[29]; /* 4 */
    cpy_r_r30 = CPyStatics[30]; /* 5 */
    cpy_r_r31 = CPyStatics[31]; /* 6 */
    cpy_r_r32 = CPyStatics[32]; /* 7 */
    cpy_r_r33 = CPyStatics[33]; /* 8 */
    cpy_r_r34 = CPyStatics[34]; /* 9 */
    cpy_r_r35 = CPyStatics[35]; /* 10 */
    cpy_r_r36 = CPyStatics[36]; /* 11 */
    cpy_r_r37 = CPyStatics[37]; /* 12 */
    cpy_r_r38 = CPyStatics[38]; /* 13 */
    cpy_r_r39 = CPyStatics[39]; /* 14 */
    cpy_r_r40 = CPyStatics[40]; /* 15 */
    cpy_r_r41 = CPyStatics[41]; /* 16 */
    cpy_r_r42 = CPyStatics[42]; /* 17 */
    cpy_r_r43 = CPyStatics[43]; /* 18 */
    cpy_r_r44 = CPyStatics[44]; /* 19 */
    cpy_r_r45 = CPyDict_Build(20, cpy_r_r5, cpy_r_r25, cpy_r_r6, cpy_r_r26, cpy_r_r7, cpy_r_r27, cpy_r_r8, cpy_r_r28, cpy_r_r9, cpy_r_r29, cpy_r_r10, cpy_r_r30, cpy_r_r11, cpy_r_r31, cpy_r_r12, cpy_r_r32, cpy_r_r13, cpy_r_r33, cpy_r_r14, cpy_r_r34, cpy_r_r15, cpy_r_r35, cpy_r_r16, cpy_r_r36, cpy_r_r17, cpy_r_r37, cpy_r_r18, cpy_r_r38, cpy_r_r19, cpy_r_r39, cpy_r_r20, cpy_r_r40, cpy_r_r21, cpy_r_r41, cpy_r_r22, cpy_r_r42, cpy_r_r23, cpy_r_r43, cpy_r_r24, cpy_r_r44);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/_custom_contract_data.py", "<module>", 1, CPyStatic_globals);
        goto CPyL6;
    }
    cpy_r_r46 = CPyStatic_globals;
    cpy_r_r47 = CPyStatics[24]; /* 'EMITTER_ENUM' */
    cpy_r_r48 = CPyDict_SetItem(cpy_r_r46, cpy_r_r47, cpy_r_r45);
    CPy_DECREF(cpy_r_r45);
    cpy_r_r49 = cpy_r_r48 >= 0;
    if (unlikely(!cpy_r_r49)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/_custom_contract_data.py", "<module>", 1, CPyStatic_globals);
        goto CPyL6;
    }
    return 1;
CPyL6: ;
    cpy_r_r50 = 2;
    return cpy_r_r50;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[45];
const char * const CPyLit_Str[] = {
    "\005\bbuiltins\fLogAnonymous\016LogNoArguments\fLogSingleArg\fLogDoubleArg",
    "\004\fLogTripleArg\017LogQuadrupleArg\022LogSingleAnonymous\022LogSingleWithIndex",
    "\003\022LogDoubleAnonymous\022LogDoubleWithIndex\022LogTripleWithIndex",
    "\005\025LogQuadrupleWithIndex\bLogBytes\tLogString\016LogDynamicArgs\vLogListArgs",
    "\003\021LogAddressIndexed\024LogAddressNotIndexed\rLogStructArgs",
    "\002\027LogIndexedAndNotIndexed\fEMITTER_ENUM",
    "",
};
const char * const CPyLit_Bytes[] = {
    "",
};
const char * const CPyLit_Int[] = {
    "\0240\0001\0002\0003\0004\0005\0006\0007\0008\0009\00010\00011\00012\00013\00014\00015\00016\00017\00018\00019",
    "",
};
const double CPyLit_Float[] = {0};
const double CPyLit_Complex[] = {0};
const int CPyLit_Tuple[] = {0};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data____custom_contract_data;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec__custom_contract_data__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data____custom_contract_data(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data____custom_contract_data, "faster_web3._utils.contract_sources.contract_data._custom_contract_data__mypyc.init_faster_web3____utils___contract_sources___contract_data____custom_contract_data", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data____custom_contract_data", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def__custom_contract_data__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data._custom_contract_data__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit__custom_contract_data__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def__custom_contract_data__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec__custom_contract_data__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
