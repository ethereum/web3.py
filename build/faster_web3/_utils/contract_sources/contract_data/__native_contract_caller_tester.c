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
#include "__native_contract_caller_tester.h"
#include "__native_internal_contract_caller_tester.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___contract_caller_tester(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.contract_caller_tester",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___contract_caller_tester(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___contract_caller_tester(CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal;
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
    CPyPtr cpy_r_r65;
    CPyPtr cpy_r_r66;
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
    PyObject *cpy_r_r81;
    PyObject *cpy_r_r82;
    PyObject *cpy_r_r83;
    PyObject *cpy_r_r84;
    CPyPtr cpy_r_r85;
    CPyPtr cpy_r_r86;
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
    PyObject *cpy_r_r103;
    PyObject *cpy_r_r104;
    CPyPtr cpy_r_r105;
    CPyPtr cpy_r_r106;
    PyObject *cpy_r_r107;
    PyObject *cpy_r_r108;
    PyObject *cpy_r_r109;
    PyObject *cpy_r_r110;
    PyObject *cpy_r_r111;
    PyObject *cpy_r_r112;
    PyObject *cpy_r_r113;
    PyObject *cpy_r_r114;
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
    PyObject *cpy_r_r133;
    PyObject *cpy_r_r134;
    PyObject *cpy_r_r135;
    PyObject *cpy_r_r136;
    PyObject *cpy_r_r137;
    PyObject *cpy_r_r138;
    PyObject *cpy_r_r139;
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
    PyObject *cpy_r_r150;
    PyObject *cpy_r_r151;
    PyObject *cpy_r_r152;
    CPyPtr cpy_r_r153;
    CPyPtr cpy_r_r154;
    CPyPtr cpy_r_r155;
    CPyPtr cpy_r_r156;
    CPyPtr cpy_r_r157;
    CPyPtr cpy_r_r158;
    PyObject *cpy_r_r159;
    PyObject *cpy_r_r160;
    PyObject *cpy_r_r161;
    PyObject *cpy_r_r162;
    PyObject *cpy_r_r163;
    PyObject *cpy_r_r164;
    CPyPtr cpy_r_r165;
    CPyPtr cpy_r_r166;
    CPyPtr cpy_r_r167;
    CPyPtr cpy_r_r168;
    CPyPtr cpy_r_r169;
    CPyPtr cpy_r_r170;
    PyObject *cpy_r_r171;
    PyObject *cpy_r_r172;
    int32_t cpy_r_r173;
    char cpy_r_r174;
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
    PyObject *cpy_r_r190;
    PyObject *cpy_r_r191;
    PyObject *cpy_r_r192;
    int32_t cpy_r_r193;
    char cpy_r_r194;
    char cpy_r_r195;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", -1, CPyStatic_globals);
        goto CPyL42;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b506104188061001c5f395ff3fe608060405260043610610049575f3560e01c806306661abd1461004d57806361bc221a14610077578063a5f3c23b14610095578063c7fa7d66146100c5578063d09de08a146100e7575b5f5ffd5b348015610058575f5ffd5b50610061610111565b60405161006e91906101d0565b60405180910390f35b61007f610116565b60405161008c91906101d0565b60405180910390f35b6100af60048036038101906100aa9190610217565b61011e565b6040516100bc91906101d0565b60405180910390f35b6100cd610133565b6040516100de95949392919061031c565b60405180910390f35b3480156100f2575f5ffd5b506100fb61019b565b60405161010891906101d0565b60405180910390f35b5f5481565b5f5f54905090565b5f818361012b91906103a1565b905092915050565b5f60605f5f5f335f365a344384848080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505093509091929350945094509450945094509091929394565b5f60015f5f8282546101ad91906103a1565b925050819055905090565b5f819050919050565b6101ca816101b8565b82525050565b5f6020820190506101e35f8301846101c1565b92915050565b5f5ffd5b6101f6816101b8565b8114610200575f5ffd5b50565b5f81359050610211816101ed565b92915050565b5f5f6040838503121561022d5761022c6101e9565b5b5f61023a85828601610203565b925050602061024b85828601610203565b9150509250929050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61027e82610255565b9050919050565b61028e81610274565b82525050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6102d682610294565b6102e0818561029e565b93506102f08185602086016102ae565b6102f9816102bc565b840191505092915050565b5f819050919050565b61031681610304565b82525050565b5f60a08201905061032f5f830188610285565b818103602083015261034181876102cc565b9050610350604083018661030d565b61035d606083018561030d565b61036a608083018461030d565b9695505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103ab826101b8565b91506103b6836101b8565b92508282019050828112155f8312168382125f8412151617156103dc576103db610374565b5b9291505056fea264697066735822122099d3d23538d14bd41a2c9185dc4a9a928014039b76eeda7e8afc81457bcfb5e064736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'CONTRACT_CALLER_TESTER_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 7, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405260043610610049575f3560e01c806306661abd1461004d57806361bc221a14610077578063a5f3c23b14610095578063c7fa7d66146100c5578063d09de08a146100e7575b5f5ffd5b348015610058575f5ffd5b50610061610111565b60405161006e91906101d0565b60405180910390f35b61007f610116565b60405161008c91906101d0565b60405180910390f35b6100af60048036038101906100aa9190610217565b61011e565b6040516100bc91906101d0565b60405180910390f35b6100cd610133565b6040516100de95949392919061031c565b60405180910390f35b3480156100f2575f5ffd5b506100fb61019b565b60405161010891906101d0565b60405180910390f35b5f5481565b5f5f54905090565b5f818361012b91906103a1565b905092915050565b5f60605f5f5f335f365a344384848080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505093509091929350945094509450945094509091929394565b5f60015f5f8282546101ad91906103a1565b925050819055905090565b5f819050919050565b6101ca816101b8565b82525050565b5f6020820190506101e35f8301846101c1565b92915050565b5f5ffd5b6101f6816101b8565b8114610200575f5ffd5b50565b5f81359050610211816101ed565b92915050565b5f5f6040838503121561022d5761022c6101e9565b5b5f61023a85828601610203565b925050602061024b85828601610203565b9150509250929050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61027e82610255565b9050919050565b61028e81610274565b82525050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6102d682610294565b6102e0818561029e565b93506102f08185602086016102ae565b6102f9816102bc565b840191505092915050565b5f819050919050565b61031681610304565b82525050565b5f60a08201905061032f5f830188610285565b818103602083015261034181876102cc565b9050610350604083018661030d565b61035d606083018561030d565b61036a608083018461030d565b9695505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103ab826101b8565b91506103b6836101b8565b92508282019050828112155f8312168382125f8412151617156103dc576103db610374565b5b9291505056fea264697066735822122099d3d23538d14bd41a2c9185dc4a9a928014039b76eeda7e8afc81457bcfb5e064736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'CONTRACT_CALLER_TESTER_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 8, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'int256' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* 'a' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'int256' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 12, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r23 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r24 = CPyStatics[10]; /* 'int256' */
    cpy_r_r25 = CPyStatics[11]; /* 'name' */
    cpy_r_r26 = CPyStatics[14]; /* 'b' */
    cpy_r_r27 = CPyStatics[13]; /* 'type' */
    cpy_r_r28 = CPyStatics[10]; /* 'int256' */
    cpy_r_r29 = CPyDict_Build(3, cpy_r_r23, cpy_r_r24, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 13, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r30 = PyList_New(2);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 11, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r31 = (CPyPtr)&((PyListObject *)cpy_r_r30)->ob_item;
    cpy_r_r32 = *(CPyPtr *)cpy_r_r31;
    *(PyObject * *)cpy_r_r32 = cpy_r_r22;
    cpy_r_r33 = cpy_r_r32 + 8;
    *(PyObject * *)cpy_r_r33 = cpy_r_r29;
    cpy_r_r34 = CPyStatics[11]; /* 'name' */
    cpy_r_r35 = CPyStatics[15]; /* 'add' */
    cpy_r_r36 = CPyStatics[16]; /* 'outputs' */
    cpy_r_r37 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r38 = CPyStatics[10]; /* 'int256' */
    cpy_r_r39 = CPyStatics[11]; /* 'name' */
    cpy_r_r40 = CPyStatics[17]; /* '' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[10]; /* 'int256' */
    cpy_r_r43 = CPyDict_Build(3, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 16, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r44 = PyList_New(1);
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 16, CPyStatic_globals);
        goto CPyL46;
    }
    cpy_r_r45 = (CPyPtr)&((PyListObject *)cpy_r_r44)->ob_item;
    cpy_r_r46 = *(CPyPtr *)cpy_r_r45;
    *(PyObject * *)cpy_r_r46 = cpy_r_r43;
    cpy_r_r47 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r48 = CPyStatics[19]; /* 'payable' */
    cpy_r_r49 = CPyStatics[13]; /* 'type' */
    cpy_r_r50 = CPyStatics[20]; /* 'function' */
    cpy_r_r51 = CPyDict_Build(5, cpy_r_r15, cpy_r_r30, cpy_r_r34, cpy_r_r35, cpy_r_r36, cpy_r_r44, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50);
    CPy_DECREF_NO_IMM(cpy_r_r30);
    CPy_DECREF_NO_IMM(cpy_r_r44);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 10, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r52 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r53 = PyList_New(0);
    if (unlikely(cpy_r_r53 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 21, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r54 = CPyStatics[11]; /* 'name' */
    cpy_r_r55 = CPyStatics[21]; /* 'count' */
    cpy_r_r56 = CPyStatics[16]; /* 'outputs' */
    cpy_r_r57 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r58 = CPyStatics[10]; /* 'int256' */
    cpy_r_r59 = CPyStatics[11]; /* 'name' */
    cpy_r_r60 = CPyStatics[17]; /* '' */
    cpy_r_r61 = CPyStatics[13]; /* 'type' */
    cpy_r_r62 = CPyStatics[10]; /* 'int256' */
    cpy_r_r63 = CPyDict_Build(3, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 23, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r64 = PyList_New(1);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 23, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r65 = (CPyPtr)&((PyListObject *)cpy_r_r64)->ob_item;
    cpy_r_r66 = *(CPyPtr *)cpy_r_r65;
    *(PyObject * *)cpy_r_r66 = cpy_r_r63;
    cpy_r_r67 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r68 = CPyStatics[22]; /* 'view' */
    cpy_r_r69 = CPyStatics[13]; /* 'type' */
    cpy_r_r70 = CPyStatics[20]; /* 'function' */
    cpy_r_r71 = CPyDict_Build(5, cpy_r_r52, cpy_r_r53, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r64, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70);
    CPy_DECREF_NO_IMM(cpy_r_r53);
    CPy_DECREF_NO_IMM(cpy_r_r64);
    if (unlikely(cpy_r_r71 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 20, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r72 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r73 = PyList_New(0);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 28, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r74 = CPyStatics[11]; /* 'name' */
    cpy_r_r75 = CPyStatics[23]; /* 'counter' */
    cpy_r_r76 = CPyStatics[16]; /* 'outputs' */
    cpy_r_r77 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r78 = CPyStatics[10]; /* 'int256' */
    cpy_r_r79 = CPyStatics[11]; /* 'name' */
    cpy_r_r80 = CPyStatics[17]; /* '' */
    cpy_r_r81 = CPyStatics[13]; /* 'type' */
    cpy_r_r82 = CPyStatics[10]; /* 'int256' */
    cpy_r_r83 = CPyDict_Build(3, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81, cpy_r_r82);
    if (unlikely(cpy_r_r83 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 30, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r84 = PyList_New(1);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 30, CPyStatic_globals);
        goto CPyL52;
    }
    cpy_r_r85 = (CPyPtr)&((PyListObject *)cpy_r_r84)->ob_item;
    cpy_r_r86 = *(CPyPtr *)cpy_r_r85;
    *(PyObject * *)cpy_r_r86 = cpy_r_r83;
    cpy_r_r87 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r88 = CPyStatics[19]; /* 'payable' */
    cpy_r_r89 = CPyStatics[13]; /* 'type' */
    cpy_r_r90 = CPyStatics[20]; /* 'function' */
    cpy_r_r91 = CPyDict_Build(5, cpy_r_r72, cpy_r_r73, cpy_r_r74, cpy_r_r75, cpy_r_r76, cpy_r_r84, cpy_r_r87, cpy_r_r88, cpy_r_r89, cpy_r_r90);
    CPy_DECREF_NO_IMM(cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r84);
    if (unlikely(cpy_r_r91 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 27, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r92 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r93 = PyList_New(0);
    if (unlikely(cpy_r_r93 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 35, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r94 = CPyStatics[11]; /* 'name' */
    cpy_r_r95 = CPyStatics[24]; /* 'increment' */
    cpy_r_r96 = CPyStatics[16]; /* 'outputs' */
    cpy_r_r97 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r98 = CPyStatics[10]; /* 'int256' */
    cpy_r_r99 = CPyStatics[11]; /* 'name' */
    cpy_r_r100 = CPyStatics[17]; /* '' */
    cpy_r_r101 = CPyStatics[13]; /* 'type' */
    cpy_r_r102 = CPyStatics[10]; /* 'int256' */
    cpy_r_r103 = CPyDict_Build(3, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101, cpy_r_r102);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 37, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r104 = PyList_New(1);
    if (unlikely(cpy_r_r104 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 37, CPyStatic_globals);
        goto CPyL55;
    }
    cpy_r_r105 = (CPyPtr)&((PyListObject *)cpy_r_r104)->ob_item;
    cpy_r_r106 = *(CPyPtr *)cpy_r_r105;
    *(PyObject * *)cpy_r_r106 = cpy_r_r103;
    cpy_r_r107 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r108 = CPyStatics[25]; /* 'nonpayable' */
    cpy_r_r109 = CPyStatics[13]; /* 'type' */
    cpy_r_r110 = CPyStatics[20]; /* 'function' */
    cpy_r_r111 = CPyDict_Build(5, cpy_r_r92, cpy_r_r93, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r104, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110);
    CPy_DECREF_NO_IMM(cpy_r_r93);
    CPy_DECREF_NO_IMM(cpy_r_r104);
    if (unlikely(cpy_r_r111 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 34, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r112 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r113 = PyList_New(0);
    if (unlikely(cpy_r_r113 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 42, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r114 = CPyStatics[11]; /* 'name' */
    cpy_r_r115 = CPyStatics[26]; /* 'returnMeta' */
    cpy_r_r116 = CPyStatics[16]; /* 'outputs' */
    cpy_r_r117 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r118 = CPyStatics[27]; /* 'address' */
    cpy_r_r119 = CPyStatics[11]; /* 'name' */
    cpy_r_r120 = CPyStatics[17]; /* '' */
    cpy_r_r121 = CPyStatics[13]; /* 'type' */
    cpy_r_r122 = CPyStatics[27]; /* 'address' */
    cpy_r_r123 = CPyDict_Build(3, cpy_r_r117, cpy_r_r118, cpy_r_r119, cpy_r_r120, cpy_r_r121, cpy_r_r122);
    if (unlikely(cpy_r_r123 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 45, CPyStatic_globals);
        goto CPyL57;
    }
    cpy_r_r124 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r125 = CPyStatics[28]; /* 'bytes' */
    cpy_r_r126 = CPyStatics[11]; /* 'name' */
    cpy_r_r127 = CPyStatics[17]; /* '' */
    cpy_r_r128 = CPyStatics[13]; /* 'type' */
    cpy_r_r129 = CPyStatics[28]; /* 'bytes' */
    cpy_r_r130 = CPyDict_Build(3, cpy_r_r124, cpy_r_r125, cpy_r_r126, cpy_r_r127, cpy_r_r128, cpy_r_r129);
    if (unlikely(cpy_r_r130 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 46, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r131 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r132 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r133 = CPyStatics[11]; /* 'name' */
    cpy_r_r134 = CPyStatics[17]; /* '' */
    cpy_r_r135 = CPyStatics[13]; /* 'type' */
    cpy_r_r136 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r137 = CPyDict_Build(3, cpy_r_r131, cpy_r_r132, cpy_r_r133, cpy_r_r134, cpy_r_r135, cpy_r_r136);
    if (unlikely(cpy_r_r137 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 47, CPyStatic_globals);
        goto CPyL59;
    }
    cpy_r_r138 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r139 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r140 = CPyStatics[11]; /* 'name' */
    cpy_r_r141 = CPyStatics[17]; /* '' */
    cpy_r_r142 = CPyStatics[13]; /* 'type' */
    cpy_r_r143 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r144 = CPyDict_Build(3, cpy_r_r138, cpy_r_r139, cpy_r_r140, cpy_r_r141, cpy_r_r142, cpy_r_r143);
    if (unlikely(cpy_r_r144 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 48, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r145 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r146 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r147 = CPyStatics[11]; /* 'name' */
    cpy_r_r148 = CPyStatics[17]; /* '' */
    cpy_r_r149 = CPyStatics[13]; /* 'type' */
    cpy_r_r150 = CPyStatics[29]; /* 'uint256' */
    cpy_r_r151 = CPyDict_Build(3, cpy_r_r145, cpy_r_r146, cpy_r_r147, cpy_r_r148, cpy_r_r149, cpy_r_r150);
    if (unlikely(cpy_r_r151 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 49, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r152 = PyList_New(5);
    if (unlikely(cpy_r_r152 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 44, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r153 = (CPyPtr)&((PyListObject *)cpy_r_r152)->ob_item;
    cpy_r_r154 = *(CPyPtr *)cpy_r_r153;
    *(PyObject * *)cpy_r_r154 = cpy_r_r123;
    cpy_r_r155 = cpy_r_r154 + 8;
    *(PyObject * *)cpy_r_r155 = cpy_r_r130;
    cpy_r_r156 = cpy_r_r154 + 16;
    *(PyObject * *)cpy_r_r156 = cpy_r_r137;
    cpy_r_r157 = cpy_r_r154 + 24;
    *(PyObject * *)cpy_r_r157 = cpy_r_r144;
    cpy_r_r158 = cpy_r_r154 + 32;
    *(PyObject * *)cpy_r_r158 = cpy_r_r151;
    cpy_r_r159 = CPyStatics[18]; /* 'stateMutability' */
    cpy_r_r160 = CPyStatics[19]; /* 'payable' */
    cpy_r_r161 = CPyStatics[13]; /* 'type' */
    cpy_r_r162 = CPyStatics[20]; /* 'function' */
    cpy_r_r163 = CPyDict_Build(5, cpy_r_r112, cpy_r_r113, cpy_r_r114, cpy_r_r115, cpy_r_r116, cpy_r_r152, cpy_r_r159, cpy_r_r160, cpy_r_r161, cpy_r_r162);
    CPy_DECREF_NO_IMM(cpy_r_r113);
    CPy_DECREF_NO_IMM(cpy_r_r152);
    if (unlikely(cpy_r_r163 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 41, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r164 = PyList_New(5);
    if (unlikely(cpy_r_r164 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 9, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r165 = (CPyPtr)&((PyListObject *)cpy_r_r164)->ob_item;
    cpy_r_r166 = *(CPyPtr *)cpy_r_r165;
    *(PyObject * *)cpy_r_r166 = cpy_r_r51;
    cpy_r_r167 = cpy_r_r166 + 8;
    *(PyObject * *)cpy_r_r167 = cpy_r_r71;
    cpy_r_r168 = cpy_r_r166 + 16;
    *(PyObject * *)cpy_r_r168 = cpy_r_r91;
    cpy_r_r169 = cpy_r_r166 + 24;
    *(PyObject * *)cpy_r_r169 = cpy_r_r111;
    cpy_r_r170 = cpy_r_r166 + 32;
    *(PyObject * *)cpy_r_r170 = cpy_r_r163;
    cpy_r_r171 = CPyStatic_globals;
    cpy_r_r172 = CPyStatics[30]; /* 'CONTRACT_CALLER_TESTER_ABI' */
    cpy_r_r173 = CPyDict_SetItem(cpy_r_r171, cpy_r_r172, cpy_r_r164);
    CPy_DECREF_NO_IMM(cpy_r_r164);
    cpy_r_r174 = cpy_r_r173 >= 0;
    if (unlikely(!cpy_r_r174)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 9, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r175 = CPyStatics[31]; /* 'bytecode' */
    cpy_r_r176 = CPyStatic_globals;
    cpy_r_r177 = CPyStatics[5]; /* 'CONTRACT_CALLER_TESTER_BYTECODE' */
    cpy_r_r178 = CPyDict_GetItem(cpy_r_r176, cpy_r_r177);
    if (unlikely(cpy_r_r178 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 56, CPyStatic_globals);
        goto CPyL42;
    }
    if (likely(PyUnicode_Check(cpy_r_r178)))
        cpy_r_r179 = cpy_r_r178;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 56, CPyStatic_globals, "str", cpy_r_r178);
        goto CPyL42;
    }
    cpy_r_r180 = CPyStatics[32]; /* 'bytecode_runtime' */
    cpy_r_r181 = CPyStatic_globals;
    cpy_r_r182 = CPyStatics[7]; /* 'CONTRACT_CALLER_TESTER_RUNTIME' */
    cpy_r_r183 = CPyDict_GetItem(cpy_r_r181, cpy_r_r182);
    if (unlikely(cpy_r_r183 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 57, CPyStatic_globals);
        goto CPyL64;
    }
    if (likely(PyUnicode_Check(cpy_r_r183)))
        cpy_r_r184 = cpy_r_r183;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 57, CPyStatic_globals, "str", cpy_r_r183);
        goto CPyL64;
    }
    cpy_r_r185 = CPyStatics[33]; /* 'abi' */
    cpy_r_r186 = CPyStatic_globals;
    cpy_r_r187 = CPyStatics[30]; /* 'CONTRACT_CALLER_TESTER_ABI' */
    cpy_r_r188 = CPyDict_GetItem(cpy_r_r186, cpy_r_r187);
    if (unlikely(cpy_r_r188 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 58, CPyStatic_globals);
        goto CPyL65;
    }
    if (likely(PyList_Check(cpy_r_r188)))
        cpy_r_r189 = cpy_r_r188;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 58, CPyStatic_globals, "list", cpy_r_r188);
        goto CPyL65;
    }
    cpy_r_r190 = CPyDict_Build(3, cpy_r_r175, cpy_r_r179, cpy_r_r180, cpy_r_r184, cpy_r_r185, cpy_r_r189);
    CPy_DECREF(cpy_r_r179);
    CPy_DECREF(cpy_r_r184);
    CPy_DECREF_NO_IMM(cpy_r_r189);
    if (unlikely(cpy_r_r190 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 55, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r191 = CPyStatic_globals;
    cpy_r_r192 = CPyStatics[34]; /* 'CONTRACT_CALLER_TESTER_DATA' */
    cpy_r_r193 = CPyDict_SetItem(cpy_r_r191, cpy_r_r192, cpy_r_r190);
    CPy_DECREF(cpy_r_r190);
    cpy_r_r194 = cpy_r_r193 >= 0;
    if (unlikely(!cpy_r_r194)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/contract_caller_tester.py", "<module>", 55, CPyStatic_globals);
        goto CPyL42;
    }
    return 1;
CPyL42: ;
    cpy_r_r195 = 2;
    return cpy_r_r195;
CPyL43: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL42;
CPyL44: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    goto CPyL42;
CPyL45: ;
    CPy_DecRef(cpy_r_r30);
    goto CPyL42;
CPyL46: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r43);
    goto CPyL42;
CPyL47: ;
    CPy_DecRef(cpy_r_r51);
    goto CPyL42;
CPyL48: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r53);
    goto CPyL42;
CPyL49: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r53);
    CPy_DecRef(cpy_r_r63);
    goto CPyL42;
CPyL50: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    goto CPyL42;
CPyL51: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r73);
    goto CPyL42;
CPyL52: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r73);
    CPy_DecRef(cpy_r_r83);
    goto CPyL42;
CPyL53: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    goto CPyL42;
CPyL54: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r93);
    goto CPyL42;
CPyL55: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r93);
    CPy_DecRef(cpy_r_r103);
    goto CPyL42;
CPyL56: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    goto CPyL42;
CPyL57: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    goto CPyL42;
CPyL58: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r123);
    goto CPyL42;
CPyL59: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r123);
    CPy_DecRef(cpy_r_r130);
    goto CPyL42;
CPyL60: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r123);
    CPy_DecRef(cpy_r_r130);
    CPy_DecRef(cpy_r_r137);
    goto CPyL42;
CPyL61: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r123);
    CPy_DecRef(cpy_r_r130);
    CPy_DecRef(cpy_r_r137);
    CPy_DecRef(cpy_r_r144);
    goto CPyL42;
CPyL62: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r123);
    CPy_DecRef(cpy_r_r130);
    CPy_DecRef(cpy_r_r137);
    CPy_DecRef(cpy_r_r144);
    CPy_DecRef(cpy_r_r151);
    goto CPyL42;
CPyL63: ;
    CPy_DecRef(cpy_r_r51);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r163);
    goto CPyL42;
CPyL64: ;
    CPy_DecRef(cpy_r_r179);
    goto CPyL42;
CPyL65: ;
    CPy_DecRef(cpy_r_r179);
    CPy_DecRef(cpy_r_r184);
    goto CPyL42;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[35];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\220j0x6080604052348015600e575f5ffd5b506104188061001c5f395ff3fe608060405260043610610049575f3560e01c806306661abd1461004d57806361bc221a14610077578063a5f3c23b14610095578063c7fa7d66146100c5578063d09de08a146100e7575b5f5ffd5b348015610058575f5ffd5b50610061610111565b60405161006e91906101d0565b60405180910390f35b61007f610116565b60405161008c91906101d0565b60405180910390f35b6100af60048036038101906100aa9190610217565b61011e565b6040516100bc91906101d0565b60405180910390f35b6100cd610133565b6040516100de95949392919061031c565b60405180910390f35b3480156100f2575f5ffd5b506100fb61019b565b60405161010891906101d0565b60405180910390f35b5f5481565b5f5f54905090565b5f818361012b91906103a1565b905092915050565b5f60605f5f5f335f365a344384848080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505093509091929350945094509450945094509091929394565b5f60015f5f8282546101ad91906103a1565b925050819055905090565b5f819050919050565b6101ca816101b8565b82525050565b5f6020820190506101e35f8301846101c1565b92915050565b5f5ffd5b6101f6816101b8565b8114610200575f5ffd5b50565b5f81359050610211816101ed565b92915050565b5f5f6040838503121561022d5761022c6101e9565b5b5f61023a85828601610203565b925050602061024b85828601610203565b9150509250929050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61027e82610255565b9050919050565b61028e81610274565b82525050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6102d682610294565b6102e0818561029e565b93506102f08185602086016102ae565b6102f9816102bc565b840191505092915050565b5f819050919050565b61031681610304565b82525050565b5f60a08201905061032f5f830188610285565b818103602083015261034181876102cc565b9050610350604083018661030d565b61035d606083018561030d565b61036a608083018461030d565b9695505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103ab826101b8565b91506103b6836101b8565b92508282019050828112155f8312168382125f8412151617156103dc576103db610374565b5b9291505056fea264697066735822122099d3d23538d14bd41a2c9185dc4a9a928014039b76eeda7e8afc81457bcfb5e064736f6c634300081e0033",
    "\001\037CONTRACT_CALLER_TESTER_BYTECODE",
    "\001\22020x608060405260043610610049575f3560e01c806306661abd1461004d57806361bc221a14610077578063a5f3c23b14610095578063c7fa7d66146100c5578063d09de08a146100e7575b5f5ffd5b348015610058575f5ffd5b50610061610111565b60405161006e91906101d0565b60405180910390f35b61007f610116565b60405161008c91906101d0565b60405180910390f35b6100af60048036038101906100aa9190610217565b61011e565b6040516100bc91906101d0565b60405180910390f35b6100cd610133565b6040516100de95949392919061031c565b60405180910390f35b3480156100f2575f5ffd5b506100fb61019b565b60405161010891906101d0565b60405180910390f35b5f5481565b5f5f54905090565b5f818361012b91906103a1565b905092915050565b5f60605f5f5f335f365a344384848080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505093509091929350945094509450945094509091929394565b5f60015f5f8282546101ad91906103a1565b925050819055905090565b5f819050919050565b6101ca816101b8565b82525050565b5f6020820190506101e35f8301846101c1565b92915050565b5f5ffd5b6101f6816101b8565b8114610200575f5ffd5b50565b5f81359050610211816101ed565b92915050565b5f5f6040838503121561022d5761022c6101e9565b5b5f61023a85828601610203565b925050602061024b85828601610203565b9150509250929050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61027e82610255565b9050919050565b61028e81610274565b82525050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6102d682610294565b6102e0818561029e565b93506102f08185602086016102ae565b6102f9816102bc565b840191505092915050565b5f819050919050565b61031681610304565b82525050565b5f60a08201905061032f5f830188610285565b818103602083015261034181876102cc565b9050610350604083018661030d565b61035d606083018561030d565b61036a608083018461030d565b9695505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103ab826101b8565b91506103b6836101b8565b92508282019050828112155f8312168382125f8412151617156103dc576103db610374565b5b9291505056fea264697066735822122099d3d23538d14bd41a2c9185dc4a9a928014039b76eeda7e8afc81457bcfb5e064736f6c634300081e0033",
    "\a\036CONTRACT_CALLER_TESTER_RUNTIME\006inputs\finternalType\006int256\004name\001a\004type",
    "\n\001b\003add\aoutputs\000\017stateMutability\apayable\bfunction\005count\004view\acounter",
    "\006\tincrement\nnonpayable\nreturnMeta\aaddress\005bytes\auint256",
    "\004\032CONTRACT_CALLER_TESTER_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\033CONTRACT_CALLER_TESTER_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___contract_caller_tester;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_contract_caller_tester__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___contract_caller_tester(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___contract_caller_tester, "faster_web3._utils.contract_sources.contract_data.contract_caller_tester__mypyc.init_faster_web3____utils___contract_sources___contract_data___contract_caller_tester", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___contract_caller_tester", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_contract_caller_tester__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.contract_caller_tester__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_contract_caller_tester__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_contract_caller_tester__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_contract_caller_tester__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
