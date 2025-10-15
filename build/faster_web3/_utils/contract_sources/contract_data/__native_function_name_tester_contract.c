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
#include "__native_function_name_tester_contract.h"
#include "__native_internal_function_name_tester_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.function_name_tester_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal;
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
    CPyPtr cpy_r_r28;
    CPyPtr cpy_r_r29;
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
    CPyPtr cpy_r_r48;
    CPyPtr cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    CPyPtr cpy_r_r56;
    CPyPtr cpy_r_r57;
    CPyPtr cpy_r_r58;
    PyObject *cpy_r_r59;
    PyObject *cpy_r_r60;
    int32_t cpy_r_r61;
    char cpy_r_r62;
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
    PyObject *cpy_r_r74;
    PyObject *cpy_r_r75;
    PyObject *cpy_r_r76;
    PyObject *cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
    int32_t cpy_r_r81;
    char cpy_r_r82;
    char cpy_r_r83;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL24;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5060dc80601a5f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063a044c987146034578063c5d7802e14604e575b5f5ffd5b603a6068565b60405160459190608f565b60405180910390f35b60546070565b604051605f9190608f565b60405180910390f35b5f6001905090565b5f5f905090565b5f8115159050919050565b6089816077565b82525050565b5f60208201905060a05f8301846082565b9291505056fea2646970667358221220e80d421a7d25249f02ba1ad2cb1bf575d771f76cd10c51edd44fcbfe3307088564736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'FUNCTION_NAME_TESTER_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063a044c987146034578063c5d7802e14604e575b5f5ffd5b603a6068565b60405160459190608f565b60405180910390f35b60546070565b604051605f9190608f565b60405180910390f35b5f6001905090565b5f5f905090565b5f8115159050919050565b6089816077565b82525050565b5f60208201905060a05f8301846082565b9291505056fea2646970667358221220e80d421a7d25249f02ba1ad2cb1bf575d771f76cd10c51edd44fcbfe3307088564736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'FUNCTION_NAME_TESTER_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'name' */
    cpy_r_r18 = CPyStatics[10]; /* 'w3' */
    cpy_r_r19 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r20 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r21 = CPyStatics[13]; /* 'bool' */
    cpy_r_r22 = CPyStatics[9]; /* 'name' */
    cpy_r_r23 = CPyStatics[14]; /* '' */
    cpy_r_r24 = CPyStatics[15]; /* 'type' */
    cpy_r_r25 = CPyStatics[13]; /* 'bool' */
    cpy_r_r26 = CPyDict_Build(3, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23, cpy_r_r24, cpy_r_r25);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL25;
    }
    cpy_r_r27 = PyList_New(1);
    if (unlikely(cpy_r_r27 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r28 = (CPyPtr)&((PyListObject *)cpy_r_r27)->ob_item;
    cpy_r_r29 = *(CPyPtr *)cpy_r_r28;
    *(PyObject * *)cpy_r_r29 = cpy_r_r26;
    cpy_r_r30 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r31 = CPyStatics[17]; /* 'nonpayable' */
    cpy_r_r32 = CPyStatics[15]; /* 'type' */
    cpy_r_r33 = CPyStatics[18]; /* 'function' */
    cpy_r_r34 = CPyDict_Build(5, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r27, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    CPy_DECREF_NO_IMM(cpy_r_r27);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r35 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r36 = PyList_New(0);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 18, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r37 = CPyStatics[9]; /* 'name' */
    cpy_r_r38 = CPyStatics[19]; /* 'z' */
    cpy_r_r39 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r40 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r41 = CPyStatics[13]; /* 'bool' */
    cpy_r_r42 = CPyStatics[9]; /* 'name' */
    cpy_r_r43 = CPyStatics[14]; /* '' */
    cpy_r_r44 = CPyStatics[15]; /* 'type' */
    cpy_r_r45 = CPyStatics[13]; /* 'bool' */
    cpy_r_r46 = CPyDict_Build(3, cpy_r_r40, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL28;
    }
    cpy_r_r47 = PyList_New(1);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL29;
    }
    cpy_r_r48 = (CPyPtr)&((PyListObject *)cpy_r_r47)->ob_item;
    cpy_r_r49 = *(CPyPtr *)cpy_r_r48;
    *(PyObject * *)cpy_r_r49 = cpy_r_r46;
    cpy_r_r50 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r51 = CPyStatics[17]; /* 'nonpayable' */
    cpy_r_r52 = CPyStatics[15]; /* 'type' */
    cpy_r_r53 = CPyStatics[18]; /* 'function' */
    cpy_r_r54 = CPyDict_Build(5, cpy_r_r35, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r47, cpy_r_r50, cpy_r_r51, cpy_r_r52, cpy_r_r53);
    CPy_DECREF_NO_IMM(cpy_r_r36);
    CPy_DECREF_NO_IMM(cpy_r_r47);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 17, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r55 = PyList_New(2);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL30;
    }
    cpy_r_r56 = (CPyPtr)&((PyListObject *)cpy_r_r55)->ob_item;
    cpy_r_r57 = *(CPyPtr *)cpy_r_r56;
    *(PyObject * *)cpy_r_r57 = cpy_r_r34;
    cpy_r_r58 = cpy_r_r57 + 8;
    *(PyObject * *)cpy_r_r58 = cpy_r_r54;
    cpy_r_r59 = CPyStatic_globals;
    cpy_r_r60 = CPyStatics[20]; /* 'FUNCTION_NAME_TESTER_CONTRACT_ABI' */
    cpy_r_r61 = CPyDict_SetItem(cpy_r_r59, cpy_r_r60, cpy_r_r55);
    CPy_DECREF_NO_IMM(cpy_r_r55);
    cpy_r_r62 = cpy_r_r61 >= 0;
    if (unlikely(!cpy_r_r62)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r63 = CPyStatics[21]; /* 'bytecode' */
    cpy_r_r64 = CPyStatic_globals;
    cpy_r_r65 = CPyStatics[5]; /* 'FUNCTION_NAME_TESTER_CONTRACT_BYTECODE' */
    cpy_r_r66 = CPyDict_GetItem(cpy_r_r64, cpy_r_r65);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL24;
    }
    if (likely(PyUnicode_Check(cpy_r_r66)))
        cpy_r_r67 = cpy_r_r66;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 26, CPyStatic_globals, "str", cpy_r_r66);
        goto CPyL24;
    }
    cpy_r_r68 = CPyStatics[22]; /* 'bytecode_runtime' */
    cpy_r_r69 = CPyStatic_globals;
    cpy_r_r70 = CPyStatics[7]; /* 'FUNCTION_NAME_TESTER_CONTRACT_RUNTIME' */
    cpy_r_r71 = CPyDict_GetItem(cpy_r_r69, cpy_r_r70);
    if (unlikely(cpy_r_r71 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 27, CPyStatic_globals);
        goto CPyL31;
    }
    if (likely(PyUnicode_Check(cpy_r_r71)))
        cpy_r_r72 = cpy_r_r71;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 27, CPyStatic_globals, "str", cpy_r_r71);
        goto CPyL31;
    }
    cpy_r_r73 = CPyStatics[23]; /* 'abi' */
    cpy_r_r74 = CPyStatic_globals;
    cpy_r_r75 = CPyStatics[20]; /* 'FUNCTION_NAME_TESTER_CONTRACT_ABI' */
    cpy_r_r76 = CPyDict_GetItem(cpy_r_r74, cpy_r_r75);
    if (unlikely(cpy_r_r76 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 28, CPyStatic_globals);
        goto CPyL32;
    }
    if (likely(PyList_Check(cpy_r_r76)))
        cpy_r_r77 = cpy_r_r76;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 28, CPyStatic_globals, "list", cpy_r_r76);
        goto CPyL32;
    }
    cpy_r_r78 = CPyDict_Build(3, cpy_r_r63, cpy_r_r67, cpy_r_r68, cpy_r_r72, cpy_r_r73, cpy_r_r77);
    CPy_DECREF(cpy_r_r67);
    CPy_DECREF(cpy_r_r72);
    CPy_DECREF_NO_IMM(cpy_r_r77);
    if (unlikely(cpy_r_r78 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL24;
    }
    cpy_r_r79 = CPyStatic_globals;
    cpy_r_r80 = CPyStatics[24]; /* 'FUNCTION_NAME_TESTER_CONTRACT_DATA' */
    cpy_r_r81 = CPyDict_SetItem(cpy_r_r79, cpy_r_r80, cpy_r_r78);
    CPy_DECREF(cpy_r_r78);
    cpy_r_r82 = cpy_r_r81 >= 0;
    if (unlikely(!cpy_r_r82)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/function_name_tester_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL24;
    }
    return 1;
CPyL24: ;
    cpy_r_r83 = 2;
    return cpy_r_r83;
CPyL25: ;
    CPy_DecRef(cpy_r_r16);
    goto CPyL24;
CPyL26: ;
    CPy_DecRef(cpy_r_r16);
    CPy_DecRef(cpy_r_r26);
    goto CPyL24;
CPyL27: ;
    CPy_DecRef(cpy_r_r34);
    goto CPyL24;
CPyL28: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r36);
    goto CPyL24;
CPyL29: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r36);
    CPy_DecRef(cpy_r_r46);
    goto CPyL24;
CPyL30: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    goto CPyL24;
CPyL31: ;
    CPy_DecRef(cpy_r_r67);
    goto CPyL24;
CPyL32: ;
    CPy_DecRef(cpy_r_r67);
    CPy_DecRef(cpy_r_r72);
    goto CPyL24;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[25];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\203n0x6080604052348015600e575f5ffd5b5060dc80601a5f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063a044c987146034578063c5d7802e14604e575b5f5ffd5b603a6068565b60405160459190608f565b60405180910390f35b60546070565b604051605f9190608f565b60405180910390f35b5f6001905090565b5f5f905090565b5f8115159050919050565b6089816077565b82525050565b5f60208201905060a05f8301846082565b9291505056fea2646970667358221220e80d421a7d25249f02ba1ad2cb1bf575d771f76cd10c51edd44fcbfe3307088564736f6c634300081e0033",
    "\001&FUNCTION_NAME_TESTER_CONTRACT_BYTECODE",
    "\001\203:0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c8063a044c987146034578063c5d7802e14604e575b5f5ffd5b603a6068565b60405160459190608f565b60405180910390f35b60546070565b604051605f9190608f565b60405180910390f35b5f6001905090565b5f5f905090565b5f8115159050919050565b6089816077565b82525050565b5f60208201905060a05f8301846082565b9291505056fea2646970667358221220e80d421a7d25249f02ba1ad2cb1bf575d771f76cd10c51edd44fcbfe3307088564736f6c634300081e0033",
    "\005%FUNCTION_NAME_TESTER_CONTRACT_RUNTIME\006inputs\004name\002w3\aoutputs",
    "\b\finternalType\004bool\000\004type\017stateMutability\nnonpayable\bfunction\001z",
    "\004!FUNCTION_NAME_TESTER_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\"FUNCTION_NAME_TESTER_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_function_name_tester_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract, "faster_web3._utils.contract_sources.contract_data.function_name_tester_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___function_name_tester_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_function_name_tester_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.function_name_tester_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_function_name_tester_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_function_name_tester_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_function_name_tester_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
