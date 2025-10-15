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
#include "__native_simple_resolver.h"
#include "__native_internal_simple_resolver.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___simple_resolver(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.simple_resolver",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___simple_resolver(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___simple_resolver(CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal;
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
    CPyPtr cpy_r_r24;
    CPyPtr cpy_r_r25;
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
    CPyPtr cpy_r_r37;
    CPyPtr cpy_r_r38;
    PyObject *cpy_r_r39;
    PyObject *cpy_r_r40;
    PyObject *cpy_r_r41;
    PyObject *cpy_r_r42;
    PyObject *cpy_r_r43;
    PyObject *cpy_r_r44;
    PyObject *cpy_r_r45;
    PyObject *cpy_r_r46;
    PyObject *cpy_r_r47;
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    CPyPtr cpy_r_r53;
    CPyPtr cpy_r_r54;
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
    CPyPtr cpy_r_r66;
    CPyPtr cpy_r_r67;
    PyObject *cpy_r_r68;
    PyObject *cpy_r_r69;
    PyObject *cpy_r_r70;
    PyObject *cpy_r_r71;
    PyObject *cpy_r_r72;
    PyObject *cpy_r_r73;
    CPyPtr cpy_r_r74;
    CPyPtr cpy_r_r75;
    CPyPtr cpy_r_r76;
    PyObject *cpy_r_r77;
    PyObject *cpy_r_r78;
    int32_t cpy_r_r79;
    char cpy_r_r80;
    PyObject *cpy_r_r81;
    PyObject *cpy_r_r82;
    PyObject *cpy_r_r83;
    PyObject *cpy_r_r84;
    PyObject *cpy_r_r85;
    PyObject *cpy_r_r86;
    PyObject *cpy_r_r87;
    PyObject *cpy_r_r88;
    PyObject *cpy_r_r89;
    PyObject *cpy_r_r90;
    PyObject *cpy_r_r91;
    PyObject *cpy_r_r92;
    PyObject *cpy_r_r93;
    PyObject *cpy_r_r94;
    PyObject *cpy_r_r95;
    PyObject *cpy_r_r96;
    PyObject *cpy_r_r97;
    PyObject *cpy_r_r98;
    int32_t cpy_r_r99;
    char cpy_r_r100;
    char cpy_r_r101;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", -1, CPyStatic_globals);
        goto CPyL26;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b506102758061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610034575f3560e01c806301ffc9a7146100385780633b3b57de14610068575b5f5ffd5b610052600480360381019061004d919061012b565b610098565b60405161005f9190610170565b60405180910390f35b610082600480360381019061007d91906101bc565b6100c9565b60405161008f9190610226565b60405180910390f35b5f633b3b57de60e01b827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f309050919050565b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61010a816100d6565b8114610114575f5ffd5b50565b5f8135905061012581610101565b92915050565b5f602082840312156101405761013f6100d2565b5b5f61014d84828501610117565b91505092915050565b5f8115159050919050565b61016a81610156565b82525050565b5f6020820190506101835f830184610161565b92915050565b5f819050919050565b61019b81610189565b81146101a5575f5ffd5b50565b5f813590506101b681610192565b92915050565b5f602082840312156101d1576101d06100d2565b5b5f6101de848285016101a8565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610210826101e7565b9050919050565b61022081610206565b82525050565b5f6020820190506102395f830184610217565b9291505056fea26469706673582212205cf7ee37a56d482fe0f5c4387f62bcd4ba469c14d8f69485c72014a1fa02f2e464736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'SIMPLE_RESOLVER_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 7, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b5060043610610034575f3560e01c806301ffc9a7146100385780633b3b57de14610068575b5f5ffd5b610052600480360381019061004d919061012b565b610098565b60405161005f9190610170565b60405180910390f35b610082600480360381019061007d91906101bc565b6100c9565b60405161008f9190610226565b60405180910390f35b5f633b3b57de60e01b827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f309050919050565b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61010a816100d6565b8114610114575f5ffd5b50565b5f8135905061012581610101565b92915050565b5f602082840312156101405761013f6100d2565b5b5f61014d84828501610117565b91505092915050565b5f8115159050919050565b61016a81610156565b82525050565b5f6020820190506101835f830184610161565b92915050565b5f819050919050565b61019b81610189565b81146101a5575f5ffd5b50565b5f813590506101b681610192565b92915050565b5f602082840312156101d1576101d06100d2565b5b5f6101de848285016101a8565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610210826101e7565b9050919050565b61022081610206565b82525050565b5f6020820190506102395f830184610217565b9291505056fea26469706673582212205cf7ee37a56d482fe0f5c4387f62bcd4ba469c14d8f69485c72014a1fa02f2e464736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'SIMPLE_RESOLVER_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 8, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'bytes32' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* 'nodeID' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'bytes32' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 11, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 11, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r24 = (CPyPtr)&((PyListObject *)cpy_r_r23)->ob_item;
    cpy_r_r25 = *(CPyPtr *)cpy_r_r24;
    *(PyObject * *)cpy_r_r25 = cpy_r_r22;
    cpy_r_r26 = CPyStatics[11]; /* 'name' */
    cpy_r_r27 = CPyStatics[14]; /* 'addr' */
    cpy_r_r28 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r29 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r30 = CPyStatics[16]; /* 'address' */
    cpy_r_r31 = CPyStatics[11]; /* 'name' */
    cpy_r_r32 = CPyStatics[17]; /* '' */
    cpy_r_r33 = CPyStatics[13]; /* 'type' */
    cpy_r_r34 = CPyStatics[16]; /* 'address' */
    cpy_r_r35 = CPyDict_Build(3, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 13, CPyStatic_globals);
        goto CPyL28;
    }
    cpy_r_r36 = PyList_New(1);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 13, CPyStatic_globals);
        goto CPyL29;
    }
    cpy_r_r37 = (CPyPtr)&((PyListObject *)cpy_r_r36)->ob_item;
    cpy_r_r38 = *(CPyPtr *)cpy_r_r37;
    *(PyObject * *)cpy_r_r38 = cpy_r_r35;
    cpy_r_r39 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r40 = CPyStatics[19]; /* 'nonpayable' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[20]; /* 'function' */
    cpy_r_r43 = CPyDict_Build(5, cpy_r_r15, cpy_r_r23, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r36, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    CPy_DECREF_NO_IMM(cpy_r_r23);
    CPy_DECREF_NO_IMM(cpy_r_r36);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 10, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r44 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r45 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r46 = CPyStatics[21]; /* 'bytes4' */
    cpy_r_r47 = CPyStatics[11]; /* 'name' */
    cpy_r_r48 = CPyStatics[22]; /* 'interfaceID' */
    cpy_r_r49 = CPyStatics[13]; /* 'type' */
    cpy_r_r50 = CPyStatics[21]; /* 'bytes4' */
    cpy_r_r51 = CPyDict_Build(3, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 18, CPyStatic_globals);
        goto CPyL30;
    }
    cpy_r_r52 = PyList_New(1);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 18, CPyStatic_globals);
        goto CPyL31;
    }
    cpy_r_r53 = (CPyPtr)&((PyListObject *)cpy_r_r52)->ob_item;
    cpy_r_r54 = *(CPyPtr *)cpy_r_r53;
    *(PyObject * *)cpy_r_r54 = cpy_r_r51;
    cpy_r_r55 = CPyStatics[11]; /* 'name' */
    cpy_r_r56 = CPyStatics[23]; /* 'supportsInterface' */
    cpy_r_r57 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r58 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r59 = CPyStatics[24]; /* 'bool' */
    cpy_r_r60 = CPyStatics[11]; /* 'name' */
    cpy_r_r61 = CPyStatics[17]; /* '' */
    cpy_r_r62 = CPyStatics[13]; /* 'type' */
    cpy_r_r63 = CPyStatics[24]; /* 'bool' */
    cpy_r_r64 = CPyDict_Build(3, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 20, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r65 = PyList_New(1);
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 20, CPyStatic_globals);
        goto CPyL33;
    }
    cpy_r_r66 = (CPyPtr)&((PyListObject *)cpy_r_r65)->ob_item;
    cpy_r_r67 = *(CPyPtr *)cpy_r_r66;
    *(PyObject * *)cpy_r_r67 = cpy_r_r64;
    cpy_r_r68 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r69 = CPyStatics[19]; /* 'nonpayable' */
    cpy_r_r70 = CPyStatics[13]; /* 'type' */
    cpy_r_r71 = CPyStatics[20]; /* 'function' */
    cpy_r_r72 = CPyDict_Build(5, cpy_r_r44, cpy_r_r52, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r65, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71);
    CPy_DECREF_NO_IMM(cpy_r_r52);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    if (unlikely(cpy_r_r72 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 17, CPyStatic_globals);
        goto CPyL30;
    }
    cpy_r_r73 = PyList_New(2);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 9, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r74 = (CPyPtr)&((PyListObject *)cpy_r_r73)->ob_item;
    cpy_r_r75 = *(CPyPtr *)cpy_r_r74;
    *(PyObject * *)cpy_r_r75 = cpy_r_r43;
    cpy_r_r76 = cpy_r_r75 + 8;
    *(PyObject * *)cpy_r_r76 = cpy_r_r72;
    cpy_r_r77 = CPyStatic_globals;
    cpy_r_r78 = CPyStatics[25]; /* 'SIMPLE_RESOLVER_ABI' */
    cpy_r_r79 = CPyDict_SetItem(cpy_r_r77, cpy_r_r78, cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r73);
    cpy_r_r80 = cpy_r_r79 >= 0;
    if (unlikely(!cpy_r_r80)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 9, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r81 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r82 = CPyStatic_globals;
    cpy_r_r83 = CPyStatics[5]; /* 'SIMPLE_RESOLVER_BYTECODE' */
    cpy_r_r84 = CPyDict_GetItem(cpy_r_r82, cpy_r_r83);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 26, CPyStatic_globals);
        goto CPyL26;
    }
    if (likely(PyUnicode_Check(cpy_r_r84)))
        cpy_r_r85 = cpy_r_r84;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 26, CPyStatic_globals, "str", cpy_r_r84);
        goto CPyL26;
    }
    cpy_r_r86 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r87 = CPyStatic_globals;
    cpy_r_r88 = CPyStatics[7]; /* 'SIMPLE_RESOLVER_RUNTIME' */
    cpy_r_r89 = CPyDict_GetItem(cpy_r_r87, cpy_r_r88);
    if (unlikely(cpy_r_r89 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 27, CPyStatic_globals);
        goto CPyL35;
    }
    if (likely(PyUnicode_Check(cpy_r_r89)))
        cpy_r_r90 = cpy_r_r89;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 27, CPyStatic_globals, "str", cpy_r_r89);
        goto CPyL35;
    }
    cpy_r_r91 = CPyStatics[28]; /* 'abi' */
    cpy_r_r92 = CPyStatic_globals;
    cpy_r_r93 = CPyStatics[25]; /* 'SIMPLE_RESOLVER_ABI' */
    cpy_r_r94 = CPyDict_GetItem(cpy_r_r92, cpy_r_r93);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 28, CPyStatic_globals);
        goto CPyL36;
    }
    if (likely(PyList_Check(cpy_r_r94)))
        cpy_r_r95 = cpy_r_r94;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 28, CPyStatic_globals, "list", cpy_r_r94);
        goto CPyL36;
    }
    cpy_r_r96 = CPyDict_Build(3, cpy_r_r81, cpy_r_r85, cpy_r_r86, cpy_r_r90, cpy_r_r91, cpy_r_r95);
    CPy_DECREF(cpy_r_r85);
    CPy_DECREF(cpy_r_r90);
    CPy_DECREF_NO_IMM(cpy_r_r95);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 25, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r97 = CPyStatic_globals;
    cpy_r_r98 = CPyStatics[29]; /* 'SIMPLE_RESOLVER_DATA' */
    cpy_r_r99 = CPyDict_SetItem(cpy_r_r97, cpy_r_r98, cpy_r_r96);
    CPy_DECREF(cpy_r_r96);
    cpy_r_r100 = cpy_r_r99 >= 0;
    if (unlikely(!cpy_r_r100)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/simple_resolver.py", "<module>", 25, CPyStatic_globals);
        goto CPyL26;
    }
    return 1;
CPyL26: ;
    cpy_r_r101 = 2;
    return cpy_r_r101;
CPyL27: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL26;
CPyL28: ;
    CPy_DecRef(cpy_r_r23);
    goto CPyL26;
CPyL29: ;
    CPy_DecRef(cpy_r_r23);
    CPy_DecRef(cpy_r_r35);
    goto CPyL26;
CPyL30: ;
    CPy_DecRef(cpy_r_r43);
    goto CPyL26;
CPyL31: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r51);
    goto CPyL26;
CPyL32: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r52);
    goto CPyL26;
CPyL33: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r52);
    CPy_DecRef(cpy_r_r64);
    goto CPyL26;
CPyL34: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r72);
    goto CPyL26;
CPyL35: ;
    CPy_DecRef(cpy_r_r85);
    goto CPyL26;
CPyL36: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r90);
    goto CPyL26;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[30];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\212$0x6080604052348015600e575f5ffd5b506102758061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610034575f3560e01c806301ffc9a7146100385780633b3b57de14610068575b5f5ffd5b610052600480360381019061004d919061012b565b610098565b60405161005f9190610170565b60405180910390f35b610082600480360381019061007d91906101bc565b6100c9565b60405161008f9190610226565b60405180910390f35b5f633b3b57de60e01b827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f309050919050565b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61010a816100d6565b8114610114575f5ffd5b50565b5f8135905061012581610101565b92915050565b5f602082840312156101405761013f6100d2565b5b5f61014d84828501610117565b91505092915050565b5f8115159050919050565b61016a81610156565b82525050565b5f6020820190506101835f830184610161565b92915050565b5f819050919050565b61019b81610189565b81146101a5575f5ffd5b50565b5f813590506101b681610192565b92915050565b5f602082840312156101d1576101d06100d2565b5b5f6101de848285016101a8565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610210826101e7565b9050919050565b61022081610206565b82525050565b5f6020820190506102395f830184610217565b9291505056fea26469706673582212205cf7ee37a56d482fe0f5c4387f62bcd4ba469c14d8f69485c72014a1fa02f2e464736f6c634300081e0033",
    "\001\030SIMPLE_RESOLVER_BYTECODE",
    "\001\211l0x608060405234801561000f575f5ffd5b5060043610610034575f3560e01c806301ffc9a7146100385780633b3b57de14610068575b5f5ffd5b610052600480360381019061004d919061012b565b610098565b60405161005f9190610170565b60405180910390f35b610082600480360381019061007d91906101bc565b6100c9565b60405161008f9190610226565b60405180910390f35b5f633b3b57de60e01b827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f309050919050565b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61010a816100d6565b8114610114575f5ffd5b50565b5f8135905061012581610101565b92915050565b5f602082840312156101405761013f6100d2565b5b5f61014d84828501610117565b91505092915050565b5f8115159050919050565b61016a81610156565b82525050565b5f6020820190506101835f830184610161565b92915050565b5f819050919050565b61019b81610189565b81146101a5575f5ffd5b50565b5f813590506101b681610192565b92915050565b5f602082840312156101d1576101d06100d2565b5b5f6101de848285016101a8565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610210826101e7565b9050919050565b61022081610206565b82525050565b5f6020820190506102395f830184610217565b9291505056fea26469706673582212205cf7ee37a56d482fe0f5c4387f62bcd4ba469c14d8f69485c72014a1fa02f2e464736f6c634300081e0033",
    "\a\027SIMPLE_RESOLVER_RUNTIME\006inputs\finternalType\abytes32\004name\006nodeID\004type",
    "\b\004addr\aoutputs\aaddress\000\017stateMutability\nnonpayable\bfunction\006bytes4",
    "\005\vinterfaceID\021supportsInterface\004bool\023SIMPLE_RESOLVER_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi\024SIMPLE_RESOLVER_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___simple_resolver;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_simple_resolver__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___simple_resolver(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___simple_resolver, "faster_web3._utils.contract_sources.contract_data.simple_resolver__mypyc.init_faster_web3____utils___contract_sources___contract_data___simple_resolver", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___simple_resolver", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_simple_resolver__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.simple_resolver__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_simple_resolver__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_simple_resolver__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_simple_resolver__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
