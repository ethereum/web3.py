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
#include "__native_string_contract.h"
#include "__native_internal_string_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___string_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.string_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___string_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___string_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal;
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
    CPyPtr cpy_r_r49;
    CPyPtr cpy_r_r50;
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
    PyObject *cpy_r_r85;
    PyObject *cpy_r_r86;
    PyObject *cpy_r_r87;
    PyObject *cpy_r_r88;
    CPyPtr cpy_r_r89;
    CPyPtr cpy_r_r90;
    PyObject *cpy_r_r91;
    PyObject *cpy_r_r92;
    PyObject *cpy_r_r93;
    PyObject *cpy_r_r94;
    PyObject *cpy_r_r95;
    PyObject *cpy_r_r96;
    CPyPtr cpy_r_r97;
    CPyPtr cpy_r_r98;
    CPyPtr cpy_r_r99;
    CPyPtr cpy_r_r100;
    CPyPtr cpy_r_r101;
    CPyPtr cpy_r_r102;
    PyObject *cpy_r_r103;
    PyObject *cpy_r_r104;
    int32_t cpy_r_r105;
    char cpy_r_r106;
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
    int32_t cpy_r_r125;
    char cpy_r_r126;
    char cpy_r_r127;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL32;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x608060405234801561000f575f5ffd5b50604051610c1a380380610c1a83398181016040528101906100319190610193565b805f908161003f91906103ea565b50506104b9565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100a58261005f565b810181811067ffffffffffffffff821117156100c4576100c361006f565b5b80604052505050565b5f6100d6610046565b90506100e2828261009c565b919050565b5f67ffffffffffffffff8211156101015761010061006f565b5b61010a8261005f565b9050602081019050919050565b8281835e5f83830152505050565b5f610137610132846100e7565b6100cd565b9050828152602081018484840111156101535761015261005b565b5b61015e848285610117565b509392505050565b5f82601f83011261017a57610179610057565b5b815161018a848260208601610125565b91505092915050565b5f602082840312156101a8576101a761004f565b5b5f82015167ffffffffffffffff8111156101c5576101c4610053565b5b6101d184828501610166565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061022857607f821691505b60208210810361023b5761023a6101e4565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261029d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610262565b6102a78683610262565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6102eb6102e66102e1846102bf565b6102c8565b6102bf565b9050919050565b5f819050919050565b610304836102d1565b610318610310826102f2565b84845461026e565b825550505050565b5f5f905090565b61032f610320565b61033a8184846102fb565b505050565b5b8181101561035d576103525f82610327565b600181019050610340565b5050565b601f8211156103a25761037381610241565b61037c84610253565b8101602085101561038b578190505b61039f61039785610253565b83018261033f565b50505b505050565b5f82821c905092915050565b5f6103c25f19846008026103a7565b1980831691505092915050565b5f6103da83836103b3565b9150826002028217905092915050565b6103f3826101da565b67ffffffffffffffff81111561040c5761040b61006f565b5b6104168254610211565b610421828285610361565b5f60209050601f831160018114610452575f8415610440578287015190505b61044a85826103cf565b8655506104b1565b601f19841661046086610241565b5f5b8281101561048757848901518255600182019150602085019450602081019050610462565b868310156104a457848901516104a0601f8916826103b3565b8355505b6001600288020188555050505b505050505050565b610754806104c65f395ff3fe608060405260043610610037575f3560e01c806320965255146100995780633fa4f245146100b757806393a09352146100e157610038565b5b348015610043575f5ffd5b505f36606082828080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f820116905080830192505050505050509050915050805190602001f35b6100a1610109565b6040516100ae91906102a5565b60405180910390f35b3480156100c2575f5ffd5b506100cb610198565b6040516100d891906102a5565b60405180910390f35b3480156100ec575f5ffd5b5061010760048036038101906101029190610402565b610223565b005b60605f805461011790610476565b80601f016020809104026020016040519081016040528092919081815260200182805461014390610476565b801561018e5780601f106101655761010080835404028352916020019161018e565b820191905f5260205f20905b81548152906001019060200180831161017157829003601f168201915b5050505050905090565b5f80546101a490610476565b80601f01602080910402602001604051908101604052809291908181526020018280546101d090610476565b801561021b5780601f106101f25761010080835404028352916020019161021b565b820191905f5260205f20905b8154815290600101906020018083116101fe57829003601f168201915b505050505081565b805f9081610231919061064f565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61027782610235565b610281818561023f565b935061029181856020860161024f565b61029a8161025d565b840191505092915050565b5f6020820190508181035f8301526102bd818461026d565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6103148261025d565b810181811067ffffffffffffffff82111715610333576103326102de565b5b80604052505050565b5f6103456102c5565b9050610351828261030b565b919050565b5f67ffffffffffffffff8211156103705761036f6102de565b5b6103798261025d565b9050602081019050919050565b828183375f83830152505050565b5f6103a66103a184610356565b61033c565b9050828152602081018484840111156103c2576103c16102da565b5b6103cd848285610386565b509392505050565b5f82601f8301126103e9576103e86102d6565b5b81356103f9848260208601610394565b91505092915050565b5f60208284031215610417576104166102ce565b5b5f82013567ffffffffffffffff811115610434576104336102d2565b5b610440848285016103d5565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061048d57607f821691505b6020821081036104a05761049f610449565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026105027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826104c7565b61050c86836104c7565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61055061054b61054684610524565b61052d565b610524565b9050919050565b5f819050919050565b61056983610536565b61057d61057582610557565b8484546104d3565b825550505050565b5f5f905090565b610594610585565b61059f818484610560565b505050565b5b818110156105c2576105b75f8261058c565b6001810190506105a5565b5050565b601f821115610607576105d8816104a6565b6105e1846104b8565b810160208510156105f0578190505b6106046105fc856104b8565b8301826105a4565b50505b505050565b5f82821c905092915050565b5f6106275f198460080261060c565b1980831691505092915050565b5f61063f8383610618565b9150826002028217905092915050565b61065882610235565b67ffffffffffffffff811115610671576106706102de565b5b61067b8254610476565b6106868282856105c6565b5f60209050601f8311600181146106b7575f84156106a5578287015190505b6106af8582610634565b865550610716565b601f1984166106c5866104a6565b5f5b828110156106ec578489015182556001820191506020850194506020810190506106c7565b868310156107095784890151610705601f891682610618565b8355505b6001600288020188555050505b50505050505056fea264697066735822122062c13ebbeffccc0fada8dca300714023d382cee7cbd94c78a6bcf2350afd835d64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'STRING_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405260043610610037575f3560e01c806320965255146100995780633fa4f245146100b757806393a09352146100e157610038565b5b348015610043575f5ffd5b505f36606082828080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f820116905080830192505050505050509050915050805190602001f35b6100a1610109565b6040516100ae91906102a5565b60405180910390f35b3480156100c2575f5ffd5b506100cb610198565b6040516100d891906102a5565b60405180910390f35b3480156100ec575f5ffd5b5061010760048036038101906101029190610402565b610223565b005b60605f805461011790610476565b80601f016020809104026020016040519081016040528092919081815260200182805461014390610476565b801561018e5780601f106101655761010080835404028352916020019161018e565b820191905f5260205f20905b81548152906001019060200180831161017157829003601f168201915b5050505050905090565b5f80546101a490610476565b80601f01602080910402602001604051908101604052809291908181526020018280546101d090610476565b801561021b5780601f106101f25761010080835404028352916020019161021b565b820191905f5260205f20905b8154815290600101906020018083116101fe57829003601f168201915b505050505081565b805f9081610231919061064f565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61027782610235565b610281818561023f565b935061029181856020860161024f565b61029a8161025d565b840191505092915050565b5f6020820190508181035f8301526102bd818461026d565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6103148261025d565b810181811067ffffffffffffffff82111715610333576103326102de565b5b80604052505050565b5f6103456102c5565b9050610351828261030b565b919050565b5f67ffffffffffffffff8211156103705761036f6102de565b5b6103798261025d565b9050602081019050919050565b828183375f83830152505050565b5f6103a66103a184610356565b61033c565b9050828152602081018484840111156103c2576103c16102da565b5b6103cd848285610386565b509392505050565b5f82601f8301126103e9576103e86102d6565b5b81356103f9848260208601610394565b91505092915050565b5f60208284031215610417576104166102ce565b5b5f82013567ffffffffffffffff811115610434576104336102d2565b5b610440848285016103d5565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061048d57607f821691505b6020821081036104a05761049f610449565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026105027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826104c7565b61050c86836104c7565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61055061054b61054684610524565b61052d565b610524565b9050919050565b5f819050919050565b61056983610536565b61057d61057582610557565b8484546104d3565b825550505050565b5f5f905090565b610594610585565b61059f818484610560565b505050565b5b818110156105c2576105b75f8261058c565b6001810190506105a5565b5050565b601f821115610607576105d8816104a6565b6105e1846104b8565b810160208510156105f0578190505b6106046105fc856104b8565b8301826105a4565b50505b505050565b5f82821c905092915050565b5f6106275f198460080261060c565b1980831691505092915050565b5f61063f8383610618565b9150826002028217905092915050565b61065882610235565b67ffffffffffffffff811115610671576106706102de565b5b61067b8254610476565b6106868282856105c6565b5f60209050601f8311600181146106b7575f84156106a5578287015190505b6106af8582610634565b865550610716565b601f1984166106c5866104a6565b5f5b828110156106ec578489015182556001820191506020850194506020810190506106c7565b868310156107095784890151610705601f891682610618565b8355505b6001600288020188555050505b50505050505056fea264697066735822122062c13ebbeffccc0fada8dca300714023d382cee7cbd94c78a6bcf2350afd835d64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'STRING_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'string' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* '_value' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'string' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL33;
    }
    cpy_r_r24 = (CPyPtr)&((PyListObject *)cpy_r_r23)->ob_item;
    cpy_r_r25 = *(CPyPtr *)cpy_r_r24;
    *(PyObject * *)cpy_r_r25 = cpy_r_r22;
    cpy_r_r26 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r27 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r28 = CPyStatics[13]; /* 'type' */
    cpy_r_r29 = CPyStatics[16]; /* 'constructor' */
    cpy_r_r30 = CPyDict_Build(3, cpy_r_r15, cpy_r_r23, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r29);
    CPy_DECREF_NO_IMM(cpy_r_r23);
    if (unlikely(cpy_r_r30 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r31 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r32 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r33 = CPyStatics[13]; /* 'type' */
    cpy_r_r34 = CPyStatics[17]; /* 'fallback' */
    cpy_r_r35 = CPyDict_Build(2, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 15, CPyStatic_globals);
        goto CPyL34;
    }
    cpy_r_r36 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r37 = PyList_New(0);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 17, CPyStatic_globals);
        goto CPyL35;
    }
    cpy_r_r38 = CPyStatics[11]; /* 'name' */
    cpy_r_r39 = CPyStatics[18]; /* 'getValue' */
    cpy_r_r40 = CPyStatics[19]; /* 'outputs' */
    cpy_r_r41 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r42 = CPyStatics[10]; /* 'string' */
    cpy_r_r43 = CPyStatics[11]; /* 'name' */
    cpy_r_r44 = CPyStatics[20]; /* '' */
    cpy_r_r45 = CPyStatics[13]; /* 'type' */
    cpy_r_r46 = CPyStatics[10]; /* 'string' */
    cpy_r_r47 = CPyDict_Build(3, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45, cpy_r_r46);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 19, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r48 = PyList_New(1);
    if (unlikely(cpy_r_r48 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 19, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r49 = (CPyPtr)&((PyListObject *)cpy_r_r48)->ob_item;
    cpy_r_r50 = *(CPyPtr *)cpy_r_r49;
    *(PyObject * *)cpy_r_r50 = cpy_r_r47;
    cpy_r_r51 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r52 = CPyStatics[21]; /* 'payable' */
    cpy_r_r53 = CPyStatics[13]; /* 'type' */
    cpy_r_r54 = CPyStatics[22]; /* 'function' */
    cpy_r_r55 = CPyDict_Build(5, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r48, cpy_r_r51, cpy_r_r52, cpy_r_r53, cpy_r_r54);
    CPy_DECREF_NO_IMM(cpy_r_r37);
    CPy_DECREF_NO_IMM(cpy_r_r48);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 16, CPyStatic_globals);
        goto CPyL35;
    }
    cpy_r_r56 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r57 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r58 = CPyStatics[10]; /* 'string' */
    cpy_r_r59 = CPyStatics[11]; /* 'name' */
    cpy_r_r60 = CPyStatics[12]; /* '_value' */
    cpy_r_r61 = CPyStatics[13]; /* 'type' */
    cpy_r_r62 = CPyStatics[10]; /* 'string' */
    cpy_r_r63 = CPyDict_Build(3, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 24, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r64 = PyList_New(1);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 24, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r65 = (CPyPtr)&((PyListObject *)cpy_r_r64)->ob_item;
    cpy_r_r66 = *(CPyPtr *)cpy_r_r65;
    *(PyObject * *)cpy_r_r66 = cpy_r_r63;
    cpy_r_r67 = CPyStatics[11]; /* 'name' */
    cpy_r_r68 = CPyStatics[23]; /* 'setValue' */
    cpy_r_r69 = CPyStatics[19]; /* 'outputs' */
    cpy_r_r70 = PyList_New(0);
    if (unlikely(cpy_r_r70 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 26, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r71 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r72 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r73 = CPyStatics[13]; /* 'type' */
    cpy_r_r74 = CPyStatics[22]; /* 'function' */
    cpy_r_r75 = CPyDict_Build(5, cpy_r_r56, cpy_r_r64, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72, cpy_r_r73, cpy_r_r74);
    CPy_DECREF_NO_IMM(cpy_r_r64);
    CPy_DECREF_NO_IMM(cpy_r_r70);
    if (unlikely(cpy_r_r75 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 23, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r76 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r77 = PyList_New(0);
    if (unlikely(cpy_r_r77 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 31, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r78 = CPyStatics[11]; /* 'name' */
    cpy_r_r79 = CPyStatics[24]; /* 'value' */
    cpy_r_r80 = CPyStatics[19]; /* 'outputs' */
    cpy_r_r81 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r82 = CPyStatics[10]; /* 'string' */
    cpy_r_r83 = CPyStatics[11]; /* 'name' */
    cpy_r_r84 = CPyStatics[20]; /* '' */
    cpy_r_r85 = CPyStatics[13]; /* 'type' */
    cpy_r_r86 = CPyStatics[10]; /* 'string' */
    cpy_r_r87 = CPyDict_Build(3, cpy_r_r81, cpy_r_r82, cpy_r_r83, cpy_r_r84, cpy_r_r85, cpy_r_r86);
    if (unlikely(cpy_r_r87 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r88 = PyList_New(1);
    if (unlikely(cpy_r_r88 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 33, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r89 = (CPyPtr)&((PyListObject *)cpy_r_r88)->ob_item;
    cpy_r_r90 = *(CPyPtr *)cpy_r_r89;
    *(PyObject * *)cpy_r_r90 = cpy_r_r87;
    cpy_r_r91 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r92 = CPyStatics[25]; /* 'view' */
    cpy_r_r93 = CPyStatics[13]; /* 'type' */
    cpy_r_r94 = CPyStatics[22]; /* 'function' */
    cpy_r_r95 = CPyDict_Build(5, cpy_r_r76, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r88, cpy_r_r91, cpy_r_r92, cpy_r_r93, cpy_r_r94);
    CPy_DECREF_NO_IMM(cpy_r_r77);
    CPy_DECREF_NO_IMM(cpy_r_r88);
    if (unlikely(cpy_r_r95 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 30, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r96 = PyList_New(5);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r97 = (CPyPtr)&((PyListObject *)cpy_r_r96)->ob_item;
    cpy_r_r98 = *(CPyPtr *)cpy_r_r97;
    *(PyObject * *)cpy_r_r98 = cpy_r_r30;
    cpy_r_r99 = cpy_r_r98 + 8;
    *(PyObject * *)cpy_r_r99 = cpy_r_r35;
    cpy_r_r100 = cpy_r_r98 + 16;
    *(PyObject * *)cpy_r_r100 = cpy_r_r55;
    cpy_r_r101 = cpy_r_r98 + 24;
    *(PyObject * *)cpy_r_r101 = cpy_r_r75;
    cpy_r_r102 = cpy_r_r98 + 32;
    *(PyObject * *)cpy_r_r102 = cpy_r_r95;
    cpy_r_r103 = CPyStatic_globals;
    cpy_r_r104 = CPyStatics[26]; /* 'STRING_CONTRACT_ABI' */
    cpy_r_r105 = CPyDict_SetItem(cpy_r_r103, cpy_r_r104, cpy_r_r96);
    CPy_DECREF_NO_IMM(cpy_r_r96);
    cpy_r_r106 = cpy_r_r105 >= 0;
    if (unlikely(!cpy_r_r106)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r107 = CPyStatics[27]; /* 'bytecode' */
    cpy_r_r108 = CPyStatic_globals;
    cpy_r_r109 = CPyStatics[5]; /* 'STRING_CONTRACT_BYTECODE' */
    cpy_r_r110 = CPyDict_GetItem(cpy_r_r108, cpy_r_r109);
    if (unlikely(cpy_r_r110 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL32;
    }
    if (likely(PyUnicode_Check(cpy_r_r110)))
        cpy_r_r111 = cpy_r_r110;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 39, CPyStatic_globals, "str", cpy_r_r110);
        goto CPyL32;
    }
    cpy_r_r112 = CPyStatics[28]; /* 'bytecode_runtime' */
    cpy_r_r113 = CPyStatic_globals;
    cpy_r_r114 = CPyStatics[7]; /* 'STRING_CONTRACT_RUNTIME' */
    cpy_r_r115 = CPyDict_GetItem(cpy_r_r113, cpy_r_r114);
    if (unlikely(cpy_r_r115 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 40, CPyStatic_globals);
        goto CPyL45;
    }
    if (likely(PyUnicode_Check(cpy_r_r115)))
        cpy_r_r116 = cpy_r_r115;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 40, CPyStatic_globals, "str", cpy_r_r115);
        goto CPyL45;
    }
    cpy_r_r117 = CPyStatics[29]; /* 'abi' */
    cpy_r_r118 = CPyStatic_globals;
    cpy_r_r119 = CPyStatics[26]; /* 'STRING_CONTRACT_ABI' */
    cpy_r_r120 = CPyDict_GetItem(cpy_r_r118, cpy_r_r119);
    if (unlikely(cpy_r_r120 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL46;
    }
    if (likely(PyList_Check(cpy_r_r120)))
        cpy_r_r121 = cpy_r_r120;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 41, CPyStatic_globals, "list", cpy_r_r120);
        goto CPyL46;
    }
    cpy_r_r122 = CPyDict_Build(3, cpy_r_r107, cpy_r_r111, cpy_r_r112, cpy_r_r116, cpy_r_r117, cpy_r_r121);
    CPy_DECREF(cpy_r_r111);
    CPy_DECREF(cpy_r_r116);
    CPy_DECREF_NO_IMM(cpy_r_r121);
    if (unlikely(cpy_r_r122 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL32;
    }
    cpy_r_r123 = CPyStatic_globals;
    cpy_r_r124 = CPyStatics[30]; /* 'STRING_CONTRACT_DATA' */
    cpy_r_r125 = CPyDict_SetItem(cpy_r_r123, cpy_r_r124, cpy_r_r122);
    CPy_DECREF(cpy_r_r122);
    cpy_r_r126 = cpy_r_r125 >= 0;
    if (unlikely(!cpy_r_r126)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/string_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL32;
    }
    return 1;
CPyL32: ;
    cpy_r_r127 = 2;
    return cpy_r_r127;
CPyL33: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL32;
CPyL34: ;
    CPy_DecRef(cpy_r_r30);
    goto CPyL32;
CPyL35: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    goto CPyL32;
CPyL36: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r37);
    goto CPyL32;
CPyL37: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r37);
    CPy_DecRef(cpy_r_r47);
    goto CPyL32;
CPyL38: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    goto CPyL32;
CPyL39: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r63);
    goto CPyL32;
CPyL40: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r64);
    goto CPyL32;
CPyL41: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r75);
    goto CPyL32;
CPyL42: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r75);
    CPy_DecRef(cpy_r_r77);
    goto CPyL32;
CPyL43: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r75);
    CPy_DecRef(cpy_r_r77);
    CPy_DecRef(cpy_r_r87);
    goto CPyL32;
CPyL44: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r35);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r75);
    CPy_DecRef(cpy_r_r95);
    goto CPyL32;
CPyL45: ;
    CPy_DecRef(cpy_r_r111);
    goto CPyL32;
CPyL46: ;
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r116);
    goto CPyL32;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[31];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\26060x608060405234801561000f575f5ffd5b50604051610c1a380380610c1a83398181016040528101906100319190610193565b805f908161003f91906103ea565b50506104b9565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6100a58261005f565b810181811067ffffffffffffffff821117156100c4576100c361006f565b5b80604052505050565b5f6100d6610046565b90506100e2828261009c565b919050565b5f67ffffffffffffffff8211156101015761010061006f565b5b61010a8261005f565b9050602081019050919050565b8281835e5f83830152505050565b5f610137610132846100e7565b6100cd565b9050828152602081018484840111156101535761015261005b565b5b61015e848285610117565b509392505050565b5f82601f83011261017a57610179610057565b5b815161018a848260208601610125565b91505092915050565b5f602082840312156101a8576101a761004f565b5b5f82015167ffffffffffffffff8111156101c5576101c4610053565b5b6101d184828501610166565b91505092915050565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061022857607f821691505b60208210810361023b5761023a6101e4565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261029d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610262565b6102a78683610262565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6102eb6102e66102e1846102bf565b6102c8565b6102bf565b9050919050565b5f819050919050565b610304836102d1565b610318610310826102f2565b84845461026e565b825550505050565b5f5f905090565b61032f610320565b61033a8184846102fb565b505050565b5b8181101561035d576103525f82610327565b600181019050610340565b5050565b601f8211156103a25761037381610241565b61037c84610253565b8101602085101561038b578190505b61039f61039785610253565b83018261033f565b50505b505050565b5f82821c905092915050565b5f6103c25f19846008026103a7565b1980831691505092915050565b5f6103da83836103b3565b9150826002028217905092915050565b6103f3826101da565b67ffffffffffffffff81111561040c5761040b61006f565b5b6104168254610211565b610421828285610361565b5f60209050601f831160018114610452575f8415610440578287015190505b61044a85826103cf565b8655506104b1565b601f19841661046086610241565b5f5b8281101561048757848901518255600182019150602085019450602081019050610462565b868310156104a457848901516104a0601f8916826103b3565b8355505b6001600288020188555050505b505050505050565b610754806104c65f395ff3fe608060405260043610610037575f3560e01c806320965255146100995780633fa4f245146100b757806393a09352146100e157610038565b5b348015610043575f5ffd5b505f36606082828080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f820116905080830192505050505050509050915050805190602001f35b6100a1610109565b6040516100ae91906102a5565b60405180910390f35b3480156100c2575f5ffd5b506100cb610198565b6040516100d891906102a5565b60405180910390f35b3480156100ec575f5ffd5b5061010760048036038101906101029190610402565b610223565b005b60605f805461011790610476565b80601f016020809104026020016040519081016040528092919081815260200182805461014390610476565b801561018e5780601f106101655761010080835404028352916020019161018e565b820191905f5260205f20905b81548152906001019060200180831161017157829003601f168201915b5050505050905090565b5f80546101a490610476565b80601f01602080910402602001604051908101604052809291908181526020018280546101d090610476565b801561021b5780601f106101f25761010080835404028352916020019161021b565b820191905f5260205f20905b8154815290600101906020018083116101fe57829003601f168201915b505050505081565b805f9081610231919061064f565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61027782610235565b610281818561023f565b935061029181856020860161024f565b61029a8161025d565b840191505092915050565b5f6020820190508181035f8301526102bd818461026d565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6103148261025d565b810181811067ffffffffffffffff82111715610333576103326102de565b5b80604052505050565b5f6103456102c5565b9050610351828261030b565b919050565b5f67ffffffffffffffff8211156103705761036f6102de565b5b6103798261025d565b9050602081019050919050565b828183375f83830152505050565b5f6103a66103a184610356565b61033c565b9050828152602081018484840111156103c2576103c16102da565b5b6103cd848285610386565b509392505050565b5f82601f8301126103e9576103e86102d6565b5b81356103f9848260208601610394565b91505092915050565b5f60208284031215610417576104166102ce565b5b5f82013567ffffffffffffffff811115610434576104336102d2565b5b610440848285016103d5565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061048d57607f821691505b6020821081036104a05761049f610449565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026105027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826104c7565b61050c86836104c7565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61055061054b61054684610524565b61052d565b610524565b9050919050565b5f819050919050565b61056983610536565b61057d61057582610557565b8484546104d3565b825550505050565b5f5f905090565b610594610585565b61059f818484610560565b505050565b5b818110156105c2576105b75f8261058c565b6001810190506105a5565b5050565b601f821115610607576105d8816104a6565b6105e1846104b8565b810160208510156105f0578190505b6106046105fc856104b8565b8301826105a4565b50505b505050565b5f82821c905092915050565b5f6106275f198460080261060c565b1980831691505092915050565b5f61063f8383610618565b9150826002028217905092915050565b61065882610235565b67ffffffffffffffff811115610671576106706102de565b5b61067b8254610476565b6106868282856105c6565b5f60209050601f8311600181146106b7575f84156106a5578287015190505b6106af8582610634565b865550610716565b601f1984166106c5866104a6565b5f5b828110156106ec578489015182556001820191506020850194506020810190506106c7565b868310156107095784890151610705601f891682610618565b8355505b6001600288020188555050505b50505050505056fea264697066735822122062c13ebbeffccc0fada8dca300714023d382cee7cbd94c78a6bcf2350afd835d64736f6c634300081e0033",
    "\001\030STRING_CONTRACT_BYTECODE",
    "\001\235*0x608060405260043610610037575f3560e01c806320965255146100995780633fa4f245146100b757806393a09352146100e157610038565b5b348015610043575f5ffd5b505f36606082828080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f820116905080830192505050505050509050915050805190602001f35b6100a1610109565b6040516100ae91906102a5565b60405180910390f35b3480156100c2575f5ffd5b506100cb610198565b6040516100d891906102a5565b60405180910390f35b3480156100ec575f5ffd5b5061010760048036038101906101029190610402565b610223565b005b60605f805461011790610476565b80601f016020809104026020016040519081016040528092919081815260200182805461014390610476565b801561018e5780601f106101655761010080835404028352916020019161018e565b820191905f5260205f20905b81548152906001019060200180831161017157829003601f168201915b5050505050905090565b5f80546101a490610476565b80601f01602080910402602001604051908101604052809291908181526020018280546101d090610476565b801561021b5780601f106101f25761010080835404028352916020019161021b565b820191905f5260205f20905b8154815290600101906020018083116101fe57829003601f168201915b505050505081565b805f9081610231919061064f565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61027782610235565b610281818561023f565b935061029181856020860161024f565b61029a8161025d565b840191505092915050565b5f6020820190508181035f8301526102bd818461026d565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6103148261025d565b810181811067ffffffffffffffff82111715610333576103326102de565b5b80604052505050565b5f6103456102c5565b9050610351828261030b565b919050565b5f67ffffffffffffffff8211156103705761036f6102de565b5b6103798261025d565b9050602081019050919050565b828183375f83830152505050565b5f6103a66103a184610356565b61033c565b9050828152602081018484840111156103c2576103c16102da565b5b6103cd848285610386565b509392505050565b5f82601f8301126103e9576103e86102d6565b5b81356103f9848260208601610394565b91505092915050565b5f60208284031215610417576104166102ce565b5b5f82013567ffffffffffffffff811115610434576104336102d2565b5b610440848285016103d5565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061048d57607f821691505b6020821081036104a05761049f610449565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026105027fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826104c7565b61050c86836104c7565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61055061054b61054684610524565b61052d565b610524565b9050919050565b5f819050919050565b61056983610536565b61057d61057582610557565b8484546104d3565b825550505050565b5f5f905090565b610594610585565b61059f818484610560565b505050565b5b818110156105c2576105b75f8261058c565b6001810190506105a5565b5050565b601f821115610607576105d8816104a6565b6105e1846104b8565b810160208510156105f0578190505b6106046105fc856104b8565b8301826105a4565b50505b505050565b5f82821c905092915050565b5f6106275f198460080261060c565b1980831691505092915050565b5f61063f8383610618565b9150826002028217905092915050565b61065882610235565b67ffffffffffffffff811115610671576106706102de565b5b61067b8254610476565b6106868282856105c6565b5f60209050601f8311600181146106b7575f84156106a5578287015190505b6106af8582610634565b865550610716565b601f1984166106c5866104a6565b5f5b828110156106ec578489015182556001820191506020850194506020810190506106c7565b868310156107095784890151610705601f891682610618565b8355505b6001600288020188555050505b50505050505056fea264697066735822122062c13ebbeffccc0fada8dca300714023d382cee7cbd94c78a6bcf2350afd835d64736f6c634300081e0033",
    "\a\027STRING_CONTRACT_RUNTIME\006inputs\finternalType\006string\004name\006_value\004type",
    "\a\017stateMutability\nnonpayable\vconstructor\bfallback\bgetValue\aoutputs\000",
    "\a\apayable\bfunction\bsetValue\005value\004view\023STRING_CONTRACT_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi\024STRING_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___string_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_string_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___string_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___string_contract, "faster_web3._utils.contract_sources.contract_data.string_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___string_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___string_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_string_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.string_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_string_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_string_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_string_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
