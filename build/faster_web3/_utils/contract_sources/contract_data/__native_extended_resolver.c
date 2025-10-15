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
#include "__native_extended_resolver.h"
#include "__native_internal_extended_resolver.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___extended_resolver(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.extended_resolver",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___extended_resolver(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___extended_resolver(CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal;
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
    CPyPtr cpy_r_r70;
    CPyPtr cpy_r_r71;
    CPyPtr cpy_r_r72;
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
    PyObject *cpy_r_r103;
    CPyPtr cpy_r_r104;
    CPyPtr cpy_r_r105;
    CPyPtr cpy_r_r106;
    CPyPtr cpy_r_r107;
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
    CPyPtr cpy_r_r119;
    CPyPtr cpy_r_r120;
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
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
    PyObject *cpy_r_r155;
    CPyPtr cpy_r_r156;
    CPyPtr cpy_r_r157;
    PyObject *cpy_r_r158;
    PyObject *cpy_r_r159;
    PyObject *cpy_r_r160;
    PyObject *cpy_r_r161;
    PyObject *cpy_r_r162;
    PyObject *cpy_r_r163;
    PyObject *cpy_r_r164;
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
    PyObject *cpy_r_r183;
    PyObject *cpy_r_r184;
    PyObject *cpy_r_r185;
    CPyPtr cpy_r_r186;
    CPyPtr cpy_r_r187;
    CPyPtr cpy_r_r188;
    CPyPtr cpy_r_r189;
    PyObject *cpy_r_r190;
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
    CPyPtr cpy_r_r208;
    CPyPtr cpy_r_r209;
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
    CPyPtr cpy_r_r221;
    CPyPtr cpy_r_r222;
    PyObject *cpy_r_r223;
    PyObject *cpy_r_r224;
    PyObject *cpy_r_r225;
    PyObject *cpy_r_r226;
    PyObject *cpy_r_r227;
    PyObject *cpy_r_r228;
    CPyPtr cpy_r_r229;
    CPyPtr cpy_r_r230;
    CPyPtr cpy_r_r231;
    CPyPtr cpy_r_r232;
    CPyPtr cpy_r_r233;
    CPyPtr cpy_r_r234;
    CPyPtr cpy_r_r235;
    PyObject *cpy_r_r236;
    PyObject *cpy_r_r237;
    int32_t cpy_r_r238;
    char cpy_r_r239;
    PyObject *cpy_r_r240;
    PyObject *cpy_r_r241;
    PyObject *cpy_r_r242;
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
    int32_t cpy_r_r258;
    char cpy_r_r259;
    char cpy_r_r260;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", -1, CPyStatic_globals);
        goto CPyL49;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x608060405234801561000f575f5ffd5b50604051610d0e380380610d0e833981810160405281019061003191906100e5565b805f5f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610110565b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b5f6100b482610099565b9050919050565b6100c4816100aa565b81146100ce575f5ffd5b50565b5f815190506100df816100bb565b92915050565b5f602082840312156100fa576100f9610076565b5b5f610107848285016100d1565b91505092915050565b610bf18061011d5f395ff3fe608060405234801561000f575f5ffd5b506004361061004a575f3560e01c806301ffc9a71461004e5780633e9ce7941461007e5780639061b9231461009a578063f86bc879146100ca575b5f5ffd5b61006860048036038101906100639190610539565b6100fa565b604051610075919061057e565b60405180910390f35b6100986004803603810190610093919061064e565b61015a565b005b6100b460048036038101906100af91906106ff565b61023a565b6040516100c191906107ed565b60405180910390f35b6100e460048036038101906100df919061080d565b610457565b6040516100f1919061057e565b60405180910390f35b5f639061b92360e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061015357506101528261048c565b5b9050919050565b8060015f8581526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055507fe1c5610a6e0cbe10764ecd182adcef1ec338dc4e199c99c32ce98f38e12791df8333848460405161022d949392919061087b565b60405180910390a1505050565b60606040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012085856040516102899291906108fa565b60405180910390201480156102a2575060248383905010155b15610352577ff0a378cc2afe91730d0105e67d6bb037cc5b8b6bfec5b5962d9b637ff6497e555f1b83836004906024926102de9392919061091a565b906102e9919061096a565b14610329576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032090610a48565b60405180910390fd5b61beef60405160200161033c9190610a66565b604051602081830303815290604052905061044f565b5f85855f81811061036657610365610a7f565b5b9050013560f81c60f81b60f81c60ff1690506040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012086868360016103c49190610ae2565b9080926103d39392919061091a565b6040516103e1929190610b15565b604051809103902014610429576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161042090610b9d565b60405180910390fd5b61dead60405160200161043c9190610a66565b6040516020818303038152906040529150505b949350505050565b6001602052825f5260405f20602052815f5260405f20602052805f5260405f205f92509250509054906101000a900460ff1681565b5f6301ffc9a760e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f5ffd5b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b610518816104e4565b8114610522575f5ffd5b50565b5f813590506105338161050f565b92915050565b5f6020828403121561054e5761054d6104dc565b5b5f61055b84828501610525565b91505092915050565b5f8115159050919050565b61057881610564565b82525050565b5f6020820190506105915f83018461056f565b92915050565b5f819050919050565b6105a981610597565b81146105b3575f5ffd5b50565b5f813590506105c4816105a0565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105f3826105ca565b9050919050565b610603816105e9565b811461060d575f5ffd5b50565b5f8135905061061e816105fa565b92915050565b61062d81610564565b8114610637575f5ffd5b50565b5f8135905061064881610624565b92915050565b5f5f5f60608486031215610665576106646104dc565b5b5f610672868287016105b6565b935050602061068386828701610610565b92505060406106948682870161063a565b9150509250925092565b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f8401126106bf576106be61069e565b5b8235905067ffffffffffffffff8111156106dc576106db6106a2565b5b6020830191508360018202830111156106f8576106f76106a6565b5b9250929050565b5f5f5f5f60408587031215610717576107166104dc565b5b5f85013567ffffffffffffffff811115610734576107336104e0565b5b610740878288016106aa565b9450945050602085013567ffffffffffffffff811115610763576107626104e0565b5b61076f878288016106aa565b925092505092959194509250565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6107bf8261077d565b6107c98185610787565b93506107d9818560208601610797565b6107e2816107a5565b840191505092915050565b5f6020820190508181035f83015261080581846107b5565b905092915050565b5f5f5f60608486031215610824576108236104dc565b5b5f610831868287016105b6565b935050602061084286828701610610565b925050604061085386828701610610565b9150509250925092565b61086681610597565b82525050565b610875816105e9565b82525050565b5f60808201905061088e5f83018761085d565b61089b602083018661086c565b6108a8604083018561086c565b6108b5606083018461056f565b95945050505050565b5f81905092915050565b828183375f83830152505050565b5f6108e183856108be565b93506108ee8385846108c8565b82840190509392505050565b5f6109068284866108d6565b91508190509392505050565b5f5ffd5b5f5ffd5b5f5f8585111561092d5761092c610912565b5b8386111561093e5761093d610916565b5b6001850283019150848603905094509492505050565b5f82905092915050565b5f82821b905092915050565b5f6109758383610954565b826109808135610597565b925060208210156109c0576109bb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8360200360080261095e565b831692505b505092915050565b5f82825260208201905092915050565b7f706172656e7420646f6d61696e206e6f742076616c69646174656420617070725f8201527f6f7072696174656c790000000000000000000000000000000000000000000000602082015250565b5f610a326029836109c8565b9150610a3d826109d8565b604082019050919050565b5f6020820190508181035f830152610a5f81610a26565b9050919050565b5f602082019050610a795f83018461086c565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b5f819050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610aec82610aac565b9150610af783610aac565b9250828201905080821115610b0f57610b0e610ab5565b5b92915050565b5f610b218284866108d6565b91508190509392505050565b7f737562646f6d61696e206e6f742076616c69646174656420617070726f7072695f8201527f6174656c79000000000000000000000000000000000000000000000000000000602082015250565b5f610b876025836109c8565b9150610b9282610b2d565b604082019050919050565b5f6020820190508181035f830152610bb481610b7b565b905091905056fea264697066735822122091498a4fca0bd22837d270a021cf395acdf414968915cd266dcd8fad47ed15d864736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'EXTENDED_RESOLVER_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 7, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b506004361061004a575f3560e01c806301ffc9a71461004e5780633e9ce7941461007e5780639061b9231461009a578063f86bc879146100ca575b5f5ffd5b61006860048036038101906100639190610539565b6100fa565b604051610075919061057e565b60405180910390f35b6100986004803603810190610093919061064e565b61015a565b005b6100b460048036038101906100af91906106ff565b61023a565b6040516100c191906107ed565b60405180910390f35b6100e460048036038101906100df919061080d565b610457565b6040516100f1919061057e565b60405180910390f35b5f639061b92360e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061015357506101528261048c565b5b9050919050565b8060015f8581526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055507fe1c5610a6e0cbe10764ecd182adcef1ec338dc4e199c99c32ce98f38e12791df8333848460405161022d949392919061087b565b60405180910390a1505050565b60606040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012085856040516102899291906108fa565b60405180910390201480156102a2575060248383905010155b15610352577ff0a378cc2afe91730d0105e67d6bb037cc5b8b6bfec5b5962d9b637ff6497e555f1b83836004906024926102de9392919061091a565b906102e9919061096a565b14610329576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032090610a48565b60405180910390fd5b61beef60405160200161033c9190610a66565b604051602081830303815290604052905061044f565b5f85855f81811061036657610365610a7f565b5b9050013560f81c60f81b60f81c60ff1690506040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012086868360016103c49190610ae2565b9080926103d39392919061091a565b6040516103e1929190610b15565b604051809103902014610429576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161042090610b9d565b60405180910390fd5b61dead60405160200161043c9190610a66565b6040516020818303038152906040529150505b949350505050565b6001602052825f5260405f20602052815f5260405f20602052805f5260405f205f92509250509054906101000a900460ff1681565b5f6301ffc9a760e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f5ffd5b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b610518816104e4565b8114610522575f5ffd5b50565b5f813590506105338161050f565b92915050565b5f6020828403121561054e5761054d6104dc565b5b5f61055b84828501610525565b91505092915050565b5f8115159050919050565b61057881610564565b82525050565b5f6020820190506105915f83018461056f565b92915050565b5f819050919050565b6105a981610597565b81146105b3575f5ffd5b50565b5f813590506105c4816105a0565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105f3826105ca565b9050919050565b610603816105e9565b811461060d575f5ffd5b50565b5f8135905061061e816105fa565b92915050565b61062d81610564565b8114610637575f5ffd5b50565b5f8135905061064881610624565b92915050565b5f5f5f60608486031215610665576106646104dc565b5b5f610672868287016105b6565b935050602061068386828701610610565b92505060406106948682870161063a565b9150509250925092565b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f8401126106bf576106be61069e565b5b8235905067ffffffffffffffff8111156106dc576106db6106a2565b5b6020830191508360018202830111156106f8576106f76106a6565b5b9250929050565b5f5f5f5f60408587031215610717576107166104dc565b5b5f85013567ffffffffffffffff811115610734576107336104e0565b5b610740878288016106aa565b9450945050602085013567ffffffffffffffff811115610763576107626104e0565b5b61076f878288016106aa565b925092505092959194509250565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6107bf8261077d565b6107c98185610787565b93506107d9818560208601610797565b6107e2816107a5565b840191505092915050565b5f6020820190508181035f83015261080581846107b5565b905092915050565b5f5f5f60608486031215610824576108236104dc565b5b5f610831868287016105b6565b935050602061084286828701610610565b925050604061085386828701610610565b9150509250925092565b61086681610597565b82525050565b610875816105e9565b82525050565b5f60808201905061088e5f83018761085d565b61089b602083018661086c565b6108a8604083018561086c565b6108b5606083018461056f565b95945050505050565b5f81905092915050565b828183375f83830152505050565b5f6108e183856108be565b93506108ee8385846108c8565b82840190509392505050565b5f6109068284866108d6565b91508190509392505050565b5f5ffd5b5f5ffd5b5f5f8585111561092d5761092c610912565b5b8386111561093e5761093d610916565b5b6001850283019150848603905094509492505050565b5f82905092915050565b5f82821b905092915050565b5f6109758383610954565b826109808135610597565b925060208210156109c0576109bb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8360200360080261095e565b831692505b505092915050565b5f82825260208201905092915050565b7f706172656e7420646f6d61696e206e6f742076616c69646174656420617070725f8201527f6f7072696174656c790000000000000000000000000000000000000000000000602082015250565b5f610a326029836109c8565b9150610a3d826109d8565b604082019050919050565b5f6020820190508181035f830152610a5f81610a26565b9050919050565b5f602082019050610a795f83018461086c565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b5f819050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610aec82610aac565b9150610af783610aac565b9250828201905080821115610b0f57610b0e610ab5565b5b92915050565b5f610b218284866108d6565b91508190509392505050565b7f737562646f6d61696e206e6f742076616c69646174656420617070726f7072695f8201527f6174656c79000000000000000000000000000000000000000000000000000000602082015250565b5f610b876025836109c8565b9150610b9282610b2d565b604082019050919050565b5f6020820190508181035f830152610bb481610b7b565b905091905056fea264697066735822122091498a4fca0bd22837d270a021cf395acdf414968915cd266dcd8fad47ed15d864736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'EXTENDED_RESOLVER_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 8, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'contract ENS' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* '_ens' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[14]; /* 'address' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 11, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 11, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r24 = (CPyPtr)&((PyListObject *)cpy_r_r23)->ob_item;
    cpy_r_r25 = *(CPyPtr *)cpy_r_r24;
    *(PyObject * *)cpy_r_r25 = cpy_r_r22;
    cpy_r_r26 = CPyStatics[15]; /* 'stateMutability' */
    cpy_r_r27 = CPyStatics[16]; /* 'nonpayable' */
    cpy_r_r28 = CPyStatics[13]; /* 'type' */
    cpy_r_r29 = CPyStatics[17]; /* 'constructor' */
    cpy_r_r30 = CPyDict_Build(3, cpy_r_r15, cpy_r_r23, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r29);
    CPy_DECREF_NO_IMM(cpy_r_r23);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 10, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r31 = CPyStatics[18]; /* 'anonymous' */
    cpy_r_r32 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r33 = CPyStatics[19]; /* 'indexed' */
    cpy_r_r34 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r35 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r36 = CPyStatics[11]; /* 'name' */
    cpy_r_r37 = CPyStatics[21]; /* 'node' */
    cpy_r_r38 = CPyStatics[13]; /* 'type' */
    cpy_r_r39 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r40 = 0 ? Py_True : Py_False;
    cpy_r_r41 = CPyDict_Build(4, cpy_r_r33, cpy_r_r40, cpy_r_r34, cpy_r_r35, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39);
    if (unlikely(cpy_r_r41 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 18, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r42 = CPyStatics[19]; /* 'indexed' */
    cpy_r_r43 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r44 = CPyStatics[14]; /* 'address' */
    cpy_r_r45 = CPyStatics[11]; /* 'name' */
    cpy_r_r46 = CPyStatics[22]; /* 'owner' */
    cpy_r_r47 = CPyStatics[13]; /* 'type' */
    cpy_r_r48 = CPyStatics[14]; /* 'address' */
    cpy_r_r49 = 0 ? Py_True : Py_False;
    cpy_r_r50 = CPyDict_Build(4, cpy_r_r42, cpy_r_r49, cpy_r_r43, cpy_r_r44, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 24, CPyStatic_globals);
        goto CPyL52;
    }
    cpy_r_r51 = CPyStatics[19]; /* 'indexed' */
    cpy_r_r52 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r53 = CPyStatics[14]; /* 'address' */
    cpy_r_r54 = CPyStatics[11]; /* 'name' */
    cpy_r_r55 = CPyStatics[23]; /* 'target' */
    cpy_r_r56 = CPyStatics[13]; /* 'type' */
    cpy_r_r57 = CPyStatics[14]; /* 'address' */
    cpy_r_r58 = 0 ? Py_True : Py_False;
    cpy_r_r59 = CPyDict_Build(4, cpy_r_r51, cpy_r_r58, cpy_r_r52, cpy_r_r53, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r57);
    if (unlikely(cpy_r_r59 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 30, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r60 = CPyStatics[19]; /* 'indexed' */
    cpy_r_r61 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r62 = CPyStatics[24]; /* 'bool' */
    cpy_r_r63 = CPyStatics[11]; /* 'name' */
    cpy_r_r64 = CPyStatics[25]; /* 'isAuthorised' */
    cpy_r_r65 = CPyStatics[13]; /* 'type' */
    cpy_r_r66 = CPyStatics[24]; /* 'bool' */
    cpy_r_r67 = 0 ? Py_True : Py_False;
    cpy_r_r68 = CPyDict_Build(4, cpy_r_r60, cpy_r_r67, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64, cpy_r_r65, cpy_r_r66);
    if (unlikely(cpy_r_r68 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 36, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r69 = PyList_New(4);
    if (unlikely(cpy_r_r69 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 17, CPyStatic_globals);
        goto CPyL55;
    }
    cpy_r_r70 = (CPyPtr)&((PyListObject *)cpy_r_r69)->ob_item;
    cpy_r_r71 = *(CPyPtr *)cpy_r_r70;
    *(PyObject * *)cpy_r_r71 = cpy_r_r41;
    cpy_r_r72 = cpy_r_r71 + 8;
    *(PyObject * *)cpy_r_r72 = cpy_r_r50;
    cpy_r_r73 = cpy_r_r71 + 16;
    *(PyObject * *)cpy_r_r73 = cpy_r_r59;
    cpy_r_r74 = cpy_r_r71 + 24;
    *(PyObject * *)cpy_r_r74 = cpy_r_r68;
    cpy_r_r75 = CPyStatics[11]; /* 'name' */
    cpy_r_r76 = CPyStatics[26]; /* 'AuthorisationChanged' */
    cpy_r_r77 = CPyStatics[13]; /* 'type' */
    cpy_r_r78 = CPyStatics[27]; /* 'event' */
    cpy_r_r79 = 0 ? Py_True : Py_False;
    cpy_r_r80 = CPyDict_Build(4, cpy_r_r31, cpy_r_r79, cpy_r_r32, cpy_r_r69, cpy_r_r75, cpy_r_r76, cpy_r_r77, cpy_r_r78);
    CPy_DECREF_NO_IMM(cpy_r_r69);
    if (unlikely(cpy_r_r80 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 15, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r81 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r82 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r83 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r84 = CPyStatics[11]; /* 'name' */
    cpy_r_r85 = CPyStatics[28]; /* '' */
    cpy_r_r86 = CPyStatics[13]; /* 'type' */
    cpy_r_r87 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r88 = CPyDict_Build(3, cpy_r_r82, cpy_r_r83, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87);
    if (unlikely(cpy_r_r88 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 48, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r89 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r90 = CPyStatics[14]; /* 'address' */
    cpy_r_r91 = CPyStatics[11]; /* 'name' */
    cpy_r_r92 = CPyStatics[28]; /* '' */
    cpy_r_r93 = CPyStatics[13]; /* 'type' */
    cpy_r_r94 = CPyStatics[14]; /* 'address' */
    cpy_r_r95 = CPyDict_Build(3, cpy_r_r89, cpy_r_r90, cpy_r_r91, cpy_r_r92, cpy_r_r93, cpy_r_r94);
    if (unlikely(cpy_r_r95 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 49, CPyStatic_globals);
        goto CPyL57;
    }
    cpy_r_r96 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r97 = CPyStatics[14]; /* 'address' */
    cpy_r_r98 = CPyStatics[11]; /* 'name' */
    cpy_r_r99 = CPyStatics[28]; /* '' */
    cpy_r_r100 = CPyStatics[13]; /* 'type' */
    cpy_r_r101 = CPyStatics[14]; /* 'address' */
    cpy_r_r102 = CPyDict_Build(3, cpy_r_r96, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 50, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r103 = PyList_New(3);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 47, CPyStatic_globals);
        goto CPyL59;
    }
    cpy_r_r104 = (CPyPtr)&((PyListObject *)cpy_r_r103)->ob_item;
    cpy_r_r105 = *(CPyPtr *)cpy_r_r104;
    *(PyObject * *)cpy_r_r105 = cpy_r_r88;
    cpy_r_r106 = cpy_r_r105 + 8;
    *(PyObject * *)cpy_r_r106 = cpy_r_r95;
    cpy_r_r107 = cpy_r_r105 + 16;
    *(PyObject * *)cpy_r_r107 = cpy_r_r102;
    cpy_r_r108 = CPyStatics[11]; /* 'name' */
    cpy_r_r109 = CPyStatics[29]; /* 'authorisations' */
    cpy_r_r110 = CPyStatics[30]; /* 'outputs' */
    cpy_r_r111 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r112 = CPyStatics[24]; /* 'bool' */
    cpy_r_r113 = CPyStatics[11]; /* 'name' */
    cpy_r_r114 = CPyStatics[28]; /* '' */
    cpy_r_r115 = CPyStatics[13]; /* 'type' */
    cpy_r_r116 = CPyStatics[24]; /* 'bool' */
    cpy_r_r117 = CPyDict_Build(3, cpy_r_r111, cpy_r_r112, cpy_r_r113, cpy_r_r114, cpy_r_r115, cpy_r_r116);
    if (unlikely(cpy_r_r117 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 53, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r118 = PyList_New(1);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 53, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r119 = (CPyPtr)&((PyListObject *)cpy_r_r118)->ob_item;
    cpy_r_r120 = *(CPyPtr *)cpy_r_r119;
    *(PyObject * *)cpy_r_r120 = cpy_r_r117;
    cpy_r_r121 = CPyStatics[15]; /* 'stateMutability' */
    cpy_r_r122 = CPyStatics[31]; /* 'view' */
    cpy_r_r123 = CPyStatics[13]; /* 'type' */
    cpy_r_r124 = CPyStatics[32]; /* 'function' */
    cpy_r_r125 = CPyDict_Build(5, cpy_r_r81, cpy_r_r103, cpy_r_r108, cpy_r_r109, cpy_r_r110, cpy_r_r118, cpy_r_r121, cpy_r_r122, cpy_r_r123, cpy_r_r124);
    CPy_DECREF_NO_IMM(cpy_r_r103);
    CPy_DECREF_NO_IMM(cpy_r_r118);
    if (unlikely(cpy_r_r125 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 46, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r126 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r127 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r128 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r129 = CPyStatics[11]; /* 'name' */
    cpy_r_r130 = CPyStatics[34]; /* 'dnsName' */
    cpy_r_r131 = CPyStatics[13]; /* 'type' */
    cpy_r_r132 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r133 = CPyDict_Build(3, cpy_r_r127, cpy_r_r128, cpy_r_r129, cpy_r_r130, cpy_r_r131, cpy_r_r132);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 59, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r134 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r135 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r136 = CPyStatics[11]; /* 'name' */
    cpy_r_r137 = CPyStatics[35]; /* 'data' */
    cpy_r_r138 = CPyStatics[13]; /* 'type' */
    cpy_r_r139 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r140 = CPyDict_Build(3, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137, cpy_r_r138, cpy_r_r139);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 60, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r141 = PyList_New(2);
    if (unlikely(cpy_r_r141 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 58, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r142 = (CPyPtr)&((PyListObject *)cpy_r_r141)->ob_item;
    cpy_r_r143 = *(CPyPtr *)cpy_r_r142;
    *(PyObject * *)cpy_r_r143 = cpy_r_r133;
    cpy_r_r144 = cpy_r_r143 + 8;
    *(PyObject * *)cpy_r_r144 = cpy_r_r140;
    cpy_r_r145 = CPyStatics[11]; /* 'name' */
    cpy_r_r146 = CPyStatics[36]; /* 'resolve' */
    cpy_r_r147 = CPyStatics[30]; /* 'outputs' */
    cpy_r_r148 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r149 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r150 = CPyStatics[11]; /* 'name' */
    cpy_r_r151 = CPyStatics[28]; /* '' */
    cpy_r_r152 = CPyStatics[13]; /* 'type' */
    cpy_r_r153 = CPyStatics[33]; /* 'bytes' */
    cpy_r_r154 = CPyDict_Build(3, cpy_r_r148, cpy_r_r149, cpy_r_r150, cpy_r_r151, cpy_r_r152, cpy_r_r153);
    if (unlikely(cpy_r_r154 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 63, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r155 = PyList_New(1);
    if (unlikely(cpy_r_r155 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 63, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r156 = (CPyPtr)&((PyListObject *)cpy_r_r155)->ob_item;
    cpy_r_r157 = *(CPyPtr *)cpy_r_r156;
    *(PyObject * *)cpy_r_r157 = cpy_r_r154;
    cpy_r_r158 = CPyStatics[15]; /* 'stateMutability' */
    cpy_r_r159 = CPyStatics[31]; /* 'view' */
    cpy_r_r160 = CPyStatics[13]; /* 'type' */
    cpy_r_r161 = CPyStatics[32]; /* 'function' */
    cpy_r_r162 = CPyDict_Build(5, cpy_r_r126, cpy_r_r141, cpy_r_r145, cpy_r_r146, cpy_r_r147, cpy_r_r155, cpy_r_r158, cpy_r_r159, cpy_r_r160, cpy_r_r161);
    CPy_DECREF_NO_IMM(cpy_r_r141);
    CPy_DECREF_NO_IMM(cpy_r_r155);
    if (unlikely(cpy_r_r162 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 57, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r163 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r164 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r165 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r166 = CPyStatics[11]; /* 'name' */
    cpy_r_r167 = CPyStatics[21]; /* 'node' */
    cpy_r_r168 = CPyStatics[13]; /* 'type' */
    cpy_r_r169 = CPyStatics[20]; /* 'bytes32' */
    cpy_r_r170 = CPyDict_Build(3, cpy_r_r164, cpy_r_r165, cpy_r_r166, cpy_r_r167, cpy_r_r168, cpy_r_r169);
    if (unlikely(cpy_r_r170 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 69, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r171 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r172 = CPyStatics[14]; /* 'address' */
    cpy_r_r173 = CPyStatics[11]; /* 'name' */
    cpy_r_r174 = CPyStatics[23]; /* 'target' */
    cpy_r_r175 = CPyStatics[13]; /* 'type' */
    cpy_r_r176 = CPyStatics[14]; /* 'address' */
    cpy_r_r177 = CPyDict_Build(3, cpy_r_r171, cpy_r_r172, cpy_r_r173, cpy_r_r174, cpy_r_r175, cpy_r_r176);
    if (unlikely(cpy_r_r177 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 70, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r178 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r179 = CPyStatics[24]; /* 'bool' */
    cpy_r_r180 = CPyStatics[11]; /* 'name' */
    cpy_r_r181 = CPyStatics[25]; /* 'isAuthorised' */
    cpy_r_r182 = CPyStatics[13]; /* 'type' */
    cpy_r_r183 = CPyStatics[24]; /* 'bool' */
    cpy_r_r184 = CPyDict_Build(3, cpy_r_r178, cpy_r_r179, cpy_r_r180, cpy_r_r181, cpy_r_r182, cpy_r_r183);
    if (unlikely(cpy_r_r184 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 71, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r185 = PyList_New(3);
    if (unlikely(cpy_r_r185 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 68, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r186 = (CPyPtr)&((PyListObject *)cpy_r_r185)->ob_item;
    cpy_r_r187 = *(CPyPtr *)cpy_r_r186;
    *(PyObject * *)cpy_r_r187 = cpy_r_r170;
    cpy_r_r188 = cpy_r_r187 + 8;
    *(PyObject * *)cpy_r_r188 = cpy_r_r177;
    cpy_r_r189 = cpy_r_r187 + 16;
    *(PyObject * *)cpy_r_r189 = cpy_r_r184;
    cpy_r_r190 = CPyStatics[11]; /* 'name' */
    cpy_r_r191 = CPyStatics[37]; /* 'setAuthorisation' */
    cpy_r_r192 = CPyStatics[30]; /* 'outputs' */
    cpy_r_r193 = PyList_New(0);
    if (unlikely(cpy_r_r193 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 74, CPyStatic_globals);
        goto CPyL71;
    }
    cpy_r_r194 = CPyStatics[15]; /* 'stateMutability' */
    cpy_r_r195 = CPyStatics[16]; /* 'nonpayable' */
    cpy_r_r196 = CPyStatics[13]; /* 'type' */
    cpy_r_r197 = CPyStatics[32]; /* 'function' */
    cpy_r_r198 = CPyDict_Build(5, cpy_r_r163, cpy_r_r185, cpy_r_r190, cpy_r_r191, cpy_r_r192, cpy_r_r193, cpy_r_r194, cpy_r_r195, cpy_r_r196, cpy_r_r197);
    CPy_DECREF_NO_IMM(cpy_r_r185);
    CPy_DECREF_NO_IMM(cpy_r_r193);
    if (unlikely(cpy_r_r198 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 67, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r199 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r200 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r201 = CPyStatics[38]; /* 'bytes4' */
    cpy_r_r202 = CPyStatics[11]; /* 'name' */
    cpy_r_r203 = CPyStatics[39]; /* 'interfaceID' */
    cpy_r_r204 = CPyStatics[13]; /* 'type' */
    cpy_r_r205 = CPyStatics[38]; /* 'bytes4' */
    cpy_r_r206 = CPyDict_Build(3, cpy_r_r200, cpy_r_r201, cpy_r_r202, cpy_r_r203, cpy_r_r204, cpy_r_r205);
    if (unlikely(cpy_r_r206 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 79, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r207 = PyList_New(1);
    if (unlikely(cpy_r_r207 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 79, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r208 = (CPyPtr)&((PyListObject *)cpy_r_r207)->ob_item;
    cpy_r_r209 = *(CPyPtr *)cpy_r_r208;
    *(PyObject * *)cpy_r_r209 = cpy_r_r206;
    cpy_r_r210 = CPyStatics[11]; /* 'name' */
    cpy_r_r211 = CPyStatics[40]; /* 'supportsInterface' */
    cpy_r_r212 = CPyStatics[30]; /* 'outputs' */
    cpy_r_r213 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r214 = CPyStatics[24]; /* 'bool' */
    cpy_r_r215 = CPyStatics[11]; /* 'name' */
    cpy_r_r216 = CPyStatics[28]; /* '' */
    cpy_r_r217 = CPyStatics[13]; /* 'type' */
    cpy_r_r218 = CPyStatics[24]; /* 'bool' */
    cpy_r_r219 = CPyDict_Build(3, cpy_r_r213, cpy_r_r214, cpy_r_r215, cpy_r_r216, cpy_r_r217, cpy_r_r218);
    if (unlikely(cpy_r_r219 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 81, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r220 = PyList_New(1);
    if (unlikely(cpy_r_r220 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 81, CPyStatic_globals);
        goto CPyL75;
    }
    cpy_r_r221 = (CPyPtr)&((PyListObject *)cpy_r_r220)->ob_item;
    cpy_r_r222 = *(CPyPtr *)cpy_r_r221;
    *(PyObject * *)cpy_r_r222 = cpy_r_r219;
    cpy_r_r223 = CPyStatics[15]; /* 'stateMutability' */
    cpy_r_r224 = CPyStatics[41]; /* 'pure' */
    cpy_r_r225 = CPyStatics[13]; /* 'type' */
    cpy_r_r226 = CPyStatics[32]; /* 'function' */
    cpy_r_r227 = CPyDict_Build(5, cpy_r_r199, cpy_r_r207, cpy_r_r210, cpy_r_r211, cpy_r_r212, cpy_r_r220, cpy_r_r223, cpy_r_r224, cpy_r_r225, cpy_r_r226);
    CPy_DECREF_NO_IMM(cpy_r_r207);
    CPy_DECREF_NO_IMM(cpy_r_r220);
    if (unlikely(cpy_r_r227 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 78, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r228 = PyList_New(6);
    if (unlikely(cpy_r_r228 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 9, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r229 = (CPyPtr)&((PyListObject *)cpy_r_r228)->ob_item;
    cpy_r_r230 = *(CPyPtr *)cpy_r_r229;
    *(PyObject * *)cpy_r_r230 = cpy_r_r30;
    cpy_r_r231 = cpy_r_r230 + 8;
    *(PyObject * *)cpy_r_r231 = cpy_r_r80;
    cpy_r_r232 = cpy_r_r230 + 16;
    *(PyObject * *)cpy_r_r232 = cpy_r_r125;
    cpy_r_r233 = cpy_r_r230 + 24;
    *(PyObject * *)cpy_r_r233 = cpy_r_r162;
    cpy_r_r234 = cpy_r_r230 + 32;
    *(PyObject * *)cpy_r_r234 = cpy_r_r198;
    cpy_r_r235 = cpy_r_r230 + 40;
    *(PyObject * *)cpy_r_r235 = cpy_r_r227;
    cpy_r_r236 = CPyStatic_globals;
    cpy_r_r237 = CPyStatics[42]; /* 'EXTENDED_RESOLVER_ABI' */
    cpy_r_r238 = CPyDict_SetItem(cpy_r_r236, cpy_r_r237, cpy_r_r228);
    CPy_DECREF_NO_IMM(cpy_r_r228);
    cpy_r_r239 = cpy_r_r238 >= 0;
    if (unlikely(!cpy_r_r239)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 9, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r240 = CPyStatics[43]; /* 'bytecode' */
    cpy_r_r241 = CPyStatic_globals;
    cpy_r_r242 = CPyStatics[5]; /* 'EXTENDED_RESOLVER_BYTECODE' */
    cpy_r_r243 = CPyDict_GetItem(cpy_r_r241, cpy_r_r242);
    if (unlikely(cpy_r_r243 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 87, CPyStatic_globals);
        goto CPyL49;
    }
    if (likely(PyUnicode_Check(cpy_r_r243)))
        cpy_r_r244 = cpy_r_r243;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 87, CPyStatic_globals, "str", cpy_r_r243);
        goto CPyL49;
    }
    cpy_r_r245 = CPyStatics[44]; /* 'bytecode_runtime' */
    cpy_r_r246 = CPyStatic_globals;
    cpy_r_r247 = CPyStatics[7]; /* 'EXTENDED_RESOLVER_RUNTIME' */
    cpy_r_r248 = CPyDict_GetItem(cpy_r_r246, cpy_r_r247);
    if (unlikely(cpy_r_r248 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 88, CPyStatic_globals);
        goto CPyL77;
    }
    if (likely(PyUnicode_Check(cpy_r_r248)))
        cpy_r_r249 = cpy_r_r248;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 88, CPyStatic_globals, "str", cpy_r_r248);
        goto CPyL77;
    }
    cpy_r_r250 = CPyStatics[45]; /* 'abi' */
    cpy_r_r251 = CPyStatic_globals;
    cpy_r_r252 = CPyStatics[42]; /* 'EXTENDED_RESOLVER_ABI' */
    cpy_r_r253 = CPyDict_GetItem(cpy_r_r251, cpy_r_r252);
    if (unlikely(cpy_r_r253 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 89, CPyStatic_globals);
        goto CPyL78;
    }
    if (likely(PyList_Check(cpy_r_r253)))
        cpy_r_r254 = cpy_r_r253;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 89, CPyStatic_globals, "list", cpy_r_r253);
        goto CPyL78;
    }
    cpy_r_r255 = CPyDict_Build(3, cpy_r_r240, cpy_r_r244, cpy_r_r245, cpy_r_r249, cpy_r_r250, cpy_r_r254);
    CPy_DECREF(cpy_r_r244);
    CPy_DECREF(cpy_r_r249);
    CPy_DECREF_NO_IMM(cpy_r_r254);
    if (unlikely(cpy_r_r255 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 86, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r256 = CPyStatic_globals;
    cpy_r_r257 = CPyStatics[46]; /* 'EXTENDED_RESOLVER_DATA' */
    cpy_r_r258 = CPyDict_SetItem(cpy_r_r256, cpy_r_r257, cpy_r_r255);
    CPy_DECREF(cpy_r_r255);
    cpy_r_r259 = cpy_r_r258 >= 0;
    if (unlikely(!cpy_r_r259)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/extended_resolver.py", "<module>", 86, CPyStatic_globals);
        goto CPyL49;
    }
    return 1;
CPyL49: ;
    cpy_r_r260 = 2;
    return cpy_r_r260;
CPyL50: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL49;
CPyL51: ;
    CPy_DecRef(cpy_r_r30);
    goto CPyL49;
CPyL52: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r41);
    goto CPyL49;
CPyL53: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r41);
    CPy_DecRef(cpy_r_r50);
    goto CPyL49;
CPyL54: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r41);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r59);
    goto CPyL49;
CPyL55: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r41);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r59);
    CPy_DecRef(cpy_r_r68);
    goto CPyL49;
CPyL56: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    goto CPyL49;
CPyL57: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r88);
    goto CPyL49;
CPyL58: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r95);
    goto CPyL49;
CPyL59: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r95);
    CPy_DecRef(cpy_r_r102);
    goto CPyL49;
CPyL60: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r103);
    goto CPyL49;
CPyL61: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r117);
    goto CPyL49;
CPyL62: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    goto CPyL49;
CPyL63: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r133);
    goto CPyL49;
CPyL64: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r140);
    goto CPyL49;
CPyL65: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r141);
    goto CPyL49;
CPyL66: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r141);
    CPy_DecRef(cpy_r_r154);
    goto CPyL49;
CPyL67: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    goto CPyL49;
CPyL68: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r170);
    goto CPyL49;
CPyL69: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r170);
    CPy_DecRef(cpy_r_r177);
    goto CPyL49;
CPyL70: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r170);
    CPy_DecRef(cpy_r_r177);
    CPy_DecRef(cpy_r_r184);
    goto CPyL49;
CPyL71: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r185);
    goto CPyL49;
CPyL72: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r198);
    goto CPyL49;
CPyL73: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r198);
    CPy_DecRef(cpy_r_r206);
    goto CPyL49;
CPyL74: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r198);
    CPy_DecRef(cpy_r_r207);
    goto CPyL49;
CPyL75: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r198);
    CPy_DecRef(cpy_r_r207);
    CPy_DecRef(cpy_r_r219);
    goto CPyL49;
CPyL76: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r80);
    CPy_DecRef(cpy_r_r125);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r198);
    CPy_DecRef(cpy_r_r227);
    goto CPyL49;
CPyL77: ;
    CPy_DecRef(cpy_r_r244);
    goto CPyL49;
CPyL78: ;
    CPy_DecRef(cpy_r_r244);
    CPy_DecRef(cpy_r_r249);
    goto CPyL49;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[47];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\264\0360x608060405234801561000f575f5ffd5b50604051610d0e380380610d0e833981810160405281019061003191906100e5565b805f5f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610110565b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b5f6100b482610099565b9050919050565b6100c4816100aa565b81146100ce575f5ffd5b50565b5f815190506100df816100bb565b92915050565b5f602082840312156100fa576100f9610076565b5b5f610107848285016100d1565b91505092915050565b610bf18061011d5f395ff3fe608060405234801561000f575f5ffd5b506004361061004a575f3560e01c806301ffc9a71461004e5780633e9ce7941461007e5780639061b9231461009a578063f86bc879146100ca575b5f5ffd5b61006860048036038101906100639190610539565b6100fa565b604051610075919061057e565b60405180910390f35b6100986004803603810190610093919061064e565b61015a565b005b6100b460048036038101906100af91906106ff565b61023a565b6040516100c191906107ed565b60405180910390f35b6100e460048036038101906100df919061080d565b610457565b6040516100f1919061057e565b60405180910390f35b5f639061b92360e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061015357506101528261048c565b5b9050919050565b8060015f8581526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055507fe1c5610a6e0cbe10764ecd182adcef1ec338dc4e199c99c32ce98f38e12791df8333848460405161022d949392919061087b565b60405180910390a1505050565b60606040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012085856040516102899291906108fa565b60405180910390201480156102a2575060248383905010155b15610352577ff0a378cc2afe91730d0105e67d6bb037cc5b8b6bfec5b5962d9b637ff6497e555f1b83836004906024926102de9392919061091a565b906102e9919061096a565b14610329576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032090610a48565b60405180910390fd5b61beef60405160200161033c9190610a66565b604051602081830303815290604052905061044f565b5f85855f81811061036657610365610a7f565b5b9050013560f81c60f81b60f81c60ff1690506040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012086868360016103c49190610ae2565b9080926103d39392919061091a565b6040516103e1929190610b15565b604051809103902014610429576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161042090610b9d565b60405180910390fd5b61dead60405160200161043c9190610a66565b6040516020818303038152906040529150505b949350505050565b6001602052825f5260405f20602052815f5260405f20602052805f5260405f205f92509250509054906101000a900460ff1681565b5f6301ffc9a760e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f5ffd5b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b610518816104e4565b8114610522575f5ffd5b50565b5f813590506105338161050f565b92915050565b5f6020828403121561054e5761054d6104dc565b5b5f61055b84828501610525565b91505092915050565b5f8115159050919050565b61057881610564565b82525050565b5f6020820190506105915f83018461056f565b92915050565b5f819050919050565b6105a981610597565b81146105b3575f5ffd5b50565b5f813590506105c4816105a0565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105f3826105ca565b9050919050565b610603816105e9565b811461060d575f5ffd5b50565b5f8135905061061e816105fa565b92915050565b61062d81610564565b8114610637575f5ffd5b50565b5f8135905061064881610624565b92915050565b5f5f5f60608486031215610665576106646104dc565b5b5f610672868287016105b6565b935050602061068386828701610610565b92505060406106948682870161063a565b9150509250925092565b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f8401126106bf576106be61069e565b5b8235905067ffffffffffffffff8111156106dc576106db6106a2565b5b6020830191508360018202830111156106f8576106f76106a6565b5b9250929050565b5f5f5f5f60408587031215610717576107166104dc565b5b5f85013567ffffffffffffffff811115610734576107336104e0565b5b610740878288016106aa565b9450945050602085013567ffffffffffffffff811115610763576107626104e0565b5b61076f878288016106aa565b925092505092959194509250565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6107bf8261077d565b6107c98185610787565b93506107d9818560208601610797565b6107e2816107a5565b840191505092915050565b5f6020820190508181035f83015261080581846107b5565b905092915050565b5f5f5f60608486031215610824576108236104dc565b5b5f610831868287016105b6565b935050602061084286828701610610565b925050604061085386828701610610565b9150509250925092565b61086681610597565b82525050565b610875816105e9565b82525050565b5f60808201905061088e5f83018761085d565b61089b602083018661086c565b6108a8604083018561086c565b6108b5606083018461056f565b95945050505050565b5f81905092915050565b828183375f83830152505050565b5f6108e183856108be565b93506108ee8385846108c8565b82840190509392505050565b5f6109068284866108d6565b91508190509392505050565b5f5ffd5b5f5ffd5b5f5f8585111561092d5761092c610912565b5b8386111561093e5761093d610916565b5b6001850283019150848603905094509492505050565b5f82905092915050565b5f82821b905092915050565b5f6109758383610954565b826109808135610597565b925060208210156109c0576109bb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8360200360080261095e565b831692505b505092915050565b5f82825260208201905092915050565b7f706172656e7420646f6d61696e206e6f742076616c69646174656420617070725f8201527f6f7072696174656c790000000000000000000000000000000000000000000000602082015250565b5f610a326029836109c8565b9150610a3d826109d8565b604082019050919050565b5f6020820190508181035f830152610a5f81610a26565b9050919050565b5f602082019050610a795f83018461086c565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b5f819050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610aec82610aac565b9150610af783610aac565b9250828201905080821115610b0f57610b0e610ab5565b5b92915050565b5f610b218284866108d6565b91508190509392505050565b7f737562646f6d61696e206e6f742076616c69646174656420617070726f7072695f8201527f6174656c79000000000000000000000000000000000000000000000000000000602082015250565b5f610b876025836109c8565b9150610b9282610b2d565b604082019050919050565b5f6020820190508181035f830152610bb481610b7b565b905091905056fea264697066735822122091498a4fca0bd22837d270a021cf395acdf414968915cd266dcd8fad47ed15d864736f6c634300081e0033",
    "\001\032EXTENDED_RESOLVER_BYTECODE",
    "\001\257d0x608060405234801561000f575f5ffd5b506004361061004a575f3560e01c806301ffc9a71461004e5780633e9ce7941461007e5780639061b9231461009a578063f86bc879146100ca575b5f5ffd5b61006860048036038101906100639190610539565b6100fa565b604051610075919061057e565b60405180910390f35b6100986004803603810190610093919061064e565b61015a565b005b6100b460048036038101906100af91906106ff565b61023a565b6040516100c191906107ed565b60405180910390f35b6100e460048036038101906100df919061080d565b610457565b6040516100f1919061057e565b60405180910390f35b5f639061b92360e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916148061015357506101528261048c565b5b9050919050565b8060015f8581526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055507fe1c5610a6e0cbe10764ecd182adcef1ec338dc4e199c99c32ce98f38e12791df8333848460405161022d949392919061087b565b60405180910390a1505050565b60606040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012085856040516102899291906108fa565b60405180910390201480156102a2575060248383905010155b15610352577ff0a378cc2afe91730d0105e67d6bb037cc5b8b6bfec5b5962d9b637ff6497e555f1b83836004906024926102de9392919061091a565b906102e9919061096a565b14610329576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032090610a48565b60405180910390fd5b61beef60405160200161033c9190610a66565b604051602081830303815290604052905061044f565b5f85855f81811061036657610365610a7f565b5b9050013560f81c60f81b60f81c60ff1690506040518060400160405280601781526020017f11657874656e6465642d7265736f6c76657203657468000000000000000000008152508051906020012086868360016103c49190610ae2565b9080926103d39392919061091a565b6040516103e1929190610b15565b604051809103902014610429576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161042090610b9d565b60405180910390fd5b61dead60405160200161043c9190610a66565b6040516020818303038152906040529150505b949350505050565b6001602052825f5260405f20602052815f5260405f20602052805f5260405f205f92509250509054906101000a900460ff1681565b5f6301ffc9a760e01b7bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916827bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916149050919050565b5f5ffd5b5f5ffd5b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b610518816104e4565b8114610522575f5ffd5b50565b5f813590506105338161050f565b92915050565b5f6020828403121561054e5761054d6104dc565b5b5f61055b84828501610525565b91505092915050565b5f8115159050919050565b61057881610564565b82525050565b5f6020820190506105915f83018461056f565b92915050565b5f819050919050565b6105a981610597565b81146105b3575f5ffd5b50565b5f813590506105c4816105a0565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105f3826105ca565b9050919050565b610603816105e9565b811461060d575f5ffd5b50565b5f8135905061061e816105fa565b92915050565b61062d81610564565b8114610637575f5ffd5b50565b5f8135905061064881610624565b92915050565b5f5f5f60608486031215610665576106646104dc565b5b5f610672868287016105b6565b935050602061068386828701610610565b92505060406106948682870161063a565b9150509250925092565b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f8401126106bf576106be61069e565b5b8235905067ffffffffffffffff8111156106dc576106db6106a2565b5b6020830191508360018202830111156106f8576106f76106a6565b5b9250929050565b5f5f5f5f60408587031215610717576107166104dc565b5b5f85013567ffffffffffffffff811115610734576107336104e0565b5b610740878288016106aa565b9450945050602085013567ffffffffffffffff811115610763576107626104e0565b5b61076f878288016106aa565b925092505092959194509250565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6107bf8261077d565b6107c98185610787565b93506107d9818560208601610797565b6107e2816107a5565b840191505092915050565b5f6020820190508181035f83015261080581846107b5565b905092915050565b5f5f5f60608486031215610824576108236104dc565b5b5f610831868287016105b6565b935050602061084286828701610610565b925050604061085386828701610610565b9150509250925092565b61086681610597565b82525050565b610875816105e9565b82525050565b5f60808201905061088e5f83018761085d565b61089b602083018661086c565b6108a8604083018561086c565b6108b5606083018461056f565b95945050505050565b5f81905092915050565b828183375f83830152505050565b5f6108e183856108be565b93506108ee8385846108c8565b82840190509392505050565b5f6109068284866108d6565b91508190509392505050565b5f5ffd5b5f5ffd5b5f5f8585111561092d5761092c610912565b5b8386111561093e5761093d610916565b5b6001850283019150848603905094509492505050565b5f82905092915050565b5f82821b905092915050565b5f6109758383610954565b826109808135610597565b925060208210156109c0576109bb7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8360200360080261095e565b831692505b505092915050565b5f82825260208201905092915050565b7f706172656e7420646f6d61696e206e6f742076616c69646174656420617070725f8201527f6f7072696174656c790000000000000000000000000000000000000000000000602082015250565b5f610a326029836109c8565b9150610a3d826109d8565b604082019050919050565b5f6020820190508181035f830152610a5f81610a26565b9050919050565b5f602082019050610a795f83018461086c565b92915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b5f819050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610aec82610aac565b9150610af783610aac565b9250828201905080821115610b0f57610b0e610ab5565b5b92915050565b5f610b218284866108d6565b91508190509392505050565b7f737562646f6d61696e206e6f742076616c69646174656420617070726f7072695f8201527f6174656c79000000000000000000000000000000000000000000000000000000602082015250565b5f610b876025836109c8565b9150610b9282610b2d565b604082019050919050565b5f6020820190508181035f830152610bb481610b7b565b905091905056fea264697066735822122091498a4fca0bd22837d270a021cf395acdf414968915cd266dcd8fad47ed15d864736f6c634300081e0033",
    "\006\031EXTENDED_RESOLVER_RUNTIME\006inputs\finternalType\fcontract ENS\004name\004_ens",
    "\a\004type\aaddress\017stateMutability\nnonpayable\vconstructor\tanonymous\aindexed",
    "\a\abytes32\004node\005owner\006target\004bool\fisAuthorised\024AuthorisationChanged",
    "\t\005event\000\016authorisations\aoutputs\004view\bfunction\005bytes\adnsName\004data",
    "\006\aresolve\020setAuthorisation\006bytes4\vinterfaceID\021supportsInterface\004pure",
    "\004\025EXTENDED_RESOLVER_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\026EXTENDED_RESOLVER_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___extended_resolver;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_extended_resolver__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___extended_resolver(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___extended_resolver, "faster_web3._utils.contract_sources.contract_data.extended_resolver__mypyc.init_faster_web3____utils___contract_sources___contract_data___extended_resolver", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___extended_resolver", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_extended_resolver__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.extended_resolver__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_extended_resolver__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_extended_resolver__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_extended_resolver__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
