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
#include "__native_tuple_contracts.h"
#include "__native_internal_tuple_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___tuple_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal);
    Py_CLEAR(modname);
    CPy_XDECREF(CPyStatic_TUPLE_CONTRACT_BYTECODE);
    CPyStatic_TUPLE_CONTRACT_BYTECODE = NULL;
    CPy_XDECREF(CPyStatic_TUPLE_CONTRACT_RUNTIME);
    CPyStatic_TUPLE_CONTRACT_RUNTIME = NULL;
    CPy_XDECREF_NO_IMM(CPyStatic_TUPLE_CONTRACT_ABI);
    CPyStatic_TUPLE_CONTRACT_ABI = NULL;
    CPy_XDECREF(CPyStatic_TUPLE_CONTRACT_DATA);
    CPyStatic_TUPLE_CONTRACT_DATA = NULL;
    CPy_XDECREF(CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE);
    CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE = NULL;
    CPy_XDECREF(CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME);
    CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME = NULL;
    CPy_XDECREF_NO_IMM(CPyStatic_NESTED_TUPLE_CONTRACT_ABI);
    CPyStatic_NESTED_TUPLE_CONTRACT_ABI = NULL;
    CPy_XDECREF(CPyStatic_NESTED_TUPLE_CONTRACT_DATA);
    CPyStatic_NESTED_TUPLE_CONTRACT_DATA = NULL;
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.tuple_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___tuple_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___tuple_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal;
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
    int32_t cpy_r_r16;
    char cpy_r_r17;
    PyObject *cpy_r_r18;
    PyObject *cpy_r_r19;
    PyObject *cpy_r_r20;
    int32_t cpy_r_r21;
    char cpy_r_r22;
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
    CPyPtr cpy_r_r62;
    CPyPtr cpy_r_r63;
    CPyPtr cpy_r_r64;
    CPyPtr cpy_r_r65;
    PyObject *cpy_r_r66;
    PyObject *cpy_r_r67;
    PyObject *cpy_r_r68;
    PyObject *cpy_r_r69;
    PyObject *cpy_r_r70;
    PyObject *cpy_r_r71;
    PyObject *cpy_r_r72;
    PyObject *cpy_r_r73;
    CPyPtr cpy_r_r74;
    CPyPtr cpy_r_r75;
    CPyPtr cpy_r_r76;
    CPyPtr cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    PyObject *cpy_r_r80;
    PyObject *cpy_r_r81;
    PyObject *cpy_r_r82;
    PyObject *cpy_r_r83;
    PyObject *cpy_r_r84;
    PyObject *cpy_r_r85;
    CPyPtr cpy_r_r86;
    CPyPtr cpy_r_r87;
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
    PyObject *cpy_r_r105;
    PyObject *cpy_r_r106;
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
    CPyPtr cpy_r_r129;
    CPyPtr cpy_r_r130;
    CPyPtr cpy_r_r131;
    CPyPtr cpy_r_r132;
    PyObject *cpy_r_r133;
    PyObject *cpy_r_r134;
    PyObject *cpy_r_r135;
    PyObject *cpy_r_r136;
    PyObject *cpy_r_r137;
    PyObject *cpy_r_r138;
    PyObject *cpy_r_r139;
    PyObject *cpy_r_r140;
    CPyPtr cpy_r_r141;
    CPyPtr cpy_r_r142;
    CPyPtr cpy_r_r143;
    CPyPtr cpy_r_r144;
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
    PyObject *cpy_r_r155;
    PyObject *cpy_r_r156;
    PyObject *cpy_r_r157;
    PyObject *cpy_r_r158;
    PyObject *cpy_r_r159;
    PyObject *cpy_r_r160;
    CPyPtr cpy_r_r161;
    CPyPtr cpy_r_r162;
    PyObject *cpy_r_r163;
    PyObject *cpy_r_r164;
    int32_t cpy_r_r165;
    char cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject *cpy_r_r168;
    char cpy_r_r169;
    PyObject *cpy_r_r170;
    PyObject *cpy_r_r171;
    char cpy_r_r172;
    PyObject *cpy_r_r173;
    PyObject *cpy_r_r174;
    char cpy_r_r175;
    PyObject *cpy_r_r176;
    PyObject *cpy_r_r177;
    PyObject *cpy_r_r178;
    int32_t cpy_r_r179;
    char cpy_r_r180;
    PyObject *cpy_r_r181;
    PyObject *cpy_r_r182;
    PyObject *cpy_r_r183;
    int32_t cpy_r_r184;
    char cpy_r_r185;
    PyObject *cpy_r_r186;
    PyObject *cpy_r_r187;
    PyObject *cpy_r_r188;
    int32_t cpy_r_r189;
    char cpy_r_r190;
    PyObject *cpy_r_r191;
    PyObject *cpy_r_r192;
    PyObject *cpy_r_r193;
    PyObject *cpy_r_r194;
    PyObject *cpy_r_r195;
    PyObject *cpy_r_r196;
    PyObject *cpy_r_r197;
    PyObject *cpy_r_r198;
    PyObject *cpy_r_r199;
    PyObject *cpy_r_r200;
    PyObject *cpy_r_r201;
    PyObject *cpy_r_r202;
    PyObject *cpy_r_r203;
    PyObject *cpy_r_r204;
    PyObject *cpy_r_r205;
    PyObject *cpy_r_r206;
    PyObject *cpy_r_r207;
    PyObject *cpy_r_r208;
    PyObject *cpy_r_r209;
    CPyPtr cpy_r_r210;
    CPyPtr cpy_r_r211;
    CPyPtr cpy_r_r212;
    PyObject *cpy_r_r213;
    PyObject *cpy_r_r214;
    PyObject *cpy_r_r215;
    PyObject *cpy_r_r216;
    PyObject *cpy_r_r217;
    PyObject *cpy_r_r218;
    PyObject *cpy_r_r219;
    PyObject *cpy_r_r220;
    CPyPtr cpy_r_r221;
    CPyPtr cpy_r_r222;
    PyObject *cpy_r_r223;
    PyObject *cpy_r_r224;
    PyObject *cpy_r_r225;
    PyObject *cpy_r_r226;
    PyObject *cpy_r_r227;
    PyObject *cpy_r_r228;
    PyObject *cpy_r_r229;
    PyObject *cpy_r_r230;
    CPyPtr cpy_r_r231;
    CPyPtr cpy_r_r232;
    PyObject *cpy_r_r233;
    PyObject *cpy_r_r234;
    PyObject *cpy_r_r235;
    PyObject *cpy_r_r236;
    PyObject *cpy_r_r237;
    PyObject *cpy_r_r238;
    PyObject *cpy_r_r239;
    PyObject *cpy_r_r240;
    CPyPtr cpy_r_r241;
    CPyPtr cpy_r_r242;
    PyObject *cpy_r_r243;
    PyObject *cpy_r_r244;
    PyObject *cpy_r_r245;
    PyObject *cpy_r_r246;
    PyObject *cpy_r_r247;
    PyObject *cpy_r_r248;
    PyObject *cpy_r_r249;
    PyObject *cpy_r_r250;
    PyObject *cpy_r_r251;
    PyObject *cpy_r_r252;
    PyObject *cpy_r_r253;
    PyObject *cpy_r_r254;
    PyObject *cpy_r_r255;
    PyObject *cpy_r_r256;
    PyObject *cpy_r_r257;
    PyObject *cpy_r_r258;
    PyObject *cpy_r_r259;
    PyObject *cpy_r_r260;
    PyObject *cpy_r_r261;
    PyObject *cpy_r_r262;
    PyObject *cpy_r_r263;
    CPyPtr cpy_r_r264;
    CPyPtr cpy_r_r265;
    CPyPtr cpy_r_r266;
    PyObject *cpy_r_r267;
    PyObject *cpy_r_r268;
    PyObject *cpy_r_r269;
    PyObject *cpy_r_r270;
    PyObject *cpy_r_r271;
    PyObject *cpy_r_r272;
    PyObject *cpy_r_r273;
    PyObject *cpy_r_r274;
    CPyPtr cpy_r_r275;
    CPyPtr cpy_r_r276;
    PyObject *cpy_r_r277;
    PyObject *cpy_r_r278;
    PyObject *cpy_r_r279;
    PyObject *cpy_r_r280;
    PyObject *cpy_r_r281;
    PyObject *cpy_r_r282;
    PyObject *cpy_r_r283;
    PyObject *cpy_r_r284;
    CPyPtr cpy_r_r285;
    CPyPtr cpy_r_r286;
    PyObject *cpy_r_r287;
    PyObject *cpy_r_r288;
    PyObject *cpy_r_r289;
    PyObject *cpy_r_r290;
    PyObject *cpy_r_r291;
    PyObject *cpy_r_r292;
    PyObject *cpy_r_r293;
    PyObject *cpy_r_r294;
    CPyPtr cpy_r_r295;
    CPyPtr cpy_r_r296;
    PyObject *cpy_r_r297;
    PyObject *cpy_r_r298;
    PyObject *cpy_r_r299;
    PyObject *cpy_r_r300;
    PyObject *cpy_r_r301;
    PyObject *cpy_r_r302;
    CPyPtr cpy_r_r303;
    CPyPtr cpy_r_r304;
    PyObject *cpy_r_r305;
    PyObject *cpy_r_r306;
    int32_t cpy_r_r307;
    char cpy_r_r308;
    PyObject *cpy_r_r309;
    PyObject *cpy_r_r310;
    char cpy_r_r311;
    PyObject *cpy_r_r312;
    PyObject *cpy_r_r313;
    char cpy_r_r314;
    PyObject *cpy_r_r315;
    PyObject *cpy_r_r316;
    char cpy_r_r317;
    PyObject *cpy_r_r318;
    PyObject *cpy_r_r319;
    PyObject *cpy_r_r320;
    int32_t cpy_r_r321;
    char cpy_r_r322;
    char cpy_r_r323;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL76;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[57]; /* ('Final', 'List') */
    cpy_r_r6 = CPyStatics[6]; /* 'typing' */
    cpy_r_r7 = CPyStatic_globals;
    cpy_r_r8 = CPyImport_ImportFromMany(cpy_r_r6, cpy_r_r5, cpy_r_r5, cpy_r_r7);
    if (unlikely(cpy_r_r8 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 6, CPyStatic_globals);
        goto CPyL76;
    }
    CPyModule_typing = cpy_r_r8;
    CPy_INCREF(CPyModule_typing);
    CPy_DECREF(cpy_r_r8);
    cpy_r_r9 = CPyStatics[58]; /* ('ABIElement', 'HexStr') */
    cpy_r_r10 = CPyStatics[9]; /* 'eth_typing' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyImport_ImportFromMany(cpy_r_r10, cpy_r_r9, cpy_r_r9, cpy_r_r11);
    if (unlikely(cpy_r_r12 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL76;
    }
    CPyModule_eth_typing = cpy_r_r12;
    CPy_INCREF(CPyModule_eth_typing);
    CPy_DECREF(cpy_r_r12);
    cpy_r_r13 = CPyStatics[10]; /* '0x6080604052348015600e575f5ffd5b50610a688061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80638e1ae3c71461002d575b5f5ffd5b6100476004803603810190610042919061064d565b61005d565b6040516100549190610a12565b60405180910390f35b61006561006d565b819050919050565b60405180606001604052805f815260200160608152602001606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100e8826100a2565b810181811067ffffffffffffffff82111715610107576101066100b2565b5b80604052505050565b5f61011961008d565b905061012582826100df565b919050565b5f5ffd5b5f819050919050565b6101408161012e565b811461014a575f5ffd5b50565b5f8135905061015b81610137565b92915050565b5f5ffd5b5f67ffffffffffffffff82111561017f5761017e6100b2565b5b602082029050602081019050919050565b5f5ffd5b5f6101a66101a184610165565b610110565b905080838252602082019050602084028301858111156101c9576101c8610190565b5b835b818110156101f257806101de888261014d565b8452602084019350506020810190506101cb565b5050509392505050565b5f82601f8301126102105761020f610161565b5b8135610220848260208601610194565b91505092915050565b5f67ffffffffffffffff821115610243576102426100b2565b5b602082029050602081019050919050565b5f819050919050565b61026681610254565b8114610270575f5ffd5b50565b5f813590506102818161025d565b92915050565b5f67ffffffffffffffff8211156102a1576102a06100b2565b5b602082029050919050565b5f8115159050919050565b6102c0816102ac565b81146102ca575f5ffd5b50565b5f813590506102db816102b7565b92915050565b5f6102f36102ee84610287565b610110565b9050806020840283018581111561030d5761030c610190565b5b835b81811015610336578061032288826102cd565b84526020840193505060208101905061030f565b5050509392505050565b5f82601f83011261035457610353610161565b5b60026103618482856102e1565b91505092915050565b5f67ffffffffffffffff821115610384576103836100b2565b5b602082029050602081019050919050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103be82610395565b9050919050565b6103ce816103b4565b81146103d8575f5ffd5b50565b5f813590506103e9816103c5565b92915050565b5f6104016103fc8461036a565b610110565b9050808382526020820190506020840283018581111561042457610423610190565b5b835b8181101561044d578061043988826103db565b845260208401935050602081019050610426565b5050509392505050565b5f82601f83011261046b5761046a610161565b5b813561047b8482602086016103ef565b91505092915050565b5f608082840312156104995761049861009e565b5b6104a36060610110565b90505f6104b284828501610273565b5f8301525060206104c584828501610340565b602083015250606082013567ffffffffffffffff8111156104e9576104e861012a565b5b6104f584828501610457565b60408301525092915050565b5f61051361050e84610229565b610110565b9050808382526020820190506020840283018581111561053657610535610190565b5b835b8181101561057d57803567ffffffffffffffff81111561055b5761055a610161565b5b8086016105688982610484565b85526020850194505050602081019050610538565b5050509392505050565b5f82601f83011261059b5761059a610161565b5b81356105ab848260208601610501565b91505092915050565b5f606082840312156105c9576105c861009e565b5b6105d36060610110565b90505f6105e28482850161014d565b5f83015250602082013567ffffffffffffffff8111156106055761060461012a565b5b610611848285016101fc565b602083015250604082013567ffffffffffffffff8111156106355761063461012a565b5b61064184828501610587565b60408301525092915050565b5f6020828403121561066257610661610096565b5b5f82013567ffffffffffffffff81111561067f5761067e61009a565b5b61068b848285016105b4565b91505092915050565b61069d8161012e565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f6106d78383610694565b60208301905092915050565b5f602082019050919050565b5f6106f9826106a3565b61070381856106ad565b935061070e836106bd565b805f5b8381101561073e57815161072588826106cc565b9750610730836106e3565b925050600181019050610711565b5085935050505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61077d81610254565b82525050565b5f60029050919050565b5f81905092915050565b5f819050919050565b6107a9816102ac565b82525050565b5f6107ba83836107a0565b60208301905092915050565b5f602082019050919050565b6107db81610783565b6107e5818461078d565b92506107f082610797565b805f5b8381101561082057815161080787826107af565b9650610812836107c6565b9250506001810190506107f3565b505050505050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61085a816103b4565b82525050565b5f61086b8383610851565b60208301905092915050565b5f602082019050919050565b5f61088d82610828565b6108978185610832565b93506108a283610842565b805f5b838110156108d25781516108b98882610860565b97506108c483610877565b9250506001810190506108a5565b5085935050505092915050565b5f608083015f8301516108f45f860182610774565b50602083015161090760208601826107d2565b506040830151848203606086015261091f8282610883565b9150508091505092915050565b5f61093783836108df565b905092915050565b5f602082019050919050565b5f6109558261074b565b61095f8185610755565b93508360208202850161097185610765565b805f5b858110156109ac578484038952815161098d858261092c565b94506109988361093f565b925060208a01995050600181019050610974565b50829750879550505050505092915050565b5f606083015f8301516109d35f860182610694565b50602083015184820360208601526109eb82826106ef565b91505060408301518482036040860152610a05828261094b565b9150508091505092915050565b5f6020820190508181035f830152610a2a81846109be565b90509291505056fea26469706673582212207c5620c2257d173ed894791417ffad7e98aad1aab11d2ec22b5148e5d77de0c464736f6c634300081e0033' */
    CPyStatic_TUPLE_CONTRACT_BYTECODE = cpy_r_r13;
    CPy_INCREF(CPyStatic_TUPLE_CONTRACT_BYTECODE);
    cpy_r_r14 = CPyStatic_globals;
    cpy_r_r15 = CPyStatics[11]; /* 'TUPLE_CONTRACT_BYTECODE' */
    cpy_r_r16 = CPyDict_SetItem(cpy_r_r14, cpy_r_r15, cpy_r_r13);
    cpy_r_r17 = cpy_r_r16 >= 0;
    if (unlikely(!cpy_r_r17)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 17, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r18 = CPyStatics[12]; /* '0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80638e1ae3c71461002d575b5f5ffd5b6100476004803603810190610042919061064d565b61005d565b6040516100549190610a12565b60405180910390f35b61006561006d565b819050919050565b60405180606001604052805f815260200160608152602001606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100e8826100a2565b810181811067ffffffffffffffff82111715610107576101066100b2565b5b80604052505050565b5f61011961008d565b905061012582826100df565b919050565b5f5ffd5b5f819050919050565b6101408161012e565b811461014a575f5ffd5b50565b5f8135905061015b81610137565b92915050565b5f5ffd5b5f67ffffffffffffffff82111561017f5761017e6100b2565b5b602082029050602081019050919050565b5f5ffd5b5f6101a66101a184610165565b610110565b905080838252602082019050602084028301858111156101c9576101c8610190565b5b835b818110156101f257806101de888261014d565b8452602084019350506020810190506101cb565b5050509392505050565b5f82601f8301126102105761020f610161565b5b8135610220848260208601610194565b91505092915050565b5f67ffffffffffffffff821115610243576102426100b2565b5b602082029050602081019050919050565b5f819050919050565b61026681610254565b8114610270575f5ffd5b50565b5f813590506102818161025d565b92915050565b5f67ffffffffffffffff8211156102a1576102a06100b2565b5b602082029050919050565b5f8115159050919050565b6102c0816102ac565b81146102ca575f5ffd5b50565b5f813590506102db816102b7565b92915050565b5f6102f36102ee84610287565b610110565b9050806020840283018581111561030d5761030c610190565b5b835b81811015610336578061032288826102cd565b84526020840193505060208101905061030f565b5050509392505050565b5f82601f83011261035457610353610161565b5b60026103618482856102e1565b91505092915050565b5f67ffffffffffffffff821115610384576103836100b2565b5b602082029050602081019050919050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103be82610395565b9050919050565b6103ce816103b4565b81146103d8575f5ffd5b50565b5f813590506103e9816103c5565b92915050565b5f6104016103fc8461036a565b610110565b9050808382526020820190506020840283018581111561042457610423610190565b5b835b8181101561044d578061043988826103db565b845260208401935050602081019050610426565b5050509392505050565b5f82601f83011261046b5761046a610161565b5b813561047b8482602086016103ef565b91505092915050565b5f608082840312156104995761049861009e565b5b6104a36060610110565b90505f6104b284828501610273565b5f8301525060206104c584828501610340565b602083015250606082013567ffffffffffffffff8111156104e9576104e861012a565b5b6104f584828501610457565b60408301525092915050565b5f61051361050e84610229565b610110565b9050808382526020820190506020840283018581111561053657610535610190565b5b835b8181101561057d57803567ffffffffffffffff81111561055b5761055a610161565b5b8086016105688982610484565b85526020850194505050602081019050610538565b5050509392505050565b5f82601f83011261059b5761059a610161565b5b81356105ab848260208601610501565b91505092915050565b5f606082840312156105c9576105c861009e565b5b6105d36060610110565b90505f6105e28482850161014d565b5f83015250602082013567ffffffffffffffff8111156106055761060461012a565b5b610611848285016101fc565b602083015250604082013567ffffffffffffffff8111156106355761063461012a565b5b61064184828501610587565b60408301525092915050565b5f6020828403121561066257610661610096565b5b5f82013567ffffffffffffffff81111561067f5761067e61009a565b5b61068b848285016105b4565b91505092915050565b61069d8161012e565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f6106d78383610694565b60208301905092915050565b5f602082019050919050565b5f6106f9826106a3565b61070381856106ad565b935061070e836106bd565b805f5b8381101561073e57815161072588826106cc565b9750610730836106e3565b925050600181019050610711565b5085935050505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61077d81610254565b82525050565b5f60029050919050565b5f81905092915050565b5f819050919050565b6107a9816102ac565b82525050565b5f6107ba83836107a0565b60208301905092915050565b5f602082019050919050565b6107db81610783565b6107e5818461078d565b92506107f082610797565b805f5b8381101561082057815161080787826107af565b9650610812836107c6565b9250506001810190506107f3565b505050505050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61085a816103b4565b82525050565b5f61086b8383610851565b60208301905092915050565b5f602082019050919050565b5f61088d82610828565b6108978185610832565b93506108a283610842565b805f5b838110156108d25781516108b98882610860565b97506108c483610877565b9250506001810190506108a5565b5085935050505092915050565b5f608083015f8301516108f45f860182610774565b50602083015161090760208601826107d2565b506040830151848203606086015261091f8282610883565b9150508091505092915050565b5f61093783836108df565b905092915050565b5f602082019050919050565b5f6109558261074b565b61095f8185610755565b93508360208202850161097185610765565b805f5b858110156109ac578484038952815161098d858261092c565b94506109988361093f565b925060208a01995050600181019050610974565b50829750879550505050505092915050565b5f606083015f8301516109d35f860182610694565b50602083015184820360208601526109eb82826106ef565b91505060408301518482036040860152610a05828261094b565b9150508091505092915050565b5f6020820190508181035f830152610a2a81846109be565b90509291505056fea26469706673582212207c5620c2257d173ed894791417ffad7e98aad1aab11d2ec22b5148e5d77de0c464736f6c634300081e0033' */
    CPyStatic_TUPLE_CONTRACT_RUNTIME = cpy_r_r18;
    CPy_INCREF(CPyStatic_TUPLE_CONTRACT_RUNTIME);
    cpy_r_r19 = CPyStatic_globals;
    cpy_r_r20 = CPyStatics[13]; /* 'TUPLE_CONTRACT_RUNTIME' */
    cpy_r_r21 = CPyDict_SetItem(cpy_r_r19, cpy_r_r20, cpy_r_r18);
    cpy_r_r22 = cpy_r_r21 >= 0;
    if (unlikely(!cpy_r_r22)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r23 = CPyStatics[14]; /* 'inputs' */
    cpy_r_r24 = CPyStatics[15]; /* 'components' */
    cpy_r_r25 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r26 = CPyStatics[17]; /* 'uint256' */
    cpy_r_r27 = CPyStatics[18]; /* 'name' */
    cpy_r_r28 = CPyStatics[19]; /* 'a' */
    cpy_r_r29 = CPyStatics[20]; /* 'type' */
    cpy_r_r30 = CPyStatics[17]; /* 'uint256' */
    cpy_r_r31 = CPyDict_Build(3, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r30);
    if (unlikely(cpy_r_r31 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 24, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r32 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r33 = CPyStatics[21]; /* 'uint256[]' */
    cpy_r_r34 = CPyStatics[18]; /* 'name' */
    cpy_r_r35 = CPyStatics[22]; /* 'b' */
    cpy_r_r36 = CPyStatics[20]; /* 'type' */
    cpy_r_r37 = CPyStatics[21]; /* 'uint256[]' */
    cpy_r_r38 = CPyDict_Build(3, cpy_r_r32, cpy_r_r33, cpy_r_r34, cpy_r_r35, cpy_r_r36, cpy_r_r37);
    if (unlikely(cpy_r_r38 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r39 = CPyStatics[15]; /* 'components' */
    cpy_r_r40 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r41 = CPyStatics[23]; /* 'int256' */
    cpy_r_r42 = CPyStatics[18]; /* 'name' */
    cpy_r_r43 = CPyStatics[24]; /* 'x' */
    cpy_r_r44 = CPyStatics[20]; /* 'type' */
    cpy_r_r45 = CPyStatics[23]; /* 'int256' */
    cpy_r_r46 = CPyDict_Build(3, cpy_r_r40, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 28, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r47 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r48 = CPyStatics[25]; /* 'bool[2]' */
    cpy_r_r49 = CPyStatics[18]; /* 'name' */
    cpy_r_r50 = CPyStatics[26]; /* 'y' */
    cpy_r_r51 = CPyStatics[20]; /* 'type' */
    cpy_r_r52 = CPyStatics[25]; /* 'bool[2]' */
    cpy_r_r53 = CPyDict_Build(3, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50, cpy_r_r51, cpy_r_r52);
    if (unlikely(cpy_r_r53 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 29, CPyStatic_globals);
        goto CPyL79;
    }
    cpy_r_r54 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r55 = CPyStatics[27]; /* 'address[]' */
    cpy_r_r56 = CPyStatics[18]; /* 'name' */
    cpy_r_r57 = CPyStatics[28]; /* 'z' */
    cpy_r_r58 = CPyStatics[20]; /* 'type' */
    cpy_r_r59 = CPyStatics[27]; /* 'address[]' */
    cpy_r_r60 = CPyDict_Build(3, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59);
    if (unlikely(cpy_r_r60 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 30, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r61 = PyList_New(3);
    if (unlikely(cpy_r_r61 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 27, CPyStatic_globals);
        goto CPyL81;
    }
    cpy_r_r62 = (CPyPtr)&((PyListObject *)cpy_r_r61)->ob_item;
    cpy_r_r63 = *(CPyPtr *)cpy_r_r62;
    *(PyObject * *)cpy_r_r63 = cpy_r_r46;
    cpy_r_r64 = cpy_r_r63 + 8;
    *(PyObject * *)cpy_r_r64 = cpy_r_r53;
    cpy_r_r65 = cpy_r_r63 + 16;
    *(PyObject * *)cpy_r_r65 = cpy_r_r60;
    cpy_r_r66 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r67 = CPyStatics[29]; /* 'struct TupleContract.T[]' */
    cpy_r_r68 = CPyStatics[18]; /* 'name' */
    cpy_r_r69 = CPyStatics[30]; /* 'c' */
    cpy_r_r70 = CPyStatics[20]; /* 'type' */
    cpy_r_r71 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r72 = CPyDict_Build(4, cpy_r_r39, cpy_r_r61, cpy_r_r66, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71);
    CPy_DECREF_NO_IMM(cpy_r_r61);
    if (unlikely(cpy_r_r72 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 26, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r73 = PyList_New(3);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 23, CPyStatic_globals);
        goto CPyL82;
    }
    cpy_r_r74 = (CPyPtr)&((PyListObject *)cpy_r_r73)->ob_item;
    cpy_r_r75 = *(CPyPtr *)cpy_r_r74;
    *(PyObject * *)cpy_r_r75 = cpy_r_r31;
    cpy_r_r76 = cpy_r_r75 + 8;
    *(PyObject * *)cpy_r_r76 = cpy_r_r38;
    cpy_r_r77 = cpy_r_r75 + 16;
    *(PyObject * *)cpy_r_r77 = cpy_r_r72;
    cpy_r_r78 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r79 = CPyStatics[32]; /* 'struct TupleContract.S' */
    cpy_r_r80 = CPyStatics[18]; /* 'name' */
    cpy_r_r81 = CPyStatics[33]; /* 's' */
    cpy_r_r82 = CPyStatics[20]; /* 'type' */
    cpy_r_r83 = CPyStatics[34]; /* 'tuple' */
    cpy_r_r84 = CPyDict_Build(4, cpy_r_r24, cpy_r_r73, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81, cpy_r_r82, cpy_r_r83);
    CPy_DECREF_NO_IMM(cpy_r_r73);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 22, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r85 = PyList_New(1);
    if (unlikely(cpy_r_r85 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 21, CPyStatic_globals);
        goto CPyL83;
    }
    cpy_r_r86 = (CPyPtr)&((PyListObject *)cpy_r_r85)->ob_item;
    cpy_r_r87 = *(CPyPtr *)cpy_r_r86;
    *(PyObject * *)cpy_r_r87 = cpy_r_r84;
    cpy_r_r88 = CPyStatics[18]; /* 'name' */
    cpy_r_r89 = CPyStatics[35]; /* 'method' */
    cpy_r_r90 = CPyStatics[36]; /* 'outputs' */
    cpy_r_r91 = CPyStatics[15]; /* 'components' */
    cpy_r_r92 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r93 = CPyStatics[17]; /* 'uint256' */
    cpy_r_r94 = CPyStatics[18]; /* 'name' */
    cpy_r_r95 = CPyStatics[19]; /* 'a' */
    cpy_r_r96 = CPyStatics[20]; /* 'type' */
    cpy_r_r97 = CPyStatics[17]; /* 'uint256' */
    cpy_r_r98 = CPyDict_Build(3, cpy_r_r92, cpy_r_r93, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r97);
    if (unlikely(cpy_r_r98 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 50, CPyStatic_globals);
        goto CPyL84;
    }
    cpy_r_r99 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r100 = CPyStatics[21]; /* 'uint256[]' */
    cpy_r_r101 = CPyStatics[18]; /* 'name' */
    cpy_r_r102 = CPyStatics[22]; /* 'b' */
    cpy_r_r103 = CPyStatics[20]; /* 'type' */
    cpy_r_r104 = CPyStatics[21]; /* 'uint256[]' */
    cpy_r_r105 = CPyDict_Build(3, cpy_r_r99, cpy_r_r100, cpy_r_r101, cpy_r_r102, cpy_r_r103, cpy_r_r104);
    if (unlikely(cpy_r_r105 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 51, CPyStatic_globals);
        goto CPyL85;
    }
    cpy_r_r106 = CPyStatics[15]; /* 'components' */
    cpy_r_r107 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r108 = CPyStatics[23]; /* 'int256' */
    cpy_r_r109 = CPyStatics[18]; /* 'name' */
    cpy_r_r110 = CPyStatics[24]; /* 'x' */
    cpy_r_r111 = CPyStatics[20]; /* 'type' */
    cpy_r_r112 = CPyStatics[23]; /* 'int256' */
    cpy_r_r113 = CPyDict_Build(3, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110, cpy_r_r111, cpy_r_r112);
    if (unlikely(cpy_r_r113 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL86;
    }
    cpy_r_r114 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r115 = CPyStatics[25]; /* 'bool[2]' */
    cpy_r_r116 = CPyStatics[18]; /* 'name' */
    cpy_r_r117 = CPyStatics[26]; /* 'y' */
    cpy_r_r118 = CPyStatics[20]; /* 'type' */
    cpy_r_r119 = CPyStatics[25]; /* 'bool[2]' */
    cpy_r_r120 = CPyDict_Build(3, cpy_r_r114, cpy_r_r115, cpy_r_r116, cpy_r_r117, cpy_r_r118, cpy_r_r119);
    if (unlikely(cpy_r_r120 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 55, CPyStatic_globals);
        goto CPyL87;
    }
    cpy_r_r121 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r122 = CPyStatics[27]; /* 'address[]' */
    cpy_r_r123 = CPyStatics[18]; /* 'name' */
    cpy_r_r124 = CPyStatics[28]; /* 'z' */
    cpy_r_r125 = CPyStatics[20]; /* 'type' */
    cpy_r_r126 = CPyStatics[27]; /* 'address[]' */
    cpy_r_r127 = CPyDict_Build(3, cpy_r_r121, cpy_r_r122, cpy_r_r123, cpy_r_r124, cpy_r_r125, cpy_r_r126);
    if (unlikely(cpy_r_r127 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL88;
    }
    cpy_r_r128 = PyList_New(3);
    if (unlikely(cpy_r_r128 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 53, CPyStatic_globals);
        goto CPyL89;
    }
    cpy_r_r129 = (CPyPtr)&((PyListObject *)cpy_r_r128)->ob_item;
    cpy_r_r130 = *(CPyPtr *)cpy_r_r129;
    *(PyObject * *)cpy_r_r130 = cpy_r_r113;
    cpy_r_r131 = cpy_r_r130 + 8;
    *(PyObject * *)cpy_r_r131 = cpy_r_r120;
    cpy_r_r132 = cpy_r_r130 + 16;
    *(PyObject * *)cpy_r_r132 = cpy_r_r127;
    cpy_r_r133 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r134 = CPyStatics[29]; /* 'struct TupleContract.T[]' */
    cpy_r_r135 = CPyStatics[18]; /* 'name' */
    cpy_r_r136 = CPyStatics[30]; /* 'c' */
    cpy_r_r137 = CPyStatics[20]; /* 'type' */
    cpy_r_r138 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r139 = CPyDict_Build(4, cpy_r_r106, cpy_r_r128, cpy_r_r133, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137, cpy_r_r138);
    CPy_DECREF_NO_IMM(cpy_r_r128);
    if (unlikely(cpy_r_r139 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 52, CPyStatic_globals);
        goto CPyL86;
    }
    cpy_r_r140 = PyList_New(3);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL90;
    }
    cpy_r_r141 = (CPyPtr)&((PyListObject *)cpy_r_r140)->ob_item;
    cpy_r_r142 = *(CPyPtr *)cpy_r_r141;
    *(PyObject * *)cpy_r_r142 = cpy_r_r98;
    cpy_r_r143 = cpy_r_r142 + 8;
    *(PyObject * *)cpy_r_r143 = cpy_r_r105;
    cpy_r_r144 = cpy_r_r142 + 16;
    *(PyObject * *)cpy_r_r144 = cpy_r_r139;
    cpy_r_r145 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r146 = CPyStatics[32]; /* 'struct TupleContract.S' */
    cpy_r_r147 = CPyStatics[18]; /* 'name' */
    cpy_r_r148 = CPyStatics[37]; /* '' */
    cpy_r_r149 = CPyStatics[20]; /* 'type' */
    cpy_r_r150 = CPyStatics[34]; /* 'tuple' */
    cpy_r_r151 = CPyDict_Build(4, cpy_r_r91, cpy_r_r140, cpy_r_r145, cpy_r_r146, cpy_r_r147, cpy_r_r148, cpy_r_r149, cpy_r_r150);
    CPy_DECREF_NO_IMM(cpy_r_r140);
    if (unlikely(cpy_r_r151 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 48, CPyStatic_globals);
        goto CPyL84;
    }
    cpy_r_r152 = PyList_New(1);
    if (unlikely(cpy_r_r152 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL91;
    }
    cpy_r_r153 = (CPyPtr)&((PyListObject *)cpy_r_r152)->ob_item;
    cpy_r_r154 = *(CPyPtr *)cpy_r_r153;
    *(PyObject * *)cpy_r_r154 = cpy_r_r151;
    cpy_r_r155 = CPyStatics[38]; /* 'stateMutability' */
    cpy_r_r156 = CPyStatics[39]; /* 'pure' */
    cpy_r_r157 = CPyStatics[20]; /* 'type' */
    cpy_r_r158 = CPyStatics[40]; /* 'function' */
    cpy_r_r159 = CPyDict_Build(5, cpy_r_r23, cpy_r_r85, cpy_r_r88, cpy_r_r89, cpy_r_r90, cpy_r_r152, cpy_r_r155, cpy_r_r156, cpy_r_r157, cpy_r_r158);
    CPy_DECREF_NO_IMM(cpy_r_r85);
    CPy_DECREF_NO_IMM(cpy_r_r152);
    if (unlikely(cpy_r_r159 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 20, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r160 = PyList_New(1);
    if (unlikely(cpy_r_r160 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 19, CPyStatic_globals);
        goto CPyL92;
    }
    cpy_r_r161 = (CPyPtr)&((PyListObject *)cpy_r_r160)->ob_item;
    cpy_r_r162 = *(CPyPtr *)cpy_r_r161;
    *(PyObject * *)cpy_r_r162 = cpy_r_r159;
    CPyStatic_TUPLE_CONTRACT_ABI = cpy_r_r160;
    CPy_INCREF_NO_IMM(CPyStatic_TUPLE_CONTRACT_ABI);
    cpy_r_r163 = CPyStatic_globals;
    cpy_r_r164 = CPyStatics[41]; /* 'TUPLE_CONTRACT_ABI' */
    cpy_r_r165 = CPyDict_SetItem(cpy_r_r163, cpy_r_r164, cpy_r_r160);
    CPy_DECREF_NO_IMM(cpy_r_r160);
    cpy_r_r166 = cpy_r_r165 >= 0;
    if (unlikely(!cpy_r_r166)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 19, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r167 = CPyStatics[42]; /* 'bytecode' */
    cpy_r_r168 = CPyStatic_TUPLE_CONTRACT_BYTECODE;
    if (likely(cpy_r_r168 != NULL)) goto CPyL33;
    PyErr_SetString(PyExc_NameError, "value for final name \"TUPLE_CONTRACT_BYTECODE\" was not set");
    cpy_r_r169 = 0;
    if (unlikely(!cpy_r_r169)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 77, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL33: ;
    cpy_r_r170 = CPyStatics[43]; /* 'bytecode_runtime' */
    cpy_r_r171 = CPyStatic_TUPLE_CONTRACT_RUNTIME;
    if (likely(cpy_r_r171 != NULL)) goto CPyL36;
    PyErr_SetString(PyExc_NameError, "value for final name \"TUPLE_CONTRACT_RUNTIME\" was not set");
    cpy_r_r172 = 0;
    if (unlikely(!cpy_r_r172)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 78, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL36: ;
    cpy_r_r173 = CPyStatics[44]; /* 'abi' */
    cpy_r_r174 = CPyStatic_TUPLE_CONTRACT_ABI;
    if (likely(cpy_r_r174 != NULL)) goto CPyL39;
    PyErr_SetString(PyExc_NameError, "value for final name \"TUPLE_CONTRACT_ABI\" was not set");
    cpy_r_r175 = 0;
    if (unlikely(!cpy_r_r175)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 79, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL39: ;
    cpy_r_r176 = CPyDict_Build(3, cpy_r_r167, cpy_r_r168, cpy_r_r170, cpy_r_r171, cpy_r_r173, cpy_r_r174);
    if (unlikely(cpy_r_r176 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL76;
    }
    CPyStatic_TUPLE_CONTRACT_DATA = cpy_r_r176;
    CPy_INCREF(CPyStatic_TUPLE_CONTRACT_DATA);
    cpy_r_r177 = CPyStatic_globals;
    cpy_r_r178 = CPyStatics[45]; /* 'TUPLE_CONTRACT_DATA' */
    cpy_r_r179 = CPyDict_SetItem(cpy_r_r177, cpy_r_r178, cpy_r_r176);
    CPy_DECREF(cpy_r_r176);
    cpy_r_r180 = cpy_r_r179 >= 0;
    if (unlikely(!cpy_r_r180)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r181 = CPyStatics[46]; /* '0x6080604052348015600e575f5ffd5b5061067b8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80632655aef11461002d575b5f5ffd5b610047600480360381019061004291906103f1565b61005d565b6040516100549190610625565b60405180910390f35b61006561006d565b819050919050565b6040518060200160405280606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100db82610095565b810181811067ffffffffffffffff821117156100fa576100f96100a5565b5b80604052505050565b5f61010c610080565b905061011882826100d2565b919050565b5f5ffd5b5f5ffd5b5f67ffffffffffffffff82111561013f5761013e6100a5565b5b602082029050602081019050919050565b5f5ffd5b5f67ffffffffffffffff82111561016e5761016d6100a5565b5b602082029050602081019050919050565b5f819050919050565b6101918161017f565b811461019b575f5ffd5b50565b5f813590506101ac81610188565b92915050565b5f604082840312156101c7576101c6610091565b5b6101d16040610103565b90505f6101e08482850161019e565b5f8301525060206101f38482850161019e565b60208301525092915050565b5f61021161020c84610154565b610103565b9050808382526020820190506040840283018581111561023457610233610150565b5b835b8181101561025d578061024988826101b2565b845260208401935050604081019050610236565b5050509392505050565b5f82601f83011261027b5761027a610121565b5b813561028b8482602086016101ff565b91505092915050565b5f602082840312156102a9576102a8610091565b5b6102b36020610103565b90505f82013567ffffffffffffffff8111156102d2576102d161011d565b5b6102de84828501610267565b5f8301525092915050565b5f6102fb6102f684610125565b610103565b9050808382526020820190506020840283018581111561031e5761031d610150565b5b835b8181101561036557803567ffffffffffffffff81111561034357610342610121565b5b8086016103508982610294565b85526020850194505050602081019050610320565b5050509392505050565b5f82601f83011261038357610382610121565b5b81356103938482602086016102e9565b91505092915050565b5f602082840312156103b1576103b0610091565b5b6103bb6020610103565b90505f82013567ffffffffffffffff8111156103da576103d961011d565b5b6103e68482850161036f565b5f8301525092915050565b5f6020828403121561040657610405610089565b5b5f82013567ffffffffffffffff8111156104235761042261008d565b5b61042f8482850161039c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b6104938161017f565b82525050565b604082015f8201516104ad5f85018261048a565b5060208201516104c0602085018261048a565b50505050565b5f6104d18383610499565b60408301905092915050565b5f602082019050919050565b5f6104f382610461565b6104fd818561046b565b93506105088361047b565b805f5b8381101561053857815161051f88826104c6565b975061052a836104dd565b92505060018101905061050b565b5085935050505092915050565b5f602083015f8301518482035f86015261055f82826104e9565b9150508091505092915050565b5f6105778383610545565b905092915050565b5f602082019050919050565b5f61059582610438565b61059f8185610442565b9350836020820285016105b185610452565b805f5b858110156105ec57848403895281516105cd858261056c565b94506105d88361057f565b925060208a019950506001810190506105b4565b50829750879550505050505092915050565b5f602083015f8301518482035f860152610618828261058b565b9150508091505092915050565b5f6020820190508181035f83015261063d81846105fe565b90509291505056fea2646970667358221220e9a46dd271224211ac317ab5deb76259a8309e527c859b3d977cfc261a3780db64736f6c634300081e0033' */
    CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE = cpy_r_r181;
    CPy_INCREF(CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE);
    cpy_r_r182 = CPyStatic_globals;
    cpy_r_r183 = CPyStatics[47]; /* 'NESTED_TUPLE_CONTRACT_BYTECODE' */
    cpy_r_r184 = CPyDict_SetItem(cpy_r_r182, cpy_r_r183, cpy_r_r181);
    cpy_r_r185 = cpy_r_r184 >= 0;
    if (unlikely(!cpy_r_r185)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 84, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r186 = CPyStatics[48]; /* '0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80632655aef11461002d575b5f5ffd5b610047600480360381019061004291906103f1565b61005d565b6040516100549190610625565b60405180910390f35b61006561006d565b819050919050565b6040518060200160405280606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100db82610095565b810181811067ffffffffffffffff821117156100fa576100f96100a5565b5b80604052505050565b5f61010c610080565b905061011882826100d2565b919050565b5f5ffd5b5f5ffd5b5f67ffffffffffffffff82111561013f5761013e6100a5565b5b602082029050602081019050919050565b5f5ffd5b5f67ffffffffffffffff82111561016e5761016d6100a5565b5b602082029050602081019050919050565b5f819050919050565b6101918161017f565b811461019b575f5ffd5b50565b5f813590506101ac81610188565b92915050565b5f604082840312156101c7576101c6610091565b5b6101d16040610103565b90505f6101e08482850161019e565b5f8301525060206101f38482850161019e565b60208301525092915050565b5f61021161020c84610154565b610103565b9050808382526020820190506040840283018581111561023457610233610150565b5b835b8181101561025d578061024988826101b2565b845260208401935050604081019050610236565b5050509392505050565b5f82601f83011261027b5761027a610121565b5b813561028b8482602086016101ff565b91505092915050565b5f602082840312156102a9576102a8610091565b5b6102b36020610103565b90505f82013567ffffffffffffffff8111156102d2576102d161011d565b5b6102de84828501610267565b5f8301525092915050565b5f6102fb6102f684610125565b610103565b9050808382526020820190506020840283018581111561031e5761031d610150565b5b835b8181101561036557803567ffffffffffffffff81111561034357610342610121565b5b8086016103508982610294565b85526020850194505050602081019050610320565b5050509392505050565b5f82601f83011261038357610382610121565b5b81356103938482602086016102e9565b91505092915050565b5f602082840312156103b1576103b0610091565b5b6103bb6020610103565b90505f82013567ffffffffffffffff8111156103da576103d961011d565b5b6103e68482850161036f565b5f8301525092915050565b5f6020828403121561040657610405610089565b5b5f82013567ffffffffffffffff8111156104235761042261008d565b5b61042f8482850161039c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b6104938161017f565b82525050565b604082015f8201516104ad5f85018261048a565b5060208201516104c0602085018261048a565b50505050565b5f6104d18383610499565b60408301905092915050565b5f602082019050919050565b5f6104f382610461565b6104fd818561046b565b93506105088361047b565b805f5b8381101561053857815161051f88826104c6565b975061052a836104dd565b92505060018101905061050b565b5085935050505092915050565b5f602083015f8301518482035f86015261055f82826104e9565b9150508091505092915050565b5f6105778383610545565b905092915050565b5f602082019050919050565b5f61059582610438565b61059f8185610442565b9350836020820285016105b185610452565b805f5b858110156105ec57848403895281516105cd858261056c565b94506105d88361057f565b925060208a019950506001810190506105b4565b50829750879550505050505092915050565b5f602083015f8301518482035f860152610618828261058b565b9150508091505092915050565b5f6020820190508181035f83015261063d81846105fe565b90509291505056fea2646970667358221220e9a46dd271224211ac317ab5deb76259a8309e527c859b3d977cfc261a3780db64736f6c634300081e0033' */
    CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME = cpy_r_r186;
    CPy_INCREF(CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME);
    cpy_r_r187 = CPyStatic_globals;
    cpy_r_r188 = CPyStatics[49]; /* 'NESTED_TUPLE_CONTRACT_RUNTIME' */
    cpy_r_r189 = CPyDict_SetItem(cpy_r_r187, cpy_r_r188, cpy_r_r186);
    cpy_r_r190 = cpy_r_r189 >= 0;
    if (unlikely(!cpy_r_r190)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 85, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r191 = CPyStatics[14]; /* 'inputs' */
    cpy_r_r192 = CPyStatics[15]; /* 'components' */
    cpy_r_r193 = CPyStatics[15]; /* 'components' */
    cpy_r_r194 = CPyStatics[15]; /* 'components' */
    cpy_r_r195 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r196 = CPyStatics[23]; /* 'int256' */
    cpy_r_r197 = CPyStatics[18]; /* 'name' */
    cpy_r_r198 = CPyStatics[24]; /* 'x' */
    cpy_r_r199 = CPyStatics[20]; /* 'type' */
    cpy_r_r200 = CPyStatics[23]; /* 'int256' */
    cpy_r_r201 = CPyDict_Build(3, cpy_r_r195, cpy_r_r196, cpy_r_r197, cpy_r_r198, cpy_r_r199, cpy_r_r200);
    if (unlikely(cpy_r_r201 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 95, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r202 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r203 = CPyStatics[23]; /* 'int256' */
    cpy_r_r204 = CPyStatics[18]; /* 'name' */
    cpy_r_r205 = CPyStatics[26]; /* 'y' */
    cpy_r_r206 = CPyStatics[20]; /* 'type' */
    cpy_r_r207 = CPyStatics[23]; /* 'int256' */
    cpy_r_r208 = CPyDict_Build(3, cpy_r_r202, cpy_r_r203, cpy_r_r204, cpy_r_r205, cpy_r_r206, cpy_r_r207);
    if (unlikely(cpy_r_r208 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 100, CPyStatic_globals);
        goto CPyL93;
    }
    cpy_r_r209 = PyList_New(2);
    if (unlikely(cpy_r_r209 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 94, CPyStatic_globals);
        goto CPyL94;
    }
    cpy_r_r210 = (CPyPtr)&((PyListObject *)cpy_r_r209)->ob_item;
    cpy_r_r211 = *(CPyPtr *)cpy_r_r210;
    *(PyObject * *)cpy_r_r211 = cpy_r_r201;
    cpy_r_r212 = cpy_r_r211 + 8;
    *(PyObject * *)cpy_r_r212 = cpy_r_r208;
    cpy_r_r213 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r214 = CPyStatics[50]; /* 'struct NestedTupleContract.U[]' */
    cpy_r_r215 = CPyStatics[18]; /* 'name' */
    cpy_r_r216 = CPyStatics[51]; /* 'u' */
    cpy_r_r217 = CPyStatics[20]; /* 'type' */
    cpy_r_r218 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r219 = CPyDict_Build(4, cpy_r_r194, cpy_r_r209, cpy_r_r213, cpy_r_r214, cpy_r_r215, cpy_r_r216, cpy_r_r217, cpy_r_r218);
    CPy_DECREF_NO_IMM(cpy_r_r209);
    if (unlikely(cpy_r_r219 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 93, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r220 = PyList_New(1);
    if (unlikely(cpy_r_r220 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 92, CPyStatic_globals);
        goto CPyL95;
    }
    cpy_r_r221 = (CPyPtr)&((PyListObject *)cpy_r_r220)->ob_item;
    cpy_r_r222 = *(CPyPtr *)cpy_r_r221;
    *(PyObject * *)cpy_r_r222 = cpy_r_r219;
    cpy_r_r223 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r224 = CPyStatics[52]; /* 'struct NestedTupleContract.T[]' */
    cpy_r_r225 = CPyStatics[18]; /* 'name' */
    cpy_r_r226 = CPyStatics[53]; /* 't' */
    cpy_r_r227 = CPyStatics[20]; /* 'type' */
    cpy_r_r228 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r229 = CPyDict_Build(4, cpy_r_r193, cpy_r_r220, cpy_r_r223, cpy_r_r224, cpy_r_r225, cpy_r_r226, cpy_r_r227, cpy_r_r228);
    CPy_DECREF_NO_IMM(cpy_r_r220);
    if (unlikely(cpy_r_r229 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 91, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r230 = PyList_New(1);
    if (unlikely(cpy_r_r230 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 90, CPyStatic_globals);
        goto CPyL96;
    }
    cpy_r_r231 = (CPyPtr)&((PyListObject *)cpy_r_r230)->ob_item;
    cpy_r_r232 = *(CPyPtr *)cpy_r_r231;
    *(PyObject * *)cpy_r_r232 = cpy_r_r229;
    cpy_r_r233 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r234 = CPyStatics[54]; /* 'struct NestedTupleContract.S' */
    cpy_r_r235 = CPyStatics[18]; /* 'name' */
    cpy_r_r236 = CPyStatics[33]; /* 's' */
    cpy_r_r237 = CPyStatics[20]; /* 'type' */
    cpy_r_r238 = CPyStatics[34]; /* 'tuple' */
    cpy_r_r239 = CPyDict_Build(4, cpy_r_r192, cpy_r_r230, cpy_r_r233, cpy_r_r234, cpy_r_r235, cpy_r_r236, cpy_r_r237, cpy_r_r238);
    CPy_DECREF_NO_IMM(cpy_r_r230);
    if (unlikely(cpy_r_r239 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 89, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r240 = PyList_New(1);
    if (unlikely(cpy_r_r240 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 88, CPyStatic_globals);
        goto CPyL97;
    }
    cpy_r_r241 = (CPyPtr)&((PyListObject *)cpy_r_r240)->ob_item;
    cpy_r_r242 = *(CPyPtr *)cpy_r_r241;
    *(PyObject * *)cpy_r_r242 = cpy_r_r239;
    cpy_r_r243 = CPyStatics[18]; /* 'name' */
    cpy_r_r244 = CPyStatics[35]; /* 'method' */
    cpy_r_r245 = CPyStatics[36]; /* 'outputs' */
    cpy_r_r246 = CPyStatics[15]; /* 'components' */
    cpy_r_r247 = CPyStatics[15]; /* 'components' */
    cpy_r_r248 = CPyStatics[15]; /* 'components' */
    cpy_r_r249 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r250 = CPyStatics[23]; /* 'int256' */
    cpy_r_r251 = CPyStatics[18]; /* 'name' */
    cpy_r_r252 = CPyStatics[24]; /* 'x' */
    cpy_r_r253 = CPyStatics[20]; /* 'type' */
    cpy_r_r254 = CPyStatics[23]; /* 'int256' */
    cpy_r_r255 = CPyDict_Build(3, cpy_r_r249, cpy_r_r250, cpy_r_r251, cpy_r_r252, cpy_r_r253, cpy_r_r254);
    if (unlikely(cpy_r_r255 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 129, CPyStatic_globals);
        goto CPyL98;
    }
    cpy_r_r256 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r257 = CPyStatics[23]; /* 'int256' */
    cpy_r_r258 = CPyStatics[18]; /* 'name' */
    cpy_r_r259 = CPyStatics[26]; /* 'y' */
    cpy_r_r260 = CPyStatics[20]; /* 'type' */
    cpy_r_r261 = CPyStatics[23]; /* 'int256' */
    cpy_r_r262 = CPyDict_Build(3, cpy_r_r256, cpy_r_r257, cpy_r_r258, cpy_r_r259, cpy_r_r260, cpy_r_r261);
    if (unlikely(cpy_r_r262 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 134, CPyStatic_globals);
        goto CPyL99;
    }
    cpy_r_r263 = PyList_New(2);
    if (unlikely(cpy_r_r263 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 128, CPyStatic_globals);
        goto CPyL100;
    }
    cpy_r_r264 = (CPyPtr)&((PyListObject *)cpy_r_r263)->ob_item;
    cpy_r_r265 = *(CPyPtr *)cpy_r_r264;
    *(PyObject * *)cpy_r_r265 = cpy_r_r255;
    cpy_r_r266 = cpy_r_r265 + 8;
    *(PyObject * *)cpy_r_r266 = cpy_r_r262;
    cpy_r_r267 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r268 = CPyStatics[50]; /* 'struct NestedTupleContract.U[]' */
    cpy_r_r269 = CPyStatics[18]; /* 'name' */
    cpy_r_r270 = CPyStatics[51]; /* 'u' */
    cpy_r_r271 = CPyStatics[20]; /* 'type' */
    cpy_r_r272 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r273 = CPyDict_Build(4, cpy_r_r248, cpy_r_r263, cpy_r_r267, cpy_r_r268, cpy_r_r269, cpy_r_r270, cpy_r_r271, cpy_r_r272);
    CPy_DECREF_NO_IMM(cpy_r_r263);
    if (unlikely(cpy_r_r273 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 127, CPyStatic_globals);
        goto CPyL98;
    }
    cpy_r_r274 = PyList_New(1);
    if (unlikely(cpy_r_r274 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 126, CPyStatic_globals);
        goto CPyL101;
    }
    cpy_r_r275 = (CPyPtr)&((PyListObject *)cpy_r_r274)->ob_item;
    cpy_r_r276 = *(CPyPtr *)cpy_r_r275;
    *(PyObject * *)cpy_r_r276 = cpy_r_r273;
    cpy_r_r277 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r278 = CPyStatics[52]; /* 'struct NestedTupleContract.T[]' */
    cpy_r_r279 = CPyStatics[18]; /* 'name' */
    cpy_r_r280 = CPyStatics[53]; /* 't' */
    cpy_r_r281 = CPyStatics[20]; /* 'type' */
    cpy_r_r282 = CPyStatics[31]; /* 'tuple[]' */
    cpy_r_r283 = CPyDict_Build(4, cpy_r_r247, cpy_r_r274, cpy_r_r277, cpy_r_r278, cpy_r_r279, cpy_r_r280, cpy_r_r281, cpy_r_r282);
    CPy_DECREF_NO_IMM(cpy_r_r274);
    if (unlikely(cpy_r_r283 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 125, CPyStatic_globals);
        goto CPyL98;
    }
    cpy_r_r284 = PyList_New(1);
    if (unlikely(cpy_r_r284 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 124, CPyStatic_globals);
        goto CPyL102;
    }
    cpy_r_r285 = (CPyPtr)&((PyListObject *)cpy_r_r284)->ob_item;
    cpy_r_r286 = *(CPyPtr *)cpy_r_r285;
    *(PyObject * *)cpy_r_r286 = cpy_r_r283;
    cpy_r_r287 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r288 = CPyStatics[54]; /* 'struct NestedTupleContract.S' */
    cpy_r_r289 = CPyStatics[18]; /* 'name' */
    cpy_r_r290 = CPyStatics[37]; /* '' */
    cpy_r_r291 = CPyStatics[20]; /* 'type' */
    cpy_r_r292 = CPyStatics[34]; /* 'tuple' */
    cpy_r_r293 = CPyDict_Build(4, cpy_r_r246, cpy_r_r284, cpy_r_r287, cpy_r_r288, cpy_r_r289, cpy_r_r290, cpy_r_r291, cpy_r_r292);
    CPy_DECREF_NO_IMM(cpy_r_r284);
    if (unlikely(cpy_r_r293 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 123, CPyStatic_globals);
        goto CPyL98;
    }
    cpy_r_r294 = PyList_New(1);
    if (unlikely(cpy_r_r294 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 122, CPyStatic_globals);
        goto CPyL103;
    }
    cpy_r_r295 = (CPyPtr)&((PyListObject *)cpy_r_r294)->ob_item;
    cpy_r_r296 = *(CPyPtr *)cpy_r_r295;
    *(PyObject * *)cpy_r_r296 = cpy_r_r293;
    cpy_r_r297 = CPyStatics[38]; /* 'stateMutability' */
    cpy_r_r298 = CPyStatics[39]; /* 'pure' */
    cpy_r_r299 = CPyStatics[20]; /* 'type' */
    cpy_r_r300 = CPyStatics[40]; /* 'function' */
    cpy_r_r301 = CPyDict_Build(5, cpy_r_r191, cpy_r_r240, cpy_r_r243, cpy_r_r244, cpy_r_r245, cpy_r_r294, cpy_r_r297, cpy_r_r298, cpy_r_r299, cpy_r_r300);
    CPy_DECREF_NO_IMM(cpy_r_r240);
    CPy_DECREF_NO_IMM(cpy_r_r294);
    if (unlikely(cpy_r_r301 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 87, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r302 = PyList_New(1);
    if (unlikely(cpy_r_r302 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 86, CPyStatic_globals);
        goto CPyL104;
    }
    cpy_r_r303 = (CPyPtr)&((PyListObject *)cpy_r_r302)->ob_item;
    cpy_r_r304 = *(CPyPtr *)cpy_r_r303;
    *(PyObject * *)cpy_r_r304 = cpy_r_r301;
    CPyStatic_NESTED_TUPLE_CONTRACT_ABI = cpy_r_r302;
    CPy_INCREF_NO_IMM(CPyStatic_NESTED_TUPLE_CONTRACT_ABI);
    cpy_r_r305 = CPyStatic_globals;
    cpy_r_r306 = CPyStatics[55]; /* 'NESTED_TUPLE_CONTRACT_ABI' */
    cpy_r_r307 = CPyDict_SetItem(cpy_r_r305, cpy_r_r306, cpy_r_r302);
    CPy_DECREF_NO_IMM(cpy_r_r302);
    cpy_r_r308 = cpy_r_r307 >= 0;
    if (unlikely(!cpy_r_r308)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 86, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r309 = CPyStatics[42]; /* 'bytecode' */
    cpy_r_r310 = CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE;
    if (likely(cpy_r_r310 != NULL)) goto CPyL67;
    PyErr_SetString(PyExc_NameError, "value for final name \"NESTED_TUPLE_CONTRACT_BYTECODE\" was not set");
    cpy_r_r311 = 0;
    if (unlikely(!cpy_r_r311)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 160, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL67: ;
    cpy_r_r312 = CPyStatics[43]; /* 'bytecode_runtime' */
    cpy_r_r313 = CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME;
    if (likely(cpy_r_r313 != NULL)) goto CPyL70;
    PyErr_SetString(PyExc_NameError, "value for final name \"NESTED_TUPLE_CONTRACT_RUNTIME\" was not set");
    cpy_r_r314 = 0;
    if (unlikely(!cpy_r_r314)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 161, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL70: ;
    cpy_r_r315 = CPyStatics[44]; /* 'abi' */
    cpy_r_r316 = CPyStatic_NESTED_TUPLE_CONTRACT_ABI;
    if (likely(cpy_r_r316 != NULL)) goto CPyL73;
    PyErr_SetString(PyExc_NameError, "value for final name \"NESTED_TUPLE_CONTRACT_ABI\" was not set");
    cpy_r_r317 = 0;
    if (unlikely(!cpy_r_r317)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 162, CPyStatic_globals);
        goto CPyL76;
    }
    CPy_Unreachable();
CPyL73: ;
    cpy_r_r318 = CPyDict_Build(3, cpy_r_r309, cpy_r_r310, cpy_r_r312, cpy_r_r313, cpy_r_r315, cpy_r_r316);
    if (unlikely(cpy_r_r318 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 159, CPyStatic_globals);
        goto CPyL76;
    }
    CPyStatic_NESTED_TUPLE_CONTRACT_DATA = cpy_r_r318;
    CPy_INCREF(CPyStatic_NESTED_TUPLE_CONTRACT_DATA);
    cpy_r_r319 = CPyStatic_globals;
    cpy_r_r320 = CPyStatics[56]; /* 'NESTED_TUPLE_CONTRACT_DATA' */
    cpy_r_r321 = CPyDict_SetItem(cpy_r_r319, cpy_r_r320, cpy_r_r318);
    CPy_DECREF(cpy_r_r318);
    cpy_r_r322 = cpy_r_r321 >= 0;
    if (unlikely(!cpy_r_r322)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/tuple_contracts.py", "<module>", 159, CPyStatic_globals);
        goto CPyL76;
    }
    return 1;
CPyL76: ;
    cpy_r_r323 = 2;
    return cpy_r_r323;
CPyL77: ;
    CPy_DecRef(cpy_r_r31);
    goto CPyL76;
CPyL78: ;
    CPy_DecRef(cpy_r_r31);
    CPy_DecRef(cpy_r_r38);
    goto CPyL76;
CPyL79: ;
    CPy_DecRef(cpy_r_r31);
    CPy_DecRef(cpy_r_r38);
    CPy_DecRef(cpy_r_r46);
    goto CPyL76;
CPyL80: ;
    CPy_DecRef(cpy_r_r31);
    CPy_DecRef(cpy_r_r38);
    CPy_DecRef(cpy_r_r46);
    CPy_DecRef(cpy_r_r53);
    goto CPyL76;
CPyL81: ;
    CPy_DecRef(cpy_r_r31);
    CPy_DecRef(cpy_r_r38);
    CPy_DecRef(cpy_r_r46);
    CPy_DecRef(cpy_r_r53);
    CPy_DecRef(cpy_r_r60);
    goto CPyL76;
CPyL82: ;
    CPy_DecRef(cpy_r_r31);
    CPy_DecRef(cpy_r_r38);
    CPy_DecRef(cpy_r_r72);
    goto CPyL76;
CPyL83: ;
    CPy_DecRef(cpy_r_r84);
    goto CPyL76;
CPyL84: ;
    CPy_DecRef(cpy_r_r85);
    goto CPyL76;
CPyL85: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    goto CPyL76;
CPyL86: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    CPy_DecRef(cpy_r_r105);
    goto CPyL76;
CPyL87: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r113);
    goto CPyL76;
CPyL88: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r120);
    goto CPyL76;
CPyL89: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r113);
    CPy_DecRef(cpy_r_r120);
    CPy_DecRef(cpy_r_r127);
    goto CPyL76;
CPyL90: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r98);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r139);
    goto CPyL76;
CPyL91: ;
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r151);
    goto CPyL76;
CPyL92: ;
    CPy_DecRef(cpy_r_r159);
    goto CPyL76;
CPyL93: ;
    CPy_DecRef(cpy_r_r201);
    goto CPyL76;
CPyL94: ;
    CPy_DecRef(cpy_r_r201);
    CPy_DecRef(cpy_r_r208);
    goto CPyL76;
CPyL95: ;
    CPy_DecRef(cpy_r_r219);
    goto CPyL76;
CPyL96: ;
    CPy_DecRef(cpy_r_r229);
    goto CPyL76;
CPyL97: ;
    CPy_DecRef(cpy_r_r239);
    goto CPyL76;
CPyL98: ;
    CPy_DecRef(cpy_r_r240);
    goto CPyL76;
CPyL99: ;
    CPy_DecRef(cpy_r_r240);
    CPy_DecRef(cpy_r_r255);
    goto CPyL76;
CPyL100: ;
    CPy_DecRef(cpy_r_r240);
    CPy_DecRef(cpy_r_r255);
    CPy_DecRef(cpy_r_r262);
    goto CPyL76;
CPyL101: ;
    CPy_DecRef(cpy_r_r240);
    CPy_DecRef(cpy_r_r273);
    goto CPyL76;
CPyL102: ;
    CPy_DecRef(cpy_r_r240);
    CPy_DecRef(cpy_r_r283);
    goto CPyL76;
CPyL103: ;
    CPy_DecRef(cpy_r_r240);
    CPy_DecRef(cpy_r_r293);
    goto CPyL76;
CPyL104: ;
    CPy_DecRef(cpy_r_r301);
    goto CPyL76;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts = Py_None;
    CPyModule_builtins = Py_None;
    CPyModule_typing = Py_None;
    CPyModule_eth_typing = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[59];
const char * const CPyLit_Str[] = {
    "\a\bbuiltins\005Final\004List\006typing\nABIElement\006HexStr\neth_typing",
    "\001\252\n0x6080604052348015600e575f5ffd5b50610a688061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80638e1ae3c71461002d575b5f5ffd5b6100476004803603810190610042919061064d565b61005d565b6040516100549190610a12565b60405180910390f35b61006561006d565b819050919050565b60405180606001604052805f815260200160608152602001606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100e8826100a2565b810181811067ffffffffffffffff82111715610107576101066100b2565b5b80604052505050565b5f61011961008d565b905061012582826100df565b919050565b5f5ffd5b5f819050919050565b6101408161012e565b811461014a575f5ffd5b50565b5f8135905061015b81610137565b92915050565b5f5ffd5b5f67ffffffffffffffff82111561017f5761017e6100b2565b5b602082029050602081019050919050565b5f5ffd5b5f6101a66101a184610165565b610110565b905080838252602082019050602084028301858111156101c9576101c8610190565b5b835b818110156101f257806101de888261014d565b8452602084019350506020810190506101cb565b5050509392505050565b5f82601f8301126102105761020f610161565b5b8135610220848260208601610194565b91505092915050565b5f67ffffffffffffffff821115610243576102426100b2565b5b602082029050602081019050919050565b5f819050919050565b61026681610254565b8114610270575f5ffd5b50565b5f813590506102818161025d565b92915050565b5f67ffffffffffffffff8211156102a1576102a06100b2565b5b602082029050919050565b5f8115159050919050565b6102c0816102ac565b81146102ca575f5ffd5b50565b5f813590506102db816102b7565b92915050565b5f6102f36102ee84610287565b610110565b9050806020840283018581111561030d5761030c610190565b5b835b81811015610336578061032288826102cd565b84526020840193505060208101905061030f565b5050509392505050565b5f82601f83011261035457610353610161565b5b60026103618482856102e1565b91505092915050565b5f67ffffffffffffffff821115610384576103836100b2565b5b602082029050602081019050919050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103be82610395565b9050919050565b6103ce816103b4565b81146103d8575f5ffd5b50565b5f813590506103e9816103c5565b92915050565b5f6104016103fc8461036a565b610110565b9050808382526020820190506020840283018581111561042457610423610190565b5b835b8181101561044d578061043988826103db565b845260208401935050602081019050610426565b5050509392505050565b5f82601f83011261046b5761046a610161565b5b813561047b8482602086016103ef565b91505092915050565b5f608082840312156104995761049861009e565b5b6104a36060610110565b90505f6104b284828501610273565b5f8301525060206104c584828501610340565b602083015250606082013567ffffffffffffffff8111156104e9576104e861012a565b5b6104f584828501610457565b60408301525092915050565b5f61051361050e84610229565b610110565b9050808382526020820190506020840283018581111561053657610535610190565b5b835b8181101561057d57803567ffffffffffffffff81111561055b5761055a610161565b5b8086016105688982610484565b85526020850194505050602081019050610538565b5050509392505050565b5f82601f83011261059b5761059a610161565b5b81356105ab848260208601610501565b91505092915050565b5f606082840312156105c9576105c861009e565b5b6105d36060610110565b90505f6105e28482850161014d565b5f83015250602082013567ffffffffffffffff8111156106055761060461012a565b5b610611848285016101fc565b602083015250604082013567ffffffffffffffff8111156106355761063461012a565b5b61064184828501610587565b60408301525092915050565b5f6020828403121561066257610661610096565b5b5f82013567ffffffffffffffff81111561067f5761067e61009a565b5b61068b848285016105b4565b91505092915050565b61069d8161012e565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f6106d78383610694565b60208301905092915050565b5f602082019050919050565b5f6106f9826106a3565b61070381856106ad565b935061070e836106bd565b805f5b8381101561073e57815161072588826106cc565b9750610730836106e3565b925050600181019050610711565b5085935050505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61077d81610254565b82525050565b5f60029050919050565b5f81905092915050565b5f819050919050565b6107a9816102ac565b82525050565b5f6107ba83836107a0565b60208301905092915050565b5f602082019050919050565b6107db81610783565b6107e5818461078d565b92506107f082610797565b805f5b8381101561082057815161080787826107af565b9650610812836107c6565b9250506001810190506107f3565b505050505050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61085a816103b4565b82525050565b5f61086b8383610851565b60208301905092915050565b5f602082019050919050565b5f61088d82610828565b6108978185610832565b93506108a283610842565b805f5b838110156108d25781516108b98882610860565b97506108c483610877565b9250506001810190506108a5565b5085935050505092915050565b5f608083015f8301516108f45f860182610774565b50602083015161090760208601826107d2565b506040830151848203606086015261091f8282610883565b9150508091505092915050565b5f61093783836108df565b905092915050565b5f602082019050919050565b5f6109558261074b565b61095f8185610755565b93508360208202850161097185610765565b805f5b858110156109ac578484038952815161098d858261092c565b94506109988361093f565b925060208a01995050600181019050610974565b50829750879550505050505092915050565b5f606083015f8301516109d35f860182610694565b50602083015184820360208601526109eb82826106ef565b91505060408301518482036040860152610a05828261094b565b9150508091505092915050565b5f6020820190508181035f830152610a2a81846109be565b90509291505056fea26469706673582212207c5620c2257d173ed894791417ffad7e98aad1aab11d2ec22b5148e5d77de0c464736f6c634300081e0033",
    "\001\027TUPLE_CONTRACT_BYTECODE",
    "\001\251R0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80638e1ae3c71461002d575b5f5ffd5b6100476004803603810190610042919061064d565b61005d565b6040516100549190610a12565b60405180910390f35b61006561006d565b819050919050565b60405180606001604052805f815260200160608152602001606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100e8826100a2565b810181811067ffffffffffffffff82111715610107576101066100b2565b5b80604052505050565b5f61011961008d565b905061012582826100df565b919050565b5f5ffd5b5f819050919050565b6101408161012e565b811461014a575f5ffd5b50565b5f8135905061015b81610137565b92915050565b5f5ffd5b5f67ffffffffffffffff82111561017f5761017e6100b2565b5b602082029050602081019050919050565b5f5ffd5b5f6101a66101a184610165565b610110565b905080838252602082019050602084028301858111156101c9576101c8610190565b5b835b818110156101f257806101de888261014d565b8452602084019350506020810190506101cb565b5050509392505050565b5f82601f8301126102105761020f610161565b5b8135610220848260208601610194565b91505092915050565b5f67ffffffffffffffff821115610243576102426100b2565b5b602082029050602081019050919050565b5f819050919050565b61026681610254565b8114610270575f5ffd5b50565b5f813590506102818161025d565b92915050565b5f67ffffffffffffffff8211156102a1576102a06100b2565b5b602082029050919050565b5f8115159050919050565b6102c0816102ac565b81146102ca575f5ffd5b50565b5f813590506102db816102b7565b92915050565b5f6102f36102ee84610287565b610110565b9050806020840283018581111561030d5761030c610190565b5b835b81811015610336578061032288826102cd565b84526020840193505060208101905061030f565b5050509392505050565b5f82601f83011261035457610353610161565b5b60026103618482856102e1565b91505092915050565b5f67ffffffffffffffff821115610384576103836100b2565b5b602082029050602081019050919050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103be82610395565b9050919050565b6103ce816103b4565b81146103d8575f5ffd5b50565b5f813590506103e9816103c5565b92915050565b5f6104016103fc8461036a565b610110565b9050808382526020820190506020840283018581111561042457610423610190565b5b835b8181101561044d578061043988826103db565b845260208401935050602081019050610426565b5050509392505050565b5f82601f83011261046b5761046a610161565b5b813561047b8482602086016103ef565b91505092915050565b5f608082840312156104995761049861009e565b5b6104a36060610110565b90505f6104b284828501610273565b5f8301525060206104c584828501610340565b602083015250606082013567ffffffffffffffff8111156104e9576104e861012a565b5b6104f584828501610457565b60408301525092915050565b5f61051361050e84610229565b610110565b9050808382526020820190506020840283018581111561053657610535610190565b5b835b8181101561057d57803567ffffffffffffffff81111561055b5761055a610161565b5b8086016105688982610484565b85526020850194505050602081019050610538565b5050509392505050565b5f82601f83011261059b5761059a610161565b5b81356105ab848260208601610501565b91505092915050565b5f606082840312156105c9576105c861009e565b5b6105d36060610110565b90505f6105e28482850161014d565b5f83015250602082013567ffffffffffffffff8111156106055761060461012a565b5b610611848285016101fc565b602083015250604082013567ffffffffffffffff8111156106355761063461012a565b5b61064184828501610587565b60408301525092915050565b5f6020828403121561066257610661610096565b5b5f82013567ffffffffffffffff81111561067f5761067e61009a565b5b61068b848285016105b4565b91505092915050565b61069d8161012e565b82525050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f6106d78383610694565b60208301905092915050565b5f602082019050919050565b5f6106f9826106a3565b61070381856106ad565b935061070e836106bd565b805f5b8381101561073e57815161072588826106cc565b9750610730836106e3565b925050600181019050610711565b5085935050505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61077d81610254565b82525050565b5f60029050919050565b5f81905092915050565b5f819050919050565b6107a9816102ac565b82525050565b5f6107ba83836107a0565b60208301905092915050565b5f602082019050919050565b6107db81610783565b6107e5818461078d565b92506107f082610797565b805f5b8381101561082057815161080787826107af565b9650610812836107c6565b9250506001810190506107f3565b505050505050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b61085a816103b4565b82525050565b5f61086b8383610851565b60208301905092915050565b5f602082019050919050565b5f61088d82610828565b6108978185610832565b93506108a283610842565b805f5b838110156108d25781516108b98882610860565b97506108c483610877565b9250506001810190506108a5565b5085935050505092915050565b5f608083015f8301516108f45f860182610774565b50602083015161090760208601826107d2565b506040830151848203606086015261091f8282610883565b9150508091505092915050565b5f61093783836108df565b905092915050565b5f602082019050919050565b5f6109558261074b565b61095f8185610755565b93508360208202850161097185610765565b805f5b858110156109ac578484038952815161098d858261092c565b94506109988361093f565b925060208a01995050600181019050610974565b50829750879550505050505092915050565b5f606083015f8301516109d35f860182610694565b50602083015184820360208601526109eb82826106ef565b91505060408301518482036040860152610a05828261094b565b9150508091505092915050565b5f6020820190508181035f830152610a2a81846109be565b90509291505056fea26469706673582212207c5620c2257d173ed894791417ffad7e98aad1aab11d2ec22b5148e5d77de0c464736f6c634300081e0033",
    "\a\026TUPLE_CONTRACT_RUNTIME\006inputs\ncomponents\finternalType\auint256\004name\001a",
    "\t\004type\tuint256[]\001b\006int256\001x\abool[2]\001y\taddress[]\001z",
    "\006\030struct TupleContract.T[]\001c\atuple[]\026struct TupleContract.S\001s\005tuple",
    "\a\006method\aoutputs\000\017stateMutability\004pure\bfunction\022TUPLE_CONTRACT_ABI",
    "\004\bbytecode\020bytecode_runtime\003abi\023TUPLE_CONTRACT_DATA",
    "\001\23200x6080604052348015600e575f5ffd5b5061067b8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80632655aef11461002d575b5f5ffd5b610047600480360381019061004291906103f1565b61005d565b6040516100549190610625565b60405180910390f35b61006561006d565b819050919050565b6040518060200160405280606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100db82610095565b810181811067ffffffffffffffff821117156100fa576100f96100a5565b5b80604052505050565b5f61010c610080565b905061011882826100d2565b919050565b5f5ffd5b5f5ffd5b5f67ffffffffffffffff82111561013f5761013e6100a5565b5b602082029050602081019050919050565b5f5ffd5b5f67ffffffffffffffff82111561016e5761016d6100a5565b5b602082029050602081019050919050565b5f819050919050565b6101918161017f565b811461019b575f5ffd5b50565b5f813590506101ac81610188565b92915050565b5f604082840312156101c7576101c6610091565b5b6101d16040610103565b90505f6101e08482850161019e565b5f8301525060206101f38482850161019e565b60208301525092915050565b5f61021161020c84610154565b610103565b9050808382526020820190506040840283018581111561023457610233610150565b5b835b8181101561025d578061024988826101b2565b845260208401935050604081019050610236565b5050509392505050565b5f82601f83011261027b5761027a610121565b5b813561028b8482602086016101ff565b91505092915050565b5f602082840312156102a9576102a8610091565b5b6102b36020610103565b90505f82013567ffffffffffffffff8111156102d2576102d161011d565b5b6102de84828501610267565b5f8301525092915050565b5f6102fb6102f684610125565b610103565b9050808382526020820190506020840283018581111561031e5761031d610150565b5b835b8181101561036557803567ffffffffffffffff81111561034357610342610121565b5b8086016103508982610294565b85526020850194505050602081019050610320565b5050509392505050565b5f82601f83011261038357610382610121565b5b81356103938482602086016102e9565b91505092915050565b5f602082840312156103b1576103b0610091565b5b6103bb6020610103565b90505f82013567ffffffffffffffff8111156103da576103d961011d565b5b6103e68482850161036f565b5f8301525092915050565b5f6020828403121561040657610405610089565b5b5f82013567ffffffffffffffff8111156104235761042261008d565b5b61042f8482850161039c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b6104938161017f565b82525050565b604082015f8201516104ad5f85018261048a565b5060208201516104c0602085018261048a565b50505050565b5f6104d18383610499565b60408301905092915050565b5f602082019050919050565b5f6104f382610461565b6104fd818561046b565b93506105088361047b565b805f5b8381101561053857815161051f88826104c6565b975061052a836104dd565b92505060018101905061050b565b5085935050505092915050565b5f602083015f8301518482035f86015261055f82826104e9565b9150508091505092915050565b5f6105778383610545565b905092915050565b5f602082019050919050565b5f61059582610438565b61059f8185610442565b9350836020820285016105b185610452565b805f5b858110156105ec57848403895281516105cd858261056c565b94506105d88361057f565b925060208a019950506001810190506105b4565b50829750879550505050505092915050565b5f602083015f8301518482035f860152610618828261058b565b9150508091505092915050565b5f6020820190508181035f83015261063d81846105fe565b90509291505056fea2646970667358221220e9a46dd271224211ac317ab5deb76259a8309e527c859b3d977cfc261a3780db64736f6c634300081e0033",
    "\001\036NESTED_TUPLE_CONTRACT_BYTECODE",
    "\001\231x0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80632655aef11461002d575b5f5ffd5b610047600480360381019061004291906103f1565b61005d565b6040516100549190610625565b60405180910390f35b61006561006d565b819050919050565b6040518060200160405280606081525090565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100db82610095565b810181811067ffffffffffffffff821117156100fa576100f96100a5565b5b80604052505050565b5f61010c610080565b905061011882826100d2565b919050565b5f5ffd5b5f5ffd5b5f67ffffffffffffffff82111561013f5761013e6100a5565b5b602082029050602081019050919050565b5f5ffd5b5f67ffffffffffffffff82111561016e5761016d6100a5565b5b602082029050602081019050919050565b5f819050919050565b6101918161017f565b811461019b575f5ffd5b50565b5f813590506101ac81610188565b92915050565b5f604082840312156101c7576101c6610091565b5b6101d16040610103565b90505f6101e08482850161019e565b5f8301525060206101f38482850161019e565b60208301525092915050565b5f61021161020c84610154565b610103565b9050808382526020820190506040840283018581111561023457610233610150565b5b835b8181101561025d578061024988826101b2565b845260208401935050604081019050610236565b5050509392505050565b5f82601f83011261027b5761027a610121565b5b813561028b8482602086016101ff565b91505092915050565b5f602082840312156102a9576102a8610091565b5b6102b36020610103565b90505f82013567ffffffffffffffff8111156102d2576102d161011d565b5b6102de84828501610267565b5f8301525092915050565b5f6102fb6102f684610125565b610103565b9050808382526020820190506020840283018581111561031e5761031d610150565b5b835b8181101561036557803567ffffffffffffffff81111561034357610342610121565b5b8086016103508982610294565b85526020850194505050602081019050610320565b5050509392505050565b5f82601f83011261038357610382610121565b5b81356103938482602086016102e9565b91505092915050565b5f602082840312156103b1576103b0610091565b5b6103bb6020610103565b90505f82013567ffffffffffffffff8111156103da576103d961011d565b5b6103e68482850161036f565b5f8301525092915050565b5f6020828403121561040657610405610089565b5b5f82013567ffffffffffffffff8111156104235761042261008d565b5b61042f8482850161039c565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b5f81519050919050565b5f82825260208201905092915050565b5f819050602082019050919050565b6104938161017f565b82525050565b604082015f8201516104ad5f85018261048a565b5060208201516104c0602085018261048a565b50505050565b5f6104d18383610499565b60408301905092915050565b5f602082019050919050565b5f6104f382610461565b6104fd818561046b565b93506105088361047b565b805f5b8381101561053857815161051f88826104c6565b975061052a836104dd565b92505060018101905061050b565b5085935050505092915050565b5f602083015f8301518482035f86015261055f82826104e9565b9150508091505092915050565b5f6105778383610545565b905092915050565b5f602082019050919050565b5f61059582610438565b61059f8185610442565b9350836020820285016105b185610452565b805f5b858110156105ec57848403895281516105cd858261056c565b94506105d88361057f565b925060208a019950506001810190506105b4565b50829750879550505050505092915050565b5f602083015f8301518482035f860152610618828261058b565b9150508091505092915050565b5f6020820190508181035f83015261063d81846105fe565b90509291505056fea2646970667358221220e9a46dd271224211ac317ab5deb76259a8309e527c859b3d977cfc261a3780db64736f6c634300081e0033",
    "\003\035NESTED_TUPLE_CONTRACT_RUNTIME\036struct NestedTupleContract.U[]\001u",
    "\003\036struct NestedTupleContract.T[]\001t\034struct NestedTupleContract.S",
    "\002\031NESTED_TUPLE_CONTRACT_ABI\032NESTED_TUPLE_CONTRACT_DATA",
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
const int CPyLit_Tuple[] = {2, 2, 4, 5, 2, 7, 8};
const int CPyLit_FrozenSet[] = {0};
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___tuple_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
CPyModule *CPyModule_typing;
CPyModule *CPyModule_eth_typing;
PyObject *CPyStatic_TUPLE_CONTRACT_BYTECODE = NULL;
PyObject *CPyStatic_TUPLE_CONTRACT_RUNTIME = NULL;
PyObject *CPyStatic_TUPLE_CONTRACT_ABI = NULL;
PyObject *CPyStatic_TUPLE_CONTRACT_DATA = NULL;
PyObject *CPyStatic_NESTED_TUPLE_CONTRACT_BYTECODE = NULL;
PyObject *CPyStatic_NESTED_TUPLE_CONTRACT_RUNTIME = NULL;
PyObject *CPyStatic_NESTED_TUPLE_CONTRACT_ABI = NULL;
PyObject *CPyStatic_NESTED_TUPLE_CONTRACT_DATA = NULL;
char CPyDef___top_level__(void);

static int exec_tuple_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___tuple_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___tuple_contracts, "faster_web3._utils.contract_sources.contract_data.tuple_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___tuple_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___tuple_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_tuple_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.tuple_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_tuple_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_tuple_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_tuple_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
