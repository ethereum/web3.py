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
#include "__native_offchain_lookup.h"
#include "__native_internal_offchain_lookup.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___offchain_lookup(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.offchain_lookup",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___offchain_lookup(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___offchain_lookup(CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal;
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
    CPyPtr cpy_r_r52;
    CPyPtr cpy_r_r53;
    CPyPtr cpy_r_r54;
    CPyPtr cpy_r_r55;
    CPyPtr cpy_r_r56;
    CPyPtr cpy_r_r57;
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
    PyObject *cpy_r_r73;
    PyObject *cpy_r_r74;
    PyObject *cpy_r_r75;
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
    PyObject *cpy_r_r86;
    PyObject *cpy_r_r87;
    PyObject *cpy_r_r88;
    PyObject *cpy_r_r89;
    PyObject *cpy_r_r90;
    PyObject *cpy_r_r91;
    CPyPtr cpy_r_r92;
    CPyPtr cpy_r_r93;
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
    CPyPtr cpy_r_r128;
    CPyPtr cpy_r_r129;
    CPyPtr cpy_r_r130;
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
    PyObject *cpy_r_r144;
    PyObject *cpy_r_r145;
    PyObject *cpy_r_r146;
    PyObject *cpy_r_r147;
    PyObject *cpy_r_r148;
    PyObject *cpy_r_r149;
    CPyPtr cpy_r_r150;
    CPyPtr cpy_r_r151;
    CPyPtr cpy_r_r152;
    CPyPtr cpy_r_r153;
    CPyPtr cpy_r_r154;
    PyObject *cpy_r_r155;
    PyObject *cpy_r_r156;
    int32_t cpy_r_r157;
    char cpy_r_r158;
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
    int32_t cpy_r_r177;
    char cpy_r_r178;
    char cpy_r_r179;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", -1, CPyStatic_globals);
        goto CPyL38;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x608060405260405180604001604052806040518060600160405280602c815260200161105e602c913981526020016040518060400160405280601781526020017f68747470733a2f2f776562332e70792f676174657761790000000000000000008152508152505f906002610075929190610087565b50348015610081575f5ffd5b50610465565b828054828255905f5260205f209081019282156100cd579160200282015b828111156100cc5782518290816100bc9190610396565b50916020019190600101906100a5565b5b5090506100da91906100de565b5090565b5b808211156100fd575f81816100f49190610101565b506001016100df565b5090565b50805461010d906101bd565b5f825580601f1061011e575061013b565b601f0160209004905f5260205f209081019061013a919061013e565b5b50565b5b80821115610155575f815f90555060010161013f565b5090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806101d457607f821691505b6020821081036101e7576101e6610190565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102497fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261020e565b610253868361020e565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61029761029261028d8461026b565b610274565b61026b565b9050919050565b5f819050919050565b6102b08361027d565b6102c46102bc8261029e565b84845461021a565b825550505050565b5f5f905090565b6102db6102cc565b6102e68184846102a7565b505050565b5b81811015610309576102fe5f826102d3565b6001810190506102ec565b5050565b601f82111561034e5761031f816101ed565b610328846101ff565b81016020851015610337578190505b61034b610343856101ff565b8301826102eb565b50505b505050565b5f82821c905092915050565b5f61036e5f1984600802610353565b1980831691505092915050565b5f610386838361035f565b9150826002028217905092915050565b61039f82610159565b67ffffffffffffffff8111156103b8576103b7610163565b5b6103c282546101bd565b6103cd82828561030d565b5f60209050601f8311600181146103fe575f84156103ec578287015190505b6103f6858261037b565b86555061045d565b601f19841661040c866101ed565b5f5b828110156104335784890151825560018201915060208501945060208101905061040e565b86831015610450578489015161044c601f89168261035f565b8355505b6001600288020188555050505b505050505050565b610bec806104725f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c806309a3c01b146100435780636337ed5814610061578063da96d05a14610091575b5f5ffd5b61004b6100c1565b60405161005891906103f2565b60405180910390f35b61007b60048036038101906100769190610484565b610110565b60405161008891906103f2565b60405180910390f35b6100ab60048036038101906100a691906104cf565b6101fc565b6040516100b891906103f2565b60405180910390f35b606080305f826309a3c01b60e01b846040517f556f1830000000000000000000000000000000000000000000000000000000008152600401610107959493929190610783565b60405180910390fd5b60605f83838101906101229190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af07581604051602001610156919061099c565b60405160208183030381529060405280519060200120146101ac576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101a390610a0c565b60405180910390fd5b305f858563da96d05a60e01b88886040517f556f18300000000000000000000000000000000000000000000000000000000081526004016101f39796959493929190610a56565b60405180910390fd5b60605f858581019061020e9190610911565b90507faed76f463930323372899e36460e078e5292aac45f645bbe567be6fca83ede1081604051602001610242919061099c565b6040516020818303038152906040528051906020012014610298576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028f90610b30565b60405180910390fd5b5f84848101906102a89190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af075816040516020016102dc919061099c565b6040516020818303038152906040528051906020012014610332576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032990610b98565b60405180910390fd5b86868080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505092505050949350505050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6103c482610382565b6103ce818561038c565b93506103de81856020860161039c565b6103e7816103aa565b840191505092915050565b5f6020820190508181035f83015261040a81846103ba565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f84011261044457610443610423565b5b8235905067ffffffffffffffff81111561046157610460610427565b5b60208301915083600182028301111561047d5761047c61042b565b5b9250929050565b5f5f6020838503121561049a5761049961041b565b5b5f83013567ffffffffffffffff8111156104b7576104b661041f565b5b6104c38582860161042f565b92509250509250929050565b5f5f5f5f604085870312156104e7576104e661041b565b5b5f85013567ffffffffffffffff8111156105045761050361041f565b5b6105108782880161042f565b9450945050602085013567ffffffffffffffff8111156105335761053261041f565b5b61053f8782880161042f565b925092505092959194509250565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105768261054d565b9050919050565b6105868161056c565b82525050565b5f81549050919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806105fc57607f821691505b60208210810361060f5761060e6105b8565b5b50919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b5f8154610643816105e5565b61064d8186610615565b9450600182165f8114610667576001811461067d576106af565b60ff1983168652811515602002860193506106af565b61068685610625565b5f5b838110156106a757815481890152600182019150602081019050610688565b808801955050505b50505092915050565b5f6106c38383610637565b905092915050565b5f600182019050919050565b5f6106e18261058c565b6106eb8185610596565b9350836020820285016106fd856105a6565b805f5b858110156107375784840389528161071885826106b8565b9450610723836106cb565b925060208a01995050600181019050610700565b50829750879550505050505092915050565b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61077d81610749565b82525050565b5f60a0820190506107965f83018861057d565b81810360208301526107a881876106d7565b905081810360408301526107bc81866103ba565b90506107cb6060830185610774565b81810360808301526107dd81846103ba565b90509695505050505050565b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610823826103aa565b810181811067ffffffffffffffff82111715610842576108416107ed565b5b80604052505050565b5f610854610412565b9050610860828261081a565b919050565b5f67ffffffffffffffff82111561087f5761087e6107ed565b5b610888826103aa565b9050602081019050919050565b828183375f83830152505050565b5f6108b56108b084610865565b61084b565b9050828152602081018484840111156108d1576108d06107e9565b5b6108dc848285610895565b509392505050565b5f82601f8301126108f8576108f7610423565b5b81356109088482602086016108a3565b91505092915050565b5f602082840312156109265761092561041b565b5b5f82013567ffffffffffffffff8111156109435761094261041f565b5b61094f848285016108e4565b91505092915050565b5f81519050919050565b5f81905092915050565b5f61097682610958565b6109808185610962565b935061099081856020860161039c565b80840191505092915050565b5f6109a7828461096c565b915081905092915050565b5f82825260208201905092915050565b7f7465737420646174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f6109f6601c836109b2565b9150610a01826109c2565b602082019050919050565b5f6020820190508181035f830152610a23816109ea565b9050919050565b5f610a35838561038c565b9350610a42838584610895565b610a4b836103aa565b840190509392505050565b5f60a082019050610a695f83018a61057d565b8181036020830152610a7b81896106d7565b90508181036040830152610a90818789610a2a565b9050610a9f6060830186610774565b8181036080830152610ab2818486610a2a565b905098975050505050505050565b7f68747470207265717565737420726573756c742076616c69646174696f6e20665f8201527f61696c65642e0000000000000000000000000000000000000000000000000000602082015250565b5f610b1a6026836109b2565b9150610b2582610ac0565b604082019050919050565b5f6020820190508181035f830152610b4781610b0e565b9050919050565b7f6578747261446174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f610b82601c836109b2565b9150610b8d82610b4e565b602082019050919050565b5f6020820190508181035f830152610baf81610b76565b905091905056fea2646970667358221220029be82598e02eb26c8cc4f7656db4919c9c779bb468c366f11ca5263eef888064736f6c634300081e003368747470733a2f2f776562332e70792f676174657761792f7b73656e6465727d2f7b646174617d2e6a736f6e' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'OFFCHAIN_LOOKUP_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 7, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c806309a3c01b146100435780636337ed5814610061578063da96d05a14610091575b5f5ffd5b61004b6100c1565b60405161005891906103f2565b60405180910390f35b61007b60048036038101906100769190610484565b610110565b60405161008891906103f2565b60405180910390f35b6100ab60048036038101906100a691906104cf565b6101fc565b6040516100b891906103f2565b60405180910390f35b606080305f826309a3c01b60e01b846040517f556f1830000000000000000000000000000000000000000000000000000000008152600401610107959493929190610783565b60405180910390fd5b60605f83838101906101229190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af07581604051602001610156919061099c565b60405160208183030381529060405280519060200120146101ac576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101a390610a0c565b60405180910390fd5b305f858563da96d05a60e01b88886040517f556f18300000000000000000000000000000000000000000000000000000000081526004016101f39796959493929190610a56565b60405180910390fd5b60605f858581019061020e9190610911565b90507faed76f463930323372899e36460e078e5292aac45f645bbe567be6fca83ede1081604051602001610242919061099c565b6040516020818303038152906040528051906020012014610298576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028f90610b30565b60405180910390fd5b5f84848101906102a89190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af075816040516020016102dc919061099c565b6040516020818303038152906040528051906020012014610332576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032990610b98565b60405180910390fd5b86868080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505092505050949350505050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6103c482610382565b6103ce818561038c565b93506103de81856020860161039c565b6103e7816103aa565b840191505092915050565b5f6020820190508181035f83015261040a81846103ba565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f84011261044457610443610423565b5b8235905067ffffffffffffffff81111561046157610460610427565b5b60208301915083600182028301111561047d5761047c61042b565b5b9250929050565b5f5f6020838503121561049a5761049961041b565b5b5f83013567ffffffffffffffff8111156104b7576104b661041f565b5b6104c38582860161042f565b92509250509250929050565b5f5f5f5f604085870312156104e7576104e661041b565b5b5f85013567ffffffffffffffff8111156105045761050361041f565b5b6105108782880161042f565b9450945050602085013567ffffffffffffffff8111156105335761053261041f565b5b61053f8782880161042f565b925092505092959194509250565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105768261054d565b9050919050565b6105868161056c565b82525050565b5f81549050919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806105fc57607f821691505b60208210810361060f5761060e6105b8565b5b50919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b5f8154610643816105e5565b61064d8186610615565b9450600182165f8114610667576001811461067d576106af565b60ff1983168652811515602002860193506106af565b61068685610625565b5f5b838110156106a757815481890152600182019150602081019050610688565b808801955050505b50505092915050565b5f6106c38383610637565b905092915050565b5f600182019050919050565b5f6106e18261058c565b6106eb8185610596565b9350836020820285016106fd856105a6565b805f5b858110156107375784840389528161071885826106b8565b9450610723836106cb565b925060208a01995050600181019050610700565b50829750879550505050505092915050565b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61077d81610749565b82525050565b5f60a0820190506107965f83018861057d565b81810360208301526107a881876106d7565b905081810360408301526107bc81866103ba565b90506107cb6060830185610774565b81810360808301526107dd81846103ba565b90509695505050505050565b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610823826103aa565b810181811067ffffffffffffffff82111715610842576108416107ed565b5b80604052505050565b5f610854610412565b9050610860828261081a565b919050565b5f67ffffffffffffffff82111561087f5761087e6107ed565b5b610888826103aa565b9050602081019050919050565b828183375f83830152505050565b5f6108b56108b084610865565b61084b565b9050828152602081018484840111156108d1576108d06107e9565b5b6108dc848285610895565b509392505050565b5f82601f8301126108f8576108f7610423565b5b81356109088482602086016108a3565b91505092915050565b5f602082840312156109265761092561041b565b5b5f82013567ffffffffffffffff8111156109435761094261041f565b5b61094f848285016108e4565b91505092915050565b5f81519050919050565b5f81905092915050565b5f61097682610958565b6109808185610962565b935061099081856020860161039c565b80840191505092915050565b5f6109a7828461096c565b915081905092915050565b5f82825260208201905092915050565b7f7465737420646174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f6109f6601c836109b2565b9150610a01826109c2565b602082019050919050565b5f6020820190508181035f830152610a23816109ea565b9050919050565b5f610a35838561038c565b9350610a42838584610895565b610a4b836103aa565b840190509392505050565b5f60a082019050610a695f83018a61057d565b8181036020830152610a7b81896106d7565b90508181036040830152610a90818789610a2a565b9050610a9f6060830186610774565b8181036080830152610ab2818486610a2a565b905098975050505050505050565b7f68747470207265717565737420726573756c742076616c69646174696f6e20665f8201527f61696c65642e0000000000000000000000000000000000000000000000000000602082015250565b5f610b1a6026836109b2565b9150610b2582610ac0565b604082019050919050565b5f6020820190508181035f830152610b4781610b0e565b9050919050565b7f6578747261446174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f610b82601c836109b2565b9150610b8d82610b4e565b602082019050919050565b5f6020820190508181035f830152610baf81610b76565b905091905056fea2646970667358221220029be82598e02eb26c8cc4f7656db4919c9c779bb468c366f11ca5263eef888064736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'OFFCHAIN_LOOKUP_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 8, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'address' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* 'sender' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'address' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 12, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r23 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r24 = CPyStatics[14]; /* 'string[]' */
    cpy_r_r25 = CPyStatics[11]; /* 'name' */
    cpy_r_r26 = CPyStatics[15]; /* 'urls' */
    cpy_r_r27 = CPyStatics[13]; /* 'type' */
    cpy_r_r28 = CPyStatics[14]; /* 'string[]' */
    cpy_r_r29 = CPyDict_Build(3, cpy_r_r23, cpy_r_r24, cpy_r_r25, cpy_r_r26, cpy_r_r27, cpy_r_r28);
    if (unlikely(cpy_r_r29 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 13, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r30 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r31 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r32 = CPyStatics[11]; /* 'name' */
    cpy_r_r33 = CPyStatics[17]; /* 'callData' */
    cpy_r_r34 = CPyStatics[13]; /* 'type' */
    cpy_r_r35 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r36 = CPyDict_Build(3, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34, cpy_r_r35);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 14, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r37 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r38 = CPyStatics[18]; /* 'bytes4' */
    cpy_r_r39 = CPyStatics[11]; /* 'name' */
    cpy_r_r40 = CPyStatics[19]; /* 'callbackFunction' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[18]; /* 'bytes4' */
    cpy_r_r43 = CPyDict_Build(3, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 15, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r44 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r45 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r46 = CPyStatics[11]; /* 'name' */
    cpy_r_r47 = CPyStatics[20]; /* 'extraData' */
    cpy_r_r48 = CPyStatics[13]; /* 'type' */
    cpy_r_r49 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r50 = CPyDict_Build(3, cpy_r_r44, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48, cpy_r_r49);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 16, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r51 = PyList_New(5);
    if (unlikely(cpy_r_r51 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 11, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r52 = (CPyPtr)&((PyListObject *)cpy_r_r51)->ob_item;
    cpy_r_r53 = *(CPyPtr *)cpy_r_r52;
    *(PyObject * *)cpy_r_r53 = cpy_r_r22;
    cpy_r_r54 = cpy_r_r53 + 8;
    *(PyObject * *)cpy_r_r54 = cpy_r_r29;
    cpy_r_r55 = cpy_r_r53 + 16;
    *(PyObject * *)cpy_r_r55 = cpy_r_r36;
    cpy_r_r56 = cpy_r_r53 + 24;
    *(PyObject * *)cpy_r_r56 = cpy_r_r43;
    cpy_r_r57 = cpy_r_r53 + 32;
    *(PyObject * *)cpy_r_r57 = cpy_r_r50;
    cpy_r_r58 = CPyStatics[11]; /* 'name' */
    cpy_r_r59 = CPyStatics[21]; /* 'OffchainLookup' */
    cpy_r_r60 = CPyStatics[13]; /* 'type' */
    cpy_r_r61 = CPyStatics[22]; /* 'error' */
    cpy_r_r62 = CPyDict_Build(3, cpy_r_r15, cpy_r_r51, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61);
    CPy_DECREF_NO_IMM(cpy_r_r51);
    if (unlikely(cpy_r_r62 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 10, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r63 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r64 = PyList_New(0);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 22, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r65 = CPyStatics[11]; /* 'name' */
    cpy_r_r66 = CPyStatics[23]; /* 'continuousOffchainLookup' */
    cpy_r_r67 = CPyStatics[24]; /* 'outputs' */
    cpy_r_r68 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r69 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r70 = CPyStatics[11]; /* 'name' */
    cpy_r_r71 = CPyStatics[25]; /* '' */
    cpy_r_r72 = CPyStatics[13]; /* 'type' */
    cpy_r_r73 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r74 = CPyDict_Build(3, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72, cpy_r_r73);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 24, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r75 = PyList_New(1);
    if (unlikely(cpy_r_r75 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 24, CPyStatic_globals);
        goto CPyL46;
    }
    cpy_r_r76 = (CPyPtr)&((PyListObject *)cpy_r_r75)->ob_item;
    cpy_r_r77 = *(CPyPtr *)cpy_r_r76;
    *(PyObject * *)cpy_r_r77 = cpy_r_r74;
    cpy_r_r78 = CPyStatics[26]; /* 'stateMutability' */
    cpy_r_r79 = CPyStatics[27]; /* 'nonpayable' */
    cpy_r_r80 = CPyStatics[13]; /* 'type' */
    cpy_r_r81 = CPyStatics[28]; /* 'function' */
    cpy_r_r82 = CPyDict_Build(5, cpy_r_r63, cpy_r_r64, cpy_r_r65, cpy_r_r66, cpy_r_r67, cpy_r_r75, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81);
    CPy_DECREF_NO_IMM(cpy_r_r64);
    CPy_DECREF_NO_IMM(cpy_r_r75);
    if (unlikely(cpy_r_r82 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 21, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r83 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r84 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r85 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r86 = CPyStatics[11]; /* 'name' */
    cpy_r_r87 = CPyStatics[29]; /* 'specifiedDataFromTest' */
    cpy_r_r88 = CPyStatics[13]; /* 'type' */
    cpy_r_r89 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r90 = CPyDict_Build(3, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87, cpy_r_r88, cpy_r_r89);
    if (unlikely(cpy_r_r90 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 30, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r91 = PyList_New(1);
    if (unlikely(cpy_r_r91 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 29, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r92 = (CPyPtr)&((PyListObject *)cpy_r_r91)->ob_item;
    cpy_r_r93 = *(CPyPtr *)cpy_r_r92;
    *(PyObject * *)cpy_r_r93 = cpy_r_r90;
    cpy_r_r94 = CPyStatics[11]; /* 'name' */
    cpy_r_r95 = CPyStatics[30]; /* 'testOffchainLookup' */
    cpy_r_r96 = CPyStatics[24]; /* 'outputs' */
    cpy_r_r97 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r98 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r99 = CPyStatics[11]; /* 'name' */
    cpy_r_r100 = CPyStatics[25]; /* '' */
    cpy_r_r101 = CPyStatics[13]; /* 'type' */
    cpy_r_r102 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r103 = CPyDict_Build(3, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101, cpy_r_r102);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 33, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r104 = PyList_New(1);
    if (unlikely(cpy_r_r104 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 33, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r105 = (CPyPtr)&((PyListObject *)cpy_r_r104)->ob_item;
    cpy_r_r106 = *(CPyPtr *)cpy_r_r105;
    *(PyObject * *)cpy_r_r106 = cpy_r_r103;
    cpy_r_r107 = CPyStatics[26]; /* 'stateMutability' */
    cpy_r_r108 = CPyStatics[27]; /* 'nonpayable' */
    cpy_r_r109 = CPyStatics[13]; /* 'type' */
    cpy_r_r110 = CPyStatics[28]; /* 'function' */
    cpy_r_r111 = CPyDict_Build(5, cpy_r_r83, cpy_r_r91, cpy_r_r94, cpy_r_r95, cpy_r_r96, cpy_r_r104, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110);
    CPy_DECREF_NO_IMM(cpy_r_r91);
    CPy_DECREF_NO_IMM(cpy_r_r104);
    if (unlikely(cpy_r_r111 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 28, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r112 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r113 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r114 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r115 = CPyStatics[11]; /* 'name' */
    cpy_r_r116 = CPyStatics[31]; /* 'result' */
    cpy_r_r117 = CPyStatics[13]; /* 'type' */
    cpy_r_r118 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r119 = CPyDict_Build(3, cpy_r_r113, cpy_r_r114, cpy_r_r115, cpy_r_r116, cpy_r_r117, cpy_r_r118);
    if (unlikely(cpy_r_r119 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 39, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r120 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r121 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r122 = CPyStatics[11]; /* 'name' */
    cpy_r_r123 = CPyStatics[20]; /* 'extraData' */
    cpy_r_r124 = CPyStatics[13]; /* 'type' */
    cpy_r_r125 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r126 = CPyDict_Build(3, cpy_r_r120, cpy_r_r121, cpy_r_r122, cpy_r_r123, cpy_r_r124, cpy_r_r125);
    if (unlikely(cpy_r_r126 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 40, CPyStatic_globals);
        goto CPyL52;
    }
    cpy_r_r127 = PyList_New(2);
    if (unlikely(cpy_r_r127 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 38, CPyStatic_globals);
        goto CPyL53;
    }
    cpy_r_r128 = (CPyPtr)&((PyListObject *)cpy_r_r127)->ob_item;
    cpy_r_r129 = *(CPyPtr *)cpy_r_r128;
    *(PyObject * *)cpy_r_r129 = cpy_r_r119;
    cpy_r_r130 = cpy_r_r129 + 8;
    *(PyObject * *)cpy_r_r130 = cpy_r_r126;
    cpy_r_r131 = CPyStatics[11]; /* 'name' */
    cpy_r_r132 = CPyStatics[32]; /* 'testOffchainLookupWithProof' */
    cpy_r_r133 = CPyStatics[24]; /* 'outputs' */
    cpy_r_r134 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r135 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r136 = CPyStatics[11]; /* 'name' */
    cpy_r_r137 = CPyStatics[25]; /* '' */
    cpy_r_r138 = CPyStatics[13]; /* 'type' */
    cpy_r_r139 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r140 = CPyDict_Build(3, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137, cpy_r_r138, cpy_r_r139);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 43, CPyStatic_globals);
        goto CPyL54;
    }
    cpy_r_r141 = PyList_New(1);
    if (unlikely(cpy_r_r141 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 43, CPyStatic_globals);
        goto CPyL55;
    }
    cpy_r_r142 = (CPyPtr)&((PyListObject *)cpy_r_r141)->ob_item;
    cpy_r_r143 = *(CPyPtr *)cpy_r_r142;
    *(PyObject * *)cpy_r_r143 = cpy_r_r140;
    cpy_r_r144 = CPyStatics[26]; /* 'stateMutability' */
    cpy_r_r145 = CPyStatics[27]; /* 'nonpayable' */
    cpy_r_r146 = CPyStatics[13]; /* 'type' */
    cpy_r_r147 = CPyStatics[28]; /* 'function' */
    cpy_r_r148 = CPyDict_Build(5, cpy_r_r112, cpy_r_r127, cpy_r_r131, cpy_r_r132, cpy_r_r133, cpy_r_r141, cpy_r_r144, cpy_r_r145, cpy_r_r146, cpy_r_r147);
    CPy_DECREF_NO_IMM(cpy_r_r127);
    CPy_DECREF_NO_IMM(cpy_r_r141);
    if (unlikely(cpy_r_r148 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 37, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r149 = PyList_New(4);
    if (unlikely(cpy_r_r149 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 9, CPyStatic_globals);
        goto CPyL56;
    }
    cpy_r_r150 = (CPyPtr)&((PyListObject *)cpy_r_r149)->ob_item;
    cpy_r_r151 = *(CPyPtr *)cpy_r_r150;
    *(PyObject * *)cpy_r_r151 = cpy_r_r62;
    cpy_r_r152 = cpy_r_r151 + 8;
    *(PyObject * *)cpy_r_r152 = cpy_r_r82;
    cpy_r_r153 = cpy_r_r151 + 16;
    *(PyObject * *)cpy_r_r153 = cpy_r_r111;
    cpy_r_r154 = cpy_r_r151 + 24;
    *(PyObject * *)cpy_r_r154 = cpy_r_r148;
    cpy_r_r155 = CPyStatic_globals;
    cpy_r_r156 = CPyStatics[33]; /* 'OFFCHAIN_LOOKUP_ABI' */
    cpy_r_r157 = CPyDict_SetItem(cpy_r_r155, cpy_r_r156, cpy_r_r149);
    CPy_DECREF_NO_IMM(cpy_r_r149);
    cpy_r_r158 = cpy_r_r157 >= 0;
    if (unlikely(!cpy_r_r158)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 9, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r159 = CPyStatics[34]; /* 'bytecode' */
    cpy_r_r160 = CPyStatic_globals;
    cpy_r_r161 = CPyStatics[5]; /* 'OFFCHAIN_LOOKUP_BYTECODE' */
    cpy_r_r162 = CPyDict_GetItem(cpy_r_r160, cpy_r_r161);
    if (unlikely(cpy_r_r162 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 49, CPyStatic_globals);
        goto CPyL38;
    }
    if (likely(PyUnicode_Check(cpy_r_r162)))
        cpy_r_r163 = cpy_r_r162;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 49, CPyStatic_globals, "str", cpy_r_r162);
        goto CPyL38;
    }
    cpy_r_r164 = CPyStatics[35]; /* 'bytecode_runtime' */
    cpy_r_r165 = CPyStatic_globals;
    cpy_r_r166 = CPyStatics[7]; /* 'OFFCHAIN_LOOKUP_RUNTIME' */
    cpy_r_r167 = CPyDict_GetItem(cpy_r_r165, cpy_r_r166);
    if (unlikely(cpy_r_r167 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 50, CPyStatic_globals);
        goto CPyL57;
    }
    if (likely(PyUnicode_Check(cpy_r_r167)))
        cpy_r_r168 = cpy_r_r167;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 50, CPyStatic_globals, "str", cpy_r_r167);
        goto CPyL57;
    }
    cpy_r_r169 = CPyStatics[36]; /* 'abi' */
    cpy_r_r170 = CPyStatic_globals;
    cpy_r_r171 = CPyStatics[33]; /* 'OFFCHAIN_LOOKUP_ABI' */
    cpy_r_r172 = CPyDict_GetItem(cpy_r_r170, cpy_r_r171);
    if (unlikely(cpy_r_r172 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 51, CPyStatic_globals);
        goto CPyL58;
    }
    if (likely(PyList_Check(cpy_r_r172)))
        cpy_r_r173 = cpy_r_r172;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 51, CPyStatic_globals, "list", cpy_r_r172);
        goto CPyL58;
    }
    cpy_r_r174 = CPyDict_Build(3, cpy_r_r159, cpy_r_r163, cpy_r_r164, cpy_r_r168, cpy_r_r169, cpy_r_r173);
    CPy_DECREF(cpy_r_r163);
    CPy_DECREF(cpy_r_r168);
    CPy_DECREF_NO_IMM(cpy_r_r173);
    if (unlikely(cpy_r_r174 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 48, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r175 = CPyStatic_globals;
    cpy_r_r176 = CPyStatics[37]; /* 'OFFCHAIN_LOOKUP_DATA' */
    cpy_r_r177 = CPyDict_SetItem(cpy_r_r175, cpy_r_r176, cpy_r_r174);
    CPy_DECREF(cpy_r_r174);
    cpy_r_r178 = cpy_r_r177 >= 0;
    if (unlikely(!cpy_r_r178)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/offchain_lookup.py", "<module>", 48, CPyStatic_globals);
        goto CPyL38;
    }
    return 1;
CPyL38: ;
    cpy_r_r179 = 2;
    return cpy_r_r179;
CPyL39: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL38;
CPyL40: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    goto CPyL38;
CPyL41: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    CPy_DecRef(cpy_r_r36);
    goto CPyL38;
CPyL42: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    CPy_DecRef(cpy_r_r36);
    CPy_DecRef(cpy_r_r43);
    goto CPyL38;
CPyL43: ;
    CPy_DecRef(cpy_r_r22);
    CPy_DecRef(cpy_r_r29);
    CPy_DecRef(cpy_r_r36);
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r50);
    goto CPyL38;
CPyL44: ;
    CPy_DecRef(cpy_r_r62);
    goto CPyL38;
CPyL45: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r64);
    goto CPyL38;
CPyL46: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r64);
    CPy_DecRef(cpy_r_r74);
    goto CPyL38;
CPyL47: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    goto CPyL38;
CPyL48: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r90);
    goto CPyL38;
CPyL49: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r91);
    goto CPyL38;
CPyL50: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r91);
    CPy_DecRef(cpy_r_r103);
    goto CPyL38;
CPyL51: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    goto CPyL38;
CPyL52: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r119);
    goto CPyL38;
CPyL53: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r119);
    CPy_DecRef(cpy_r_r126);
    goto CPyL38;
CPyL54: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r127);
    goto CPyL38;
CPyL55: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r140);
    goto CPyL38;
CPyL56: ;
    CPy_DecRef(cpy_r_r62);
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r111);
    CPy_DecRef(cpy_r_r148);
    goto CPyL38;
CPyL57: ;
    CPy_DecRef(cpy_r_r163);
    goto CPyL38;
CPyL58: ;
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r168);
    goto CPyL38;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[38];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\302\0260x608060405260405180604001604052806040518060600160405280602c815260200161105e602c913981526020016040518060400160405280601781526020017f68747470733a2f2f776562332e70792f676174657761790000000000000000008152508152505f906002610075929190610087565b50348015610081575f5ffd5b50610465565b828054828255905f5260205f209081019282156100cd579160200282015b828111156100cc5782518290816100bc9190610396565b50916020019190600101906100a5565b5b5090506100da91906100de565b5090565b5b808211156100fd575f81816100f49190610101565b506001016100df565b5090565b50805461010d906101bd565b5f825580601f1061011e575061013b565b601f0160209004905f5260205f209081019061013a919061013e565b5b50565b5b80821115610155575f815f90555060010161013f565b5090565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806101d457607f821691505b6020821081036101e7576101e6610190565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f600883026102497fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261020e565b610253868361020e565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61029761029261028d8461026b565b610274565b61026b565b9050919050565b5f819050919050565b6102b08361027d565b6102c46102bc8261029e565b84845461021a565b825550505050565b5f5f905090565b6102db6102cc565b6102e68184846102a7565b505050565b5b81811015610309576102fe5f826102d3565b6001810190506102ec565b5050565b601f82111561034e5761031f816101ed565b610328846101ff565b81016020851015610337578190505b61034b610343856101ff565b8301826102eb565b50505b505050565b5f82821c905092915050565b5f61036e5f1984600802610353565b1980831691505092915050565b5f610386838361035f565b9150826002028217905092915050565b61039f82610159565b67ffffffffffffffff8111156103b8576103b7610163565b5b6103c282546101bd565b6103cd82828561030d565b5f60209050601f8311600181146103fe575f84156103ec578287015190505b6103f6858261037b565b86555061045d565b601f19841661040c866101ed565b5f5b828110156104335784890151825560018201915060208501945060208101905061040e565b86831015610450578489015161044c601f89168261035f565b8355505b6001600288020188555050505b505050505050565b610bec806104725f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c806309a3c01b146100435780636337ed5814610061578063da96d05a14610091575b5f5ffd5b61004b6100c1565b60405161005891906103f2565b60405180910390f35b61007b60048036038101906100769190610484565b610110565b60405161008891906103f2565b60405180910390f35b6100ab60048036038101906100a691906104cf565b6101fc565b6040516100b891906103f2565b60405180910390f35b606080305f826309a3c01b60e01b846040517f556f1830000000000000000000000000000000000000000000000000000000008152600401610107959493929190610783565b60405180910390fd5b60605f83838101906101229190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af07581604051602001610156919061099c565b60405160208183030381529060405280519060200120146101ac576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101a390610a0c565b60405180910390fd5b305f858563da96d05a60e01b88886040517f556f18300000000000000000000000000000000000000000000000000000000081526004016101f39796959493929190610a56565b60405180910390fd5b60605f858581019061020e9190610911565b90507faed76f463930323372899e36460e078e5292aac45f645bbe567be6fca83ede1081604051602001610242919061099c565b6040516020818303038152906040528051906020012014610298576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028f90610b30565b60405180910390fd5b5f84848101906102a89190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af075816040516020016102dc919061099c565b6040516020818303038152906040528051906020012014610332576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032990610b98565b60405180910390fd5b86868080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505092505050949350505050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6103c482610382565b6103ce818561038c565b93506103de81856020860161039c565b6103e7816103aa565b840191505092915050565b5f6020820190508181035f83015261040a81846103ba565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f84011261044457610443610423565b5b8235905067ffffffffffffffff81111561046157610460610427565b5b60208301915083600182028301111561047d5761047c61042b565b5b9250929050565b5f5f6020838503121561049a5761049961041b565b5b5f83013567ffffffffffffffff8111156104b7576104b661041f565b5b6104c38582860161042f565b92509250509250929050565b5f5f5f5f604085870312156104e7576104e661041b565b5b5f85013567ffffffffffffffff8111156105045761050361041f565b5b6105108782880161042f565b9450945050602085013567ffffffffffffffff8111156105335761053261041f565b5b61053f8782880161042f565b925092505092959194509250565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105768261054d565b9050919050565b6105868161056c565b82525050565b5f81549050919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806105fc57607f821691505b60208210810361060f5761060e6105b8565b5b50919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b5f8154610643816105e5565b61064d8186610615565b9450600182165f8114610667576001811461067d576106af565b60ff1983168652811515602002860193506106af565b61068685610625565b5f5b838110156106a757815481890152600182019150602081019050610688565b808801955050505b50505092915050565b5f6106c38383610637565b905092915050565b5f600182019050919050565b5f6106e18261058c565b6106eb8185610596565b9350836020820285016106fd856105a6565b805f5b858110156107375784840389528161071885826106b8565b9450610723836106cb565b925060208a01995050600181019050610700565b50829750879550505050505092915050565b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61077d81610749565b82525050565b5f60a0820190506107965f83018861057d565b81810360208301526107a881876106d7565b905081810360408301526107bc81866103ba565b90506107cb6060830185610774565b81810360808301526107dd81846103ba565b90509695505050505050565b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610823826103aa565b810181811067ffffffffffffffff82111715610842576108416107ed565b5b80604052505050565b5f610854610412565b9050610860828261081a565b919050565b5f67ffffffffffffffff82111561087f5761087e6107ed565b5b610888826103aa565b9050602081019050919050565b828183375f83830152505050565b5f6108b56108b084610865565b61084b565b9050828152602081018484840111156108d1576108d06107e9565b5b6108dc848285610895565b509392505050565b5f82601f8301126108f8576108f7610423565b5b81356109088482602086016108a3565b91505092915050565b5f602082840312156109265761092561041b565b5b5f82013567ffffffffffffffff8111156109435761094261041f565b5b61094f848285016108e4565b91505092915050565b5f81519050919050565b5f81905092915050565b5f61097682610958565b6109808185610962565b935061099081856020860161039c565b80840191505092915050565b5f6109a7828461096c565b915081905092915050565b5f82825260208201905092915050565b7f7465737420646174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f6109f6601c836109b2565b9150610a01826109c2565b602082019050919050565b5f6020820190508181035f830152610a23816109ea565b9050919050565b5f610a35838561038c565b9350610a42838584610895565b610a4b836103aa565b840190509392505050565b5f60a082019050610a695f83018a61057d565b8181036020830152610a7b81896106d7565b90508181036040830152610a90818789610a2a565b9050610a9f6060830186610774565b8181036080830152610ab2818486610a2a565b905098975050505050505050565b7f68747470207265717565737420726573756c742076616c69646174696f6e20665f8201527f61696c65642e0000000000000000000000000000000000000000000000000000602082015250565b5f610b1a6026836109b2565b9150610b2582610ac0565b604082019050919050565b5f6020820190508181035f830152610b4781610b0e565b9050919050565b7f6578747261446174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f610b82601c836109b2565b9150610b8d82610b4e565b602082019050919050565b5f6020820190508181035f830152610baf81610b76565b905091905056fea2646970667358221220029be82598e02eb26c8cc4f7656db4919c9c779bb468c366f11ca5263eef888064736f6c634300081e003368747470733a2f2f776562332e70792f676174657761792f7b73656e6465727d2f7b646174617d2e6a736f6e",
    "\001\030OFFCHAIN_LOOKUP_BYTECODE",
    "\001\257Z0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c806309a3c01b146100435780636337ed5814610061578063da96d05a14610091575b5f5ffd5b61004b6100c1565b60405161005891906103f2565b60405180910390f35b61007b60048036038101906100769190610484565b610110565b60405161008891906103f2565b60405180910390f35b6100ab60048036038101906100a691906104cf565b6101fc565b6040516100b891906103f2565b60405180910390f35b606080305f826309a3c01b60e01b846040517f556f1830000000000000000000000000000000000000000000000000000000008152600401610107959493929190610783565b60405180910390fd5b60605f83838101906101229190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af07581604051602001610156919061099c565b60405160208183030381529060405280519060200120146101ac576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016101a390610a0c565b60405180910390fd5b305f858563da96d05a60e01b88886040517f556f18300000000000000000000000000000000000000000000000000000000081526004016101f39796959493929190610a56565b60405180910390fd5b60605f858581019061020e9190610911565b90507faed76f463930323372899e36460e078e5292aac45f645bbe567be6fca83ede1081604051602001610242919061099c565b6040516020818303038152906040528051906020012014610298576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161028f90610b30565b60405180910390fd5b5f84848101906102a89190610911565b90507fd9bdd1345ca2a00d0c1413137c1b2b1d0a35e5b0e11508f3b3eff856286af075816040516020016102dc919061099c565b6040516020818303038152906040528051906020012014610332576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161032990610b98565b60405180910390fd5b86868080601f0160208091040260200160405190810160405280939291908181526020018383808284375f81840152601f19601f8201169050808301925050505050505092505050949350505050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f6103c482610382565b6103ce818561038c565b93506103de81856020860161039c565b6103e7816103aa565b840191505092915050565b5f6020820190508181035f83015261040a81846103ba565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f5f83601f84011261044457610443610423565b5b8235905067ffffffffffffffff81111561046157610460610427565b5b60208301915083600182028301111561047d5761047c61042b565b5b9250929050565b5f5f6020838503121561049a5761049961041b565b5b5f83013567ffffffffffffffff8111156104b7576104b661041f565b5b6104c38582860161042f565b92509250509250929050565b5f5f5f5f604085870312156104e7576104e661041b565b5b5f85013567ffffffffffffffff8111156105045761050361041f565b5b6105108782880161042f565b9450945050602085013567ffffffffffffffff8111156105335761053261041f565b5b61053f8782880161042f565b925092505092959194509250565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6105768261054d565b9050919050565b6105868161056c565b82525050565b5f81549050919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806105fc57607f821691505b60208210810361060f5761060e6105b8565b5b50919050565b5f82825260208201905092915050565b5f819050815f5260205f209050919050565b5f8154610643816105e5565b61064d8186610615565b9450600182165f8114610667576001811461067d576106af565b60ff1983168652811515602002860193506106af565b61068685610625565b5f5b838110156106a757815481890152600182019150602081019050610688565b808801955050505b50505092915050565b5f6106c38383610637565b905092915050565b5f600182019050919050565b5f6106e18261058c565b6106eb8185610596565b9350836020820285016106fd856105a6565b805f5b858110156107375784840389528161071885826106b8565b9450610723836106cb565b925060208a01995050600181019050610700565b50829750879550505050505092915050565b5f7fffffffff0000000000000000000000000000000000000000000000000000000082169050919050565b61077d81610749565b82525050565b5f60a0820190506107965f83018861057d565b81810360208301526107a881876106d7565b905081810360408301526107bc81866103ba565b90506107cb6060830185610774565b81810360808301526107dd81846103ba565b90509695505050505050565b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610823826103aa565b810181811067ffffffffffffffff82111715610842576108416107ed565b5b80604052505050565b5f610854610412565b9050610860828261081a565b919050565b5f67ffffffffffffffff82111561087f5761087e6107ed565b5b610888826103aa565b9050602081019050919050565b828183375f83830152505050565b5f6108b56108b084610865565b61084b565b9050828152602081018484840111156108d1576108d06107e9565b5b6108dc848285610895565b509392505050565b5f82601f8301126108f8576108f7610423565b5b81356109088482602086016108a3565b91505092915050565b5f602082840312156109265761092561041b565b5b5f82013567ffffffffffffffff8111156109435761094261041f565b5b61094f848285016108e4565b91505092915050565b5f81519050919050565b5f81905092915050565b5f61097682610958565b6109808185610962565b935061099081856020860161039c565b80840191505092915050565b5f6109a7828461096c565b915081905092915050565b5f82825260208201905092915050565b7f7465737420646174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f6109f6601c836109b2565b9150610a01826109c2565b602082019050919050565b5f6020820190508181035f830152610a23816109ea565b9050919050565b5f610a35838561038c565b9350610a42838584610895565b610a4b836103aa565b840190509392505050565b5f60a082019050610a695f83018a61057d565b8181036020830152610a7b81896106d7565b90508181036040830152610a90818789610a2a565b9050610a9f6060830186610774565b8181036080830152610ab2818486610a2a565b905098975050505050505050565b7f68747470207265717565737420726573756c742076616c69646174696f6e20665f8201527f61696c65642e0000000000000000000000000000000000000000000000000000602082015250565b5f610b1a6026836109b2565b9150610b2582610ac0565b604082019050919050565b5f6020820190508181035f830152610b4781610b0e565b9050919050565b7f6578747261446174612076616c69646174696f6e206661696c65642e000000005f82015250565b5f610b82601c836109b2565b9150610b8d82610b4e565b602082019050919050565b5f6020820190508181035f830152610baf81610b76565b905091905056fea2646970667358221220029be82598e02eb26c8cc4f7656db4919c9c779bb468c366f11ca5263eef888064736f6c634300081e0033",
    "\a\027OFFCHAIN_LOOKUP_RUNTIME\006inputs\finternalType\aaddress\004name\006sender\004type",
    "\a\bstring[]\004urls\005bytes\bcallData\006bytes4\020callbackFunction\textraData",
    "\005\016OffchainLookup\005error\030continuousOffchainLookup\aoutputs\000",
    "\004\017stateMutability\nnonpayable\bfunction\025specifiedDataFromTest",
    "\003\022testOffchainLookup\006result\033testOffchainLookupWithProof",
    "\004\023OFFCHAIN_LOOKUP_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\024OFFCHAIN_LOOKUP_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___offchain_lookup;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_offchain_lookup__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___offchain_lookup(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___offchain_lookup, "faster_web3._utils.contract_sources.contract_data.offchain_lookup__mypyc.init_faster_web3____utils___contract_sources___contract_data___offchain_lookup", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___offchain_lookup", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_offchain_lookup__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.offchain_lookup__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_offchain_lookup__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_offchain_lookup__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_offchain_lookup__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
