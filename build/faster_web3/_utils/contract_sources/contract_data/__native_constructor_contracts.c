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
#include "__native_constructor_contracts.h"
#include "__native_internal_constructor_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___constructor_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.constructor_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___constructor_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___constructor_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal;
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
    CPyPtr cpy_r_r23;
    CPyPtr cpy_r_r24;
    PyObject *cpy_r_r25;
    PyObject *cpy_r_r26;
    int32_t cpy_r_r27;
    char cpy_r_r28;
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
    int32_t cpy_r_r47;
    char cpy_r_r48;
    PyObject *cpy_r_r49;
    PyObject *cpy_r_r50;
    PyObject *cpy_r_r51;
    int32_t cpy_r_r52;
    char cpy_r_r53;
    PyObject *cpy_r_r54;
    PyObject *cpy_r_r55;
    PyObject *cpy_r_r56;
    int32_t cpy_r_r57;
    char cpy_r_r58;
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
    PyObject *cpy_r_r92;
    PyObject *cpy_r_r93;
    PyObject *cpy_r_r94;
    PyObject *cpy_r_r95;
    CPyPtr cpy_r_r96;
    CPyPtr cpy_r_r97;
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
    CPyPtr cpy_r_r116;
    CPyPtr cpy_r_r117;
    PyObject *cpy_r_r118;
    PyObject *cpy_r_r119;
    PyObject *cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    CPyPtr cpy_r_r124;
    CPyPtr cpy_r_r125;
    CPyPtr cpy_r_r126;
    CPyPtr cpy_r_r127;
    PyObject *cpy_r_r128;
    PyObject *cpy_r_r129;
    int32_t cpy_r_r130;
    char cpy_r_r131;
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
    int32_t cpy_r_r150;
    char cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
    int32_t cpy_r_r155;
    char cpy_r_r156;
    PyObject *cpy_r_r157;
    PyObject *cpy_r_r158;
    PyObject *cpy_r_r159;
    int32_t cpy_r_r160;
    char cpy_r_r161;
    PyObject *cpy_r_r162;
    PyObject *cpy_r_r163;
    PyObject *cpy_r_r164;
    PyObject *cpy_r_r165;
    PyObject *cpy_r_r166;
    PyObject *cpy_r_r167;
    PyObject *cpy_r_r168;
    PyObject *cpy_r_r169;
    PyObject *cpy_r_r170;
    CPyPtr cpy_r_r171;
    CPyPtr cpy_r_r172;
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
    PyObject *cpy_r_r186;
    PyObject *cpy_r_r187;
    PyObject *cpy_r_r188;
    PyObject *cpy_r_r189;
    PyObject *cpy_r_r190;
    CPyPtr cpy_r_r191;
    CPyPtr cpy_r_r192;
    PyObject *cpy_r_r193;
    PyObject *cpy_r_r194;
    PyObject *cpy_r_r195;
    PyObject *cpy_r_r196;
    PyObject *cpy_r_r197;
    PyObject *cpy_r_r198;
    CPyPtr cpy_r_r199;
    CPyPtr cpy_r_r200;
    CPyPtr cpy_r_r201;
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
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL61;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b50603e80601a5f395ff3fe60806040525f5ffdfea26469706673582212209e191fa382f12b19b6452b5f4a2aa0219b128737733ec839fa9a00044a51a5b264736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 7, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x60806040525f5ffdfea26469706673582212209e191fa382f12b19b6452b5f4a2aa0219b128737733ec839fa9a00044a51a5b264736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 8, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r16 = PyList_New(0);
    if (unlikely(cpy_r_r16 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r17 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r18 = CPyStatics[10]; /* 'nonpayable' */
    cpy_r_r19 = CPyStatics[11]; /* 'type' */
    cpy_r_r20 = CPyStatics[12]; /* 'constructor' */
    cpy_r_r21 = CPyDict_Build(3, cpy_r_r15, cpy_r_r16, cpy_r_r17, cpy_r_r18, cpy_r_r19, cpy_r_r20);
    CPy_DECREF_NO_IMM(cpy_r_r16);
    if (unlikely(cpy_r_r21 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r22 = PyList_New(1);
    if (unlikely(cpy_r_r22 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL62;
    }
    cpy_r_r23 = (CPyPtr)&((PyListObject *)cpy_r_r22)->ob_item;
    cpy_r_r24 = *(CPyPtr *)cpy_r_r23;
    *(PyObject * *)cpy_r_r24 = cpy_r_r21;
    cpy_r_r25 = CPyStatic_globals;
    cpy_r_r26 = CPyStatics[13]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_ABI' */
    cpy_r_r27 = CPyDict_SetItem(cpy_r_r25, cpy_r_r26, cpy_r_r22);
    CPy_DECREF_NO_IMM(cpy_r_r22);
    cpy_r_r28 = cpy_r_r27 >= 0;
    if (unlikely(!cpy_r_r28)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r29 = CPyStatics[14]; /* 'bytecode' */
    cpy_r_r30 = CPyStatic_globals;
    cpy_r_r31 = CPyStatics[5]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE' */
    cpy_r_r32 = CPyDict_GetItem(cpy_r_r30, cpy_r_r31);
    if (unlikely(cpy_r_r32 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 13, CPyStatic_globals);
        goto CPyL61;
    }
    if (likely(PyUnicode_Check(cpy_r_r32)))
        cpy_r_r33 = cpy_r_r32;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 13, CPyStatic_globals, "str", cpy_r_r32);
        goto CPyL61;
    }
    cpy_r_r34 = CPyStatics[15]; /* 'bytecode_runtime' */
    cpy_r_r35 = CPyStatic_globals;
    cpy_r_r36 = CPyStatics[7]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME' */
    cpy_r_r37 = CPyDict_GetItem(cpy_r_r35, cpy_r_r36);
    if (unlikely(cpy_r_r37 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 14, CPyStatic_globals);
        goto CPyL63;
    }
    if (likely(PyUnicode_Check(cpy_r_r37)))
        cpy_r_r38 = cpy_r_r37;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 14, CPyStatic_globals, "str", cpy_r_r37);
        goto CPyL63;
    }
    cpy_r_r39 = CPyStatics[16]; /* 'abi' */
    cpy_r_r40 = CPyStatic_globals;
    cpy_r_r41 = CPyStatics[13]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_ABI' */
    cpy_r_r42 = CPyDict_GetItem(cpy_r_r40, cpy_r_r41);
    if (unlikely(cpy_r_r42 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 15, CPyStatic_globals);
        goto CPyL64;
    }
    if (likely(PyList_Check(cpy_r_r42)))
        cpy_r_r43 = cpy_r_r42;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 15, CPyStatic_globals, "list", cpy_r_r42);
        goto CPyL64;
    }
    cpy_r_r44 = CPyDict_Build(3, cpy_r_r29, cpy_r_r33, cpy_r_r34, cpy_r_r38, cpy_r_r39, cpy_r_r43);
    CPy_DECREF(cpy_r_r33);
    CPy_DECREF(cpy_r_r38);
    CPy_DECREF_NO_IMM(cpy_r_r43);
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 12, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r45 = CPyStatic_globals;
    cpy_r_r46 = CPyStatics[17]; /* 'SIMPLE_CONSTRUCTOR_CONTRACT_DATA' */
    cpy_r_r47 = CPyDict_SetItem(cpy_r_r45, cpy_r_r46, cpy_r_r44);
    CPy_DECREF(cpy_r_r44);
    cpy_r_r48 = cpy_r_r47 >= 0;
    if (unlikely(!cpy_r_r48)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 12, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r49 = CPyStatics[18]; /* '0x6080604052348015600e575f5ffd5b506040516101e83803806101e88339818101604052810190602e919060a1565b815f8190555080600181905550505060d8565b5f5ffd5b5f819050919050565b6055816045565b8114605e575f5ffd5b50565b5f81519050606d81604e565b92915050565b5f819050919050565b6083816073565b8114608c575f5ffd5b50565b5f81519050609b81607c565b92915050565b5f5f6040838503121560b45760b36041565b5b5f60bf858286016061565b925050602060ce85828601608f565b9150509250929050565b610103806100e55f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f5ffd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea26469706673582212207d403d1908a2cf17f2230e67186cf271a4264a5fa23cebf6bb111ac4ff68fb4964736f6c634300081e0033' */
    cpy_r_r50 = CPyStatic_globals;
    cpy_r_r51 = CPyStatics[19]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE' */
    cpy_r_r52 = CPyDict_SetItem(cpy_r_r50, cpy_r_r51, cpy_r_r49);
    cpy_r_r53 = cpy_r_r52 >= 0;
    if (unlikely(!cpy_r_r53)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 20, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r54 = CPyStatics[20]; /* '0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f5ffd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea26469706673582212207d403d1908a2cf17f2230e67186cf271a4264a5fa23cebf6bb111ac4ff68fb4964736f6c634300081e0033' */
    cpy_r_r55 = CPyStatic_globals;
    cpy_r_r56 = CPyStatics[21]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME' */
    cpy_r_r57 = CPyDict_SetItem(cpy_r_r55, cpy_r_r56, cpy_r_r54);
    cpy_r_r58 = cpy_r_r57 >= 0;
    if (unlikely(!cpy_r_r58)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 21, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r59 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r60 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r61 = CPyStatics[23]; /* 'uint256' */
    cpy_r_r62 = CPyStatics[24]; /* 'name' */
    cpy_r_r63 = CPyStatics[25]; /* 'a' */
    cpy_r_r64 = CPyStatics[11]; /* 'type' */
    cpy_r_r65 = CPyStatics[23]; /* 'uint256' */
    cpy_r_r66 = CPyDict_Build(3, cpy_r_r60, cpy_r_r61, cpy_r_r62, cpy_r_r63, cpy_r_r64, cpy_r_r65);
    if (unlikely(cpy_r_r66 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r67 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r68 = CPyStatics[26]; /* 'bytes32' */
    cpy_r_r69 = CPyStatics[24]; /* 'name' */
    cpy_r_r70 = CPyStatics[27]; /* 'b' */
    cpy_r_r71 = CPyStatics[11]; /* 'type' */
    cpy_r_r72 = CPyStatics[26]; /* 'bytes32' */
    cpy_r_r73 = CPyDict_Build(3, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72);
    if (unlikely(cpy_r_r73 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 26, CPyStatic_globals);
        goto CPyL65;
    }
    cpy_r_r74 = PyList_New(2);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 24, CPyStatic_globals);
        goto CPyL66;
    }
    cpy_r_r75 = (CPyPtr)&((PyListObject *)cpy_r_r74)->ob_item;
    cpy_r_r76 = *(CPyPtr *)cpy_r_r75;
    *(PyObject * *)cpy_r_r76 = cpy_r_r66;
    cpy_r_r77 = cpy_r_r76 + 8;
    *(PyObject * *)cpy_r_r77 = cpy_r_r73;
    cpy_r_r78 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r79 = CPyStatics[10]; /* 'nonpayable' */
    cpy_r_r80 = CPyStatics[11]; /* 'type' */
    cpy_r_r81 = CPyStatics[12]; /* 'constructor' */
    cpy_r_r82 = CPyDict_Build(3, cpy_r_r59, cpy_r_r74, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81);
    CPy_DECREF_NO_IMM(cpy_r_r74);
    if (unlikely(cpy_r_r82 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 23, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r83 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r84 = PyList_New(0);
    if (unlikely(cpy_r_r84 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 32, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r85 = CPyStatics[24]; /* 'name' */
    cpy_r_r86 = CPyStatics[28]; /* 'data_a' */
    cpy_r_r87 = CPyStatics[29]; /* 'outputs' */
    cpy_r_r88 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r89 = CPyStatics[23]; /* 'uint256' */
    cpy_r_r90 = CPyStatics[24]; /* 'name' */
    cpy_r_r91 = CPyStatics[30]; /* '' */
    cpy_r_r92 = CPyStatics[11]; /* 'type' */
    cpy_r_r93 = CPyStatics[23]; /* 'uint256' */
    cpy_r_r94 = CPyDict_Build(3, cpy_r_r88, cpy_r_r89, cpy_r_r90, cpy_r_r91, cpy_r_r92, cpy_r_r93);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 34, CPyStatic_globals);
        goto CPyL68;
    }
    cpy_r_r95 = PyList_New(1);
    if (unlikely(cpy_r_r95 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 34, CPyStatic_globals);
        goto CPyL69;
    }
    cpy_r_r96 = (CPyPtr)&((PyListObject *)cpy_r_r95)->ob_item;
    cpy_r_r97 = *(CPyPtr *)cpy_r_r96;
    *(PyObject * *)cpy_r_r97 = cpy_r_r94;
    cpy_r_r98 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r99 = CPyStatics[31]; /* 'view' */
    cpy_r_r100 = CPyStatics[11]; /* 'type' */
    cpy_r_r101 = CPyStatics[32]; /* 'function' */
    cpy_r_r102 = CPyDict_Build(5, cpy_r_r83, cpy_r_r84, cpy_r_r85, cpy_r_r86, cpy_r_r87, cpy_r_r95, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101);
    CPy_DECREF_NO_IMM(cpy_r_r84);
    CPy_DECREF_NO_IMM(cpy_r_r95);
    if (unlikely(cpy_r_r102 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 31, CPyStatic_globals);
        goto CPyL67;
    }
    cpy_r_r103 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r104 = PyList_New(0);
    if (unlikely(cpy_r_r104 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 39, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r105 = CPyStatics[24]; /* 'name' */
    cpy_r_r106 = CPyStatics[33]; /* 'data_b' */
    cpy_r_r107 = CPyStatics[29]; /* 'outputs' */
    cpy_r_r108 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r109 = CPyStatics[26]; /* 'bytes32' */
    cpy_r_r110 = CPyStatics[24]; /* 'name' */
    cpy_r_r111 = CPyStatics[30]; /* '' */
    cpy_r_r112 = CPyStatics[11]; /* 'type' */
    cpy_r_r113 = CPyStatics[26]; /* 'bytes32' */
    cpy_r_r114 = CPyDict_Build(3, cpy_r_r108, cpy_r_r109, cpy_r_r110, cpy_r_r111, cpy_r_r112, cpy_r_r113);
    if (unlikely(cpy_r_r114 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 41, CPyStatic_globals);
        goto CPyL71;
    }
    cpy_r_r115 = PyList_New(1);
    if (unlikely(cpy_r_r115 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 41, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r116 = (CPyPtr)&((PyListObject *)cpy_r_r115)->ob_item;
    cpy_r_r117 = *(CPyPtr *)cpy_r_r116;
    *(PyObject * *)cpy_r_r117 = cpy_r_r114;
    cpy_r_r118 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r119 = CPyStatics[31]; /* 'view' */
    cpy_r_r120 = CPyStatics[11]; /* 'type' */
    cpy_r_r121 = CPyStatics[32]; /* 'function' */
    cpy_r_r122 = CPyDict_Build(5, cpy_r_r103, cpy_r_r104, cpy_r_r105, cpy_r_r106, cpy_r_r107, cpy_r_r115, cpy_r_r118, cpy_r_r119, cpy_r_r120, cpy_r_r121);
    CPy_DECREF_NO_IMM(cpy_r_r104);
    CPy_DECREF_NO_IMM(cpy_r_r115);
    if (unlikely(cpy_r_r122 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 38, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r123 = PyList_New(3);
    if (unlikely(cpy_r_r123 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 22, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r124 = (CPyPtr)&((PyListObject *)cpy_r_r123)->ob_item;
    cpy_r_r125 = *(CPyPtr *)cpy_r_r124;
    *(PyObject * *)cpy_r_r125 = cpy_r_r82;
    cpy_r_r126 = cpy_r_r125 + 8;
    *(PyObject * *)cpy_r_r126 = cpy_r_r102;
    cpy_r_r127 = cpy_r_r125 + 16;
    *(PyObject * *)cpy_r_r127 = cpy_r_r122;
    cpy_r_r128 = CPyStatic_globals;
    cpy_r_r129 = CPyStatics[34]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI' */
    cpy_r_r130 = CPyDict_SetItem(cpy_r_r128, cpy_r_r129, cpy_r_r123);
    CPy_DECREF_NO_IMM(cpy_r_r123);
    cpy_r_r131 = cpy_r_r130 >= 0;
    if (unlikely(!cpy_r_r131)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 22, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r132 = CPyStatics[14]; /* 'bytecode' */
    cpy_r_r133 = CPyStatic_globals;
    cpy_r_r134 = CPyStatics[19]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE' */
    cpy_r_r135 = CPyDict_GetItem(cpy_r_r133, cpy_r_r134);
    if (unlikely(cpy_r_r135 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL61;
    }
    if (likely(PyUnicode_Check(cpy_r_r135)))
        cpy_r_r136 = cpy_r_r135;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 47, CPyStatic_globals, "str", cpy_r_r135);
        goto CPyL61;
    }
    cpy_r_r137 = CPyStatics[15]; /* 'bytecode_runtime' */
    cpy_r_r138 = CPyStatic_globals;
    cpy_r_r139 = CPyStatics[21]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME' */
    cpy_r_r140 = CPyDict_GetItem(cpy_r_r138, cpy_r_r139);
    if (unlikely(cpy_r_r140 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 48, CPyStatic_globals);
        goto CPyL74;
    }
    if (likely(PyUnicode_Check(cpy_r_r140)))
        cpy_r_r141 = cpy_r_r140;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 48, CPyStatic_globals, "str", cpy_r_r140);
        goto CPyL74;
    }
    cpy_r_r142 = CPyStatics[16]; /* 'abi' */
    cpy_r_r143 = CPyStatic_globals;
    cpy_r_r144 = CPyStatics[34]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI' */
    cpy_r_r145 = CPyDict_GetItem(cpy_r_r143, cpy_r_r144);
    if (unlikely(cpy_r_r145 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 49, CPyStatic_globals);
        goto CPyL75;
    }
    if (likely(PyList_Check(cpy_r_r145)))
        cpy_r_r146 = cpy_r_r145;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 49, CPyStatic_globals, "list", cpy_r_r145);
        goto CPyL75;
    }
    cpy_r_r147 = CPyDict_Build(3, cpy_r_r132, cpy_r_r136, cpy_r_r137, cpy_r_r141, cpy_r_r142, cpy_r_r146);
    CPy_DECREF(cpy_r_r136);
    CPy_DECREF(cpy_r_r141);
    CPy_DECREF_NO_IMM(cpy_r_r146);
    if (unlikely(cpy_r_r147 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 46, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r148 = CPyStatic_globals;
    cpy_r_r149 = CPyStatics[35]; /* 'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_DATA' */
    cpy_r_r150 = CPyDict_SetItem(cpy_r_r148, cpy_r_r149, cpy_r_r147);
    CPy_DECREF(cpy_r_r147);
    cpy_r_r151 = cpy_r_r150 >= 0;
    if (unlikely(!cpy_r_r151)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 46, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r152 = CPyStatics[36]; /* '0x608060405234801561000f575f5ffd5b506040516101fb3803806101fb833981810160405281019061003191906100d4565b805f5f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506100ff565b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b6100b381610099565b81146100bd575f5ffd5b50565b5f815190506100ce816100aa565b92915050565b5f602082840312156100e9576100e8610076565b5b5f6100f6848285016100c0565b91505092915050565b60f08061010b5f395ff3fe6080604052348015600e575f5ffd5b50600436106026575f3560e01c806334664e3a14602a575b5f5ffd5b60306044565b604051603b919060a3565b60405180910390f35b5f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608f826068565b9050919050565b609d816087565b82525050565b5f60208201905060b45f8301846096565b9291505056fea2646970667358221220d29806ab73246c53e77ade19f47279948e66b8efb71c14084c98c3d059ea35ee64736f6c634300081e0033' */
    cpy_r_r153 = CPyStatic_globals;
    cpy_r_r154 = CPyStatics[37]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE' */
    cpy_r_r155 = CPyDict_SetItem(cpy_r_r153, cpy_r_r154, cpy_r_r152);
    cpy_r_r156 = cpy_r_r155 >= 0;
    if (unlikely(!cpy_r_r156)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r157 = CPyStatics[38]; /* '0x6080604052348015600e575f5ffd5b50600436106026575f3560e01c806334664e3a14602a575b5f5ffd5b60306044565b604051603b919060a3565b60405180910390f35b5f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608f826068565b9050919050565b609d816087565b82525050565b5f60208201905060b45f8301846096565b9291505056fea2646970667358221220d29806ab73246c53e77ade19f47279948e66b8efb71c14084c98c3d059ea35ee64736f6c634300081e0033' */
    cpy_r_r158 = CPyStatic_globals;
    cpy_r_r159 = CPyStatics[39]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME' */
    cpy_r_r160 = CPyDict_SetItem(cpy_r_r158, cpy_r_r159, cpy_r_r157);
    cpy_r_r161 = cpy_r_r160 >= 0;
    if (unlikely(!cpy_r_r161)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 55, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r162 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r163 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r164 = CPyStatics[40]; /* 'address' */
    cpy_r_r165 = CPyStatics[24]; /* 'name' */
    cpy_r_r166 = CPyStatics[41]; /* '_testAddr' */
    cpy_r_r167 = CPyStatics[11]; /* 'type' */
    cpy_r_r168 = CPyStatics[40]; /* 'address' */
    cpy_r_r169 = CPyDict_Build(3, cpy_r_r163, cpy_r_r164, cpy_r_r165, cpy_r_r166, cpy_r_r167, cpy_r_r168);
    if (unlikely(cpy_r_r169 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 58, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r170 = PyList_New(1);
    if (unlikely(cpy_r_r170 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 58, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r171 = (CPyPtr)&((PyListObject *)cpy_r_r170)->ob_item;
    cpy_r_r172 = *(CPyPtr *)cpy_r_r171;
    *(PyObject * *)cpy_r_r172 = cpy_r_r169;
    cpy_r_r173 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r174 = CPyStatics[10]; /* 'nonpayable' */
    cpy_r_r175 = CPyStatics[11]; /* 'type' */
    cpy_r_r176 = CPyStatics[12]; /* 'constructor' */
    cpy_r_r177 = CPyDict_Build(3, cpy_r_r162, cpy_r_r170, cpy_r_r173, cpy_r_r174, cpy_r_r175, cpy_r_r176);
    CPy_DECREF_NO_IMM(cpy_r_r170);
    if (unlikely(cpy_r_r177 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r178 = CPyStatics[8]; /* 'inputs' */
    cpy_r_r179 = PyList_New(0);
    if (unlikely(cpy_r_r179 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 63, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r180 = CPyStatics[24]; /* 'name' */
    cpy_r_r181 = CPyStatics[42]; /* 'testAddr' */
    cpy_r_r182 = CPyStatics[29]; /* 'outputs' */
    cpy_r_r183 = CPyStatics[22]; /* 'internalType' */
    cpy_r_r184 = CPyStatics[40]; /* 'address' */
    cpy_r_r185 = CPyStatics[24]; /* 'name' */
    cpy_r_r186 = CPyStatics[30]; /* '' */
    cpy_r_r187 = CPyStatics[11]; /* 'type' */
    cpy_r_r188 = CPyStatics[40]; /* 'address' */
    cpy_r_r189 = CPyDict_Build(3, cpy_r_r183, cpy_r_r184, cpy_r_r185, cpy_r_r186, cpy_r_r187, cpy_r_r188);
    if (unlikely(cpy_r_r189 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 65, CPyStatic_globals);
        goto CPyL78;
    }
    cpy_r_r190 = PyList_New(1);
    if (unlikely(cpy_r_r190 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 65, CPyStatic_globals);
        goto CPyL79;
    }
    cpy_r_r191 = (CPyPtr)&((PyListObject *)cpy_r_r190)->ob_item;
    cpy_r_r192 = *(CPyPtr *)cpy_r_r191;
    *(PyObject * *)cpy_r_r192 = cpy_r_r189;
    cpy_r_r193 = CPyStatics[9]; /* 'stateMutability' */
    cpy_r_r194 = CPyStatics[31]; /* 'view' */
    cpy_r_r195 = CPyStatics[11]; /* 'type' */
    cpy_r_r196 = CPyStatics[32]; /* 'function' */
    cpy_r_r197 = CPyDict_Build(5, cpy_r_r178, cpy_r_r179, cpy_r_r180, cpy_r_r181, cpy_r_r182, cpy_r_r190, cpy_r_r193, cpy_r_r194, cpy_r_r195, cpy_r_r196);
    CPy_DECREF_NO_IMM(cpy_r_r179);
    CPy_DECREF_NO_IMM(cpy_r_r190);
    if (unlikely(cpy_r_r197 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 62, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r198 = PyList_New(2);
    if (unlikely(cpy_r_r198 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r199 = (CPyPtr)&((PyListObject *)cpy_r_r198)->ob_item;
    cpy_r_r200 = *(CPyPtr *)cpy_r_r199;
    *(PyObject * *)cpy_r_r200 = cpy_r_r177;
    cpy_r_r201 = cpy_r_r200 + 8;
    *(PyObject * *)cpy_r_r201 = cpy_r_r197;
    cpy_r_r202 = CPyStatic_globals;
    cpy_r_r203 = CPyStatics[43]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI' */
    cpy_r_r204 = CPyDict_SetItem(cpy_r_r202, cpy_r_r203, cpy_r_r198);
    CPy_DECREF_NO_IMM(cpy_r_r198);
    cpy_r_r205 = cpy_r_r204 >= 0;
    if (unlikely(!cpy_r_r205)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 56, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r206 = CPyStatics[14]; /* 'bytecode' */
    cpy_r_r207 = CPyStatic_globals;
    cpy_r_r208 = CPyStatics[37]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE' */
    cpy_r_r209 = CPyDict_GetItem(cpy_r_r207, cpy_r_r208);
    if (unlikely(cpy_r_r209 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 71, CPyStatic_globals);
        goto CPyL61;
    }
    if (likely(PyUnicode_Check(cpy_r_r209)))
        cpy_r_r210 = cpy_r_r209;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 71, CPyStatic_globals, "str", cpy_r_r209);
        goto CPyL61;
    }
    cpy_r_r211 = CPyStatics[15]; /* 'bytecode_runtime' */
    cpy_r_r212 = CPyStatic_globals;
    cpy_r_r213 = CPyStatics[39]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME' */
    cpy_r_r214 = CPyDict_GetItem(cpy_r_r212, cpy_r_r213);
    if (unlikely(cpy_r_r214 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 72, CPyStatic_globals);
        goto CPyL81;
    }
    if (likely(PyUnicode_Check(cpy_r_r214)))
        cpy_r_r215 = cpy_r_r214;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 72, CPyStatic_globals, "str", cpy_r_r214);
        goto CPyL81;
    }
    cpy_r_r216 = CPyStatics[16]; /* 'abi' */
    cpy_r_r217 = CPyStatic_globals;
    cpy_r_r218 = CPyStatics[43]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI' */
    cpy_r_r219 = CPyDict_GetItem(cpy_r_r217, cpy_r_r218);
    if (unlikely(cpy_r_r219 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 73, CPyStatic_globals);
        goto CPyL82;
    }
    if (likely(PyList_Check(cpy_r_r219)))
        cpy_r_r220 = cpy_r_r219;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 73, CPyStatic_globals, "list", cpy_r_r219);
        goto CPyL82;
    }
    cpy_r_r221 = CPyDict_Build(3, cpy_r_r206, cpy_r_r210, cpy_r_r211, cpy_r_r215, cpy_r_r216, cpy_r_r220);
    CPy_DECREF(cpy_r_r210);
    CPy_DECREF(cpy_r_r215);
    CPy_DECREF_NO_IMM(cpy_r_r220);
    if (unlikely(cpy_r_r221 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 70, CPyStatic_globals);
        goto CPyL61;
    }
    cpy_r_r222 = CPyStatic_globals;
    cpy_r_r223 = CPyStatics[44]; /* 'CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_DATA' */
    cpy_r_r224 = CPyDict_SetItem(cpy_r_r222, cpy_r_r223, cpy_r_r221);
    CPy_DECREF(cpy_r_r221);
    cpy_r_r225 = cpy_r_r224 >= 0;
    if (unlikely(!cpy_r_r225)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/constructor_contracts.py", "<module>", 70, CPyStatic_globals);
        goto CPyL61;
    }
    return 1;
CPyL61: ;
    cpy_r_r226 = 2;
    return cpy_r_r226;
CPyL62: ;
    CPy_DecRef(cpy_r_r21);
    goto CPyL61;
CPyL63: ;
    CPy_DecRef(cpy_r_r33);
    goto CPyL61;
CPyL64: ;
    CPy_DecRef(cpy_r_r33);
    CPy_DecRef(cpy_r_r38);
    goto CPyL61;
CPyL65: ;
    CPy_DecRef(cpy_r_r66);
    goto CPyL61;
CPyL66: ;
    CPy_DecRef(cpy_r_r66);
    CPy_DecRef(cpy_r_r73);
    goto CPyL61;
CPyL67: ;
    CPy_DecRef(cpy_r_r82);
    goto CPyL61;
CPyL68: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r84);
    goto CPyL61;
CPyL69: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r84);
    CPy_DecRef(cpy_r_r94);
    goto CPyL61;
CPyL70: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r102);
    goto CPyL61;
CPyL71: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r102);
    CPy_DecRef(cpy_r_r104);
    goto CPyL61;
CPyL72: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r102);
    CPy_DecRef(cpy_r_r104);
    CPy_DecRef(cpy_r_r114);
    goto CPyL61;
CPyL73: ;
    CPy_DecRef(cpy_r_r82);
    CPy_DecRef(cpy_r_r102);
    CPy_DecRef(cpy_r_r122);
    goto CPyL61;
CPyL74: ;
    CPy_DecRef(cpy_r_r136);
    goto CPyL61;
CPyL75: ;
    CPy_DecRef(cpy_r_r136);
    CPy_DecRef(cpy_r_r141);
    goto CPyL61;
CPyL76: ;
    CPy_DecRef(cpy_r_r169);
    goto CPyL61;
CPyL77: ;
    CPy_DecRef(cpy_r_r177);
    goto CPyL61;
CPyL78: ;
    CPy_DecRef(cpy_r_r177);
    CPy_DecRef(cpy_r_r179);
    goto CPyL61;
CPyL79: ;
    CPy_DecRef(cpy_r_r177);
    CPy_DecRef(cpy_r_r179);
    CPy_DecRef(cpy_r_r189);
    goto CPyL61;
CPyL80: ;
    CPy_DecRef(cpy_r_r177);
    CPy_DecRef(cpy_r_r197);
    goto CPyL61;
CPyL81: ;
    CPy_DecRef(cpy_r_r210);
    goto CPyL61;
CPyL82: ;
    CPy_DecRef(cpy_r_r210);
    CPy_DecRef(cpy_r_r215);
    goto CPyL61;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[45];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\20120x6080604052348015600e575f5ffd5b50603e80601a5f395ff3fe60806040525f5ffdfea26469706673582212209e191fa382f12b19b6452b5f4a2aa0219b128737733ec839fa9a00044a51a5b264736f6c634300081e0033",
    "\001$SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE",
    "\001~0x60806040525f5ffdfea26469706673582212209e191fa382f12b19b6452b5f4a2aa0219b128737733ec839fa9a00044a51a5b264736f6c634300081e0033",
    "\004#SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME\006inputs\017stateMutability\nnonpayable",
    "\004\004type\vconstructor\037SIMPLE_CONSTRUCTOR_CONTRACT_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi SIMPLE_CONSTRUCTOR_CONTRACT_DATA",
    "\001\207R0x6080604052348015600e575f5ffd5b506040516101e83803806101e88339818101604052810190602e919060a1565b815f8190555080600181905550505060d8565b5f5ffd5b5f819050919050565b6055816045565b8114605e575f5ffd5b50565b5f81519050606d81604e565b92915050565b5f819050919050565b6083816073565b8114608c575f5ffd5b50565b5f81519050609b81607c565b92915050565b5f5f6040838503121560b45760b36041565b5b5f60bf858286016061565b925050602060ce85828601608f565b9150509250929050565b610103806100e55f395ff3fe6080604052348015600e575f5ffd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f5ffd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea26469706673582212207d403d1908a2cf17f2230e67186cf271a4264a5fa23cebf6bb111ac4ff68fb4964736f6c634300081e0033",
    "\001,CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE",
    "\001\204\b0x6080604052348015600e575f5ffd5b50600436106030575f3560e01c806388ec1346146034578063d4c46c7614604e575b5f5ffd5b603a6068565b604051604591906089565b60405180910390f35b6054606d565b604051605f919060b6565b60405180910390f35b5f5481565b60015481565b5f819050919050565b6083816073565b82525050565b5f602082019050609a5f830184607c565b92915050565b5f819050919050565b60b08160a0565b82525050565b5f60208201905060c75f83018460a9565b9291505056fea26469706673582212207d403d1908a2cf17f2230e67186cf271a4264a5fa23cebf6bb111ac4ff68fb4964736f6c634300081e0033",
    "\004+CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME\finternalType\auint256\004name",
    "\t\001a\abytes32\001b\006data_a\aoutputs\000\004view\bfunction\006data_b",
    "\001\'CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI",
    "\001(CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_DATA",
    "\001\207x0x608060405234801561000f575f5ffd5b506040516101fb3803806101fb833981810160405281019061003191906100d4565b805f5f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506100ff565b5f5ffd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6100a38261007a565b9050919050565b6100b381610099565b81146100bd575f5ffd5b50565b5f815190506100ce816100aa565b92915050565b5f602082840312156100e9576100e8610076565b5b5f6100f6848285016100c0565b91505092915050565b60f08061010b5f395ff3fe6080604052348015600e575f5ffd5b50600436106026575f3560e01c806334664e3a14602a575b5f5ffd5b60306044565b604051603b919060a3565b60405180910390f35b5f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608f826068565b9050919050565b609d816087565b82525050565b5f60208201905060b45f8301846096565b9291505056fea2646970667358221220d29806ab73246c53e77ade19f47279948e66b8efb71c14084c98c3d059ea35ee64736f6c634300081e0033",
    "\0013CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE",
    "\001\203b0x6080604052348015600e575f5ffd5b50600436106026575f3560e01c806334664e3a14602a575b5f5ffd5b60306044565b604051603b919060a3565b60405180910390f35b5f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f608f826068565b9050919050565b609d816087565b82525050565b5f60208201905060b45f8301846096565b9291505056fea2646970667358221220d29806ab73246c53e77ade19f47279948e66b8efb71c14084c98c3d059ea35ee64736f6c634300081e0033",
    "\0032CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME\aaddress\t_testAddr",
    "\002\btestAddr.CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI",
    "\001/CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___constructor_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_constructor_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___constructor_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___constructor_contracts, "faster_web3._utils.contract_sources.contract_data.constructor_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___constructor_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___constructor_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_constructor_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.constructor_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_constructor_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_constructor_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_constructor_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
