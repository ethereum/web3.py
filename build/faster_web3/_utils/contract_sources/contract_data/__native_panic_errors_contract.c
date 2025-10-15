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
#include "__native_panic_errors_contract.h"
#include "__native_internal_panic_errors_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___panic_errors_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.panic_errors_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___panic_errors_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___panic_errors_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal;
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
    PyObject *cpy_r_r73;
    PyObject *cpy_r_r74;
    CPyPtr cpy_r_r75;
    CPyPtr cpy_r_r76;
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
    CPyPtr cpy_r_r95;
    CPyPtr cpy_r_r96;
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
    CPyPtr cpy_r_r174;
    CPyPtr cpy_r_r175;
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
    PyObject *cpy_r_r193;
    CPyPtr cpy_r_r194;
    CPyPtr cpy_r_r195;
    PyObject *cpy_r_r196;
    PyObject *cpy_r_r197;
    PyObject *cpy_r_r198;
    PyObject *cpy_r_r199;
    PyObject *cpy_r_r200;
    PyObject *cpy_r_r201;
    PyObject *cpy_r_r202;
    PyObject *cpy_r_r203;
    int32_t cpy_r_r204;
    char cpy_r_r205;
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
    PyObject *cpy_r_r221;
    PyObject *cpy_r_r222;
    PyObject *cpy_r_r223;
    int32_t cpy_r_r224;
    char cpy_r_r225;
    char cpy_r_r226;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL58;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x60806040525f67ffffffffffffffff81111561001e5761001d61018f565b5b60405190808252806020026020018201604052801561005157816020015b606081526020019060019003908161003c5790505b505f90805190602001906100669291906100bd565b506040518060400160405280600381526020017f6162630000000000000000000000000000000000000000000000000000000000815250600190816100ab91906103cc565b503480156100b7575f5ffd5b50610574565b828054828255905f5260205f20908101928215610103579160200282015b828111156101025782518290816100f291906104a5565b50916020019190600101906100db565b5b5090506101109190610114565b5090565b5b80821115610133575f818161012a9190610137565b50600101610115565b5090565b508054610143906101f3565b5f825580601f106101545750610171565b601f0160209004905f5260205f20908101906101709190610174565b5b50565b5b8082111561018b575f815f905550600101610175565b5090565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061020a57607f821691505b60208210810361021d5761021c6101c6565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261027f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610244565b6102898683610244565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6102cd6102c86102c3846102a1565b6102aa565b6102a1565b9050919050565b5f819050919050565b6102e6836102b3565b6102fa6102f2826102d4565b848454610250565b825550505050565b5f5f905090565b610311610302565b61031c8184846102dd565b505050565b5b8181101561033f576103345f82610309565b600181019050610322565b5050565b601f8211156103845761035581610223565b61035e84610235565b8101602085101561036d578190505b61038161037985610235565b830182610321565b50505b505050565b5f82821c905092915050565b5f6103a45f1984600802610389565b1980831691505092915050565b5f6103bc8383610395565b9150826002028217905092915050565b6103d5826101bc565b67ffffffffffffffff8111156103ee576103ed61018f565b5b6103f882546101f3565b610403828285610343565b5f60209050601f831160018114610434575f8415610422578287015190505b61042c85826103b1565b865550610493565b601f19841661044286610223565b5f5b8281101561046957848901518255600182019150602085019450602081019050610444565b868310156104865784890151610482601f891682610395565b8355505b6001600288020188555050505b505050505050565b5f81519050919050565b6104ae8261049b565b67ffffffffffffffff8111156104c7576104c661018f565b5b6104d182546101f3565b6104dc828285610343565b5f60209050601f83116001811461050d575f84156104fb578287015190505b61050585826103b1565b86555061056c565b601f19841661051b86610223565b5f5b828110156105425784890151825560018201915060208501945060208101905061051d565b8683101561055f578489015161055b601f891682610395565b8355505b6001600288020188555050505b505050505050565b610990806105815f395ff3fe608060405234801561000f575f5ffd5b50600436106100b2575f3560e01c80638e5ab2d21161006f5780638e5ab2d214610118578063946c05b214610122578063a56dfe4a1461012c578063b6a3bfb11461014a578063c2eb2ebb14610166578063fc430d5c14610170576100b2565b80630c55699c146100b65780633124bba4146100d45780633b447353146100de578063554c0809146100e85780636407fe2c146100f25780636fff525e146100fc575b5f5ffd5b6100be6101a0565b6040516100cb919061065e565b60405180910390f35b6100dc61022c565b005b6100e661024b565b005b6100f06102bf565b005b6100fa6102d4565b005b610116600480360381019061011191906106b5565b6102e4565b005b6101206102fd565b005b61012a61032b565b005b610134610355565b604051610141919061065e565b60405180910390f35b610164600480360381019061015f9190610713565b6103e1565b005b61016e6103f5565b005b61018a60048036038101906101859190610713565b6104e7565b604051610197919061065e565b60405180910390f35b600180546101ad9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546101d99061076b565b80156102245780601f106101fb57610100808354040283529160200191610224565b820191905f5260205f20905b81548152906001019060200180831161020757829003601f168201915b505050505081565b5f6001815481106102405761023f61079b565b5b905f5260205f205050565b5f7f080000000000000000000000000000000000000000000000000000000000000090505f8167ffffffffffffffff81111561028a576102896107c8565b5b6040519080825280602002602001820160405280156102b85781602001602082028036833780820191505090505b5090505050565b5f5f905080806102ce90610822565b91505050565b5f6102e2576102e1610849565b5b565b5f815f8111156102f7576102f6610876565b5b90505050565b5f80548061030e5761030d6108a3565b5b600190038181905f5260205f20015f610327919061058c565b9055565b61035360035f9054906101000a900480156105c9021767ffffffffffffffff1663ffffffff16565b565b600280546103629061076b565b80601f016020809104026020016040519081016040528092919081815260200182805461038e9061076b565b80156103d95780601f106103b0576101008083540402835291602001916103d9565b820191905f5260205f20905b8154815290600101906020018083116103bc57829003601f168201915b505050505081565b5f8160056103ef91906108fd565b90505050565b604060015560025f610407919061058c565b60018054806104159061076b565b80610447577f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b601f81115f811461045f5760018114610481576104de565b6001826021036101000a036001830392506002830284821916179350506104de565b835f5260205f2082602081146104c757601f6001850316602060018603048301925082546001826020036101000a038181191691508185556002880397505050506104db565b81545f835560ff1981169050603e81179550505b50505b50818355505050565b5f81815481106104f5575f80fd5b905f5260205f20015f91509050805461050d9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546105399061076b565b80156105845780601f1061055b57610100808354040283529160200191610584565b820191905f5260205f20905b81548152906001019060200180831161056757829003601f168201915b505050505081565b5080546105989061076b565b5f825580601f106105a957506105c6565b601f0160209004905f5260205f20908101906105c591906105d3565b5b50565b6105d161092d565b565b5b808211156105ea575f815f9055506001016105d4565b5090565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f610630826105ee565b61063a81856105f8565b935061064a818560208601610608565b61065381610616565b840191505092915050565b5f6020820190508181035f8301526106768184610626565b905092915050565b5f5ffd5b5f819050919050565b61069481610682565b811461069e575f5ffd5b50565b5f813590506106af8161068b565b92915050565b5f602082840312156106ca576106c961067e565b5b5f6106d7848285016106a1565b91505092915050565b5f819050919050565b6106f2816106e0565b81146106fc575f5ffd5b50565b5f8135905061070d816106e9565b92915050565b5f602082840312156107285761072761067e565b5b5f610735848285016106ff565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061078257607f821691505b6020821081036107955761079461073e565b5b50919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61082c826106e0565b91505f820361083e5761083d6107f5565b5b600182039050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52600160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f610907826106e0565b9150610912836106e0565b925082610922576109216108d0565b5b828204905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52605160045260245ffdfea26469706673582212204171ea044bdab54fb9f772923ea05ce4bed278fbc8ad7dcae1c768f2ab5fbb6f64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'PANIC_ERRORS_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b50600436106100b2575f3560e01c80638e5ab2d21161006f5780638e5ab2d214610118578063946c05b214610122578063a56dfe4a1461012c578063b6a3bfb11461014a578063c2eb2ebb14610166578063fc430d5c14610170576100b2565b80630c55699c146100b65780633124bba4146100d45780633b447353146100de578063554c0809146100e85780636407fe2c146100f25780636fff525e146100fc575b5f5ffd5b6100be6101a0565b6040516100cb919061065e565b60405180910390f35b6100dc61022c565b005b6100e661024b565b005b6100f06102bf565b005b6100fa6102d4565b005b610116600480360381019061011191906106b5565b6102e4565b005b6101206102fd565b005b61012a61032b565b005b610134610355565b604051610141919061065e565b60405180910390f35b610164600480360381019061015f9190610713565b6103e1565b005b61016e6103f5565b005b61018a60048036038101906101859190610713565b6104e7565b604051610197919061065e565b60405180910390f35b600180546101ad9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546101d99061076b565b80156102245780601f106101fb57610100808354040283529160200191610224565b820191905f5260205f20905b81548152906001019060200180831161020757829003601f168201915b505050505081565b5f6001815481106102405761023f61079b565b5b905f5260205f205050565b5f7f080000000000000000000000000000000000000000000000000000000000000090505f8167ffffffffffffffff81111561028a576102896107c8565b5b6040519080825280602002602001820160405280156102b85781602001602082028036833780820191505090505b5090505050565b5f5f905080806102ce90610822565b91505050565b5f6102e2576102e1610849565b5b565b5f815f8111156102f7576102f6610876565b5b90505050565b5f80548061030e5761030d6108a3565b5b600190038181905f5260205f20015f610327919061058c565b9055565b61035360035f9054906101000a900480156105c9021767ffffffffffffffff1663ffffffff16565b565b600280546103629061076b565b80601f016020809104026020016040519081016040528092919081815260200182805461038e9061076b565b80156103d95780601f106103b0576101008083540402835291602001916103d9565b820191905f5260205f20905b8154815290600101906020018083116103bc57829003601f168201915b505050505081565b5f8160056103ef91906108fd565b90505050565b604060015560025f610407919061058c565b60018054806104159061076b565b80610447577f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b601f81115f811461045f5760018114610481576104de565b6001826021036101000a036001830392506002830284821916179350506104de565b835f5260205f2082602081146104c757601f6001850316602060018603048301925082546001826020036101000a038181191691508185556002880397505050506104db565b81545f835560ff1981169050603e81179550505b50505b50818355505050565b5f81815481106104f5575f80fd5b905f5260205f20015f91509050805461050d9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546105399061076b565b80156105845780601f1061055b57610100808354040283529160200191610584565b820191905f5260205f20905b81548152906001019060200180831161056757829003601f168201915b505050505081565b5080546105989061076b565b5f825580601f106105a957506105c6565b601f0160209004905f5260205f20908101906105c591906105d3565b5b50565b6105d161092d565b565b5b808211156105ea575f815f9055506001016105d4565b5090565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f610630826105ee565b61063a81856105f8565b935061064a818560208601610608565b61065381610616565b840191505092915050565b5f6020820190508181035f8301526106768184610626565b905092915050565b5f5ffd5b5f819050919050565b61069481610682565b811461069e575f5ffd5b50565b5f813590506106af8161068b565b92915050565b5f602082840312156106ca576106c961067e565b5b5f6106d7848285016106a1565b91505092915050565b5f819050919050565b6106f2816106e0565b81146106fc575f5ffd5b50565b5f8135905061070d816106e9565b92915050565b5f602082840312156107285761072761067e565b5b5f610735848285016106ff565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061078257607f821691505b6020821081036107955761079461073e565b5b50919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61082c826106e0565b91505f820361083e5761083d6107f5565b5b600182039050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52600160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f610907826106e0565b9150610912836106e0565b925082610922576109216108d0565b5b828204905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52605160045260245ffdfea26469706673582212204171ea044bdab54fb9f772923ea05ce4bed278fbc8ad7dcae1c768f2ab5fbb6f64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'PANIC_ERRORS_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'uint256' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* '' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'uint256' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL59;
    }
    cpy_r_r24 = (CPyPtr)&((PyListObject *)cpy_r_r23)->ob_item;
    cpy_r_r25 = *(CPyPtr *)cpy_r_r24;
    *(PyObject * *)cpy_r_r25 = cpy_r_r22;
    cpy_r_r26 = CPyStatics[11]; /* 'name' */
    cpy_r_r27 = CPyStatics[14]; /* 'emptyArray' */
    cpy_r_r28 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r29 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r30 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r31 = CPyStatics[11]; /* 'name' */
    cpy_r_r32 = CPyStatics[12]; /* '' */
    cpy_r_r33 = CPyStatics[13]; /* 'type' */
    cpy_r_r34 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r35 = CPyDict_Build(3, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r36 = PyList_New(1);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r37 = (CPyPtr)&((PyListObject *)cpy_r_r36)->ob_item;
    cpy_r_r38 = *(CPyPtr *)cpy_r_r37;
    *(PyObject * *)cpy_r_r38 = cpy_r_r35;
    cpy_r_r39 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r40 = CPyStatics[18]; /* 'view' */
    cpy_r_r41 = CPyStatics[13]; /* 'type' */
    cpy_r_r42 = CPyStatics[19]; /* 'function' */
    cpy_r_r43 = CPyDict_Build(5, cpy_r_r15, cpy_r_r23, cpy_r_r26, cpy_r_r27, cpy_r_r28, cpy_r_r36, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    CPy_DECREF_NO_IMM(cpy_r_r23);
    CPy_DECREF_NO_IMM(cpy_r_r36);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r44 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r45 = PyList_New(0);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 18, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r46 = CPyStatics[11]; /* 'name' */
    cpy_r_r47 = CPyStatics[20]; /* 'errorCode01' */
    cpy_r_r48 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r49 = PyList_New(0);
    if (unlikely(cpy_r_r49 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r50 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r51 = CPyStatics[21]; /* 'pure' */
    cpy_r_r52 = CPyStatics[13]; /* 'type' */
    cpy_r_r53 = CPyStatics[19]; /* 'function' */
    cpy_r_r54 = CPyDict_Build(5, cpy_r_r44, cpy_r_r45, cpy_r_r46, cpy_r_r47, cpy_r_r48, cpy_r_r49, cpy_r_r50, cpy_r_r51, cpy_r_r52, cpy_r_r53);
    CPy_DECREF_NO_IMM(cpy_r_r45);
    CPy_DECREF_NO_IMM(cpy_r_r49);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 17, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r55 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r56 = PyList_New(0);
    if (unlikely(cpy_r_r56 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r57 = CPyStatics[11]; /* 'name' */
    cpy_r_r58 = CPyStatics[22]; /* 'errorCode11' */
    cpy_r_r59 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r60 = PyList_New(0);
    if (unlikely(cpy_r_r60 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 27, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r61 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r62 = CPyStatics[21]; /* 'pure' */
    cpy_r_r63 = CPyStatics[13]; /* 'type' */
    cpy_r_r64 = CPyStatics[19]; /* 'function' */
    cpy_r_r65 = CPyDict_Build(5, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64);
    CPy_DECREF_NO_IMM(cpy_r_r56);
    CPy_DECREF_NO_IMM(cpy_r_r60);
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 24, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r66 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r67 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r68 = CPyStatics[10]; /* 'uint256' */
    cpy_r_r69 = CPyStatics[11]; /* 'name' */
    cpy_r_r70 = CPyStatics[23]; /* 'zero' */
    cpy_r_r71 = CPyStatics[13]; /* 'type' */
    cpy_r_r72 = CPyStatics[10]; /* 'uint256' */
    cpy_r_r73 = CPyDict_Build(3, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 32, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r74 = PyList_New(1);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 32, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r75 = (CPyPtr)&((PyListObject *)cpy_r_r74)->ob_item;
    cpy_r_r76 = *(CPyPtr *)cpy_r_r75;
    *(PyObject * *)cpy_r_r76 = cpy_r_r73;
    cpy_r_r77 = CPyStatics[11]; /* 'name' */
    cpy_r_r78 = CPyStatics[24]; /* 'errorCode12' */
    cpy_r_r79 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r80 = PyList_New(0);
    if (unlikely(cpy_r_r80 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 34, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r81 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r82 = CPyStatics[21]; /* 'pure' */
    cpy_r_r83 = CPyStatics[13]; /* 'type' */
    cpy_r_r84 = CPyStatics[19]; /* 'function' */
    cpy_r_r85 = CPyDict_Build(5, cpy_r_r66, cpy_r_r74, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81, cpy_r_r82, cpy_r_r83, cpy_r_r84);
    CPy_DECREF_NO_IMM(cpy_r_r74);
    CPy_DECREF_NO_IMM(cpy_r_r80);
    if (unlikely(cpy_r_r85 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 31, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r86 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r87 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r88 = CPyStatics[25]; /* 'int256' */
    cpy_r_r89 = CPyStatics[11]; /* 'name' */
    cpy_r_r90 = CPyStatics[26]; /* 'negativeInt' */
    cpy_r_r91 = CPyStatics[13]; /* 'type' */
    cpy_r_r92 = CPyStatics[25]; /* 'int256' */
    cpy_r_r93 = CPyDict_Build(3, cpy_r_r87, cpy_r_r88, cpy_r_r89, cpy_r_r90, cpy_r_r91, cpy_r_r92);
    if (unlikely(cpy_r_r93 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r94 = PyList_New(1);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r95 = (CPyPtr)&((PyListObject *)cpy_r_r94)->ob_item;
    cpy_r_r96 = *(CPyPtr *)cpy_r_r95;
    *(PyObject * *)cpy_r_r96 = cpy_r_r93;
    cpy_r_r97 = CPyStatics[11]; /* 'name' */
    cpy_r_r98 = CPyStatics[27]; /* 'errorCode21' */
    cpy_r_r99 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r100 = PyList_New(0);
    if (unlikely(cpy_r_r100 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL71;
    }
    cpy_r_r101 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r102 = CPyStatics[21]; /* 'pure' */
    cpy_r_r103 = CPyStatics[13]; /* 'type' */
    cpy_r_r104 = CPyStatics[19]; /* 'function' */
    cpy_r_r105 = CPyDict_Build(5, cpy_r_r86, cpy_r_r94, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101, cpy_r_r102, cpy_r_r103, cpy_r_r104);
    CPy_DECREF_NO_IMM(cpy_r_r94);
    CPy_DECREF_NO_IMM(cpy_r_r100);
    if (unlikely(cpy_r_r105 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r106 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r107 = PyList_New(0);
    if (unlikely(cpy_r_r107 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 46, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r108 = CPyStatics[11]; /* 'name' */
    cpy_r_r109 = CPyStatics[28]; /* 'errorCode22' */
    cpy_r_r110 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r111 = PyList_New(0);
    if (unlikely(cpy_r_r111 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r112 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r113 = CPyStatics[29]; /* 'nonpayable' */
    cpy_r_r114 = CPyStatics[13]; /* 'type' */
    cpy_r_r115 = CPyStatics[19]; /* 'function' */
    cpy_r_r116 = CPyDict_Build(5, cpy_r_r106, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110, cpy_r_r111, cpy_r_r112, cpy_r_r113, cpy_r_r114, cpy_r_r115);
    CPy_DECREF_NO_IMM(cpy_r_r107);
    CPy_DECREF_NO_IMM(cpy_r_r111);
    if (unlikely(cpy_r_r116 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 45, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r117 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r118 = PyList_New(0);
    if (unlikely(cpy_r_r118 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 53, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r119 = CPyStatics[11]; /* 'name' */
    cpy_r_r120 = CPyStatics[30]; /* 'errorCode31' */
    cpy_r_r121 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r122 = PyList_New(0);
    if (unlikely(cpy_r_r122 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 55, CPyStatic_globals);
        goto CPyL75;
    }
    cpy_r_r123 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r124 = CPyStatics[29]; /* 'nonpayable' */
    cpy_r_r125 = CPyStatics[13]; /* 'type' */
    cpy_r_r126 = CPyStatics[19]; /* 'function' */
    cpy_r_r127 = CPyDict_Build(5, cpy_r_r117, cpy_r_r118, cpy_r_r119, cpy_r_r120, cpy_r_r121, cpy_r_r122, cpy_r_r123, cpy_r_r124, cpy_r_r125, cpy_r_r126);
    CPy_DECREF_NO_IMM(cpy_r_r118);
    CPy_DECREF_NO_IMM(cpy_r_r122);
    if (unlikely(cpy_r_r127 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 52, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r128 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r129 = PyList_New(0);
    if (unlikely(cpy_r_r129 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 60, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r130 = CPyStatics[11]; /* 'name' */
    cpy_r_r131 = CPyStatics[31]; /* 'errorCode32' */
    cpy_r_r132 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r133 = PyList_New(0);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 62, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r134 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r135 = CPyStatics[29]; /* 'nonpayable' */
    cpy_r_r136 = CPyStatics[13]; /* 'type' */
    cpy_r_r137 = CPyStatics[19]; /* 'function' */
    cpy_r_r138 = CPyDict_Build(5, cpy_r_r128, cpy_r_r129, cpy_r_r130, cpy_r_r131, cpy_r_r132, cpy_r_r133, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137);
    CPy_DECREF_NO_IMM(cpy_r_r129);
    CPy_DECREF_NO_IMM(cpy_r_r133);
    if (unlikely(cpy_r_r138 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 59, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r139 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r140 = PyList_New(0);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 67, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r141 = CPyStatics[11]; /* 'name' */
    cpy_r_r142 = CPyStatics[32]; /* 'errorCode41' */
    cpy_r_r143 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r144 = PyList_New(0);
    if (unlikely(cpy_r_r144 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 69, CPyStatic_globals);
        goto CPyL79;
    }
    cpy_r_r145 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r146 = CPyStatics[21]; /* 'pure' */
    cpy_r_r147 = CPyStatics[13]; /* 'type' */
    cpy_r_r148 = CPyStatics[19]; /* 'function' */
    cpy_r_r149 = CPyDict_Build(5, cpy_r_r139, cpy_r_r140, cpy_r_r141, cpy_r_r142, cpy_r_r143, cpy_r_r144, cpy_r_r145, cpy_r_r146, cpy_r_r147, cpy_r_r148);
    CPy_DECREF_NO_IMM(cpy_r_r140);
    CPy_DECREF_NO_IMM(cpy_r_r144);
    if (unlikely(cpy_r_r149 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 66, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r150 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r151 = PyList_New(0);
    if (unlikely(cpy_r_r151 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 74, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r152 = CPyStatics[11]; /* 'name' */
    cpy_r_r153 = CPyStatics[33]; /* 'errorCode51' */
    cpy_r_r154 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r155 = PyList_New(0);
    if (unlikely(cpy_r_r155 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 76, CPyStatic_globals);
        goto CPyL81;
    }
    cpy_r_r156 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r157 = CPyStatics[29]; /* 'nonpayable' */
    cpy_r_r158 = CPyStatics[13]; /* 'type' */
    cpy_r_r159 = CPyStatics[19]; /* 'function' */
    cpy_r_r160 = CPyDict_Build(5, cpy_r_r150, cpy_r_r151, cpy_r_r152, cpy_r_r153, cpy_r_r154, cpy_r_r155, cpy_r_r156, cpy_r_r157, cpy_r_r158, cpy_r_r159);
    CPy_DECREF_NO_IMM(cpy_r_r151);
    CPy_DECREF_NO_IMM(cpy_r_r155);
    if (unlikely(cpy_r_r160 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 73, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r161 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r162 = PyList_New(0);
    if (unlikely(cpy_r_r162 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 81, CPyStatic_globals);
        goto CPyL82;
    }
    cpy_r_r163 = CPyStatics[11]; /* 'name' */
    cpy_r_r164 = CPyStatics[34]; /* 'x' */
    cpy_r_r165 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r166 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r167 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r168 = CPyStatics[11]; /* 'name' */
    cpy_r_r169 = CPyStatics[12]; /* '' */
    cpy_r_r170 = CPyStatics[13]; /* 'type' */
    cpy_r_r171 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r172 = CPyDict_Build(3, cpy_r_r166, cpy_r_r167, cpy_r_r168, cpy_r_r169, cpy_r_r170, cpy_r_r171);
    if (unlikely(cpy_r_r172 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 83, CPyStatic_globals);
        goto CPyL83;
    }
    cpy_r_r173 = PyList_New(1);
    if (unlikely(cpy_r_r173 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 83, CPyStatic_globals);
        goto CPyL84;
    }
    cpy_r_r174 = (CPyPtr)&((PyListObject *)cpy_r_r173)->ob_item;
    cpy_r_r175 = *(CPyPtr *)cpy_r_r174;
    *(PyObject * *)cpy_r_r175 = cpy_r_r172;
    cpy_r_r176 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r177 = CPyStatics[18]; /* 'view' */
    cpy_r_r178 = CPyStatics[13]; /* 'type' */
    cpy_r_r179 = CPyStatics[19]; /* 'function' */
    cpy_r_r180 = CPyDict_Build(5, cpy_r_r161, cpy_r_r162, cpy_r_r163, cpy_r_r164, cpy_r_r165, cpy_r_r173, cpy_r_r176, cpy_r_r177, cpy_r_r178, cpy_r_r179);
    CPy_DECREF_NO_IMM(cpy_r_r162);
    CPy_DECREF_NO_IMM(cpy_r_r173);
    if (unlikely(cpy_r_r180 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 80, CPyStatic_globals);
        goto CPyL82;
    }
    cpy_r_r181 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r182 = PyList_New(0);
    if (unlikely(cpy_r_r182 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 88, CPyStatic_globals);
        goto CPyL85;
    }
    cpy_r_r183 = CPyStatics[11]; /* 'name' */
    cpy_r_r184 = CPyStatics[35]; /* 'y' */
    cpy_r_r185 = CPyStatics[15]; /* 'outputs' */
    cpy_r_r186 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r187 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r188 = CPyStatics[11]; /* 'name' */
    cpy_r_r189 = CPyStatics[12]; /* '' */
    cpy_r_r190 = CPyStatics[13]; /* 'type' */
    cpy_r_r191 = CPyStatics[16]; /* 'bytes' */
    cpy_r_r192 = CPyDict_Build(3, cpy_r_r186, cpy_r_r187, cpy_r_r188, cpy_r_r189, cpy_r_r190, cpy_r_r191);
    if (unlikely(cpy_r_r192 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 90, CPyStatic_globals);
        goto CPyL86;
    }
    cpy_r_r193 = PyList_New(1);
    if (unlikely(cpy_r_r193 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 90, CPyStatic_globals);
        goto CPyL87;
    }
    cpy_r_r194 = (CPyPtr)&((PyListObject *)cpy_r_r193)->ob_item;
    cpy_r_r195 = *(CPyPtr *)cpy_r_r194;
    *(PyObject * *)cpy_r_r195 = cpy_r_r192;
    cpy_r_r196 = CPyStatics[17]; /* 'stateMutability' */
    cpy_r_r197 = CPyStatics[18]; /* 'view' */
    cpy_r_r198 = CPyStatics[13]; /* 'type' */
    cpy_r_r199 = CPyStatics[19]; /* 'function' */
    cpy_r_r200 = CPyDict_Build(5, cpy_r_r181, cpy_r_r182, cpy_r_r183, cpy_r_r184, cpy_r_r185, cpy_r_r193, cpy_r_r196, cpy_r_r197, cpy_r_r198, cpy_r_r199);
    CPy_DECREF_NO_IMM(cpy_r_r182);
    CPy_DECREF_NO_IMM(cpy_r_r193);
    if (unlikely(cpy_r_r200 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 87, CPyStatic_globals);
        goto CPyL85;
    }
    cpy_r_r201 = CPyList_Build(12, cpy_r_r43, cpy_r_r54, cpy_r_r65, cpy_r_r85, cpy_r_r105, cpy_r_r116, cpy_r_r127, cpy_r_r138, cpy_r_r149, cpy_r_r160, cpy_r_r180, cpy_r_r200);
    if (unlikely(cpy_r_r201 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r202 = CPyStatic_globals;
    cpy_r_r203 = CPyStatics[36]; /* 'PANIC_ERRORS_CONTRACT_ABI' */
    cpy_r_r204 = CPyDict_SetItem(cpy_r_r202, cpy_r_r203, cpy_r_r201);
    CPy_DECREF_NO_IMM(cpy_r_r201);
    cpy_r_r205 = cpy_r_r204 >= 0;
    if (unlikely(!cpy_r_r205)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r206 = CPyStatics[37]; /* 'bytecode' */
    cpy_r_r207 = CPyStatic_globals;
    cpy_r_r208 = CPyStatics[5]; /* 'PANIC_ERRORS_CONTRACT_BYTECODE' */
    cpy_r_r209 = CPyDict_GetItem(cpy_r_r207, cpy_r_r208);
    if (unlikely(cpy_r_r209 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 96, CPyStatic_globals);
        goto CPyL58;
    }
    if (likely(PyUnicode_Check(cpy_r_r209)))
        cpy_r_r210 = cpy_r_r209;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 96, CPyStatic_globals, "str", cpy_r_r209);
        goto CPyL58;
    }
    cpy_r_r211 = CPyStatics[38]; /* 'bytecode_runtime' */
    cpy_r_r212 = CPyStatic_globals;
    cpy_r_r213 = CPyStatics[7]; /* 'PANIC_ERRORS_CONTRACT_RUNTIME' */
    cpy_r_r214 = CPyDict_GetItem(cpy_r_r212, cpy_r_r213);
    if (unlikely(cpy_r_r214 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 97, CPyStatic_globals);
        goto CPyL88;
    }
    if (likely(PyUnicode_Check(cpy_r_r214)))
        cpy_r_r215 = cpy_r_r214;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 97, CPyStatic_globals, "str", cpy_r_r214);
        goto CPyL88;
    }
    cpy_r_r216 = CPyStatics[39]; /* 'abi' */
    cpy_r_r217 = CPyStatic_globals;
    cpy_r_r218 = CPyStatics[36]; /* 'PANIC_ERRORS_CONTRACT_ABI' */
    cpy_r_r219 = CPyDict_GetItem(cpy_r_r217, cpy_r_r218);
    if (unlikely(cpy_r_r219 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 98, CPyStatic_globals);
        goto CPyL89;
    }
    if (likely(PyList_Check(cpy_r_r219)))
        cpy_r_r220 = cpy_r_r219;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 98, CPyStatic_globals, "list", cpy_r_r219);
        goto CPyL89;
    }
    cpy_r_r221 = CPyDict_Build(3, cpy_r_r206, cpy_r_r210, cpy_r_r211, cpy_r_r215, cpy_r_r216, cpy_r_r220);
    CPy_DECREF(cpy_r_r210);
    CPy_DECREF(cpy_r_r215);
    CPy_DECREF_NO_IMM(cpy_r_r220);
    if (unlikely(cpy_r_r221 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 95, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r222 = CPyStatic_globals;
    cpy_r_r223 = CPyStatics[40]; /* 'PANIC_ERRORS_CONTRACT_DATA' */
    cpy_r_r224 = CPyDict_SetItem(cpy_r_r222, cpy_r_r223, cpy_r_r221);
    CPy_DECREF(cpy_r_r221);
    cpy_r_r225 = cpy_r_r224 >= 0;
    if (unlikely(!cpy_r_r225)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/panic_errors_contract.py", "<module>", 95, CPyStatic_globals);
        goto CPyL58;
    }
    return 1;
CPyL58: ;
    cpy_r_r226 = 2;
    return cpy_r_r226;
CPyL59: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL58;
CPyL60: ;
    CPy_DecRef(cpy_r_r23);
    goto CPyL58;
CPyL61: ;
    CPy_DecRef(cpy_r_r23);
    CPy_DecRef(cpy_r_r35);
    goto CPyL58;
CPyL62: ;
    CPy_DecRef(cpy_r_r43);
    goto CPyL58;
CPyL63: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r45);
    goto CPyL58;
CPyL64: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    goto CPyL58;
CPyL65: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r56);
    goto CPyL58;
CPyL66: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    goto CPyL58;
CPyL67: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r73);
    goto CPyL58;
CPyL68: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r74);
    goto CPyL58;
CPyL69: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    goto CPyL58;
CPyL70: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r93);
    goto CPyL58;
CPyL71: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r94);
    goto CPyL58;
CPyL72: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    goto CPyL58;
CPyL73: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r107);
    goto CPyL58;
CPyL74: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    goto CPyL58;
CPyL75: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r118);
    goto CPyL58;
CPyL76: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    goto CPyL58;
CPyL77: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r129);
    goto CPyL58;
CPyL78: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    goto CPyL58;
CPyL79: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r140);
    goto CPyL58;
CPyL80: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    goto CPyL58;
CPyL81: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r151);
    goto CPyL58;
CPyL82: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    goto CPyL58;
CPyL83: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    CPy_DecRef(cpy_r_r162);
    goto CPyL58;
CPyL84: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    CPy_DecRef(cpy_r_r162);
    CPy_DecRef(cpy_r_r172);
    goto CPyL58;
CPyL85: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    CPy_DecRef(cpy_r_r180);
    goto CPyL58;
CPyL86: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    CPy_DecRef(cpy_r_r180);
    CPy_DecRef(cpy_r_r182);
    goto CPyL58;
CPyL87: ;
    CPy_DecRef(cpy_r_r43);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r65);
    CPy_DecRef(cpy_r_r85);
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r116);
    CPy_DecRef(cpy_r_r127);
    CPy_DecRef(cpy_r_r138);
    CPy_DecRef(cpy_r_r149);
    CPy_DecRef(cpy_r_r160);
    CPy_DecRef(cpy_r_r180);
    CPy_DecRef(cpy_r_r182);
    CPy_DecRef(cpy_r_r192);
    goto CPyL58;
CPyL88: ;
    CPy_DecRef(cpy_r_r210);
    goto CPyL58;
CPyL89: ;
    CPy_DecRef(cpy_r_r210);
    CPy_DecRef(cpy_r_r215);
    goto CPyL58;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[41];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\274$0x60806040525f67ffffffffffffffff81111561001e5761001d61018f565b5b60405190808252806020026020018201604052801561005157816020015b606081526020019060019003908161003c5790505b505f90805190602001906100669291906100bd565b506040518060400160405280600381526020017f6162630000000000000000000000000000000000000000000000000000000000815250600190816100ab91906103cc565b503480156100b7575f5ffd5b50610574565b828054828255905f5260205f20908101928215610103579160200282015b828111156101025782518290816100f291906104a5565b50916020019190600101906100db565b5b5090506101109190610114565b5090565b5b80821115610133575f818161012a9190610137565b50600101610115565b5090565b508054610143906101f3565b5f825580601f106101545750610171565b601f0160209004905f5260205f20908101906101709190610174565b5b50565b5b8082111561018b575f815f905550600101610175565b5090565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061020a57607f821691505b60208210810361021d5761021c6101c6565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261027f7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610244565b6102898683610244565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6102cd6102c86102c3846102a1565b6102aa565b6102a1565b9050919050565b5f819050919050565b6102e6836102b3565b6102fa6102f2826102d4565b848454610250565b825550505050565b5f5f905090565b610311610302565b61031c8184846102dd565b505050565b5b8181101561033f576103345f82610309565b600181019050610322565b5050565b601f8211156103845761035581610223565b61035e84610235565b8101602085101561036d578190505b61038161037985610235565b830182610321565b50505b505050565b5f82821c905092915050565b5f6103a45f1984600802610389565b1980831691505092915050565b5f6103bc8383610395565b9150826002028217905092915050565b6103d5826101bc565b67ffffffffffffffff8111156103ee576103ed61018f565b5b6103f882546101f3565b610403828285610343565b5f60209050601f831160018114610434575f8415610422578287015190505b61042c85826103b1565b865550610493565b601f19841661044286610223565b5f5b8281101561046957848901518255600182019150602085019450602081019050610444565b868310156104865784890151610482601f891682610395565b8355505b6001600288020188555050505b505050505050565b5f81519050919050565b6104ae8261049b565b67ffffffffffffffff8111156104c7576104c661018f565b5b6104d182546101f3565b6104dc828285610343565b5f60209050601f83116001811461050d575f84156104fb578287015190505b61050585826103b1565b86555061056c565b601f19841661051b86610223565b5f5b828110156105425784890151825560018201915060208501945060208101905061051d565b8683101561055f578489015161055b601f891682610395565b8355505b6001600288020188555050505b505050505050565b610990806105815f395ff3fe608060405234801561000f575f5ffd5b50600436106100b2575f3560e01c80638e5ab2d21161006f5780638e5ab2d214610118578063946c05b214610122578063a56dfe4a1461012c578063b6a3bfb11461014a578063c2eb2ebb14610166578063fc430d5c14610170576100b2565b80630c55699c146100b65780633124bba4146100d45780633b447353146100de578063554c0809146100e85780636407fe2c146100f25780636fff525e146100fc575b5f5ffd5b6100be6101a0565b6040516100cb919061065e565b60405180910390f35b6100dc61022c565b005b6100e661024b565b005b6100f06102bf565b005b6100fa6102d4565b005b610116600480360381019061011191906106b5565b6102e4565b005b6101206102fd565b005b61012a61032b565b005b610134610355565b604051610141919061065e565b60405180910390f35b610164600480360381019061015f9190610713565b6103e1565b005b61016e6103f5565b005b61018a60048036038101906101859190610713565b6104e7565b604051610197919061065e565b60405180910390f35b600180546101ad9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546101d99061076b565b80156102245780601f106101fb57610100808354040283529160200191610224565b820191905f5260205f20905b81548152906001019060200180831161020757829003601f168201915b505050505081565b5f6001815481106102405761023f61079b565b5b905f5260205f205050565b5f7f080000000000000000000000000000000000000000000000000000000000000090505f8167ffffffffffffffff81111561028a576102896107c8565b5b6040519080825280602002602001820160405280156102b85781602001602082028036833780820191505090505b5090505050565b5f5f905080806102ce90610822565b91505050565b5f6102e2576102e1610849565b5b565b5f815f8111156102f7576102f6610876565b5b90505050565b5f80548061030e5761030d6108a3565b5b600190038181905f5260205f20015f610327919061058c565b9055565b61035360035f9054906101000a900480156105c9021767ffffffffffffffff1663ffffffff16565b565b600280546103629061076b565b80601f016020809104026020016040519081016040528092919081815260200182805461038e9061076b565b80156103d95780601f106103b0576101008083540402835291602001916103d9565b820191905f5260205f20905b8154815290600101906020018083116103bc57829003601f168201915b505050505081565b5f8160056103ef91906108fd565b90505050565b604060015560025f610407919061058c565b60018054806104159061076b565b80610447577f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b601f81115f811461045f5760018114610481576104de565b6001826021036101000a036001830392506002830284821916179350506104de565b835f5260205f2082602081146104c757601f6001850316602060018603048301925082546001826020036101000a038181191691508185556002880397505050506104db565b81545f835560ff1981169050603e81179550505b50505b50818355505050565b5f81815481106104f5575f80fd5b905f5260205f20015f91509050805461050d9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546105399061076b565b80156105845780601f1061055b57610100808354040283529160200191610584565b820191905f5260205f20905b81548152906001019060200180831161056757829003601f168201915b505050505081565b5080546105989061076b565b5f825580601f106105a957506105c6565b601f0160209004905f5260205f20908101906105c591906105d3565b5b50565b6105d161092d565b565b5b808211156105ea575f815f9055506001016105d4565b5090565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f610630826105ee565b61063a81856105f8565b935061064a818560208601610608565b61065381610616565b840191505092915050565b5f6020820190508181035f8301526106768184610626565b905092915050565b5f5ffd5b5f819050919050565b61069481610682565b811461069e575f5ffd5b50565b5f813590506106af8161068b565b92915050565b5f602082840312156106ca576106c961067e565b5b5f6106d7848285016106a1565b91505092915050565b5f819050919050565b6106f2816106e0565b81146106fc575f5ffd5b50565b5f8135905061070d816106e9565b92915050565b5f602082840312156107285761072761067e565b5b5f610735848285016106ff565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061078257607f821691505b6020821081036107955761079461073e565b5b50919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61082c826106e0565b91505f820361083e5761083d6107f5565b5b600182039050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52600160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f610907826106e0565b9150610912836106e0565b925082610922576109216108d0565b5b828204905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52605160045260245ffdfea26469706673582212204171ea044bdab54fb9f772923ea05ce4bed278fbc8ad7dcae1c768f2ab5fbb6f64736f6c634300081e0033",
    "\001\036PANIC_ERRORS_CONTRACT_BYTECODE",
    "\001\246\"0x608060405234801561000f575f5ffd5b50600436106100b2575f3560e01c80638e5ab2d21161006f5780638e5ab2d214610118578063946c05b214610122578063a56dfe4a1461012c578063b6a3bfb11461014a578063c2eb2ebb14610166578063fc430d5c14610170576100b2565b80630c55699c146100b65780633124bba4146100d45780633b447353146100de578063554c0809146100e85780636407fe2c146100f25780636fff525e146100fc575b5f5ffd5b6100be6101a0565b6040516100cb919061065e565b60405180910390f35b6100dc61022c565b005b6100e661024b565b005b6100f06102bf565b005b6100fa6102d4565b005b610116600480360381019061011191906106b5565b6102e4565b005b6101206102fd565b005b61012a61032b565b005b610134610355565b604051610141919061065e565b60405180910390f35b610164600480360381019061015f9190610713565b6103e1565b005b61016e6103f5565b005b61018a60048036038101906101859190610713565b6104e7565b604051610197919061065e565b60405180910390f35b600180546101ad9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546101d99061076b565b80156102245780601f106101fb57610100808354040283529160200191610224565b820191905f5260205f20905b81548152906001019060200180831161020757829003601f168201915b505050505081565b5f6001815481106102405761023f61079b565b5b905f5260205f205050565b5f7f080000000000000000000000000000000000000000000000000000000000000090505f8167ffffffffffffffff81111561028a576102896107c8565b5b6040519080825280602002602001820160405280156102b85781602001602082028036833780820191505090505b5090505050565b5f5f905080806102ce90610822565b91505050565b5f6102e2576102e1610849565b5b565b5f815f8111156102f7576102f6610876565b5b90505050565b5f80548061030e5761030d6108a3565b5b600190038181905f5260205f20015f610327919061058c565b9055565b61035360035f9054906101000a900480156105c9021767ffffffffffffffff1663ffffffff16565b565b600280546103629061076b565b80601f016020809104026020016040519081016040528092919081815260200182805461038e9061076b565b80156103d95780601f106103b0576101008083540402835291602001916103d9565b820191905f5260205f20905b8154815290600101906020018083116103bc57829003601f168201915b505050505081565b5f8160056103ef91906108fd565b90505050565b604060015560025f610407919061058c565b60018054806104159061076b565b80610447577f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b601f81115f811461045f5760018114610481576104de565b6001826021036101000a036001830392506002830284821916179350506104de565b835f5260205f2082602081146104c757601f6001850316602060018603048301925082546001826020036101000a038181191691508185556002880397505050506104db565b81545f835560ff1981169050603e81179550505b50505b50818355505050565b5f81815481106104f5575f80fd5b905f5260205f20015f91509050805461050d9061076b565b80601f01602080910402602001604051908101604052809291908181526020018280546105399061076b565b80156105845780601f1061055b57610100808354040283529160200191610584565b820191905f5260205f20905b81548152906001019060200180831161056757829003601f168201915b505050505081565b5080546105989061076b565b5f825580601f106105a957506105c6565b601f0160209004905f5260205f20908101906105c591906105d3565b5b50565b6105d161092d565b565b5b808211156105ea575f815f9055506001016105d4565b5090565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f610630826105ee565b61063a81856105f8565b935061064a818560208601610608565b61065381610616565b840191505092915050565b5f6020820190508181035f8301526106768184610626565b905092915050565b5f5ffd5b5f819050919050565b61069481610682565b811461069e575f5ffd5b50565b5f813590506106af8161068b565b92915050565b5f602082840312156106ca576106c961067e565b5b5f6106d7848285016106a1565b91505092915050565b5f819050919050565b6106f2816106e0565b81146106fc575f5ffd5b50565b5f8135905061070d816106e9565b92915050565b5f602082840312156107285761072761067e565b5b5f610735848285016106ff565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061078257607f821691505b6020821081036107955761079461073e565b5b50919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603260045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f61082c826106e0565b91505f820361083e5761083d6107f5565b5b600182039050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52600160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52603160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601260045260245ffd5b5f610907826106e0565b9150610912836106e0565b925082610922576109216108d0565b5b828204905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52605160045260245ffdfea26469706673582212204171ea044bdab54fb9f772923ea05ce4bed278fbc8ad7dcae1c768f2ab5fbb6f64736f6c634300081e0033",
    "\a\035PANIC_ERRORS_CONTRACT_RUNTIME\006inputs\finternalType\auint256\004name\000\004type",
    "\a\nemptyArray\aoutputs\005bytes\017stateMutability\004view\bfunction\verrorCode01",
    "\a\004pure\verrorCode11\004zero\verrorCode12\006int256\vnegativeInt\verrorCode21",
    "\005\verrorCode22\nnonpayable\verrorCode31\verrorCode32\verrorCode41",
    "\006\verrorCode51\001x\001y\031PANIC_ERRORS_CONTRACT_ABI\bbytecode\020bytecode_runtime",
    "\002\003abi\032PANIC_ERRORS_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___panic_errors_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_panic_errors_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___panic_errors_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___panic_errors_contract, "faster_web3._utils.contract_sources.contract_data.panic_errors_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___panic_errors_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___panic_errors_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_panic_errors_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.panic_errors_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_panic_errors_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_panic_errors_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_panic_errors_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
