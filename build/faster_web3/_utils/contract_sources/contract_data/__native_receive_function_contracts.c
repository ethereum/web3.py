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
#include "__native_receive_function_contracts.h"
#include "__native_internal_receive_function_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___receive_function_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.receive_function_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___receive_function_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___receive_function_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal;
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
    PyObject *cpy_r_r31;
    PyObject *cpy_r_r32;
    CPyPtr cpy_r_r33;
    CPyPtr cpy_r_r34;
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
    CPyPtr cpy_r_r62;
    CPyPtr cpy_r_r63;
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
    CPyPtr cpy_r_r75;
    CPyPtr cpy_r_r76;
    CPyPtr cpy_r_r77;
    CPyPtr cpy_r_r78;
    CPyPtr cpy_r_r79;
    PyObject *cpy_r_r80;
    PyObject *cpy_r_r81;
    int32_t cpy_r_r82;
    char cpy_r_r83;
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
    int32_t cpy_r_r102;
    char cpy_r_r103;
    PyObject *cpy_r_r104;
    PyObject *cpy_r_r105;
    PyObject *cpy_r_r106;
    int32_t cpy_r_r107;
    char cpy_r_r108;
    PyObject *cpy_r_r109;
    PyObject *cpy_r_r110;
    PyObject *cpy_r_r111;
    int32_t cpy_r_r112;
    char cpy_r_r113;
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
    CPyPtr cpy_r_r132;
    CPyPtr cpy_r_r133;
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
    CPyPtr cpy_r_r148;
    CPyPtr cpy_r_r149;
    PyObject *cpy_r_r150;
    PyObject *cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
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
    PyObject *cpy_r_r165;
    PyObject *cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject *cpy_r_r168;
    CPyPtr cpy_r_r169;
    CPyPtr cpy_r_r170;
    CPyPtr cpy_r_r171;
    CPyPtr cpy_r_r172;
    PyObject *cpy_r_r173;
    PyObject *cpy_r_r174;
    int32_t cpy_r_r175;
    char cpy_r_r176;
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
    PyObject *cpy_r_r193;
    PyObject *cpy_r_r194;
    int32_t cpy_r_r195;
    char cpy_r_r196;
    char cpy_r_r197;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL49;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5061076d8061001c5f395ff3fe60806040526004361061002c575f3560e01c80635d3a1f9d146100bb578063e00fe2eb146100f757610076565b36610076576040518060400160405280600781526020017f72656365697665000000000000000000000000000000000000000000000000008152505f9081610074919061048b565b005b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f90816100b9919061048b565b005b3480156100c6575f5ffd5b506100e160048036038101906100dc919061067a565b610121565b6040516100ee9190610717565b60405180910390f35b348015610102575f5ffd5b5061010b6101bf565b6040516101189190610717565b60405180910390f35b6060815f9081610131919061048b565b805461013c906102b2565b80601f0160208091040260200160405190810160405280929190818152602001828054610168906102b2565b80156101b35780601f1061018a576101008083540402835291602001916101b3565b820191905f5260205f20905b81548152906001019060200180831161019657829003601f168201915b50505050509050919050565b60605f80546101cd906102b2565b80601f01602080910402602001604051908101604052809291908181526020018280546101f9906102b2565b80156102445780601f1061021b57610100808354040283529160200191610244565b820191905f5260205f20905b81548152906001019060200180831161022757829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806102c957607f821691505b6020821081036102dc576102db610285565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261033e7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610303565b6103488683610303565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61038c61038761038284610360565b610369565b610360565b9050919050565b5f819050919050565b6103a583610372565b6103b96103b182610393565b84845461030f565b825550505050565b5f5f905090565b6103d06103c1565b6103db81848461039c565b505050565b5b818110156103fe576103f35f826103c8565b6001810190506103e1565b5050565b601f82111561044357610414816102e2565b61041d846102f4565b8101602085101561042c578190505b610440610438856102f4565b8301826103e0565b50505b505050565b5f82821c905092915050565b5f6104635f1984600802610448565b1980831691505092915050565b5f61047b8383610454565b9150826002028217905092915050565b6104948261024e565b67ffffffffffffffff8111156104ad576104ac610258565b5b6104b782546102b2565b6104c2828285610402565b5f60209050601f8311600181146104f3575f84156104e1578287015190505b6104eb8582610470565b865550610552565b601f198416610501866102e2565b5f5b8281101561052857848901518255600182019150602085019450602081019050610503565b868310156105455784890151610541601f891682610454565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b61058c82610573565b810181811067ffffffffffffffff821117156105ab576105aa610258565b5b80604052505050565b5f6105bd61055a565b90506105c98282610583565b919050565b5f67ffffffffffffffff8211156105e8576105e7610258565b5b6105f182610573565b9050602081019050919050565b828183375f83830152505050565b5f61061e610619846105ce565b6105b4565b90508281526020810184848401111561063a5761063961056f565b5b6106458482856105fe565b509392505050565b5f82601f8301126106615761066061056b565b5b813561067184826020860161060c565b91505092915050565b5f6020828403121561068f5761068e610563565b5b5f82013567ffffffffffffffff8111156106ac576106ab610567565b5b6106b88482850161064d565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6106e98261024e565b6106f381856106c1565b93506107038185602086016106d1565b61070c81610573565b840191505092915050565b5f6020820190508181035f83015261072f81846106df565b90509291505056fea2646970667358221220838a5744d5c70fa48b5d3d06020d3825a03e7845033c1a3f012abb3151c97f7064736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'RECEIVE_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 7, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x60806040526004361061002c575f3560e01c80635d3a1f9d146100bb578063e00fe2eb146100f757610076565b36610076576040518060400160405280600781526020017f72656365697665000000000000000000000000000000000000000000000000008152505f9081610074919061048b565b005b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f90816100b9919061048b565b005b3480156100c6575f5ffd5b506100e160048036038101906100dc919061067a565b610121565b6040516100ee9190610717565b60405180910390f35b348015610102575f5ffd5b5061010b6101bf565b6040516101189190610717565b60405180910390f35b6060815f9081610131919061048b565b805461013c906102b2565b80601f0160208091040260200160405190810160405280929190818152602001828054610168906102b2565b80156101b35780601f1061018a576101008083540402835291602001916101b3565b820191905f5260205f20905b81548152906001019060200180831161019657829003601f168201915b50505050509050919050565b60605f80546101cd906102b2565b80601f01602080910402602001604051908101604052809291908181526020018280546101f9906102b2565b80156102445780601f1061021b57610100808354040283529160200191610244565b820191905f5260205f20905b81548152906001019060200180831161022757829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806102c957607f821691505b6020821081036102dc576102db610285565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261033e7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610303565b6103488683610303565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61038c61038761038284610360565b610369565b610360565b9050919050565b5f819050919050565b6103a583610372565b6103b96103b182610393565b84845461030f565b825550505050565b5f5f905090565b6103d06103c1565b6103db81848461039c565b505050565b5b818110156103fe576103f35f826103c8565b6001810190506103e1565b5050565b601f82111561044357610414816102e2565b61041d846102f4565b8101602085101561042c578190505b610440610438856102f4565b8301826103e0565b50505b505050565b5f82821c905092915050565b5f6104635f1984600802610448565b1980831691505092915050565b5f61047b8383610454565b9150826002028217905092915050565b6104948261024e565b67ffffffffffffffff8111156104ad576104ac610258565b5b6104b782546102b2565b6104c2828285610402565b5f60209050601f8311600181146104f3575f84156104e1578287015190505b6104eb8582610470565b865550610552565b601f198416610501866102e2565b5f5b8281101561052857848901518255600182019150602085019450602081019050610503565b868310156105455784890151610541601f891682610454565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b61058c82610573565b810181811067ffffffffffffffff821117156105ab576105aa610258565b5b80604052505050565b5f6105bd61055a565b90506105c98282610583565b919050565b5f67ffffffffffffffff8211156105e8576105e7610258565b5b6105f182610573565b9050602081019050919050565b828183375f83830152505050565b5f61061e610619846105ce565b6105b4565b90508281526020810184848401111561063a5761063961056f565b5b6106458482856105fe565b509392505050565b5f82601f8301126106615761066061056b565b5b813561067184826020860161060c565b91505092915050565b5f6020828403121561068f5761068e610563565b5b5f82013567ffffffffffffffff8111156106ac576106ab610567565b5b6106b88482850161064d565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6106e98261024e565b6106f381856106c1565b93506107038185602086016106d1565b61070c81610573565b840191505092915050565b5f6020820190508181035f83015261072f81846106df565b90509291505056fea2646970667358221220838a5744d5c70fa48b5d3d06020d3825a03e7845033c1a3f012abb3151c97f7064736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'RECEIVE_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 8, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r16 = CPyStatics[9]; /* 'payable' */
    cpy_r_r17 = CPyStatics[10]; /* 'type' */
    cpy_r_r18 = CPyStatics[11]; /* 'fallback' */
    cpy_r_r19 = CPyDict_Build(2, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18);
    if (unlikely(cpy_r_r19 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r20 = CPyStatics[12]; /* 'inputs' */
    cpy_r_r21 = PyList_New(0);
    if (unlikely(cpy_r_r21 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 12, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r22 = CPyStatics[13]; /* 'name' */
    cpy_r_r23 = CPyStatics[14]; /* 'getText' */
    cpy_r_r24 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r25 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r26 = CPyStatics[17]; /* 'string' */
    cpy_r_r27 = CPyStatics[13]; /* 'name' */
    cpy_r_r28 = CPyStatics[18]; /* '' */
    cpy_r_r29 = CPyStatics[10]; /* 'type' */
    cpy_r_r30 = CPyStatics[17]; /* 'string' */
    cpy_r_r31 = CPyDict_Build(3, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r30);
    if (unlikely(cpy_r_r31 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 14, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r32 = PyList_New(1);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 14, CPyStatic_globals);
        goto CPyL52;
    }
    cpy_r_r33 = (CPyPtr)&((PyListObject *)cpy_r_r32)->ob_item;
    cpy_r_r34 = *(CPyPtr *)cpy_r_r33;
    *(PyObject * *)cpy_r_r34 = cpy_r_r31;
    cpy_r_r35 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r36 = CPyStatics[19]; /* 'view' */
    cpy_r_r37 = CPyStatics[10]; /* 'type' */
    cpy_r_r38 = CPyStatics[20]; /* 'function' */
    cpy_r_r39 = CPyDict_Build(5, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23, cpy_r_r24, cpy_r_r32, cpy_r_r35, cpy_r_r36, cpy_r_r37, cpy_r_r38);
    CPy_DECREF_NO_IMM(cpy_r_r21);
    CPy_DECREF_NO_IMM(cpy_r_r32);
    if (unlikely(cpy_r_r39 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r40 = CPyStatics[12]; /* 'inputs' */
    cpy_r_r41 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r42 = CPyStatics[17]; /* 'string' */
    cpy_r_r43 = CPyStatics[13]; /* 'name' */
    cpy_r_r44 = CPyStatics[21]; /* 'new_text' */
    cpy_r_r45 = CPyStatics[10]; /* 'type' */
    cpy_r_r46 = CPyStatics[17]; /* 'string' */
    cpy_r_r47 = CPyDict_Build(3, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45, cpy_r_r46);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 19, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r48 = PyList_New(1);
    if (unlikely(cpy_r_r48 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 19, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r49 = (CPyPtr)&((PyListObject *)cpy_r_r48)->ob_item;
    cpy_r_r50 = *(CPyPtr *)cpy_r_r49;
    *(PyObject * *)cpy_r_r50 = cpy_r_r47;
    cpy_r_r51 = CPyStatics[13]; /* 'name' */
    cpy_r_r52 = CPyStatics[22]; /* 'setText' */
    cpy_r_r53 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r54 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r55 = CPyStatics[17]; /* 'string' */
    cpy_r_r56 = CPyStatics[13]; /* 'name' */
    cpy_r_r57 = CPyStatics[18]; /* '' */
    cpy_r_r58 = CPyStatics[10]; /* 'type' */
    cpy_r_r59 = CPyStatics[17]; /* 'string' */
    cpy_r_r60 = CPyDict_Build(3, cpy_r_r54, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59);
    if (unlikely(cpy_r_r60 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 21, CPyStatic_globals);
        goto CPyL55;
    }
    cpy_r_r61 = PyList_New(1);
    if (unlikely(cpy_r_r61 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 21, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r62 = (CPyPtr)&((PyListObject *)cpy_r_r61)->ob_item;
    cpy_r_r63 = *(CPyPtr *)cpy_r_r62;
    *(PyObject * *)cpy_r_r63 = cpy_r_r60;
    cpy_r_r64 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r65 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r66 = CPyStatics[10]; /* 'type' */
    cpy_r_r67 = CPyStatics[20]; /* 'function' */
    cpy_r_r68 = CPyDict_Build(5, cpy_r_r40, cpy_r_r48, cpy_r_r51, cpy_r_r52, cpy_r_r53, cpy_r_r61, cpy_r_r64, cpy_r_r65, cpy_r_r66, cpy_r_r67);
    CPy_DECREF_NO_IMM(cpy_r_r48);
    CPy_DECREF_NO_IMM(cpy_r_r61);
    if (unlikely(cpy_r_r68 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r69 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r70 = CPyStatics[9]; /* 'payable' */
    cpy_r_r71 = CPyStatics[10]; /* 'type' */
    cpy_r_r72 = CPyStatics[24]; /* 'receive' */
    cpy_r_r73 = CPyDict_Build(2, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL57;
    }
    cpy_r_r74 = PyList_New(4);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r75 = (CPyPtr)&((PyListObject *)cpy_r_r74)->ob_item;
    cpy_r_r76 = *(CPyPtr *)cpy_r_r75;
    *(PyObject * *)cpy_r_r76 = cpy_r_r19;
    cpy_r_r77 = cpy_r_r76 + 8;
    *(PyObject * *)cpy_r_r77 = cpy_r_r39;
    cpy_r_r78 = cpy_r_r76 + 16;
    *(PyObject * *)cpy_r_r78 = cpy_r_r68;
    cpy_r_r79 = cpy_r_r76 + 24;
    *(PyObject * *)cpy_r_r79 = cpy_r_r73;
    cpy_r_r80 = CPyStatic_globals;
    cpy_r_r81 = CPyStatics[25]; /* 'RECEIVE_FUNCTION_CONTRACT_ABI' */
    cpy_r_r82 = CPyDict_SetItem(cpy_r_r80, cpy_r_r81, cpy_r_r74);
    CPy_DECREF_NO_IMM(cpy_r_r74);
    cpy_r_r83 = cpy_r_r82 >= 0;
    if (unlikely(!cpy_r_r83)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r84 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r85 = CPyStatic_globals;
    cpy_r_r86 = CPyStatics[5]; /* 'RECEIVE_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r87 = CPyDict_GetItem(cpy_r_r85, cpy_r_r86);
    if (unlikely(cpy_r_r87 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 28, CPyStatic_globals);
        goto CPyL49;
    }
    if (likely(PyUnicode_Check(cpy_r_r87)))
        cpy_r_r88 = cpy_r_r87;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 28, CPyStatic_globals, "str", cpy_r_r87);
        goto CPyL49;
    }
    cpy_r_r89 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r90 = CPyStatic_globals;
    cpy_r_r91 = CPyStatics[7]; /* 'RECEIVE_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r92 = CPyDict_GetItem(cpy_r_r90, cpy_r_r91);
    if (unlikely(cpy_r_r92 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 29, CPyStatic_globals);
        goto CPyL59;
    }
    if (likely(PyUnicode_Check(cpy_r_r92)))
        cpy_r_r93 = cpy_r_r92;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 29, CPyStatic_globals, "str", cpy_r_r92);
        goto CPyL59;
    }
    cpy_r_r94 = CPyStatics[28]; /* 'abi' */
    cpy_r_r95 = CPyStatic_globals;
    cpy_r_r96 = CPyStatics[25]; /* 'RECEIVE_FUNCTION_CONTRACT_ABI' */
    cpy_r_r97 = CPyDict_GetItem(cpy_r_r95, cpy_r_r96);
    if (unlikely(cpy_r_r97 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 30, CPyStatic_globals);
        goto CPyL60;
    }
    if (likely(PyList_Check(cpy_r_r97)))
        cpy_r_r98 = cpy_r_r97;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 30, CPyStatic_globals, "list", cpy_r_r97);
        goto CPyL60;
    }
    cpy_r_r99 = CPyDict_Build(3, cpy_r_r84, cpy_r_r88, cpy_r_r89, cpy_r_r93, cpy_r_r94, cpy_r_r98);
    CPy_DECREF(cpy_r_r88);
    CPy_DECREF(cpy_r_r93);
    CPy_DECREF_NO_IMM(cpy_r_r98);
    if (unlikely(cpy_r_r99 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 27, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r100 = CPyStatic_globals;
    cpy_r_r101 = CPyStatics[29]; /* 'RECEIVE_FUNCTION_CONTRACT_DATA' */
    cpy_r_r102 = CPyDict_SetItem(cpy_r_r100, cpy_r_r101, cpy_r_r99);
    CPy_DECREF(cpy_r_r99);
    cpy_r_r103 = cpy_r_r102 >= 0;
    if (unlikely(!cpy_r_r103)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 27, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r104 = CPyStatics[30]; /* '0x6080604052348015600e575f5ffd5b506107188061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610038575f3560e01c80635d3a1f9d1461007e578063e00fe2eb146100ae57610039565b5b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f908161007c9190610436565b005b61009860048036038101906100939190610625565b6100cc565b6040516100a591906106c2565b60405180910390f35b6100b661016a565b6040516100c391906106c2565b60405180910390f35b6060815f90816100dc9190610436565b80546100e79061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101139061025d565b801561015e5780601f106101355761010080835404028352916020019161015e565b820191905f5260205f20905b81548152906001019060200180831161014157829003601f168201915b50505050509050919050565b60605f80546101789061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101a49061025d565b80156101ef5780601f106101c6576101008083540402835291602001916101ef565b820191905f5260205f20905b8154815290600101906020018083116101d257829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061027457607f821691505b60208210810361028757610286610230565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102e97fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826102ae565b6102f386836102ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61033761033261032d8461030b565b610314565b61030b565b9050919050565b5f819050919050565b6103508361031d565b61036461035c8261033e565b8484546102ba565b825550505050565b5f5f905090565b61037b61036c565b610386818484610347565b505050565b5b818110156103a95761039e5f82610373565b60018101905061038c565b5050565b601f8211156103ee576103bf8161028d565b6103c88461029f565b810160208510156103d7578190505b6103eb6103e38561029f565b83018261038b565b50505b505050565b5f82821c905092915050565b5f61040e5f19846008026103f3565b1980831691505092915050565b5f61042683836103ff565b9150826002028217905092915050565b61043f826101f9565b67ffffffffffffffff81111561045857610457610203565b5b610462825461025d565b61046d8282856103ad565b5f60209050601f83116001811461049e575f841561048c578287015190505b610496858261041b565b8655506104fd565b601f1984166104ac8661028d565b5f5b828110156104d3578489015182556001820191506020850194506020810190506104ae565b868310156104f057848901516104ec601f8916826103ff565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6105378261051e565b810181811067ffffffffffffffff8211171561055657610555610203565b5b80604052505050565b5f610568610505565b9050610574828261052e565b919050565b5f67ffffffffffffffff82111561059357610592610203565b5b61059c8261051e565b9050602081019050919050565b828183375f83830152505050565b5f6105c96105c484610579565b61055f565b9050828152602081018484840111156105e5576105e461051a565b5b6105f08482856105a9565b509392505050565b5f82601f83011261060c5761060b610516565b5b813561061c8482602086016105b7565b91505092915050565b5f6020828403121561063a5761063961050e565b5b5f82013567ffffffffffffffff81111561065757610656610512565b5b610663848285016105f8565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f610694826101f9565b61069e818561066c565b93506106ae81856020860161067c565b6106b78161051e565b840191505092915050565b5f6020820190508181035f8301526106da818461068a565b90509291505056fea26469706673582212209768bc0c518f9f30f85e9a2aa2d59494907bf2411e4588944c18481ac9c320d764736f6c634300081e0033' */
    cpy_r_r105 = CPyStatic_globals;
    cpy_r_r106 = CPyStatics[31]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r107 = CPyDict_SetItem(cpy_r_r105, cpy_r_r106, cpy_r_r104);
    cpy_r_r108 = cpy_r_r107 >= 0;
    if (unlikely(!cpy_r_r108)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 35, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r109 = CPyStatics[32]; /* '0x608060405234801561000f575f5ffd5b5060043610610038575f3560e01c80635d3a1f9d1461007e578063e00fe2eb146100ae57610039565b5b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f908161007c9190610436565b005b61009860048036038101906100939190610625565b6100cc565b6040516100a591906106c2565b60405180910390f35b6100b661016a565b6040516100c391906106c2565b60405180910390f35b6060815f90816100dc9190610436565b80546100e79061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101139061025d565b801561015e5780601f106101355761010080835404028352916020019161015e565b820191905f5260205f20905b81548152906001019060200180831161014157829003601f168201915b50505050509050919050565b60605f80546101789061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101a49061025d565b80156101ef5780601f106101c6576101008083540402835291602001916101ef565b820191905f5260205f20905b8154815290600101906020018083116101d257829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061027457607f821691505b60208210810361028757610286610230565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102e97fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826102ae565b6102f386836102ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61033761033261032d8461030b565b610314565b61030b565b9050919050565b5f819050919050565b6103508361031d565b61036461035c8261033e565b8484546102ba565b825550505050565b5f5f905090565b61037b61036c565b610386818484610347565b505050565b5b818110156103a95761039e5f82610373565b60018101905061038c565b5050565b601f8211156103ee576103bf8161028d565b6103c88461029f565b810160208510156103d7578190505b6103eb6103e38561029f565b83018261038b565b50505b505050565b5f82821c905092915050565b5f61040e5f19846008026103f3565b1980831691505092915050565b5f61042683836103ff565b9150826002028217905092915050565b61043f826101f9565b67ffffffffffffffff81111561045857610457610203565b5b610462825461025d565b61046d8282856103ad565b5f60209050601f83116001811461049e575f841561048c578287015190505b610496858261041b565b8655506104fd565b601f1984166104ac8661028d565b5f5b828110156104d3578489015182556001820191506020850194506020810190506104ae565b868310156104f057848901516104ec601f8916826103ff565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6105378261051e565b810181811067ffffffffffffffff8211171561055657610555610203565b5b80604052505050565b5f610568610505565b9050610574828261052e565b919050565b5f67ffffffffffffffff82111561059357610592610203565b5b61059c8261051e565b9050602081019050919050565b828183375f83830152505050565b5f6105c96105c484610579565b61055f565b9050828152602081018484840111156105e5576105e461051a565b5b6105f08482856105a9565b509392505050565b5f82601f83011261060c5761060b610516565b5b813561061c8482602086016105b7565b91505092915050565b5f6020828403121561063a5761063961050e565b5b5f82013567ffffffffffffffff81111561065757610656610512565b5b610663848285016105f8565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f610694826101f9565b61069e818561066c565b93506106ae81856020860161067c565b6106b78161051e565b840191505092915050565b5f6020820190508181035f8301526106da818461068a565b90509291505056fea26469706673582212209768bc0c518f9f30f85e9a2aa2d59494907bf2411e4588944c18481ac9c320d764736f6c634300081e0033' */
    cpy_r_r110 = CPyStatic_globals;
    cpy_r_r111 = CPyStatics[33]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r112 = CPyDict_SetItem(cpy_r_r110, cpy_r_r111, cpy_r_r109);
    cpy_r_r113 = cpy_r_r112 >= 0;
    if (unlikely(!cpy_r_r113)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 36, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r114 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r115 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r116 = CPyStatics[10]; /* 'type' */
    cpy_r_r117 = CPyStatics[11]; /* 'fallback' */
    cpy_r_r118 = CPyDict_Build(2, cpy_r_r114, cpy_r_r115, cpy_r_r116, cpy_r_r117);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 38, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r119 = CPyStatics[12]; /* 'inputs' */
    cpy_r_r120 = PyList_New(0);
    if (unlikely(cpy_r_r120 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 40, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r121 = CPyStatics[13]; /* 'name' */
    cpy_r_r122 = CPyStatics[14]; /* 'getText' */
    cpy_r_r123 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r124 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r125 = CPyStatics[17]; /* 'string' */
    cpy_r_r126 = CPyStatics[13]; /* 'name' */
    cpy_r_r127 = CPyStatics[18]; /* '' */
    cpy_r_r128 = CPyStatics[10]; /* 'type' */
    cpy_r_r129 = CPyStatics[17]; /* 'string' */
    cpy_r_r130 = CPyDict_Build(3, cpy_r_r124, cpy_r_r125, cpy_r_r126, cpy_r_r127, cpy_r_r128, cpy_r_r129);
    if (unlikely(cpy_r_r130 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 42, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r131 = PyList_New(1);
    if (unlikely(cpy_r_r131 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 42, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r132 = (CPyPtr)&((PyListObject *)cpy_r_r131)->ob_item;
    cpy_r_r133 = *(CPyPtr *)cpy_r_r132;
    *(PyObject * *)cpy_r_r133 = cpy_r_r130;
    cpy_r_r134 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r135 = CPyStatics[19]; /* 'view' */
    cpy_r_r136 = CPyStatics[10]; /* 'type' */
    cpy_r_r137 = CPyStatics[20]; /* 'function' */
    cpy_r_r138 = CPyDict_Build(5, cpy_r_r119, cpy_r_r120, cpy_r_r121, cpy_r_r122, cpy_r_r123, cpy_r_r131, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137);
    CPy_DECREF_NO_IMM(cpy_r_r120);
    CPy_DECREF_NO_IMM(cpy_r_r131);
    if (unlikely(cpy_r_r138 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 39, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r139 = CPyStatics[12]; /* 'inputs' */
    cpy_r_r140 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r141 = CPyStatics[17]; /* 'string' */
    cpy_r_r142 = CPyStatics[13]; /* 'name' */
    cpy_r_r143 = CPyStatics[21]; /* 'new_text' */
    cpy_r_r144 = CPyStatics[10]; /* 'type' */
    cpy_r_r145 = CPyStatics[17]; /* 'string' */
    cpy_r_r146 = CPyDict_Build(3, cpy_r_r140, cpy_r_r141, cpy_r_r142, cpy_r_r143, cpy_r_r144, cpy_r_r145);
    if (unlikely(cpy_r_r146 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r147 = PyList_New(1);
    if (unlikely(cpy_r_r147 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r148 = (CPyPtr)&((PyListObject *)cpy_r_r147)->ob_item;
    cpy_r_r149 = *(CPyPtr *)cpy_r_r148;
    *(PyObject * *)cpy_r_r149 = cpy_r_r146;
    cpy_r_r150 = CPyStatics[13]; /* 'name' */
    cpy_r_r151 = CPyStatics[22]; /* 'setText' */
    cpy_r_r152 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r153 = CPyStatics[16]; /* 'internalType' */
    cpy_r_r154 = CPyStatics[17]; /* 'string' */
    cpy_r_r155 = CPyStatics[13]; /* 'name' */
    cpy_r_r156 = CPyStatics[18]; /* '' */
    cpy_r_r157 = CPyStatics[10]; /* 'type' */
    cpy_r_r158 = CPyStatics[17]; /* 'string' */
    cpy_r_r159 = CPyDict_Build(3, cpy_r_r153, cpy_r_r154, cpy_r_r155, cpy_r_r156, cpy_r_r157, cpy_r_r158);
    if (unlikely(cpy_r_r159 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r160 = PyList_New(1);
    if (unlikely(cpy_r_r160 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r161 = (CPyPtr)&((PyListObject *)cpy_r_r160)->ob_item;
    cpy_r_r162 = *(CPyPtr *)cpy_r_r161;
    *(PyObject * *)cpy_r_r162 = cpy_r_r159;
    cpy_r_r163 = CPyStatics[8]; /* 'stateMutability' */
    cpy_r_r164 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r165 = CPyStatics[10]; /* 'type' */
    cpy_r_r166 = CPyStatics[20]; /* 'function' */
    cpy_r_r167 = CPyDict_Build(5, cpy_r_r139, cpy_r_r147, cpy_r_r150, cpy_r_r151, cpy_r_r152, cpy_r_r160, cpy_r_r163, cpy_r_r164, cpy_r_r165, cpy_r_r166);
    CPy_DECREF_NO_IMM(cpy_r_r147);
    CPy_DECREF_NO_IMM(cpy_r_r160);
    if (unlikely(cpy_r_r167 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 46, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r168 = PyList_New(3);
    if (unlikely(cpy_r_r168 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r169 = (CPyPtr)&((PyListObject *)cpy_r_r168)->ob_item;
    cpy_r_r170 = *(CPyPtr *)cpy_r_r169;
    *(PyObject * *)cpy_r_r170 = cpy_r_r118;
    cpy_r_r171 = cpy_r_r170 + 8;
    *(PyObject * *)cpy_r_r171 = cpy_r_r138;
    cpy_r_r172 = cpy_r_r170 + 16;
    *(PyObject * *)cpy_r_r172 = cpy_r_r167;
    cpy_r_r173 = CPyStatic_globals;
    cpy_r_r174 = CPyStatics[34]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_ABI' */
    cpy_r_r175 = CPyDict_SetItem(cpy_r_r173, cpy_r_r174, cpy_r_r168);
    CPy_DECREF_NO_IMM(cpy_r_r168);
    cpy_r_r176 = cpy_r_r175 >= 0;
    if (unlikely(!cpy_r_r176)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r177 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r178 = CPyStatic_globals;
    cpy_r_r179 = CPyStatics[31]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_BYTECODE' */
    cpy_r_r180 = CPyDict_GetItem(cpy_r_r178, cpy_r_r179);
    if (unlikely(cpy_r_r180 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 55, CPyStatic_globals);
        goto CPyL49;
    }
    if (likely(PyUnicode_Check(cpy_r_r180)))
        cpy_r_r181 = cpy_r_r180;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 55, CPyStatic_globals, "str", cpy_r_r180);
        goto CPyL49;
    }
    cpy_r_r182 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r183 = CPyStatic_globals;
    cpy_r_r184 = CPyStatics[33]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_RUNTIME' */
    cpy_r_r185 = CPyDict_GetItem(cpy_r_r183, cpy_r_r184);
    if (unlikely(cpy_r_r185 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL69;
    }
    if (likely(PyUnicode_Check(cpy_r_r185)))
        cpy_r_r186 = cpy_r_r185;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 56, CPyStatic_globals, "str", cpy_r_r185);
        goto CPyL69;
    }
    cpy_r_r187 = CPyStatics[28]; /* 'abi' */
    cpy_r_r188 = CPyStatic_globals;
    cpy_r_r189 = CPyStatics[34]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_ABI' */
    cpy_r_r190 = CPyDict_GetItem(cpy_r_r188, cpy_r_r189);
    if (unlikely(cpy_r_r190 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL70;
    }
    if (likely(PyList_Check(cpy_r_r190)))
        cpy_r_r191 = cpy_r_r190;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 57, CPyStatic_globals, "list", cpy_r_r190);
        goto CPyL70;
    }
    cpy_r_r192 = CPyDict_Build(3, cpy_r_r177, cpy_r_r181, cpy_r_r182, cpy_r_r186, cpy_r_r187, cpy_r_r191);
    CPy_DECREF(cpy_r_r181);
    CPy_DECREF(cpy_r_r186);
    CPy_DECREF_NO_IMM(cpy_r_r191);
    if (unlikely(cpy_r_r192 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r193 = CPyStatic_globals;
    cpy_r_r194 = CPyStatics[35]; /* 'NO_RECEIVE_FUNCTION_CONTRACT_DATA' */
    cpy_r_r195 = CPyDict_SetItem(cpy_r_r193, cpy_r_r194, cpy_r_r192);
    CPy_DECREF(cpy_r_r192);
    cpy_r_r196 = cpy_r_r195 >= 0;
    if (unlikely(!cpy_r_r196)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/receive_function_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL49;
    }
    return 1;
CPyL49: ;
    cpy_r_r197 = 2;
    return cpy_r_r197;
CPyL50: ;
    CPy_DecRef(cpy_r_r19);
    goto CPyL49;
CPyL51: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r21);
    goto CPyL49;
CPyL52: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r21);
    CPy_DecRef(cpy_r_r31);
    goto CPyL49;
CPyL53: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    goto CPyL49;
CPyL54: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    CPy_DecRef(cpy_r_r47);
    goto CPyL49;
CPyL55: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    CPy_DecRef(cpy_r_r48);
    goto CPyL49;
CPyL56: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    CPy_DecRef(cpy_r_r48);
    CPy_DecRef(cpy_r_r60);
    goto CPyL49;
CPyL57: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    CPy_DecRef(cpy_r_r68);
    goto CPyL49;
CPyL58: ;
    CPy_DecRef(cpy_r_r19);
    CPy_DecRef(cpy_r_r39);
    CPy_DecRef(cpy_r_r68);
    CPy_DecRef(cpy_r_r73);
    goto CPyL49;
CPyL59: ;
    CPy_DecRef(cpy_r_r88);
    goto CPyL49;
CPyL60: ;
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r93);
    goto CPyL49;
CPyL61: ;
    CPy_DecRef(cpy_r_r118);
    goto CPyL49;
CPyL62: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r120);
    goto CPyL49;
CPyL63: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r120);
    CPy_DecRef(cpy_r_r130);
    goto CPyL49;
CPyL64: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r138);
    goto CPyL49;
CPyL65: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r146);
    goto CPyL49;
CPyL66: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r147);
    goto CPyL49;
CPyL67: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r147);
    CPy_DecRef(cpy_r_r159);
    goto CPyL49;
CPyL68: ;
    CPy_DecRef(cpy_r_r118);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r167);
    goto CPyL49;
CPyL69: ;
    CPy_DecRef(cpy_r_r181);
    goto CPyL49;
CPyL70: ;
    CPy_DecRef(cpy_r_r181);
    CPy_DecRef(cpy_r_r186);
    goto CPyL49;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[36];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\236\0240x6080604052348015600e575f5ffd5b5061076d8061001c5f395ff3fe60806040526004361061002c575f3560e01c80635d3a1f9d146100bb578063e00fe2eb146100f757610076565b36610076576040518060400160405280600781526020017f72656365697665000000000000000000000000000000000000000000000000008152505f9081610074919061048b565b005b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f90816100b9919061048b565b005b3480156100c6575f5ffd5b506100e160048036038101906100dc919061067a565b610121565b6040516100ee9190610717565b60405180910390f35b348015610102575f5ffd5b5061010b6101bf565b6040516101189190610717565b60405180910390f35b6060815f9081610131919061048b565b805461013c906102b2565b80601f0160208091040260200160405190810160405280929190818152602001828054610168906102b2565b80156101b35780601f1061018a576101008083540402835291602001916101b3565b820191905f5260205f20905b81548152906001019060200180831161019657829003601f168201915b50505050509050919050565b60605f80546101cd906102b2565b80601f01602080910402602001604051908101604052809291908181526020018280546101f9906102b2565b80156102445780601f1061021b57610100808354040283529160200191610244565b820191905f5260205f20905b81548152906001019060200180831161022757829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806102c957607f821691505b6020821081036102dc576102db610285565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261033e7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610303565b6103488683610303565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61038c61038761038284610360565b610369565b610360565b9050919050565b5f819050919050565b6103a583610372565b6103b96103b182610393565b84845461030f565b825550505050565b5f5f905090565b6103d06103c1565b6103db81848461039c565b505050565b5b818110156103fe576103f35f826103c8565b6001810190506103e1565b5050565b601f82111561044357610414816102e2565b61041d846102f4565b8101602085101561042c578190505b610440610438856102f4565b8301826103e0565b50505b505050565b5f82821c905092915050565b5f6104635f1984600802610448565b1980831691505092915050565b5f61047b8383610454565b9150826002028217905092915050565b6104948261024e565b67ffffffffffffffff8111156104ad576104ac610258565b5b6104b782546102b2565b6104c2828285610402565b5f60209050601f8311600181146104f3575f84156104e1578287015190505b6104eb8582610470565b865550610552565b601f198416610501866102e2565b5f5b8281101561052857848901518255600182019150602085019450602081019050610503565b868310156105455784890151610541601f891682610454565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b61058c82610573565b810181811067ffffffffffffffff821117156105ab576105aa610258565b5b80604052505050565b5f6105bd61055a565b90506105c98282610583565b919050565b5f67ffffffffffffffff8211156105e8576105e7610258565b5b6105f182610573565b9050602081019050919050565b828183375f83830152505050565b5f61061e610619846105ce565b6105b4565b90508281526020810184848401111561063a5761063961056f565b5b6106458482856105fe565b509392505050565b5f82601f8301126106615761066061056b565b5b813561067184826020860161060c565b91505092915050565b5f6020828403121561068f5761068e610563565b5b5f82013567ffffffffffffffff8111156106ac576106ab610567565b5b6106b88482850161064d565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6106e98261024e565b6106f381856106c1565b93506107038185602086016106d1565b61070c81610573565b840191505092915050565b5f6020820190508181035f83015261072f81846106df565b90509291505056fea2646970667358221220838a5744d5c70fa48b5d3d06020d3825a03e7845033c1a3f012abb3151c97f7064736f6c634300081e0033",
    "\001\"RECEIVE_FUNCTION_CONTRACT_BYTECODE",
    "\001\235\\0x60806040526004361061002c575f3560e01c80635d3a1f9d146100bb578063e00fe2eb146100f757610076565b36610076576040518060400160405280600781526020017f72656365697665000000000000000000000000000000000000000000000000008152505f9081610074919061048b565b005b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f90816100b9919061048b565b005b3480156100c6575f5ffd5b506100e160048036038101906100dc919061067a565b610121565b6040516100ee9190610717565b60405180910390f35b348015610102575f5ffd5b5061010b6101bf565b6040516101189190610717565b60405180910390f35b6060815f9081610131919061048b565b805461013c906102b2565b80601f0160208091040260200160405190810160405280929190818152602001828054610168906102b2565b80156101b35780601f1061018a576101008083540402835291602001916101b3565b820191905f5260205f20905b81548152906001019060200180831161019657829003601f168201915b50505050509050919050565b60605f80546101cd906102b2565b80601f01602080910402602001604051908101604052809291908181526020018280546101f9906102b2565b80156102445780601f1061021b57610100808354040283529160200191610244565b820191905f5260205f20905b81548152906001019060200180831161022757829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806102c957607f821691505b6020821081036102dc576102db610285565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261033e7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610303565b6103488683610303565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61038c61038761038284610360565b610369565b610360565b9050919050565b5f819050919050565b6103a583610372565b6103b96103b182610393565b84845461030f565b825550505050565b5f5f905090565b6103d06103c1565b6103db81848461039c565b505050565b5b818110156103fe576103f35f826103c8565b6001810190506103e1565b5050565b601f82111561044357610414816102e2565b61041d846102f4565b8101602085101561042c578190505b610440610438856102f4565b8301826103e0565b50505b505050565b5f82821c905092915050565b5f6104635f1984600802610448565b1980831691505092915050565b5f61047b8383610454565b9150826002028217905092915050565b6104948261024e565b67ffffffffffffffff8111156104ad576104ac610258565b5b6104b782546102b2565b6104c2828285610402565b5f60209050601f8311600181146104f3575f84156104e1578287015190505b6104eb8582610470565b865550610552565b601f198416610501866102e2565b5f5b8281101561052857848901518255600182019150602085019450602081019050610503565b868310156105455784890151610541601f891682610454565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b61058c82610573565b810181811067ffffffffffffffff821117156105ab576105aa610258565b5b80604052505050565b5f6105bd61055a565b90506105c98282610583565b919050565b5f67ffffffffffffffff8211156105e8576105e7610258565b5b6105f182610573565b9050602081019050919050565b828183375f83830152505050565b5f61061e610619846105ce565b6105b4565b90508281526020810184848401111561063a5761063961056f565b5b6106458482856105fe565b509392505050565b5f82601f8301126106615761066061056b565b5b813561067184826020860161060c565b91505092915050565b5f6020828403121561068f5761068e610563565b5b5f82013567ffffffffffffffff8111156106ac576106ab610567565b5b6106b88482850161064d565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6106e98261024e565b6106f381856106c1565b93506107038185602086016106d1565b61070c81610573565b840191505092915050565b5f6020820190508181035f83015261072f81846106df565b90509291505056fea2646970667358221220838a5744d5c70fa48b5d3d06020d3825a03e7845033c1a3f012abb3151c97f7064736f6c634300081e0033",
    "\004!RECEIVE_FUNCTION_CONTRACT_RUNTIME\017stateMutability\apayable\004type",
    "\t\bfallback\006inputs\004name\agetText\aoutputs\finternalType\006string\000\004view",
    "\005\bfunction\bnew_text\asetText\nnonpayable\areceive",
    "\004\035RECEIVE_FUNCTION_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\036RECEIVE_FUNCTION_CONTRACT_DATA",
    "\001\234j0x6080604052348015600e575f5ffd5b506107188061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610038575f3560e01c80635d3a1f9d1461007e578063e00fe2eb146100ae57610039565b5b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f908161007c9190610436565b005b61009860048036038101906100939190610625565b6100cc565b6040516100a591906106c2565b60405180910390f35b6100b661016a565b6040516100c391906106c2565b60405180910390f35b6060815f90816100dc9190610436565b80546100e79061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101139061025d565b801561015e5780601f106101355761010080835404028352916020019161015e565b820191905f5260205f20905b81548152906001019060200180831161014157829003601f168201915b50505050509050919050565b60605f80546101789061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101a49061025d565b80156101ef5780601f106101c6576101008083540402835291602001916101ef565b820191905f5260205f20905b8154815290600101906020018083116101d257829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061027457607f821691505b60208210810361028757610286610230565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102e97fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826102ae565b6102f386836102ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61033761033261032d8461030b565b610314565b61030b565b9050919050565b5f819050919050565b6103508361031d565b61036461035c8261033e565b8484546102ba565b825550505050565b5f5f905090565b61037b61036c565b610386818484610347565b505050565b5b818110156103a95761039e5f82610373565b60018101905061038c565b5050565b601f8211156103ee576103bf8161028d565b6103c88461029f565b810160208510156103d7578190505b6103eb6103e38561029f565b83018261038b565b50505b505050565b5f82821c905092915050565b5f61040e5f19846008026103f3565b1980831691505092915050565b5f61042683836103ff565b9150826002028217905092915050565b61043f826101f9565b67ffffffffffffffff81111561045857610457610203565b5b610462825461025d565b61046d8282856103ad565b5f60209050601f83116001811461049e575f841561048c578287015190505b610496858261041b565b8655506104fd565b601f1984166104ac8661028d565b5f5b828110156104d3578489015182556001820191506020850194506020810190506104ae565b868310156104f057848901516104ec601f8916826103ff565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6105378261051e565b810181811067ffffffffffffffff8211171561055657610555610203565b5b80604052505050565b5f610568610505565b9050610574828261052e565b919050565b5f67ffffffffffffffff82111561059357610592610203565b5b61059c8261051e565b9050602081019050919050565b828183375f83830152505050565b5f6105c96105c484610579565b61055f565b9050828152602081018484840111156105e5576105e461051a565b5b6105f08482856105a9565b509392505050565b5f82601f83011261060c5761060b610516565b5b813561061c8482602086016105b7565b91505092915050565b5f6020828403121561063a5761063961050e565b5b5f82013567ffffffffffffffff81111561065757610656610512565b5b610663848285016105f8565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f610694826101f9565b61069e818561066c565b93506106ae81856020860161067c565b6106b78161051e565b840191505092915050565b5f6020820190508181035f8301526106da818461068a565b90509291505056fea26469706673582212209768bc0c518f9f30f85e9a2aa2d59494907bf2411e4588944c18481ac9c320d764736f6c634300081e0033",
    "\001%NO_RECEIVE_FUNCTION_CONTRACT_BYTECODE",
    "\001\23420x608060405234801561000f575f5ffd5b5060043610610038575f3560e01c80635d3a1f9d1461007e578063e00fe2eb146100ae57610039565b5b6040518060400160405280600881526020017f66616c6c6261636b0000000000000000000000000000000000000000000000008152505f908161007c9190610436565b005b61009860048036038101906100939190610625565b6100cc565b6040516100a591906106c2565b60405180910390f35b6100b661016a565b6040516100c391906106c2565b60405180910390f35b6060815f90816100dc9190610436565b80546100e79061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101139061025d565b801561015e5780601f106101355761010080835404028352916020019161015e565b820191905f5260205f20905b81548152906001019060200180831161014157829003601f168201915b50505050509050919050565b60605f80546101789061025d565b80601f01602080910402602001604051908101604052809291908181526020018280546101a49061025d565b80156101ef5780601f106101c6576101008083540402835291602001916101ef565b820191905f5260205f20905b8154815290600101906020018083116101d257829003601f168201915b5050505050905090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061027457607f821691505b60208210810361028757610286610230565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102e97fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826102ae565b6102f386836102ae565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61033761033261032d8461030b565b610314565b61030b565b9050919050565b5f819050919050565b6103508361031d565b61036461035c8261033e565b8484546102ba565b825550505050565b5f5f905090565b61037b61036c565b610386818484610347565b505050565b5b818110156103a95761039e5f82610373565b60018101905061038c565b5050565b601f8211156103ee576103bf8161028d565b6103c88461029f565b810160208510156103d7578190505b6103eb6103e38561029f565b83018261038b565b50505b505050565b5f82821c905092915050565b5f61040e5f19846008026103f3565b1980831691505092915050565b5f61042683836103ff565b9150826002028217905092915050565b61043f826101f9565b67ffffffffffffffff81111561045857610457610203565b5b610462825461025d565b61046d8282856103ad565b5f60209050601f83116001811461049e575f841561048c578287015190505b610496858261041b565b8655506104fd565b601f1984166104ac8661028d565b5f5b828110156104d3578489015182556001820191506020850194506020810190506104ae565b868310156104f057848901516104ec601f8916826103ff565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6105378261051e565b810181811067ffffffffffffffff8211171561055657610555610203565b5b80604052505050565b5f610568610505565b9050610574828261052e565b919050565b5f67ffffffffffffffff82111561059357610592610203565b5b61059c8261051e565b9050602081019050919050565b828183375f83830152505050565b5f6105c96105c484610579565b61055f565b9050828152602081018484840111156105e5576105e461051a565b5b6105f08482856105a9565b509392505050565b5f82601f83011261060c5761060b610516565b5b813561061c8482602086016105b7565b91505092915050565b5f6020828403121561063a5761063961050e565b5b5f82013567ffffffffffffffff81111561065757610656610512565b5b610663848285016105f8565b91505092915050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f610694826101f9565b61069e818561066c565b93506106ae81856020860161067c565b6106b78161051e565b840191505092915050565b5f6020820190508181035f8301526106da818461068a565b90509291505056fea26469706673582212209768bc0c518f9f30f85e9a2aa2d59494907bf2411e4588944c18481ac9c320d764736f6c634300081e0033",
    "\002$NO_RECEIVE_FUNCTION_CONTRACT_RUNTIME NO_RECEIVE_FUNCTION_CONTRACT_ABI",
    "\001!NO_RECEIVE_FUNCTION_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___receive_function_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_receive_function_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___receive_function_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___receive_function_contracts, "faster_web3._utils.contract_sources.contract_data.receive_function_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___receive_function_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___receive_function_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_receive_function_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.receive_function_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_receive_function_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_receive_function_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_receive_function_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
