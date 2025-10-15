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
#include "__native_bytes_contracts.h"
#include "__native_internal_bytes_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___bytes_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.bytes_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___bytes_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___bytes_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal;
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
    CPyPtr cpy_r_r44;
    CPyPtr cpy_r_r45;
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
    PyObject *cpy_r_r74;
    PyObject *cpy_r_r75;
    PyObject *cpy_r_r76;
    PyObject *cpy_r_r77;
    PyObject *cpy_r_r78;
    PyObject *cpy_r_r79;
    CPyPtr cpy_r_r80;
    CPyPtr cpy_r_r81;
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
    CPyPtr cpy_r_r94;
    CPyPtr cpy_r_r95;
    CPyPtr cpy_r_r96;
    PyObject *cpy_r_r97;
    PyObject *cpy_r_r98;
    int32_t cpy_r_r99;
    char cpy_r_r100;
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
    int32_t cpy_r_r119;
    char cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    int32_t cpy_r_r124;
    char cpy_r_r125;
    PyObject *cpy_r_r126;
    PyObject *cpy_r_r127;
    PyObject *cpy_r_r128;
    int32_t cpy_r_r129;
    char cpy_r_r130;
    PyObject *cpy_r_r131;
    PyObject *cpy_r_r132;
    PyObject *cpy_r_r133;
    PyObject *cpy_r_r134;
    PyObject *cpy_r_r135;
    PyObject *cpy_r_r136;
    PyObject *cpy_r_r137;
    PyObject *cpy_r_r138;
    PyObject *cpy_r_r139;
    CPyPtr cpy_r_r140;
    CPyPtr cpy_r_r141;
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
    CPyPtr cpy_r_r160;
    CPyPtr cpy_r_r161;
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
    CPyPtr cpy_r_r180;
    CPyPtr cpy_r_r181;
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
    PyObject *cpy_r_r195;
    CPyPtr cpy_r_r196;
    CPyPtr cpy_r_r197;
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
    CPyPtr cpy_r_r210;
    CPyPtr cpy_r_r211;
    CPyPtr cpy_r_r212;
    PyObject *cpy_r_r213;
    PyObject *cpy_r_r214;
    int32_t cpy_r_r215;
    char cpy_r_r216;
    PyObject *cpy_r_r217;
    PyObject *cpy_r_r218;
    PyObject *cpy_r_r219;
    PyObject *cpy_r_r220;
    PyObject *cpy_r_r221;
    PyObject *cpy_r_r222;
    PyObject *cpy_r_r223;
    PyObject *cpy_r_r224;
    PyObject *cpy_r_r225;
    PyObject *cpy_r_r226;
    PyObject *cpy_r_r227;
    PyObject *cpy_r_r228;
    PyObject *cpy_r_r229;
    PyObject *cpy_r_r230;
    PyObject *cpy_r_r231;
    PyObject *cpy_r_r232;
    PyObject *cpy_r_r233;
    PyObject *cpy_r_r234;
    int32_t cpy_r_r235;
    char cpy_r_r236;
    char cpy_r_r237;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL58;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x60806040526040518060400160405280600281526020017f01230000000000000000000000000000000000000000000000000000000000008152505f908161004791906102c8565b50348015610053575f5ffd5b50604051610cd0380380610cd0833981810160405281019061007591906104b7565b80600190816100849190610508565b50506105d7565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061010657607f821691505b602082108103610119576101186100c2565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261017b7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610140565b6101858683610140565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6101c96101c46101bf8461019d565b6101a6565b61019d565b9050919050565b5f819050919050565b6101e2836101af565b6101f66101ee826101d0565b84845461014c565b825550505050565b5f5f905090565b61020d6101fe565b6102188184846101d9565b505050565b5b8181101561023b576102305f82610205565b60018101905061021e565b5050565b601f821115610280576102518161011f565b61025a84610131565b81016020851015610269578190505b61027d61027585610131565b83018261021d565b50505b505050565b5f82821c905092915050565b5f6102a05f1984600802610285565b1980831691505092915050565b5f6102b88383610291565b9150826002028217905092915050565b6102d18261008b565b67ffffffffffffffff8111156102ea576102e9610095565b5b6102f482546100ef565b6102ff82828561023f565b5f60209050601f831160018114610330575f841561031e578287015190505b61032885826102ad565b86555061038f565b601f19841661033e8661011f565b5f5b8281101561036557848901518255600182019150602085019450602081019050610340565b86831015610382578489015161037e601f891682610291565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6103c9826103b0565b810181811067ffffffffffffffff821117156103e8576103e7610095565b5b80604052505050565b5f6103fa610397565b905061040682826103c0565b919050565b5f67ffffffffffffffff82111561042557610424610095565b5b61042e826103b0565b9050602081019050919050565b8281835e5f83830152505050565b5f61045b6104568461040b565b6103f1565b905082815260208101848484011115610477576104766103ac565b5b61048284828561043b565b509392505050565b5f82601f83011261049e5761049d6103a8565b5b81516104ae848260208601610449565b91505092915050565b5f602082840312156104cc576104cb6103a0565b5b5f82015167ffffffffffffffff8111156104e9576104e86103a4565b5b6104f58482850161048a565b91505092915050565b5f81519050919050565b610511826104fe565b67ffffffffffffffff81111561052a57610529610095565b5b61053482546100ef565b61053f82828561023f565b5f60209050601f831160018114610570575f841561055e578287015190505b61056885826102ad565b8655506105cf565b601f19841661057e8661011f565b5f5b828110156105a557848901518255600182019150602085019450602081019050610580565b868310156105c257848901516105be601f891682610291565b8355505b6001600288020188555050505b505050505050565b6106ec806105e45f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee14610061578063439970aa1461007f575b5f5ffd5b61004b61009b565b604051610058919061023d565b60405180910390f35b61006961012b565b604051610076919061023d565b60405180910390f35b6100996004803603810190610094919061039a565b6101ba565b005b6060600180546100aa9061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546100d69061040e565b80156101215780601f106100f857610100808354040283529160200191610121565b820191905f5260205f20905b81548152906001019060200180831161010457829003601f168201915b5050505050905090565b60605f80546101399061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546101659061040e565b80156101b05780601f10610187576101008083540402835291602001916101b0565b820191905f5260205f20905b81548152906001019060200180831161019357829003601f168201915b5050505050905090565b80600190816101c991906105e7565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61020f826101cd565b61021981856101d7565b93506102298185602086016101e7565b610232816101f5565b840191505092915050565b5f6020820190508181035f8301526102558184610205565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6102ac826101f5565b810181811067ffffffffffffffff821117156102cb576102ca610276565b5b80604052505050565b5f6102dd61025d565b90506102e982826102a3565b919050565b5f67ffffffffffffffff82111561030857610307610276565b5b610311826101f5565b9050602081019050919050565b828183375f83830152505050565b5f61033e610339846102ee565b6102d4565b90508281526020810184848401111561035a57610359610272565b5b61036584828561031e565b509392505050565b5f82601f8301126103815761038061026e565b5b813561039184826020860161032c565b91505092915050565b5f602082840312156103af576103ae610266565b5b5f82013567ffffffffffffffff8111156103cc576103cb61026a565b5b6103d88482850161036d565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061042557607f821691505b602082108103610438576104376103e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261049a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261045f565b6104a4868361045f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6104e86104e36104de846104bc565b6104c5565b6104bc565b9050919050565b5f819050919050565b610501836104ce565b61051561050d826104ef565b84845461046b565b825550505050565b5f5f905090565b61052c61051d565b6105378184846104f8565b505050565b5b8181101561055a5761054f5f82610524565b60018101905061053d565b5050565b601f82111561059f576105708161043e565b61057984610450565b81016020851015610588578190505b61059c61059485610450565b83018261053c565b50505b505050565b5f82821c905092915050565b5f6105bf5f19846008026105a4565b1980831691505092915050565b5f6105d783836105b0565b9150826002028217905092915050565b6105f0826101cd565b67ffffffffffffffff81111561060957610608610276565b5b610613825461040e565b61061e82828561055e565b5f60209050601f83116001811461064f575f841561063d578287015190505b61064785826105cc565b8655506106ae565b601f19841661065d8661043e565b5f5b828110156106845784890151825560018201915060208501945060208101905061065f565b868310156106a1578489015161069d601f8916826105b0565b8355505b6001600288020188555050505b50505050505056fea264697066735822122016f03ea646f744b37e74f32f6ca48b4a1b46030eb5d31dd562f4b2e8caf3e05a64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'BYTES_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 7, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee14610061578063439970aa1461007f575b5f5ffd5b61004b61009b565b604051610058919061023d565b60405180910390f35b61006961012b565b604051610076919061023d565b60405180910390f35b6100996004803603810190610094919061039a565b6101ba565b005b6060600180546100aa9061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546100d69061040e565b80156101215780601f106100f857610100808354040283529160200191610121565b820191905f5260205f20905b81548152906001019060200180831161010457829003601f168201915b5050505050905090565b60605f80546101399061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546101659061040e565b80156101b05780601f10610187576101008083540402835291602001916101b0565b820191905f5260205f20905b81548152906001019060200180831161019357829003601f168201915b5050505050905090565b80600190816101c991906105e7565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61020f826101cd565b61021981856101d7565b93506102298185602086016101e7565b610232816101f5565b840191505092915050565b5f6020820190508181035f8301526102558184610205565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6102ac826101f5565b810181811067ffffffffffffffff821117156102cb576102ca610276565b5b80604052505050565b5f6102dd61025d565b90506102e982826102a3565b919050565b5f67ffffffffffffffff82111561030857610307610276565b5b610311826101f5565b9050602081019050919050565b828183375f83830152505050565b5f61033e610339846102ee565b6102d4565b90508281526020810184848401111561035a57610359610272565b5b61036584828561031e565b509392505050565b5f82601f8301126103815761038061026e565b5b813561039184826020860161032c565b91505092915050565b5f602082840312156103af576103ae610266565b5b5f82013567ffffffffffffffff8111156103cc576103cb61026a565b5b6103d88482850161036d565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061042557607f821691505b602082108103610438576104376103e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261049a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261045f565b6104a4868361045f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6104e86104e36104de846104bc565b6104c5565b6104bc565b9050919050565b5f819050919050565b610501836104ce565b61051561050d826104ef565b84845461046b565b825550505050565b5f5f905090565b61052c61051d565b6105378184846104f8565b505050565b5b8181101561055a5761054f5f82610524565b60018101905061053d565b5050565b601f82111561059f576105708161043e565b61057984610450565b81016020851015610588578190505b61059c61059485610450565b83018261053c565b50505b505050565b5f82821c905092915050565b5f6105bf5f19846008026105a4565b1980831691505092915050565b5f6105d783836105b0565b9150826002028217905092915050565b6105f0826101cd565b67ffffffffffffffff81111561060957610608610276565b5b610613825461040e565b61061e82828561055e565b5f60209050601f83116001811461064f575f841561063d578287015190505b61064785826105cc565b8655506106ae565b601f19841661065d8661043e565b5f5b828110156106845784890151825560018201915060208501945060208101905061065f565b868310156106a1578489015161069d601f8916826105b0565b8355505b6001600288020188555050505b50505050505056fea264697066735822122016f03ea646f744b37e74f32f6ca48b4a1b46030eb5d31dd562f4b2e8caf3e05a64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'BYTES_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 8, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r17 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r18 = CPyStatics[11]; /* 'name' */
    cpy_r_r19 = CPyStatics[12]; /* '_value' */
    cpy_r_r20 = CPyStatics[13]; /* 'type' */
    cpy_r_r21 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r22 = CPyDict_Build(3, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r23 = PyList_New(1);
    if (unlikely(cpy_r_r23 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 11, CPyStatic_globals);
        goto CPyL59;
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
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r31 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r32 = PyList_New(0);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 16, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r33 = CPyStatics[11]; /* 'name' */
    cpy_r_r34 = CPyStatics[17]; /* 'constValue' */
    cpy_r_r35 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r36 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r37 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r38 = CPyStatics[11]; /* 'name' */
    cpy_r_r39 = CPyStatics[19]; /* '' */
    cpy_r_r40 = CPyStatics[13]; /* 'type' */
    cpy_r_r41 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r42 = CPyDict_Build(3, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41);
    if (unlikely(cpy_r_r42 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r43 = PyList_New(1);
    if (unlikely(cpy_r_r43 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 18, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r44 = (CPyPtr)&((PyListObject *)cpy_r_r43)->ob_item;
    cpy_r_r45 = *(CPyPtr *)cpy_r_r44;
    *(PyObject * *)cpy_r_r45 = cpy_r_r42;
    cpy_r_r46 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r47 = CPyStatics[20]; /* 'view' */
    cpy_r_r48 = CPyStatics[13]; /* 'type' */
    cpy_r_r49 = CPyStatics[21]; /* 'function' */
    cpy_r_r50 = CPyDict_Build(5, cpy_r_r31, cpy_r_r32, cpy_r_r33, cpy_r_r34, cpy_r_r35, cpy_r_r43, cpy_r_r46, cpy_r_r47, cpy_r_r48, cpy_r_r49);
    CPy_DECREF_NO_IMM(cpy_r_r32);
    CPy_DECREF_NO_IMM(cpy_r_r43);
    if (unlikely(cpy_r_r50 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 15, CPyStatic_globals);
        goto CPyL60;
    }
    cpy_r_r51 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r52 = PyList_New(0);
    if (unlikely(cpy_r_r52 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 23, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r53 = CPyStatics[11]; /* 'name' */
    cpy_r_r54 = CPyStatics[22]; /* 'getValue' */
    cpy_r_r55 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r56 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r57 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r58 = CPyStatics[11]; /* 'name' */
    cpy_r_r59 = CPyStatics[19]; /* '' */
    cpy_r_r60 = CPyStatics[13]; /* 'type' */
    cpy_r_r61 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r62 = CPyDict_Build(3, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61);
    if (unlikely(cpy_r_r62 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL64;
    }
    cpy_r_r63 = PyList_New(1);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r64 = (CPyPtr)&((PyListObject *)cpy_r_r63)->ob_item;
    cpy_r_r65 = *(CPyPtr *)cpy_r_r64;
    *(PyObject * *)cpy_r_r65 = cpy_r_r62;
    cpy_r_r66 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r67 = CPyStatics[20]; /* 'view' */
    cpy_r_r68 = CPyStatics[13]; /* 'type' */
    cpy_r_r69 = CPyStatics[21]; /* 'function' */
    cpy_r_r70 = CPyDict_Build(5, cpy_r_r51, cpy_r_r52, cpy_r_r53, cpy_r_r54, cpy_r_r55, cpy_r_r63, cpy_r_r66, cpy_r_r67, cpy_r_r68, cpy_r_r69);
    CPy_DECREF_NO_IMM(cpy_r_r52);
    CPy_DECREF_NO_IMM(cpy_r_r63);
    if (unlikely(cpy_r_r70 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 22, CPyStatic_globals);
        goto CPyL63;
    }
    cpy_r_r71 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r72 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r73 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r74 = CPyStatics[11]; /* 'name' */
    cpy_r_r75 = CPyStatics[12]; /* '_value' */
    cpy_r_r76 = CPyStatics[13]; /* 'type' */
    cpy_r_r77 = CPyStatics[10]; /* 'bytes' */
    cpy_r_r78 = CPyDict_Build(3, cpy_r_r72, cpy_r_r73, cpy_r_r74, cpy_r_r75, cpy_r_r76, cpy_r_r77);
    if (unlikely(cpy_r_r78 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 30, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r79 = PyList_New(1);
    if (unlikely(cpy_r_r79 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 30, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r80 = (CPyPtr)&((PyListObject *)cpy_r_r79)->ob_item;
    cpy_r_r81 = *(CPyPtr *)cpy_r_r80;
    *(PyObject * *)cpy_r_r81 = cpy_r_r78;
    cpy_r_r82 = CPyStatics[11]; /* 'name' */
    cpy_r_r83 = CPyStatics[23]; /* 'setValue' */
    cpy_r_r84 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r85 = PyList_New(0);
    if (unlikely(cpy_r_r85 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 32, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r86 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r87 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r88 = CPyStatics[13]; /* 'type' */
    cpy_r_r89 = CPyStatics[21]; /* 'function' */
    cpy_r_r90 = CPyDict_Build(5, cpy_r_r71, cpy_r_r79, cpy_r_r82, cpy_r_r83, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87, cpy_r_r88, cpy_r_r89);
    CPy_DECREF_NO_IMM(cpy_r_r79);
    CPy_DECREF_NO_IMM(cpy_r_r85);
    if (unlikely(cpy_r_r90 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 29, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r91 = PyList_New(4);
    if (unlikely(cpy_r_r91 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r92 = (CPyPtr)&((PyListObject *)cpy_r_r91)->ob_item;
    cpy_r_r93 = *(CPyPtr *)cpy_r_r92;
    *(PyObject * *)cpy_r_r93 = cpy_r_r30;
    cpy_r_r94 = cpy_r_r93 + 8;
    *(PyObject * *)cpy_r_r94 = cpy_r_r50;
    cpy_r_r95 = cpy_r_r93 + 16;
    *(PyObject * *)cpy_r_r95 = cpy_r_r70;
    cpy_r_r96 = cpy_r_r93 + 24;
    *(PyObject * *)cpy_r_r96 = cpy_r_r90;
    cpy_r_r97 = CPyStatic_globals;
    cpy_r_r98 = CPyStatics[24]; /* 'BYTES_CONTRACT_ABI' */
    cpy_r_r99 = CPyDict_SetItem(cpy_r_r97, cpy_r_r98, cpy_r_r91);
    CPy_DECREF_NO_IMM(cpy_r_r91);
    cpy_r_r100 = cpy_r_r99 >= 0;
    if (unlikely(!cpy_r_r100)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r101 = CPyStatics[25]; /* 'bytecode' */
    cpy_r_r102 = CPyStatic_globals;
    cpy_r_r103 = CPyStatics[5]; /* 'BYTES_CONTRACT_BYTECODE' */
    cpy_r_r104 = CPyDict_GetItem(cpy_r_r102, cpy_r_r103);
    if (unlikely(cpy_r_r104 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 38, CPyStatic_globals);
        goto CPyL58;
    }
    if (likely(PyUnicode_Check(cpy_r_r104)))
        cpy_r_r105 = cpy_r_r104;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 38, CPyStatic_globals, "str", cpy_r_r104);
        goto CPyL58;
    }
    cpy_r_r106 = CPyStatics[26]; /* 'bytecode_runtime' */
    cpy_r_r107 = CPyStatic_globals;
    cpy_r_r108 = CPyStatics[7]; /* 'BYTES_CONTRACT_RUNTIME' */
    cpy_r_r109 = CPyDict_GetItem(cpy_r_r107, cpy_r_r108);
    if (unlikely(cpy_r_r109 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 39, CPyStatic_globals);
        goto CPyL70;
    }
    if (likely(PyUnicode_Check(cpy_r_r109)))
        cpy_r_r110 = cpy_r_r109;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 39, CPyStatic_globals, "str", cpy_r_r109);
        goto CPyL70;
    }
    cpy_r_r111 = CPyStatics[27]; /* 'abi' */
    cpy_r_r112 = CPyStatic_globals;
    cpy_r_r113 = CPyStatics[24]; /* 'BYTES_CONTRACT_ABI' */
    cpy_r_r114 = CPyDict_GetItem(cpy_r_r112, cpy_r_r113);
    if (unlikely(cpy_r_r114 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 40, CPyStatic_globals);
        goto CPyL71;
    }
    if (likely(PyList_Check(cpy_r_r114)))
        cpy_r_r115 = cpy_r_r114;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 40, CPyStatic_globals, "list", cpy_r_r114);
        goto CPyL71;
    }
    cpy_r_r116 = CPyDict_Build(3, cpy_r_r101, cpy_r_r105, cpy_r_r106, cpy_r_r110, cpy_r_r111, cpy_r_r115);
    CPy_DECREF(cpy_r_r105);
    CPy_DECREF(cpy_r_r110);
    CPy_DECREF_NO_IMM(cpy_r_r115);
    if (unlikely(cpy_r_r116 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r117 = CPyStatic_globals;
    cpy_r_r118 = CPyStatics[28]; /* 'BYTES_CONTRACT_DATA' */
    cpy_r_r119 = CPyDict_SetItem(cpy_r_r117, cpy_r_r118, cpy_r_r116);
    CPy_DECREF(cpy_r_r116);
    cpy_r_r120 = cpy_r_r119 >= 0;
    if (unlikely(!cpy_r_r120)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r121 = CPyStatics[29]; /* '0x60806040527f01230123012301230123012301230123012301230123012301230123012301235f553480156031575f5ffd5b50604051610238380380610238833981810160405281019060519190608f565b806001819055505060b5565b5f5ffd5b5f819050919050565b6071816061565b8114607a575f5ffd5b50565b5f81519050608981606a565b92915050565b5f6020828403121560a15760a0605d565b5b5f60ac84828501607d565b91505092915050565b610176806100c25f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee1461006157806358825b101461007f575b5f5ffd5b61004b61009b565b60405161005891906100ce565b60405180910390f35b6100696100a4565b60405161007691906100ce565b60405180910390f35b61009960048036038101906100949190610115565b6100ac565b005b5f600154905090565b5f5f54905090565b8060018190555050565b5f819050919050565b6100c8816100b6565b82525050565b5f6020820190506100e15f8301846100bf565b92915050565b5f5ffd5b6100f4816100b6565b81146100fe575f5ffd5b50565b5f8135905061010f816100eb565b92915050565b5f6020828403121561012a576101296100e7565b5b5f61013784828501610101565b9150509291505056fea2646970667358221220c158440d9344fca45315eee01e851c4a2624e94a37ca3b0012b31b3b2c85dd6364736f6c634300081e0033' */
    cpy_r_r122 = CPyStatic_globals;
    cpy_r_r123 = CPyStatics[30]; /* 'BYTES32_CONTRACT_BYTECODE' */
    cpy_r_r124 = CPyDict_SetItem(cpy_r_r122, cpy_r_r123, cpy_r_r121);
    cpy_r_r125 = cpy_r_r124 >= 0;
    if (unlikely(!cpy_r_r125)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 45, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r126 = CPyStatics[31]; /* '0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee1461006157806358825b101461007f575b5f5ffd5b61004b61009b565b60405161005891906100ce565b60405180910390f35b6100696100a4565b60405161007691906100ce565b60405180910390f35b61009960048036038101906100949190610115565b6100ac565b005b5f600154905090565b5f5f54905090565b8060018190555050565b5f819050919050565b6100c8816100b6565b82525050565b5f6020820190506100e15f8301846100bf565b92915050565b5f5ffd5b6100f4816100b6565b81146100fe575f5ffd5b50565b5f8135905061010f816100eb565b92915050565b5f6020828403121561012a576101296100e7565b5b5f61013784828501610101565b9150509291505056fea2646970667358221220c158440d9344fca45315eee01e851c4a2624e94a37ca3b0012b31b3b2c85dd6364736f6c634300081e0033' */
    cpy_r_r127 = CPyStatic_globals;
    cpy_r_r128 = CPyStatics[32]; /* 'BYTES32_CONTRACT_RUNTIME' */
    cpy_r_r129 = CPyDict_SetItem(cpy_r_r127, cpy_r_r128, cpy_r_r126);
    cpy_r_r130 = cpy_r_r129 >= 0;
    if (unlikely(!cpy_r_r130)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 46, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r131 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r132 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r133 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r134 = CPyStatics[11]; /* 'name' */
    cpy_r_r135 = CPyStatics[12]; /* '_value' */
    cpy_r_r136 = CPyStatics[13]; /* 'type' */
    cpy_r_r137 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r138 = CPyDict_Build(3, cpy_r_r132, cpy_r_r133, cpy_r_r134, cpy_r_r135, cpy_r_r136, cpy_r_r137);
    if (unlikely(cpy_r_r138 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r139 = PyList_New(1);
    if (unlikely(cpy_r_r139 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r140 = (CPyPtr)&((PyListObject *)cpy_r_r139)->ob_item;
    cpy_r_r141 = *(CPyPtr *)cpy_r_r140;
    *(PyObject * *)cpy_r_r141 = cpy_r_r138;
    cpy_r_r142 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r143 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r144 = CPyStatics[13]; /* 'type' */
    cpy_r_r145 = CPyStatics[16]; /* 'constructor' */
    cpy_r_r146 = CPyDict_Build(3, cpy_r_r131, cpy_r_r139, cpy_r_r142, cpy_r_r143, cpy_r_r144, cpy_r_r145);
    CPy_DECREF_NO_IMM(cpy_r_r139);
    if (unlikely(cpy_r_r146 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 48, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r147 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r148 = PyList_New(0);
    if (unlikely(cpy_r_r148 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r149 = CPyStatics[11]; /* 'name' */
    cpy_r_r150 = CPyStatics[17]; /* 'constValue' */
    cpy_r_r151 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r152 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r153 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r154 = CPyStatics[11]; /* 'name' */
    cpy_r_r155 = CPyStatics[19]; /* '' */
    cpy_r_r156 = CPyStatics[13]; /* 'type' */
    cpy_r_r157 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r158 = CPyDict_Build(3, cpy_r_r152, cpy_r_r153, cpy_r_r154, cpy_r_r155, cpy_r_r156, cpy_r_r157);
    if (unlikely(cpy_r_r158 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r159 = PyList_New(1);
    if (unlikely(cpy_r_r159 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL75;
    }
    cpy_r_r160 = (CPyPtr)&((PyListObject *)cpy_r_r159)->ob_item;
    cpy_r_r161 = *(CPyPtr *)cpy_r_r160;
    *(PyObject * *)cpy_r_r161 = cpy_r_r158;
    cpy_r_r162 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r163 = CPyStatics[20]; /* 'view' */
    cpy_r_r164 = CPyStatics[13]; /* 'type' */
    cpy_r_r165 = CPyStatics[21]; /* 'function' */
    cpy_r_r166 = CPyDict_Build(5, cpy_r_r147, cpy_r_r148, cpy_r_r149, cpy_r_r150, cpy_r_r151, cpy_r_r159, cpy_r_r162, cpy_r_r163, cpy_r_r164, cpy_r_r165);
    CPy_DECREF_NO_IMM(cpy_r_r148);
    CPy_DECREF_NO_IMM(cpy_r_r159);
    if (unlikely(cpy_r_r166 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 53, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r167 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r168 = PyList_New(0);
    if (unlikely(cpy_r_r168 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 61, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r169 = CPyStatics[11]; /* 'name' */
    cpy_r_r170 = CPyStatics[22]; /* 'getValue' */
    cpy_r_r171 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r172 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r173 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r174 = CPyStatics[11]; /* 'name' */
    cpy_r_r175 = CPyStatics[19]; /* '' */
    cpy_r_r176 = CPyStatics[13]; /* 'type' */
    cpy_r_r177 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r178 = CPyDict_Build(3, cpy_r_r172, cpy_r_r173, cpy_r_r174, cpy_r_r175, cpy_r_r176, cpy_r_r177);
    if (unlikely(cpy_r_r178 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 63, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r179 = PyList_New(1);
    if (unlikely(cpy_r_r179 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 63, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r180 = (CPyPtr)&((PyListObject *)cpy_r_r179)->ob_item;
    cpy_r_r181 = *(CPyPtr *)cpy_r_r180;
    *(PyObject * *)cpy_r_r181 = cpy_r_r178;
    cpy_r_r182 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r183 = CPyStatics[20]; /* 'view' */
    cpy_r_r184 = CPyStatics[13]; /* 'type' */
    cpy_r_r185 = CPyStatics[21]; /* 'function' */
    cpy_r_r186 = CPyDict_Build(5, cpy_r_r167, cpy_r_r168, cpy_r_r169, cpy_r_r170, cpy_r_r171, cpy_r_r179, cpy_r_r182, cpy_r_r183, cpy_r_r184, cpy_r_r185);
    CPy_DECREF_NO_IMM(cpy_r_r168);
    CPy_DECREF_NO_IMM(cpy_r_r179);
    if (unlikely(cpy_r_r186 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 60, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r187 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r188 = CPyStatics[9]; /* 'internalType' */
    cpy_r_r189 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r190 = CPyStatics[11]; /* 'name' */
    cpy_r_r191 = CPyStatics[12]; /* '_value' */
    cpy_r_r192 = CPyStatics[13]; /* 'type' */
    cpy_r_r193 = CPyStatics[33]; /* 'bytes32' */
    cpy_r_r194 = CPyDict_Build(3, cpy_r_r188, cpy_r_r189, cpy_r_r190, cpy_r_r191, cpy_r_r192, cpy_r_r193);
    if (unlikely(cpy_r_r194 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 68, CPyStatic_globals);
        goto CPyL79;
    }
    cpy_r_r195 = PyList_New(1);
    if (unlikely(cpy_r_r195 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 68, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r196 = (CPyPtr)&((PyListObject *)cpy_r_r195)->ob_item;
    cpy_r_r197 = *(CPyPtr *)cpy_r_r196;
    *(PyObject * *)cpy_r_r197 = cpy_r_r194;
    cpy_r_r198 = CPyStatics[11]; /* 'name' */
    cpy_r_r199 = CPyStatics[23]; /* 'setValue' */
    cpy_r_r200 = CPyStatics[18]; /* 'outputs' */
    cpy_r_r201 = PyList_New(0);
    if (unlikely(cpy_r_r201 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 70, CPyStatic_globals);
        goto CPyL81;
    }
    cpy_r_r202 = CPyStatics[14]; /* 'stateMutability' */
    cpy_r_r203 = CPyStatics[15]; /* 'nonpayable' */
    cpy_r_r204 = CPyStatics[13]; /* 'type' */
    cpy_r_r205 = CPyStatics[21]; /* 'function' */
    cpy_r_r206 = CPyDict_Build(5, cpy_r_r187, cpy_r_r195, cpy_r_r198, cpy_r_r199, cpy_r_r200, cpy_r_r201, cpy_r_r202, cpy_r_r203, cpy_r_r204, cpy_r_r205);
    CPy_DECREF_NO_IMM(cpy_r_r195);
    CPy_DECREF_NO_IMM(cpy_r_r201);
    if (unlikely(cpy_r_r206 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 67, CPyStatic_globals);
        goto CPyL79;
    }
    cpy_r_r207 = PyList_New(4);
    if (unlikely(cpy_r_r207 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL82;
    }
    cpy_r_r208 = (CPyPtr)&((PyListObject *)cpy_r_r207)->ob_item;
    cpy_r_r209 = *(CPyPtr *)cpy_r_r208;
    *(PyObject * *)cpy_r_r209 = cpy_r_r146;
    cpy_r_r210 = cpy_r_r209 + 8;
    *(PyObject * *)cpy_r_r210 = cpy_r_r166;
    cpy_r_r211 = cpy_r_r209 + 16;
    *(PyObject * *)cpy_r_r211 = cpy_r_r186;
    cpy_r_r212 = cpy_r_r209 + 24;
    *(PyObject * *)cpy_r_r212 = cpy_r_r206;
    cpy_r_r213 = CPyStatic_globals;
    cpy_r_r214 = CPyStatics[34]; /* 'BYTES32_CONTRACT_ABI' */
    cpy_r_r215 = CPyDict_SetItem(cpy_r_r213, cpy_r_r214, cpy_r_r207);
    CPy_DECREF_NO_IMM(cpy_r_r207);
    cpy_r_r216 = cpy_r_r215 >= 0;
    if (unlikely(!cpy_r_r216)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r217 = CPyStatics[25]; /* 'bytecode' */
    cpy_r_r218 = CPyStatic_globals;
    cpy_r_r219 = CPyStatics[30]; /* 'BYTES32_CONTRACT_BYTECODE' */
    cpy_r_r220 = CPyDict_GetItem(cpy_r_r218, cpy_r_r219);
    if (unlikely(cpy_r_r220 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 76, CPyStatic_globals);
        goto CPyL58;
    }
    if (likely(PyUnicode_Check(cpy_r_r220)))
        cpy_r_r221 = cpy_r_r220;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 76, CPyStatic_globals, "str", cpy_r_r220);
        goto CPyL58;
    }
    cpy_r_r222 = CPyStatics[26]; /* 'bytecode_runtime' */
    cpy_r_r223 = CPyStatic_globals;
    cpy_r_r224 = CPyStatics[32]; /* 'BYTES32_CONTRACT_RUNTIME' */
    cpy_r_r225 = CPyDict_GetItem(cpy_r_r223, cpy_r_r224);
    if (unlikely(cpy_r_r225 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 77, CPyStatic_globals);
        goto CPyL83;
    }
    if (likely(PyUnicode_Check(cpy_r_r225)))
        cpy_r_r226 = cpy_r_r225;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 77, CPyStatic_globals, "str", cpy_r_r225);
        goto CPyL83;
    }
    cpy_r_r227 = CPyStatics[27]; /* 'abi' */
    cpy_r_r228 = CPyStatic_globals;
    cpy_r_r229 = CPyStatics[34]; /* 'BYTES32_CONTRACT_ABI' */
    cpy_r_r230 = CPyDict_GetItem(cpy_r_r228, cpy_r_r229);
    if (unlikely(cpy_r_r230 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 78, CPyStatic_globals);
        goto CPyL84;
    }
    if (likely(PyList_Check(cpy_r_r230)))
        cpy_r_r231 = cpy_r_r230;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 78, CPyStatic_globals, "list", cpy_r_r230);
        goto CPyL84;
    }
    cpy_r_r232 = CPyDict_Build(3, cpy_r_r217, cpy_r_r221, cpy_r_r222, cpy_r_r226, cpy_r_r227, cpy_r_r231);
    CPy_DECREF(cpy_r_r221);
    CPy_DECREF(cpy_r_r226);
    CPy_DECREF_NO_IMM(cpy_r_r231);
    if (unlikely(cpy_r_r232 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 75, CPyStatic_globals);
        goto CPyL58;
    }
    cpy_r_r233 = CPyStatic_globals;
    cpy_r_r234 = CPyStatics[35]; /* 'BYTES32_CONTRACT_DATA' */
    cpy_r_r235 = CPyDict_SetItem(cpy_r_r233, cpy_r_r234, cpy_r_r232);
    CPy_DECREF(cpy_r_r232);
    cpy_r_r236 = cpy_r_r235 >= 0;
    if (unlikely(!cpy_r_r236)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/bytes_contracts.py", "<module>", 75, CPyStatic_globals);
        goto CPyL58;
    }
    return 1;
CPyL58: ;
    cpy_r_r237 = 2;
    return cpy_r_r237;
CPyL59: ;
    CPy_DecRef(cpy_r_r22);
    goto CPyL58;
CPyL60: ;
    CPy_DecRef(cpy_r_r30);
    goto CPyL58;
CPyL61: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r32);
    goto CPyL58;
CPyL62: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r32);
    CPy_DecRef(cpy_r_r42);
    goto CPyL58;
CPyL63: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    goto CPyL58;
CPyL64: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r52);
    goto CPyL58;
CPyL65: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r52);
    CPy_DecRef(cpy_r_r62);
    goto CPyL58;
CPyL66: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r70);
    goto CPyL58;
CPyL67: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r70);
    CPy_DecRef(cpy_r_r78);
    goto CPyL58;
CPyL68: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r70);
    CPy_DecRef(cpy_r_r79);
    goto CPyL58;
CPyL69: ;
    CPy_DecRef(cpy_r_r30);
    CPy_DecRef(cpy_r_r50);
    CPy_DecRef(cpy_r_r70);
    CPy_DecRef(cpy_r_r90);
    goto CPyL58;
CPyL70: ;
    CPy_DecRef(cpy_r_r105);
    goto CPyL58;
CPyL71: ;
    CPy_DecRef(cpy_r_r105);
    CPy_DecRef(cpy_r_r110);
    goto CPyL58;
CPyL72: ;
    CPy_DecRef(cpy_r_r138);
    goto CPyL58;
CPyL73: ;
    CPy_DecRef(cpy_r_r146);
    goto CPyL58;
CPyL74: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r148);
    goto CPyL58;
CPyL75: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r148);
    CPy_DecRef(cpy_r_r158);
    goto CPyL58;
CPyL76: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    goto CPyL58;
CPyL77: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r168);
    goto CPyL58;
CPyL78: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r168);
    CPy_DecRef(cpy_r_r178);
    goto CPyL58;
CPyL79: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r186);
    goto CPyL58;
CPyL80: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r186);
    CPy_DecRef(cpy_r_r194);
    goto CPyL58;
CPyL81: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r186);
    CPy_DecRef(cpy_r_r195);
    goto CPyL58;
CPyL82: ;
    CPy_DecRef(cpy_r_r146);
    CPy_DecRef(cpy_r_r166);
    CPy_DecRef(cpy_r_r186);
    CPy_DecRef(cpy_r_r206);
    goto CPyL58;
CPyL83: ;
    CPy_DecRef(cpy_r_r221);
    goto CPyL58;
CPyL84: ;
    CPy_DecRef(cpy_r_r221);
    CPy_DecRef(cpy_r_r226);
    goto CPyL58;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts = Py_None;
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
    "\001\263\"0x60806040526040518060400160405280600281526020017f01230000000000000000000000000000000000000000000000000000000000008152505f908161004791906102c8565b50348015610053575f5ffd5b50604051610cd0380380610cd0833981810160405281019061007591906104b7565b80600190816100849190610508565b50506105d7565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061010657607f821691505b602082108103610119576101186100c2565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261017b7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82610140565b6101858683610140565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6101c96101c46101bf8461019d565b6101a6565b61019d565b9050919050565b5f819050919050565b6101e2836101af565b6101f66101ee826101d0565b84845461014c565b825550505050565b5f5f905090565b61020d6101fe565b6102188184846101d9565b505050565b5b8181101561023b576102305f82610205565b60018101905061021e565b5050565b601f821115610280576102518161011f565b61025a84610131565b81016020851015610269578190505b61027d61027585610131565b83018261021d565b50505b505050565b5f82821c905092915050565b5f6102a05f1984600802610285565b1980831691505092915050565b5f6102b88383610291565b9150826002028217905092915050565b6102d18261008b565b67ffffffffffffffff8111156102ea576102e9610095565b5b6102f482546100ef565b6102ff82828561023f565b5f60209050601f831160018114610330575f841561031e578287015190505b61032885826102ad565b86555061038f565b601f19841661033e8661011f565b5f5b8281101561036557848901518255600182019150602085019450602081019050610340565b86831015610382578489015161037e601f891682610291565b8355505b6001600288020188555050505b505050505050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b6103c9826103b0565b810181811067ffffffffffffffff821117156103e8576103e7610095565b5b80604052505050565b5f6103fa610397565b905061040682826103c0565b919050565b5f67ffffffffffffffff82111561042557610424610095565b5b61042e826103b0565b9050602081019050919050565b8281835e5f83830152505050565b5f61045b6104568461040b565b6103f1565b905082815260208101848484011115610477576104766103ac565b5b61048284828561043b565b509392505050565b5f82601f83011261049e5761049d6103a8565b5b81516104ae848260208601610449565b91505092915050565b5f602082840312156104cc576104cb6103a0565b5b5f82015167ffffffffffffffff8111156104e9576104e86103a4565b5b6104f58482850161048a565b91505092915050565b5f81519050919050565b610511826104fe565b67ffffffffffffffff81111561052a57610529610095565b5b61053482546100ef565b61053f82828561023f565b5f60209050601f831160018114610570575f841561055e578287015190505b61056885826102ad565b8655506105cf565b601f19841661057e8661011f565b5f5b828110156105a557848901518255600182019150602085019450602081019050610580565b868310156105c257848901516105be601f891682610291565b8355505b6001600288020188555050505b505050505050565b6106ec806105e45f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee14610061578063439970aa1461007f575b5f5ffd5b61004b61009b565b604051610058919061023d565b60405180910390f35b61006961012b565b604051610076919061023d565b60405180910390f35b6100996004803603810190610094919061039a565b6101ba565b005b6060600180546100aa9061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546100d69061040e565b80156101215780601f106100f857610100808354040283529160200191610121565b820191905f5260205f20905b81548152906001019060200180831161010457829003601f168201915b5050505050905090565b60605f80546101399061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546101659061040e565b80156101b05780601f10610187576101008083540402835291602001916101b0565b820191905f5260205f20905b81548152906001019060200180831161019357829003601f168201915b5050505050905090565b80600190816101c991906105e7565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61020f826101cd565b61021981856101d7565b93506102298185602086016101e7565b610232816101f5565b840191505092915050565b5f6020820190508181035f8301526102558184610205565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6102ac826101f5565b810181811067ffffffffffffffff821117156102cb576102ca610276565b5b80604052505050565b5f6102dd61025d565b90506102e982826102a3565b919050565b5f67ffffffffffffffff82111561030857610307610276565b5b610311826101f5565b9050602081019050919050565b828183375f83830152505050565b5f61033e610339846102ee565b6102d4565b90508281526020810184848401111561035a57610359610272565b5b61036584828561031e565b509392505050565b5f82601f8301126103815761038061026e565b5b813561039184826020860161032c565b91505092915050565b5f602082840312156103af576103ae610266565b5b5f82013567ffffffffffffffff8111156103cc576103cb61026a565b5b6103d88482850161036d565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061042557607f821691505b602082108103610438576104376103e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261049a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261045f565b6104a4868361045f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6104e86104e36104de846104bc565b6104c5565b6104bc565b9050919050565b5f819050919050565b610501836104ce565b61051561050d826104ef565b84845461046b565b825550505050565b5f5f905090565b61052c61051d565b6105378184846104f8565b505050565b5b8181101561055a5761054f5f82610524565b60018101905061053d565b5050565b601f82111561059f576105708161043e565b61057984610450565b81016020851015610588578190505b61059c61059485610450565b83018261053c565b50505b505050565b5f82821c905092915050565b5f6105bf5f19846008026105a4565b1980831691505092915050565b5f6105d783836105b0565b9150826002028217905092915050565b6105f0826101cd565b67ffffffffffffffff81111561060957610608610276565b5b610613825461040e565b61061e82828561055e565b5f60209050601f83116001811461064f575f841561063d578287015190505b61064785826105cc565b8655506106ae565b601f19841661065d8661043e565b5f5b828110156106845784890151825560018201915060208501945060208101905061065f565b868310156106a1578489015161069d601f8916826105b0565b8355505b6001600288020188555050505b50505050505056fea264697066735822122016f03ea646f744b37e74f32f6ca48b4a1b46030eb5d31dd562f4b2e8caf3e05a64736f6c634300081e0033",
    "\001\027BYTES_CONTRACT_BYTECODE",
    "\001\233Z0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee14610061578063439970aa1461007f575b5f5ffd5b61004b61009b565b604051610058919061023d565b60405180910390f35b61006961012b565b604051610076919061023d565b60405180910390f35b6100996004803603810190610094919061039a565b6101ba565b005b6060600180546100aa9061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546100d69061040e565b80156101215780601f106100f857610100808354040283529160200191610121565b820191905f5260205f20905b81548152906001019060200180831161010457829003601f168201915b5050505050905090565b60605f80546101399061040e565b80601f01602080910402602001604051908101604052809291908181526020018280546101659061040e565b80156101b05780601f10610187576101008083540402835291602001916101b0565b820191905f5260205f20905b81548152906001019060200180831161019357829003601f168201915b5050505050905090565b80600190816101c991906105e7565b5050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61020f826101cd565b61021981856101d7565b93506102298185602086016101e7565b610232816101f5565b840191505092915050565b5f6020820190508181035f8301526102558184610205565b905092915050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b6102ac826101f5565b810181811067ffffffffffffffff821117156102cb576102ca610276565b5b80604052505050565b5f6102dd61025d565b90506102e982826102a3565b919050565b5f67ffffffffffffffff82111561030857610307610276565b5b610311826101f5565b9050602081019050919050565b828183375f83830152505050565b5f61033e610339846102ee565b6102d4565b90508281526020810184848401111561035a57610359610272565b5b61036584828561031e565b509392505050565b5f82601f8301126103815761038061026e565b5b813561039184826020860161032c565b91505092915050565b5f602082840312156103af576103ae610266565b5b5f82013567ffffffffffffffff8111156103cc576103cb61026a565b5b6103d88482850161036d565b91505092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061042557607f821691505b602082108103610438576104376103e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261049a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261045f565b6104a4868361045f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6104e86104e36104de846104bc565b6104c5565b6104bc565b9050919050565b5f819050919050565b610501836104ce565b61051561050d826104ef565b84845461046b565b825550505050565b5f5f905090565b61052c61051d565b6105378184846104f8565b505050565b5b8181101561055a5761054f5f82610524565b60018101905061053d565b5050565b601f82111561059f576105708161043e565b61057984610450565b81016020851015610588578190505b61059c61059485610450565b83018261053c565b50505b505050565b5f82821c905092915050565b5f6105bf5f19846008026105a4565b1980831691505092915050565b5f6105d783836105b0565b9150826002028217905092915050565b6105f0826101cd565b67ffffffffffffffff81111561060957610608610276565b5b610613825461040e565b61061e82828561055e565b5f60209050601f83116001811461064f575f841561063d578287015190505b61064785826105cc565b8655506106ae565b601f19841661065d8661043e565b5f5b828110156106845784890151825560018201915060208501945060208101905061065f565b868310156106a1578489015161069d601f8916826105b0565b8355505b6001600288020188555050505b50505050505056fea264697066735822122016f03ea646f744b37e74f32f6ca48b4a1b46030eb5d31dd562f4b2e8caf3e05a64736f6c634300081e0033",
    "\a\026BYTES_CONTRACT_RUNTIME\006inputs\finternalType\005bytes\004name\006_value\004type",
    "\a\017stateMutability\nnonpayable\vconstructor\nconstValue\aoutputs\000\004view",
    "\005\bfunction\bgetValue\bsetValue\022BYTES_CONTRACT_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi\023BYTES_CONTRACT_DATA",
    "\001\210r0x60806040527f01230123012301230123012301230123012301230123012301230123012301235f553480156031575f5ffd5b50604051610238380380610238833981810160405281019060519190608f565b806001819055505060b5565b5f5ffd5b5f819050919050565b6071816061565b8114607a575f5ffd5b50565b5f81519050608981606a565b92915050565b5f6020828403121560a15760a0605d565b5b5f60ac84828501607d565b91505092915050565b610176806100c25f395ff3fe608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee1461006157806358825b101461007f575b5f5ffd5b61004b61009b565b60405161005891906100ce565b60405180910390f35b6100696100a4565b60405161007691906100ce565b60405180910390f35b61009960048036038101906100949190610115565b6100ac565b005b5f600154905090565b5f5f54905090565b8060018190555050565b5f819050919050565b6100c8816100b6565b82525050565b5f6020820190506100e15f8301846100bf565b92915050565b5f5ffd5b6100f4816100b6565b81146100fe575f5ffd5b50565b5f8135905061010f816100eb565b92915050565b5f6020828403121561012a576101296100e7565b5b5f61013784828501610101565b9150509291505056fea2646970667358221220c158440d9344fca45315eee01e851c4a2624e94a37ca3b0012b31b3b2c85dd6364736f6c634300081e0033",
    "\001\031BYTES32_CONTRACT_BYTECODE",
    "\001\205n0x608060405234801561000f575f5ffd5b506004361061003f575f3560e01c8063209652551461004357806330de3cee1461006157806358825b101461007f575b5f5ffd5b61004b61009b565b60405161005891906100ce565b60405180910390f35b6100696100a4565b60405161007691906100ce565b60405180910390f35b61009960048036038101906100949190610115565b6100ac565b005b5f600154905090565b5f5f54905090565b8060018190555050565b5f819050919050565b6100c8816100b6565b82525050565b5f6020820190506100e15f8301846100bf565b92915050565b5f5ffd5b6100f4816100b6565b81146100fe575f5ffd5b50565b5f8135905061010f816100eb565b92915050565b5f6020828403121561012a576101296100e7565b5b5f61013784828501610101565b9150509291505056fea2646970667358221220c158440d9344fca45315eee01e851c4a2624e94a37ca3b0012b31b3b2c85dd6364736f6c634300081e0033",
    "\003\030BYTES32_CONTRACT_RUNTIME\abytes32\024BYTES32_CONTRACT_ABI",
    "\001\025BYTES32_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___bytes_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_bytes_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___bytes_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___bytes_contracts, "faster_web3._utils.contract_sources.contract_data.bytes_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___bytes_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___bytes_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_bytes_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.bytes_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_bytes_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_bytes_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_bytes_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
