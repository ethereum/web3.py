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
#include "__native_event_contracts.h"
#include "__native_internal_event_contracts.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___event_contracts(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.event_contracts",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___event_contracts(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___event_contracts(CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal;
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
    CPyPtr cpy_r_r47;
    CPyPtr cpy_r_r48;
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
    CPyPtr cpy_r_r126;
    CPyPtr cpy_r_r127;
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
    CPyPtr cpy_r_r146;
    CPyPtr cpy_r_r147;
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
    CPyPtr cpy_r_r175;
    CPyPtr cpy_r_r176;
    CPyPtr cpy_r_r177;
    CPyPtr cpy_r_r178;
    PyObject *cpy_r_r179;
    PyObject *cpy_r_r180;
    int32_t cpy_r_r181;
    char cpy_r_r182;
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
    PyObject *cpy_r_r196;
    PyObject *cpy_r_r197;
    PyObject *cpy_r_r198;
    PyObject *cpy_r_r199;
    PyObject *cpy_r_r200;
    int32_t cpy_r_r201;
    char cpy_r_r202;
    PyObject *cpy_r_r203;
    PyObject *cpy_r_r204;
    PyObject *cpy_r_r205;
    int32_t cpy_r_r206;
    char cpy_r_r207;
    PyObject *cpy_r_r208;
    PyObject *cpy_r_r209;
    PyObject *cpy_r_r210;
    int32_t cpy_r_r211;
    char cpy_r_r212;
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
    PyObject *cpy_r_r224;
    CPyPtr cpy_r_r225;
    CPyPtr cpy_r_r226;
    PyObject *cpy_r_r227;
    PyObject *cpy_r_r228;
    PyObject *cpy_r_r229;
    PyObject *cpy_r_r230;
    PyObject *cpy_r_r231;
    PyObject *cpy_r_r232;
    PyObject *cpy_r_r233;
    PyObject *cpy_r_r234;
    PyObject *cpy_r_r235;
    PyObject *cpy_r_r236;
    PyObject *cpy_r_r237;
    PyObject *cpy_r_r238;
    PyObject *cpy_r_r239;
    PyObject *cpy_r_r240;
    PyObject *cpy_r_r241;
    PyObject *cpy_r_r242;
    PyObject *cpy_r_r243;
    PyObject *cpy_r_r244;
    CPyPtr cpy_r_r245;
    CPyPtr cpy_r_r246;
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
    CPyPtr cpy_r_r262;
    CPyPtr cpy_r_r263;
    PyObject *cpy_r_r264;
    PyObject *cpy_r_r265;
    PyObject *cpy_r_r266;
    PyObject *cpy_r_r267;
    PyObject *cpy_r_r268;
    PyObject *cpy_r_r269;
    PyObject *cpy_r_r270;
    PyObject *cpy_r_r271;
    PyObject *cpy_r_r272;
    PyObject *cpy_r_r273;
    CPyPtr cpy_r_r274;
    CPyPtr cpy_r_r275;
    CPyPtr cpy_r_r276;
    CPyPtr cpy_r_r277;
    PyObject *cpy_r_r278;
    PyObject *cpy_r_r279;
    int32_t cpy_r_r280;
    char cpy_r_r281;
    PyObject *cpy_r_r282;
    PyObject *cpy_r_r283;
    PyObject *cpy_r_r284;
    PyObject *cpy_r_r285;
    PyObject *cpy_r_r286;
    PyObject *cpy_r_r287;
    PyObject *cpy_r_r288;
    PyObject *cpy_r_r289;
    PyObject *cpy_r_r290;
    PyObject *cpy_r_r291;
    PyObject *cpy_r_r292;
    PyObject *cpy_r_r293;
    PyObject *cpy_r_r294;
    PyObject *cpy_r_r295;
    PyObject *cpy_r_r296;
    PyObject *cpy_r_r297;
    PyObject *cpy_r_r298;
    PyObject *cpy_r_r299;
    int32_t cpy_r_r300;
    char cpy_r_r301;
    char cpy_r_r302;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", -1, CPyStatic_globals);
        goto CPyL70;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b5061017a8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea264697066735822122024dd83d4ed45a24e04cc3847bf220951b8e223a67484b966cda4cedca6223a0564736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'EVENT_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 7, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea264697066735822122024dd83d4ed45a24e04cc3847bf220951b8e223a67484b966cda4cedca6223a0564736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'EVENT_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 8, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r16 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r17 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r18 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r19 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r20 = CPyStatics[13]; /* 'name' */
    cpy_r_r21 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r22 = CPyStatics[15]; /* 'type' */
    cpy_r_r23 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r24 = 0 ? Py_True : Py_False;
    cpy_r_r25 = CPyDict_Build(4, cpy_r_r17, cpy_r_r24, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 13, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r26 = PyList_New(1);
    if (unlikely(cpy_r_r26 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 12, CPyStatic_globals);
        goto CPyL71;
    }
    cpy_r_r27 = (CPyPtr)&((PyListObject *)cpy_r_r26)->ob_item;
    cpy_r_r28 = *(CPyPtr *)cpy_r_r27;
    *(PyObject * *)cpy_r_r28 = cpy_r_r25;
    cpy_r_r29 = CPyStatics[13]; /* 'name' */
    cpy_r_r30 = CPyStatics[16]; /* 'LogSingleArg' */
    cpy_r_r31 = CPyStatics[15]; /* 'type' */
    cpy_r_r32 = CPyStatics[17]; /* 'event' */
    cpy_r_r33 = 0 ? Py_True : Py_False;
    cpy_r_r34 = CPyDict_Build(4, cpy_r_r15, cpy_r_r33, cpy_r_r16, cpy_r_r26, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32);
    CPy_DECREF_NO_IMM(cpy_r_r26);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 10, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r35 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r36 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r37 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r38 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r39 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r40 = CPyStatics[13]; /* 'name' */
    cpy_r_r41 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r42 = CPyStatics[15]; /* 'type' */
    cpy_r_r43 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r44 = 0 ? Py_True : Py_False;
    cpy_r_r45 = CPyDict_Build(4, cpy_r_r37, cpy_r_r44, cpy_r_r38, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42, cpy_r_r43);
    if (unlikely(cpy_r_r45 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 26, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r46 = PyList_New(1);
    if (unlikely(cpy_r_r46 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 25, CPyStatic_globals);
        goto CPyL73;
    }
    cpy_r_r47 = (CPyPtr)&((PyListObject *)cpy_r_r46)->ob_item;
    cpy_r_r48 = *(CPyPtr *)cpy_r_r47;
    *(PyObject * *)cpy_r_r48 = cpy_r_r45;
    cpy_r_r49 = CPyStatics[13]; /* 'name' */
    cpy_r_r50 = CPyStatics[18]; /* 'LogSingleWithIndex' */
    cpy_r_r51 = CPyStatics[15]; /* 'type' */
    cpy_r_r52 = CPyStatics[17]; /* 'event' */
    cpy_r_r53 = 0 ? Py_True : Py_False;
    cpy_r_r54 = CPyDict_Build(4, cpy_r_r35, cpy_r_r53, cpy_r_r36, cpy_r_r46, cpy_r_r49, cpy_r_r50, cpy_r_r51, cpy_r_r52);
    CPy_DECREF_NO_IMM(cpy_r_r46);
    if (unlikely(cpy_r_r54 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 23, CPyStatic_globals);
        goto CPyL72;
    }
    cpy_r_r55 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r56 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r57 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r58 = CPyStatics[13]; /* 'name' */
    cpy_r_r59 = CPyStatics[19]; /* '_arg0' */
    cpy_r_r60 = CPyStatics[15]; /* 'type' */
    cpy_r_r61 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r62 = CPyDict_Build(3, cpy_r_r56, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61);
    if (unlikely(cpy_r_r62 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r63 = PyList_New(1);
    if (unlikely(cpy_r_r63 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 37, CPyStatic_globals);
        goto CPyL75;
    }
    cpy_r_r64 = (CPyPtr)&((PyListObject *)cpy_r_r63)->ob_item;
    cpy_r_r65 = *(CPyPtr *)cpy_r_r64;
    *(PyObject * *)cpy_r_r65 = cpy_r_r62;
    cpy_r_r66 = CPyStatics[13]; /* 'name' */
    cpy_r_r67 = CPyStatics[20]; /* 'logTwoEvents' */
    cpy_r_r68 = CPyStatics[21]; /* 'outputs' */
    cpy_r_r69 = PyList_New(0);
    if (unlikely(cpy_r_r69 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 39, CPyStatic_globals);
        goto CPyL76;
    }
    cpy_r_r70 = CPyStatics[22]; /* 'stateMutability' */
    cpy_r_r71 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r72 = CPyStatics[15]; /* 'type' */
    cpy_r_r73 = CPyStatics[24]; /* 'function' */
    cpy_r_r74 = CPyDict_Build(5, cpy_r_r55, cpy_r_r63, cpy_r_r66, cpy_r_r67, cpy_r_r68, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72, cpy_r_r73);
    CPy_DECREF_NO_IMM(cpy_r_r63);
    CPy_DECREF_NO_IMM(cpy_r_r69);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 36, CPyStatic_globals);
        goto CPyL74;
    }
    cpy_r_r75 = PyList_New(3);
    if (unlikely(cpy_r_r75 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL77;
    }
    cpy_r_r76 = (CPyPtr)&((PyListObject *)cpy_r_r75)->ob_item;
    cpy_r_r77 = *(CPyPtr *)cpy_r_r76;
    *(PyObject * *)cpy_r_r77 = cpy_r_r34;
    cpy_r_r78 = cpy_r_r77 + 8;
    *(PyObject * *)cpy_r_r78 = cpy_r_r54;
    cpy_r_r79 = cpy_r_r77 + 16;
    *(PyObject * *)cpy_r_r79 = cpy_r_r74;
    cpy_r_r80 = CPyStatic_globals;
    cpy_r_r81 = CPyStatics[25]; /* 'EVENT_CONTRACT_ABI' */
    cpy_r_r82 = CPyDict_SetItem(cpy_r_r80, cpy_r_r81, cpy_r_r75);
    CPy_DECREF_NO_IMM(cpy_r_r75);
    cpy_r_r83 = cpy_r_r82 >= 0;
    if (unlikely(!cpy_r_r83)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 9, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r84 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r85 = CPyStatic_globals;
    cpy_r_r86 = CPyStatics[5]; /* 'EVENT_CONTRACT_BYTECODE' */
    cpy_r_r87 = CPyDict_GetItem(cpy_r_r85, cpy_r_r86);
    if (unlikely(cpy_r_r87 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 45, CPyStatic_globals);
        goto CPyL70;
    }
    if (likely(PyUnicode_Check(cpy_r_r87)))
        cpy_r_r88 = cpy_r_r87;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 45, CPyStatic_globals, "str", cpy_r_r87);
        goto CPyL70;
    }
    cpy_r_r89 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r90 = CPyStatic_globals;
    cpy_r_r91 = CPyStatics[7]; /* 'EVENT_CONTRACT_RUNTIME' */
    cpy_r_r92 = CPyDict_GetItem(cpy_r_r90, cpy_r_r91);
    if (unlikely(cpy_r_r92 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 46, CPyStatic_globals);
        goto CPyL78;
    }
    if (likely(PyUnicode_Check(cpy_r_r92)))
        cpy_r_r93 = cpy_r_r92;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 46, CPyStatic_globals, "str", cpy_r_r92);
        goto CPyL78;
    }
    cpy_r_r94 = CPyStatics[28]; /* 'abi' */
    cpy_r_r95 = CPyStatic_globals;
    cpy_r_r96 = CPyStatics[25]; /* 'EVENT_CONTRACT_ABI' */
    cpy_r_r97 = CPyDict_GetItem(cpy_r_r95, cpy_r_r96);
    if (unlikely(cpy_r_r97 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 47, CPyStatic_globals);
        goto CPyL79;
    }
    if (likely(PyList_Check(cpy_r_r97)))
        cpy_r_r98 = cpy_r_r97;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 47, CPyStatic_globals, "list", cpy_r_r97);
        goto CPyL79;
    }
    cpy_r_r99 = CPyDict_Build(3, cpy_r_r84, cpy_r_r88, cpy_r_r89, cpy_r_r93, cpy_r_r94, cpy_r_r98);
    CPy_DECREF(cpy_r_r88);
    CPy_DECREF(cpy_r_r93);
    CPy_DECREF_NO_IMM(cpy_r_r98);
    if (unlikely(cpy_r_r99 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 44, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r100 = CPyStatic_globals;
    cpy_r_r101 = CPyStatics[29]; /* 'EVENT_CONTRACT_DATA' */
    cpy_r_r102 = CPyDict_SetItem(cpy_r_r100, cpy_r_r101, cpy_r_r99);
    CPy_DECREF(cpy_r_r99);
    cpy_r_r103 = cpy_r_r102 >= 0;
    if (unlikely(!cpy_r_r103)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 44, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r104 = CPyStatics[30]; /* '0x6080604052348015600e575f5ffd5b506101708061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea26469706673582212203cd1266da088b06eb4010c3d410ac280b80cdf191b74b15b1cf76af93679dadb64736f6c634300081e0033' */
    cpy_r_r105 = CPyStatic_globals;
    cpy_r_r106 = CPyStatics[31]; /* 'INDEXED_EVENT_CONTRACT_BYTECODE' */
    cpy_r_r107 = CPyDict_SetItem(cpy_r_r105, cpy_r_r106, cpy_r_r104);
    cpy_r_r108 = cpy_r_r107 >= 0;
    if (unlikely(!cpy_r_r108)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 52, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r109 = CPyStatics[32]; /* '0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea26469706673582212203cd1266da088b06eb4010c3d410ac280b80cdf191b74b15b1cf76af93679dadb64736f6c634300081e0033' */
    cpy_r_r110 = CPyStatic_globals;
    cpy_r_r111 = CPyStatics[33]; /* 'INDEXED_EVENT_CONTRACT_RUNTIME' */
    cpy_r_r112 = CPyDict_SetItem(cpy_r_r110, cpy_r_r111, cpy_r_r109);
    cpy_r_r113 = cpy_r_r112 >= 0;
    if (unlikely(!cpy_r_r113)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 53, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r114 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r115 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r116 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r117 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r118 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r119 = CPyStatics[13]; /* 'name' */
    cpy_r_r120 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r121 = CPyStatics[15]; /* 'type' */
    cpy_r_r122 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r123 = 0 ? Py_True : Py_False;
    cpy_r_r124 = CPyDict_Build(4, cpy_r_r116, cpy_r_r123, cpy_r_r117, cpy_r_r118, cpy_r_r119, cpy_r_r120, cpy_r_r121, cpy_r_r122);
    if (unlikely(cpy_r_r124 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 58, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r125 = PyList_New(1);
    if (unlikely(cpy_r_r125 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 57, CPyStatic_globals);
        goto CPyL80;
    }
    cpy_r_r126 = (CPyPtr)&((PyListObject *)cpy_r_r125)->ob_item;
    cpy_r_r127 = *(CPyPtr *)cpy_r_r126;
    *(PyObject * *)cpy_r_r127 = cpy_r_r124;
    cpy_r_r128 = CPyStatics[13]; /* 'name' */
    cpy_r_r129 = CPyStatics[16]; /* 'LogSingleArg' */
    cpy_r_r130 = CPyStatics[15]; /* 'type' */
    cpy_r_r131 = CPyStatics[17]; /* 'event' */
    cpy_r_r132 = 0 ? Py_True : Py_False;
    cpy_r_r133 = CPyDict_Build(4, cpy_r_r114, cpy_r_r132, cpy_r_r115, cpy_r_r125, cpy_r_r128, cpy_r_r129, cpy_r_r130, cpy_r_r131);
    CPy_DECREF_NO_IMM(cpy_r_r125);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 55, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r134 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r135 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r136 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r137 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r138 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r139 = CPyStatics[13]; /* 'name' */
    cpy_r_r140 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r141 = CPyStatics[15]; /* 'type' */
    cpy_r_r142 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r143 = 1 ? Py_True : Py_False;
    cpy_r_r144 = CPyDict_Build(4, cpy_r_r136, cpy_r_r143, cpy_r_r137, cpy_r_r138, cpy_r_r139, cpy_r_r140, cpy_r_r141, cpy_r_r142);
    if (unlikely(cpy_r_r144 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 71, CPyStatic_globals);
        goto CPyL81;
    }
    cpy_r_r145 = PyList_New(1);
    if (unlikely(cpy_r_r145 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 70, CPyStatic_globals);
        goto CPyL82;
    }
    cpy_r_r146 = (CPyPtr)&((PyListObject *)cpy_r_r145)->ob_item;
    cpy_r_r147 = *(CPyPtr *)cpy_r_r146;
    *(PyObject * *)cpy_r_r147 = cpy_r_r144;
    cpy_r_r148 = CPyStatics[13]; /* 'name' */
    cpy_r_r149 = CPyStatics[18]; /* 'LogSingleWithIndex' */
    cpy_r_r150 = CPyStatics[15]; /* 'type' */
    cpy_r_r151 = CPyStatics[17]; /* 'event' */
    cpy_r_r152 = 0 ? Py_True : Py_False;
    cpy_r_r153 = CPyDict_Build(4, cpy_r_r134, cpy_r_r152, cpy_r_r135, cpy_r_r145, cpy_r_r148, cpy_r_r149, cpy_r_r150, cpy_r_r151);
    CPy_DECREF_NO_IMM(cpy_r_r145);
    if (unlikely(cpy_r_r153 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 68, CPyStatic_globals);
        goto CPyL81;
    }
    cpy_r_r154 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r155 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r156 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r157 = CPyStatics[13]; /* 'name' */
    cpy_r_r158 = CPyStatics[19]; /* '_arg0' */
    cpy_r_r159 = CPyStatics[15]; /* 'type' */
    cpy_r_r160 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r161 = CPyDict_Build(3, cpy_r_r155, cpy_r_r156, cpy_r_r157, cpy_r_r158, cpy_r_r159, cpy_r_r160);
    if (unlikely(cpy_r_r161 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 82, CPyStatic_globals);
        goto CPyL83;
    }
    cpy_r_r162 = PyList_New(1);
    if (unlikely(cpy_r_r162 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 82, CPyStatic_globals);
        goto CPyL84;
    }
    cpy_r_r163 = (CPyPtr)&((PyListObject *)cpy_r_r162)->ob_item;
    cpy_r_r164 = *(CPyPtr *)cpy_r_r163;
    *(PyObject * *)cpy_r_r164 = cpy_r_r161;
    cpy_r_r165 = CPyStatics[13]; /* 'name' */
    cpy_r_r166 = CPyStatics[20]; /* 'logTwoEvents' */
    cpy_r_r167 = CPyStatics[21]; /* 'outputs' */
    cpy_r_r168 = PyList_New(0);
    if (unlikely(cpy_r_r168 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 84, CPyStatic_globals);
        goto CPyL85;
    }
    cpy_r_r169 = CPyStatics[22]; /* 'stateMutability' */
    cpy_r_r170 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r171 = CPyStatics[15]; /* 'type' */
    cpy_r_r172 = CPyStatics[24]; /* 'function' */
    cpy_r_r173 = CPyDict_Build(5, cpy_r_r154, cpy_r_r162, cpy_r_r165, cpy_r_r166, cpy_r_r167, cpy_r_r168, cpy_r_r169, cpy_r_r170, cpy_r_r171, cpy_r_r172);
    CPy_DECREF_NO_IMM(cpy_r_r162);
    CPy_DECREF_NO_IMM(cpy_r_r168);
    if (unlikely(cpy_r_r173 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 81, CPyStatic_globals);
        goto CPyL83;
    }
    cpy_r_r174 = PyList_New(3);
    if (unlikely(cpy_r_r174 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL86;
    }
    cpy_r_r175 = (CPyPtr)&((PyListObject *)cpy_r_r174)->ob_item;
    cpy_r_r176 = *(CPyPtr *)cpy_r_r175;
    *(PyObject * *)cpy_r_r176 = cpy_r_r133;
    cpy_r_r177 = cpy_r_r176 + 8;
    *(PyObject * *)cpy_r_r177 = cpy_r_r153;
    cpy_r_r178 = cpy_r_r176 + 16;
    *(PyObject * *)cpy_r_r178 = cpy_r_r173;
    cpy_r_r179 = CPyStatic_globals;
    cpy_r_r180 = CPyStatics[34]; /* 'INDEXED_EVENT_CONTRACT_ABI' */
    cpy_r_r181 = CPyDict_SetItem(cpy_r_r179, cpy_r_r180, cpy_r_r174);
    CPy_DECREF_NO_IMM(cpy_r_r174);
    cpy_r_r182 = cpy_r_r181 >= 0;
    if (unlikely(!cpy_r_r182)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 54, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r183 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r184 = CPyStatic_globals;
    cpy_r_r185 = CPyStatics[31]; /* 'INDEXED_EVENT_CONTRACT_BYTECODE' */
    cpy_r_r186 = CPyDict_GetItem(cpy_r_r184, cpy_r_r185);
    if (unlikely(cpy_r_r186 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 90, CPyStatic_globals);
        goto CPyL70;
    }
    if (likely(PyUnicode_Check(cpy_r_r186)))
        cpy_r_r187 = cpy_r_r186;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 90, CPyStatic_globals, "str", cpy_r_r186);
        goto CPyL70;
    }
    cpy_r_r188 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r189 = CPyStatic_globals;
    cpy_r_r190 = CPyStatics[33]; /* 'INDEXED_EVENT_CONTRACT_RUNTIME' */
    cpy_r_r191 = CPyDict_GetItem(cpy_r_r189, cpy_r_r190);
    if (unlikely(cpy_r_r191 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 91, CPyStatic_globals);
        goto CPyL87;
    }
    if (likely(PyUnicode_Check(cpy_r_r191)))
        cpy_r_r192 = cpy_r_r191;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 91, CPyStatic_globals, "str", cpy_r_r191);
        goto CPyL87;
    }
    cpy_r_r193 = CPyStatics[28]; /* 'abi' */
    cpy_r_r194 = CPyStatic_globals;
    cpy_r_r195 = CPyStatics[34]; /* 'INDEXED_EVENT_CONTRACT_ABI' */
    cpy_r_r196 = CPyDict_GetItem(cpy_r_r194, cpy_r_r195);
    if (unlikely(cpy_r_r196 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 92, CPyStatic_globals);
        goto CPyL88;
    }
    if (likely(PyList_Check(cpy_r_r196)))
        cpy_r_r197 = cpy_r_r196;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 92, CPyStatic_globals, "list", cpy_r_r196);
        goto CPyL88;
    }
    cpy_r_r198 = CPyDict_Build(3, cpy_r_r183, cpy_r_r187, cpy_r_r188, cpy_r_r192, cpy_r_r193, cpy_r_r197);
    CPy_DECREF(cpy_r_r187);
    CPy_DECREF(cpy_r_r192);
    CPy_DECREF_NO_IMM(cpy_r_r197);
    if (unlikely(cpy_r_r198 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 89, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r199 = CPyStatic_globals;
    cpy_r_r200 = CPyStatics[35]; /* 'INDEXED_EVENT_CONTRACT_DATA' */
    cpy_r_r201 = CPyDict_SetItem(cpy_r_r199, cpy_r_r200, cpy_r_r198);
    CPy_DECREF(cpy_r_r198);
    cpy_r_r202 = cpy_r_r201 >= 0;
    if (unlikely(!cpy_r_r202)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 89, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r203 = CPyStatics[36]; /* '0x6080604052348015600e575f5ffd5b506102728061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b61004760048036038101906100429190610119565b610049565b005b7f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100789190610153565b60405180910390a17fe466ad4edc182e32048f6e723b179ae20d1030f298fcfa1e9ad4a759b5a63112816040516020016100b29190610153565b6040516020818303038152906040526100ca906101ae565b6040516100d79190610223565b60405180910390a150565b5f5ffd5b5f819050919050565b6100f8816100e6565b8114610102575f5ffd5b50565b5f81359050610113816100ef565b92915050565b5f6020828403121561012e5761012d6100e2565b5b5f61013b84828501610105565b91505092915050565b61014d816100e6565b82525050565b5f6020820190506101665f830184610144565b92915050565b5f81519050919050565b5f819050602082019050919050565b5f819050919050565b5f6101998251610185565b80915050919050565b5f82821b905092915050565b5f6101b88261016c565b826101c284610176565b90506101cd8161018e565b9250602082101561020d576102087fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff836020036008026101a2565b831692505b5050919050565b61021d81610185565b82525050565b5f6020820190506102365f830184610214565b9291505056fea2646970667358221220606bc1ddfcd8b77dae3483714ddada7ba373cbf1798893d081138811a379ce7364736f6c634300081e0033' */
    cpy_r_r204 = CPyStatic_globals;
    cpy_r_r205 = CPyStatics[37]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_BYTECODE' */
    cpy_r_r206 = CPyDict_SetItem(cpy_r_r204, cpy_r_r205, cpy_r_r203);
    cpy_r_r207 = cpy_r_r206 >= 0;
    if (unlikely(!cpy_r_r207)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 97, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r208 = CPyStatics[38]; /* '0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b61004760048036038101906100429190610119565b610049565b005b7f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100789190610153565b60405180910390a17fe466ad4edc182e32048f6e723b179ae20d1030f298fcfa1e9ad4a759b5a63112816040516020016100b29190610153565b6040516020818303038152906040526100ca906101ae565b6040516100d79190610223565b60405180910390a150565b5f5ffd5b5f819050919050565b6100f8816100e6565b8114610102575f5ffd5b50565b5f81359050610113816100ef565b92915050565b5f6020828403121561012e5761012d6100e2565b5b5f61013b84828501610105565b91505092915050565b61014d816100e6565b82525050565b5f6020820190506101665f830184610144565b92915050565b5f81519050919050565b5f819050602082019050919050565b5f819050919050565b5f6101998251610185565b80915050919050565b5f82821b905092915050565b5f6101b88261016c565b826101c284610176565b90506101cd8161018e565b9250602082101561020d576102087fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff836020036008026101a2565b831692505b5050919050565b61021d81610185565b82525050565b5f6020820190506102365f830184610214565b9291505056fea2646970667358221220606bc1ddfcd8b77dae3483714ddada7ba373cbf1798893d081138811a379ce7364736f6c634300081e0033' */
    cpy_r_r209 = CPyStatic_globals;
    cpy_r_r210 = CPyStatics[39]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_RUNTIME' */
    cpy_r_r211 = CPyDict_SetItem(cpy_r_r209, cpy_r_r210, cpy_r_r208);
    cpy_r_r212 = cpy_r_r211 >= 0;
    if (unlikely(!cpy_r_r212)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 98, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r213 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r214 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r215 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r216 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r217 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r218 = CPyStatics[13]; /* 'name' */
    cpy_r_r219 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r220 = CPyStatics[15]; /* 'type' */
    cpy_r_r221 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r222 = 0 ? Py_True : Py_False;
    cpy_r_r223 = CPyDict_Build(4, cpy_r_r215, cpy_r_r222, cpy_r_r216, cpy_r_r217, cpy_r_r218, cpy_r_r219, cpy_r_r220, cpy_r_r221);
    if (unlikely(cpy_r_r223 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 103, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r224 = PyList_New(1);
    if (unlikely(cpy_r_r224 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 102, CPyStatic_globals);
        goto CPyL89;
    }
    cpy_r_r225 = (CPyPtr)&((PyListObject *)cpy_r_r224)->ob_item;
    cpy_r_r226 = *(CPyPtr *)cpy_r_r225;
    *(PyObject * *)cpy_r_r226 = cpy_r_r223;
    cpy_r_r227 = CPyStatics[13]; /* 'name' */
    cpy_r_r228 = CPyStatics[16]; /* 'LogSingleArg' */
    cpy_r_r229 = CPyStatics[15]; /* 'type' */
    cpy_r_r230 = CPyStatics[17]; /* 'event' */
    cpy_r_r231 = 0 ? Py_True : Py_False;
    cpy_r_r232 = CPyDict_Build(4, cpy_r_r213, cpy_r_r231, cpy_r_r214, cpy_r_r224, cpy_r_r227, cpy_r_r228, cpy_r_r229, cpy_r_r230);
    CPy_DECREF_NO_IMM(cpy_r_r224);
    if (unlikely(cpy_r_r232 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 100, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r233 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r234 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r235 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r236 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r237 = CPyStatics[40]; /* 'bytes32' */
    cpy_r_r238 = CPyStatics[13]; /* 'name' */
    cpy_r_r239 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r240 = CPyStatics[15]; /* 'type' */
    cpy_r_r241 = CPyStatics[40]; /* 'bytes32' */
    cpy_r_r242 = 0 ? Py_True : Py_False;
    cpy_r_r243 = CPyDict_Build(4, cpy_r_r235, cpy_r_r242, cpy_r_r236, cpy_r_r237, cpy_r_r238, cpy_r_r239, cpy_r_r240, cpy_r_r241);
    if (unlikely(cpy_r_r243 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 116, CPyStatic_globals);
        goto CPyL90;
    }
    cpy_r_r244 = PyList_New(1);
    if (unlikely(cpy_r_r244 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 115, CPyStatic_globals);
        goto CPyL91;
    }
    cpy_r_r245 = (CPyPtr)&((PyListObject *)cpy_r_r244)->ob_item;
    cpy_r_r246 = *(CPyPtr *)cpy_r_r245;
    *(PyObject * *)cpy_r_r246 = cpy_r_r243;
    cpy_r_r247 = CPyStatics[13]; /* 'name' */
    cpy_r_r248 = CPyStatics[16]; /* 'LogSingleArg' */
    cpy_r_r249 = CPyStatics[15]; /* 'type' */
    cpy_r_r250 = CPyStatics[17]; /* 'event' */
    cpy_r_r251 = 0 ? Py_True : Py_False;
    cpy_r_r252 = CPyDict_Build(4, cpy_r_r233, cpy_r_r251, cpy_r_r234, cpy_r_r244, cpy_r_r247, cpy_r_r248, cpy_r_r249, cpy_r_r250);
    CPy_DECREF_NO_IMM(cpy_r_r244);
    if (unlikely(cpy_r_r252 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 113, CPyStatic_globals);
        goto CPyL90;
    }
    cpy_r_r253 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r254 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r255 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r256 = CPyStatics[13]; /* 'name' */
    cpy_r_r257 = CPyStatics[19]; /* '_arg0' */
    cpy_r_r258 = CPyStatics[15]; /* 'type' */
    cpy_r_r259 = CPyStatics[12]; /* 'uint256' */
    cpy_r_r260 = CPyDict_Build(3, cpy_r_r254, cpy_r_r255, cpy_r_r256, cpy_r_r257, cpy_r_r258, cpy_r_r259);
    if (unlikely(cpy_r_r260 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 127, CPyStatic_globals);
        goto CPyL92;
    }
    cpy_r_r261 = PyList_New(1);
    if (unlikely(cpy_r_r261 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 127, CPyStatic_globals);
        goto CPyL93;
    }
    cpy_r_r262 = (CPyPtr)&((PyListObject *)cpy_r_r261)->ob_item;
    cpy_r_r263 = *(CPyPtr *)cpy_r_r262;
    *(PyObject * *)cpy_r_r263 = cpy_r_r260;
    cpy_r_r264 = CPyStatics[13]; /* 'name' */
    cpy_r_r265 = CPyStatics[20]; /* 'logTwoEvents' */
    cpy_r_r266 = CPyStatics[21]; /* 'outputs' */
    cpy_r_r267 = PyList_New(0);
    if (unlikely(cpy_r_r267 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 129, CPyStatic_globals);
        goto CPyL94;
    }
    cpy_r_r268 = CPyStatics[22]; /* 'stateMutability' */
    cpy_r_r269 = CPyStatics[23]; /* 'nonpayable' */
    cpy_r_r270 = CPyStatics[15]; /* 'type' */
    cpy_r_r271 = CPyStatics[24]; /* 'function' */
    cpy_r_r272 = CPyDict_Build(5, cpy_r_r253, cpy_r_r261, cpy_r_r264, cpy_r_r265, cpy_r_r266, cpy_r_r267, cpy_r_r268, cpy_r_r269, cpy_r_r270, cpy_r_r271);
    CPy_DECREF_NO_IMM(cpy_r_r261);
    CPy_DECREF_NO_IMM(cpy_r_r267);
    if (unlikely(cpy_r_r272 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 126, CPyStatic_globals);
        goto CPyL92;
    }
    cpy_r_r273 = PyList_New(3);
    if (unlikely(cpy_r_r273 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 99, CPyStatic_globals);
        goto CPyL95;
    }
    cpy_r_r274 = (CPyPtr)&((PyListObject *)cpy_r_r273)->ob_item;
    cpy_r_r275 = *(CPyPtr *)cpy_r_r274;
    *(PyObject * *)cpy_r_r275 = cpy_r_r232;
    cpy_r_r276 = cpy_r_r275 + 8;
    *(PyObject * *)cpy_r_r276 = cpy_r_r252;
    cpy_r_r277 = cpy_r_r275 + 16;
    *(PyObject * *)cpy_r_r277 = cpy_r_r272;
    cpy_r_r278 = CPyStatic_globals;
    cpy_r_r279 = CPyStatics[41]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_ABI' */
    cpy_r_r280 = CPyDict_SetItem(cpy_r_r278, cpy_r_r279, cpy_r_r273);
    CPy_DECREF_NO_IMM(cpy_r_r273);
    cpy_r_r281 = cpy_r_r280 >= 0;
    if (unlikely(!cpy_r_r281)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 99, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r282 = CPyStatics[26]; /* 'bytecode' */
    cpy_r_r283 = CPyStatic_globals;
    cpy_r_r284 = CPyStatics[37]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_BYTECODE' */
    cpy_r_r285 = CPyDict_GetItem(cpy_r_r283, cpy_r_r284);
    if (unlikely(cpy_r_r285 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 135, CPyStatic_globals);
        goto CPyL70;
    }
    if (likely(PyUnicode_Check(cpy_r_r285)))
        cpy_r_r286 = cpy_r_r285;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 135, CPyStatic_globals, "str", cpy_r_r285);
        goto CPyL70;
    }
    cpy_r_r287 = CPyStatics[27]; /* 'bytecode_runtime' */
    cpy_r_r288 = CPyStatic_globals;
    cpy_r_r289 = CPyStatics[39]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_RUNTIME' */
    cpy_r_r290 = CPyDict_GetItem(cpy_r_r288, cpy_r_r289);
    if (unlikely(cpy_r_r290 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 136, CPyStatic_globals);
        goto CPyL96;
    }
    if (likely(PyUnicode_Check(cpy_r_r290)))
        cpy_r_r291 = cpy_r_r290;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 136, CPyStatic_globals, "str", cpy_r_r290);
        goto CPyL96;
    }
    cpy_r_r292 = CPyStatics[28]; /* 'abi' */
    cpy_r_r293 = CPyStatic_globals;
    cpy_r_r294 = CPyStatics[41]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_ABI' */
    cpy_r_r295 = CPyDict_GetItem(cpy_r_r293, cpy_r_r294);
    if (unlikely(cpy_r_r295 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 137, CPyStatic_globals);
        goto CPyL97;
    }
    if (likely(PyList_Check(cpy_r_r295)))
        cpy_r_r296 = cpy_r_r295;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 137, CPyStatic_globals, "list", cpy_r_r295);
        goto CPyL97;
    }
    cpy_r_r297 = CPyDict_Build(3, cpy_r_r282, cpy_r_r286, cpy_r_r287, cpy_r_r291, cpy_r_r292, cpy_r_r296);
    CPy_DECREF(cpy_r_r286);
    CPy_DECREF(cpy_r_r291);
    CPy_DECREF_NO_IMM(cpy_r_r296);
    if (unlikely(cpy_r_r297 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 134, CPyStatic_globals);
        goto CPyL70;
    }
    cpy_r_r298 = CPyStatic_globals;
    cpy_r_r299 = CPyStatics[42]; /* 'AMBIGUOUS_EVENT_NAME_CONTRACT_DATA' */
    cpy_r_r300 = CPyDict_SetItem(cpy_r_r298, cpy_r_r299, cpy_r_r297);
    CPy_DECREF(cpy_r_r297);
    cpy_r_r301 = cpy_r_r300 >= 0;
    if (unlikely(!cpy_r_r301)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/event_contracts.py", "<module>", 134, CPyStatic_globals);
        goto CPyL70;
    }
    return 1;
CPyL70: ;
    cpy_r_r302 = 2;
    return cpy_r_r302;
CPyL71: ;
    CPy_DecRef(cpy_r_r25);
    goto CPyL70;
CPyL72: ;
    CPy_DecRef(cpy_r_r34);
    goto CPyL70;
CPyL73: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r45);
    goto CPyL70;
CPyL74: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    goto CPyL70;
CPyL75: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r62);
    goto CPyL70;
CPyL76: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r63);
    goto CPyL70;
CPyL77: ;
    CPy_DecRef(cpy_r_r34);
    CPy_DecRef(cpy_r_r54);
    CPy_DecRef(cpy_r_r74);
    goto CPyL70;
CPyL78: ;
    CPy_DecRef(cpy_r_r88);
    goto CPyL70;
CPyL79: ;
    CPy_DecRef(cpy_r_r88);
    CPy_DecRef(cpy_r_r93);
    goto CPyL70;
CPyL80: ;
    CPy_DecRef(cpy_r_r124);
    goto CPyL70;
CPyL81: ;
    CPy_DecRef(cpy_r_r133);
    goto CPyL70;
CPyL82: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r144);
    goto CPyL70;
CPyL83: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r153);
    goto CPyL70;
CPyL84: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r153);
    CPy_DecRef(cpy_r_r161);
    goto CPyL70;
CPyL85: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r153);
    CPy_DecRef(cpy_r_r162);
    goto CPyL70;
CPyL86: ;
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r153);
    CPy_DecRef(cpy_r_r173);
    goto CPyL70;
CPyL87: ;
    CPy_DecRef(cpy_r_r187);
    goto CPyL70;
CPyL88: ;
    CPy_DecRef(cpy_r_r187);
    CPy_DecRef(cpy_r_r192);
    goto CPyL70;
CPyL89: ;
    CPy_DecRef(cpy_r_r223);
    goto CPyL70;
CPyL90: ;
    CPy_DecRef(cpy_r_r232);
    goto CPyL70;
CPyL91: ;
    CPy_DecRef(cpy_r_r232);
    CPy_DecRef(cpy_r_r243);
    goto CPyL70;
CPyL92: ;
    CPy_DecRef(cpy_r_r232);
    CPy_DecRef(cpy_r_r252);
    goto CPyL70;
CPyL93: ;
    CPy_DecRef(cpy_r_r232);
    CPy_DecRef(cpy_r_r252);
    CPy_DecRef(cpy_r_r260);
    goto CPyL70;
CPyL94: ;
    CPy_DecRef(cpy_r_r232);
    CPy_DecRef(cpy_r_r252);
    CPy_DecRef(cpy_r_r261);
    goto CPyL70;
CPyL95: ;
    CPy_DecRef(cpy_r_r232);
    CPy_DecRef(cpy_r_r252);
    CPy_DecRef(cpy_r_r272);
    goto CPyL70;
CPyL96: ;
    CPy_DecRef(cpy_r_r286);
    goto CPyL70;
CPyL97: ;
    CPy_DecRef(cpy_r_r286);
    CPy_DecRef(cpy_r_r291);
    goto CPyL70;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[43];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\206.0x6080604052348015600e575f5ffd5b5061017a8061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea264697066735822122024dd83d4ed45a24e04cc3847bf220951b8e223a67484b966cda4cedca6223a0564736f6c634300081e0033",
    "\001\027EVENT_CONTRACT_BYTECODE",
    "\001\205v0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100f1565b610049565b005b7ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1581604051610078919061012b565b60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100af919061012b565b60405180910390a150565b5f5ffd5b5f819050919050565b6100d0816100be565b81146100da575f5ffd5b50565b5f813590506100eb816100c7565b92915050565b5f60208284031215610106576101056100ba565b5b5f610113848285016100dd565b91505092915050565b610125816100be565b82525050565b5f60208201905061013e5f83018461011c565b9291505056fea264697066735822122024dd83d4ed45a24e04cc3847bf220951b8e223a67484b966cda4cedca6223a0564736f6c634300081e0033",
    "\006\026EVENT_CONTRACT_RUNTIME\tanonymous\006inputs\aindexed\finternalType\auint256",
    "\a\004name\004arg0\004type\fLogSingleArg\005event\022LogSingleWithIndex\005_arg0",
    "\005\flogTwoEvents\aoutputs\017stateMutability\nnonpayable\bfunction",
    "\005\022EVENT_CONTRACT_ABI\bbytecode\020bytecode_runtime\003abi\023EVENT_CONTRACT_DATA",
    "\001\206\0320x6080604052348015600e575f5ffd5b506101708061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea26469706673582212203cd1266da088b06eb4010c3d410ac280b80cdf191b74b15b1cf76af93679dadb64736f6c634300081e0033",
    "\001\037INDEXED_EVENT_CONTRACT_BYTECODE",
    "\001\205b0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b610047600480360381019061004291906100e7565b610049565b005b807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100a59190610121565b60405180910390a150565b5f5ffd5b5f819050919050565b6100c6816100b4565b81146100d0575f5ffd5b50565b5f813590506100e1816100bd565b92915050565b5f602082840312156100fc576100fb6100b0565b5b5f610109848285016100d3565b91505092915050565b61011b816100b4565b82525050565b5f6020820190506101345f830184610112565b9291505056fea26469706673582212203cd1266da088b06eb4010c3d410ac280b80cdf191b74b15b1cf76af93679dadb64736f6c634300081e0033",
    "\002\036INDEXED_EVENT_CONTRACT_RUNTIME\032INDEXED_EVENT_CONTRACT_ABI",
    "\001\033INDEXED_EVENT_CONTRACT_DATA",
    "\001\212\0360x6080604052348015600e575f5ffd5b506102728061001c5f395ff3fe608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b61004760048036038101906100429190610119565b610049565b005b7f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100789190610153565b60405180910390a17fe466ad4edc182e32048f6e723b179ae20d1030f298fcfa1e9ad4a759b5a63112816040516020016100b29190610153565b6040516020818303038152906040526100ca906101ae565b6040516100d79190610223565b60405180910390a150565b5f5ffd5b5f819050919050565b6100f8816100e6565b8114610102575f5ffd5b50565b5f81359050610113816100ef565b92915050565b5f6020828403121561012e5761012d6100e2565b5b5f61013b84828501610105565b91505092915050565b61014d816100e6565b82525050565b5f6020820190506101665f830184610144565b92915050565b5f81519050919050565b5f819050602082019050919050565b5f819050919050565b5f6101998251610185565b80915050919050565b5f82821b905092915050565b5f6101b88261016c565b826101c284610176565b90506101cd8161018e565b9250602082101561020d576102087fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff836020036008026101a2565b831692505b5050919050565b61021d81610185565b82525050565b5f6020820190506102365f830184610214565b9291505056fea2646970667358221220606bc1ddfcd8b77dae3483714ddada7ba373cbf1798893d081138811a379ce7364736f6c634300081e0033",
    "\001&AMBIGUOUS_EVENT_NAME_CONTRACT_BYTECODE",
    "\001\211f0x608060405234801561000f575f5ffd5b5060043610610029575f3560e01c80635818fad71461002d575b5f5ffd5b61004760048036038101906100429190610119565b610049565b005b7f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516100789190610153565b60405180910390a17fe466ad4edc182e32048f6e723b179ae20d1030f298fcfa1e9ad4a759b5a63112816040516020016100b29190610153565b6040516020818303038152906040526100ca906101ae565b6040516100d79190610223565b60405180910390a150565b5f5ffd5b5f819050919050565b6100f8816100e6565b8114610102575f5ffd5b50565b5f81359050610113816100ef565b92915050565b5f6020828403121561012e5761012d6100e2565b5b5f61013b84828501610105565b91505092915050565b61014d816100e6565b82525050565b5f6020820190506101665f830184610144565b92915050565b5f81519050919050565b5f819050602082019050919050565b5f819050919050565b5f6101998251610185565b80915050919050565b5f82821b905092915050565b5f6101b88261016c565b826101c284610176565b90506101cd8161018e565b9250602082101561020d576102087fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff836020036008026101a2565b831692505b5050919050565b61021d81610185565b82525050565b5f6020820190506102365f830184610214565b9291505056fea2646970667358221220606bc1ddfcd8b77dae3483714ddada7ba373cbf1798893d081138811a379ce7364736f6c634300081e0033",
    "\002%AMBIGUOUS_EVENT_NAME_CONTRACT_RUNTIME\abytes32",
    "\002!AMBIGUOUS_EVENT_NAME_CONTRACT_ABI\"AMBIGUOUS_EVENT_NAME_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___event_contracts;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_event_contracts__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___event_contracts(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___event_contracts, "faster_web3._utils.contract_sources.contract_data.event_contracts__mypyc.init_faster_web3____utils___contract_sources___contract_data___event_contracts", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___event_contracts", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_event_contracts__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.event_contracts__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_event_contracts__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_event_contracts__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_event_contracts__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
