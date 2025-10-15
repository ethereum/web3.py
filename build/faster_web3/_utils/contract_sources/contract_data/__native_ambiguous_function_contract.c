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
#include "__native_ambiguous_function_contract.h"
#include "__native_internal_ambiguous_function_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.ambiguous_function_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal;
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
    CPyPtr cpy_r_r33;
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
    CPyPtr cpy_r_r45;
    CPyPtr cpy_r_r46;
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
    CPyPtr cpy_r_r68;
    CPyPtr cpy_r_r69;
    CPyPtr cpy_r_r70;
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
    PyObject *cpy_r_r81;
    CPyPtr cpy_r_r82;
    CPyPtr cpy_r_r83;
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
    CPyPtr cpy_r_r102;
    CPyPtr cpy_r_r103;
    PyObject *cpy_r_r104;
    PyObject *cpy_r_r105;
    PyObject *cpy_r_r106;
    PyObject *cpy_r_r107;
    PyObject *cpy_r_r108;
    PyObject *cpy_r_r109;
    CPyPtr cpy_r_r110;
    CPyPtr cpy_r_r111;
    CPyPtr cpy_r_r112;
    CPyPtr cpy_r_r113;
    PyObject *cpy_r_r114;
    PyObject *cpy_r_r115;
    int32_t cpy_r_r116;
    char cpy_r_r117;
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
    PyObject *cpy_r_r133;
    PyObject *cpy_r_r134;
    PyObject *cpy_r_r135;
    int32_t cpy_r_r136;
    char cpy_r_r137;
    char cpy_r_r138;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL32;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5061044a8061001c5f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c80631626ba7e1461004357806320c13b0b14610073578063d482bb47146100a3575b5f5ffd5b61005d60048036038101906100589190610293565b6100c1565b60405161006a9190610305565b60405180910390f35b61008d6004803603810190610088919061031e565b6100cb565b60405161009a9190610305565b60405180910390f35b6100ab6100d6565b6040516100b891906103f4565b60405180910390f35b5f5f905092915050565b5f6001905092915050565b60606040518060400160405280600581526020017f76616c6964000000000000000000000000000000000000000000000000000000815250905090565b5f604051905090565b5f5ffd5b5f5ffd5b5f819050919050565b61013681610124565b8114610140575f5ffd5b50565b5f813590506101518161012d565b92915050565b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101a58261015f565b810181811067ffffffffffffffff821117156101c4576101c361016f565b5b80604052505050565b5f6101d6610113565b90506101e2828261019c565b919050565b5f67ffffffffffffffff8211156102015761020061016f565b5b61020a8261015f565b9050602081019050919050565b828183375f83830152505050565b5f610237610232846101e7565b6101cd565b9050828152602081018484840111156102535761025261015b565b5b61025e848285610217565b509392505050565b5f82601f83011261027a57610279610157565b5b813561028a848260208601610225565b91505092915050565b5f5f604083850312156102a9576102a861011c565b5b5f6102b685828601610143565b925050602083013567ffffffffffffffff8111156102d7576102d6610120565b5b6102e385828601610266565b9150509250929050565b5f819050919050565b6102ff816102ed565b82525050565b5f6020820190506103185f8301846102f6565b92915050565b5f5f604083850312156103345761033361011c565b5b5f83013567ffffffffffffffff81111561035157610350610120565b5b61035d85828601610266565b925050602083013567ffffffffffffffff81111561037e5761037d610120565b5b61038a85828601610266565b9150509250929050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6103c682610394565b6103d0818561039e565b93506103e08185602086016103ae565b6103e98161015f565b840191505092915050565b5f6020820190508181035f83015261040c81846103bc565b90509291505056fea26469706673582212207771e80e03817222551c15a244685f02dd958991f78b46e6373f839b286c0be264736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c80631626ba7e1461004357806320c13b0b14610073578063d482bb47146100a3575b5f5ffd5b61005d60048036038101906100589190610293565b6100c1565b60405161006a9190610305565b60405180910390f35b61008d6004803603810190610088919061031e565b6100cb565b60405161009a9190610305565b60405180910390f35b6100ab6100d6565b6040516100b891906103f4565b60405180910390f35b5f5f905092915050565b5f6001905092915050565b60606040518060400160405280600581526020017f76616c6964000000000000000000000000000000000000000000000000000000815250905090565b5f604051905090565b5f5ffd5b5f5ffd5b5f819050919050565b61013681610124565b8114610140575f5ffd5b50565b5f813590506101518161012d565b92915050565b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101a58261015f565b810181811067ffffffffffffffff821117156101c4576101c361016f565b5b80604052505050565b5f6101d6610113565b90506101e2828261019c565b919050565b5f67ffffffffffffffff8211156102015761020061016f565b5b61020a8261015f565b9050602081019050919050565b828183375f83830152505050565b5f610237610232846101e7565b6101cd565b9050828152602081018484840111156102535761025261015b565b5b61025e848285610217565b509392505050565b5f82601f83011261027a57610279610157565b5b813561028a848260208601610225565b91505092915050565b5f5f604083850312156102a9576102a861011c565b5b5f6102b685828601610143565b925050602083013567ffffffffffffffff8111156102d7576102d6610120565b5b6102e385828601610266565b9150509250929050565b5f819050919050565b6102ff816102ed565b82525050565b5f6020820190506103185f8301846102f6565b92915050565b5f5f604083850312156103345761033361011c565b5b5f83013567ffffffffffffffff81111561035157610350610120565b5b61035d85828601610266565b925050602083013567ffffffffffffffff81111561037e5761037d610120565b5b61038a85828601610266565b9150509250929050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6103c682610394565b6103d0818561039e565b93506103e08185602086016103ae565b6103e98161015f565b840191505092915050565b5f6020820190508181035f83015261040c81846103bc565b90509291505056fea26469706673582212207771e80e03817222551c15a244685f02dd958991f78b46e6373f839b286c0be264736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'bytes32' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* 'message' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'bytes32' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 12, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r23 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r24 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r25 = CPyStatics[11]; /* 'name' */
    cpy_r_r26 = CPyStatics[15]; /* 'signature' */
    cpy_r_r27 = CPyStatics[13]; /* 'type' */
    cpy_r_r28 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r29 = CPyDict_Build(3, cpy_r_r23, cpy_r_r24, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL33;
    }
    cpy_r_r30 = PyList_New(2);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r31 = (CPyPtr)&((PyListObject *)cpy_r_r30)->ob_item;
    cpy_r_r32 = *(CPyPtr *)cpy_r_r31;
    *(PyObject * *)cpy_r_r32 = cpy_r_r22;
    cpy_r_r33 = cpy_r_r32 + 8;
    *(PyObject * *)cpy_r_r33 = cpy_r_r29;
    cpy_r_r34 = CPyStatics[11]; /* 'name' */
    cpy_r_r35 = CPyStatics[16]; /* 'isValidSignature' */
    cpy_r_r36 = CPyStatics[17]; /* 'outputs' */
    cpy_r_r37 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r38 = CPyStatics[18]; /* 'uint256' */
    cpy_r_r39 = CPyStatics[11]; /* 'name' */
    cpy_r_r40 = CPyStatics[19]; /* 'result' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[18]; /* 'uint256' */
    cpy_r_r43 = CPyDict_Build(3, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 16, CPyStatic_globals);
        goto CPyL35;
    }
    cpy_r_r44 = PyList_New(1);
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 16, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r45 = (CPyPtr)&((PyListObject *)cpy_r_r44)->ob_item;
    cpy_r_r46 = *(CPyPtr *)cpy_r_r45;
    *(PyObject * *)cpy_r_r46 = cpy_r_r43;
    cpy_r_r47 = CPyStatics[20]; /* 'stateMutability' */
    cpy_r_r48 = CPyStatics[21]; /* 'view' */
    cpy_r_r49 = CPyStatics[13]; /* 'type' */
    cpy_r_r50 = CPyStatics[22]; /* 'function' */
    cpy_r_r51 = CPyDict_Build(5, cpy_r_r15, cpy_r_r30, cpy_r_r34, cpy_r_r35, cpy_r_r36, cpy_r_r44, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50);
    CPy_DECREF_NO_IMM(cpy_r_r30);
    CPy_DECREF_NO_IMM(cpy_r_r44);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r52 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r53 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r54 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r55 = CPyStatics[11]; /* 'name' */
    cpy_r_r56 = CPyStatics[12]; /* 'message' */
    cpy_r_r57 = CPyStatics[13]; /* 'type' */
    cpy_r_r58 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r59 = CPyDict_Build(3, cpy_r_r53, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58);
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 22, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r60 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r61 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r62 = CPyStatics[11]; /* 'name' */
    cpy_r_r63 = CPyStatics[15]; /* 'signature' */
    cpy_r_r64 = CPyStatics[13]; /* 'type' */
    cpy_r_r65 = CPyStatics[14]; /* 'bytes' */
    cpy_r_r66 = CPyDict_Build(3, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64, cpy_r_r65);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 23, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r67 = PyList_New(2);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 21, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r68 = (CPyPtr)&((PyListObject *)cpy_r_r67)->ob_item;
    cpy_r_r69 = *(CPyPtr *)cpy_r_r68;
    *(PyObject * *)cpy_r_r69 = cpy_r_r59;
    cpy_r_r70 = cpy_r_r69 + 8;
    *(PyObject * *)cpy_r_r70 = cpy_r_r66;
    cpy_r_r71 = CPyStatics[11]; /* 'name' */
    cpy_r_r72 = CPyStatics[16]; /* 'isValidSignature' */
    cpy_r_r73 = CPyStatics[17]; /* 'outputs' */
    cpy_r_r74 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r75 = CPyStatics[18]; /* 'uint256' */
    cpy_r_r76 = CPyStatics[11]; /* 'name' */
    cpy_r_r77 = CPyStatics[19]; /* 'result' */
    cpy_r_r78 = CPyStatics[13]; /* 'type' */
    cpy_r_r79 = CPyStatics[18]; /* 'uint256' */
    cpy_r_r80 = CPyDict_Build(3, cpy_r_r74, cpy_r_r75, cpy_r_r76, cpy_r_r77, cpy_r_r78, cpy_r_r79);
    if (unlikely(cpy_r_r80 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r81 = PyList_New(1);
    if (unlikely(cpy_r_r81 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r82 = (CPyPtr)&((PyListObject *)cpy_r_r81)->ob_item;
    cpy_r_r83 = *(CPyPtr *)cpy_r_r82;
    *(PyObject * *)cpy_r_r83 = cpy_r_r80;
    cpy_r_r84 = CPyStatics[20]; /* 'stateMutability' */
    cpy_r_r85 = CPyStatics[21]; /* 'view' */
    cpy_r_r86 = CPyStatics[13]; /* 'type' */
    cpy_r_r87 = CPyStatics[22]; /* 'function' */
    cpy_r_r88 = CPyDict_Build(5, cpy_r_r52, cpy_r_r67, cpy_r_r71, cpy_r_r72, cpy_r_r73, cpy_r_r81, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87);
    CPy_DECREF_NO_IMM(cpy_r_r67);
    CPy_DECREF_NO_IMM(cpy_r_r81);
    if (unlikely(cpy_r_r88 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r89 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r90 = PyList_New(0);
    if (unlikely(cpy_r_r90 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 31, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r91 = CPyStatics[11]; /* 'name' */
    cpy_r_r92 = CPyStatics[16]; /* 'isValidSignature' */
    cpy_r_r93 = CPyStatics[17]; /* 'outputs' */
    cpy_r_r94 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r95 = CPyStatics[23]; /* 'string' */
    cpy_r_r96 = CPyStatics[11]; /* 'name' */
    cpy_r_r97 = CPyStatics[19]; /* 'result' */
    cpy_r_r98 = CPyStatics[13]; /* 'type' */
    cpy_r_r99 = CPyStatics[23]; /* 'string' */
    cpy_r_r100 = CPyDict_Build(3, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r97, cpy_r_r98, cpy_r_r99);
    if (unlikely(cpy_r_r100 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r101 = PyList_New(1);
    if (unlikely(cpy_r_r101 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r102 = (CPyPtr)&((PyListObject *)cpy_r_r101)->ob_item;
    cpy_r_r103 = *(CPyPtr *)cpy_r_r102;
    *(PyObject * *)cpy_r_r103 = cpy_r_r100;
    cpy_r_r104 = CPyStatics[20]; /* 'stateMutability' */
    cpy_r_r105 = CPyStatics[21]; /* 'view' */
    cpy_r_r106 = CPyStatics[13]; /* 'type' */
    cpy_r_r107 = CPyStatics[22]; /* 'function' */
    cpy_r_r108 = CPyDict_Build(5, cpy_r_r89, cpy_r_r90, cpy_r_r91, cpy_r_r92, cpy_r_r93, cpy_r_r101, cpy_r_r104, cpy_r_r105, cpy_r_r106, cpy_r_r107);
    CPy_DECREF_NO_IMM(cpy_r_r90);
    CPy_DECREF_NO_IMM(cpy_r_r101);
    if (unlikely(cpy_r_r108 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 30, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r109 = PyList_New(3);
    if (unlikely(cpy_r_r109 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r110 = (CPyPtr)&((PyListObject *)cpy_r_r109)->ob_item;
    cpy_r_r111 = *(CPyPtr *)cpy_r_r110;
    *(PyObject * *)cpy_r_r111 = cpy_r_r51;
    cpy_r_r112 = cpy_r_r111 + 8;
    *(PyObject * *)cpy_r_r112 = cpy_r_r88;
    cpy_r_r113 = cpy_r_r111 + 16;
    *(PyObject * *)cpy_r_r113 = cpy_r_r108;
    cpy_r_r114 = CPyStatic_globals;
    cpy_r_r115 = CPyStatics[24]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_ABI' */
    cpy_r_r116 = CPyDict_SetItem(cpy_r_r114, cpy_r_r115, cpy_r_r109);
    CPy_DECREF_NO_IMM(cpy_r_r109);
    cpy_r_r117 = cpy_r_r116 >= 0;
    if (unlikely(!cpy_r_r117)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r118 = CPyStatics[25]; /* 'bytecode' */
    cpy_r_r119 = CPyStatic_globals;
    cpy_r_r120 = CPyStatics[5]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r121 = CPyDict_GetItem(cpy_r_r119, cpy_r_r120);
    if (unlikely(cpy_r_r121 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL32;
    }
    if (likely(PyUnicode_Check(cpy_r_r121)))
        cpy_r_r122 = cpy_r_r121;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 39, CPyStatic_globals, "str", cpy_r_r121);
        goto CPyL32;
    }
    cpy_r_r123 = CPyStatics[26]; /* 'bytecode_runtime' */
    cpy_r_r124 = CPyStatic_globals;
    cpy_r_r125 = CPyStatics[7]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r126 = CPyDict_GetItem(cpy_r_r124, cpy_r_r125);
    if (unlikely(cpy_r_r126 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 40, CPyStatic_globals);
        goto CPyL46;
    }
    if (likely(PyUnicode_Check(cpy_r_r126)))
        cpy_r_r127 = cpy_r_r126;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 40, CPyStatic_globals, "str", cpy_r_r126);
        goto CPyL46;
    }
    cpy_r_r128 = CPyStatics[27]; /* 'abi' */
    cpy_r_r129 = CPyStatic_globals;
    cpy_r_r130 = CPyStatics[24]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_ABI' */
    cpy_r_r131 = CPyDict_GetItem(cpy_r_r129, cpy_r_r130);
    if (unlikely(cpy_r_r131 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL47;
    }
    if (likely(PyList_Check(cpy_r_r131)))
        cpy_r_r132 = cpy_r_r131;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 41, CPyStatic_globals, "list", cpy_r_r131);
        goto CPyL47;
    }
    cpy_r_r133 = CPyDict_Build(3, cpy_r_r118, cpy_r_r122, cpy_r_r123, cpy_r_r127, cpy_r_r128, cpy_r_r132);
    CPy_DECREF(cpy_r_r122);
    CPy_DECREF(cpy_r_r127);
    CPy_DECREF_NO_IMM(cpy_r_r132);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r134 = CPyStatic_globals;
    cpy_r_r135 = CPyStatics[28]; /* 'AMBIGUOUS_FUNCTION_CONTRACT_DATA' */
    cpy_r_r136 = CPyDict_SetItem(cpy_r_r134, cpy_r_r135, cpy_r_r133);
    CPy_DECREF(cpy_r_r133);
    cpy_r_r137 = cpy_r_r136 >= 0;
    if (unlikely(!cpy_r_r137)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/ambiguous_function_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL32;
    }
    return 1;
CPyL32: ;
    cpy_r_r138 = 2;
    return cpy_r_r138;
CPyL33: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL32;
CPyL34: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    goto CPyL32;
CPyL35: ;
    CPy_DecRef(cpy_r_r30);
    goto CPyL32;
CPyL36: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r43);
    goto CPyL32;
CPyL37: ;
    CPy_DecRef(cpy_r_r51);
    goto CPyL32;
CPyL38: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r59);
    goto CPyL32;
CPyL39: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r66);
    goto CPyL32;
CPyL40: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r67);
    goto CPyL32;
CPyL41: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r67);
    CPy_DecRef(cpy_r_r80);
    goto CPyL32;
CPyL42: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r88);
    goto CPyL32;
CPyL43: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r90);
    goto CPyL32;
CPyL44: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r90);
    CPy_DecRef(cpy_r_r100);
    goto CPyL32;
CPyL45: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r108);
    goto CPyL32;
CPyL46: ;
    CPy_DecRef(cpy_r_r122);
    goto CPyL32;
CPyL47: ;
    CPy_DecRef(cpy_r_r122);
    CPy_DecRef(cpy_r_r127);
    goto CPyL32;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[29];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\221N0x6080604052348015600e575f5ffd5b5061044a8061001c5f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c80631626ba7e1461004357806320c13b0b14610073578063d482bb47146100a3575b5f5ffd5b61005d60048036038101906100589190610293565b6100c1565b60405161006a9190610305565b60405180910390f35b61008d6004803603810190610088919061031e565b6100cb565b60405161009a9190610305565b60405180910390f35b6100ab6100d6565b6040516100b891906103f4565b60405180910390f35b5f5f905092915050565b5f6001905092915050565b60606040518060400160405280600581526020017f76616c6964000000000000000000000000000000000000000000000000000000815250905090565b5f604051905090565b5f5ffd5b5f5ffd5b5f819050919050565b61013681610124565b8114610140575f5ffd5b50565b5f813590506101518161012d565b92915050565b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101a58261015f565b810181811067ffffffffffffffff821117156101c4576101c361016f565b5b80604052505050565b5f6101d6610113565b90506101e2828261019c565b919050565b5f67ffffffffffffffff8211156102015761020061016f565b5b61020a8261015f565b9050602081019050919050565b828183375f83830152505050565b5f610237610232846101e7565b6101cd565b9050828152602081018484840111156102535761025261015b565b5b61025e848285610217565b509392505050565b5f82601f83011261027a57610279610157565b5b813561028a848260208601610225565b91505092915050565b5f5f604083850312156102a9576102a861011c565b5b5f6102b685828601610143565b925050602083013567ffffffffffffffff8111156102d7576102d6610120565b5b6102e385828601610266565b9150509250929050565b5f819050919050565b6102ff816102ed565b82525050565b5f6020820190506103185f8301846102f6565b92915050565b5f5f604083850312156103345761033361011c565b5b5f83013567ffffffffffffffff81111561035157610350610120565b5b61035d85828601610266565b925050602083013567ffffffffffffffff81111561037e5761037d610120565b5b61038a85828601610266565b9150509250929050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6103c682610394565b6103d0818561039e565b93506103e08185602086016103ae565b6103e98161015f565b840191505092915050565b5f6020820190508181035f83015261040c81846103bc565b90509291505056fea26469706673582212207771e80e03817222551c15a244685f02dd958991f78b46e6373f839b286c0be264736f6c634300081e0033",
    "\001$AMBIGUOUS_FUNCTION_CONTRACT_BYTECODE",
    "\001\221\0260x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c80631626ba7e1461004357806320c13b0b14610073578063d482bb47146100a3575b5f5ffd5b61005d60048036038101906100589190610293565b6100c1565b60405161006a9190610305565b60405180910390f35b61008d6004803603810190610088919061031e565b6100cb565b60405161009a9190610305565b60405180910390f35b6100ab6100d6565b6040516100b891906103f4565b60405180910390f35b5f5f905092915050565b5f6001905092915050565b60606040518060400160405280600581526020017f76616c6964000000000000000000000000000000000000000000000000000000815250905090565b5f604051905090565b5f5ffd5b5f5ffd5b5f819050919050565b61013681610124565b8114610140575f5ffd5b50565b5f813590506101518161012d565b92915050565b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6101a58261015f565b810181811067ffffffffffffffff821117156101c4576101c361016f565b5b80604052505050565b5f6101d6610113565b90506101e2828261019c565b919050565b5f67ffffffffffffffff8211156102015761020061016f565b5b61020a8261015f565b9050602081019050919050565b828183375f83830152505050565b5f610237610232846101e7565b6101cd565b9050828152602081018484840111156102535761025261015b565b5b61025e848285610217565b509392505050565b5f82601f83011261027a57610279610157565b5b813561028a848260208601610225565b91505092915050565b5f5f604083850312156102a9576102a861011c565b5b5f6102b685828601610143565b925050602083013567ffffffffffffffff8111156102d7576102d6610120565b5b6102e385828601610266565b9150509250929050565b5f819050919050565b6102ff816102ed565b82525050565b5f6020820190506103185f8301846102f6565b92915050565b5f5f604083850312156103345761033361011c565b5b5f83013567ffffffffffffffff81111561035157610350610120565b5b61035d85828601610266565b925050602083013567ffffffffffffffff81111561037e5761037d610120565b5b61038a85828601610266565b9150509250929050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6103c682610394565b6103d0818561039e565b93506103e08185602086016103ae565b6103e98161015f565b840191505092915050565b5f6020820190508181035f83015261040c81846103bc565b90509291505056fea26469706673582212207771e80e03817222551c15a244685f02dd958991f78b46e6373f839b286c0be264736f6c634300081e0033",
    "\005#AMBIGUOUS_FUNCTION_CONTRACT_RUNTIME\006inputs\finternalType\abytes32\004name",
    "\b\amessage\004type\005bytes\tsignature\020isValidSignature\aoutputs\auint256\006result",
    "\005\017stateMutability\004view\bfunction\006string\037AMBIGUOUS_FUNCTION_CONTRACT_ABI",
    "\004\bbytecode\020bytecode_runtime\003abi AMBIGUOUS_FUNCTION_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_ambiguous_function_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract, "faster_web3._utils.contract_sources.contract_data.ambiguous_function_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___ambiguous_function_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_ambiguous_function_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.ambiguous_function_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_ambiguous_function_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_ambiguous_function_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_ambiguous_function_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
