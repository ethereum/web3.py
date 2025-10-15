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
#include "__native_storage_contract.h"
#include "__native_internal_storage_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___storage_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.storage_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___storage_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___storage_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal;
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
    CPyPtr cpy_r_r28;
    CPyPtr cpy_r_r29;
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
    CPyPtr cpy_r_r48;
    CPyPtr cpy_r_r49;
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
    CPyPtr cpy_r_r88;
    CPyPtr cpy_r_r89;
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
    CPyPtr cpy_r_r108;
    CPyPtr cpy_r_r109;
    PyObject *cpy_r_r110;
    PyObject *cpy_r_r111;
    PyObject *cpy_r_r112;
    PyObject *cpy_r_r113;
    PyObject *cpy_r_r114;
    PyObject *cpy_r_r115;
    CPyPtr cpy_r_r116;
    CPyPtr cpy_r_r117;
    CPyPtr cpy_r_r118;
    CPyPtr cpy_r_r119;
    CPyPtr cpy_r_r120;
    CPyPtr cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    int32_t cpy_r_r124;
    char cpy_r_r125;
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
    int32_t cpy_r_r144;
    char cpy_r_r145;
    char cpy_r_r146;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL36;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x60806040525f5f5560018055600280556040518060400160405280600581526020017f74687265650000000000000000000000000000000000000000000000000000008152506003908161005391906102e7565b506040518060400160405280600481526020017f666f757200000000000000000000000000000000000000000000000000000000815250600490816100989190610418565b503480156100a4575f5ffd5b506104e7565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061012557607f821691505b602082108103610138576101376100e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261019a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261015f565b6101a4868361015f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6101e86101e36101de846101bc565b6101c5565b6101bc565b9050919050565b5f819050919050565b610201836101ce565b61021561020d826101ef565b84845461016b565b825550505050565b5f5f905090565b61022c61021d565b6102378184846101f8565b505050565b5b8181101561025a5761024f5f82610224565b60018101905061023d565b5050565b601f82111561029f576102708161013e565b61027984610150565b81016020851015610288578190505b61029c61029485610150565b83018261023c565b50505b505050565b5f82821c905092915050565b5f6102bf5f19846008026102a4565b1980831691505092915050565b5f6102d783836102b0565b9150826002028217905092915050565b6102f0826100aa565b67ffffffffffffffff811115610309576103086100b4565b5b610313825461010e565b61031e82828561025e565b5f60209050601f83116001811461034f575f841561033d578287015190505b61034785826102cc565b8655506103ae565b601f19841661035d8661013e565b5f5b828110156103845784890151825560018201915060208501945060208101905061035f565b868310156103a1578489015161039d601f8916826102b0565b8355505b6001600288020188555050505b505050505050565b5f81519050919050565b5f819050815f5260205f209050919050565b601f821115610413576103e4816103c0565b6103ed84610150565b810160208510156103fc578190505b61041061040885610150565b83018261023c565b50505b505050565b610421826103b6565b67ffffffffffffffff81111561043a576104396100b4565b5b610444825461010e565b61044f8282856103d2565b5f60209050601f831160018114610480575f841561046e578287015190505b61047885826102cc565b8655506104df565b601f19841661048e866103c0565b5f5b828110156104b557848901518255600182019150602085019450602081019050610490565b868310156104d257848901516104ce601f8916826102b0565b8355505b6001600288020188555050505b505050505050565b6103de806104f45f395ff3fe608060405234801561000f575f5ffd5b5060043610610055575f3560e01c80631f457cb5146100595780633850c7bd146100775780634a9a010914610095578063924fe315146100b3578063d987e6b5146100d1575b5f5ffd5b6100616100ef565b60405161006e9190610230565b60405180910390f35b61007f6100f5565b60405161008c9190610230565b60405180910390f35b61009d6100fa565b6040516100aa91906102b9565b60405180910390f35b6100bb610186565b6040516100c8919061032b565b60405180910390f35b6100d9610212565b6040516100e69190610230565b60405180910390f35b60015481565b5f5481565b6004805461010790610378565b80601f016020809104026020016040519081016040528092919081815260200182805461013390610378565b801561017e5780601f106101555761010080835404028352916020019161017e565b820191905f5260205f20905b81548152906001019060200180831161016157829003601f168201915b505050505081565b6003805461019390610378565b80601f01602080910402602001604051908101604052809291908181526020018280546101bf90610378565b801561020a5780601f106101e15761010080835404028352916020019161020a565b820191905f5260205f20905b8154815290600101906020018083116101ed57829003601f168201915b505050505081565b60025481565b5f819050919050565b61022a81610218565b82525050565b5f6020820190506102435f830184610221565b92915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61028b82610249565b6102958185610253565b93506102a5818560208601610263565b6102ae81610271565b840191505092915050565b5f6020820190508181035f8301526102d18184610281565b905092915050565b5f81519050919050565b5f82825260208201905092915050565b5f6102fd826102d9565b61030781856102e3565b9350610317818560208601610263565b61032081610271565b840191505092915050565b5f6020820190508181035f83015261034381846102f3565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061038f57607f821691505b6020821081036103a2576103a161034b565b5b5091905056fea26469706673582212200eb6f59ca49bcaca2e053475392d2aca99e18fc25cc0b30e81436c83b1217c8d64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'STORAGE_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b5060043610610055575f3560e01c80631f457cb5146100595780633850c7bd146100775780634a9a010914610095578063924fe315146100b3578063d987e6b5146100d1575b5f5ffd5b6100616100ef565b60405161006e9190610230565b60405180910390f35b61007f6100f5565b60405161008c9190610230565b60405180910390f35b61009d6100fa565b6040516100aa91906102b9565b60405180910390f35b6100bb610186565b6040516100c8919061032b565b60405180910390f35b6100d9610212565b6040516100e69190610230565b60405180910390f35b60015481565b5f5481565b6004805461010790610378565b80601f016020809104026020016040519081016040528092919081815260200182805461013390610378565b801561017e5780601f106101555761010080835404028352916020019161017e565b820191905f5260205f20905b81548152906001019060200180831161016157829003601f168201915b505050505081565b6003805461019390610378565b80601f01602080910402602001604051908101604052809291908181526020018280546101bf90610378565b801561020a5780601f106101e15761010080835404028352916020019161020a565b820191905f5260205f20905b8154815290600101906020018083116101ed57829003601f168201915b505050505081565b60025481565b5f819050919050565b61022a81610218565b82525050565b5f6020820190506102435f830184610221565b92915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61028b82610249565b6102958185610253565b93506102a5818560208601610263565b6102ae81610271565b840191505092915050565b5f6020820190508181035f8301526102d18184610281565b905092915050565b5f81519050919050565b5f82825260208201905092915050565b5f6102fd826102d9565b61030781856102e3565b9350610317818560208601610263565b61032081610271565b840191505092915050565b5f6020820190508181035f83015261034381846102f3565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061038f57607f821691505b6020821081036103a2576103a161034b565b5b5091905056fea26469706673582212200eb6f59ca49bcaca2e053475392d2aca99e18fc25cc0b30e81436c83b1217c8d64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'STORAGE_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 11, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'name' */
    cpy_r_r18 = CPyStatics[10]; /* 'slot0' */
    cpy_r_r19 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r20 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r21 = CPyStatics[13]; /* 'int256' */
    cpy_r_r22 = CPyStatics[9]; /* 'name' */
    cpy_r_r23 = CPyStatics[14]; /* '' */
    cpy_r_r24 = CPyStatics[15]; /* 'type' */
    cpy_r_r25 = CPyStatics[13]; /* 'int256' */
    cpy_r_r26 = CPyDict_Build(3, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23, cpy_r_r24, cpy_r_r25);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL37;
    }
    cpy_r_r27 = PyList_New(1);
    if (unlikely(cpy_r_r27 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL38;
    }
    cpy_r_r28 = (CPyPtr)&((PyListObject *)cpy_r_r27)->ob_item;
    cpy_r_r29 = *(CPyPtr *)cpy_r_r28;
    *(PyObject * *)cpy_r_r29 = cpy_r_r26;
    cpy_r_r30 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r31 = CPyStatics[17]; /* 'view' */
    cpy_r_r32 = CPyStatics[15]; /* 'type' */
    cpy_r_r33 = CPyStatics[18]; /* 'function' */
    cpy_r_r34 = CPyDict_Build(5, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r27, cpy_r_r30, cpy_r_r31, cpy_r_r32, cpy_r_r33);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    CPy_DECREF_NO_IMM(cpy_r_r27);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r35 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r36 = PyList_New(0);
    if (unlikely(cpy_r_r36 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 18, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r37 = CPyStatics[9]; /* 'name' */
    cpy_r_r38 = CPyStatics[19]; /* 'slot1' */
    cpy_r_r39 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r40 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r41 = CPyStatics[13]; /* 'int256' */
    cpy_r_r42 = CPyStatics[9]; /* 'name' */
    cpy_r_r43 = CPyStatics[14]; /* '' */
    cpy_r_r44 = CPyStatics[15]; /* 'type' */
    cpy_r_r45 = CPyStatics[13]; /* 'int256' */
    cpy_r_r46 = CPyDict_Build(3, cpy_r_r40, cpy_r_r41, cpy_r_r42, cpy_r_r43, cpy_r_r44, cpy_r_r45);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL40;
    }
    cpy_r_r47 = PyList_New(1);
    if (unlikely(cpy_r_r47 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 20, CPyStatic_globals);
        goto CPyL41;
    }
    cpy_r_r48 = (CPyPtr)&((PyListObject *)cpy_r_r47)->ob_item;
    cpy_r_r49 = *(CPyPtr *)cpy_r_r48;
    *(PyObject * *)cpy_r_r49 = cpy_r_r46;
    cpy_r_r50 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r51 = CPyStatics[17]; /* 'view' */
    cpy_r_r52 = CPyStatics[15]; /* 'type' */
    cpy_r_r53 = CPyStatics[18]; /* 'function' */
    cpy_r_r54 = CPyDict_Build(5, cpy_r_r35, cpy_r_r36, cpy_r_r37, cpy_r_r38, cpy_r_r39, cpy_r_r47, cpy_r_r50, cpy_r_r51, cpy_r_r52, cpy_r_r53);
    CPy_DECREF_NO_IMM(cpy_r_r36);
    CPy_DECREF_NO_IMM(cpy_r_r47);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 17, CPyStatic_globals);
        goto CPyL39;
    }
    cpy_r_r55 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r56 = PyList_New(0);
    if (unlikely(cpy_r_r56 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 25, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r57 = CPyStatics[9]; /* 'name' */
    cpy_r_r58 = CPyStatics[20]; /* 'slot2' */
    cpy_r_r59 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r60 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r61 = CPyStatics[13]; /* 'int256' */
    cpy_r_r62 = CPyStatics[9]; /* 'name' */
    cpy_r_r63 = CPyStatics[14]; /* '' */
    cpy_r_r64 = CPyStatics[15]; /* 'type' */
    cpy_r_r65 = CPyStatics[13]; /* 'int256' */
    cpy_r_r66 = CPyDict_Build(3, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64, cpy_r_r65);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 27, CPyStatic_globals);
        goto CPyL43;
    }
    cpy_r_r67 = PyList_New(1);
    if (unlikely(cpy_r_r67 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 27, CPyStatic_globals);
        goto CPyL44;
    }
    cpy_r_r68 = (CPyPtr)&((PyListObject *)cpy_r_r67)->ob_item;
    cpy_r_r69 = *(CPyPtr *)cpy_r_r68;
    *(PyObject * *)cpy_r_r69 = cpy_r_r66;
    cpy_r_r70 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r71 = CPyStatics[17]; /* 'view' */
    cpy_r_r72 = CPyStatics[15]; /* 'type' */
    cpy_r_r73 = CPyStatics[18]; /* 'function' */
    cpy_r_r74 = CPyDict_Build(5, cpy_r_r55, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r67, cpy_r_r70, cpy_r_r71, cpy_r_r72, cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r56);
    CPy_DECREF_NO_IMM(cpy_r_r67);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 24, CPyStatic_globals);
        goto CPyL42;
    }
    cpy_r_r75 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r76 = PyList_New(0);
    if (unlikely(cpy_r_r76 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 32, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r77 = CPyStatics[9]; /* 'name' */
    cpy_r_r78 = CPyStatics[21]; /* 'slot3' */
    cpy_r_r79 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r80 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r81 = CPyStatics[22]; /* 'string' */
    cpy_r_r82 = CPyStatics[9]; /* 'name' */
    cpy_r_r83 = CPyStatics[14]; /* '' */
    cpy_r_r84 = CPyStatics[15]; /* 'type' */
    cpy_r_r85 = CPyStatics[22]; /* 'string' */
    cpy_r_r86 = CPyDict_Build(3, cpy_r_r80, cpy_r_r81, cpy_r_r82, cpy_r_r83, cpy_r_r84, cpy_r_r85);
    if (unlikely(cpy_r_r86 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 34, CPyStatic_globals);
        goto CPyL46;
    }
    cpy_r_r87 = PyList_New(1);
    if (unlikely(cpy_r_r87 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 34, CPyStatic_globals);
        goto CPyL47;
    }
    cpy_r_r88 = (CPyPtr)&((PyListObject *)cpy_r_r87)->ob_item;
    cpy_r_r89 = *(CPyPtr *)cpy_r_r88;
    *(PyObject * *)cpy_r_r89 = cpy_r_r86;
    cpy_r_r90 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r91 = CPyStatics[17]; /* 'view' */
    cpy_r_r92 = CPyStatics[15]; /* 'type' */
    cpy_r_r93 = CPyStatics[18]; /* 'function' */
    cpy_r_r94 = CPyDict_Build(5, cpy_r_r75, cpy_r_r76, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r87, cpy_r_r90, cpy_r_r91, cpy_r_r92, cpy_r_r93);
    CPy_DECREF_NO_IMM(cpy_r_r76);
    CPy_DECREF_NO_IMM(cpy_r_r87);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 31, CPyStatic_globals);
        goto CPyL45;
    }
    cpy_r_r95 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r96 = PyList_New(0);
    if (unlikely(cpy_r_r96 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 39, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r97 = CPyStatics[9]; /* 'name' */
    cpy_r_r98 = CPyStatics[23]; /* 'slot4' */
    cpy_r_r99 = CPyStatics[11]; /* 'outputs' */
    cpy_r_r100 = CPyStatics[12]; /* 'internalType' */
    cpy_r_r101 = CPyStatics[24]; /* 'bytes' */
    cpy_r_r102 = CPyStatics[9]; /* 'name' */
    cpy_r_r103 = CPyStatics[14]; /* '' */
    cpy_r_r104 = CPyStatics[15]; /* 'type' */
    cpy_r_r105 = CPyStatics[24]; /* 'bytes' */
    cpy_r_r106 = CPyDict_Build(3, cpy_r_r100, cpy_r_r101, cpy_r_r102, cpy_r_r103, cpy_r_r104, cpy_r_r105);
    if (unlikely(cpy_r_r106 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL49;
    }
    cpy_r_r107 = PyList_New(1);
    if (unlikely(cpy_r_r107 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 41, CPyStatic_globals);
        goto CPyL50;
    }
    cpy_r_r108 = (CPyPtr)&((PyListObject *)cpy_r_r107)->ob_item;
    cpy_r_r109 = *(CPyPtr *)cpy_r_r108;
    *(PyObject * *)cpy_r_r109 = cpy_r_r106;
    cpy_r_r110 = CPyStatics[16]; /* 'stateMutability' */
    cpy_r_r111 = CPyStatics[17]; /* 'view' */
    cpy_r_r112 = CPyStatics[15]; /* 'type' */
    cpy_r_r113 = CPyStatics[18]; /* 'function' */
    cpy_r_r114 = CPyDict_Build(5, cpy_r_r95, cpy_r_r96, cpy_r_r97, cpy_r_r98, cpy_r_r99, cpy_r_r107, cpy_r_r110, cpy_r_r111, cpy_r_r112, cpy_r_r113);
    CPy_DECREF_NO_IMM(cpy_r_r96);
    CPy_DECREF_NO_IMM(cpy_r_r107);
    if (unlikely(cpy_r_r114 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL48;
    }
    cpy_r_r115 = PyList_New(5);
    if (unlikely(cpy_r_r115 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL51;
    }
    cpy_r_r116 = (CPyPtr)&((PyListObject *)cpy_r_r115)->ob_item;
    cpy_r_r117 = *(CPyPtr *)cpy_r_r116;
    *(PyObject * *)cpy_r_r117 = cpy_r_r34;
    cpy_r_r118 = cpy_r_r117 + 8;
    *(PyObject * *)cpy_r_r118 = cpy_r_r54;
    cpy_r_r119 = cpy_r_r117 + 16;
    *(PyObject * *)cpy_r_r119 = cpy_r_r74;
    cpy_r_r120 = cpy_r_r117 + 24;
    *(PyObject * *)cpy_r_r120 = cpy_r_r94;
    cpy_r_r121 = cpy_r_r117 + 32;
    *(PyObject * *)cpy_r_r121 = cpy_r_r114;
    cpy_r_r122 = CPyStatic_globals;
    cpy_r_r123 = CPyStatics[25]; /* 'STORAGE_CONTRACT_ABI' */
    cpy_r_r124 = CPyDict_SetItem(cpy_r_r122, cpy_r_r123, cpy_r_r115);
    CPy_DECREF_NO_IMM(cpy_r_r115);
    cpy_r_r125 = cpy_r_r124 >= 0;
    if (unlikely(!cpy_r_r125)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r126 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r127 = CPyStatic_globals;
    cpy_r_r128 = CPyStatics[5]; /* 'STORAGE_CONTRACT_BYTECODE' */
    cpy_r_r129 = CPyDict_GetItem(cpy_r_r127, cpy_r_r128);
    if (unlikely(cpy_r_r129 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 47, CPyStatic_globals);
        goto CPyL36;
    }
    if (likely(PyUnicode_Check(cpy_r_r129)))
        cpy_r_r130 = cpy_r_r129;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 47, CPyStatic_globals, "str", cpy_r_r129);
        goto CPyL36;
    }
    cpy_r_r131 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r132 = CPyStatic_globals;
    cpy_r_r133 = CPyStatics[7]; /* 'STORAGE_CONTRACT_RUNTIME' */
    cpy_r_r134 = CPyDict_GetItem(cpy_r_r132, cpy_r_r133);
    if (unlikely(cpy_r_r134 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL52;
    }
    if (likely(PyUnicode_Check(cpy_r_r134)))
        cpy_r_r135 = cpy_r_r134;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 48, CPyStatic_globals, "str", cpy_r_r134);
        goto CPyL52;
    }
    cpy_r_r136 = CPyStatics[28]; /* 'abi' */
    cpy_r_r137 = CPyStatic_globals;
    cpy_r_r138 = CPyStatics[25]; /* 'STORAGE_CONTRACT_ABI' */
    cpy_r_r139 = CPyDict_GetItem(cpy_r_r137, cpy_r_r138);
    if (unlikely(cpy_r_r139 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 49, CPyStatic_globals);
        goto CPyL53;
    }
    if (likely(PyList_Check(cpy_r_r139)))
        cpy_r_r140 = cpy_r_r139;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 49, CPyStatic_globals, "list", cpy_r_r139);
        goto CPyL53;
    }
    cpy_r_r141 = CPyDict_Build(3, cpy_r_r126, cpy_r_r130, cpy_r_r131, cpy_r_r135, cpy_r_r136, cpy_r_r140);
    CPy_DECREF(cpy_r_r130);
    CPy_DECREF(cpy_r_r135);
    CPy_DECREF_NO_IMM(cpy_r_r140);
    if (unlikely(cpy_r_r141 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 46, CPyStatic_globals);
        goto CPyL36;
    }
    cpy_r_r142 = CPyStatic_globals;
    cpy_r_r143 = CPyStatics[29]; /* 'STORAGE_CONTRACT_DATA' */
    cpy_r_r144 = CPyDict_SetItem(cpy_r_r142, cpy_r_r143, cpy_r_r141);
    CPy_DECREF(cpy_r_r141);
    cpy_r_r145 = cpy_r_r144 >= 0;
    if (unlikely(!cpy_r_r145)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/storage_contract.py", "<module>", 46, CPyStatic_globals);
        goto CPyL36;
    }
    return 1;
CPyL36: ;
    cpy_r_r146 = 2;
    return cpy_r_r146;
CPyL37: ;
    CPy_DecRef(cpy_r_r16);
    goto CPyL36;
CPyL38: ;
    CPy_DecRef(cpy_r_r16);
    CPy_DecRef(cpy_r_r26);
    goto CPyL36;
CPyL39: ;
    CPy_DecRef(cpy_r_r34);
    goto CPyL36;
CPyL40: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r36);
    goto CPyL36;
CPyL41: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r36);
    CPy_DecRef(cpy_r_r46);
    goto CPyL36;
CPyL42: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    goto CPyL36;
CPyL43: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r56);
    goto CPyL36;
CPyL44: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r56);
    CPy_DecRef(cpy_r_r66);
    goto CPyL36;
CPyL45: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    goto CPyL36;
CPyL46: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r76);
    goto CPyL36;
CPyL47: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r76);
    CPy_DecRef(cpy_r_r86);
    goto CPyL36;
CPyL48: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r94);
    goto CPyL36;
CPyL49: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r94);
    CPy_DecRef(cpy_r_r96);
    goto CPyL36;
CPyL50: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r94);
    CPy_DecRef(cpy_r_r96);
    CPy_DecRef(cpy_r_r106);
    goto CPyL36;
CPyL51: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r94);
    CPy_DecRef(cpy_r_r114);
    goto CPyL36;
CPyL52: ;
    CPy_DecRef(cpy_r_r130);
    goto CPyL36;
CPyL53: ;
    CPy_DecRef(cpy_r_r130);
    CPy_DecRef(cpy_r_r135);
    goto CPyL36;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[30];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\243&0x60806040525f5f5560018055600280556040518060400160405280600581526020017f74687265650000000000000000000000000000000000000000000000000000008152506003908161005391906102e7565b506040518060400160405280600481526020017f666f757200000000000000000000000000000000000000000000000000000000815250600490816100989190610418565b503480156100a4575f5ffd5b506104e7565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061012557607f821691505b602082108103610138576101376100e1565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261019a7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8261015f565b6101a4868361015f565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f6101e86101e36101de846101bc565b6101c5565b6101bc565b9050919050565b5f819050919050565b610201836101ce565b61021561020d826101ef565b84845461016b565b825550505050565b5f5f905090565b61022c61021d565b6102378184846101f8565b505050565b5b8181101561025a5761024f5f82610224565b60018101905061023d565b5050565b601f82111561029f576102708161013e565b61027984610150565b81016020851015610288578190505b61029c61029485610150565b83018261023c565b50505b505050565b5f82821c905092915050565b5f6102bf5f19846008026102a4565b1980831691505092915050565b5f6102d783836102b0565b9150826002028217905092915050565b6102f0826100aa565b67ffffffffffffffff811115610309576103086100b4565b5b610313825461010e565b61031e82828561025e565b5f60209050601f83116001811461034f575f841561033d578287015190505b61034785826102cc565b8655506103ae565b601f19841661035d8661013e565b5f5b828110156103845784890151825560018201915060208501945060208101905061035f565b868310156103a1578489015161039d601f8916826102b0565b8355505b6001600288020188555050505b505050505050565b5f81519050919050565b5f819050815f5260205f209050919050565b601f821115610413576103e4816103c0565b6103ed84610150565b810160208510156103fc578190505b61041061040885610150565b83018261023c565b50505b505050565b610421826103b6565b67ffffffffffffffff81111561043a576104396100b4565b5b610444825461010e565b61044f8282856103d2565b5f60209050601f831160018114610480575f841561046e578287015190505b61047885826102cc565b8655506104df565b601f19841661048e866103c0565b5f5b828110156104b557848901518255600182019150602085019450602081019050610490565b868310156104d257848901516104ce601f8916826102b0565b8355505b6001600288020188555050505b505050505050565b6103de806104f45f395ff3fe608060405234801561000f575f5ffd5b5060043610610055575f3560e01c80631f457cb5146100595780633850c7bd146100775780634a9a010914610095578063924fe315146100b3578063d987e6b5146100d1575b5f5ffd5b6100616100ef565b60405161006e9190610230565b60405180910390f35b61007f6100f5565b60405161008c9190610230565b60405180910390f35b61009d6100fa565b6040516100aa91906102b9565b60405180910390f35b6100bb610186565b6040516100c8919061032b565b60405180910390f35b6100d9610212565b6040516100e69190610230565b60405180910390f35b60015481565b5f5481565b6004805461010790610378565b80601f016020809104026020016040519081016040528092919081815260200182805461013390610378565b801561017e5780601f106101555761010080835404028352916020019161017e565b820191905f5260205f20905b81548152906001019060200180831161016157829003601f168201915b505050505081565b6003805461019390610378565b80601f01602080910402602001604051908101604052809291908181526020018280546101bf90610378565b801561020a5780601f106101e15761010080835404028352916020019161020a565b820191905f5260205f20905b8154815290600101906020018083116101ed57829003601f168201915b505050505081565b60025481565b5f819050919050565b61022a81610218565b82525050565b5f6020820190506102435f830184610221565b92915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61028b82610249565b6102958185610253565b93506102a5818560208601610263565b6102ae81610271565b840191505092915050565b5f6020820190508181035f8301526102d18184610281565b905092915050565b5f81519050919050565b5f82825260208201905092915050565b5f6102fd826102d9565b61030781856102e3565b9350610317818560208601610263565b61032081610271565b840191505092915050565b5f6020820190508181035f83015261034381846102f3565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061038f57607f821691505b6020821081036103a2576103a161034b565b5b5091905056fea26469706673582212200eb6f59ca49bcaca2e053475392d2aca99e18fc25cc0b30e81436c83b1217c8d64736f6c634300081e0033",
    "\001\031STORAGE_CONTRACT_BYTECODE",
    "\001\217>0x608060405234801561000f575f5ffd5b5060043610610055575f3560e01c80631f457cb5146100595780633850c7bd146100775780634a9a010914610095578063924fe315146100b3578063d987e6b5146100d1575b5f5ffd5b6100616100ef565b60405161006e9190610230565b60405180910390f35b61007f6100f5565b60405161008c9190610230565b60405180910390f35b61009d6100fa565b6040516100aa91906102b9565b60405180910390f35b6100bb610186565b6040516100c8919061032b565b60405180910390f35b6100d9610212565b6040516100e69190610230565b60405180910390f35b60015481565b5f5481565b6004805461010790610378565b80601f016020809104026020016040519081016040528092919081815260200182805461013390610378565b801561017e5780601f106101555761010080835404028352916020019161017e565b820191905f5260205f20905b81548152906001019060200180831161016157829003601f168201915b505050505081565b6003805461019390610378565b80601f01602080910402602001604051908101604052809291908181526020018280546101bf90610378565b801561020a5780601f106101e15761010080835404028352916020019161020a565b820191905f5260205f20905b8154815290600101906020018083116101ed57829003601f168201915b505050505081565b60025481565b5f819050919050565b61022a81610218565b82525050565b5f6020820190506102435f830184610221565b92915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f61028b82610249565b6102958185610253565b93506102a5818560208601610263565b6102ae81610271565b840191505092915050565b5f6020820190508181035f8301526102d18184610281565b905092915050565b5f81519050919050565b5f82825260208201905092915050565b5f6102fd826102d9565b61030781856102e3565b9350610317818560208601610263565b61032081610271565b840191505092915050565b5f6020820190508181035f83015261034381846102f3565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f600282049050600182168061038f57607f821691505b6020821081036103a2576103a161034b565b5b5091905056fea26469706673582212200eb6f59ca49bcaca2e053475392d2aca99e18fc25cc0b30e81436c83b1217c8d64736f6c634300081e0033",
    "\006\030STORAGE_CONTRACT_RUNTIME\006inputs\004name\005slot0\aoutputs\finternalType",
    "\n\006int256\000\004type\017stateMutability\004view\bfunction\005slot1\005slot2\005slot3\006string",
    "\006\005slot4\005bytes\024STORAGE_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi",
    "\001\025STORAGE_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___storage_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_storage_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___storage_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___storage_contract, "faster_web3._utils.contract_sources.contract_data.storage_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___storage_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___storage_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_storage_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.storage_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_storage_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_storage_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_storage_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
