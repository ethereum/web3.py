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
#include "__native_payable_tester.h"
#include "__native_internal_payable_tester.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___payable_tester(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.payable_tester",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___payable_tester(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___payable_tester(CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal;
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
    int32_t cpy_r_r8;
    char cpy_r_r9;
    PyObject *cpy_r_r10;
    PyObject *cpy_r_r11;
    PyObject *cpy_r_r12;
    int32_t cpy_r_r13;
    char cpy_r_r14;
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
    CPyPtr cpy_r_r39;
    CPyPtr cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    CPyPtr cpy_r_r47;
    CPyPtr cpy_r_r48;
    CPyPtr cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    int32_t cpy_r_r52;
    char cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    PyObject *cpy_r_r57;
    PyObject *cpy_r_r58;
    PyObject *cpy_r_r59;
    PyObject *cpy_r_r60;
    PyObject *cpy_r_r61;
    PyObject *cpy_r_r62;
    PyObject *cpy_r_r63;
    PyObject *cpy_r_r64;
    PyObject *cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject *cpy_r_r68;
    PyObject *cpy_r_r69;
    PyObject *cpy_r_r70;
    PyObject *cpy_r_r71;
    int32_t cpy_r_r72;
    char cpy_r_r73;
    char cpy_r_r74;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", -1, CPyStatic_globals);
        goto CPyL23;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5060e78061001b5f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063c6803622146034578063e4cb8f5c14604e575b5f5ffd5b603a6056565b60405160459190609a565b60405180910390f35b60546067565b005b5f5f9054906101000a900460ff1681565b60015f5f6101000a81548160ff021916908315150217905550565b5f8115159050919050565b6094816082565b82525050565b5f60208201905060ab5f830184608d565b9291505056fea2646970667358221220a9b00e8591f184642b3b3dfbbe6465e7a6ad284ba74537a9e2445f737666c8a364736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'PAYABLE_TESTER_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 7, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063c6803622146034578063e4cb8f5c14604e575b5f5ffd5b603a6056565b60405160459190609a565b60405180910390f35b60546067565b005b5f5f9054906101000a900460ff1681565b60015f5f6101000a81548160ff021916908315150217905550565b5f8115159050919050565b6094816082565b82525050565b5f60208201905060ab5f830184608d565b9291505056fea2646970667358221220a9b00e8591f184642b3b3dfbbe6465e7a6ad284ba74537a9e2445f737666c8a364736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'PAYABLE_TESTER_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 8, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 11, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'name' */
    cpy_r_r18 = CPyStatics[10]; /* 'doNoValueCall' */
    cpy_r_r19 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r20 = PyList_New(0);
    if (unlikely(cpy_r_r20 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 13, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r21 = CPyStatics[12]; /* 'stateMutability' */
    cpy_r_r22 = CPyStatics[13]; /* 'nonpayable' */
    cpy_r_r23 = CPyStatics[14]; /* 'type' */
    cpy_r_r24 = CPyStatics[15]; /* 'function' */
    cpy_r_r25 = CPyDict_Build(5, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23, cpy_r_r24);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    CPy_DECREF_NO_IMM(cpy_r_r20);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 10, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r26 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r27 = PyList_New(0);
    if (unlikely(cpy_r_r27 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 18, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r28 = CPyStatics[9]; /* 'name' */
    cpy_r_r29 = CPyStatics[16]; /* 'wasCalled' */
    cpy_r_r30 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r31 = CPyStatics[17]; /* 'internalType' */
    cpy_r_r32 = CPyStatics[18]; /* 'bool' */
    cpy_r_r33 = CPyStatics[9]; /* 'name' */
    cpy_r_r34 = CPyStatics[19]; /* '' */
    cpy_r_r35 = CPyStatics[14]; /* 'type' */
    cpy_r_r36 = CPyStatics[18]; /* 'bool' */
    cpy_r_r37 = CPyDict_Build(3, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34, cpy_r_r35, cpy_r_r36);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 20, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r38 = PyList_New(1);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 20, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r39 = (CPyPtr)&((PyListObject *)cpy_r_r38)->ob_item;
    cpy_r_r40 = *(CPyPtr *)cpy_r_r39;
    *(PyObject * *)cpy_r_r40 = cpy_r_r37;
    cpy_r_r41 = CPyStatics[12]; /* 'stateMutability' */
    cpy_r_r42 = CPyStatics[20]; /* 'view' */
    cpy_r_r43 = CPyStatics[14]; /* 'type' */
    cpy_r_r44 = CPyStatics[15]; /* 'function' */
    cpy_r_r45 = CPyDict_Build(5, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r30, cpy_r_r38, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44);
    CPy_DECREF_NO_IMM(cpy_r_r27);
    CPy_DECREF_NO_IMM(cpy_r_r38);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 17, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r46 = PyList_New(2);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 9, CPyStatic_globals);
        goto CPyL28;
    }
    cpy_r_r47 = (CPyPtr)&((PyListObject *)cpy_r_r46)->ob_item;
    cpy_r_r48 = *(CPyPtr *)cpy_r_r47;
    *(PyObject * *)cpy_r_r48 = cpy_r_r25;
    cpy_r_r49 = cpy_r_r48 + 8;
    *(PyObject * *)cpy_r_r49 = cpy_r_r45;
    cpy_r_r50 = CPyStatic_globals;
    cpy_r_r51 = CPyStatics[21]; /* 'PAYABLE_TESTER_CONTRACT_ABI' */
    cpy_r_r52 = CPyDict_SetItem(cpy_r_r50, cpy_r_r51, cpy_r_r46);
    CPy_DECREF_NO_IMM(cpy_r_r46);
    cpy_r_r53 = cpy_r_r52 >= 0;
    if (unlikely(!cpy_r_r53)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 9, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r54 = CPyStatics[22]; /* 'bytecode' */
    cpy_r_r55 = CPyStatic_globals;
    cpy_r_r56 = CPyStatics[5]; /* 'PAYABLE_TESTER_CONTRACT_BYTECODE' */
    cpy_r_r57 = CPyDict_GetItem(cpy_r_r55, cpy_r_r56);
    if (unlikely(cpy_r_r57 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 26, CPyStatic_globals);
        goto CPyL23;
    }
    if (likely(PyUnicode_Check(cpy_r_r57)))
        cpy_r_r58 = cpy_r_r57;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 26, CPyStatic_globals, "str", cpy_r_r57);
        goto CPyL23;
    }
    cpy_r_r59 = CPyStatics[23]; /* 'bytecode_runtime' */
    cpy_r_r60 = CPyStatic_globals;
    cpy_r_r61 = CPyStatics[7]; /* 'PAYABLE_TESTER_CONTRACT_RUNTIME' */
    cpy_r_r62 = CPyDict_GetItem(cpy_r_r60, cpy_r_r61);
    if (unlikely(cpy_r_r62 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 27, CPyStatic_globals);
        goto CPyL29;
    }
    if (likely(PyUnicode_Check(cpy_r_r62)))
        cpy_r_r63 = cpy_r_r62;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 27, CPyStatic_globals, "str", cpy_r_r62);
        goto CPyL29;
    }
    cpy_r_r64 = CPyStatics[24]; /* 'abi' */
    cpy_r_r65 = CPyStatic_globals;
    cpy_r_r66 = CPyStatics[21]; /* 'PAYABLE_TESTER_CONTRACT_ABI' */
    cpy_r_r67 = CPyDict_GetItem(cpy_r_r65, cpy_r_r66);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 28, CPyStatic_globals);
        goto CPyL30;
    }
    if (likely(PyList_Check(cpy_r_r67)))
        cpy_r_r68 = cpy_r_r67;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 28, CPyStatic_globals, "list", cpy_r_r67);
        goto CPyL30;
    }
    cpy_r_r69 = CPyDict_Build(3, cpy_r_r54, cpy_r_r58, cpy_r_r59, cpy_r_r63, cpy_r_r64, cpy_r_r68);
    CPy_DECREF(cpy_r_r58);
    CPy_DECREF(cpy_r_r63);
    CPy_DECREF_NO_IMM(cpy_r_r68);
    if (unlikely(cpy_r_r69 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 25, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r70 = CPyStatic_globals;
    cpy_r_r71 = CPyStatics[25]; /* 'PAYABLE_TESTER_CONTRACT_DATA' */
    cpy_r_r72 = CPyDict_SetItem(cpy_r_r70, cpy_r_r71, cpy_r_r69);
    CPy_DECREF(cpy_r_r69);
    cpy_r_r73 = cpy_r_r72 >= 0;
    if (unlikely(!cpy_r_r73)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/payable_tester.py", "<module>", 25, CPyStatic_globals);
        goto CPyL23;
    }
    return 1;
CPyL23: ;
    cpy_r_r74 = 2;
    return cpy_r_r74;
CPyL24: ;
    CPy_DecRef(cpy_r_r16);
    goto CPyL23;
CPyL25: ;
    CPy_DecRef(cpy_r_r25);
    goto CPyL23;
CPyL26: ;
    CPy_DecRef(cpy_r_r25);
    CPy_DecRef(cpy_r_r27);
    goto CPyL23;
CPyL27: ;
    CPy_DecRef(cpy_r_r25);
    CPy_DecRef(cpy_r_r27);
    CPy_DecRef(cpy_r_r37);
    goto CPyL23;
CPyL28: ;
    CPy_DecRef(cpy_r_r25);
    CPy_DecRef(cpy_r_r45);
    goto CPyL23;
CPyL29: ;
    CPy_DecRef(cpy_r_r58);
    goto CPyL23;
CPyL30: ;
    CPy_DecRef(cpy_r_r58);
    CPy_DecRef(cpy_r_r63);
    goto CPyL23;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[26];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\204\0060x6080604052348015600e575f5ffd5b5060e78061001b5f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063c6803622146034578063e4cb8f5c14604e575b5f5ffd5b603a6056565b60405160459190609a565b60405180910390f35b60546067565b005b5f5f9054906101000a900460ff1681565b60015f5f6101000a81548160ff021916908315150217905550565b5f8115159050919050565b6094816082565b82525050565b5f60208201905060ab5f830184608d565b9291505056fea2646970667358221220a9b00e8591f184642b3b3dfbbe6465e7a6ad284ba74537a9e2445f737666c8a364736f6c634300081e0033",
    "\001 PAYABLE_TESTER_CONTRACT_BYTECODE",
    "\001\203P0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063c6803622146034578063e4cb8f5c14604e575b5f5ffd5b603a6056565b60405160459190609a565b60405180910390f35b60546067565b005b5f5f9054906101000a900460ff1681565b60015f5f6101000a81548160ff021916908315150217905550565b5f8115159050919050565b6094816082565b82525050565b5f60208201905060ab5f830184608d565b9291505056fea2646970667358221220a9b00e8591f184642b3b3dfbbe6465e7a6ad284ba74537a9e2445f737666c8a364736f6c634300081e0033",
    "\005\037PAYABLE_TESTER_CONTRACT_RUNTIME\006inputs\004name\rdoNoValueCall\aoutputs",
    "\b\017stateMutability\nnonpayable\004type\bfunction\twasCalled\finternalType\004bool\000",
    "\005\004view\033PAYABLE_TESTER_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\034PAYABLE_TESTER_CONTRACT_DATA",
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
const int CPyLit_Tuple[] = {0};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___payable_tester;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_payable_tester__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___payable_tester(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___payable_tester, "faster_web3._utils.contract_sources.contract_data.payable_tester__mypyc.init_faster_web3____utils___contract_sources___contract_data___payable_tester", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___payable_tester", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_payable_tester__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.payable_tester__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_payable_tester__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_payable_tester__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_payable_tester__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
