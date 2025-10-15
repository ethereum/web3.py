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
#include "__native_revert_contract.h"
#include "__native_internal_revert_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___revert_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.revert_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___revert_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___revert_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal;
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
    CPyPtr cpy_r_r31;
    CPyPtr cpy_r_r32;
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
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    PyObject *cpy_r_r52;
    PyObject *cpy_r_r53;
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
    PyObject *cpy_r_r72;
    CPyPtr cpy_r_r73;
    CPyPtr cpy_r_r74;
    PyObject *cpy_r_r75;
    PyObject *cpy_r_r76;
    PyObject *cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
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
    PyObject *cpy_r_r99;
    PyObject *cpy_r_r100;
    PyObject *cpy_r_r101;
    PyObject *cpy_r_r102;
    CPyPtr cpy_r_r103;
    CPyPtr cpy_r_r104;
    CPyPtr cpy_r_r105;
    CPyPtr cpy_r_r106;
    CPyPtr cpy_r_r107;
    CPyPtr cpy_r_r108;
    CPyPtr cpy_r_r109;
    CPyPtr cpy_r_r110;
    PyObject *cpy_r_r111;
    PyObject *cpy_r_r112;
    int32_t cpy_r_r113;
    char cpy_r_r114;
    PyObject *cpy_r_r115;
    PyObject *cpy_r_r116;
    PyObject *cpy_r_r117;
    PyObject *cpy_r_r118;
    PyObject *cpy_r_r119;
    PyObject *cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    PyObject *cpy_r_r124;
    PyObject *cpy_r_r125;
    PyObject *cpy_r_r126;
    PyObject *cpy_r_r127;
    PyObject *cpy_r_r128;
    PyObject *cpy_r_r129;
    PyObject *cpy_r_r130;
    PyObject *cpy_r_r131;
    PyObject *cpy_r_r132;
    int32_t cpy_r_r133;
    char cpy_r_r134;
    char cpy_r_r135;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL37;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5061029c8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f5ffd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f5ffd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea26469706673582212202d8ccc055c01870a6d80c5aa5526a92e31b542448b7077752700fe921dea786864736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'REVERT_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f5ffd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f5ffd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea26469706673582212202d8ccc055c01870a6d80c5aa5526a92e31b542448b7077752700fe921dea786864736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'REVERT_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'name' */
    cpy_r_r18 = CPyStatics[10]; /* 'Unauthorized' */
    cpy_r_r19 = CPyStatics[11]; /* 'type' */
    cpy_r_r20 = CPyStatics[12]; /* 'error' */
    cpy_r_r21 = CPyDict_Build(3, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    if (unlikely(cpy_r_r21 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r22 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r23 = CPyStatics[13]; /* 'internalType' */
    cpy_r_r24 = CPyStatics[14]; /* 'string' */
    cpy_r_r25 = CPyStatics[9]; /* 'name' */
    cpy_r_r26 = CPyStatics[15]; /* 'errorMessage' */
    cpy_r_r27 = CPyStatics[11]; /* 'type' */
    cpy_r_r28 = CPyStatics[14]; /* 'string' */
    cpy_r_r29 = CPyDict_Build(3, cpy_r_r23, cpy_r_r24, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r30 = PyList_New(1);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 12, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r31 = (CPyPtr)&((PyListObject *)cpy_r_r30)->ob_item;
    cpy_r_r32 = *(CPyPtr *)cpy_r_r31;
    *(PyObject * *)cpy_r_r32 = cpy_r_r29;
    cpy_r_r33 = CPyStatics[9]; /* 'name' */
    cpy_r_r34 = CPyStatics[16]; /* 'UnauthorizedWithMessage' */
    cpy_r_r35 = CPyStatics[11]; /* 'type' */
    cpy_r_r36 = CPyStatics[12]; /* 'error' */
    cpy_r_r37 = CPyDict_Build(3, cpy_r_r22, cpy_r_r30, cpy_r_r33, cpy_r_r34, cpy_r_r35, cpy_r_r36);
    CPy_DECREF_NO_IMM(cpy_r_r30);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r38 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r39 = PyList_New(0);
    if (unlikely(cpy_r_r39 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 19, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r40 = CPyStatics[9]; /* 'name' */
    cpy_r_r41 = CPyStatics[17]; /* 'customErrorWithMessage' */
    cpy_r_r42 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r43 = PyList_New(0);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 21, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r44 = CPyStatics[19]; /* 'stateMutability' */
    cpy_r_r45 = CPyStatics[20]; /* 'pure' */
    cpy_r_r46 = CPyStatics[11]; /* 'type' */
    cpy_r_r47 = CPyStatics[21]; /* 'function' */
    cpy_r_r48 = CPyDict_Build(5, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45, cpy_r_r46, cpy_r_r47);
    CPy_DECREF_NO_IMM(cpy_r_r39);
    CPy_DECREF_NO_IMM(cpy_r_r43);
    if (unlikely(cpy_r_r48 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 18, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r49 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r50 = PyList_New(0);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r51 = CPyStatics[9]; /* 'name' */
    cpy_r_r52 = CPyStatics[22]; /* 'customErrorWithoutMessage' */
    cpy_r_r53 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r54 = PyList_New(0);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 28, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r55 = CPyStatics[19]; /* 'stateMutability' */
    cpy_r_r56 = CPyStatics[20]; /* 'pure' */
    cpy_r_r57 = CPyStatics[11]; /* 'type' */
    cpy_r_r58 = CPyStatics[21]; /* 'function' */
    cpy_r_r59 = CPyDict_Build(5, cpy_r_r49, cpy_r_r50, cpy_r_r51, cpy_r_r52, cpy_r_r53, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58);
    CPy_DECREF_NO_IMM(cpy_r_r50);
    CPy_DECREF_NO_IMM(cpy_r_r54);
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r60 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r61 = PyList_New(0);
    if (unlikely(cpy_r_r61 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r62 = CPyStatics[9]; /* 'name' */
    cpy_r_r63 = CPyStatics[23]; /* 'normalFunction' */
    cpy_r_r64 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r65 = CPyStatics[13]; /* 'internalType' */
    cpy_r_r66 = CPyStatics[24]; /* 'bool' */
    cpy_r_r67 = CPyStatics[9]; /* 'name' */
    cpy_r_r68 = CPyStatics[25]; /* '' */
    cpy_r_r69 = CPyStatics[11]; /* 'type' */
    cpy_r_r70 = CPyStatics[24]; /* 'bool' */
    cpy_r_r71 = CPyDict_Build(3, cpy_r_r65, cpy_r_r66, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70);
    if (unlikely(cpy_r_r71 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 35, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r72 = PyList_New(1);
    if (unlikely(cpy_r_r72 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 35, CPyStatic_globals);
        goto CPyL46;
    }
    cpy_r_r73 = (CPyPtr)&((PyListObject *)cpy_r_r72)->ob_item;
    cpy_r_r74 = *(CPyPtr *)cpy_r_r73;
    *(PyObject * *)cpy_r_r74 = cpy_r_r71;
    cpy_r_r75 = CPyStatics[19]; /* 'stateMutability' */
    cpy_r_r76 = CPyStatics[20]; /* 'pure' */
    cpy_r_r77 = CPyStatics[11]; /* 'type' */
    cpy_r_r78 = CPyStatics[21]; /* 'function' */
    cpy_r_r79 = CPyDict_Build(5, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64, cpy_r_r72, cpy_r_r75, cpy_r_r76, cpy_r_r77, cpy_r_r78);
    CPy_DECREF_NO_IMM(cpy_r_r61);
    CPy_DECREF_NO_IMM(cpy_r_r72);
    if (unlikely(cpy_r_r79 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 32, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r80 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r81 = PyList_New(0);
    if (unlikely(cpy_r_r81 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 40, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r82 = CPyStatics[9]; /* 'name' */
    cpy_r_r83 = CPyStatics[26]; /* 'revertWithMessage' */
    cpy_r_r84 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r85 = PyList_New(0);
    if (unlikely(cpy_r_r85 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 42, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r86 = CPyStatics[19]; /* 'stateMutability' */
    cpy_r_r87 = CPyStatics[20]; /* 'pure' */
    cpy_r_r88 = CPyStatics[11]; /* 'type' */
    cpy_r_r89 = CPyStatics[21]; /* 'function' */
    cpy_r_r90 = CPyDict_Build(5, cpy_r_r80, cpy_r_r81, cpy_r_r82, cpy_r_r83, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87, cpy_r_r88, cpy_r_r89);
    CPy_DECREF_NO_IMM(cpy_r_r81);
    CPy_DECREF_NO_IMM(cpy_r_r85);
    if (unlikely(cpy_r_r90 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r91 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r92 = PyList_New(0);
    if (unlikely(cpy_r_r92 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 47, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r93 = CPyStatics[9]; /* 'name' */
    cpy_r_r94 = CPyStatics[27]; /* 'revertWithoutMessage' */
    cpy_r_r95 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r96 = PyList_New(0);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 49, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r97 = CPyStatics[19]; /* 'stateMutability' */
    cpy_r_r98 = CPyStatics[20]; /* 'pure' */
    cpy_r_r99 = CPyStatics[11]; /* 'type' */
    cpy_r_r100 = CPyStatics[21]; /* 'function' */
    cpy_r_r101 = CPyDict_Build(5, cpy_r_r91, cpy_r_r92, cpy_r_r93, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100);
    CPy_DECREF_NO_IMM(cpy_r_r92);
    CPy_DECREF_NO_IMM(cpy_r_r96);
    if (unlikely(cpy_r_r101 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 46, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r102 = PyList_New(7);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r103 = (CPyPtr)&((PyListObject *)cpy_r_r102)->ob_item;
    cpy_r_r104 = *(CPyPtr *)cpy_r_r103;
    *(PyObject * *)cpy_r_r104 = cpy_r_r21;
    cpy_r_r105 = cpy_r_r104 + 8;
    *(PyObject * *)cpy_r_r105 = cpy_r_r37;
    cpy_r_r106 = cpy_r_r104 + 16;
    *(PyObject * *)cpy_r_r106 = cpy_r_r48;
    cpy_r_r107 = cpy_r_r104 + 24;
    *(PyObject * *)cpy_r_r107 = cpy_r_r59;
    cpy_r_r108 = cpy_r_r104 + 32;
    *(PyObject * *)cpy_r_r108 = cpy_r_r79;
    cpy_r_r109 = cpy_r_r104 + 40;
    *(PyObject * *)cpy_r_r109 = cpy_r_r90;
    cpy_r_r110 = cpy_r_r104 + 48;
    *(PyObject * *)cpy_r_r110 = cpy_r_r101;
    cpy_r_r111 = CPyStatic_globals;
    cpy_r_r112 = CPyStatics[28]; /* 'REVERT_CONTRACT_ABI' */
    cpy_r_r113 = CPyDict_SetItem(cpy_r_r111, cpy_r_r112, cpy_r_r102);
    CPy_DECREF_NO_IMM(cpy_r_r102);
    cpy_r_r114 = cpy_r_r113 >= 0;
    if (unlikely(!cpy_r_r114)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r115 = CPyStatics[29]; /* 'bytecode' */
    cpy_r_r116 = CPyStatic_globals;
    cpy_r_r117 = CPyStatics[5]; /* 'REVERT_CONTRACT_BYTECODE' */
    cpy_r_r118 = CPyDict_GetItem(cpy_r_r116, cpy_r_r117);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 55, CPyStatic_globals);
        goto CPyL37;
    }
    if (likely(PyUnicode_Check(cpy_r_r118)))
        cpy_r_r119 = cpy_r_r118;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 55, CPyStatic_globals, "str", cpy_r_r118);
        goto CPyL37;
    }
    cpy_r_r120 = CPyStatics[30]; /* 'bytecode_runtime' */
    cpy_r_r121 = CPyStatic_globals;
    cpy_r_r122 = CPyStatics[7]; /* 'REVERT_CONTRACT_RUNTIME' */
    cpy_r_r123 = CPyDict_GetItem(cpy_r_r121, cpy_r_r122);
    if (unlikely(cpy_r_r123 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 56, CPyStatic_globals);
        goto CPyL52;
    }
    if (likely(PyUnicode_Check(cpy_r_r123)))
        cpy_r_r124 = cpy_r_r123;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 56, CPyStatic_globals, "str", cpy_r_r123);
        goto CPyL52;
    }
    cpy_r_r125 = CPyStatics[31]; /* 'abi' */
    cpy_r_r126 = CPyStatic_globals;
    cpy_r_r127 = CPyStatics[28]; /* 'REVERT_CONTRACT_ABI' */
    cpy_r_r128 = CPyDict_GetItem(cpy_r_r126, cpy_r_r127);
    if (unlikely(cpy_r_r128 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 57, CPyStatic_globals);
        goto CPyL53;
    }
    if (likely(PyList_Check(cpy_r_r128)))
        cpy_r_r129 = cpy_r_r128;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 57, CPyStatic_globals, "list", cpy_r_r128);
        goto CPyL53;
    }
    cpy_r_r130 = CPyDict_Build(3, cpy_r_r115, cpy_r_r119, cpy_r_r120, cpy_r_r124, cpy_r_r125, cpy_r_r129);
    CPy_DECREF(cpy_r_r119);
    CPy_DECREF(cpy_r_r124);
    CPy_DECREF_NO_IMM(cpy_r_r129);
    if (unlikely(cpy_r_r130 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 54, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r131 = CPyStatic_globals;
    cpy_r_r132 = CPyStatics[32]; /* 'REVERT_CONTRACT_DATA' */
    cpy_r_r133 = CPyDict_SetItem(cpy_r_r131, cpy_r_r132, cpy_r_r130);
    CPy_DECREF(cpy_r_r130);
    cpy_r_r134 = cpy_r_r133 >= 0;
    if (unlikely(!cpy_r_r134)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/revert_contract.py", "<module>", 54, CPyStatic_globals);
        goto CPyL37;
    }
    return 1;
CPyL37: ;
    cpy_r_r135 = 2;
    return cpy_r_r135;
CPyL38: ;
    CPy_DecRef(cpy_r_r21);
    goto CPyL37;
CPyL39: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r29);
    goto CPyL37;
CPyL40: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    goto CPyL37;
CPyL41: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r39);
    goto CPyL37;
CPyL42: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    goto CPyL37;
CPyL43: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r50);
    goto CPyL37;
CPyL44: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    goto CPyL37;
CPyL45: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r61);
    goto CPyL37;
CPyL46: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r61);
    CPy_DecRef(cpy_r_r71);
    goto CPyL37;
CPyL47: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r79);
    goto CPyL37;
CPyL48: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r79);
    CPy_DecRef(cpy_r_r81);
    goto CPyL37;
CPyL49: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r79);
    CPy_DecRef(cpy_r_r90);
    goto CPyL37;
CPyL50: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r79);
    CPy_DecRef(cpy_r_r90);
    CPy_DecRef(cpy_r_r92);
    goto CPyL37;
CPyL51: ;
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r79);
    CPy_DecRef(cpy_r_r90);
    CPy_DecRef(cpy_r_r101);
    goto CPyL37;
CPyL52: ;
    CPy_DecRef(cpy_r_r119);
    goto CPyL37;
CPyL53: ;
    CPy_DecRef(cpy_r_r119);
    CPy_DecRef(cpy_r_r124);
    goto CPyL37;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[33];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\212r0x6080604052348015600e575f5ffd5b5061029c8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f5ffd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f5ffd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea26469706673582212202d8ccc055c01870a6d80c5aa5526a92e31b542448b7077752700fe921dea786864736f6c634300081e0033",
    "\001\030REVERT_CONTRACT_BYTECODE",
    "\001\212:0x608060405234801561000f575f5ffd5b5060043610610055575f3560e01c8063185c38a414610059578063bc53eca814610063578063c06a97cb1461006d578063d67e4b8414610077578063e766d49814610095575b5f5ffd5b61006161009f565b005b61006b6100da565b005b610075610115565b005b61007f610119565b60405161008c919061016d565b60405180910390f35b61009d610121565b005b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016100d1906101e0565b60405180910390fd5b6040517f9553947a00000000000000000000000000000000000000000000000000000000815260040161010c90610248565b60405180910390fd5b5f5ffd5b5f6001905090565b6040517f82b4290000000000000000000000000000000000000000000000000000000000815260040160405180910390fd5b5f8115159050919050565b61016781610153565b82525050565b5f6020820190506101805f83018461015e565b92915050565b5f82825260208201905092915050565b7f46756e6374696f6e20686173206265656e2072657665727465642e00000000005f82015250565b5f6101ca601b83610186565b91506101d582610196565b602082019050919050565b5f6020820190508181035f8301526101f7816101be565b9050919050565b7f596f7520617265206e6f7420617574686f72697a6564000000000000000000005f82015250565b5f610232601683610186565b915061023d826101fe565b602082019050919050565b5f6020820190508181035f83015261025f81610226565b905091905056fea26469706673582212202d8ccc055c01870a6d80c5aa5526a92e31b542448b7077752700fe921dea786864736f6c634300081e0033",
    "\006\027REVERT_CONTRACT_RUNTIME\006inputs\004name\fUnauthorized\004type\005error",
    "\004\finternalType\006string\ferrorMessage\027UnauthorizedWithMessage",
    "\005\026customErrorWithMessage\aoutputs\017stateMutability\004pure\bfunction",
    "\005\031customErrorWithoutMessage\016normalFunction\004bool\000\021revertWithMessage",
    "\004\024revertWithoutMessage\023REVERT_CONTRACT_ABI\bbytecode\020bytecode_runtime",
    "\002\003abi\024REVERT_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___revert_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_revert_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___revert_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___revert_contract, "faster_web3._utils.contract_sources.contract_data.revert_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___revert_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___revert_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_revert_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.revert_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_revert_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_revert_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_revert_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
