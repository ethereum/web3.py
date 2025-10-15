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
#include "__native_math_contract.h"
#include "__native_internal_math_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___math_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.math_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___math_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___math_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal;
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
    CPyPtr cpy_r_r27;
    CPyPtr cpy_r_r28;
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
    PyObject *cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    CPyPtr cpy_r_r51;
    CPyPtr cpy_r_r52;
    CPyPtr cpy_r_r53;
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
    CPyPtr cpy_r_r121;
    CPyPtr cpy_r_r122;
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
    CPyPtr cpy_r_r134;
    CPyPtr cpy_r_r135;
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
    CPyPtr cpy_r_r150;
    CPyPtr cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
    PyObject *cpy_r_r155;
    PyObject *cpy_r_r156;
    PyObject *cpy_r_r157;
    PyObject *cpy_r_r158;
    PyObject *cpy_r_r159;
    PyObject *cpy_r_r160;
    PyObject *cpy_r_r161;
    PyObject *cpy_r_r162;
    CPyPtr cpy_r_r163;
    CPyPtr cpy_r_r164;
    PyObject *cpy_r_r165;
    PyObject *cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject *cpy_r_r168;
    PyObject *cpy_r_r169;
    PyObject *cpy_r_r170;
    PyObject *cpy_r_r171;
    PyObject *cpy_r_r172;
    PyObject *cpy_r_r173;
    PyObject *cpy_r_r174;
    PyObject *cpy_r_r175;
    PyObject *cpy_r_r176;
    PyObject *cpy_r_r177;
    PyObject *cpy_r_r178;
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
    CPyPtr cpy_r_r191;
    CPyPtr cpy_r_r192;
    CPyPtr cpy_r_r193;
    CPyPtr cpy_r_r194;
    CPyPtr cpy_r_r195;
    CPyPtr cpy_r_r196;
    CPyPtr cpy_r_r197;
    CPyPtr cpy_r_r198;
    PyObject *cpy_r_r199;
    PyObject *cpy_r_r200;
    int32_t cpy_r_r201;
    char cpy_r_r202;
    PyObject *cpy_r_r203;
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
    PyObject *cpy_r_r214;
    PyObject *cpy_r_r215;
    PyObject *cpy_r_r216;
    PyObject *cpy_r_r217;
    PyObject *cpy_r_r218;
    PyObject *cpy_r_r219;
    PyObject *cpy_r_r220;
    int32_t cpy_r_r221;
    char cpy_r_r222;
    char cpy_r_r223;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL47;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x60806040525f5f553480156011575f5ffd5b5061052d8061001f5f395ff3fe608060405260043610610054575f3560e01c806316216f39146100585780635b34b9661461008257806361bc221a146100a05780636abbb3b4146100ca578063a5f3c23b146100fa578063dcf537b11461012a575b5f5ffd5b348015610063575f5ffd5b5061006c61015a565b604051610079919061024f565b60405180910390f35b61008a610162565b6040516100979190610280565b60405180910390f35b3480156100ab575f5ffd5b506100b46101b5565b6040516100c19190610280565b60405180910390f35b6100e460048036038101906100df91906102c7565b6101ba565b6040516100f19190610280565b60405180910390f35b610114600480360381019061010f919061031c565b61020d565b604051610121919061024f565b60405180910390f35b610144600480360381019061013f919061035a565b610222565b604051610151919061024f565b60405180910390f35b5f600d905090565b5f60015f5461017191906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c560016040516101a69190610427565b60405180910390a15f54905090565b5f5481565b5f815f546101c891906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5826040516101fc9190610280565b60405180910390a15f549050919050565b5f818361021a9190610440565b905092915050565b5f6007826102309190610481565b9050919050565b5f819050919050565b61024981610237565b82525050565b5f6020820190506102625f830184610240565b92915050565b5f819050919050565b61027a81610268565b82525050565b5f6020820190506102935f830184610271565b92915050565b5f5ffd5b6102a681610268565b81146102b0575f5ffd5b50565b5f813590506102c18161029d565b92915050565b5f602082840312156102dc576102db610299565b5b5f6102e9848285016102b3565b91505092915050565b6102fb81610237565b8114610305575f5ffd5b50565b5f81359050610316816102f2565b92915050565b5f5f6040838503121561033257610331610299565b5b5f61033f85828601610308565b925050602061035085828601610308565b9150509250929050565b5f6020828403121561036f5761036e610299565b5b5f61037c84828501610308565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103bc82610268565b91506103c783610268565b92508282019050808211156103df576103de610385565b5b92915050565b5f819050919050565b5f819050919050565b5f61041161040c610407846103e5565b6103ee565b610268565b9050919050565b610421816103f7565b82525050565b5f60208201905061043a5f830184610418565b92915050565b5f61044a82610237565b915061045583610237565b92508282019050828112155f8312168382125f84121516171561047b5761047a610385565b5b92915050565b5f61048b82610237565b915061049683610237565b92508282026104a481610237565b91507f800000000000000000000000000000000000000000000000000000000000000084145f841216156104db576104da610385565b5b82820584148315176104f0576104ef610385565b5b509291505056fea264697066735822122011a65cebc9a2456d3d12ae6d239cb90e576295a155544d2515af1db2cdc5c71a64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'MATH_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405260043610610054575f3560e01c806316216f39146100585780635b34b9661461008257806361bc221a146100a05780636abbb3b4146100ca578063a5f3c23b146100fa578063dcf537b11461012a575b5f5ffd5b348015610063575f5ffd5b5061006c61015a565b604051610079919061024f565b60405180910390f35b61008a610162565b6040516100979190610280565b60405180910390f35b3480156100ab575f5ffd5b506100b46101b5565b6040516100c19190610280565b60405180910390f35b6100e460048036038101906100df91906102c7565b6101ba565b6040516100f19190610280565b60405180910390f35b610114600480360381019061010f919061031c565b61020d565b604051610121919061024f565b60405180910390f35b610144600480360381019061013f919061035a565b610222565b604051610151919061024f565b60405180910390f35b5f600d905090565b5f60015f5461017191906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c560016040516101a69190610427565b60405180910390a15f54905090565b5f5481565b5f815f546101c891906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5826040516101fc9190610280565b60405180910390a15f549050919050565b5f818361021a9190610440565b905092915050565b5f6007826102309190610481565b9050919050565b5f819050919050565b61024981610237565b82525050565b5f6020820190506102625f830184610240565b92915050565b5f819050919050565b61027a81610268565b82525050565b5f6020820190506102935f830184610271565b92915050565b5f5ffd5b6102a681610268565b81146102b0575f5ffd5b50565b5f813590506102c18161029d565b92915050565b5f602082840312156102dc576102db610299565b5b5f6102e9848285016102b3565b91505092915050565b6102fb81610237565b8114610305575f5ffd5b50565b5f81359050610316816102f2565b92915050565b5f5f6040838503121561033257610331610299565b5b5f61033f85828601610308565b925050602061035085828601610308565b9150509250929050565b5f6020828403121561036f5761036e610299565b5b5f61037c84828501610308565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103bc82610268565b91506103c783610268565b92508282019050808211156103df576103de610385565b5b92915050565b5f819050919050565b5f819050919050565b5f61041161040c610407846103e5565b6103ee565b610268565b9050919050565b610421816103f7565b82525050565b5f60208201905061043a5f830184610418565b92915050565b5f61044a82610237565b915061045583610237565b92508282019050828112155f8312168382125f84121516171561047b5761047a610385565b5b92915050565b5f61048b82610237565b915061049683610237565b92508282026104a481610237565b91507f800000000000000000000000000000000000000000000000000000000000000084145f841216156104db576104da610385565b5b82820584148315176104f0576104ef610385565b5b509291505056fea264697066735822122011a65cebc9a2456d3d12ae6d239cb90e576295a155544d2515af1db2cdc5c71a64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'MATH_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r16 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r17 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r18 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r19 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r20 = CPyStatics[13]; /* 'name' */
    cpy_r_r21 = CPyStatics[14]; /* 'value' */
    cpy_r_r22 = CPyStatics[15]; /* 'type' */
    cpy_r_r23 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r24 = 0 ? Py_True : Py_False;
    cpy_r_r25 = CPyDict_Build(4, cpy_r_r17, cpy_r_r24, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r26 = PyList_New(1);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 12, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r27 = (CPyPtr)&((PyListObject *)cpy_r_r26)->ob_item;
    cpy_r_r28 = *(CPyPtr *)cpy_r_r27;
    *(PyObject * *)cpy_r_r28 = cpy_r_r25;
    cpy_r_r29 = CPyStatics[13]; /* 'name' */
    cpy_r_r30 = CPyStatics[16]; /* 'Increased' */
    cpy_r_r31 = CPyStatics[15]; /* 'type' */
    cpy_r_r32 = CPyStatics[17]; /* 'event' */
    cpy_r_r33 = 0 ? Py_True : Py_False;
    cpy_r_r34 = CPyDict_Build(4, cpy_r_r15, cpy_r_r33, cpy_r_r16, cpy_r_r26, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32);
    CPy_DECREF_NO_IMM(cpy_r_r26);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r35 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r36 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r37 = CPyStatics[18]; /* 'int256' */
    cpy_r_r38 = CPyStatics[13]; /* 'name' */
    cpy_r_r39 = CPyStatics[19]; /* 'a' */
    cpy_r_r40 = CPyStatics[15]; /* 'type' */
    cpy_r_r41 = CPyStatics[18]; /* 'int256' */
    cpy_r_r42 = CPyDict_Build(3, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41);
    if (unlikely(cpy_r_r42 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r43 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r44 = CPyStatics[18]; /* 'int256' */
    cpy_r_r45 = CPyStatics[13]; /* 'name' */
    cpy_r_r46 = CPyStatics[20]; /* 'b' */
    cpy_r_r47 = CPyStatics[15]; /* 'type' */
    cpy_r_r48 = CPyStatics[18]; /* 'int256' */
    cpy_r_r49 = CPyDict_Build(3, cpy_r_r43, cpy_r_r44, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48);
    if (unlikely(cpy_r_r49 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r50 = PyList_New(2);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 24, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r51 = (CPyPtr)&((PyListObject *)cpy_r_r50)->ob_item;
    cpy_r_r52 = *(CPyPtr *)cpy_r_r51;
    *(PyObject * *)cpy_r_r52 = cpy_r_r42;
    cpy_r_r53 = cpy_r_r52 + 8;
    *(PyObject * *)cpy_r_r53 = cpy_r_r49;
    cpy_r_r54 = CPyStatics[13]; /* 'name' */
    cpy_r_r55 = CPyStatics[21]; /* 'add' */
    cpy_r_r56 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r57 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r58 = CPyStatics[18]; /* 'int256' */
    cpy_r_r59 = CPyStatics[13]; /* 'name' */
    cpy_r_r60 = CPyStatics[23]; /* 'result' */
    cpy_r_r61 = CPyStatics[15]; /* 'type' */
    cpy_r_r62 = CPyStatics[18]; /* 'int256' */
    cpy_r_r63 = CPyDict_Build(3, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 29, CPyStatic_globals);
        goto CPyL52;
    }
    cpy_r_r64 = PyList_New(1);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 29, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r65 = (CPyPtr)&((PyListObject *)cpy_r_r64)->ob_item;
    cpy_r_r66 = *(CPyPtr *)cpy_r_r65;
    *(PyObject * *)cpy_r_r66 = cpy_r_r63;
    cpy_r_r67 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r68 = CPyStatics[25]; /* 'payable' */
    cpy_r_r69 = CPyStatics[15]; /* 'type' */
    cpy_r_r70 = CPyStatics[26]; /* 'function' */
    cpy_r_r71 = CPyDict_Build(5, cpy_r_r35, cpy_r_r50, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r64, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70);
    CPy_DECREF_NO_IMM(cpy_r_r50);
    CPy_DECREF_NO_IMM(cpy_r_r64);
    if (unlikely(cpy_r_r71 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 23, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r72 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r73 = PyList_New(0);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 34, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r74 = CPyStatics[13]; /* 'name' */
    cpy_r_r75 = CPyStatics[27]; /* 'counter' */
    cpy_r_r76 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r77 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r78 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r79 = CPyStatics[13]; /* 'name' */
    cpy_r_r80 = CPyStatics[28]; /* '' */
    cpy_r_r81 = CPyStatics[15]; /* 'type' */
    cpy_r_r82 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r83 = CPyDict_Build(3, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81, cpy_r_r82);
    if (unlikely(cpy_r_r83 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 36, CPyStatic_globals);
        goto CPyL55;
    }
    cpy_r_r84 = PyList_New(1);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 36, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r85 = (CPyPtr)&((PyListObject *)cpy_r_r84)->ob_item;
    cpy_r_r86 = *(CPyPtr *)cpy_r_r85;
    *(PyObject * *)cpy_r_r86 = cpy_r_r83;
    cpy_r_r87 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r88 = CPyStatics[29]; /* 'view' */
    cpy_r_r89 = CPyStatics[15]; /* 'type' */
    cpy_r_r90 = CPyStatics[26]; /* 'function' */
    cpy_r_r91 = CPyDict_Build(5, cpy_r_r72, cpy_r_r73, cpy_r_r74, cpy_r_r75, cpy_r_r76, cpy_r_r84, cpy_r_r87, cpy_r_r88, cpy_r_r89, cpy_r_r90);
    CPy_DECREF_NO_IMM(cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r84);
    if (unlikely(cpy_r_r91 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r92 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r93 = PyList_New(0);
    if (unlikely(cpy_r_r93 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL57;
    }
    cpy_r_r94 = CPyStatics[13]; /* 'name' */
    cpy_r_r95 = CPyStatics[30]; /* 'incrementCounter' */
    cpy_r_r96 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r97 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r98 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r99 = CPyStatics[13]; /* 'name' */
    cpy_r_r100 = CPyStatics[23]; /* 'result' */
    cpy_r_r101 = CPyStatics[15]; /* 'type' */
    cpy_r_r102 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r103 = CPyDict_Build(3, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101, cpy_r_r102);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 43, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r104 = PyList_New(1);
    if (unlikely(cpy_r_r104 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 43, CPyStatic_globals);
        goto CPyL59;
    }
    cpy_r_r105 = (CPyPtr)&((PyListObject *)cpy_r_r104)->ob_item;
    cpy_r_r106 = *(CPyPtr *)cpy_r_r105;
    *(PyObject * *)cpy_r_r106 = cpy_r_r103;
    cpy_r_r107 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r108 = CPyStatics[25]; /* 'payable' */
    cpy_r_r109 = CPyStatics[15]; /* 'type' */
    cpy_r_r110 = CPyStatics[26]; /* 'function' */
    cpy_r_r111 = CPyDict_Build(5, cpy_r_r92, cpy_r_r93, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r104, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110);
    CPy_DECREF_NO_IMM(cpy_r_r93);
    CPy_DECREF_NO_IMM(cpy_r_r104);
    if (unlikely(cpy_r_r111 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 40, CPyStatic_globals);
        goto CPyL57;
    }
    cpy_r_r112 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r113 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r114 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r115 = CPyStatics[13]; /* 'name' */
    cpy_r_r116 = CPyStatics[31]; /* 'amount' */
    cpy_r_r117 = CPyStatics[15]; /* 'type' */
    cpy_r_r118 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r119 = CPyDict_Build(3, cpy_r_r113, cpy_r_r114, cpy_r_r115, cpy_r_r116, cpy_r_r117, cpy_r_r118);
    if (unlikely(cpy_r_r119 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r120 = PyList_New(1);
    if (unlikely(cpy_r_r120 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r121 = (CPyPtr)&((PyListObject *)cpy_r_r120)->ob_item;
    cpy_r_r122 = *(CPyPtr *)cpy_r_r121;
    *(PyObject * *)cpy_r_r122 = cpy_r_r119;
    cpy_r_r123 = CPyStatics[13]; /* 'name' */
    cpy_r_r124 = CPyStatics[30]; /* 'incrementCounter' */
    cpy_r_r125 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r126 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r127 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r128 = CPyStatics[13]; /* 'name' */
    cpy_r_r129 = CPyStatics[23]; /* 'result' */
    cpy_r_r130 = CPyStatics[15]; /* 'type' */
    cpy_r_r131 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r132 = CPyDict_Build(3, cpy_r_r126, cpy_r_r127, cpy_r_r128, cpy_r_r129, cpy_r_r130, cpy_r_r131);
    if (unlikely(cpy_r_r132 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 50, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r133 = PyList_New(1);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 50, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r134 = (CPyPtr)&((PyListObject *)cpy_r_r133)->ob_item;
    cpy_r_r135 = *(CPyPtr *)cpy_r_r134;
    *(PyObject * *)cpy_r_r135 = cpy_r_r132;
    cpy_r_r136 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r137 = CPyStatics[25]; /* 'payable' */
    cpy_r_r138 = CPyStatics[15]; /* 'type' */
    cpy_r_r139 = CPyStatics[26]; /* 'function' */
    cpy_r_r140 = CPyDict_Build(5, cpy_r_r112, cpy_r_r120, cpy_r_r123, cpy_r_r124, cpy_r_r125, cpy_r_r133, cpy_r_r136, cpy_r_r137, cpy_r_r138, cpy_r_r139);
    CPy_DECREF_NO_IMM(cpy_r_r120);
    CPy_DECREF_NO_IMM(cpy_r_r133);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 47, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r141 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r142 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r143 = CPyStatics[18]; /* 'int256' */
    cpy_r_r144 = CPyStatics[13]; /* 'name' */
    cpy_r_r145 = CPyStatics[19]; /* 'a' */
    cpy_r_r146 = CPyStatics[15]; /* 'type' */
    cpy_r_r147 = CPyStatics[18]; /* 'int256' */
    cpy_r_r148 = CPyDict_Build(3, cpy_r_r142, cpy_r_r143, cpy_r_r144, cpy_r_r145, cpy_r_r146, cpy_r_r147);
    if (unlikely(cpy_r_r148 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 55, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r149 = PyList_New(1);
    if (unlikely(cpy_r_r149 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 55, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r150 = (CPyPtr)&((PyListObject *)cpy_r_r149)->ob_item;
    cpy_r_r151 = *(CPyPtr *)cpy_r_r150;
    *(PyObject * *)cpy_r_r151 = cpy_r_r148;
    cpy_r_r152 = CPyStatics[13]; /* 'name' */
    cpy_r_r153 = CPyStatics[32]; /* 'multiply7' */
    cpy_r_r154 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r155 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r156 = CPyStatics[18]; /* 'int256' */
    cpy_r_r157 = CPyStatics[13]; /* 'name' */
    cpy_r_r158 = CPyStatics[23]; /* 'result' */
    cpy_r_r159 = CPyStatics[15]; /* 'type' */
    cpy_r_r160 = CPyStatics[18]; /* 'int256' */
    cpy_r_r161 = CPyDict_Build(3, cpy_r_r155, cpy_r_r156, cpy_r_r157, cpy_r_r158, cpy_r_r159, cpy_r_r160);
    if (unlikely(cpy_r_r161 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 57, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r162 = PyList_New(1);
    if (unlikely(cpy_r_r162 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 57, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r163 = (CPyPtr)&((PyListObject *)cpy_r_r162)->ob_item;
    cpy_r_r164 = *(CPyPtr *)cpy_r_r163;
    *(PyObject * *)cpy_r_r164 = cpy_r_r161;
    cpy_r_r165 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r166 = CPyStatics[25]; /* 'payable' */
    cpy_r_r167 = CPyStatics[15]; /* 'type' */
    cpy_r_r168 = CPyStatics[26]; /* 'function' */
    cpy_r_r169 = CPyDict_Build(5, cpy_r_r141, cpy_r_r149, cpy_r_r152, cpy_r_r153, cpy_r_r154, cpy_r_r162, cpy_r_r165, cpy_r_r166, cpy_r_r167, cpy_r_r168);
    CPy_DECREF_NO_IMM(cpy_r_r149);
    CPy_DECREF_NO_IMM(cpy_r_r162);
    if (unlikely(cpy_r_r169 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 54, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r170 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r171 = PyList_New(0);
    if (unlikely(cpy_r_r171 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 62, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r172 = CPyStatics[13]; /* 'name' */
    cpy_r_r173 = CPyStatics[33]; /* 'return13' */
    cpy_r_r174 = CPyStatics[22]; /* 'outputs' */
    cpy_r_r175 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r176 = CPyStatics[18]; /* 'int256' */
    cpy_r_r177 = CPyStatics[13]; /* 'name' */
    cpy_r_r178 = CPyStatics[23]; /* 'result' */
    cpy_r_r179 = CPyStatics[15]; /* 'type' */
    cpy_r_r180 = CPyStatics[18]; /* 'int256' */
    cpy_r_r181 = CPyDict_Build(3, cpy_r_r175, cpy_r_r176, cpy_r_r177, cpy_r_r178, cpy_r_r179, cpy_r_r180);
    if (unlikely(cpy_r_r181 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 64, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r182 = PyList_New(1);
    if (unlikely(cpy_r_r182 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 64, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r183 = (CPyPtr)&((PyListObject *)cpy_r_r182)->ob_item;
    cpy_r_r184 = *(CPyPtr *)cpy_r_r183;
    *(PyObject * *)cpy_r_r184 = cpy_r_r181;
    cpy_r_r185 = CPyStatics[24]; /* 'stateMutability' */
    cpy_r_r186 = CPyStatics[34]; /* 'nonpayable' */
    cpy_r_r187 = CPyStatics[15]; /* 'type' */
    cpy_r_r188 = CPyStatics[26]; /* 'function' */
    cpy_r_r189 = CPyDict_Build(5, cpy_r_r170, cpy_r_r171, cpy_r_r172, cpy_r_r173, cpy_r_r174, cpy_r_r182, cpy_r_r185, cpy_r_r186, cpy_r_r187, cpy_r_r188);
    CPy_DECREF_NO_IMM(cpy_r_r171);
    CPy_DECREF_NO_IMM(cpy_r_r182);
    if (unlikely(cpy_r_r189 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 61, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r190 = PyList_New(7);
    if (unlikely(cpy_r_r190 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL71;
    }
    cpy_r_r191 = (CPyPtr)&((PyListObject *)cpy_r_r190)->ob_item;
    cpy_r_r192 = *(CPyPtr *)cpy_r_r191;
    *(PyObject * *)cpy_r_r192 = cpy_r_r34;
    cpy_r_r193 = cpy_r_r192 + 8;
    *(PyObject * *)cpy_r_r193 = cpy_r_r71;
    cpy_r_r194 = cpy_r_r192 + 16;
    *(PyObject * *)cpy_r_r194 = cpy_r_r91;
    cpy_r_r195 = cpy_r_r192 + 24;
    *(PyObject * *)cpy_r_r195 = cpy_r_r111;
    cpy_r_r196 = cpy_r_r192 + 32;
    *(PyObject * *)cpy_r_r196 = cpy_r_r140;
    cpy_r_r197 = cpy_r_r192 + 40;
    *(PyObject * *)cpy_r_r197 = cpy_r_r169;
    cpy_r_r198 = cpy_r_r192 + 48;
    *(PyObject * *)cpy_r_r198 = cpy_r_r189;
    cpy_r_r199 = CPyStatic_globals;
    cpy_r_r200 = CPyStatics[35]; /* 'MATH_CONTRACT_ABI' */
    cpy_r_r201 = CPyDict_SetItem(cpy_r_r199, cpy_r_r200, cpy_r_r190);
    CPy_DECREF_NO_IMM(cpy_r_r190);
    cpy_r_r202 = cpy_r_r201 >= 0;
    if (unlikely(!cpy_r_r202)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r203 = CPyStatics[36]; /* 'bytecode' */
    cpy_r_r204 = CPyStatic_globals;
    cpy_r_r205 = CPyStatics[5]; /* 'MATH_CONTRACT_BYTECODE' */
    cpy_r_r206 = CPyDict_GetItem(cpy_r_r204, cpy_r_r205);
    if (unlikely(cpy_r_r206 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 70, CPyStatic_globals);
        goto CPyL47;
    }
    if (likely(PyUnicode_Check(cpy_r_r206)))
        cpy_r_r207 = cpy_r_r206;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 70, CPyStatic_globals, "str", cpy_r_r206);
        goto CPyL47;
    }
    cpy_r_r208 = CPyStatics[37]; /* 'bytecode_runtime' */
    cpy_r_r209 = CPyStatic_globals;
    cpy_r_r210 = CPyStatics[7]; /* 'MATH_CONTRACT_RUNTIME' */
    cpy_r_r211 = CPyDict_GetItem(cpy_r_r209, cpy_r_r210);
    if (unlikely(cpy_r_r211 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 71, CPyStatic_globals);
        goto CPyL72;
    }
    if (likely(PyUnicode_Check(cpy_r_r211)))
        cpy_r_r212 = cpy_r_r211;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 71, CPyStatic_globals, "str", cpy_r_r211);
        goto CPyL72;
    }
    cpy_r_r213 = CPyStatics[38]; /* 'abi' */
    cpy_r_r214 = CPyStatic_globals;
    cpy_r_r215 = CPyStatics[35]; /* 'MATH_CONTRACT_ABI' */
    cpy_r_r216 = CPyDict_GetItem(cpy_r_r214, cpy_r_r215);
    if (unlikely(cpy_r_r216 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 72, CPyStatic_globals);
        goto CPyL73;
    }
    if (likely(PyList_Check(cpy_r_r216)))
        cpy_r_r217 = cpy_r_r216;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 72, CPyStatic_globals, "list", cpy_r_r216);
        goto CPyL73;
    }
    cpy_r_r218 = CPyDict_Build(3, cpy_r_r203, cpy_r_r207, cpy_r_r208, cpy_r_r212, cpy_r_r213, cpy_r_r217);
    CPy_DECREF(cpy_r_r207);
    CPy_DECREF(cpy_r_r212);
    CPy_DECREF_NO_IMM(cpy_r_r217);
    if (unlikely(cpy_r_r218 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 69, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r219 = CPyStatic_globals;
    cpy_r_r220 = CPyStatics[39]; /* 'MATH_CONTRACT_DATA' */
    cpy_r_r221 = CPyDict_SetItem(cpy_r_r219, cpy_r_r220, cpy_r_r218);
    CPy_DECREF(cpy_r_r218);
    cpy_r_r222 = cpy_r_r221 >= 0;
    if (unlikely(!cpy_r_r222)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/math_contract.py", "<module>", 69, CPyStatic_globals);
        goto CPyL47;
    }
    return 1;
CPyL47: ;
    cpy_r_r223 = 2;
    return cpy_r_r223;
CPyL48: ;
    CPy_DecRef(cpy_r_r25);
    goto CPyL47;
CPyL49: ;
    CPy_DecRef(cpy_r_r34);
    goto CPyL47;
CPyL50: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r42);
    goto CPyL47;
CPyL51: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r42);
    CPy_DecRef(cpy_r_r49);
    goto CPyL47;
CPyL52: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r50);
    goto CPyL47;
CPyL53: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r63);
    goto CPyL47;
CPyL54: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    goto CPyL47;
CPyL55: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r73);
    goto CPyL47;
CPyL56: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r73);
    CPy_DecRef(cpy_r_r83);
    goto CPyL47;
CPyL57: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    goto CPyL47;
CPyL58: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r93);
    goto CPyL47;
CPyL59: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r93);
    CPy_DecRef(cpy_r_r103);
    goto CPyL47;
CPyL60: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    goto CPyL47;
CPyL61: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r119);
    goto CPyL47;
CPyL62: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r120);
    goto CPyL47;
CPyL63: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r120);
    CPy_DecRef(cpy_r_r132);
    goto CPyL47;
CPyL64: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    goto CPyL47;
CPyL65: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r148);
    goto CPyL47;
CPyL66: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r149);
    goto CPyL47;
CPyL67: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r161);
    goto CPyL47;
CPyL68: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r169);
    goto CPyL47;
CPyL69: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r169);
    CPy_DecRef(cpy_r_r171);
    goto CPyL47;
CPyL70: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r169);
    CPy_DecRef(cpy_r_r171);
    CPy_DecRef(cpy_r_r181);
    goto CPyL47;
CPyL71: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r71);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r140);
    CPy_DecRef(cpy_r_r169);
    CPy_DecRef(cpy_r_r189);
    goto CPyL47;
CPyL72: ;
    CPy_DecRef(cpy_r_r207);
    goto CPyL47;
CPyL73: ;
    CPy_DecRef(cpy_r_r207);
    CPy_DecRef(cpy_r_r212);
    goto CPyL47;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[40];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\225\0320x60806040525f5f553480156011575f5ffd5b5061052d8061001f5f395ff3fe608060405260043610610054575f3560e01c806316216f39146100585780635b34b9661461008257806361bc221a146100a05780636abbb3b4146100ca578063a5f3c23b146100fa578063dcf537b11461012a575b5f5ffd5b348015610063575f5ffd5b5061006c61015a565b604051610079919061024f565b60405180910390f35b61008a610162565b6040516100979190610280565b60405180910390f35b3480156100ab575f5ffd5b506100b46101b5565b6040516100c19190610280565b60405180910390f35b6100e460048036038101906100df91906102c7565b6101ba565b6040516100f19190610280565b60405180910390f35b610114600480360381019061010f919061031c565b61020d565b604051610121919061024f565b60405180910390f35b610144600480360381019061013f919061035a565b610222565b604051610151919061024f565b60405180910390f35b5f600d905090565b5f60015f5461017191906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c560016040516101a69190610427565b60405180910390a15f54905090565b5f5481565b5f815f546101c891906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5826040516101fc9190610280565b60405180910390a15f549050919050565b5f818361021a9190610440565b905092915050565b5f6007826102309190610481565b9050919050565b5f819050919050565b61024981610237565b82525050565b5f6020820190506102625f830184610240565b92915050565b5f819050919050565b61027a81610268565b82525050565b5f6020820190506102935f830184610271565b92915050565b5f5ffd5b6102a681610268565b81146102b0575f5ffd5b50565b5f813590506102c18161029d565b92915050565b5f602082840312156102dc576102db610299565b5b5f6102e9848285016102b3565b91505092915050565b6102fb81610237565b8114610305575f5ffd5b50565b5f81359050610316816102f2565b92915050565b5f5f6040838503121561033257610331610299565b5b5f61033f85828601610308565b925050602061035085828601610308565b9150509250929050565b5f6020828403121561036f5761036e610299565b5b5f61037c84828501610308565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103bc82610268565b91506103c783610268565b92508282019050808211156103df576103de610385565b5b92915050565b5f819050919050565b5f819050919050565b5f61041161040c610407846103e5565b6103ee565b610268565b9050919050565b610421816103f7565b82525050565b5f60208201905061043a5f830184610418565b92915050565b5f61044a82610237565b915061045583610237565b92508282019050828112155f8312168382125f84121516171561047b5761047a610385565b5b92915050565b5f61048b82610237565b915061049683610237565b92508282026104a481610237565b91507f800000000000000000000000000000000000000000000000000000000000000084145f841216156104db576104da610385565b5b82820584148315176104f0576104ef610385565b5b509291505056fea264697066735822122011a65cebc9a2456d3d12ae6d239cb90e576295a155544d2515af1db2cdc5c71a64736f6c634300081e0033",
    "\001\026MATH_CONTRACT_BYTECODE",
    "\001\224\\0x608060405260043610610054575f3560e01c806316216f39146100585780635b34b9661461008257806361bc221a146100a05780636abbb3b4146100ca578063a5f3c23b146100fa578063dcf537b11461012a575b5f5ffd5b348015610063575f5ffd5b5061006c61015a565b604051610079919061024f565b60405180910390f35b61008a610162565b6040516100979190610280565b60405180910390f35b3480156100ab575f5ffd5b506100b46101b5565b6040516100c19190610280565b60405180910390f35b6100e460048036038101906100df91906102c7565b6101ba565b6040516100f19190610280565b60405180910390f35b610114600480360381019061010f919061031c565b61020d565b604051610121919061024f565b60405180910390f35b610144600480360381019061013f919061035a565b610222565b604051610151919061024f565b60405180910390f35b5f600d905090565b5f60015f5461017191906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c560016040516101a69190610427565b60405180910390a15f54905090565b5f5481565b5f815f546101c891906103b2565b5f819055507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5826040516101fc9190610280565b60405180910390a15f549050919050565b5f818361021a9190610440565b905092915050565b5f6007826102309190610481565b9050919050565b5f819050919050565b61024981610237565b82525050565b5f6020820190506102625f830184610240565b92915050565b5f819050919050565b61027a81610268565b82525050565b5f6020820190506102935f830184610271565b92915050565b5f5ffd5b6102a681610268565b81146102b0575f5ffd5b50565b5f813590506102c18161029d565b92915050565b5f602082840312156102dc576102db610299565b5b5f6102e9848285016102b3565b91505092915050565b6102fb81610237565b8114610305575f5ffd5b50565b5f81359050610316816102f2565b92915050565b5f5f6040838503121561033257610331610299565b5b5f61033f85828601610308565b925050602061035085828601610308565b9150509250929050565b5f6020828403121561036f5761036e610299565b5b5f61037c84828501610308565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f6103bc82610268565b91506103c783610268565b92508282019050808211156103df576103de610385565b5b92915050565b5f819050919050565b5f819050919050565b5f61041161040c610407846103e5565b6103ee565b610268565b9050919050565b610421816103f7565b82525050565b5f60208201905061043a5f830184610418565b92915050565b5f61044a82610237565b915061045583610237565b92508282019050828112155f8312168382125f84121516171561047b5761047a610385565b5b92915050565b5f61048b82610237565b915061049683610237565b92508282026104a481610237565b91507f800000000000000000000000000000000000000000000000000000000000000084145f841216156104db576104da610385565b5b82820584148315176104f0576104ef610385565b5b509291505056fea264697066735822122011a65cebc9a2456d3d12ae6d239cb90e576295a155544d2515af1db2cdc5c71a64736f6c634300081e0033",
    "\006\025MATH_CONTRACT_RUNTIME\tanonymous\006inputs\aindexed\finternalType\auint256",
    "\v\004name\005value\004type\tIncreased\005event\006int256\001a\001b\003add\aoutputs\006result",
    "\a\017stateMutability\apayable\bfunction\acounter\000\004view\020incrementCounter",
    "\006\006amount\tmultiply7\breturn13\nnonpayable\021MATH_CONTRACT_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi\022MATH_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___math_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_math_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___math_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___math_contract, "faster_web3._utils.contract_sources.contract_data.math_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___math_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___math_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_math_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.math_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_math_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_math_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_math_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
