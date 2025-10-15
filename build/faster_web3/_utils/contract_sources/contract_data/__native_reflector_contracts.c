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
#include "__native_reflector_contracts.h"
#include "__native_internal_reflector_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___reflector_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.reflector_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___reflector_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___reflector_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal;
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
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL26;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5061040d8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f5ffd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f5ffd5b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f5ffd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f5ffd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea264697066735822122009f600775ae570ad2217d53d261d8bbad526d8a48aa30d3ccd54d2823eb0c82c64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'ADDRESS_REFLECTOR_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 7, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f5ffd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f5ffd5b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f5ffd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f5ffd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea264697066735822122009f600775ae570ad2217d53d261d8bbad526d8a48aa30d3ccd54d2823eb0c82c64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'ADDRESS_REFLECTOR_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 8, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'address' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* 'arg' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'address' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL27;
    }
    cpy_r_r24 = (CPyPtr)&((PyListObject *)cpy_r_r23)->ob_item;
    cpy_r_r25 = *(CPyPtr *)cpy_r_r24;
    *(PyObject * *)cpy_r_r25 = cpy_r_r22;
    cpy_r_r26 = CPyStatics[11]; /* 'name' */
    cpy_r_r27 = CPyStatics[14]; /* 'reflect' */
    cpy_r_r28 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r29 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r30 = CPyStatics[10]; /* 'address' */
    cpy_r_r31 = CPyStatics[11]; /* 'name' */
    cpy_r_r32 = CPyStatics[16]; /* '' */
    cpy_r_r33 = CPyStatics[13]; /* 'type' */
    cpy_r_r34 = CPyStatics[10]; /* 'address' */
    cpy_r_r35 = CPyDict_Build(3, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 13, CPyStatic_globals);
        goto CPyL28;
    }
    cpy_r_r36 = PyList_New(1);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 13, CPyStatic_globals);
        goto CPyL29;
    }
    cpy_r_r37 = (CPyPtr)&((PyListObject *)cpy_r_r36)->ob_item;
    cpy_r_r38 = *(CPyPtr *)cpy_r_r37;
    *(PyObject * *)cpy_r_r38 = cpy_r_r35;
    cpy_r_r39 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r40 = CPyStatics[18]; /* 'pure' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[19]; /* 'function' */
    cpy_r_r43 = CPyDict_Build(5, cpy_r_r15, cpy_r_r23, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r36, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    CPy_DECREF_NO_IMM(cpy_r_r23);
    CPy_DECREF_NO_IMM(cpy_r_r36);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r44 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r45 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r46 = CPyStatics[20]; /* 'address[]' */
    cpy_r_r47 = CPyStatics[11]; /* 'name' */
    cpy_r_r48 = CPyStatics[12]; /* 'arg' */
    cpy_r_r49 = CPyStatics[13]; /* 'type' */
    cpy_r_r50 = CPyStatics[20]; /* 'address[]' */
    cpy_r_r51 = CPyDict_Build(3, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL30;
    }
    cpy_r_r52 = PyList_New(1);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL31;
    }
    cpy_r_r53 = (CPyPtr)&((PyListObject *)cpy_r_r52)->ob_item;
    cpy_r_r54 = *(CPyPtr *)cpy_r_r53;
    *(PyObject * *)cpy_r_r54 = cpy_r_r51;
    cpy_r_r55 = CPyStatics[11]; /* 'name' */
    cpy_r_r56 = CPyStatics[14]; /* 'reflect' */
    cpy_r_r57 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r58 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r59 = CPyStatics[20]; /* 'address[]' */
    cpy_r_r60 = CPyStatics[11]; /* 'name' */
    cpy_r_r61 = CPyStatics[16]; /* '' */
    cpy_r_r62 = CPyStatics[13]; /* 'type' */
    cpy_r_r63 = CPyStatics[20]; /* 'address[]' */
    cpy_r_r64 = CPyDict_Build(3, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 20, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r65 = PyList_New(1);
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 20, CPyStatic_globals);
        goto CPyL33;
    }
    cpy_r_r66 = (CPyPtr)&((PyListObject *)cpy_r_r65)->ob_item;
    cpy_r_r67 = *(CPyPtr *)cpy_r_r66;
    *(PyObject * *)cpy_r_r67 = cpy_r_r64;
    cpy_r_r68 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r69 = CPyStatics[18]; /* 'pure' */
    cpy_r_r70 = CPyStatics[13]; /* 'type' */
    cpy_r_r71 = CPyStatics[19]; /* 'function' */
    cpy_r_r72 = CPyDict_Build(5, cpy_r_r44, cpy_r_r52, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r65, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71);
    CPy_DECREF_NO_IMM(cpy_r_r52);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    if (unlikely(cpy_r_r72 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 17, CPyStatic_globals);
        goto CPyL30;
    }
    cpy_r_r73 = PyList_New(2);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r74 = (CPyPtr)&((PyListObject *)cpy_r_r73)->ob_item;
    cpy_r_r75 = *(CPyPtr *)cpy_r_r74;
    *(PyObject * *)cpy_r_r75 = cpy_r_r43;
    cpy_r_r76 = cpy_r_r75 + 8;
    *(PyObject * *)cpy_r_r76 = cpy_r_r72;
    cpy_r_r77 = CPyStatic_globals;
    cpy_r_r78 = CPyStatics[21]; /* 'ADDRESS_REFLECTOR_CONTRACT_ABI' */
    cpy_r_r79 = CPyDict_SetItem(cpy_r_r77, cpy_r_r78, cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r73);
    cpy_r_r80 = cpy_r_r79 >= 0;
    if (unlikely(!cpy_r_r80)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r81 = CPyStatics[22]; /* 'bytecode' */
    cpy_r_r82 = CPyStatic_globals;
    cpy_r_r83 = CPyStatics[5]; /* 'ADDRESS_REFLECTOR_CONTRACT_BYTECODE' */
    cpy_r_r84 = CPyDict_GetItem(cpy_r_r82, cpy_r_r83);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 26, CPyStatic_globals);
        goto CPyL26;
    }
    if (likely(PyUnicode_Check(cpy_r_r84)))
        cpy_r_r85 = cpy_r_r84;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 26, CPyStatic_globals, "str", cpy_r_r84);
        goto CPyL26;
    }
    cpy_r_r86 = CPyStatics[23]; /* 'bytecode_runtime' */
    cpy_r_r87 = CPyStatic_globals;
    cpy_r_r88 = CPyStatics[7]; /* 'ADDRESS_REFLECTOR_CONTRACT_RUNTIME' */
    cpy_r_r89 = CPyDict_GetItem(cpy_r_r87, cpy_r_r88);
    if (unlikely(cpy_r_r89 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 27, CPyStatic_globals);
        goto CPyL35;
    }
    if (likely(PyUnicode_Check(cpy_r_r89)))
        cpy_r_r90 = cpy_r_r89;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 27, CPyStatic_globals, "str", cpy_r_r89);
        goto CPyL35;
    }
    cpy_r_r91 = CPyStatics[24]; /* 'abi' */
    cpy_r_r92 = CPyStatic_globals;
    cpy_r_r93 = CPyStatics[21]; /* 'ADDRESS_REFLECTOR_CONTRACT_ABI' */
    cpy_r_r94 = CPyDict_GetItem(cpy_r_r92, cpy_r_r93);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 28, CPyStatic_globals);
        goto CPyL36;
    }
    if (likely(PyList_Check(cpy_r_r94)))
        cpy_r_r95 = cpy_r_r94;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 28, CPyStatic_globals, "list", cpy_r_r94);
        goto CPyL36;
    }
    cpy_r_r96 = CPyDict_Build(3, cpy_r_r81, cpy_r_r85, cpy_r_r86, cpy_r_r90, cpy_r_r91, cpy_r_r95);
    CPy_DECREF(cpy_r_r85);
    CPy_DECREF(cpy_r_r90);
    CPy_DECREF_NO_IMM(cpy_r_r95);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL26;
    }
    cpy_r_r97 = CPyStatic_globals;
    cpy_r_r98 = CPyStatics[25]; /* 'ADDRESS_REFLECTOR_CONTRACT_DATA' */
    cpy_r_r99 = CPyDict_SetItem(cpy_r_r97, cpy_r_r98, cpy_r_r96);
    CPy_DECREF(cpy_r_r96);
    cpy_r_r100 = cpy_r_r99 >= 0;
    if (unlikely(!cpy_r_r100)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/reflector_contracts.py", "<module>", 25, CPyStatic_globals);
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
    CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts = Py_None;
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
    "\001\220T0x6080604052348015600e575f5ffd5b5061040d8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f5ffd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f5ffd5b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f5ffd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f5ffd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea264697066735822122009f600775ae570ad2217d53d261d8bbad526d8a48aa30d3ccd54d2823eb0c82c64736f6c634300081e0033",
    "\001#ADDRESS_REFLECTOR_CONTRACT_BYTECODE",
    "\001\220\0340x608060405234801561000f575f5ffd5b5060043610610034575f3560e01c80630b816c1614610038578063c04d11fc14610068575b5f5ffd5b610052600480360381019061004d9190610116565b610098565b60405161005f9190610150565b60405180910390f35b610082600480360381019061007d91906102b9565b6100a1565b60405161008f91906103b7565b60405180910390f35b5f819050919050565b6060819050919050565b5f604051905090565b5f5ffd5b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100e5826100bc565b9050919050565b6100f5816100db565b81146100ff575f5ffd5b50565b5f81359050610110816100ec565b92915050565b5f6020828403121561012b5761012a6100b4565b5b5f61013884828501610102565b91505092915050565b61014a816100db565b82525050565b5f6020820190506101635f830184610141565b92915050565b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101b38261016d565b810181811067ffffffffffffffff821117156101d2576101d161017d565b5b80604052505050565b5f6101e46100ab565b90506101f082826101aa565b919050565b5f67ffffffffffffffff82111561020f5761020e61017d565b5b602082029050602081019050919050565b5f5ffd5b5f610236610231846101f5565b6101db565b9050808382526020820190506020840283018581111561025957610258610220565b5b835b81811015610282578061026e8882610102565b84526020840193505060208101905061025b565b5050509392505050565b5f82601f8301126102a05761029f610169565b5b81356102b0848260208601610224565b91505092915050565b5f602082840312156102ce576102cd6100b4565b5b5f82013567ffffffffffffffff8111156102eb576102ea6100b8565b5b6102f78482850161028c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b610332816100db565b82525050565b5f6103438383610329565b60208301905092915050565b5f602082019050919050565b5f61036582610300565b61036f818561030a565b935061037a8361031a565b805f5b838110156103aa5781516103918882610338565b975061039c8361034f565b92505060018101905061037d565b5085935050505092915050565b5f6020820190508181035f8301526103cf818461035b565b90509291505056fea264697066735822122009f600775ae570ad2217d53d261d8bbad526d8a48aa30d3ccd54d2823eb0c82c64736f6c634300081e0033",
    "\005\"ADDRESS_REFLECTOR_CONTRACT_RUNTIME\006inputs\finternalType\aaddress\004name",
    "\t\003arg\004type\areflect\aoutputs\000\017stateMutability\004pure\bfunction\taddress[]",
    "\004\036ADDRESS_REFLECTOR_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\037ADDRESS_REFLECTOR_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___reflector_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_reflector_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___reflector_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___reflector_contracts, "faster_web3._utils.contract_sources.contract_data.reflector_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___reflector_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___reflector_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_reflector_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.reflector_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_reflector_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_reflector_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_reflector_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
