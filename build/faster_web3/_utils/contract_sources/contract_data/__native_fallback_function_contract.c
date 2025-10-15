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
#include "__native_fallback_function_contract.h"
#include "__native_internal_fallback_function_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___fallback_function_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.fallback_function_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___fallback_function_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___fallback_function_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal;
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
    PyObject *cpy_r_r39;
    CPyPtr cpy_r_r40;
    CPyPtr cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    PyObject *cpy_r_r47;
    CPyPtr cpy_r_r48;
    CPyPtr cpy_r_r49;
    CPyPtr cpy_r_r50;
    CPyPtr cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    int32_t cpy_r_r54;
    char cpy_r_r55;
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
    PyObject *cpy_r_r72;
    PyObject *cpy_r_r73;
    int32_t cpy_r_r74;
    char cpy_r_r75;
    char cpy_r_r76;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL23;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x60806040525f5f8190555060b78060155f395ff3fe6080604052348015600e575f5ffd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f5f54905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea264697066735822122046c6693c62c80acbe96048ed262cd69dc31f380a491d7c6dcd21dab372b0f49f64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'FALLBACK_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x6080604052348015600e575f5ffd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f5f54905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea264697066735822122046c6693c62c80acbe96048ed262cd69dc31f380a491d7c6dcd21dab372b0f49f64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'FALLBACK_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r18 = CPyStatics[10]; /* 'payable' */
    cpy_r_r19 = CPyStatics[11]; /* 'type' */
    cpy_r_r20 = CPyStatics[12]; /* 'constructor' */
    cpy_r_r21 = CPyDict_Build(3, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    if (unlikely(cpy_r_r21 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r22 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r23 = CPyStatics[13]; /* 'nonpayable' */
    cpy_r_r24 = CPyStatics[11]; /* 'type' */
    cpy_r_r25 = CPyStatics[14]; /* 'fallback' */
    cpy_r_r26 = CPyDict_Build(2, cpy_r_r22, cpy_r_r23, cpy_r_r24, cpy_r_r25);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r27 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r28 = PyList_New(0);
    if (unlikely(cpy_r_r28 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r29 = CPyStatics[15]; /* 'name' */
    cpy_r_r30 = CPyStatics[16]; /* 'getData' */
    cpy_r_r31 = CPyStatics[17]; /* 'outputs' */
    cpy_r_r32 = CPyStatics[18]; /* 'internalType' */
    cpy_r_r33 = CPyStatics[19]; /* 'uint256' */
    cpy_r_r34 = CPyStatics[15]; /* 'name' */
    cpy_r_r35 = CPyStatics[20]; /* 'r' */
    cpy_r_r36 = CPyStatics[11]; /* 'type' */
    cpy_r_r37 = CPyStatics[19]; /* 'uint256' */
    cpy_r_r38 = CPyDict_Build(3, cpy_r_r32, cpy_r_r33, cpy_r_r34, cpy_r_r35, cpy_r_r36, cpy_r_r37);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 15, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r39 = PyList_New(1);
    if (unlikely(cpy_r_r39 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 15, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r40 = (CPyPtr)&((PyListObject *)cpy_r_r39)->ob_item;
    cpy_r_r41 = *(CPyPtr *)cpy_r_r40;
    *(PyObject * *)cpy_r_r41 = cpy_r_r38;
    cpy_r_r42 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r43 = CPyStatics[21]; /* 'view' */
    cpy_r_r44 = CPyStatics[11]; /* 'type' */
    cpy_r_r45 = CPyStatics[22]; /* 'function' */
    cpy_r_r46 = CPyDict_Build(5, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r39, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45);
    CPy_DECREF_NO_IMM(cpy_r_r28);
    CPy_DECREF_NO_IMM(cpy_r_r39);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 12, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r47 = PyList_New(3);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL28;
    }
    cpy_r_r48 = (CPyPtr)&((PyListObject *)cpy_r_r47)->ob_item;
    cpy_r_r49 = *(CPyPtr *)cpy_r_r48;
    *(PyObject * *)cpy_r_r49 = cpy_r_r21;
    cpy_r_r50 = cpy_r_r49 + 8;
    *(PyObject * *)cpy_r_r50 = cpy_r_r26;
    cpy_r_r51 = cpy_r_r49 + 16;
    *(PyObject * *)cpy_r_r51 = cpy_r_r46;
    cpy_r_r52 = CPyStatic_globals;
    cpy_r_r53 = CPyStatics[23]; /* 'FALLBACK_FUNCTION_CONTRACT_ABI' */
    cpy_r_r54 = CPyDict_SetItem(cpy_r_r52, cpy_r_r53, cpy_r_r47);
    CPy_DECREF_NO_IMM(cpy_r_r47);
    cpy_r_r55 = cpy_r_r54 >= 0;
    if (unlikely(!cpy_r_r55)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r56 = CPyStatics[24]; /* 'bytecode' */
    cpy_r_r57 = CPyStatic_globals;
    cpy_r_r58 = CPyStatics[5]; /* 'FALLBACK_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r59 = CPyDict_GetItem(cpy_r_r57, cpy_r_r58);
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 21, CPyStatic_globals);
        goto CPyL23;
    }
    if (likely(PyUnicode_Check(cpy_r_r59)))
        cpy_r_r60 = cpy_r_r59;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 21, CPyStatic_globals, "str", cpy_r_r59);
        goto CPyL23;
    }
    cpy_r_r61 = CPyStatics[25]; /* 'bytecode_runtime' */
    cpy_r_r62 = CPyStatic_globals;
    cpy_r_r63 = CPyStatics[7]; /* 'FALLBACK_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r64 = CPyDict_GetItem(cpy_r_r62, cpy_r_r63);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 22, CPyStatic_globals);
        goto CPyL29;
    }
    if (likely(PyUnicode_Check(cpy_r_r64)))
        cpy_r_r65 = cpy_r_r64;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 22, CPyStatic_globals, "str", cpy_r_r64);
        goto CPyL29;
    }
    cpy_r_r66 = CPyStatics[26]; /* 'abi' */
    cpy_r_r67 = CPyStatic_globals;
    cpy_r_r68 = CPyStatics[23]; /* 'FALLBACK_FUNCTION_CONTRACT_ABI' */
    cpy_r_r69 = CPyDict_GetItem(cpy_r_r67, cpy_r_r68);
    if (unlikely(cpy_r_r69 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 23, CPyStatic_globals);
        goto CPyL30;
    }
    if (likely(PyList_Check(cpy_r_r69)))
        cpy_r_r70 = cpy_r_r69;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 23, CPyStatic_globals, "list", cpy_r_r69);
        goto CPyL30;
    }
    cpy_r_r71 = CPyDict_Build(3, cpy_r_r56, cpy_r_r60, cpy_r_r61, cpy_r_r65, cpy_r_r66, cpy_r_r70);
    CPy_DECREF(cpy_r_r60);
    CPy_DECREF(cpy_r_r65);
    CPy_DECREF_NO_IMM(cpy_r_r70);
    if (unlikely(cpy_r_r71 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL23;
    }
    cpy_r_r72 = CPyStatic_globals;
    cpy_r_r73 = CPyStatics[27]; /* 'FALLBACK_FUNCTION_CONTRACT_DATA' */
    cpy_r_r74 = CPyDict_SetItem(cpy_r_r72, cpy_r_r73, cpy_r_r71);
    CPy_DECREF(cpy_r_r71);
    cpy_r_r75 = cpy_r_r74 >= 0;
    if (unlikely(!cpy_r_r75)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/fallback_function_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL23;
    }
    return 1;
CPyL23: ;
    cpy_r_r76 = 2;
    return cpy_r_r76;
CPyL24: ;
    CPy_DecRef(cpy_r_r21);
    goto CPyL23;
CPyL25: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r26);
    goto CPyL23;
CPyL26: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r26);
    CPy_DecRef(cpy_r_r28);
    goto CPyL23;
CPyL27: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r26);
    CPy_DecRef(cpy_r_r28);
    CPy_DecRef(cpy_r_r38);
    goto CPyL23;
CPyL28: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r26);
    CPy_DecRef(cpy_r_r46);
    goto CPyL23;
CPyL29: ;
    CPy_DecRef(cpy_r_r60);
    goto CPyL23;
CPyL30: ;
    CPy_DecRef(cpy_r_r60);
    CPy_DecRef(cpy_r_r65);
    goto CPyL23;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[28];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\203\0320x60806040525f5f8190555060b78060155f395ff3fe6080604052348015600e575f5ffd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f5f54905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea264697066735822122046c6693c62c80acbe96048ed262cd69dc31f380a491d7c6dcd21dab372b0f49f64736f6c634300081e0033",
    "\001#FALLBACK_FUNCTION_CONTRACT_BYTECODE",
    "\001\202p0x6080604052348015600e575f5ffd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f5f54905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea264697066735822122046c6693c62c80acbe96048ed262cd69dc31f380a491d7c6dcd21dab372b0f49f64736f6c634300081e0033",
    "\004\"FALLBACK_FUNCTION_CONTRACT_RUNTIME\006inputs\017stateMutability\apayable",
    "\a\004type\vconstructor\nnonpayable\bfallback\004name\agetData\aoutputs",
    "\006\finternalType\auint256\001r\004view\bfunction\036FALLBACK_FUNCTION_CONTRACT_ABI",
    "\004\bbytecode\020bytecode_runtime\003abi\037FALLBACK_FUNCTION_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___fallback_function_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_fallback_function_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___fallback_function_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___fallback_function_contract, "faster_web3._utils.contract_sources.contract_data.fallback_function_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___fallback_function_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___fallback_function_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_fallback_function_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.fallback_function_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_fallback_function_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_fallback_function_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_fallback_function_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
