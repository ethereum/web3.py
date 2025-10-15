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
#include "__native_emitter_contract.h"
#include "__native_internal_emitter_contract.h"
static PyMethodDef module_methods[] = {
    {NULL, NULL, 0, NULL}
};

int CPyExec_faster_web3____utils___contract_sources___contract_data___emitter_contract(PyObject *module)
{
    PyObject* modname = NULL;
    modname = PyObject_GetAttrString((PyObject *)CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal, "__name__");
    CPyStatic_globals = PyModule_GetDict(CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal);
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
    Py_CLEAR(CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal);
    Py_CLEAR(modname);
    return -1;
}
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "faster_web3._utils.contract_sources.contract_data.emitter_contract",
    NULL, /* docstring */
    0,       /* size of per-interpreter state of the module */
    module_methods,
    NULL,
};

PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___emitter_contract(void)
{
    if (CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal) {
        Py_INCREF(CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal);
        return CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal;
    }
    CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal = PyModule_Create(&module);
    if (unlikely(CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal == NULL))
        goto fail;
    if (CPyExec_faster_web3____utils___contract_sources___contract_data___emitter_contract(CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal) != 0)
        goto fail;
    return CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal;
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
    CPyPtr cpy_r_r36;
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
    CPyPtr cpy_r_r66;
    CPyPtr cpy_r_r67;
    CPyPtr cpy_r_r68;
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
    PyObject *cpy_r_r116;
    PyObject *cpy_r_r117;
    PyObject *cpy_r_r118;
    PyObject *cpy_r_r119;
    PyObject *cpy_r_r120;
    PyObject *cpy_r_r121;
    PyObject *cpy_r_r122;
    PyObject *cpy_r_r123;
    PyObject *cpy_r_r124;
    CPyPtr cpy_r_r125;
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
    PyObject *cpy_r_r146;
    PyObject *cpy_r_r147;
    PyObject *cpy_r_r148;
    PyObject *cpy_r_r149;
    PyObject *cpy_r_r150;
    PyObject *cpy_r_r151;
    PyObject *cpy_r_r152;
    PyObject *cpy_r_r153;
    PyObject *cpy_r_r154;
    CPyPtr cpy_r_r155;
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
    CPyPtr cpy_r_r185;
    CPyPtr cpy_r_r186;
    CPyPtr cpy_r_r187;
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
    PyObject *cpy_r_r201;
    PyObject *cpy_r_r202;
    PyObject *cpy_r_r203;
    PyObject *cpy_r_r204;
    PyObject *cpy_r_r205;
    PyObject *cpy_r_r206;
    PyObject *cpy_r_r207;
    PyObject *cpy_r_r208;
    PyObject *cpy_r_r209;
    PyObject *cpy_r_r210;
    PyObject *cpy_r_r211;
    PyObject *cpy_r_r212;
    PyObject *cpy_r_r213;
    PyObject *cpy_r_r214;
    CPyPtr cpy_r_r215;
    CPyPtr cpy_r_r216;
    CPyPtr cpy_r_r217;
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
    PyObject *cpy_r_r264;
    PyObject *cpy_r_r265;
    PyObject *cpy_r_r266;
    PyObject *cpy_r_r267;
    PyObject *cpy_r_r268;
    PyObject *cpy_r_r269;
    PyObject *cpy_r_r270;
    PyObject *cpy_r_r271;
    CPyPtr cpy_r_r272;
    CPyPtr cpy_r_r273;
    CPyPtr cpy_r_r274;
    CPyPtr cpy_r_r275;
    CPyPtr cpy_r_r276;
    CPyPtr cpy_r_r277;
    PyObject *cpy_r_r278;
    PyObject *cpy_r_r279;
    PyObject *cpy_r_r280;
    PyObject *cpy_r_r281;
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
    PyObject *cpy_r_r300;
    PyObject *cpy_r_r301;
    PyObject *cpy_r_r302;
    PyObject *cpy_r_r303;
    PyObject *cpy_r_r304;
    CPyPtr cpy_r_r305;
    CPyPtr cpy_r_r306;
    CPyPtr cpy_r_r307;
    PyObject *cpy_r_r308;
    PyObject *cpy_r_r309;
    PyObject *cpy_r_r310;
    PyObject *cpy_r_r311;
    PyObject *cpy_r_r312;
    PyObject *cpy_r_r313;
    PyObject *cpy_r_r314;
    PyObject *cpy_r_r315;
    PyObject *cpy_r_r316;
    PyObject *cpy_r_r317;
    PyObject *cpy_r_r318;
    PyObject *cpy_r_r319;
    PyObject *cpy_r_r320;
    PyObject *cpy_r_r321;
    PyObject *cpy_r_r322;
    PyObject *cpy_r_r323;
    PyObject *cpy_r_r324;
    PyObject *cpy_r_r325;
    PyObject *cpy_r_r326;
    PyObject *cpy_r_r327;
    PyObject *cpy_r_r328;
    PyObject *cpy_r_r329;
    PyObject *cpy_r_r330;
    PyObject *cpy_r_r331;
    PyObject *cpy_r_r332;
    PyObject *cpy_r_r333;
    PyObject *cpy_r_r334;
    PyObject *cpy_r_r335;
    PyObject *cpy_r_r336;
    PyObject *cpy_r_r337;
    PyObject *cpy_r_r338;
    PyObject *cpy_r_r339;
    PyObject *cpy_r_r340;
    PyObject *cpy_r_r341;
    PyObject *cpy_r_r342;
    PyObject *cpy_r_r343;
    PyObject *cpy_r_r344;
    PyObject *cpy_r_r345;
    PyObject *cpy_r_r346;
    PyObject *cpy_r_r347;
    PyObject *cpy_r_r348;
    PyObject *cpy_r_r349;
    PyObject *cpy_r_r350;
    PyObject *cpy_r_r351;
    PyObject *cpy_r_r352;
    PyObject *cpy_r_r353;
    PyObject *cpy_r_r354;
    PyObject *cpy_r_r355;
    PyObject *cpy_r_r356;
    PyObject *cpy_r_r357;
    PyObject *cpy_r_r358;
    PyObject *cpy_r_r359;
    PyObject *cpy_r_r360;
    PyObject *cpy_r_r361;
    CPyPtr cpy_r_r362;
    CPyPtr cpy_r_r363;
    CPyPtr cpy_r_r364;
    CPyPtr cpy_r_r365;
    CPyPtr cpy_r_r366;
    PyObject *cpy_r_r367;
    PyObject *cpy_r_r368;
    PyObject *cpy_r_r369;
    PyObject *cpy_r_r370;
    PyObject *cpy_r_r371;
    PyObject *cpy_r_r372;
    PyObject *cpy_r_r373;
    PyObject *cpy_r_r374;
    PyObject *cpy_r_r375;
    PyObject *cpy_r_r376;
    PyObject *cpy_r_r377;
    PyObject *cpy_r_r378;
    PyObject *cpy_r_r379;
    PyObject *cpy_r_r380;
    PyObject *cpy_r_r381;
    PyObject *cpy_r_r382;
    PyObject *cpy_r_r383;
    PyObject *cpy_r_r384;
    PyObject *cpy_r_r385;
    PyObject *cpy_r_r386;
    PyObject *cpy_r_r387;
    PyObject *cpy_r_r388;
    PyObject *cpy_r_r389;
    PyObject *cpy_r_r390;
    PyObject *cpy_r_r391;
    PyObject *cpy_r_r392;
    PyObject *cpy_r_r393;
    PyObject *cpy_r_r394;
    PyObject *cpy_r_r395;
    PyObject *cpy_r_r396;
    PyObject *cpy_r_r397;
    PyObject *cpy_r_r398;
    PyObject *cpy_r_r399;
    PyObject *cpy_r_r400;
    PyObject *cpy_r_r401;
    PyObject *cpy_r_r402;
    PyObject *cpy_r_r403;
    PyObject *cpy_r_r404;
    PyObject *cpy_r_r405;
    PyObject *cpy_r_r406;
    PyObject *cpy_r_r407;
    PyObject *cpy_r_r408;
    PyObject *cpy_r_r409;
    PyObject *cpy_r_r410;
    PyObject *cpy_r_r411;
    CPyPtr cpy_r_r412;
    CPyPtr cpy_r_r413;
    CPyPtr cpy_r_r414;
    CPyPtr cpy_r_r415;
    CPyPtr cpy_r_r416;
    PyObject *cpy_r_r417;
    PyObject *cpy_r_r418;
    PyObject *cpy_r_r419;
    PyObject *cpy_r_r420;
    PyObject *cpy_r_r421;
    PyObject *cpy_r_r422;
    PyObject *cpy_r_r423;
    PyObject *cpy_r_r424;
    PyObject *cpy_r_r425;
    PyObject *cpy_r_r426;
    PyObject *cpy_r_r427;
    PyObject *cpy_r_r428;
    PyObject *cpy_r_r429;
    PyObject *cpy_r_r430;
    PyObject *cpy_r_r431;
    PyObject *cpy_r_r432;
    PyObject *cpy_r_r433;
    PyObject *cpy_r_r434;
    CPyPtr cpy_r_r435;
    CPyPtr cpy_r_r436;
    PyObject *cpy_r_r437;
    PyObject *cpy_r_r438;
    PyObject *cpy_r_r439;
    PyObject *cpy_r_r440;
    PyObject *cpy_r_r441;
    PyObject *cpy_r_r442;
    PyObject *cpy_r_r443;
    PyObject *cpy_r_r444;
    PyObject *cpy_r_r445;
    PyObject *cpy_r_r446;
    PyObject *cpy_r_r447;
    PyObject *cpy_r_r448;
    PyObject *cpy_r_r449;
    PyObject *cpy_r_r450;
    PyObject *cpy_r_r451;
    PyObject *cpy_r_r452;
    PyObject *cpy_r_r453;
    PyObject *cpy_r_r454;
    CPyPtr cpy_r_r455;
    CPyPtr cpy_r_r456;
    PyObject *cpy_r_r457;
    PyObject *cpy_r_r458;
    PyObject *cpy_r_r459;
    PyObject *cpy_r_r460;
    PyObject *cpy_r_r461;
    PyObject *cpy_r_r462;
    PyObject *cpy_r_r463;
    PyObject *cpy_r_r464;
    PyObject *cpy_r_r465;
    PyObject *cpy_r_r466;
    PyObject *cpy_r_r467;
    PyObject *cpy_r_r468;
    PyObject *cpy_r_r469;
    PyObject *cpy_r_r470;
    PyObject *cpy_r_r471;
    PyObject *cpy_r_r472;
    PyObject *cpy_r_r473;
    PyObject *cpy_r_r474;
    CPyPtr cpy_r_r475;
    CPyPtr cpy_r_r476;
    PyObject *cpy_r_r477;
    PyObject *cpy_r_r478;
    PyObject *cpy_r_r479;
    PyObject *cpy_r_r480;
    PyObject *cpy_r_r481;
    PyObject *cpy_r_r482;
    PyObject *cpy_r_r483;
    PyObject *cpy_r_r484;
    PyObject *cpy_r_r485;
    PyObject *cpy_r_r486;
    PyObject *cpy_r_r487;
    PyObject *cpy_r_r488;
    PyObject *cpy_r_r489;
    PyObject *cpy_r_r490;
    PyObject *cpy_r_r491;
    PyObject *cpy_r_r492;
    PyObject *cpy_r_r493;
    PyObject *cpy_r_r494;
    CPyPtr cpy_r_r495;
    CPyPtr cpy_r_r496;
    PyObject *cpy_r_r497;
    PyObject *cpy_r_r498;
    PyObject *cpy_r_r499;
    PyObject *cpy_r_r500;
    PyObject *cpy_r_r501;
    PyObject *cpy_r_r502;
    PyObject *cpy_r_r503;
    PyObject *cpy_r_r504;
    PyObject *cpy_r_r505;
    PyObject *cpy_r_r506;
    PyObject *cpy_r_r507;
    PyObject *cpy_r_r508;
    PyObject *cpy_r_r509;
    PyObject *cpy_r_r510;
    PyObject *cpy_r_r511;
    PyObject *cpy_r_r512;
    PyObject *cpy_r_r513;
    PyObject *cpy_r_r514;
    PyObject *cpy_r_r515;
    PyObject *cpy_r_r516;
    PyObject *cpy_r_r517;
    PyObject *cpy_r_r518;
    PyObject *cpy_r_r519;
    PyObject *cpy_r_r520;
    PyObject *cpy_r_r521;
    PyObject *cpy_r_r522;
    PyObject *cpy_r_r523;
    PyObject *cpy_r_r524;
    PyObject *cpy_r_r525;
    PyObject *cpy_r_r526;
    PyObject *cpy_r_r527;
    PyObject *cpy_r_r528;
    PyObject *cpy_r_r529;
    PyObject *cpy_r_r530;
    PyObject *cpy_r_r531;
    PyObject *cpy_r_r532;
    PyObject *cpy_r_r533;
    PyObject *cpy_r_r534;
    PyObject *cpy_r_r535;
    PyObject *cpy_r_r536;
    PyObject *cpy_r_r537;
    CPyPtr cpy_r_r538;
    CPyPtr cpy_r_r539;
    PyObject *cpy_r_r540;
    PyObject *cpy_r_r541;
    PyObject *cpy_r_r542;
    PyObject *cpy_r_r543;
    PyObject *cpy_r_r544;
    PyObject *cpy_r_r545;
    PyObject *cpy_r_r546;
    PyObject *cpy_r_r547;
    CPyPtr cpy_r_r548;
    CPyPtr cpy_r_r549;
    CPyPtr cpy_r_r550;
    CPyPtr cpy_r_r551;
    PyObject *cpy_r_r552;
    PyObject *cpy_r_r553;
    PyObject *cpy_r_r554;
    PyObject *cpy_r_r555;
    PyObject *cpy_r_r556;
    PyObject *cpy_r_r557;
    PyObject *cpy_r_r558;
    PyObject *cpy_r_r559;
    PyObject *cpy_r_r560;
    PyObject *cpy_r_r561;
    CPyPtr cpy_r_r562;
    CPyPtr cpy_r_r563;
    CPyPtr cpy_r_r564;
    PyObject *cpy_r_r565;
    PyObject *cpy_r_r566;
    PyObject *cpy_r_r567;
    PyObject *cpy_r_r568;
    PyObject *cpy_r_r569;
    PyObject *cpy_r_r570;
    PyObject *cpy_r_r571;
    PyObject *cpy_r_r572;
    PyObject *cpy_r_r573;
    PyObject *cpy_r_r574;
    PyObject *cpy_r_r575;
    PyObject *cpy_r_r576;
    PyObject *cpy_r_r577;
    PyObject *cpy_r_r578;
    PyObject *cpy_r_r579;
    PyObject *cpy_r_r580;
    PyObject *cpy_r_r581;
    PyObject *cpy_r_r582;
    PyObject *cpy_r_r583;
    PyObject *cpy_r_r584;
    PyObject *cpy_r_r585;
    PyObject *cpy_r_r586;
    PyObject *cpy_r_r587;
    PyObject *cpy_r_r588;
    PyObject *cpy_r_r589;
    PyObject *cpy_r_r590;
    PyObject *cpy_r_r591;
    PyObject *cpy_r_r592;
    PyObject *cpy_r_r593;
    PyObject *cpy_r_r594;
    PyObject *cpy_r_r595;
    PyObject *cpy_r_r596;
    PyObject *cpy_r_r597;
    PyObject *cpy_r_r598;
    PyObject *cpy_r_r599;
    PyObject *cpy_r_r600;
    CPyPtr cpy_r_r601;
    CPyPtr cpy_r_r602;
    CPyPtr cpy_r_r603;
    CPyPtr cpy_r_r604;
    PyObject *cpy_r_r605;
    PyObject *cpy_r_r606;
    PyObject *cpy_r_r607;
    PyObject *cpy_r_r608;
    PyObject *cpy_r_r609;
    PyObject *cpy_r_r610;
    PyObject *cpy_r_r611;
    PyObject *cpy_r_r612;
    PyObject *cpy_r_r613;
    PyObject *cpy_r_r614;
    PyObject *cpy_r_r615;
    PyObject *cpy_r_r616;
    PyObject *cpy_r_r617;
    PyObject *cpy_r_r618;
    PyObject *cpy_r_r619;
    PyObject *cpy_r_r620;
    PyObject *cpy_r_r621;
    PyObject *cpy_r_r622;
    PyObject *cpy_r_r623;
    PyObject *cpy_r_r624;
    PyObject *cpy_r_r625;
    PyObject *cpy_r_r626;
    PyObject *cpy_r_r627;
    PyObject *cpy_r_r628;
    PyObject *cpy_r_r629;
    PyObject *cpy_r_r630;
    PyObject *cpy_r_r631;
    PyObject *cpy_r_r632;
    PyObject *cpy_r_r633;
    PyObject *cpy_r_r634;
    PyObject *cpy_r_r635;
    PyObject *cpy_r_r636;
    PyObject *cpy_r_r637;
    PyObject *cpy_r_r638;
    PyObject *cpy_r_r639;
    PyObject *cpy_r_r640;
    CPyPtr cpy_r_r641;
    CPyPtr cpy_r_r642;
    CPyPtr cpy_r_r643;
    CPyPtr cpy_r_r644;
    PyObject *cpy_r_r645;
    PyObject *cpy_r_r646;
    PyObject *cpy_r_r647;
    PyObject *cpy_r_r648;
    PyObject *cpy_r_r649;
    PyObject *cpy_r_r650;
    PyObject *cpy_r_r651;
    PyObject *cpy_r_r652;
    PyObject *cpy_r_r653;
    PyObject *cpy_r_r654;
    PyObject *cpy_r_r655;
    PyObject *cpy_r_r656;
    PyObject *cpy_r_r657;
    PyObject *cpy_r_r658;
    PyObject *cpy_r_r659;
    PyObject *cpy_r_r660;
    PyObject *cpy_r_r661;
    PyObject *cpy_r_r662;
    PyObject *cpy_r_r663;
    PyObject *cpy_r_r664;
    PyObject *cpy_r_r665;
    PyObject *cpy_r_r666;
    CPyPtr cpy_r_r667;
    CPyPtr cpy_r_r668;
    CPyPtr cpy_r_r669;
    PyObject *cpy_r_r670;
    PyObject *cpy_r_r671;
    PyObject *cpy_r_r672;
    PyObject *cpy_r_r673;
    PyObject *cpy_r_r674;
    PyObject *cpy_r_r675;
    PyObject *cpy_r_r676;
    PyObject *cpy_r_r677;
    PyObject *cpy_r_r678;
    PyObject *cpy_r_r679;
    PyObject *cpy_r_r680;
    PyObject *cpy_r_r681;
    PyObject *cpy_r_r682;
    PyObject *cpy_r_r683;
    PyObject *cpy_r_r684;
    PyObject *cpy_r_r685;
    PyObject *cpy_r_r686;
    PyObject *cpy_r_r687;
    PyObject *cpy_r_r688;
    PyObject *cpy_r_r689;
    PyObject *cpy_r_r690;
    PyObject *cpy_r_r691;
    PyObject *cpy_r_r692;
    PyObject *cpy_r_r693;
    PyObject *cpy_r_r694;
    CPyPtr cpy_r_r695;
    CPyPtr cpy_r_r696;
    CPyPtr cpy_r_r697;
    PyObject *cpy_r_r698;
    PyObject *cpy_r_r699;
    PyObject *cpy_r_r700;
    PyObject *cpy_r_r701;
    PyObject *cpy_r_r702;
    PyObject *cpy_r_r703;
    PyObject *cpy_r_r704;
    PyObject *cpy_r_r705;
    PyObject *cpy_r_r706;
    PyObject *cpy_r_r707;
    PyObject *cpy_r_r708;
    PyObject *cpy_r_r709;
    PyObject *cpy_r_r710;
    PyObject *cpy_r_r711;
    PyObject *cpy_r_r712;
    PyObject *cpy_r_r713;
    PyObject *cpy_r_r714;
    PyObject *cpy_r_r715;
    CPyPtr cpy_r_r716;
    CPyPtr cpy_r_r717;
    PyObject *cpy_r_r718;
    PyObject *cpy_r_r719;
    PyObject *cpy_r_r720;
    PyObject *cpy_r_r721;
    PyObject *cpy_r_r722;
    PyObject *cpy_r_r723;
    PyObject *cpy_r_r724;
    PyObject *cpy_r_r725;
    PyObject *cpy_r_r726;
    PyObject *cpy_r_r727;
    PyObject *cpy_r_r728;
    PyObject *cpy_r_r729;
    PyObject *cpy_r_r730;
    PyObject *cpy_r_r731;
    PyObject *cpy_r_r732;
    PyObject *cpy_r_r733;
    PyObject *cpy_r_r734;
    PyObject *cpy_r_r735;
    PyObject *cpy_r_r736;
    PyObject *cpy_r_r737;
    PyObject *cpy_r_r738;
    PyObject *cpy_r_r739;
    PyObject *cpy_r_r740;
    PyObject *cpy_r_r741;
    PyObject *cpy_r_r742;
    PyObject *cpy_r_r743;
    PyObject *cpy_r_r744;
    PyObject *cpy_r_r745;
    PyObject *cpy_r_r746;
    PyObject *cpy_r_r747;
    PyObject *cpy_r_r748;
    PyObject *cpy_r_r749;
    CPyPtr cpy_r_r750;
    CPyPtr cpy_r_r751;
    CPyPtr cpy_r_r752;
    CPyPtr cpy_r_r753;
    PyObject *cpy_r_r754;
    PyObject *cpy_r_r755;
    PyObject *cpy_r_r756;
    PyObject *cpy_r_r757;
    PyObject *cpy_r_r758;
    PyObject *cpy_r_r759;
    PyObject *cpy_r_r760;
    PyObject *cpy_r_r761;
    PyObject *cpy_r_r762;
    PyObject *cpy_r_r763;
    PyObject *cpy_r_r764;
    PyObject *cpy_r_r765;
    PyObject *cpy_r_r766;
    PyObject *cpy_r_r767;
    PyObject *cpy_r_r768;
    PyObject *cpy_r_r769;
    PyObject *cpy_r_r770;
    PyObject *cpy_r_r771;
    PyObject *cpy_r_r772;
    PyObject *cpy_r_r773;
    PyObject *cpy_r_r774;
    PyObject *cpy_r_r775;
    PyObject *cpy_r_r776;
    PyObject *cpy_r_r777;
    PyObject *cpy_r_r778;
    CPyPtr cpy_r_r779;
    CPyPtr cpy_r_r780;
    CPyPtr cpy_r_r781;
    PyObject *cpy_r_r782;
    PyObject *cpy_r_r783;
    PyObject *cpy_r_r784;
    PyObject *cpy_r_r785;
    PyObject *cpy_r_r786;
    PyObject *cpy_r_r787;
    PyObject *cpy_r_r788;
    PyObject *cpy_r_r789;
    PyObject *cpy_r_r790;
    PyObject *cpy_r_r791;
    PyObject *cpy_r_r792;
    PyObject *cpy_r_r793;
    PyObject *cpy_r_r794;
    PyObject *cpy_r_r795;
    PyObject *cpy_r_r796;
    PyObject *cpy_r_r797;
    PyObject *cpy_r_r798;
    PyObject *cpy_r_r799;
    PyObject *cpy_r_r800;
    PyObject *cpy_r_r801;
    PyObject *cpy_r_r802;
    PyObject *cpy_r_r803;
    PyObject *cpy_r_r804;
    PyObject *cpy_r_r805;
    PyObject *cpy_r_r806;
    PyObject *cpy_r_r807;
    PyObject *cpy_r_r808;
    PyObject *cpy_r_r809;
    PyObject *cpy_r_r810;
    PyObject *cpy_r_r811;
    PyObject *cpy_r_r812;
    PyObject *cpy_r_r813;
    PyObject *cpy_r_r814;
    PyObject *cpy_r_r815;
    PyObject *cpy_r_r816;
    PyObject *cpy_r_r817;
    PyObject *cpy_r_r818;
    PyObject *cpy_r_r819;
    PyObject *cpy_r_r820;
    PyObject *cpy_r_r821;
    PyObject *cpy_r_r822;
    PyObject *cpy_r_r823;
    PyObject *cpy_r_r824;
    PyObject *cpy_r_r825;
    PyObject *cpy_r_r826;
    PyObject *cpy_r_r827;
    CPyPtr cpy_r_r828;
    CPyPtr cpy_r_r829;
    CPyPtr cpy_r_r830;
    CPyPtr cpy_r_r831;
    CPyPtr cpy_r_r832;
    CPyPtr cpy_r_r833;
    PyObject *cpy_r_r834;
    PyObject *cpy_r_r835;
    PyObject *cpy_r_r836;
    PyObject *cpy_r_r837;
    PyObject *cpy_r_r838;
    PyObject *cpy_r_r839;
    PyObject *cpy_r_r840;
    PyObject *cpy_r_r841;
    PyObject *cpy_r_r842;
    PyObject *cpy_r_r843;
    PyObject *cpy_r_r844;
    PyObject *cpy_r_r845;
    PyObject *cpy_r_r846;
    PyObject *cpy_r_r847;
    PyObject *cpy_r_r848;
    PyObject *cpy_r_r849;
    PyObject *cpy_r_r850;
    PyObject *cpy_r_r851;
    PyObject *cpy_r_r852;
    PyObject *cpy_r_r853;
    PyObject *cpy_r_r854;
    PyObject *cpy_r_r855;
    PyObject *cpy_r_r856;
    PyObject *cpy_r_r857;
    PyObject *cpy_r_r858;
    CPyPtr cpy_r_r859;
    CPyPtr cpy_r_r860;
    CPyPtr cpy_r_r861;
    PyObject *cpy_r_r862;
    PyObject *cpy_r_r863;
    PyObject *cpy_r_r864;
    PyObject *cpy_r_r865;
    PyObject *cpy_r_r866;
    PyObject *cpy_r_r867;
    PyObject *cpy_r_r868;
    PyObject *cpy_r_r869;
    PyObject *cpy_r_r870;
    PyObject *cpy_r_r871;
    PyObject *cpy_r_r872;
    PyObject *cpy_r_r873;
    PyObject *cpy_r_r874;
    PyObject *cpy_r_r875;
    PyObject *cpy_r_r876;
    PyObject *cpy_r_r877;
    PyObject *cpy_r_r878;
    PyObject *cpy_r_r879;
    CPyPtr cpy_r_r880;
    CPyPtr cpy_r_r881;
    PyObject *cpy_r_r882;
    PyObject *cpy_r_r883;
    PyObject *cpy_r_r884;
    PyObject *cpy_r_r885;
    PyObject *cpy_r_r886;
    PyObject *cpy_r_r887;
    PyObject *cpy_r_r888;
    PyObject *cpy_r_r889;
    PyObject *cpy_r_r890;
    PyObject *cpy_r_r891;
    PyObject *cpy_r_r892;
    PyObject *cpy_r_r893;
    PyObject *cpy_r_r894;
    PyObject *cpy_r_r895;
    PyObject *cpy_r_r896;
    PyObject *cpy_r_r897;
    PyObject *cpy_r_r898;
    PyObject *cpy_r_r899;
    PyObject *cpy_r_r900;
    PyObject *cpy_r_r901;
    PyObject *cpy_r_r902;
    PyObject *cpy_r_r903;
    PyObject *cpy_r_r904;
    PyObject *cpy_r_r905;
    PyObject *cpy_r_r906;
    PyObject *cpy_r_r907;
    PyObject *cpy_r_r908;
    PyObject *cpy_r_r909;
    PyObject *cpy_r_r910;
    PyObject *cpy_r_r911;
    PyObject *cpy_r_r912;
    PyObject *cpy_r_r913;
    PyObject *cpy_r_r914;
    PyObject *cpy_r_r915;
    PyObject *cpy_r_r916;
    PyObject *cpy_r_r917;
    PyObject *cpy_r_r918;
    PyObject *cpy_r_r919;
    PyObject *cpy_r_r920;
    PyObject *cpy_r_r921;
    PyObject *cpy_r_r922;
    PyObject *cpy_r_r923;
    PyObject *cpy_r_r924;
    PyObject *cpy_r_r925;
    PyObject *cpy_r_r926;
    PyObject *cpy_r_r927;
    CPyPtr cpy_r_r928;
    CPyPtr cpy_r_r929;
    CPyPtr cpy_r_r930;
    CPyPtr cpy_r_r931;
    CPyPtr cpy_r_r932;
    CPyPtr cpy_r_r933;
    PyObject *cpy_r_r934;
    PyObject *cpy_r_r935;
    PyObject *cpy_r_r936;
    PyObject *cpy_r_r937;
    PyObject *cpy_r_r938;
    PyObject *cpy_r_r939;
    PyObject *cpy_r_r940;
    PyObject *cpy_r_r941;
    PyObject *cpy_r_r942;
    PyObject *cpy_r_r943;
    PyObject *cpy_r_r944;
    PyObject *cpy_r_r945;
    PyObject *cpy_r_r946;
    PyObject *cpy_r_r947;
    PyObject *cpy_r_r948;
    PyObject *cpy_r_r949;
    PyObject *cpy_r_r950;
    PyObject *cpy_r_r951;
    PyObject *cpy_r_r952;
    PyObject *cpy_r_r953;
    PyObject *cpy_r_r954;
    PyObject *cpy_r_r955;
    PyObject *cpy_r_r956;
    PyObject *cpy_r_r957;
    PyObject *cpy_r_r958;
    CPyPtr cpy_r_r959;
    CPyPtr cpy_r_r960;
    CPyPtr cpy_r_r961;
    PyObject *cpy_r_r962;
    PyObject *cpy_r_r963;
    PyObject *cpy_r_r964;
    PyObject *cpy_r_r965;
    PyObject *cpy_r_r966;
    PyObject *cpy_r_r967;
    PyObject *cpy_r_r968;
    PyObject *cpy_r_r969;
    PyObject *cpy_r_r970;
    PyObject *cpy_r_r971;
    PyObject *cpy_r_r972;
    PyObject *cpy_r_r973;
    PyObject *cpy_r_r974;
    PyObject *cpy_r_r975;
    PyObject *cpy_r_r976;
    PyObject *cpy_r_r977;
    PyObject *cpy_r_r978;
    PyObject *cpy_r_r979;
    CPyPtr cpy_r_r980;
    CPyPtr cpy_r_r981;
    PyObject *cpy_r_r982;
    PyObject *cpy_r_r983;
    PyObject *cpy_r_r984;
    PyObject *cpy_r_r985;
    PyObject *cpy_r_r986;
    PyObject *cpy_r_r987;
    PyObject *cpy_r_r988;
    PyObject *cpy_r_r989;
    PyObject *cpy_r_r990;
    PyObject *cpy_r_r991;
    PyObject *cpy_r_r992;
    PyObject *cpy_r_r993;
    PyObject *cpy_r_r994;
    PyObject *cpy_r_r995;
    PyObject *cpy_r_r996;
    PyObject *cpy_r_r997;
    PyObject *cpy_r_r998;
    PyObject *cpy_r_r999;
    PyObject *cpy_r_r1000;
    PyObject *cpy_r_r1001;
    PyObject *cpy_r_r1002;
    PyObject *cpy_r_r1003;
    PyObject *cpy_r_r1004;
    PyObject *cpy_r_r1005;
    PyObject *cpy_r_r1006;
    PyObject *cpy_r_r1007;
    PyObject *cpy_r_r1008;
    PyObject *cpy_r_r1009;
    PyObject *cpy_r_r1010;
    PyObject *cpy_r_r1011;
    PyObject *cpy_r_r1012;
    PyObject *cpy_r_r1013;
    PyObject *cpy_r_r1014;
    PyObject *cpy_r_r1015;
    PyObject *cpy_r_r1016;
    PyObject *cpy_r_r1017;
    PyObject *cpy_r_r1018;
    PyObject *cpy_r_r1019;
    PyObject *cpy_r_r1020;
    PyObject *cpy_r_r1021;
    PyObject *cpy_r_r1022;
    CPyPtr cpy_r_r1023;
    CPyPtr cpy_r_r1024;
    PyObject *cpy_r_r1025;
    PyObject *cpy_r_r1026;
    PyObject *cpy_r_r1027;
    PyObject *cpy_r_r1028;
    PyObject *cpy_r_r1029;
    PyObject *cpy_r_r1030;
    PyObject *cpy_r_r1031;
    PyObject *cpy_r_r1032;
    CPyPtr cpy_r_r1033;
    CPyPtr cpy_r_r1034;
    CPyPtr cpy_r_r1035;
    CPyPtr cpy_r_r1036;
    PyObject *cpy_r_r1037;
    PyObject *cpy_r_r1038;
    PyObject *cpy_r_r1039;
    PyObject *cpy_r_r1040;
    PyObject *cpy_r_r1041;
    PyObject *cpy_r_r1042;
    PyObject *cpy_r_r1043;
    PyObject *cpy_r_r1044;
    CPyPtr cpy_r_r1045;
    CPyPtr cpy_r_r1046;
    CPyPtr cpy_r_r1047;
    PyObject *cpy_r_r1048;
    PyObject *cpy_r_r1049;
    PyObject *cpy_r_r1050;
    PyObject *cpy_r_r1051;
    PyObject *cpy_r_r1052;
    PyObject *cpy_r_r1053;
    PyObject *cpy_r_r1054;
    PyObject *cpy_r_r1055;
    PyObject *cpy_r_r1056;
    PyObject *cpy_r_r1057;
    PyObject *cpy_r_r1058;
    PyObject *cpy_r_r1059;
    PyObject *cpy_r_r1060;
    PyObject *cpy_r_r1061;
    PyObject *cpy_r_r1062;
    PyObject *cpy_r_r1063;
    PyObject *cpy_r_r1064;
    PyObject *cpy_r_r1065;
    PyObject *cpy_r_r1066;
    PyObject *cpy_r_r1067;
    PyObject *cpy_r_r1068;
    PyObject *cpy_r_r1069;
    PyObject *cpy_r_r1070;
    PyObject *cpy_r_r1071;
    PyObject *cpy_r_r1072;
    PyObject *cpy_r_r1073;
    PyObject *cpy_r_r1074;
    PyObject *cpy_r_r1075;
    PyObject *cpy_r_r1076;
    PyObject *cpy_r_r1077;
    PyObject *cpy_r_r1078;
    PyObject *cpy_r_r1079;
    PyObject *cpy_r_r1080;
    PyObject *cpy_r_r1081;
    PyObject *cpy_r_r1082;
    PyObject *cpy_r_r1083;
    PyObject *cpy_r_r1084;
    PyObject *cpy_r_r1085;
    PyObject *cpy_r_r1086;
    CPyPtr cpy_r_r1087;
    CPyPtr cpy_r_r1088;
    CPyPtr cpy_r_r1089;
    CPyPtr cpy_r_r1090;
    CPyPtr cpy_r_r1091;
    PyObject *cpy_r_r1092;
    PyObject *cpy_r_r1093;
    PyObject *cpy_r_r1094;
    PyObject *cpy_r_r1095;
    PyObject *cpy_r_r1096;
    PyObject *cpy_r_r1097;
    PyObject *cpy_r_r1098;
    PyObject *cpy_r_r1099;
    PyObject *cpy_r_r1100;
    PyObject *cpy_r_r1101;
    PyObject *cpy_r_r1102;
    PyObject *cpy_r_r1103;
    int32_t cpy_r_r1104;
    char cpy_r_r1105;
    PyObject *cpy_r_r1106;
    PyObject *cpy_r_r1107;
    PyObject *cpy_r_r1108;
    PyObject *cpy_r_r1109;
    PyObject *cpy_r_r1110;
    PyObject *cpy_r_r1111;
    PyObject *cpy_r_r1112;
    PyObject *cpy_r_r1113;
    PyObject *cpy_r_r1114;
    PyObject *cpy_r_r1115;
    PyObject *cpy_r_r1116;
    PyObject *cpy_r_r1117;
    PyObject *cpy_r_r1118;
    PyObject *cpy_r_r1119;
    PyObject *cpy_r_r1120;
    PyObject *cpy_r_r1121;
    PyObject *cpy_r_r1122;
    PyObject *cpy_r_r1123;
    int32_t cpy_r_r1124;
    char cpy_r_r1125;
    char cpy_r_r1126;
    cpy_r_r0 = CPyModule_builtins;
    cpy_r_r1 = (PyObject *)&_Py_NoneStruct;
    cpy_r_r2 = cpy_r_r0 != cpy_r_r1;
    if (cpy_r_r2) goto CPyL3;
    cpy_r_r3 = CPyStatics[3]; /* 'builtins' */
    cpy_r_r4 = PyImport_Import(cpy_r_r3);
    if (unlikely(cpy_r_r4 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", -1, CPyStatic_globals);
        goto CPyL179;
    }
    CPyModule_builtins = cpy_r_r4;
    CPy_INCREF(CPyModule_builtins);
    CPy_DECREF(cpy_r_r4);
CPyL3: ;
    cpy_r_r5 = CPyStatics[4]; /* '0x6080604052348015600e575f5ffd5b506118238061001c5f395ff3fe608060405234801561000f575f5ffd5b50600436106100cd575f3560e01c8063966b50e01161008a578063acabb9ed11610064578063acabb9ed146101cd578063b2ddc449146101e9578063e17bf95614610205578063f82ef69e14610221576100cd565b8063966b50e0146101795780639c37705314610195578063aa6fd822146101b1576100cd565b80630bb563d6146100d157806317c0c180146100ed57806320f0256e146101095780632c0e6fde146101255780635da86c171461014157806390b41d8b1461015d575b5f5ffd5b6100eb60048036038101906100e69190610b73565b61023d565b005b61010760048036038101906101029190610bdd565b610277565b005b610123600480360381019061011e9190610c3b565b61034e565b005b61013f600480360381019061013a9190610d0c565b61046b565b005b61015b60048036038101906101569190610e3d565b6104c5565b005b61017760048036038101906101729190610e7b565b610502565b005b610193600480360381019061018e9190610fe4565b61065f565b005b6101af60048036038101906101aa919061105a565b6106b0565b005b6101cb60048036038101906101c691906110be565b6107c8565b005b6101e760048036038101906101e291906110fc565b61090c565b005b61020360048036038101906101fe9190611172565b61095d565b005b61021f600480360381019061021a919061124e565b6109af565b005b61023b60048036038101906102369190611172565b6109e9565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405161026c91906112f5565b60405180910390a150565b6001601381111561028b5761028a611315565b5b81601381111561029e5761029d611315565b5b036102d4577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60405160405180910390a161034b565b5f60138111156102e7576102e6611315565b5b8160138111156102fa576102f9611315565b5b0361030f5760405160405180910390a061034a565b6040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610341906113b2565b60405180910390fd5b5b50565b6005601381111561036257610361611315565b5b85601381111561037557610374611315565b5b036103bc577ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf9848484846040516103af94939291906113df565b60405180910390a1610464565b600b60138111156103d0576103cf611315565b5b8560138111156103e3576103e2611315565b5b036104285780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b5868660405161041b929190611422565b60405180910390a3610463565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161045a906113b2565b60405180910390fd5b5b5050505050565b838573ffffffffffffffffffffffffffffffffffffffff167fd5adc9babd0133de6cececc75e340da3fc18ae5ccab91bc1c03ff3b194f9a3c18585856040516104b693929190611458565b60405180910390a35050505050565b7f8ccce2523cca5f3851d20df50b5a59509bc4ac7d9ddba344f5e331969d09b8e782826040516104f69291906114fd565b60405180910390a15050565b6003601381111561051657610515611315565b5b83601381111561052957610528611315565b5b0361056c577fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5828260405161055f929190611422565b60405180910390a161065a565b600960138111156105805761057f611315565b5b83601381111561059357610592611315565b5b036105d557807f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca836040516105c89190611524565b60405180910390a2610659565b600860138111156105e9576105e8611315565b5b8360138111156105fc576105fb611315565b5b0361061d5780826040516106109190611524565b60405180910390a1610658565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161064f906113b2565b60405180910390fd5b5b5b505050565b8160405161066d91906115ee565b60405180910390207fdbc4c1d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040516106a49190611696565b60405180910390a25050565b600460138111156106c4576106c3611315565b5b8460138111156106d7576106d6611315565b5b0361071c577f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5506283838360405161070f939291906116b6565b60405180910390a16107c2565b600a60138111156107305761072f611315565b5b84601381111561074357610742611315565b5b036107865780827ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec856040516107799190611524565b60405180910390a36107c1565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107b8906113b2565b60405180910390fd5b5b50505050565b600260138111156107dc576107db611315565b5b8260138111156107ef576107ee611315565b5b03610830577f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516108239190611524565b60405180910390a1610908565b6007601381111561084457610843611315565b5b82601381111561085757610856611315565b5b0361088e57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a2610907565b600660138111156108a2576108a1611315565b5b8260138111156108b5576108b4611315565b5b036108cb578060405160405180910390a1610906565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108fd906113b2565b60405180910390fd5b5b5b5050565b8160405161091a9190611725565b60405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405161095191906112f5565b60405180910390a25050565b8173ffffffffffffffffffffffffffffffffffffffff167ff922c215689548d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c826040516109a3919061173b565b60405180910390a25050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040516109de91906117a6565b60405180910390a150565b7f06029e18f16caae06a69281f35b00ed3fcf47950e6c99dafa1bdd8c4b93479a08282604051610a1a9291906117c6565b60405180910390a15050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610a8582610a3f565b810181811067ffffffffffffffff82111715610aa457610aa3610a4f565b5b80604052505050565b5f610ab6610a26565b9050610ac28282610a7c565b919050565b5f67ffffffffffffffff821115610ae157610ae0610a4f565b5b610aea82610a3f565b9050602081019050919050565b828183375f83830152505050565b5f610b17610b1284610ac7565b610aad565b905082815260208101848484011115610b3357610b32610a3b565b5b610b3e848285610af7565b509392505050565b5f82601f830112610b5a57610b59610a37565b5b8135610b6a848260208601610b05565b91505092915050565b5f60208284031215610b8857610b87610a2f565b5b5f82013567ffffffffffffffff811115610ba557610ba4610a33565b5b610bb184828501610b46565b91505092915050565b60148110610bc6575f5ffd5b50565b5f81359050610bd781610bba565b92915050565b5f60208284031215610bf257610bf1610a2f565b5b5f610bff84828501610bc9565b91505092915050565b5f819050919050565b610c1a81610c08565b8114610c24575f5ffd5b50565b5f81359050610c3581610c11565b92915050565b5f5f5f5f5f60a08688031215610c5457610c53610a2f565b5b5f610c6188828901610bc9565b9550506020610c7288828901610c27565b9450506040610c8388828901610c27565b9350506060610c9488828901610c27565b9250506080610ca588828901610c27565b9150509295509295909350565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610cdb82610cb2565b9050919050565b610ceb81610cd1565b8114610cf5575f5ffd5b50565b5f81359050610d0681610ce2565b92915050565b5f5f5f5f5f60a08688031215610d2557610d24610a2f565b5b5f610d3288828901610cf8565b9550506020610d4388828901610c27565b9450506040610d5488828901610cf8565b9350506060610d6588828901610c27565b925050608086013567ffffffffffffffff811115610d8657610d85610a33565b5b610d9288828901610b46565b9150509295509295909350565b5f5ffd5b5f60208284031215610db857610db7610d9f565b5b610dc26020610aad565b90505f610dd184828501610c27565b5f8301525092915050565b5f60608284031215610df157610df0610d9f565b5b610dfb6060610aad565b90505f610e0a84828501610c27565b5f830152506020610e1d84828501610c27565b6020830152506040610e3184828501610da3565b60408301525092915050565b5f5f60808385031215610e5357610e52610a2f565b5b5f610e6085828601610c27565b9250506020610e7185828601610ddc565b9150509250929050565b5f5f5f60608486031215610e9257610e91610a2f565b5b5f610e9f86828701610bc9565b9350506020610eb086828701610c27565b9250506040610ec186828701610c27565b9150509250925092565b5f67ffffffffffffffff821115610ee557610ee4610a4f565b5b602082029050602081019050919050565b5f5ffd5b5f7fffff00000000000000000000000000000000000000000000000000000000000082169050919050565b610f2e81610efa565b8114610f38575f5ffd5b50565b5f81359050610f4981610f25565b92915050565b5f610f61610f5c84610ecb565b610aad565b90508083825260208201905060208402830185811115610f8457610f83610ef6565b5b835b81811015610fad5780610f998882610f3b565b845260208401935050602081019050610f86565b5050509392505050565b5f82601f830112610fcb57610fca610a37565b5b8135610fdb848260208601610f4f565b91505092915050565b5f5f60408385031215610ffa57610ff9610a2f565b5b5f83013567ffffffffffffffff81111561101757611016610a33565b5b61102385828601610fb7565b925050602083013567ffffffffffffffff81111561104457611043610a33565b5b61105085828601610fb7565b9150509250929050565b5f5f5f5f6080858703121561107257611071610a2f565b5b5f61107f87828801610bc9565b945050602061109087828801610c27565b93505060406110a187828801610c27565b92505060606110b287828801610c27565b91505092959194509250565b5f5f604083850312156110d4576110d3610a2f565b5b5f6110e185828601610bc9565b92505060206110f285828601610c27565b9150509250929050565b5f5f6040838503121561111257611111610a2f565b5b5f83013567ffffffffffffffff81111561112f5761112e610a33565b5b61113b85828601610b46565b925050602083013567ffffffffffffffff81111561115c5761115b610a33565b5b61116885828601610b46565b9150509250929050565b5f5f6040838503121561118857611187610a2f565b5b5f61119585828601610cf8565b92505060206111a685828601610cf8565b9150509250929050565b5f67ffffffffffffffff8211156111ca576111c9610a4f565b5b6111d382610a3f565b9050602081019050919050565b5f6111f26111ed846111b0565b610aad565b90508281526020810184848401111561120e5761120d610a3b565b5b611219848285610af7565b509392505050565b5f82601f83011261123557611234610a37565b5b81356112458482602086016111e0565b91505092915050565b5f6020828403121561126357611262610a2f565b5b5f82013567ffffffffffffffff8111156112805761127f610a33565b5b61128c84828501611221565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6112c782611295565b6112d1818561129f565b93506112e18185602086016112af565b6112ea81610a3f565b840191505092915050565b5f6020820190508181035f83015261130d81846112bd565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4469646e2774206d6174636820616e7920616c6c6f7761626c65206576656e745f8201527f20696e6465780000000000000000000000000000000000000000000000000000602082015250565b5f61139c60268361129f565b91506113a782611342565b604082019050919050565b5f6020820190508181035f8301526113c981611390565b9050919050565b6113d981610c08565b82525050565b5f6080820190506113f25f8301876113d0565b6113ff60208301866113d0565b61140c60408301856113d0565b61141960608301846113d0565b95945050505050565b5f6040820190506114355f8301856113d0565b61144260208301846113d0565b9392505050565b61145281610cd1565b82525050565b5f60608201905061146b5f830186611449565b61147860208301856113d0565b818103604083015261148a81846112bd565b9050949350505050565b61149d81610c08565b82525050565b602082015f8201516114b75f850182611494565b50505050565b606082015f8201516114d15f850182611494565b5060208201516114e46020850182611494565b5060408201516114f760408501826114a3565b50505050565b5f6080820190506115105f8301856113d0565b61151d60208301846114bd565b9392505050565b5f6020820190506115375f8301846113d0565b92915050565b5f81519050919050565b5f81905092915050565b5f819050602082019050919050565b61156981610efa565b82525050565b5f61157a8383611560565b60208301905092915050565b5f602082019050919050565b5f61159c8261153d565b6115a68185611547565b93506115b183611551565b805f5b838110156115e15781516115c8888261156f565b97506115d383611586565b9250506001810190506115b4565b5085935050505092915050565b5f6115f98284611592565b915081905092915050565b5f82825260208201905092915050565b61161d81610efa565b82525050565b5f61162e8383611614565b60208301905092915050565b5f6116448261153d565b61164e8185611604565b935061165983611551565b805f5b838110156116895781516116708882611623565b975061167b83611586565b92505060018101905061165c565b5085935050505092915050565b5f6020820190508181035f8301526116ae818461163a565b905092915050565b5f6060820190506116c95f8301866113d0565b6116d660208301856113d0565b6116e360408301846113d0565b949350505050565b5f81905092915050565b5f6116ff82611295565b61170981856116eb565b93506117198185602086016112af565b80840191505092915050565b5f61173082846116f5565b915081905092915050565b5f60208201905061174e5f830184611449565b92915050565b5f81519050919050565b5f82825260208201905092915050565b5f61177882611754565b611782818561175e565b93506117928185602086016112af565b61179b81610a3f565b840191505092915050565b5f6020820190508181035f8301526117be818461176e565b905092915050565b5f6040820190506117d95f830185611449565b6117e66020830184611449565b939250505056fea264697066735822122003376e7a5d27c43ad43676e9f1efff563c626b7d1b96bd09006b9562e3dc714b64736f6c634300081e0033' */
    cpy_r_r6 = CPyStatic_globals;
    cpy_r_r7 = CPyStatics[5]; /* 'EMITTER_CONTRACT_BYTECODE' */
    cpy_r_r8 = CPyDict_SetItem(cpy_r_r6, cpy_r_r7, cpy_r_r5);
    cpy_r_r9 = cpy_r_r8 >= 0;
    if (unlikely(!cpy_r_r9)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 7, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r10 = CPyStatics[6]; /* '0x608060405234801561000f575f5ffd5b50600436106100cd575f3560e01c8063966b50e01161008a578063acabb9ed11610064578063acabb9ed146101cd578063b2ddc449146101e9578063e17bf95614610205578063f82ef69e14610221576100cd565b8063966b50e0146101795780639c37705314610195578063aa6fd822146101b1576100cd565b80630bb563d6146100d157806317c0c180146100ed57806320f0256e146101095780632c0e6fde146101255780635da86c171461014157806390b41d8b1461015d575b5f5ffd5b6100eb60048036038101906100e69190610b73565b61023d565b005b61010760048036038101906101029190610bdd565b610277565b005b610123600480360381019061011e9190610c3b565b61034e565b005b61013f600480360381019061013a9190610d0c565b61046b565b005b61015b60048036038101906101569190610e3d565b6104c5565b005b61017760048036038101906101729190610e7b565b610502565b005b610193600480360381019061018e9190610fe4565b61065f565b005b6101af60048036038101906101aa919061105a565b6106b0565b005b6101cb60048036038101906101c691906110be565b6107c8565b005b6101e760048036038101906101e291906110fc565b61090c565b005b61020360048036038101906101fe9190611172565b61095d565b005b61021f600480360381019061021a919061124e565b6109af565b005b61023b60048036038101906102369190611172565b6109e9565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405161026c91906112f5565b60405180910390a150565b6001601381111561028b5761028a611315565b5b81601381111561029e5761029d611315565b5b036102d4577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60405160405180910390a161034b565b5f60138111156102e7576102e6611315565b5b8160138111156102fa576102f9611315565b5b0361030f5760405160405180910390a061034a565b6040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610341906113b2565b60405180910390fd5b5b50565b6005601381111561036257610361611315565b5b85601381111561037557610374611315565b5b036103bc577ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf9848484846040516103af94939291906113df565b60405180910390a1610464565b600b60138111156103d0576103cf611315565b5b8560138111156103e3576103e2611315565b5b036104285780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b5868660405161041b929190611422565b60405180910390a3610463565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161045a906113b2565b60405180910390fd5b5b5050505050565b838573ffffffffffffffffffffffffffffffffffffffff167fd5adc9babd0133de6cececc75e340da3fc18ae5ccab91bc1c03ff3b194f9a3c18585856040516104b693929190611458565b60405180910390a35050505050565b7f8ccce2523cca5f3851d20df50b5a59509bc4ac7d9ddba344f5e331969d09b8e782826040516104f69291906114fd565b60405180910390a15050565b6003601381111561051657610515611315565b5b83601381111561052957610528611315565b5b0361056c577fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5828260405161055f929190611422565b60405180910390a161065a565b600960138111156105805761057f611315565b5b83601381111561059357610592611315565b5b036105d557807f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca836040516105c89190611524565b60405180910390a2610659565b600860138111156105e9576105e8611315565b5b8360138111156105fc576105fb611315565b5b0361061d5780826040516106109190611524565b60405180910390a1610658565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161064f906113b2565b60405180910390fd5b5b5b505050565b8160405161066d91906115ee565b60405180910390207fdbc4c1d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040516106a49190611696565b60405180910390a25050565b600460138111156106c4576106c3611315565b5b8460138111156106d7576106d6611315565b5b0361071c577f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5506283838360405161070f939291906116b6565b60405180910390a16107c2565b600a60138111156107305761072f611315565b5b84601381111561074357610742611315565b5b036107865780827ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec856040516107799190611524565b60405180910390a36107c1565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107b8906113b2565b60405180910390fd5b5b50505050565b600260138111156107dc576107db611315565b5b8260138111156107ef576107ee611315565b5b03610830577f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516108239190611524565b60405180910390a1610908565b6007601381111561084457610843611315565b5b82601381111561085757610856611315565b5b0361088e57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a2610907565b600660138111156108a2576108a1611315565b5b8260138111156108b5576108b4611315565b5b036108cb578060405160405180910390a1610906565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108fd906113b2565b60405180910390fd5b5b5b5050565b8160405161091a9190611725565b60405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405161095191906112f5565b60405180910390a25050565b8173ffffffffffffffffffffffffffffffffffffffff167ff922c215689548d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c826040516109a3919061173b565b60405180910390a25050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040516109de91906117a6565b60405180910390a150565b7f06029e18f16caae06a69281f35b00ed3fcf47950e6c99dafa1bdd8c4b93479a08282604051610a1a9291906117c6565b60405180910390a15050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610a8582610a3f565b810181811067ffffffffffffffff82111715610aa457610aa3610a4f565b5b80604052505050565b5f610ab6610a26565b9050610ac28282610a7c565b919050565b5f67ffffffffffffffff821115610ae157610ae0610a4f565b5b610aea82610a3f565b9050602081019050919050565b828183375f83830152505050565b5f610b17610b1284610ac7565b610aad565b905082815260208101848484011115610b3357610b32610a3b565b5b610b3e848285610af7565b509392505050565b5f82601f830112610b5a57610b59610a37565b5b8135610b6a848260208601610b05565b91505092915050565b5f60208284031215610b8857610b87610a2f565b5b5f82013567ffffffffffffffff811115610ba557610ba4610a33565b5b610bb184828501610b46565b91505092915050565b60148110610bc6575f5ffd5b50565b5f81359050610bd781610bba565b92915050565b5f60208284031215610bf257610bf1610a2f565b5b5f610bff84828501610bc9565b91505092915050565b5f819050919050565b610c1a81610c08565b8114610c24575f5ffd5b50565b5f81359050610c3581610c11565b92915050565b5f5f5f5f5f60a08688031215610c5457610c53610a2f565b5b5f610c6188828901610bc9565b9550506020610c7288828901610c27565b9450506040610c8388828901610c27565b9350506060610c9488828901610c27565b9250506080610ca588828901610c27565b9150509295509295909350565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610cdb82610cb2565b9050919050565b610ceb81610cd1565b8114610cf5575f5ffd5b50565b5f81359050610d0681610ce2565b92915050565b5f5f5f5f5f60a08688031215610d2557610d24610a2f565b5b5f610d3288828901610cf8565b9550506020610d4388828901610c27565b9450506040610d5488828901610cf8565b9350506060610d6588828901610c27565b925050608086013567ffffffffffffffff811115610d8657610d85610a33565b5b610d9288828901610b46565b9150509295509295909350565b5f5ffd5b5f60208284031215610db857610db7610d9f565b5b610dc26020610aad565b90505f610dd184828501610c27565b5f8301525092915050565b5f60608284031215610df157610df0610d9f565b5b610dfb6060610aad565b90505f610e0a84828501610c27565b5f830152506020610e1d84828501610c27565b6020830152506040610e3184828501610da3565b60408301525092915050565b5f5f60808385031215610e5357610e52610a2f565b5b5f610e6085828601610c27565b9250506020610e7185828601610ddc565b9150509250929050565b5f5f5f60608486031215610e9257610e91610a2f565b5b5f610e9f86828701610bc9565b9350506020610eb086828701610c27565b9250506040610ec186828701610c27565b9150509250925092565b5f67ffffffffffffffff821115610ee557610ee4610a4f565b5b602082029050602081019050919050565b5f5ffd5b5f7fffff00000000000000000000000000000000000000000000000000000000000082169050919050565b610f2e81610efa565b8114610f38575f5ffd5b50565b5f81359050610f4981610f25565b92915050565b5f610f61610f5c84610ecb565b610aad565b90508083825260208201905060208402830185811115610f8457610f83610ef6565b5b835b81811015610fad5780610f998882610f3b565b845260208401935050602081019050610f86565b5050509392505050565b5f82601f830112610fcb57610fca610a37565b5b8135610fdb848260208601610f4f565b91505092915050565b5f5f60408385031215610ffa57610ff9610a2f565b5b5f83013567ffffffffffffffff81111561101757611016610a33565b5b61102385828601610fb7565b925050602083013567ffffffffffffffff81111561104457611043610a33565b5b61105085828601610fb7565b9150509250929050565b5f5f5f5f6080858703121561107257611071610a2f565b5b5f61107f87828801610bc9565b945050602061109087828801610c27565b93505060406110a187828801610c27565b92505060606110b287828801610c27565b91505092959194509250565b5f5f604083850312156110d4576110d3610a2f565b5b5f6110e185828601610bc9565b92505060206110f285828601610c27565b9150509250929050565b5f5f6040838503121561111257611111610a2f565b5b5f83013567ffffffffffffffff81111561112f5761112e610a33565b5b61113b85828601610b46565b925050602083013567ffffffffffffffff81111561115c5761115b610a33565b5b61116885828601610b46565b9150509250929050565b5f5f6040838503121561118857611187610a2f565b5b5f61119585828601610cf8565b92505060206111a685828601610cf8565b9150509250929050565b5f67ffffffffffffffff8211156111ca576111c9610a4f565b5b6111d382610a3f565b9050602081019050919050565b5f6111f26111ed846111b0565b610aad565b90508281526020810184848401111561120e5761120d610a3b565b5b611219848285610af7565b509392505050565b5f82601f83011261123557611234610a37565b5b81356112458482602086016111e0565b91505092915050565b5f6020828403121561126357611262610a2f565b5b5f82013567ffffffffffffffff8111156112805761127f610a33565b5b61128c84828501611221565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6112c782611295565b6112d1818561129f565b93506112e18185602086016112af565b6112ea81610a3f565b840191505092915050565b5f6020820190508181035f83015261130d81846112bd565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4469646e2774206d6174636820616e7920616c6c6f7761626c65206576656e745f8201527f20696e6465780000000000000000000000000000000000000000000000000000602082015250565b5f61139c60268361129f565b91506113a782611342565b604082019050919050565b5f6020820190508181035f8301526113c981611390565b9050919050565b6113d981610c08565b82525050565b5f6080820190506113f25f8301876113d0565b6113ff60208301866113d0565b61140c60408301856113d0565b61141960608301846113d0565b95945050505050565b5f6040820190506114355f8301856113d0565b61144260208301846113d0565b9392505050565b61145281610cd1565b82525050565b5f60608201905061146b5f830186611449565b61147860208301856113d0565b818103604083015261148a81846112bd565b9050949350505050565b61149d81610c08565b82525050565b602082015f8201516114b75f850182611494565b50505050565b606082015f8201516114d15f850182611494565b5060208201516114e46020850182611494565b5060408201516114f760408501826114a3565b50505050565b5f6080820190506115105f8301856113d0565b61151d60208301846114bd565b9392505050565b5f6020820190506115375f8301846113d0565b92915050565b5f81519050919050565b5f81905092915050565b5f819050602082019050919050565b61156981610efa565b82525050565b5f61157a8383611560565b60208301905092915050565b5f602082019050919050565b5f61159c8261153d565b6115a68185611547565b93506115b183611551565b805f5b838110156115e15781516115c8888261156f565b97506115d383611586565b9250506001810190506115b4565b5085935050505092915050565b5f6115f98284611592565b915081905092915050565b5f82825260208201905092915050565b61161d81610efa565b82525050565b5f61162e8383611614565b60208301905092915050565b5f6116448261153d565b61164e8185611604565b935061165983611551565b805f5b838110156116895781516116708882611623565b975061167b83611586565b92505060018101905061165c565b5085935050505092915050565b5f6020820190508181035f8301526116ae818461163a565b905092915050565b5f6060820190506116c95f8301866113d0565b6116d660208301856113d0565b6116e360408301846113d0565b949350505050565b5f81905092915050565b5f6116ff82611295565b61170981856116eb565b93506117198185602086016112af565b80840191505092915050565b5f61173082846116f5565b915081905092915050565b5f60208201905061174e5f830184611449565b92915050565b5f81519050919050565b5f82825260208201905092915050565b5f61177882611754565b611782818561175e565b93506117928185602086016112af565b61179b81610a3f565b840191505092915050565b5f6020820190508181035f8301526117be818461176e565b905092915050565b5f6040820190506117d95f830185611449565b6117e66020830184611449565b939250505056fea264697066735822122003376e7a5d27c43ad43676e9f1efff563c626b7d1b96bd09006b9562e3dc714b64736f6c634300081e0033' */
    cpy_r_r11 = CPyStatic_globals;
    cpy_r_r12 = CPyStatics[7]; /* 'EMITTER_CONTRACT_RUNTIME' */
    cpy_r_r13 = CPyDict_SetItem(cpy_r_r11, cpy_r_r12, cpy_r_r10);
    cpy_r_r14 = cpy_r_r13 >= 0;
    if (unlikely(!cpy_r_r14)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 8, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r15 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r16 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r17 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r18 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r19 = CPyStatics[12]; /* 'address' */
    cpy_r_r20 = CPyStatics[13]; /* 'name' */
    cpy_r_r21 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r22 = CPyStatics[15]; /* 'type' */
    cpy_r_r23 = CPyStatics[12]; /* 'address' */
    cpy_r_r24 = 1 ? Py_True : Py_False;
    cpy_r_r25 = CPyDict_Build(4, cpy_r_r17, cpy_r_r24, cpy_r_r18, cpy_r_r19, cpy_r_r20, cpy_r_r21, cpy_r_r22, cpy_r_r23);
    if (unlikely(cpy_r_r25 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 13, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r26 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r27 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r28 = CPyStatics[12]; /* 'address' */
    cpy_r_r29 = CPyStatics[13]; /* 'name' */
    cpy_r_r30 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r31 = CPyStatics[15]; /* 'type' */
    cpy_r_r32 = CPyStatics[12]; /* 'address' */
    cpy_r_r33 = 0 ? Py_True : Py_False;
    cpy_r_r34 = CPyDict_Build(4, cpy_r_r26, cpy_r_r33, cpy_r_r27, cpy_r_r28, cpy_r_r29, cpy_r_r30, cpy_r_r31, cpy_r_r32);
    if (unlikely(cpy_r_r34 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 19, CPyStatic_globals);
        goto CPyL180;
    }
    cpy_r_r35 = PyList_New(2);
    if (unlikely(cpy_r_r35 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 12, CPyStatic_globals);
        goto CPyL181;
    }
    cpy_r_r36 = (CPyPtr)&((PyListObject *)cpy_r_r35)->ob_item;
    cpy_r_r37 = *(CPyPtr *)cpy_r_r36;
    *(PyObject * *)cpy_r_r37 = cpy_r_r25;
    cpy_r_r38 = cpy_r_r37 + 8;
    *(PyObject * *)cpy_r_r38 = cpy_r_r34;
    cpy_r_r39 = CPyStatics[13]; /* 'name' */
    cpy_r_r40 = CPyStatics[17]; /* 'LogAddressIndexed' */
    cpy_r_r41 = CPyStatics[15]; /* 'type' */
    cpy_r_r42 = CPyStatics[18]; /* 'event' */
    cpy_r_r43 = 0 ? Py_True : Py_False;
    cpy_r_r44 = CPyDict_Build(4, cpy_r_r15, cpy_r_r43, cpy_r_r16, cpy_r_r35, cpy_r_r39, cpy_r_r40, cpy_r_r41, cpy_r_r42);
    CPy_DECREF_NO_IMM(cpy_r_r35);
    if (unlikely(cpy_r_r44 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 10, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r45 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r46 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r47 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r48 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r49 = CPyStatics[12]; /* 'address' */
    cpy_r_r50 = CPyStatics[13]; /* 'name' */
    cpy_r_r51 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r52 = CPyStatics[15]; /* 'type' */
    cpy_r_r53 = CPyStatics[12]; /* 'address' */
    cpy_r_r54 = 0 ? Py_True : Py_False;
    cpy_r_r55 = CPyDict_Build(4, cpy_r_r47, cpy_r_r54, cpy_r_r48, cpy_r_r49, cpy_r_r50, cpy_r_r51, cpy_r_r52, cpy_r_r53);
    if (unlikely(cpy_r_r55 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 32, CPyStatic_globals);
        goto CPyL182;
    }
    cpy_r_r56 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r57 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r58 = CPyStatics[12]; /* 'address' */
    cpy_r_r59 = CPyStatics[13]; /* 'name' */
    cpy_r_r60 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r61 = CPyStatics[15]; /* 'type' */
    cpy_r_r62 = CPyStatics[12]; /* 'address' */
    cpy_r_r63 = 0 ? Py_True : Py_False;
    cpy_r_r64 = CPyDict_Build(4, cpy_r_r56, cpy_r_r63, cpy_r_r57, cpy_r_r58, cpy_r_r59, cpy_r_r60, cpy_r_r61, cpy_r_r62);
    if (unlikely(cpy_r_r64 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 38, CPyStatic_globals);
        goto CPyL183;
    }
    cpy_r_r65 = PyList_New(2);
    if (unlikely(cpy_r_r65 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 31, CPyStatic_globals);
        goto CPyL184;
    }
    cpy_r_r66 = (CPyPtr)&((PyListObject *)cpy_r_r65)->ob_item;
    cpy_r_r67 = *(CPyPtr *)cpy_r_r66;
    *(PyObject * *)cpy_r_r67 = cpy_r_r55;
    cpy_r_r68 = cpy_r_r67 + 8;
    *(PyObject * *)cpy_r_r68 = cpy_r_r64;
    cpy_r_r69 = CPyStatics[13]; /* 'name' */
    cpy_r_r70 = CPyStatics[19]; /* 'LogAddressNotIndexed' */
    cpy_r_r71 = CPyStatics[15]; /* 'type' */
    cpy_r_r72 = CPyStatics[18]; /* 'event' */
    cpy_r_r73 = 0 ? Py_True : Py_False;
    cpy_r_r74 = CPyDict_Build(4, cpy_r_r45, cpy_r_r73, cpy_r_r46, cpy_r_r65, cpy_r_r69, cpy_r_r70, cpy_r_r71, cpy_r_r72);
    CPy_DECREF_NO_IMM(cpy_r_r65);
    if (unlikely(cpy_r_r74 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 29, CPyStatic_globals);
        goto CPyL182;
    }
    cpy_r_r75 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r76 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r77 = PyList_New(0);
    if (unlikely(cpy_r_r77 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL185;
    }
    cpy_r_r78 = CPyStatics[13]; /* 'name' */
    cpy_r_r79 = CPyStatics[20]; /* 'LogAnonymous' */
    cpy_r_r80 = CPyStatics[15]; /* 'type' */
    cpy_r_r81 = CPyStatics[18]; /* 'event' */
    cpy_r_r82 = 1 ? Py_True : Py_False;
    cpy_r_r83 = CPyDict_Build(4, cpy_r_r75, cpy_r_r82, cpy_r_r76, cpy_r_r77, cpy_r_r78, cpy_r_r79, cpy_r_r80, cpy_r_r81);
    CPy_DECREF_NO_IMM(cpy_r_r77);
    if (unlikely(cpy_r_r83 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 48, CPyStatic_globals);
        goto CPyL185;
    }
    cpy_r_r84 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r85 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r86 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r87 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r88 = CPyStatics[21]; /* 'bytes' */
    cpy_r_r89 = CPyStatics[13]; /* 'name' */
    cpy_r_r90 = CPyStatics[22]; /* 'v' */
    cpy_r_r91 = CPyStatics[15]; /* 'type' */
    cpy_r_r92 = CPyStatics[21]; /* 'bytes' */
    cpy_r_r93 = 0 ? Py_True : Py_False;
    cpy_r_r94 = CPyDict_Build(4, cpy_r_r86, cpy_r_r93, cpy_r_r87, cpy_r_r88, cpy_r_r89, cpy_r_r90, cpy_r_r91, cpy_r_r92);
    if (unlikely(cpy_r_r94 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 52, CPyStatic_globals);
        goto CPyL186;
    }
    cpy_r_r95 = PyList_New(1);
    if (unlikely(cpy_r_r95 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 51, CPyStatic_globals);
        goto CPyL187;
    }
    cpy_r_r96 = (CPyPtr)&((PyListObject *)cpy_r_r95)->ob_item;
    cpy_r_r97 = *(CPyPtr *)cpy_r_r96;
    *(PyObject * *)cpy_r_r97 = cpy_r_r94;
    cpy_r_r98 = CPyStatics[13]; /* 'name' */
    cpy_r_r99 = CPyStatics[23]; /* 'LogBytes' */
    cpy_r_r100 = CPyStatics[15]; /* 'type' */
    cpy_r_r101 = CPyStatics[18]; /* 'event' */
    cpy_r_r102 = 0 ? Py_True : Py_False;
    cpy_r_r103 = CPyDict_Build(4, cpy_r_r84, cpy_r_r102, cpy_r_r85, cpy_r_r95, cpy_r_r98, cpy_r_r99, cpy_r_r100, cpy_r_r101);
    CPy_DECREF_NO_IMM(cpy_r_r95);
    if (unlikely(cpy_r_r103 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 49, CPyStatic_globals);
        goto CPyL186;
    }
    cpy_r_r104 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r105 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r106 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r107 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r108 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r109 = CPyStatics[13]; /* 'name' */
    cpy_r_r110 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r111 = CPyStatics[15]; /* 'type' */
    cpy_r_r112 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r113 = 0 ? Py_True : Py_False;
    cpy_r_r114 = CPyDict_Build(4, cpy_r_r106, cpy_r_r113, cpy_r_r107, cpy_r_r108, cpy_r_r109, cpy_r_r110, cpy_r_r111, cpy_r_r112);
    if (unlikely(cpy_r_r114 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 60, CPyStatic_globals);
        goto CPyL188;
    }
    cpy_r_r115 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r116 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r117 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r118 = CPyStatics[13]; /* 'name' */
    cpy_r_r119 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r120 = CPyStatics[15]; /* 'type' */
    cpy_r_r121 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r122 = 1 ? Py_True : Py_False;
    cpy_r_r123 = CPyDict_Build(4, cpy_r_r115, cpy_r_r122, cpy_r_r116, cpy_r_r117, cpy_r_r118, cpy_r_r119, cpy_r_r120, cpy_r_r121);
    if (unlikely(cpy_r_r123 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 66, CPyStatic_globals);
        goto CPyL189;
    }
    cpy_r_r124 = PyList_New(2);
    if (unlikely(cpy_r_r124 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 59, CPyStatic_globals);
        goto CPyL190;
    }
    cpy_r_r125 = (CPyPtr)&((PyListObject *)cpy_r_r124)->ob_item;
    cpy_r_r126 = *(CPyPtr *)cpy_r_r125;
    *(PyObject * *)cpy_r_r126 = cpy_r_r114;
    cpy_r_r127 = cpy_r_r126 + 8;
    *(PyObject * *)cpy_r_r127 = cpy_r_r123;
    cpy_r_r128 = CPyStatics[13]; /* 'name' */
    cpy_r_r129 = CPyStatics[25]; /* 'LogDoubleAnonymous' */
    cpy_r_r130 = CPyStatics[15]; /* 'type' */
    cpy_r_r131 = CPyStatics[18]; /* 'event' */
    cpy_r_r132 = 1 ? Py_True : Py_False;
    cpy_r_r133 = CPyDict_Build(4, cpy_r_r104, cpy_r_r132, cpy_r_r105, cpy_r_r124, cpy_r_r128, cpy_r_r129, cpy_r_r130, cpy_r_r131);
    CPy_DECREF_NO_IMM(cpy_r_r124);
    if (unlikely(cpy_r_r133 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 57, CPyStatic_globals);
        goto CPyL188;
    }
    cpy_r_r134 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r135 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r136 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r137 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r138 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r139 = CPyStatics[13]; /* 'name' */
    cpy_r_r140 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r141 = CPyStatics[15]; /* 'type' */
    cpy_r_r142 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r143 = 0 ? Py_True : Py_False;
    cpy_r_r144 = CPyDict_Build(4, cpy_r_r136, cpy_r_r143, cpy_r_r137, cpy_r_r138, cpy_r_r139, cpy_r_r140, cpy_r_r141, cpy_r_r142);
    if (unlikely(cpy_r_r144 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 79, CPyStatic_globals);
        goto CPyL191;
    }
    cpy_r_r145 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r146 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r147 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r148 = CPyStatics[13]; /* 'name' */
    cpy_r_r149 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r150 = CPyStatics[15]; /* 'type' */
    cpy_r_r151 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r152 = 0 ? Py_True : Py_False;
    cpy_r_r153 = CPyDict_Build(4, cpy_r_r145, cpy_r_r152, cpy_r_r146, cpy_r_r147, cpy_r_r148, cpy_r_r149, cpy_r_r150, cpy_r_r151);
    if (unlikely(cpy_r_r153 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 85, CPyStatic_globals);
        goto CPyL192;
    }
    cpy_r_r154 = PyList_New(2);
    if (unlikely(cpy_r_r154 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 78, CPyStatic_globals);
        goto CPyL193;
    }
    cpy_r_r155 = (CPyPtr)&((PyListObject *)cpy_r_r154)->ob_item;
    cpy_r_r156 = *(CPyPtr *)cpy_r_r155;
    *(PyObject * *)cpy_r_r156 = cpy_r_r144;
    cpy_r_r157 = cpy_r_r156 + 8;
    *(PyObject * *)cpy_r_r157 = cpy_r_r153;
    cpy_r_r158 = CPyStatics[13]; /* 'name' */
    cpy_r_r159 = CPyStatics[26]; /* 'LogDoubleArg' */
    cpy_r_r160 = CPyStatics[15]; /* 'type' */
    cpy_r_r161 = CPyStatics[18]; /* 'event' */
    cpy_r_r162 = 0 ? Py_True : Py_False;
    cpy_r_r163 = CPyDict_Build(4, cpy_r_r134, cpy_r_r162, cpy_r_r135, cpy_r_r154, cpy_r_r158, cpy_r_r159, cpy_r_r160, cpy_r_r161);
    CPy_DECREF_NO_IMM(cpy_r_r154);
    if (unlikely(cpy_r_r163 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 76, CPyStatic_globals);
        goto CPyL191;
    }
    cpy_r_r164 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r165 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r166 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r167 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r168 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r169 = CPyStatics[13]; /* 'name' */
    cpy_r_r170 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r171 = CPyStatics[15]; /* 'type' */
    cpy_r_r172 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r173 = 0 ? Py_True : Py_False;
    cpy_r_r174 = CPyDict_Build(4, cpy_r_r166, cpy_r_r173, cpy_r_r167, cpy_r_r168, cpy_r_r169, cpy_r_r170, cpy_r_r171, cpy_r_r172);
    if (unlikely(cpy_r_r174 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 98, CPyStatic_globals);
        goto CPyL194;
    }
    cpy_r_r175 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r176 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r177 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r178 = CPyStatics[13]; /* 'name' */
    cpy_r_r179 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r180 = CPyStatics[15]; /* 'type' */
    cpy_r_r181 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r182 = 1 ? Py_True : Py_False;
    cpy_r_r183 = CPyDict_Build(4, cpy_r_r175, cpy_r_r182, cpy_r_r176, cpy_r_r177, cpy_r_r178, cpy_r_r179, cpy_r_r180, cpy_r_r181);
    if (unlikely(cpy_r_r183 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 104, CPyStatic_globals);
        goto CPyL195;
    }
    cpy_r_r184 = PyList_New(2);
    if (unlikely(cpy_r_r184 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 97, CPyStatic_globals);
        goto CPyL196;
    }
    cpy_r_r185 = (CPyPtr)&((PyListObject *)cpy_r_r184)->ob_item;
    cpy_r_r186 = *(CPyPtr *)cpy_r_r185;
    *(PyObject * *)cpy_r_r186 = cpy_r_r174;
    cpy_r_r187 = cpy_r_r186 + 8;
    *(PyObject * *)cpy_r_r187 = cpy_r_r183;
    cpy_r_r188 = CPyStatics[13]; /* 'name' */
    cpy_r_r189 = CPyStatics[27]; /* 'LogDoubleWithIndex' */
    cpy_r_r190 = CPyStatics[15]; /* 'type' */
    cpy_r_r191 = CPyStatics[18]; /* 'event' */
    cpy_r_r192 = 0 ? Py_True : Py_False;
    cpy_r_r193 = CPyDict_Build(4, cpy_r_r164, cpy_r_r192, cpy_r_r165, cpy_r_r184, cpy_r_r188, cpy_r_r189, cpy_r_r190, cpy_r_r191);
    CPy_DECREF_NO_IMM(cpy_r_r184);
    if (unlikely(cpy_r_r193 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 95, CPyStatic_globals);
        goto CPyL194;
    }
    cpy_r_r194 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r195 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r196 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r197 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r198 = CPyStatics[28]; /* 'string' */
    cpy_r_r199 = CPyStatics[13]; /* 'name' */
    cpy_r_r200 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r201 = CPyStatics[15]; /* 'type' */
    cpy_r_r202 = CPyStatics[28]; /* 'string' */
    cpy_r_r203 = 1 ? Py_True : Py_False;
    cpy_r_r204 = CPyDict_Build(4, cpy_r_r196, cpy_r_r203, cpy_r_r197, cpy_r_r198, cpy_r_r199, cpy_r_r200, cpy_r_r201, cpy_r_r202);
    if (unlikely(cpy_r_r204 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 117, CPyStatic_globals);
        goto CPyL197;
    }
    cpy_r_r205 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r206 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r207 = CPyStatics[28]; /* 'string' */
    cpy_r_r208 = CPyStatics[13]; /* 'name' */
    cpy_r_r209 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r210 = CPyStatics[15]; /* 'type' */
    cpy_r_r211 = CPyStatics[28]; /* 'string' */
    cpy_r_r212 = 0 ? Py_True : Py_False;
    cpy_r_r213 = CPyDict_Build(4, cpy_r_r205, cpy_r_r212, cpy_r_r206, cpy_r_r207, cpy_r_r208, cpy_r_r209, cpy_r_r210, cpy_r_r211);
    if (unlikely(cpy_r_r213 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 123, CPyStatic_globals);
        goto CPyL198;
    }
    cpy_r_r214 = PyList_New(2);
    if (unlikely(cpy_r_r214 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 116, CPyStatic_globals);
        goto CPyL199;
    }
    cpy_r_r215 = (CPyPtr)&((PyListObject *)cpy_r_r214)->ob_item;
    cpy_r_r216 = *(CPyPtr *)cpy_r_r215;
    *(PyObject * *)cpy_r_r216 = cpy_r_r204;
    cpy_r_r217 = cpy_r_r216 + 8;
    *(PyObject * *)cpy_r_r217 = cpy_r_r213;
    cpy_r_r218 = CPyStatics[13]; /* 'name' */
    cpy_r_r219 = CPyStatics[29]; /* 'LogDynamicArgs' */
    cpy_r_r220 = CPyStatics[15]; /* 'type' */
    cpy_r_r221 = CPyStatics[18]; /* 'event' */
    cpy_r_r222 = 0 ? Py_True : Py_False;
    cpy_r_r223 = CPyDict_Build(4, cpy_r_r194, cpy_r_r222, cpy_r_r195, cpy_r_r214, cpy_r_r218, cpy_r_r219, cpy_r_r220, cpy_r_r221);
    CPy_DECREF_NO_IMM(cpy_r_r214);
    if (unlikely(cpy_r_r223 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 114, CPyStatic_globals);
        goto CPyL197;
    }
    cpy_r_r224 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r225 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r226 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r227 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r228 = CPyStatics[12]; /* 'address' */
    cpy_r_r229 = CPyStatics[13]; /* 'name' */
    cpy_r_r230 = CPyStatics[30]; /* 'indexedAddress' */
    cpy_r_r231 = CPyStatics[15]; /* 'type' */
    cpy_r_r232 = CPyStatics[12]; /* 'address' */
    cpy_r_r233 = 1 ? Py_True : Py_False;
    cpy_r_r234 = CPyDict_Build(4, cpy_r_r226, cpy_r_r233, cpy_r_r227, cpy_r_r228, cpy_r_r229, cpy_r_r230, cpy_r_r231, cpy_r_r232);
    if (unlikely(cpy_r_r234 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 136, CPyStatic_globals);
        goto CPyL200;
    }
    cpy_r_r235 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r236 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r237 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r238 = CPyStatics[13]; /* 'name' */
    cpy_r_r239 = CPyStatics[31]; /* 'indexedUint256' */
    cpy_r_r240 = CPyStatics[15]; /* 'type' */
    cpy_r_r241 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r242 = 1 ? Py_True : Py_False;
    cpy_r_r243 = CPyDict_Build(4, cpy_r_r235, cpy_r_r242, cpy_r_r236, cpy_r_r237, cpy_r_r238, cpy_r_r239, cpy_r_r240, cpy_r_r241);
    if (unlikely(cpy_r_r243 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 142, CPyStatic_globals);
        goto CPyL201;
    }
    cpy_r_r244 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r245 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r246 = CPyStatics[12]; /* 'address' */
    cpy_r_r247 = CPyStatics[13]; /* 'name' */
    cpy_r_r248 = CPyStatics[32]; /* 'nonIndexedAddress' */
    cpy_r_r249 = CPyStatics[15]; /* 'type' */
    cpy_r_r250 = CPyStatics[12]; /* 'address' */
    cpy_r_r251 = 0 ? Py_True : Py_False;
    cpy_r_r252 = CPyDict_Build(4, cpy_r_r244, cpy_r_r251, cpy_r_r245, cpy_r_r246, cpy_r_r247, cpy_r_r248, cpy_r_r249, cpy_r_r250);
    if (unlikely(cpy_r_r252 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 148, CPyStatic_globals);
        goto CPyL202;
    }
    cpy_r_r253 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r254 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r255 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r256 = CPyStatics[13]; /* 'name' */
    cpy_r_r257 = CPyStatics[33]; /* 'nonIndexedUint256' */
    cpy_r_r258 = CPyStatics[15]; /* 'type' */
    cpy_r_r259 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r260 = 0 ? Py_True : Py_False;
    cpy_r_r261 = CPyDict_Build(4, cpy_r_r253, cpy_r_r260, cpy_r_r254, cpy_r_r255, cpy_r_r256, cpy_r_r257, cpy_r_r258, cpy_r_r259);
    if (unlikely(cpy_r_r261 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 154, CPyStatic_globals);
        goto CPyL203;
    }
    cpy_r_r262 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r263 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r264 = CPyStatics[28]; /* 'string' */
    cpy_r_r265 = CPyStatics[13]; /* 'name' */
    cpy_r_r266 = CPyStatics[34]; /* 'nonIndexedString' */
    cpy_r_r267 = CPyStatics[15]; /* 'type' */
    cpy_r_r268 = CPyStatics[28]; /* 'string' */
    cpy_r_r269 = 0 ? Py_True : Py_False;
    cpy_r_r270 = CPyDict_Build(4, cpy_r_r262, cpy_r_r269, cpy_r_r263, cpy_r_r264, cpy_r_r265, cpy_r_r266, cpy_r_r267, cpy_r_r268);
    if (unlikely(cpy_r_r270 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 160, CPyStatic_globals);
        goto CPyL204;
    }
    cpy_r_r271 = PyList_New(5);
    if (unlikely(cpy_r_r271 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 135, CPyStatic_globals);
        goto CPyL205;
    }
    cpy_r_r272 = (CPyPtr)&((PyListObject *)cpy_r_r271)->ob_item;
    cpy_r_r273 = *(CPyPtr *)cpy_r_r272;
    *(PyObject * *)cpy_r_r273 = cpy_r_r234;
    cpy_r_r274 = cpy_r_r273 + 8;
    *(PyObject * *)cpy_r_r274 = cpy_r_r243;
    cpy_r_r275 = cpy_r_r273 + 16;
    *(PyObject * *)cpy_r_r275 = cpy_r_r252;
    cpy_r_r276 = cpy_r_r273 + 24;
    *(PyObject * *)cpy_r_r276 = cpy_r_r261;
    cpy_r_r277 = cpy_r_r273 + 32;
    *(PyObject * *)cpy_r_r277 = cpy_r_r270;
    cpy_r_r278 = CPyStatics[13]; /* 'name' */
    cpy_r_r279 = CPyStatics[35]; /* 'LogIndexedAndNotIndexed' */
    cpy_r_r280 = CPyStatics[15]; /* 'type' */
    cpy_r_r281 = CPyStatics[18]; /* 'event' */
    cpy_r_r282 = 0 ? Py_True : Py_False;
    cpy_r_r283 = CPyDict_Build(4, cpy_r_r224, cpy_r_r282, cpy_r_r225, cpy_r_r271, cpy_r_r278, cpy_r_r279, cpy_r_r280, cpy_r_r281);
    CPy_DECREF_NO_IMM(cpy_r_r271);
    if (unlikely(cpy_r_r283 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 133, CPyStatic_globals);
        goto CPyL200;
    }
    cpy_r_r284 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r285 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r286 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r287 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r288 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r289 = CPyStatics[13]; /* 'name' */
    cpy_r_r290 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r291 = CPyStatics[15]; /* 'type' */
    cpy_r_r292 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r293 = 1 ? Py_True : Py_False;
    cpy_r_r294 = CPyDict_Build(4, cpy_r_r286, cpy_r_r293, cpy_r_r287, cpy_r_r288, cpy_r_r289, cpy_r_r290, cpy_r_r291, cpy_r_r292);
    if (unlikely(cpy_r_r294 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 173, CPyStatic_globals);
        goto CPyL206;
    }
    cpy_r_r295 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r296 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r297 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r298 = CPyStatics[13]; /* 'name' */
    cpy_r_r299 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r300 = CPyStatics[15]; /* 'type' */
    cpy_r_r301 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r302 = 0 ? Py_True : Py_False;
    cpy_r_r303 = CPyDict_Build(4, cpy_r_r295, cpy_r_r302, cpy_r_r296, cpy_r_r297, cpy_r_r298, cpy_r_r299, cpy_r_r300, cpy_r_r301);
    if (unlikely(cpy_r_r303 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 179, CPyStatic_globals);
        goto CPyL207;
    }
    cpy_r_r304 = PyList_New(2);
    if (unlikely(cpy_r_r304 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 172, CPyStatic_globals);
        goto CPyL208;
    }
    cpy_r_r305 = (CPyPtr)&((PyListObject *)cpy_r_r304)->ob_item;
    cpy_r_r306 = *(CPyPtr *)cpy_r_r305;
    *(PyObject * *)cpy_r_r306 = cpy_r_r294;
    cpy_r_r307 = cpy_r_r306 + 8;
    *(PyObject * *)cpy_r_r307 = cpy_r_r303;
    cpy_r_r308 = CPyStatics[13]; /* 'name' */
    cpy_r_r309 = CPyStatics[37]; /* 'LogListArgs' */
    cpy_r_r310 = CPyStatics[15]; /* 'type' */
    cpy_r_r311 = CPyStatics[18]; /* 'event' */
    cpy_r_r312 = 0 ? Py_True : Py_False;
    cpy_r_r313 = CPyDict_Build(4, cpy_r_r284, cpy_r_r312, cpy_r_r285, cpy_r_r304, cpy_r_r308, cpy_r_r309, cpy_r_r310, cpy_r_r311);
    CPy_DECREF_NO_IMM(cpy_r_r304);
    if (unlikely(cpy_r_r313 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 170, CPyStatic_globals);
        goto CPyL206;
    }
    cpy_r_r314 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r315 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r316 = PyList_New(0);
    if (unlikely(cpy_r_r316 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 189, CPyStatic_globals);
        goto CPyL209;
    }
    cpy_r_r317 = CPyStatics[13]; /* 'name' */
    cpy_r_r318 = CPyStatics[38]; /* 'LogNoArguments' */
    cpy_r_r319 = CPyStatics[15]; /* 'type' */
    cpy_r_r320 = CPyStatics[18]; /* 'event' */
    cpy_r_r321 = 0 ? Py_True : Py_False;
    cpy_r_r322 = CPyDict_Build(4, cpy_r_r314, cpy_r_r321, cpy_r_r315, cpy_r_r316, cpy_r_r317, cpy_r_r318, cpy_r_r319, cpy_r_r320);
    CPy_DECREF_NO_IMM(cpy_r_r316);
    if (unlikely(cpy_r_r322 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 189, CPyStatic_globals);
        goto CPyL209;
    }
    cpy_r_r323 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r324 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r325 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r326 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r327 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r328 = CPyStatics[13]; /* 'name' */
    cpy_r_r329 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r330 = CPyStatics[15]; /* 'type' */
    cpy_r_r331 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r332 = 0 ? Py_True : Py_False;
    cpy_r_r333 = CPyDict_Build(4, cpy_r_r325, cpy_r_r332, cpy_r_r326, cpy_r_r327, cpy_r_r328, cpy_r_r329, cpy_r_r330, cpy_r_r331);
    if (unlikely(cpy_r_r333 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 193, CPyStatic_globals);
        goto CPyL210;
    }
    cpy_r_r334 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r335 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r336 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r337 = CPyStatics[13]; /* 'name' */
    cpy_r_r338 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r339 = CPyStatics[15]; /* 'type' */
    cpy_r_r340 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r341 = 0 ? Py_True : Py_False;
    cpy_r_r342 = CPyDict_Build(4, cpy_r_r334, cpy_r_r341, cpy_r_r335, cpy_r_r336, cpy_r_r337, cpy_r_r338, cpy_r_r339, cpy_r_r340);
    if (unlikely(cpy_r_r342 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 199, CPyStatic_globals);
        goto CPyL211;
    }
    cpy_r_r343 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r344 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r345 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r346 = CPyStatics[13]; /* 'name' */
    cpy_r_r347 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r348 = CPyStatics[15]; /* 'type' */
    cpy_r_r349 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r350 = 0 ? Py_True : Py_False;
    cpy_r_r351 = CPyDict_Build(4, cpy_r_r343, cpy_r_r350, cpy_r_r344, cpy_r_r345, cpy_r_r346, cpy_r_r347, cpy_r_r348, cpy_r_r349);
    if (unlikely(cpy_r_r351 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 205, CPyStatic_globals);
        goto CPyL212;
    }
    cpy_r_r352 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r353 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r354 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r355 = CPyStatics[13]; /* 'name' */
    cpy_r_r356 = CPyStatics[40]; /* 'arg3' */
    cpy_r_r357 = CPyStatics[15]; /* 'type' */
    cpy_r_r358 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r359 = 0 ? Py_True : Py_False;
    cpy_r_r360 = CPyDict_Build(4, cpy_r_r352, cpy_r_r359, cpy_r_r353, cpy_r_r354, cpy_r_r355, cpy_r_r356, cpy_r_r357, cpy_r_r358);
    if (unlikely(cpy_r_r360 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 211, CPyStatic_globals);
        goto CPyL213;
    }
    cpy_r_r361 = PyList_New(4);
    if (unlikely(cpy_r_r361 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 192, CPyStatic_globals);
        goto CPyL214;
    }
    cpy_r_r362 = (CPyPtr)&((PyListObject *)cpy_r_r361)->ob_item;
    cpy_r_r363 = *(CPyPtr *)cpy_r_r362;
    *(PyObject * *)cpy_r_r363 = cpy_r_r333;
    cpy_r_r364 = cpy_r_r363 + 8;
    *(PyObject * *)cpy_r_r364 = cpy_r_r342;
    cpy_r_r365 = cpy_r_r363 + 16;
    *(PyObject * *)cpy_r_r365 = cpy_r_r351;
    cpy_r_r366 = cpy_r_r363 + 24;
    *(PyObject * *)cpy_r_r366 = cpy_r_r360;
    cpy_r_r367 = CPyStatics[13]; /* 'name' */
    cpy_r_r368 = CPyStatics[41]; /* 'LogQuadrupleArg' */
    cpy_r_r369 = CPyStatics[15]; /* 'type' */
    cpy_r_r370 = CPyStatics[18]; /* 'event' */
    cpy_r_r371 = 0 ? Py_True : Py_False;
    cpy_r_r372 = CPyDict_Build(4, cpy_r_r323, cpy_r_r371, cpy_r_r324, cpy_r_r361, cpy_r_r367, cpy_r_r368, cpy_r_r369, cpy_r_r370);
    CPy_DECREF_NO_IMM(cpy_r_r361);
    if (unlikely(cpy_r_r372 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 190, CPyStatic_globals);
        goto CPyL210;
    }
    cpy_r_r373 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r374 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r375 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r376 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r377 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r378 = CPyStatics[13]; /* 'name' */
    cpy_r_r379 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r380 = CPyStatics[15]; /* 'type' */
    cpy_r_r381 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r382 = 0 ? Py_True : Py_False;
    cpy_r_r383 = CPyDict_Build(4, cpy_r_r375, cpy_r_r382, cpy_r_r376, cpy_r_r377, cpy_r_r378, cpy_r_r379, cpy_r_r380, cpy_r_r381);
    if (unlikely(cpy_r_r383 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 224, CPyStatic_globals);
        goto CPyL215;
    }
    cpy_r_r384 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r385 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r386 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r387 = CPyStatics[13]; /* 'name' */
    cpy_r_r388 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r389 = CPyStatics[15]; /* 'type' */
    cpy_r_r390 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r391 = 0 ? Py_True : Py_False;
    cpy_r_r392 = CPyDict_Build(4, cpy_r_r384, cpy_r_r391, cpy_r_r385, cpy_r_r386, cpy_r_r387, cpy_r_r388, cpy_r_r389, cpy_r_r390);
    if (unlikely(cpy_r_r392 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 230, CPyStatic_globals);
        goto CPyL216;
    }
    cpy_r_r393 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r394 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r395 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r396 = CPyStatics[13]; /* 'name' */
    cpy_r_r397 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r398 = CPyStatics[15]; /* 'type' */
    cpy_r_r399 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r400 = 1 ? Py_True : Py_False;
    cpy_r_r401 = CPyDict_Build(4, cpy_r_r393, cpy_r_r400, cpy_r_r394, cpy_r_r395, cpy_r_r396, cpy_r_r397, cpy_r_r398, cpy_r_r399);
    if (unlikely(cpy_r_r401 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 236, CPyStatic_globals);
        goto CPyL217;
    }
    cpy_r_r402 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r403 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r404 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r405 = CPyStatics[13]; /* 'name' */
    cpy_r_r406 = CPyStatics[40]; /* 'arg3' */
    cpy_r_r407 = CPyStatics[15]; /* 'type' */
    cpy_r_r408 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r409 = 1 ? Py_True : Py_False;
    cpy_r_r410 = CPyDict_Build(4, cpy_r_r402, cpy_r_r409, cpy_r_r403, cpy_r_r404, cpy_r_r405, cpy_r_r406, cpy_r_r407, cpy_r_r408);
    if (unlikely(cpy_r_r410 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 242, CPyStatic_globals);
        goto CPyL218;
    }
    cpy_r_r411 = PyList_New(4);
    if (unlikely(cpy_r_r411 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 223, CPyStatic_globals);
        goto CPyL219;
    }
    cpy_r_r412 = (CPyPtr)&((PyListObject *)cpy_r_r411)->ob_item;
    cpy_r_r413 = *(CPyPtr *)cpy_r_r412;
    *(PyObject * *)cpy_r_r413 = cpy_r_r383;
    cpy_r_r414 = cpy_r_r413 + 8;
    *(PyObject * *)cpy_r_r414 = cpy_r_r392;
    cpy_r_r415 = cpy_r_r413 + 16;
    *(PyObject * *)cpy_r_r415 = cpy_r_r401;
    cpy_r_r416 = cpy_r_r413 + 24;
    *(PyObject * *)cpy_r_r416 = cpy_r_r410;
    cpy_r_r417 = CPyStatics[13]; /* 'name' */
    cpy_r_r418 = CPyStatics[42]; /* 'LogQuadrupleWithIndex' */
    cpy_r_r419 = CPyStatics[15]; /* 'type' */
    cpy_r_r420 = CPyStatics[18]; /* 'event' */
    cpy_r_r421 = 0 ? Py_True : Py_False;
    cpy_r_r422 = CPyDict_Build(4, cpy_r_r373, cpy_r_r421, cpy_r_r374, cpy_r_r411, cpy_r_r417, cpy_r_r418, cpy_r_r419, cpy_r_r420);
    CPy_DECREF_NO_IMM(cpy_r_r411);
    if (unlikely(cpy_r_r422 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 221, CPyStatic_globals);
        goto CPyL215;
    }
    cpy_r_r423 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r424 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r425 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r426 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r427 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r428 = CPyStatics[13]; /* 'name' */
    cpy_r_r429 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r430 = CPyStatics[15]; /* 'type' */
    cpy_r_r431 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r432 = 1 ? Py_True : Py_False;
    cpy_r_r433 = CPyDict_Build(4, cpy_r_r425, cpy_r_r432, cpy_r_r426, cpy_r_r427, cpy_r_r428, cpy_r_r429, cpy_r_r430, cpy_r_r431);
    if (unlikely(cpy_r_r433 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 255, CPyStatic_globals);
        goto CPyL220;
    }
    cpy_r_r434 = PyList_New(1);
    if (unlikely(cpy_r_r434 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 254, CPyStatic_globals);
        goto CPyL221;
    }
    cpy_r_r435 = (CPyPtr)&((PyListObject *)cpy_r_r434)->ob_item;
    cpy_r_r436 = *(CPyPtr *)cpy_r_r435;
    *(PyObject * *)cpy_r_r436 = cpy_r_r433;
    cpy_r_r437 = CPyStatics[13]; /* 'name' */
    cpy_r_r438 = CPyStatics[43]; /* 'LogSingleAnonymous' */
    cpy_r_r439 = CPyStatics[15]; /* 'type' */
    cpy_r_r440 = CPyStatics[18]; /* 'event' */
    cpy_r_r441 = 1 ? Py_True : Py_False;
    cpy_r_r442 = CPyDict_Build(4, cpy_r_r423, cpy_r_r441, cpy_r_r424, cpy_r_r434, cpy_r_r437, cpy_r_r438, cpy_r_r439, cpy_r_r440);
    CPy_DECREF_NO_IMM(cpy_r_r434);
    if (unlikely(cpy_r_r442 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 252, CPyStatic_globals);
        goto CPyL220;
    }
    cpy_r_r443 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r444 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r445 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r446 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r447 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r448 = CPyStatics[13]; /* 'name' */
    cpy_r_r449 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r450 = CPyStatics[15]; /* 'type' */
    cpy_r_r451 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r452 = 0 ? Py_True : Py_False;
    cpy_r_r453 = CPyDict_Build(4, cpy_r_r445, cpy_r_r452, cpy_r_r446, cpy_r_r447, cpy_r_r448, cpy_r_r449, cpy_r_r450, cpy_r_r451);
    if (unlikely(cpy_r_r453 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 268, CPyStatic_globals);
        goto CPyL222;
    }
    cpy_r_r454 = PyList_New(1);
    if (unlikely(cpy_r_r454 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 267, CPyStatic_globals);
        goto CPyL223;
    }
    cpy_r_r455 = (CPyPtr)&((PyListObject *)cpy_r_r454)->ob_item;
    cpy_r_r456 = *(CPyPtr *)cpy_r_r455;
    *(PyObject * *)cpy_r_r456 = cpy_r_r453;
    cpy_r_r457 = CPyStatics[13]; /* 'name' */
    cpy_r_r458 = CPyStatics[44]; /* 'LogSingleArg' */
    cpy_r_r459 = CPyStatics[15]; /* 'type' */
    cpy_r_r460 = CPyStatics[18]; /* 'event' */
    cpy_r_r461 = 0 ? Py_True : Py_False;
    cpy_r_r462 = CPyDict_Build(4, cpy_r_r443, cpy_r_r461, cpy_r_r444, cpy_r_r454, cpy_r_r457, cpy_r_r458, cpy_r_r459, cpy_r_r460);
    CPy_DECREF_NO_IMM(cpy_r_r454);
    if (unlikely(cpy_r_r462 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 265, CPyStatic_globals);
        goto CPyL222;
    }
    cpy_r_r463 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r464 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r465 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r466 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r467 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r468 = CPyStatics[13]; /* 'name' */
    cpy_r_r469 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r470 = CPyStatics[15]; /* 'type' */
    cpy_r_r471 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r472 = 1 ? Py_True : Py_False;
    cpy_r_r473 = CPyDict_Build(4, cpy_r_r465, cpy_r_r472, cpy_r_r466, cpy_r_r467, cpy_r_r468, cpy_r_r469, cpy_r_r470, cpy_r_r471);
    if (unlikely(cpy_r_r473 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 281, CPyStatic_globals);
        goto CPyL224;
    }
    cpy_r_r474 = PyList_New(1);
    if (unlikely(cpy_r_r474 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 280, CPyStatic_globals);
        goto CPyL225;
    }
    cpy_r_r475 = (CPyPtr)&((PyListObject *)cpy_r_r474)->ob_item;
    cpy_r_r476 = *(CPyPtr *)cpy_r_r475;
    *(PyObject * *)cpy_r_r476 = cpy_r_r473;
    cpy_r_r477 = CPyStatics[13]; /* 'name' */
    cpy_r_r478 = CPyStatics[45]; /* 'LogSingleWithIndex' */
    cpy_r_r479 = CPyStatics[15]; /* 'type' */
    cpy_r_r480 = CPyStatics[18]; /* 'event' */
    cpy_r_r481 = 0 ? Py_True : Py_False;
    cpy_r_r482 = CPyDict_Build(4, cpy_r_r463, cpy_r_r481, cpy_r_r464, cpy_r_r474, cpy_r_r477, cpy_r_r478, cpy_r_r479, cpy_r_r480);
    CPy_DECREF_NO_IMM(cpy_r_r474);
    if (unlikely(cpy_r_r482 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 278, CPyStatic_globals);
        goto CPyL224;
    }
    cpy_r_r483 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r484 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r485 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r486 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r487 = CPyStatics[28]; /* 'string' */
    cpy_r_r488 = CPyStatics[13]; /* 'name' */
    cpy_r_r489 = CPyStatics[22]; /* 'v' */
    cpy_r_r490 = CPyStatics[15]; /* 'type' */
    cpy_r_r491 = CPyStatics[28]; /* 'string' */
    cpy_r_r492 = 0 ? Py_True : Py_False;
    cpy_r_r493 = CPyDict_Build(4, cpy_r_r485, cpy_r_r492, cpy_r_r486, cpy_r_r487, cpy_r_r488, cpy_r_r489, cpy_r_r490, cpy_r_r491);
    if (unlikely(cpy_r_r493 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 294, CPyStatic_globals);
        goto CPyL226;
    }
    cpy_r_r494 = PyList_New(1);
    if (unlikely(cpy_r_r494 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 293, CPyStatic_globals);
        goto CPyL227;
    }
    cpy_r_r495 = (CPyPtr)&((PyListObject *)cpy_r_r494)->ob_item;
    cpy_r_r496 = *(CPyPtr *)cpy_r_r495;
    *(PyObject * *)cpy_r_r496 = cpy_r_r493;
    cpy_r_r497 = CPyStatics[13]; /* 'name' */
    cpy_r_r498 = CPyStatics[46]; /* 'LogString' */
    cpy_r_r499 = CPyStatics[15]; /* 'type' */
    cpy_r_r500 = CPyStatics[18]; /* 'event' */
    cpy_r_r501 = 0 ? Py_True : Py_False;
    cpy_r_r502 = CPyDict_Build(4, cpy_r_r483, cpy_r_r501, cpy_r_r484, cpy_r_r494, cpy_r_r497, cpy_r_r498, cpy_r_r499, cpy_r_r500);
    CPy_DECREF_NO_IMM(cpy_r_r494);
    if (unlikely(cpy_r_r502 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 291, CPyStatic_globals);
        goto CPyL226;
    }
    cpy_r_r503 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r504 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r505 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r506 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r507 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r508 = CPyStatics[13]; /* 'name' */
    cpy_r_r509 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r510 = CPyStatics[15]; /* 'type' */
    cpy_r_r511 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r512 = 0 ? Py_True : Py_False;
    cpy_r_r513 = CPyDict_Build(4, cpy_r_r505, cpy_r_r512, cpy_r_r506, cpy_r_r507, cpy_r_r508, cpy_r_r509, cpy_r_r510, cpy_r_r511);
    if (unlikely(cpy_r_r513 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 302, CPyStatic_globals);
        goto CPyL228;
    }
    cpy_r_r514 = CPyStatics[47]; /* 'components' */
    cpy_r_r515 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r516 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r517 = CPyStatics[13]; /* 'name' */
    cpy_r_r518 = CPyStatics[48]; /* 'a' */
    cpy_r_r519 = CPyStatics[15]; /* 'type' */
    cpy_r_r520 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r521 = CPyDict_Build(3, cpy_r_r515, cpy_r_r516, cpy_r_r517, cpy_r_r518, cpy_r_r519, cpy_r_r520);
    if (unlikely(cpy_r_r521 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 310, CPyStatic_globals);
        goto CPyL229;
    }
    cpy_r_r522 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r523 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r524 = CPyStatics[13]; /* 'name' */
    cpy_r_r525 = CPyStatics[49]; /* 'b' */
    cpy_r_r526 = CPyStatics[15]; /* 'type' */
    cpy_r_r527 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r528 = CPyDict_Build(3, cpy_r_r522, cpy_r_r523, cpy_r_r524, cpy_r_r525, cpy_r_r526, cpy_r_r527);
    if (unlikely(cpy_r_r528 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 311, CPyStatic_globals);
        goto CPyL230;
    }
    cpy_r_r529 = CPyStatics[47]; /* 'components' */
    cpy_r_r530 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r531 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r532 = CPyStatics[13]; /* 'name' */
    cpy_r_r533 = CPyStatics[50]; /* 'c' */
    cpy_r_r534 = CPyStatics[15]; /* 'type' */
    cpy_r_r535 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r536 = CPyDict_Build(3, cpy_r_r530, cpy_r_r531, cpy_r_r532, cpy_r_r533, cpy_r_r534, cpy_r_r535);
    if (unlikely(cpy_r_r536 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 314, CPyStatic_globals);
        goto CPyL231;
    }
    cpy_r_r537 = PyList_New(1);
    if (unlikely(cpy_r_r537 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 313, CPyStatic_globals);
        goto CPyL232;
    }
    cpy_r_r538 = (CPyPtr)&((PyListObject *)cpy_r_r537)->ob_item;
    cpy_r_r539 = *(CPyPtr *)cpy_r_r538;
    *(PyObject * *)cpy_r_r539 = cpy_r_r536;
    cpy_r_r540 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r541 = CPyStatics[51]; /* 'struct EmitterContract.NestedTestTuple' */
    cpy_r_r542 = CPyStatics[13]; /* 'name' */
    cpy_r_r543 = CPyStatics[52]; /* 'nested' */
    cpy_r_r544 = CPyStatics[15]; /* 'type' */
    cpy_r_r545 = CPyStatics[53]; /* 'tuple' */
    cpy_r_r546 = CPyDict_Build(4, cpy_r_r529, cpy_r_r537, cpy_r_r540, cpy_r_r541, cpy_r_r542, cpy_r_r543, cpy_r_r544, cpy_r_r545);
    CPy_DECREF_NO_IMM(cpy_r_r537);
    if (unlikely(cpy_r_r546 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 312, CPyStatic_globals);
        goto CPyL231;
    }
    cpy_r_r547 = PyList_New(3);
    if (unlikely(cpy_r_r547 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 309, CPyStatic_globals);
        goto CPyL233;
    }
    cpy_r_r548 = (CPyPtr)&((PyListObject *)cpy_r_r547)->ob_item;
    cpy_r_r549 = *(CPyPtr *)cpy_r_r548;
    *(PyObject * *)cpy_r_r549 = cpy_r_r521;
    cpy_r_r550 = cpy_r_r549 + 8;
    *(PyObject * *)cpy_r_r550 = cpy_r_r528;
    cpy_r_r551 = cpy_r_r549 + 16;
    *(PyObject * *)cpy_r_r551 = cpy_r_r546;
    cpy_r_r552 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r553 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r554 = CPyStatics[54]; /* 'struct EmitterContract.TestTuple' */
    cpy_r_r555 = CPyStatics[13]; /* 'name' */
    cpy_r_r556 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r557 = CPyStatics[15]; /* 'type' */
    cpy_r_r558 = CPyStatics[53]; /* 'tuple' */
    cpy_r_r559 = 0 ? Py_True : Py_False;
    cpy_r_r560 = CPyDict_Build(5, cpy_r_r514, cpy_r_r547, cpy_r_r552, cpy_r_r559, cpy_r_r553, cpy_r_r554, cpy_r_r555, cpy_r_r556, cpy_r_r557, cpy_r_r558);
    CPy_DECREF_NO_IMM(cpy_r_r547);
    if (unlikely(cpy_r_r560 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 308, CPyStatic_globals);
        goto CPyL229;
    }
    cpy_r_r561 = PyList_New(2);
    if (unlikely(cpy_r_r561 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 301, CPyStatic_globals);
        goto CPyL234;
    }
    cpy_r_r562 = (CPyPtr)&((PyListObject *)cpy_r_r561)->ob_item;
    cpy_r_r563 = *(CPyPtr *)cpy_r_r562;
    *(PyObject * *)cpy_r_r563 = cpy_r_r513;
    cpy_r_r564 = cpy_r_r563 + 8;
    *(PyObject * *)cpy_r_r564 = cpy_r_r560;
    cpy_r_r565 = CPyStatics[13]; /* 'name' */
    cpy_r_r566 = CPyStatics[55]; /* 'LogStructArgs' */
    cpy_r_r567 = CPyStatics[15]; /* 'type' */
    cpy_r_r568 = CPyStatics[18]; /* 'event' */
    cpy_r_r569 = 0 ? Py_True : Py_False;
    cpy_r_r570 = CPyDict_Build(4, cpy_r_r503, cpy_r_r569, cpy_r_r504, cpy_r_r561, cpy_r_r565, cpy_r_r566, cpy_r_r567, cpy_r_r568);
    CPy_DECREF_NO_IMM(cpy_r_r561);
    if (unlikely(cpy_r_r570 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 299, CPyStatic_globals);
        goto CPyL228;
    }
    cpy_r_r571 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r572 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r573 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r574 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r575 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r576 = CPyStatics[13]; /* 'name' */
    cpy_r_r577 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r578 = CPyStatics[15]; /* 'type' */
    cpy_r_r579 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r580 = 0 ? Py_True : Py_False;
    cpy_r_r581 = CPyDict_Build(4, cpy_r_r573, cpy_r_r580, cpy_r_r574, cpy_r_r575, cpy_r_r576, cpy_r_r577, cpy_r_r578, cpy_r_r579);
    if (unlikely(cpy_r_r581 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 333, CPyStatic_globals);
        goto CPyL235;
    }
    cpy_r_r582 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r583 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r584 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r585 = CPyStatics[13]; /* 'name' */
    cpy_r_r586 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r587 = CPyStatics[15]; /* 'type' */
    cpy_r_r588 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r589 = 0 ? Py_True : Py_False;
    cpy_r_r590 = CPyDict_Build(4, cpy_r_r582, cpy_r_r589, cpy_r_r583, cpy_r_r584, cpy_r_r585, cpy_r_r586, cpy_r_r587, cpy_r_r588);
    if (unlikely(cpy_r_r590 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 339, CPyStatic_globals);
        goto CPyL236;
    }
    cpy_r_r591 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r592 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r593 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r594 = CPyStatics[13]; /* 'name' */
    cpy_r_r595 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r596 = CPyStatics[15]; /* 'type' */
    cpy_r_r597 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r598 = 0 ? Py_True : Py_False;
    cpy_r_r599 = CPyDict_Build(4, cpy_r_r591, cpy_r_r598, cpy_r_r592, cpy_r_r593, cpy_r_r594, cpy_r_r595, cpy_r_r596, cpy_r_r597);
    if (unlikely(cpy_r_r599 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 345, CPyStatic_globals);
        goto CPyL237;
    }
    cpy_r_r600 = PyList_New(3);
    if (unlikely(cpy_r_r600 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 332, CPyStatic_globals);
        goto CPyL238;
    }
    cpy_r_r601 = (CPyPtr)&((PyListObject *)cpy_r_r600)->ob_item;
    cpy_r_r602 = *(CPyPtr *)cpy_r_r601;
    *(PyObject * *)cpy_r_r602 = cpy_r_r581;
    cpy_r_r603 = cpy_r_r602 + 8;
    *(PyObject * *)cpy_r_r603 = cpy_r_r590;
    cpy_r_r604 = cpy_r_r602 + 16;
    *(PyObject * *)cpy_r_r604 = cpy_r_r599;
    cpy_r_r605 = CPyStatics[13]; /* 'name' */
    cpy_r_r606 = CPyStatics[56]; /* 'LogTripleArg' */
    cpy_r_r607 = CPyStatics[15]; /* 'type' */
    cpy_r_r608 = CPyStatics[18]; /* 'event' */
    cpy_r_r609 = 0 ? Py_True : Py_False;
    cpy_r_r610 = CPyDict_Build(4, cpy_r_r571, cpy_r_r609, cpy_r_r572, cpy_r_r600, cpy_r_r605, cpy_r_r606, cpy_r_r607, cpy_r_r608);
    CPy_DECREF_NO_IMM(cpy_r_r600);
    if (unlikely(cpy_r_r610 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 330, CPyStatic_globals);
        goto CPyL235;
    }
    cpy_r_r611 = CPyStatics[8]; /* 'anonymous' */
    cpy_r_r612 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r613 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r614 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r615 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r616 = CPyStatics[13]; /* 'name' */
    cpy_r_r617 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r618 = CPyStatics[15]; /* 'type' */
    cpy_r_r619 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r620 = 0 ? Py_True : Py_False;
    cpy_r_r621 = CPyDict_Build(4, cpy_r_r613, cpy_r_r620, cpy_r_r614, cpy_r_r615, cpy_r_r616, cpy_r_r617, cpy_r_r618, cpy_r_r619);
    if (unlikely(cpy_r_r621 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 358, CPyStatic_globals);
        goto CPyL239;
    }
    cpy_r_r622 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r623 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r624 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r625 = CPyStatics[13]; /* 'name' */
    cpy_r_r626 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r627 = CPyStatics[15]; /* 'type' */
    cpy_r_r628 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r629 = 1 ? Py_True : Py_False;
    cpy_r_r630 = CPyDict_Build(4, cpy_r_r622, cpy_r_r629, cpy_r_r623, cpy_r_r624, cpy_r_r625, cpy_r_r626, cpy_r_r627, cpy_r_r628);
    if (unlikely(cpy_r_r630 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 364, CPyStatic_globals);
        goto CPyL240;
    }
    cpy_r_r631 = CPyStatics[10]; /* 'indexed' */
    cpy_r_r632 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r633 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r634 = CPyStatics[13]; /* 'name' */
    cpy_r_r635 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r636 = CPyStatics[15]; /* 'type' */
    cpy_r_r637 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r638 = 1 ? Py_True : Py_False;
    cpy_r_r639 = CPyDict_Build(4, cpy_r_r631, cpy_r_r638, cpy_r_r632, cpy_r_r633, cpy_r_r634, cpy_r_r635, cpy_r_r636, cpy_r_r637);
    if (unlikely(cpy_r_r639 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 370, CPyStatic_globals);
        goto CPyL241;
    }
    cpy_r_r640 = PyList_New(3);
    if (unlikely(cpy_r_r640 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 357, CPyStatic_globals);
        goto CPyL242;
    }
    cpy_r_r641 = (CPyPtr)&((PyListObject *)cpy_r_r640)->ob_item;
    cpy_r_r642 = *(CPyPtr *)cpy_r_r641;
    *(PyObject * *)cpy_r_r642 = cpy_r_r621;
    cpy_r_r643 = cpy_r_r642 + 8;
    *(PyObject * *)cpy_r_r643 = cpy_r_r630;
    cpy_r_r644 = cpy_r_r642 + 16;
    *(PyObject * *)cpy_r_r644 = cpy_r_r639;
    cpy_r_r645 = CPyStatics[13]; /* 'name' */
    cpy_r_r646 = CPyStatics[57]; /* 'LogTripleWithIndex' */
    cpy_r_r647 = CPyStatics[15]; /* 'type' */
    cpy_r_r648 = CPyStatics[18]; /* 'event' */
    cpy_r_r649 = 0 ? Py_True : Py_False;
    cpy_r_r650 = CPyDict_Build(4, cpy_r_r611, cpy_r_r649, cpy_r_r612, cpy_r_r640, cpy_r_r645, cpy_r_r646, cpy_r_r647, cpy_r_r648);
    CPy_DECREF_NO_IMM(cpy_r_r640);
    if (unlikely(cpy_r_r650 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 355, CPyStatic_globals);
        goto CPyL239;
    }
    cpy_r_r651 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r652 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r653 = CPyStatics[12]; /* 'address' */
    cpy_r_r654 = CPyStatics[13]; /* 'name' */
    cpy_r_r655 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r656 = CPyStatics[15]; /* 'type' */
    cpy_r_r657 = CPyStatics[12]; /* 'address' */
    cpy_r_r658 = CPyDict_Build(3, cpy_r_r652, cpy_r_r653, cpy_r_r654, cpy_r_r655, cpy_r_r656, cpy_r_r657);
    if (unlikely(cpy_r_r658 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 382, CPyStatic_globals);
        goto CPyL243;
    }
    cpy_r_r659 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r660 = CPyStatics[12]; /* 'address' */
    cpy_r_r661 = CPyStatics[13]; /* 'name' */
    cpy_r_r662 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r663 = CPyStatics[15]; /* 'type' */
    cpy_r_r664 = CPyStatics[12]; /* 'address' */
    cpy_r_r665 = CPyDict_Build(3, cpy_r_r659, cpy_r_r660, cpy_r_r661, cpy_r_r662, cpy_r_r663, cpy_r_r664);
    if (unlikely(cpy_r_r665 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 383, CPyStatic_globals);
        goto CPyL244;
    }
    cpy_r_r666 = PyList_New(2);
    if (unlikely(cpy_r_r666 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 381, CPyStatic_globals);
        goto CPyL245;
    }
    cpy_r_r667 = (CPyPtr)&((PyListObject *)cpy_r_r666)->ob_item;
    cpy_r_r668 = *(CPyPtr *)cpy_r_r667;
    *(PyObject * *)cpy_r_r668 = cpy_r_r658;
    cpy_r_r669 = cpy_r_r668 + 8;
    *(PyObject * *)cpy_r_r669 = cpy_r_r665;
    cpy_r_r670 = CPyStatics[13]; /* 'name' */
    cpy_r_r671 = CPyStatics[58]; /* 'logAddressIndexedArgs' */
    cpy_r_r672 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r673 = PyList_New(0);
    if (unlikely(cpy_r_r673 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 386, CPyStatic_globals);
        goto CPyL246;
    }
    cpy_r_r674 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r675 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r676 = CPyStatics[15]; /* 'type' */
    cpy_r_r677 = CPyStatics[62]; /* 'function' */
    cpy_r_r678 = CPyDict_Build(5, cpy_r_r651, cpy_r_r666, cpy_r_r670, cpy_r_r671, cpy_r_r672, cpy_r_r673, cpy_r_r674, cpy_r_r675, cpy_r_r676, cpy_r_r677);
    CPy_DECREF_NO_IMM(cpy_r_r666);
    CPy_DECREF_NO_IMM(cpy_r_r673);
    if (unlikely(cpy_r_r678 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 380, CPyStatic_globals);
        goto CPyL243;
    }
    cpy_r_r679 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r680 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r681 = CPyStatics[12]; /* 'address' */
    cpy_r_r682 = CPyStatics[13]; /* 'name' */
    cpy_r_r683 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r684 = CPyStatics[15]; /* 'type' */
    cpy_r_r685 = CPyStatics[12]; /* 'address' */
    cpy_r_r686 = CPyDict_Build(3, cpy_r_r680, cpy_r_r681, cpy_r_r682, cpy_r_r683, cpy_r_r684, cpy_r_r685);
    if (unlikely(cpy_r_r686 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 392, CPyStatic_globals);
        goto CPyL247;
    }
    cpy_r_r687 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r688 = CPyStatics[12]; /* 'address' */
    cpy_r_r689 = CPyStatics[13]; /* 'name' */
    cpy_r_r690 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r691 = CPyStatics[15]; /* 'type' */
    cpy_r_r692 = CPyStatics[12]; /* 'address' */
    cpy_r_r693 = CPyDict_Build(3, cpy_r_r687, cpy_r_r688, cpy_r_r689, cpy_r_r690, cpy_r_r691, cpy_r_r692);
    if (unlikely(cpy_r_r693 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 393, CPyStatic_globals);
        goto CPyL248;
    }
    cpy_r_r694 = PyList_New(2);
    if (unlikely(cpy_r_r694 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 391, CPyStatic_globals);
        goto CPyL249;
    }
    cpy_r_r695 = (CPyPtr)&((PyListObject *)cpy_r_r694)->ob_item;
    cpy_r_r696 = *(CPyPtr *)cpy_r_r695;
    *(PyObject * *)cpy_r_r696 = cpy_r_r686;
    cpy_r_r697 = cpy_r_r696 + 8;
    *(PyObject * *)cpy_r_r697 = cpy_r_r693;
    cpy_r_r698 = CPyStatics[13]; /* 'name' */
    cpy_r_r699 = CPyStatics[63]; /* 'logAddressNotIndexedArgs' */
    cpy_r_r700 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r701 = PyList_New(0);
    if (unlikely(cpy_r_r701 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 396, CPyStatic_globals);
        goto CPyL250;
    }
    cpy_r_r702 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r703 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r704 = CPyStatics[15]; /* 'type' */
    cpy_r_r705 = CPyStatics[62]; /* 'function' */
    cpy_r_r706 = CPyDict_Build(5, cpy_r_r679, cpy_r_r694, cpy_r_r698, cpy_r_r699, cpy_r_r700, cpy_r_r701, cpy_r_r702, cpy_r_r703, cpy_r_r704, cpy_r_r705);
    CPy_DECREF_NO_IMM(cpy_r_r694);
    CPy_DECREF_NO_IMM(cpy_r_r701);
    if (unlikely(cpy_r_r706 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 390, CPyStatic_globals);
        goto CPyL247;
    }
    cpy_r_r707 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r708 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r709 = CPyStatics[21]; /* 'bytes' */
    cpy_r_r710 = CPyStatics[13]; /* 'name' */
    cpy_r_r711 = CPyStatics[22]; /* 'v' */
    cpy_r_r712 = CPyStatics[15]; /* 'type' */
    cpy_r_r713 = CPyStatics[21]; /* 'bytes' */
    cpy_r_r714 = CPyDict_Build(3, cpy_r_r708, cpy_r_r709, cpy_r_r710, cpy_r_r711, cpy_r_r712, cpy_r_r713);
    if (unlikely(cpy_r_r714 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 401, CPyStatic_globals);
        goto CPyL251;
    }
    cpy_r_r715 = PyList_New(1);
    if (unlikely(cpy_r_r715 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 401, CPyStatic_globals);
        goto CPyL252;
    }
    cpy_r_r716 = (CPyPtr)&((PyListObject *)cpy_r_r715)->ob_item;
    cpy_r_r717 = *(CPyPtr *)cpy_r_r716;
    *(PyObject * *)cpy_r_r717 = cpy_r_r714;
    cpy_r_r718 = CPyStatics[13]; /* 'name' */
    cpy_r_r719 = CPyStatics[64]; /* 'logBytes' */
    cpy_r_r720 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r721 = PyList_New(0);
    if (unlikely(cpy_r_r721 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 403, CPyStatic_globals);
        goto CPyL253;
    }
    cpy_r_r722 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r723 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r724 = CPyStatics[15]; /* 'type' */
    cpy_r_r725 = CPyStatics[62]; /* 'function' */
    cpy_r_r726 = CPyDict_Build(5, cpy_r_r707, cpy_r_r715, cpy_r_r718, cpy_r_r719, cpy_r_r720, cpy_r_r721, cpy_r_r722, cpy_r_r723, cpy_r_r724, cpy_r_r725);
    CPy_DECREF_NO_IMM(cpy_r_r715);
    CPy_DECREF_NO_IMM(cpy_r_r721);
    if (unlikely(cpy_r_r726 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 400, CPyStatic_globals);
        goto CPyL251;
    }
    cpy_r_r727 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r728 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r729 = CPyStatics[65]; /* 'enum EmitterContract.WhichEvent' */
    cpy_r_r730 = CPyStatics[13]; /* 'name' */
    cpy_r_r731 = CPyStatics[66]; /* 'which' */
    cpy_r_r732 = CPyStatics[15]; /* 'type' */
    cpy_r_r733 = CPyStatics[67]; /* 'uint8' */
    cpy_r_r734 = CPyDict_Build(3, cpy_r_r728, cpy_r_r729, cpy_r_r730, cpy_r_r731, cpy_r_r732, cpy_r_r733);
    if (unlikely(cpy_r_r734 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 409, CPyStatic_globals);
        goto CPyL254;
    }
    cpy_r_r735 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r736 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r737 = CPyStatics[13]; /* 'name' */
    cpy_r_r738 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r739 = CPyStatics[15]; /* 'type' */
    cpy_r_r740 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r741 = CPyDict_Build(3, cpy_r_r735, cpy_r_r736, cpy_r_r737, cpy_r_r738, cpy_r_r739, cpy_r_r740);
    if (unlikely(cpy_r_r741 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 414, CPyStatic_globals);
        goto CPyL255;
    }
    cpy_r_r742 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r743 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r744 = CPyStatics[13]; /* 'name' */
    cpy_r_r745 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r746 = CPyStatics[15]; /* 'type' */
    cpy_r_r747 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r748 = CPyDict_Build(3, cpy_r_r742, cpy_r_r743, cpy_r_r744, cpy_r_r745, cpy_r_r746, cpy_r_r747);
    if (unlikely(cpy_r_r748 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 415, CPyStatic_globals);
        goto CPyL256;
    }
    cpy_r_r749 = PyList_New(3);
    if (unlikely(cpy_r_r749 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 408, CPyStatic_globals);
        goto CPyL257;
    }
    cpy_r_r750 = (CPyPtr)&((PyListObject *)cpy_r_r749)->ob_item;
    cpy_r_r751 = *(CPyPtr *)cpy_r_r750;
    *(PyObject * *)cpy_r_r751 = cpy_r_r734;
    cpy_r_r752 = cpy_r_r751 + 8;
    *(PyObject * *)cpy_r_r752 = cpy_r_r741;
    cpy_r_r753 = cpy_r_r751 + 16;
    *(PyObject * *)cpy_r_r753 = cpy_r_r748;
    cpy_r_r754 = CPyStatics[13]; /* 'name' */
    cpy_r_r755 = CPyStatics[68]; /* 'logDouble' */
    cpy_r_r756 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r757 = PyList_New(0);
    if (unlikely(cpy_r_r757 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 418, CPyStatic_globals);
        goto CPyL258;
    }
    cpy_r_r758 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r759 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r760 = CPyStatics[15]; /* 'type' */
    cpy_r_r761 = CPyStatics[62]; /* 'function' */
    cpy_r_r762 = CPyDict_Build(5, cpy_r_r727, cpy_r_r749, cpy_r_r754, cpy_r_r755, cpy_r_r756, cpy_r_r757, cpy_r_r758, cpy_r_r759, cpy_r_r760, cpy_r_r761);
    CPy_DECREF_NO_IMM(cpy_r_r749);
    CPy_DECREF_NO_IMM(cpy_r_r757);
    if (unlikely(cpy_r_r762 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 407, CPyStatic_globals);
        goto CPyL254;
    }
    cpy_r_r763 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r764 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r765 = CPyStatics[28]; /* 'string' */
    cpy_r_r766 = CPyStatics[13]; /* 'name' */
    cpy_r_r767 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r768 = CPyStatics[15]; /* 'type' */
    cpy_r_r769 = CPyStatics[28]; /* 'string' */
    cpy_r_r770 = CPyDict_Build(3, cpy_r_r764, cpy_r_r765, cpy_r_r766, cpy_r_r767, cpy_r_r768, cpy_r_r769);
    if (unlikely(cpy_r_r770 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 424, CPyStatic_globals);
        goto CPyL259;
    }
    cpy_r_r771 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r772 = CPyStatics[28]; /* 'string' */
    cpy_r_r773 = CPyStatics[13]; /* 'name' */
    cpy_r_r774 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r775 = CPyStatics[15]; /* 'type' */
    cpy_r_r776 = CPyStatics[28]; /* 'string' */
    cpy_r_r777 = CPyDict_Build(3, cpy_r_r771, cpy_r_r772, cpy_r_r773, cpy_r_r774, cpy_r_r775, cpy_r_r776);
    if (unlikely(cpy_r_r777 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 425, CPyStatic_globals);
        goto CPyL260;
    }
    cpy_r_r778 = PyList_New(2);
    if (unlikely(cpy_r_r778 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 423, CPyStatic_globals);
        goto CPyL261;
    }
    cpy_r_r779 = (CPyPtr)&((PyListObject *)cpy_r_r778)->ob_item;
    cpy_r_r780 = *(CPyPtr *)cpy_r_r779;
    *(PyObject * *)cpy_r_r780 = cpy_r_r770;
    cpy_r_r781 = cpy_r_r780 + 8;
    *(PyObject * *)cpy_r_r781 = cpy_r_r777;
    cpy_r_r782 = CPyStatics[13]; /* 'name' */
    cpy_r_r783 = CPyStatics[69]; /* 'logDynamicArgs' */
    cpy_r_r784 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r785 = PyList_New(0);
    if (unlikely(cpy_r_r785 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 428, CPyStatic_globals);
        goto CPyL262;
    }
    cpy_r_r786 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r787 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r788 = CPyStatics[15]; /* 'type' */
    cpy_r_r789 = CPyStatics[62]; /* 'function' */
    cpy_r_r790 = CPyDict_Build(5, cpy_r_r763, cpy_r_r778, cpy_r_r782, cpy_r_r783, cpy_r_r784, cpy_r_r785, cpy_r_r786, cpy_r_r787, cpy_r_r788, cpy_r_r789);
    CPy_DECREF_NO_IMM(cpy_r_r778);
    CPy_DECREF_NO_IMM(cpy_r_r785);
    if (unlikely(cpy_r_r790 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 422, CPyStatic_globals);
        goto CPyL259;
    }
    cpy_r_r791 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r792 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r793 = CPyStatics[12]; /* 'address' */
    cpy_r_r794 = CPyStatics[13]; /* 'name' */
    cpy_r_r795 = CPyStatics[30]; /* 'indexedAddress' */
    cpy_r_r796 = CPyStatics[15]; /* 'type' */
    cpy_r_r797 = CPyStatics[12]; /* 'address' */
    cpy_r_r798 = CPyDict_Build(3, cpy_r_r792, cpy_r_r793, cpy_r_r794, cpy_r_r795, cpy_r_r796, cpy_r_r797);
    if (unlikely(cpy_r_r798 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 434, CPyStatic_globals);
        goto CPyL263;
    }
    cpy_r_r799 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r800 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r801 = CPyStatics[13]; /* 'name' */
    cpy_r_r802 = CPyStatics[31]; /* 'indexedUint256' */
    cpy_r_r803 = CPyStatics[15]; /* 'type' */
    cpy_r_r804 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r805 = CPyDict_Build(3, cpy_r_r799, cpy_r_r800, cpy_r_r801, cpy_r_r802, cpy_r_r803, cpy_r_r804);
    if (unlikely(cpy_r_r805 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 435, CPyStatic_globals);
        goto CPyL264;
    }
    cpy_r_r806 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r807 = CPyStatics[12]; /* 'address' */
    cpy_r_r808 = CPyStatics[13]; /* 'name' */
    cpy_r_r809 = CPyStatics[32]; /* 'nonIndexedAddress' */
    cpy_r_r810 = CPyStatics[15]; /* 'type' */
    cpy_r_r811 = CPyStatics[12]; /* 'address' */
    cpy_r_r812 = CPyDict_Build(3, cpy_r_r806, cpy_r_r807, cpy_r_r808, cpy_r_r809, cpy_r_r810, cpy_r_r811);
    if (unlikely(cpy_r_r812 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 436, CPyStatic_globals);
        goto CPyL265;
    }
    cpy_r_r813 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r814 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r815 = CPyStatics[13]; /* 'name' */
    cpy_r_r816 = CPyStatics[33]; /* 'nonIndexedUint256' */
    cpy_r_r817 = CPyStatics[15]; /* 'type' */
    cpy_r_r818 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r819 = CPyDict_Build(3, cpy_r_r813, cpy_r_r814, cpy_r_r815, cpy_r_r816, cpy_r_r817, cpy_r_r818);
    if (unlikely(cpy_r_r819 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 437, CPyStatic_globals);
        goto CPyL266;
    }
    cpy_r_r820 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r821 = CPyStatics[28]; /* 'string' */
    cpy_r_r822 = CPyStatics[13]; /* 'name' */
    cpy_r_r823 = CPyStatics[34]; /* 'nonIndexedString' */
    cpy_r_r824 = CPyStatics[15]; /* 'type' */
    cpy_r_r825 = CPyStatics[28]; /* 'string' */
    cpy_r_r826 = CPyDict_Build(3, cpy_r_r820, cpy_r_r821, cpy_r_r822, cpy_r_r823, cpy_r_r824, cpy_r_r825);
    if (unlikely(cpy_r_r826 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 438, CPyStatic_globals);
        goto CPyL267;
    }
    cpy_r_r827 = PyList_New(5);
    if (unlikely(cpy_r_r827 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 433, CPyStatic_globals);
        goto CPyL268;
    }
    cpy_r_r828 = (CPyPtr)&((PyListObject *)cpy_r_r827)->ob_item;
    cpy_r_r829 = *(CPyPtr *)cpy_r_r828;
    *(PyObject * *)cpy_r_r829 = cpy_r_r798;
    cpy_r_r830 = cpy_r_r829 + 8;
    *(PyObject * *)cpy_r_r830 = cpy_r_r805;
    cpy_r_r831 = cpy_r_r829 + 16;
    *(PyObject * *)cpy_r_r831 = cpy_r_r812;
    cpy_r_r832 = cpy_r_r829 + 24;
    *(PyObject * *)cpy_r_r832 = cpy_r_r819;
    cpy_r_r833 = cpy_r_r829 + 32;
    *(PyObject * *)cpy_r_r833 = cpy_r_r826;
    cpy_r_r834 = CPyStatics[13]; /* 'name' */
    cpy_r_r835 = CPyStatics[70]; /* 'logIndexedAndNotIndexedArgs' */
    cpy_r_r836 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r837 = PyList_New(0);
    if (unlikely(cpy_r_r837 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 441, CPyStatic_globals);
        goto CPyL269;
    }
    cpy_r_r838 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r839 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r840 = CPyStatics[15]; /* 'type' */
    cpy_r_r841 = CPyStatics[62]; /* 'function' */
    cpy_r_r842 = CPyDict_Build(5, cpy_r_r791, cpy_r_r827, cpy_r_r834, cpy_r_r835, cpy_r_r836, cpy_r_r837, cpy_r_r838, cpy_r_r839, cpy_r_r840, cpy_r_r841);
    CPy_DECREF_NO_IMM(cpy_r_r827);
    CPy_DECREF_NO_IMM(cpy_r_r837);
    if (unlikely(cpy_r_r842 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 432, CPyStatic_globals);
        goto CPyL263;
    }
    cpy_r_r843 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r844 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r845 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r846 = CPyStatics[13]; /* 'name' */
    cpy_r_r847 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r848 = CPyStatics[15]; /* 'type' */
    cpy_r_r849 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r850 = CPyDict_Build(3, cpy_r_r844, cpy_r_r845, cpy_r_r846, cpy_r_r847, cpy_r_r848, cpy_r_r849);
    if (unlikely(cpy_r_r850 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 447, CPyStatic_globals);
        goto CPyL270;
    }
    cpy_r_r851 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r852 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r853 = CPyStatics[13]; /* 'name' */
    cpy_r_r854 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r855 = CPyStatics[15]; /* 'type' */
    cpy_r_r856 = CPyStatics[36]; /* 'bytes2[]' */
    cpy_r_r857 = CPyDict_Build(3, cpy_r_r851, cpy_r_r852, cpy_r_r853, cpy_r_r854, cpy_r_r855, cpy_r_r856);
    if (unlikely(cpy_r_r857 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 448, CPyStatic_globals);
        goto CPyL271;
    }
    cpy_r_r858 = PyList_New(2);
    if (unlikely(cpy_r_r858 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 446, CPyStatic_globals);
        goto CPyL272;
    }
    cpy_r_r859 = (CPyPtr)&((PyListObject *)cpy_r_r858)->ob_item;
    cpy_r_r860 = *(CPyPtr *)cpy_r_r859;
    *(PyObject * *)cpy_r_r860 = cpy_r_r850;
    cpy_r_r861 = cpy_r_r860 + 8;
    *(PyObject * *)cpy_r_r861 = cpy_r_r857;
    cpy_r_r862 = CPyStatics[13]; /* 'name' */
    cpy_r_r863 = CPyStatics[71]; /* 'logListArgs' */
    cpy_r_r864 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r865 = PyList_New(0);
    if (unlikely(cpy_r_r865 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 451, CPyStatic_globals);
        goto CPyL273;
    }
    cpy_r_r866 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r867 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r868 = CPyStatics[15]; /* 'type' */
    cpy_r_r869 = CPyStatics[62]; /* 'function' */
    cpy_r_r870 = CPyDict_Build(5, cpy_r_r843, cpy_r_r858, cpy_r_r862, cpy_r_r863, cpy_r_r864, cpy_r_r865, cpy_r_r866, cpy_r_r867, cpy_r_r868, cpy_r_r869);
    CPy_DECREF_NO_IMM(cpy_r_r858);
    CPy_DECREF_NO_IMM(cpy_r_r865);
    if (unlikely(cpy_r_r870 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 445, CPyStatic_globals);
        goto CPyL270;
    }
    cpy_r_r871 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r872 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r873 = CPyStatics[65]; /* 'enum EmitterContract.WhichEvent' */
    cpy_r_r874 = CPyStatics[13]; /* 'name' */
    cpy_r_r875 = CPyStatics[66]; /* 'which' */
    cpy_r_r876 = CPyStatics[15]; /* 'type' */
    cpy_r_r877 = CPyStatics[67]; /* 'uint8' */
    cpy_r_r878 = CPyDict_Build(3, cpy_r_r872, cpy_r_r873, cpy_r_r874, cpy_r_r875, cpy_r_r876, cpy_r_r877);
    if (unlikely(cpy_r_r878 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 457, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_r879 = PyList_New(1);
    if (unlikely(cpy_r_r879 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 456, CPyStatic_globals);
        goto CPyL275;
    }
    cpy_r_r880 = (CPyPtr)&((PyListObject *)cpy_r_r879)->ob_item;
    cpy_r_r881 = *(CPyPtr *)cpy_r_r880;
    *(PyObject * *)cpy_r_r881 = cpy_r_r878;
    cpy_r_r882 = CPyStatics[13]; /* 'name' */
    cpy_r_r883 = CPyStatics[72]; /* 'logNoArgs' */
    cpy_r_r884 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r885 = PyList_New(0);
    if (unlikely(cpy_r_r885 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 464, CPyStatic_globals);
        goto CPyL276;
    }
    cpy_r_r886 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r887 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r888 = CPyStatics[15]; /* 'type' */
    cpy_r_r889 = CPyStatics[62]; /* 'function' */
    cpy_r_r890 = CPyDict_Build(5, cpy_r_r871, cpy_r_r879, cpy_r_r882, cpy_r_r883, cpy_r_r884, cpy_r_r885, cpy_r_r886, cpy_r_r887, cpy_r_r888, cpy_r_r889);
    CPy_DECREF_NO_IMM(cpy_r_r879);
    CPy_DECREF_NO_IMM(cpy_r_r885);
    if (unlikely(cpy_r_r890 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 455, CPyStatic_globals);
        goto CPyL274;
    }
    cpy_r_r891 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r892 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r893 = CPyStatics[65]; /* 'enum EmitterContract.WhichEvent' */
    cpy_r_r894 = CPyStatics[13]; /* 'name' */
    cpy_r_r895 = CPyStatics[66]; /* 'which' */
    cpy_r_r896 = CPyStatics[15]; /* 'type' */
    cpy_r_r897 = CPyStatics[67]; /* 'uint8' */
    cpy_r_r898 = CPyDict_Build(3, cpy_r_r892, cpy_r_r893, cpy_r_r894, cpy_r_r895, cpy_r_r896, cpy_r_r897);
    if (unlikely(cpy_r_r898 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 470, CPyStatic_globals);
        goto CPyL277;
    }
    cpy_r_r899 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r900 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r901 = CPyStatics[13]; /* 'name' */
    cpy_r_r902 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r903 = CPyStatics[15]; /* 'type' */
    cpy_r_r904 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r905 = CPyDict_Build(3, cpy_r_r899, cpy_r_r900, cpy_r_r901, cpy_r_r902, cpy_r_r903, cpy_r_r904);
    if (unlikely(cpy_r_r905 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 475, CPyStatic_globals);
        goto CPyL278;
    }
    cpy_r_r906 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r907 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r908 = CPyStatics[13]; /* 'name' */
    cpy_r_r909 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r910 = CPyStatics[15]; /* 'type' */
    cpy_r_r911 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r912 = CPyDict_Build(3, cpy_r_r906, cpy_r_r907, cpy_r_r908, cpy_r_r909, cpy_r_r910, cpy_r_r911);
    if (unlikely(cpy_r_r912 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 476, CPyStatic_globals);
        goto CPyL279;
    }
    cpy_r_r913 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r914 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r915 = CPyStatics[13]; /* 'name' */
    cpy_r_r916 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r917 = CPyStatics[15]; /* 'type' */
    cpy_r_r918 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r919 = CPyDict_Build(3, cpy_r_r913, cpy_r_r914, cpy_r_r915, cpy_r_r916, cpy_r_r917, cpy_r_r918);
    if (unlikely(cpy_r_r919 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 477, CPyStatic_globals);
        goto CPyL280;
    }
    cpy_r_r920 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r921 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r922 = CPyStatics[13]; /* 'name' */
    cpy_r_r923 = CPyStatics[40]; /* 'arg3' */
    cpy_r_r924 = CPyStatics[15]; /* 'type' */
    cpy_r_r925 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r926 = CPyDict_Build(3, cpy_r_r920, cpy_r_r921, cpy_r_r922, cpy_r_r923, cpy_r_r924, cpy_r_r925);
    if (unlikely(cpy_r_r926 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 478, CPyStatic_globals);
        goto CPyL281;
    }
    cpy_r_r927 = PyList_New(5);
    if (unlikely(cpy_r_r927 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 469, CPyStatic_globals);
        goto CPyL282;
    }
    cpy_r_r928 = (CPyPtr)&((PyListObject *)cpy_r_r927)->ob_item;
    cpy_r_r929 = *(CPyPtr *)cpy_r_r928;
    *(PyObject * *)cpy_r_r929 = cpy_r_r898;
    cpy_r_r930 = cpy_r_r929 + 8;
    *(PyObject * *)cpy_r_r930 = cpy_r_r905;
    cpy_r_r931 = cpy_r_r929 + 16;
    *(PyObject * *)cpy_r_r931 = cpy_r_r912;
    cpy_r_r932 = cpy_r_r929 + 24;
    *(PyObject * *)cpy_r_r932 = cpy_r_r919;
    cpy_r_r933 = cpy_r_r929 + 32;
    *(PyObject * *)cpy_r_r933 = cpy_r_r926;
    cpy_r_r934 = CPyStatics[13]; /* 'name' */
    cpy_r_r935 = CPyStatics[73]; /* 'logQuadruple' */
    cpy_r_r936 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r937 = PyList_New(0);
    if (unlikely(cpy_r_r937 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 481, CPyStatic_globals);
        goto CPyL283;
    }
    cpy_r_r938 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r939 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r940 = CPyStatics[15]; /* 'type' */
    cpy_r_r941 = CPyStatics[62]; /* 'function' */
    cpy_r_r942 = CPyDict_Build(5, cpy_r_r891, cpy_r_r927, cpy_r_r934, cpy_r_r935, cpy_r_r936, cpy_r_r937, cpy_r_r938, cpy_r_r939, cpy_r_r940, cpy_r_r941);
    CPy_DECREF_NO_IMM(cpy_r_r927);
    CPy_DECREF_NO_IMM(cpy_r_r937);
    if (unlikely(cpy_r_r942 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 468, CPyStatic_globals);
        goto CPyL277;
    }
    cpy_r_r943 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r944 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r945 = CPyStatics[65]; /* 'enum EmitterContract.WhichEvent' */
    cpy_r_r946 = CPyStatics[13]; /* 'name' */
    cpy_r_r947 = CPyStatics[66]; /* 'which' */
    cpy_r_r948 = CPyStatics[15]; /* 'type' */
    cpy_r_r949 = CPyStatics[67]; /* 'uint8' */
    cpy_r_r950 = CPyDict_Build(3, cpy_r_r944, cpy_r_r945, cpy_r_r946, cpy_r_r947, cpy_r_r948, cpy_r_r949);
    if (unlikely(cpy_r_r950 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 487, CPyStatic_globals);
        goto CPyL284;
    }
    cpy_r_r951 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r952 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r953 = CPyStatics[13]; /* 'name' */
    cpy_r_r954 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r955 = CPyStatics[15]; /* 'type' */
    cpy_r_r956 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r957 = CPyDict_Build(3, cpy_r_r951, cpy_r_r952, cpy_r_r953, cpy_r_r954, cpy_r_r955, cpy_r_r956);
    if (unlikely(cpy_r_r957 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 492, CPyStatic_globals);
        goto CPyL285;
    }
    cpy_r_r958 = PyList_New(2);
    if (unlikely(cpy_r_r958 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 486, CPyStatic_globals);
        goto CPyL286;
    }
    cpy_r_r959 = (CPyPtr)&((PyListObject *)cpy_r_r958)->ob_item;
    cpy_r_r960 = *(CPyPtr *)cpy_r_r959;
    *(PyObject * *)cpy_r_r960 = cpy_r_r950;
    cpy_r_r961 = cpy_r_r960 + 8;
    *(PyObject * *)cpy_r_r961 = cpy_r_r957;
    cpy_r_r962 = CPyStatics[13]; /* 'name' */
    cpy_r_r963 = CPyStatics[74]; /* 'logSingle' */
    cpy_r_r964 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r965 = PyList_New(0);
    if (unlikely(cpy_r_r965 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 495, CPyStatic_globals);
        goto CPyL287;
    }
    cpy_r_r966 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r967 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r968 = CPyStatics[15]; /* 'type' */
    cpy_r_r969 = CPyStatics[62]; /* 'function' */
    cpy_r_r970 = CPyDict_Build(5, cpy_r_r943, cpy_r_r958, cpy_r_r962, cpy_r_r963, cpy_r_r964, cpy_r_r965, cpy_r_r966, cpy_r_r967, cpy_r_r968, cpy_r_r969);
    CPy_DECREF_NO_IMM(cpy_r_r958);
    CPy_DECREF_NO_IMM(cpy_r_r965);
    if (unlikely(cpy_r_r970 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 485, CPyStatic_globals);
        goto CPyL284;
    }
    cpy_r_r971 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r972 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r973 = CPyStatics[28]; /* 'string' */
    cpy_r_r974 = CPyStatics[13]; /* 'name' */
    cpy_r_r975 = CPyStatics[22]; /* 'v' */
    cpy_r_r976 = CPyStatics[15]; /* 'type' */
    cpy_r_r977 = CPyStatics[28]; /* 'string' */
    cpy_r_r978 = CPyDict_Build(3, cpy_r_r972, cpy_r_r973, cpy_r_r974, cpy_r_r975, cpy_r_r976, cpy_r_r977);
    if (unlikely(cpy_r_r978 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 500, CPyStatic_globals);
        goto CPyL288;
    }
    cpy_r_r979 = PyList_New(1);
    if (unlikely(cpy_r_r979 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 500, CPyStatic_globals);
        goto CPyL289;
    }
    cpy_r_r980 = (CPyPtr)&((PyListObject *)cpy_r_r979)->ob_item;
    cpy_r_r981 = *(CPyPtr *)cpy_r_r980;
    *(PyObject * *)cpy_r_r981 = cpy_r_r978;
    cpy_r_r982 = CPyStatics[13]; /* 'name' */
    cpy_r_r983 = CPyStatics[75]; /* 'logString' */
    cpy_r_r984 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r985 = PyList_New(0);
    if (unlikely(cpy_r_r985 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 502, CPyStatic_globals);
        goto CPyL290;
    }
    cpy_r_r986 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r987 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r988 = CPyStatics[15]; /* 'type' */
    cpy_r_r989 = CPyStatics[62]; /* 'function' */
    cpy_r_r990 = CPyDict_Build(5, cpy_r_r971, cpy_r_r979, cpy_r_r982, cpy_r_r983, cpy_r_r984, cpy_r_r985, cpy_r_r986, cpy_r_r987, cpy_r_r988, cpy_r_r989);
    CPy_DECREF_NO_IMM(cpy_r_r979);
    CPy_DECREF_NO_IMM(cpy_r_r985);
    if (unlikely(cpy_r_r990 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 499, CPyStatic_globals);
        goto CPyL288;
    }
    cpy_r_r991 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r992 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r993 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r994 = CPyStatics[13]; /* 'name' */
    cpy_r_r995 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r996 = CPyStatics[15]; /* 'type' */
    cpy_r_r997 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r998 = CPyDict_Build(3, cpy_r_r992, cpy_r_r993, cpy_r_r994, cpy_r_r995, cpy_r_r996, cpy_r_r997);
    if (unlikely(cpy_r_r998 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 508, CPyStatic_globals);
        goto CPyL291;
    }
    cpy_r_r999 = CPyStatics[47]; /* 'components' */
    cpy_r_r1000 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1001 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1002 = CPyStatics[13]; /* 'name' */
    cpy_r_r1003 = CPyStatics[48]; /* 'a' */
    cpy_r_r1004 = CPyStatics[15]; /* 'type' */
    cpy_r_r1005 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1006 = CPyDict_Build(3, cpy_r_r1000, cpy_r_r1001, cpy_r_r1002, cpy_r_r1003, cpy_r_r1004, cpy_r_r1005);
    if (unlikely(cpy_r_r1006 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 511, CPyStatic_globals);
        goto CPyL292;
    }
    cpy_r_r1007 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1008 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1009 = CPyStatics[13]; /* 'name' */
    cpy_r_r1010 = CPyStatics[49]; /* 'b' */
    cpy_r_r1011 = CPyStatics[15]; /* 'type' */
    cpy_r_r1012 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1013 = CPyDict_Build(3, cpy_r_r1007, cpy_r_r1008, cpy_r_r1009, cpy_r_r1010, cpy_r_r1011, cpy_r_r1012);
    if (unlikely(cpy_r_r1013 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 512, CPyStatic_globals);
        goto CPyL293;
    }
    cpy_r_r1014 = CPyStatics[47]; /* 'components' */
    cpy_r_r1015 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1016 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1017 = CPyStatics[13]; /* 'name' */
    cpy_r_r1018 = CPyStatics[50]; /* 'c' */
    cpy_r_r1019 = CPyStatics[15]; /* 'type' */
    cpy_r_r1020 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1021 = CPyDict_Build(3, cpy_r_r1015, cpy_r_r1016, cpy_r_r1017, cpy_r_r1018, cpy_r_r1019, cpy_r_r1020);
    if (unlikely(cpy_r_r1021 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 515, CPyStatic_globals);
        goto CPyL294;
    }
    cpy_r_r1022 = PyList_New(1);
    if (unlikely(cpy_r_r1022 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 514, CPyStatic_globals);
        goto CPyL295;
    }
    cpy_r_r1023 = (CPyPtr)&((PyListObject *)cpy_r_r1022)->ob_item;
    cpy_r_r1024 = *(CPyPtr *)cpy_r_r1023;
    *(PyObject * *)cpy_r_r1024 = cpy_r_r1021;
    cpy_r_r1025 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1026 = CPyStatics[51]; /* 'struct EmitterContract.NestedTestTuple' */
    cpy_r_r1027 = CPyStatics[13]; /* 'name' */
    cpy_r_r1028 = CPyStatics[52]; /* 'nested' */
    cpy_r_r1029 = CPyStatics[15]; /* 'type' */
    cpy_r_r1030 = CPyStatics[53]; /* 'tuple' */
    cpy_r_r1031 = CPyDict_Build(4, cpy_r_r1014, cpy_r_r1022, cpy_r_r1025, cpy_r_r1026, cpy_r_r1027, cpy_r_r1028, cpy_r_r1029, cpy_r_r1030);
    CPy_DECREF_NO_IMM(cpy_r_r1022);
    if (unlikely(cpy_r_r1031 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 513, CPyStatic_globals);
        goto CPyL294;
    }
    cpy_r_r1032 = PyList_New(3);
    if (unlikely(cpy_r_r1032 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 510, CPyStatic_globals);
        goto CPyL296;
    }
    cpy_r_r1033 = (CPyPtr)&((PyListObject *)cpy_r_r1032)->ob_item;
    cpy_r_r1034 = *(CPyPtr *)cpy_r_r1033;
    *(PyObject * *)cpy_r_r1034 = cpy_r_r1006;
    cpy_r_r1035 = cpy_r_r1034 + 8;
    *(PyObject * *)cpy_r_r1035 = cpy_r_r1013;
    cpy_r_r1036 = cpy_r_r1034 + 16;
    *(PyObject * *)cpy_r_r1036 = cpy_r_r1031;
    cpy_r_r1037 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1038 = CPyStatics[54]; /* 'struct EmitterContract.TestTuple' */
    cpy_r_r1039 = CPyStatics[13]; /* 'name' */
    cpy_r_r1040 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r1041 = CPyStatics[15]; /* 'type' */
    cpy_r_r1042 = CPyStatics[53]; /* 'tuple' */
    cpy_r_r1043 = CPyDict_Build(4, cpy_r_r999, cpy_r_r1032, cpy_r_r1037, cpy_r_r1038, cpy_r_r1039, cpy_r_r1040, cpy_r_r1041, cpy_r_r1042);
    CPy_DECREF_NO_IMM(cpy_r_r1032);
    if (unlikely(cpy_r_r1043 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 509, CPyStatic_globals);
        goto CPyL292;
    }
    cpy_r_r1044 = PyList_New(2);
    if (unlikely(cpy_r_r1044 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 507, CPyStatic_globals);
        goto CPyL297;
    }
    cpy_r_r1045 = (CPyPtr)&((PyListObject *)cpy_r_r1044)->ob_item;
    cpy_r_r1046 = *(CPyPtr *)cpy_r_r1045;
    *(PyObject * *)cpy_r_r1046 = cpy_r_r998;
    cpy_r_r1047 = cpy_r_r1046 + 8;
    *(PyObject * *)cpy_r_r1047 = cpy_r_r1043;
    cpy_r_r1048 = CPyStatics[13]; /* 'name' */
    cpy_r_r1049 = CPyStatics[76]; /* 'logStruct' */
    cpy_r_r1050 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r1051 = PyList_New(0);
    if (unlikely(cpy_r_r1051 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 528, CPyStatic_globals);
        goto CPyL298;
    }
    cpy_r_r1052 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r1053 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r1054 = CPyStatics[15]; /* 'type' */
    cpy_r_r1055 = CPyStatics[62]; /* 'function' */
    cpy_r_r1056 = CPyDict_Build(5, cpy_r_r991, cpy_r_r1044, cpy_r_r1048, cpy_r_r1049, cpy_r_r1050, cpy_r_r1051, cpy_r_r1052, cpy_r_r1053, cpy_r_r1054, cpy_r_r1055);
    CPy_DECREF_NO_IMM(cpy_r_r1044);
    CPy_DECREF_NO_IMM(cpy_r_r1051);
    if (unlikely(cpy_r_r1056 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 506, CPyStatic_globals);
        goto CPyL291;
    }
    cpy_r_r1057 = CPyStatics[9]; /* 'inputs' */
    cpy_r_r1058 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1059 = CPyStatics[65]; /* 'enum EmitterContract.WhichEvent' */
    cpy_r_r1060 = CPyStatics[13]; /* 'name' */
    cpy_r_r1061 = CPyStatics[66]; /* 'which' */
    cpy_r_r1062 = CPyStatics[15]; /* 'type' */
    cpy_r_r1063 = CPyStatics[67]; /* 'uint8' */
    cpy_r_r1064 = CPyDict_Build(3, cpy_r_r1058, cpy_r_r1059, cpy_r_r1060, cpy_r_r1061, cpy_r_r1062, cpy_r_r1063);
    if (unlikely(cpy_r_r1064 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 534, CPyStatic_globals);
        goto CPyL299;
    }
    cpy_r_r1065 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1066 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1067 = CPyStatics[13]; /* 'name' */
    cpy_r_r1068 = CPyStatics[14]; /* 'arg0' */
    cpy_r_r1069 = CPyStatics[15]; /* 'type' */
    cpy_r_r1070 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1071 = CPyDict_Build(3, cpy_r_r1065, cpy_r_r1066, cpy_r_r1067, cpy_r_r1068, cpy_r_r1069, cpy_r_r1070);
    if (unlikely(cpy_r_r1071 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 539, CPyStatic_globals);
        goto CPyL300;
    }
    cpy_r_r1072 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1073 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1074 = CPyStatics[13]; /* 'name' */
    cpy_r_r1075 = CPyStatics[16]; /* 'arg1' */
    cpy_r_r1076 = CPyStatics[15]; /* 'type' */
    cpy_r_r1077 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1078 = CPyDict_Build(3, cpy_r_r1072, cpy_r_r1073, cpy_r_r1074, cpy_r_r1075, cpy_r_r1076, cpy_r_r1077);
    if (unlikely(cpy_r_r1078 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 540, CPyStatic_globals);
        goto CPyL301;
    }
    cpy_r_r1079 = CPyStatics[11]; /* 'internalType' */
    cpy_r_r1080 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1081 = CPyStatics[13]; /* 'name' */
    cpy_r_r1082 = CPyStatics[39]; /* 'arg2' */
    cpy_r_r1083 = CPyStatics[15]; /* 'type' */
    cpy_r_r1084 = CPyStatics[24]; /* 'uint256' */
    cpy_r_r1085 = CPyDict_Build(3, cpy_r_r1079, cpy_r_r1080, cpy_r_r1081, cpy_r_r1082, cpy_r_r1083, cpy_r_r1084);
    if (unlikely(cpy_r_r1085 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 541, CPyStatic_globals);
        goto CPyL302;
    }
    cpy_r_r1086 = PyList_New(4);
    if (unlikely(cpy_r_r1086 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 533, CPyStatic_globals);
        goto CPyL303;
    }
    cpy_r_r1087 = (CPyPtr)&((PyListObject *)cpy_r_r1086)->ob_item;
    cpy_r_r1088 = *(CPyPtr *)cpy_r_r1087;
    *(PyObject * *)cpy_r_r1088 = cpy_r_r1064;
    cpy_r_r1089 = cpy_r_r1088 + 8;
    *(PyObject * *)cpy_r_r1089 = cpy_r_r1071;
    cpy_r_r1090 = cpy_r_r1088 + 16;
    *(PyObject * *)cpy_r_r1090 = cpy_r_r1078;
    cpy_r_r1091 = cpy_r_r1088 + 24;
    *(PyObject * *)cpy_r_r1091 = cpy_r_r1085;
    cpy_r_r1092 = CPyStatics[13]; /* 'name' */
    cpy_r_r1093 = CPyStatics[77]; /* 'logTriple' */
    cpy_r_r1094 = CPyStatics[59]; /* 'outputs' */
    cpy_r_r1095 = PyList_New(0);
    if (unlikely(cpy_r_r1095 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 544, CPyStatic_globals);
        goto CPyL304;
    }
    cpy_r_r1096 = CPyStatics[60]; /* 'stateMutability' */
    cpy_r_r1097 = CPyStatics[61]; /* 'nonpayable' */
    cpy_r_r1098 = CPyStatics[15]; /* 'type' */
    cpy_r_r1099 = CPyStatics[62]; /* 'function' */
    cpy_r_r1100 = CPyDict_Build(5, cpy_r_r1057, cpy_r_r1086, cpy_r_r1092, cpy_r_r1093, cpy_r_r1094, cpy_r_r1095, cpy_r_r1096, cpy_r_r1097, cpy_r_r1098, cpy_r_r1099);
    CPy_DECREF_NO_IMM(cpy_r_r1086);
    CPy_DECREF_NO_IMM(cpy_r_r1095);
    if (unlikely(cpy_r_r1100 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 532, CPyStatic_globals);
        goto CPyL299;
    }
    cpy_r_r1101 = CPyList_Build(33, cpy_r_r44, cpy_r_r74, cpy_r_r83, cpy_r_r103, cpy_r_r133, cpy_r_r163, cpy_r_r193, cpy_r_r223, cpy_r_r283, cpy_r_r313, cpy_r_r322, cpy_r_r372, cpy_r_r422, cpy_r_r442, cpy_r_r462, cpy_r_r482, cpy_r_r502, cpy_r_r570, cpy_r_r610, cpy_r_r650, cpy_r_r678, cpy_r_r706, cpy_r_r726, cpy_r_r762, cpy_r_r790, cpy_r_r842, cpy_r_r870, cpy_r_r890, cpy_r_r942, cpy_r_r970, cpy_r_r990, cpy_r_r1056, cpy_r_r1100);
    if (unlikely(cpy_r_r1101 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r1102 = CPyStatic_globals;
    cpy_r_r1103 = CPyStatics[78]; /* 'EMITTER_CONTRACT_ABI' */
    cpy_r_r1104 = CPyDict_SetItem(cpy_r_r1102, cpy_r_r1103, cpy_r_r1101);
    CPy_DECREF_NO_IMM(cpy_r_r1101);
    cpy_r_r1105 = cpy_r_r1104 >= 0;
    if (unlikely(!cpy_r_r1105)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 9, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r1106 = CPyStatics[79]; /* 'bytecode' */
    cpy_r_r1107 = CPyStatic_globals;
    cpy_r_r1108 = CPyStatics[5]; /* 'EMITTER_CONTRACT_BYTECODE' */
    cpy_r_r1109 = CPyDict_GetItem(cpy_r_r1107, cpy_r_r1108);
    if (unlikely(cpy_r_r1109 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 550, CPyStatic_globals);
        goto CPyL179;
    }
    if (likely(PyUnicode_Check(cpy_r_r1109)))
        cpy_r_r1110 = cpy_r_r1109;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 550, CPyStatic_globals, "str", cpy_r_r1109);
        goto CPyL179;
    }
    cpy_r_r1111 = CPyStatics[80]; /* 'bytecode_runtime' */
    cpy_r_r1112 = CPyStatic_globals;
    cpy_r_r1113 = CPyStatics[7]; /* 'EMITTER_CONTRACT_RUNTIME' */
    cpy_r_r1114 = CPyDict_GetItem(cpy_r_r1112, cpy_r_r1113);
    if (unlikely(cpy_r_r1114 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 551, CPyStatic_globals);
        goto CPyL305;
    }
    if (likely(PyUnicode_Check(cpy_r_r1114)))
        cpy_r_r1115 = cpy_r_r1114;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 551, CPyStatic_globals, "str", cpy_r_r1114);
        goto CPyL305;
    }
    cpy_r_r1116 = CPyStatics[81]; /* 'abi' */
    cpy_r_r1117 = CPyStatic_globals;
    cpy_r_r1118 = CPyStatics[78]; /* 'EMITTER_CONTRACT_ABI' */
    cpy_r_r1119 = CPyDict_GetItem(cpy_r_r1117, cpy_r_r1118);
    if (unlikely(cpy_r_r1119 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 552, CPyStatic_globals);
        goto CPyL306;
    }
    if (likely(PyList_Check(cpy_r_r1119)))
        cpy_r_r1120 = cpy_r_r1119;
    else {
        CPy_TypeErrorTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 552, CPyStatic_globals, "list", cpy_r_r1119);
        goto CPyL306;
    }
    cpy_r_r1121 = CPyDict_Build(3, cpy_r_r1106, cpy_r_r1110, cpy_r_r1111, cpy_r_r1115, cpy_r_r1116, cpy_r_r1120);
    CPy_DECREF(cpy_r_r1110);
    CPy_DECREF(cpy_r_r1115);
    CPy_DECREF_NO_IMM(cpy_r_r1120);
    if (unlikely(cpy_r_r1121 == NULL)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 549, CPyStatic_globals);
        goto CPyL179;
    }
    cpy_r_r1122 = CPyStatic_globals;
    cpy_r_r1123 = CPyStatics[82]; /* 'EMITTER_CONTRACT_DATA' */
    cpy_r_r1124 = CPyDict_SetItem(cpy_r_r1122, cpy_r_r1123, cpy_r_r1121);
    CPy_DECREF(cpy_r_r1121);
    cpy_r_r1125 = cpy_r_r1124 >= 0;
    if (unlikely(!cpy_r_r1125)) {
        CPy_AddTraceback("faster_web3/_utils/contract_sources/contract_data/emitter_contract.py", "<module>", 549, CPyStatic_globals);
        goto CPyL179;
    }
    return 1;
CPyL179: ;
    cpy_r_r1126 = 2;
    return cpy_r_r1126;
CPyL180: ;
    CPy_DecRef(cpy_r_r25);
    goto CPyL179;
CPyL181: ;
    CPy_DecRef(cpy_r_r25);
    CPy_DecRef(cpy_r_r34);
    goto CPyL179;
CPyL182: ;
    CPy_DecRef(cpy_r_r44);
    goto CPyL179;
CPyL183: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r55);
    goto CPyL179;
CPyL184: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r55);
    CPy_DecRef(cpy_r_r64);
    goto CPyL179;
CPyL185: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    goto CPyL179;
CPyL186: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    goto CPyL179;
CPyL187: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r94);
    goto CPyL179;
CPyL188: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    goto CPyL179;
CPyL189: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r114);
    goto CPyL179;
CPyL190: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r114);
    CPy_DecRef(cpy_r_r123);
    goto CPyL179;
CPyL191: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    goto CPyL179;
CPyL192: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r144);
    goto CPyL179;
CPyL193: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r144);
    CPy_DecRef(cpy_r_r153);
    goto CPyL179;
CPyL194: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    goto CPyL179;
CPyL195: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r174);
    goto CPyL179;
CPyL196: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r174);
    CPy_DecRef(cpy_r_r183);
    goto CPyL179;
CPyL197: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    goto CPyL179;
CPyL198: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r204);
    goto CPyL179;
CPyL199: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r204);
    CPy_DecRef(cpy_r_r213);
    goto CPyL179;
CPyL200: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    goto CPyL179;
CPyL201: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r234);
    goto CPyL179;
CPyL202: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r234);
    CPy_DecRef(cpy_r_r243);
    goto CPyL179;
CPyL203: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r234);
    CPy_DecRef(cpy_r_r243);
    CPy_DecRef(cpy_r_r252);
    goto CPyL179;
CPyL204: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r234);
    CPy_DecRef(cpy_r_r243);
    CPy_DecRef(cpy_r_r252);
    CPy_DecRef(cpy_r_r261);
    goto CPyL179;
CPyL205: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r234);
    CPy_DecRef(cpy_r_r243);
    CPy_DecRef(cpy_r_r252);
    CPy_DecRef(cpy_r_r261);
    CPy_DecRef(cpy_r_r270);
    goto CPyL179;
CPyL206: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    goto CPyL179;
CPyL207: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r294);
    goto CPyL179;
CPyL208: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r294);
    CPy_DecRef(cpy_r_r303);
    goto CPyL179;
CPyL209: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    goto CPyL179;
CPyL210: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    goto CPyL179;
CPyL211: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r333);
    goto CPyL179;
CPyL212: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r333);
    CPy_DecRef(cpy_r_r342);
    goto CPyL179;
CPyL213: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r333);
    CPy_DecRef(cpy_r_r342);
    CPy_DecRef(cpy_r_r351);
    goto CPyL179;
CPyL214: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r333);
    CPy_DecRef(cpy_r_r342);
    CPy_DecRef(cpy_r_r351);
    CPy_DecRef(cpy_r_r360);
    goto CPyL179;
CPyL215: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    goto CPyL179;
CPyL216: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r383);
    goto CPyL179;
CPyL217: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r383);
    CPy_DecRef(cpy_r_r392);
    goto CPyL179;
CPyL218: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r383);
    CPy_DecRef(cpy_r_r392);
    CPy_DecRef(cpy_r_r401);
    goto CPyL179;
CPyL219: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r383);
    CPy_DecRef(cpy_r_r392);
    CPy_DecRef(cpy_r_r401);
    CPy_DecRef(cpy_r_r410);
    goto CPyL179;
CPyL220: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    goto CPyL179;
CPyL221: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r433);
    goto CPyL179;
CPyL222: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    goto CPyL179;
CPyL223: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r453);
    goto CPyL179;
CPyL224: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    goto CPyL179;
CPyL225: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r473);
    goto CPyL179;
CPyL226: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    goto CPyL179;
CPyL227: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r493);
    goto CPyL179;
CPyL228: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    goto CPyL179;
CPyL229: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    goto CPyL179;
CPyL230: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    CPy_DecRef(cpy_r_r521);
    goto CPyL179;
CPyL231: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    CPy_DecRef(cpy_r_r521);
    CPy_DecRef(cpy_r_r528);
    goto CPyL179;
CPyL232: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    CPy_DecRef(cpy_r_r521);
    CPy_DecRef(cpy_r_r528);
    CPy_DecRef(cpy_r_r536);
    goto CPyL179;
CPyL233: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    CPy_DecRef(cpy_r_r521);
    CPy_DecRef(cpy_r_r528);
    CPy_DecRef(cpy_r_r546);
    goto CPyL179;
CPyL234: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r513);
    CPy_DecRef(cpy_r_r560);
    goto CPyL179;
CPyL235: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    goto CPyL179;
CPyL236: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r581);
    goto CPyL179;
CPyL237: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r581);
    CPy_DecRef(cpy_r_r590);
    goto CPyL179;
CPyL238: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r581);
    CPy_DecRef(cpy_r_r590);
    CPy_DecRef(cpy_r_r599);
    goto CPyL179;
CPyL239: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    goto CPyL179;
CPyL240: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r621);
    goto CPyL179;
CPyL241: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r621);
    CPy_DecRef(cpy_r_r630);
    goto CPyL179;
CPyL242: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r621);
    CPy_DecRef(cpy_r_r630);
    CPy_DecRef(cpy_r_r639);
    goto CPyL179;
CPyL243: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    goto CPyL179;
CPyL244: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r658);
    goto CPyL179;
CPyL245: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r658);
    CPy_DecRef(cpy_r_r665);
    goto CPyL179;
CPyL246: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r666);
    goto CPyL179;
CPyL247: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    goto CPyL179;
CPyL248: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r686);
    goto CPyL179;
CPyL249: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r686);
    CPy_DecRef(cpy_r_r693);
    goto CPyL179;
CPyL250: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r694);
    goto CPyL179;
CPyL251: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    goto CPyL179;
CPyL252: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r714);
    goto CPyL179;
CPyL253: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r715);
    goto CPyL179;
CPyL254: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    goto CPyL179;
CPyL255: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r734);
    goto CPyL179;
CPyL256: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r734);
    CPy_DecRef(cpy_r_r741);
    goto CPyL179;
CPyL257: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r734);
    CPy_DecRef(cpy_r_r741);
    CPy_DecRef(cpy_r_r748);
    goto CPyL179;
CPyL258: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r749);
    goto CPyL179;
CPyL259: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    goto CPyL179;
CPyL260: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r770);
    goto CPyL179;
CPyL261: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r770);
    CPy_DecRef(cpy_r_r777);
    goto CPyL179;
CPyL262: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r778);
    goto CPyL179;
CPyL263: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    goto CPyL179;
CPyL264: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r798);
    goto CPyL179;
CPyL265: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r798);
    CPy_DecRef(cpy_r_r805);
    goto CPyL179;
CPyL266: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r798);
    CPy_DecRef(cpy_r_r805);
    CPy_DecRef(cpy_r_r812);
    goto CPyL179;
CPyL267: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r798);
    CPy_DecRef(cpy_r_r805);
    CPy_DecRef(cpy_r_r812);
    CPy_DecRef(cpy_r_r819);
    goto CPyL179;
CPyL268: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r798);
    CPy_DecRef(cpy_r_r805);
    CPy_DecRef(cpy_r_r812);
    CPy_DecRef(cpy_r_r819);
    CPy_DecRef(cpy_r_r826);
    goto CPyL179;
CPyL269: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r827);
    goto CPyL179;
CPyL270: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    goto CPyL179;
CPyL271: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r850);
    goto CPyL179;
CPyL272: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r850);
    CPy_DecRef(cpy_r_r857);
    goto CPyL179;
CPyL273: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r858);
    goto CPyL179;
CPyL274: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    goto CPyL179;
CPyL275: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r878);
    goto CPyL179;
CPyL276: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r879);
    goto CPyL179;
CPyL277: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    goto CPyL179;
CPyL278: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r898);
    goto CPyL179;
CPyL279: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r898);
    CPy_DecRef(cpy_r_r905);
    goto CPyL179;
CPyL280: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r898);
    CPy_DecRef(cpy_r_r905);
    CPy_DecRef(cpy_r_r912);
    goto CPyL179;
CPyL281: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r898);
    CPy_DecRef(cpy_r_r905);
    CPy_DecRef(cpy_r_r912);
    CPy_DecRef(cpy_r_r919);
    goto CPyL179;
CPyL282: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r898);
    CPy_DecRef(cpy_r_r905);
    CPy_DecRef(cpy_r_r912);
    CPy_DecRef(cpy_r_r919);
    CPy_DecRef(cpy_r_r926);
    goto CPyL179;
CPyL283: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r927);
    goto CPyL179;
CPyL284: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    goto CPyL179;
CPyL285: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r950);
    goto CPyL179;
CPyL286: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r950);
    CPy_DecRef(cpy_r_r957);
    goto CPyL179;
CPyL287: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r958);
    goto CPyL179;
CPyL288: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    goto CPyL179;
CPyL289: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r978);
    goto CPyL179;
CPyL290: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r979);
    goto CPyL179;
CPyL291: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    goto CPyL179;
CPyL292: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    goto CPyL179;
CPyL293: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    CPy_DecRef(cpy_r_r1006);
    goto CPyL179;
CPyL294: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    CPy_DecRef(cpy_r_r1006);
    CPy_DecRef(cpy_r_r1013);
    goto CPyL179;
CPyL295: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    CPy_DecRef(cpy_r_r1006);
    CPy_DecRef(cpy_r_r1013);
    CPy_DecRef(cpy_r_r1021);
    goto CPyL179;
CPyL296: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    CPy_DecRef(cpy_r_r1006);
    CPy_DecRef(cpy_r_r1013);
    CPy_DecRef(cpy_r_r1031);
    goto CPyL179;
CPyL297: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r998);
    CPy_DecRef(cpy_r_r1043);
    goto CPyL179;
CPyL298: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1044);
    goto CPyL179;
CPyL299: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    goto CPyL179;
CPyL300: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    CPy_DecRef(cpy_r_r1064);
    goto CPyL179;
CPyL301: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    CPy_DecRef(cpy_r_r1064);
    CPy_DecRef(cpy_r_r1071);
    goto CPyL179;
CPyL302: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    CPy_DecRef(cpy_r_r1064);
    CPy_DecRef(cpy_r_r1071);
    CPy_DecRef(cpy_r_r1078);
    goto CPyL179;
CPyL303: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    CPy_DecRef(cpy_r_r1064);
    CPy_DecRef(cpy_r_r1071);
    CPy_DecRef(cpy_r_r1078);
    CPy_DecRef(cpy_r_r1085);
    goto CPyL179;
CPyL304: ;
    CPy_DecRef(cpy_r_r44);
    CPy_DecRef(cpy_r_r74);
    CPy_DecRef(cpy_r_r83);
    CPy_DecRef(cpy_r_r103);
    CPy_DecRef(cpy_r_r133);
    CPy_DecRef(cpy_r_r163);
    CPy_DecRef(cpy_r_r193);
    CPy_DecRef(cpy_r_r223);
    CPy_DecRef(cpy_r_r283);
    CPy_DecRef(cpy_r_r313);
    CPy_DecRef(cpy_r_r322);
    CPy_DecRef(cpy_r_r372);
    CPy_DecRef(cpy_r_r422);
    CPy_DecRef(cpy_r_r442);
    CPy_DecRef(cpy_r_r462);
    CPy_DecRef(cpy_r_r482);
    CPy_DecRef(cpy_r_r502);
    CPy_DecRef(cpy_r_r570);
    CPy_DecRef(cpy_r_r610);
    CPy_DecRef(cpy_r_r650);
    CPy_DecRef(cpy_r_r678);
    CPy_DecRef(cpy_r_r706);
    CPy_DecRef(cpy_r_r726);
    CPy_DecRef(cpy_r_r762);
    CPy_DecRef(cpy_r_r790);
    CPy_DecRef(cpy_r_r842);
    CPy_DecRef(cpy_r_r870);
    CPy_DecRef(cpy_r_r890);
    CPy_DecRef(cpy_r_r942);
    CPy_DecRef(cpy_r_r970);
    CPy_DecRef(cpy_r_r990);
    CPy_DecRef(cpy_r_r1056);
    CPy_DecRef(cpy_r_r1086);
    goto CPyL179;
CPyL305: ;
    CPy_DecRef(cpy_r_r1110);
    goto CPyL179;
CPyL306: ;
    CPy_DecRef(cpy_r_r1110);
    CPy_DecRef(cpy_r_r1115);
    goto CPyL179;
}

int CPyGlobalsInit(void)
{
    static int is_initialized = 0;
    if (is_initialized) return 0;
    
    CPy_Init();
    CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract = Py_None;
    CPyModule_builtins = Py_None;
    if (CPyStatics_Initialize(CPyStatics, CPyLit_Str, CPyLit_Bytes, CPyLit_Int, CPyLit_Float, CPyLit_Complex, CPyLit_Tuple, CPyLit_FrozenSet) < 0) {
        return -1;
    }
    is_initialized = 1;
    return 0;
}

PyObject *CPyStatics[83];
const char * const CPyLit_Str[] = {
    "\001\bbuiltins",
    "\001\341\0000x6080604052348015600e575f5ffd5b506118238061001c5f395ff3fe608060405234801561000f575f5ffd5b50600436106100cd575f3560e01c8063966b50e01161008a578063acabb9ed11610064578063acabb9ed146101cd578063b2ddc449146101e9578063e17bf95614610205578063f82ef69e14610221576100cd565b8063966b50e0146101795780639c37705314610195578063aa6fd822146101b1576100cd565b80630bb563d6146100d157806317c0c180146100ed57806320f0256e146101095780632c0e6fde146101255780635da86c171461014157806390b41d8b1461015d575b5f5ffd5b6100eb60048036038101906100e69190610b73565b61023d565b005b61010760048036038101906101029190610bdd565b610277565b005b610123600480360381019061011e9190610c3b565b61034e565b005b61013f600480360381019061013a9190610d0c565b61046b565b005b61015b60048036038101906101569190610e3d565b6104c5565b005b61017760048036038101906101729190610e7b565b610502565b005b610193600480360381019061018e9190610fe4565b61065f565b005b6101af60048036038101906101aa919061105a565b6106b0565b005b6101cb60048036038101906101c691906110be565b6107c8565b005b6101e760048036038101906101e291906110fc565b61090c565b005b61020360048036038101906101fe9190611172565b61095d565b005b61021f600480360381019061021a919061124e565b6109af565b005b61023b60048036038101906102369190611172565b6109e9565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405161026c91906112f5565b60405180910390a150565b6001601381111561028b5761028a611315565b5b81601381111561029e5761029d611315565b5b036102d4577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60405160405180910390a161034b565b5f60138111156102e7576102e6611315565b5b8160138111156102fa576102f9611315565b5b0361030f5760405160405180910390a061034a565b6040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610341906113b2565b60405180910390fd5b5b50565b6005601381111561036257610361611315565b5b85601381111561037557610374611315565b5b036103bc577ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf9848484846040516103af94939291906113df565b60405180910390a1610464565b600b60138111156103d0576103cf611315565b5b8560138111156103e3576103e2611315565b5b036104285780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b5868660405161041b929190611422565b60405180910390a3610463565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161045a906113b2565b60405180910390fd5b5b5050505050565b838573ffffffffffffffffffffffffffffffffffffffff167fd5adc9babd0133de6cececc75e340da3fc18ae5ccab91bc1c03ff3b194f9a3c18585856040516104b693929190611458565b60405180910390a35050505050565b7f8ccce2523cca5f3851d20df50b5a59509bc4ac7d9ddba344f5e331969d09b8e782826040516104f69291906114fd565b60405180910390a15050565b6003601381111561051657610515611315565b5b83601381111561052957610528611315565b5b0361056c577fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5828260405161055f929190611422565b60405180910390a161065a565b600960138111156105805761057f611315565b5b83601381111561059357610592611315565b5b036105d557807f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca836040516105c89190611524565b60405180910390a2610659565b600860138111156105e9576105e8611315565b5b8360138111156105fc576105fb611315565b5b0361061d5780826040516106109190611524565b60405180910390a1610658565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161064f906113b2565b60405180910390fd5b5b5b505050565b8160405161066d91906115ee565b60405180910390207fdbc4c1d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040516106a49190611696565b60405180910390a25050565b600460138111156106c4576106c3611315565b5b8460138111156106d7576106d6611315565b5b0361071c577f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5506283838360405161070f939291906116b6565b60405180910390a16107c2565b600a60138111156107305761072f611315565b5b84601381111561074357610742611315565b5b036107865780827ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec856040516107799190611524565b60405180910390a36107c1565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107b8906113b2565b60405180910390fd5b5b50505050565b600260138111156107dc576107db611315565b5b8260138111156107ef576107ee611315565b5b03610830577f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516108239190611524565b60405180910390a1610908565b6007601381111561084457610843611315565b5b82601381111561085757610856611315565b5b0361088e57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a2610907565b600660138111156108a2576108a1611315565b5b8260138111156108b5576108b4611315565b5b036108cb578060405160405180910390a1610906565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108fd906113b2565b60405180910390fd5b5b5b5050565b8160405161091a9190611725565b60405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405161095191906112f5565b60405180910390a25050565b8173ffffffffffffffffffffffffffffffffffffffff167ff922c215689548d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c826040516109a3919061173b565b60405180910390a25050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040516109de91906117a6565b60405180910390a150565b7f06029e18f16caae06a69281f35b00ed3fcf47950e6c99dafa1bdd8c4b93479a08282604051610a1a9291906117c6565b60405180910390a15050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610a8582610a3f565b810181811067ffffffffffffffff82111715610aa457610aa3610a4f565b5b80604052505050565b5f610ab6610a26565b9050610ac28282610a7c565b919050565b5f67ffffffffffffffff821115610ae157610ae0610a4f565b5b610aea82610a3f565b9050602081019050919050565b828183375f83830152505050565b5f610b17610b1284610ac7565b610aad565b905082815260208101848484011115610b3357610b32610a3b565b5b610b3e848285610af7565b509392505050565b5f82601f830112610b5a57610b59610a37565b5b8135610b6a848260208601610b05565b91505092915050565b5f60208284031215610b8857610b87610a2f565b5b5f82013567ffffffffffffffff811115610ba557610ba4610a33565b5b610bb184828501610b46565b91505092915050565b60148110610bc6575f5ffd5b50565b5f81359050610bd781610bba565b92915050565b5f60208284031215610bf257610bf1610a2f565b5b5f610bff84828501610bc9565b91505092915050565b5f819050919050565b610c1a81610c08565b8114610c24575f5ffd5b50565b5f81359050610c3581610c11565b92915050565b5f5f5f5f5f60a08688031215610c5457610c53610a2f565b5b5f610c6188828901610bc9565b9550506020610c7288828901610c27565b9450506040610c8388828901610c27565b9350506060610c9488828901610c27565b9250506080610ca588828901610c27565b9150509295509295909350565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610cdb82610cb2565b9050919050565b610ceb81610cd1565b8114610cf5575f5ffd5b50565b5f81359050610d0681610ce2565b92915050565b5f5f5f5f5f60a08688031215610d2557610d24610a2f565b5b5f610d3288828901610cf8565b9550506020610d4388828901610c27565b9450506040610d5488828901610cf8565b9350506060610d6588828901610c27565b925050608086013567ffffffffffffffff811115610d8657610d85610a33565b5b610d9288828901610b46565b9150509295509295909350565b5f5ffd5b5f60208284031215610db857610db7610d9f565b5b610dc26020610aad565b90505f610dd184828501610c27565b5f8301525092915050565b5f60608284031215610df157610df0610d9f565b5b610dfb6060610aad565b90505f610e0a84828501610c27565b5f830152506020610e1d84828501610c27565b6020830152506040610e3184828501610da3565b60408301525092915050565b5f5f60808385031215610e5357610e52610a2f565b5b5f610e6085828601610c27565b9250506020610e7185828601610ddc565b9150509250929050565b5f5f5f60608486031215610e9257610e91610a2f565b5b5f610e9f86828701610bc9565b9350506020610eb086828701610c27565b9250506040610ec186828701610c27565b9150509250925092565b5f67ffffffffffffffff821115610ee557610ee4610a4f565b5b602082029050602081019050919050565b5f5ffd5b5f7fffff00000000000000000000000000000000000000000000000000000000000082169050919050565b610f2e81610efa565b8114610f38575f5ffd5b50565b5f81359050610f4981610f25565b92915050565b5f610f61610f5c84610ecb565b610aad565b90508083825260208201905060208402830185811115610f8457610f83610ef6565b5b835b81811015610fad5780610f998882610f3b565b845260208401935050602081019050610f86565b5050509392505050565b5f82601f830112610fcb57610fca610a37565b5b8135610fdb848260208601610f4f565b91505092915050565b5f5f60408385031215610ffa57610ff9610a2f565b5b5f83013567ffffffffffffffff81111561101757611016610a33565b5b61102385828601610fb7565b925050602083013567ffffffffffffffff81111561104457611043610a33565b5b61105085828601610fb7565b9150509250929050565b5f5f5f5f6080858703121561107257611071610a2f565b5b5f61107f87828801610bc9565b945050602061109087828801610c27565b93505060406110a187828801610c27565b92505060606110b287828801610c27565b91505092959194509250565b5f5f604083850312156110d4576110d3610a2f565b5b5f6110e185828601610bc9565b92505060206110f285828601610c27565b9150509250929050565b5f5f6040838503121561111257611111610a2f565b5b5f83013567ffffffffffffffff81111561112f5761112e610a33565b5b61113b85828601610b46565b925050602083013567ffffffffffffffff81111561115c5761115b610a33565b5b61116885828601610b46565b9150509250929050565b5f5f6040838503121561118857611187610a2f565b5b5f61119585828601610cf8565b92505060206111a685828601610cf8565b9150509250929050565b5f67ffffffffffffffff8211156111ca576111c9610a4f565b5b6111d382610a3f565b9050602081019050919050565b5f6111f26111ed846111b0565b610aad565b90508281526020810184848401111561120e5761120d610a3b565b5b611219848285610af7565b509392505050565b5f82601f83011261123557611234610a37565b5b81356112458482602086016111e0565b91505092915050565b5f6020828403121561126357611262610a2f565b5b5f82013567ffffffffffffffff8111156112805761127f610a33565b5b61128c84828501611221565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6112c782611295565b6112d1818561129f565b93506112e18185602086016112af565b6112ea81610a3f565b840191505092915050565b5f6020820190508181035f83015261130d81846112bd565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4469646e2774206d6174636820616e7920616c6c6f7761626c65206576656e745f8201527f20696e6465780000000000000000000000000000000000000000000000000000602082015250565b5f61139c60268361129f565b91506113a782611342565b604082019050919050565b5f6020820190508181035f8301526113c981611390565b9050919050565b6113d981610c08565b82525050565b5f6080820190506113f25f8301876113d0565b6113ff60208301866113d0565b61140c60408301856113d0565b61141960608301846113d0565b95945050505050565b5f6040820190506114355f8301856113d0565b61144260208301846113d0565b9392505050565b61145281610cd1565b82525050565b5f60608201905061146b5f830186611449565b61147860208301856113d0565b818103604083015261148a81846112bd565b9050949350505050565b61149d81610c08565b82525050565b602082015f8201516114b75f850182611494565b50505050565b606082015f8201516114d15f850182611494565b5060208201516114e46020850182611494565b5060408201516114f760408501826114a3565b50505050565b5f6080820190506115105f8301856113d0565b61151d60208301846114bd565b9392505050565b5f6020820190506115375f8301846113d0565b92915050565b5f81519050919050565b5f81905092915050565b5f819050602082019050919050565b61156981610efa565b82525050565b5f61157a8383611560565b60208301905092915050565b5f602082019050919050565b5f61159c8261153d565b6115a68185611547565b93506115b183611551565b805f5b838110156115e15781516115c8888261156f565b97506115d383611586565b9250506001810190506115b4565b5085935050505092915050565b5f6115f98284611592565b915081905092915050565b5f82825260208201905092915050565b61161d81610efa565b82525050565b5f61162e8383611614565b60208301905092915050565b5f6116448261153d565b61164e8185611604565b935061165983611551565b805f5b838110156116895781516116708882611623565b975061167b83611586565b92505060018101905061165c565b5085935050505092915050565b5f6020820190508181035f8301526116ae818461163a565b905092915050565b5f6060820190506116c95f8301866113d0565b6116d660208301856113d0565b6116e360408301846113d0565b949350505050565b5f81905092915050565b5f6116ff82611295565b61170981856116eb565b93506117198185602086016112af565b80840191505092915050565b5f61173082846116f5565b915081905092915050565b5f60208201905061174e5f830184611449565b92915050565b5f81519050919050565b5f82825260208201905092915050565b5f61177882611754565b611782818561175e565b93506117928185602086016112af565b61179b81610a3f565b840191505092915050565b5f6020820190508181035f8301526117be818461176e565b905092915050565b5f6040820190506117d95f830185611449565b6117e66020830184611449565b939250505056fea264697066735822122003376e7a5d27c43ad43676e9f1efff563c626b7d1b96bd09006b9562e3dc714b64736f6c634300081e0033",
    "\001\031EMITTER_CONTRACT_BYTECODE",
    "\001\340H0x608060405234801561000f575f5ffd5b50600436106100cd575f3560e01c8063966b50e01161008a578063acabb9ed11610064578063acabb9ed146101cd578063b2ddc449146101e9578063e17bf95614610205578063f82ef69e14610221576100cd565b8063966b50e0146101795780639c37705314610195578063aa6fd822146101b1576100cd565b80630bb563d6146100d157806317c0c180146100ed57806320f0256e146101095780632c0e6fde146101255780635da86c171461014157806390b41d8b1461015d575b5f5ffd5b6100eb60048036038101906100e69190610b73565b61023d565b005b61010760048036038101906101029190610bdd565b610277565b005b610123600480360381019061011e9190610c3b565b61034e565b005b61013f600480360381019061013a9190610d0c565b61046b565b005b61015b60048036038101906101569190610e3d565b6104c5565b005b61017760048036038101906101729190610e7b565b610502565b005b610193600480360381019061018e9190610fe4565b61065f565b005b6101af60048036038101906101aa919061105a565b6106b0565b005b6101cb60048036038101906101c691906110be565b6107c8565b005b6101e760048036038101906101e291906110fc565b61090c565b005b61020360048036038101906101fe9190611172565b61095d565b005b61021f600480360381019061021a919061124e565b6109af565b005b61023b60048036038101906102369190611172565b6109e9565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405161026c91906112f5565b60405180910390a150565b6001601381111561028b5761028a611315565b5b81601381111561029e5761029d611315565b5b036102d4577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60405160405180910390a161034b565b5f60138111156102e7576102e6611315565b5b8160138111156102fa576102f9611315565b5b0361030f5760405160405180910390a061034a565b6040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610341906113b2565b60405180910390fd5b5b50565b6005601381111561036257610361611315565b5b85601381111561037557610374611315565b5b036103bc577ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf9848484846040516103af94939291906113df565b60405180910390a1610464565b600b60138111156103d0576103cf611315565b5b8560138111156103e3576103e2611315565b5b036104285780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b5868660405161041b929190611422565b60405180910390a3610463565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161045a906113b2565b60405180910390fd5b5b5050505050565b838573ffffffffffffffffffffffffffffffffffffffff167fd5adc9babd0133de6cececc75e340da3fc18ae5ccab91bc1c03ff3b194f9a3c18585856040516104b693929190611458565b60405180910390a35050505050565b7f8ccce2523cca5f3851d20df50b5a59509bc4ac7d9ddba344f5e331969d09b8e782826040516104f69291906114fd565b60405180910390a15050565b6003601381111561051657610515611315565b5b83601381111561052957610528611315565b5b0361056c577fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5828260405161055f929190611422565b60405180910390a161065a565b600960138111156105805761057f611315565b5b83601381111561059357610592611315565b5b036105d557807f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca836040516105c89190611524565b60405180910390a2610659565b600860138111156105e9576105e8611315565b5b8360138111156105fc576105fb611315565b5b0361061d5780826040516106109190611524565b60405180910390a1610658565b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161064f906113b2565b60405180910390fd5b5b5b505050565b8160405161066d91906115ee565b60405180910390207fdbc4c1d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040516106a49190611696565b60405180910390a25050565b600460138111156106c4576106c3611315565b5b8460138111156106d7576106d6611315565b5b0361071c577f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5506283838360405161070f939291906116b6565b60405180910390a16107c2565b600a60138111156107305761072f611315565b5b84601381111561074357610742611315565b5b036107865780827ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec856040516107799190611524565b60405180910390a36107c1565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016107b8906113b2565b60405180910390fd5b5b50505050565b600260138111156107dc576107db611315565b5b8260138111156107ef576107ee611315565b5b03610830577f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d4816040516108239190611524565b60405180910390a1610908565b6007601381111561084457610843611315565b5b82601381111561085757610856611315565b5b0361088e57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a2610907565b600660138111156108a2576108a1611315565b5b8260138111156108b5576108b4611315565b5b036108cb578060405160405180910390a1610906565b6040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016108fd906113b2565b60405180910390fd5b5b5b5050565b8160405161091a9190611725565b60405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405161095191906112f5565b60405180910390a25050565b8173ffffffffffffffffffffffffffffffffffffffff167ff922c215689548d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c826040516109a3919061173b565b60405180910390a25050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040516109de91906117a6565b60405180910390a150565b7f06029e18f16caae06a69281f35b00ed3fcf47950e6c99dafa1bdd8c4b93479a08282604051610a1a9291906117c6565b60405180910390a15050565b5f604051905090565b5f5ffd5b5f5ffd5b5f5ffd5b5f5ffd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b610a8582610a3f565b810181811067ffffffffffffffff82111715610aa457610aa3610a4f565b5b80604052505050565b5f610ab6610a26565b9050610ac28282610a7c565b919050565b5f67ffffffffffffffff821115610ae157610ae0610a4f565b5b610aea82610a3f565b9050602081019050919050565b828183375f83830152505050565b5f610b17610b1284610ac7565b610aad565b905082815260208101848484011115610b3357610b32610a3b565b5b610b3e848285610af7565b509392505050565b5f82601f830112610b5a57610b59610a37565b5b8135610b6a848260208601610b05565b91505092915050565b5f60208284031215610b8857610b87610a2f565b5b5f82013567ffffffffffffffff811115610ba557610ba4610a33565b5b610bb184828501610b46565b91505092915050565b60148110610bc6575f5ffd5b50565b5f81359050610bd781610bba565b92915050565b5f60208284031215610bf257610bf1610a2f565b5b5f610bff84828501610bc9565b91505092915050565b5f819050919050565b610c1a81610c08565b8114610c24575f5ffd5b50565b5f81359050610c3581610c11565b92915050565b5f5f5f5f5f60a08688031215610c5457610c53610a2f565b5b5f610c6188828901610bc9565b9550506020610c7288828901610c27565b9450506040610c8388828901610c27565b9350506060610c9488828901610c27565b9250506080610ca588828901610c27565b9150509295509295909350565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f610cdb82610cb2565b9050919050565b610ceb81610cd1565b8114610cf5575f5ffd5b50565b5f81359050610d0681610ce2565b92915050565b5f5f5f5f5f60a08688031215610d2557610d24610a2f565b5b5f610d3288828901610cf8565b9550506020610d4388828901610c27565b9450506040610d5488828901610cf8565b9350506060610d6588828901610c27565b925050608086013567ffffffffffffffff811115610d8657610d85610a33565b5b610d9288828901610b46565b9150509295509295909350565b5f5ffd5b5f60208284031215610db857610db7610d9f565b5b610dc26020610aad565b90505f610dd184828501610c27565b5f8301525092915050565b5f60608284031215610df157610df0610d9f565b5b610dfb6060610aad565b90505f610e0a84828501610c27565b5f830152506020610e1d84828501610c27565b6020830152506040610e3184828501610da3565b60408301525092915050565b5f5f60808385031215610e5357610e52610a2f565b5b5f610e6085828601610c27565b9250506020610e7185828601610ddc565b9150509250929050565b5f5f5f60608486031215610e9257610e91610a2f565b5b5f610e9f86828701610bc9565b9350506020610eb086828701610c27565b9250506040610ec186828701610c27565b9150509250925092565b5f67ffffffffffffffff821115610ee557610ee4610a4f565b5b602082029050602081019050919050565b5f5ffd5b5f7fffff00000000000000000000000000000000000000000000000000000000000082169050919050565b610f2e81610efa565b8114610f38575f5ffd5b50565b5f81359050610f4981610f25565b92915050565b5f610f61610f5c84610ecb565b610aad565b90508083825260208201905060208402830185811115610f8457610f83610ef6565b5b835b81811015610fad5780610f998882610f3b565b845260208401935050602081019050610f86565b5050509392505050565b5f82601f830112610fcb57610fca610a37565b5b8135610fdb848260208601610f4f565b91505092915050565b5f5f60408385031215610ffa57610ff9610a2f565b5b5f83013567ffffffffffffffff81111561101757611016610a33565b5b61102385828601610fb7565b925050602083013567ffffffffffffffff81111561104457611043610a33565b5b61105085828601610fb7565b9150509250929050565b5f5f5f5f6080858703121561107257611071610a2f565b5b5f61107f87828801610bc9565b945050602061109087828801610c27565b93505060406110a187828801610c27565b92505060606110b287828801610c27565b91505092959194509250565b5f5f604083850312156110d4576110d3610a2f565b5b5f6110e185828601610bc9565b92505060206110f285828601610c27565b9150509250929050565b5f5f6040838503121561111257611111610a2f565b5b5f83013567ffffffffffffffff81111561112f5761112e610a33565b5b61113b85828601610b46565b925050602083013567ffffffffffffffff81111561115c5761115b610a33565b5b61116885828601610b46565b9150509250929050565b5f5f6040838503121561118857611187610a2f565b5b5f61119585828601610cf8565b92505060206111a685828601610cf8565b9150509250929050565b5f67ffffffffffffffff8211156111ca576111c9610a4f565b5b6111d382610a3f565b9050602081019050919050565b5f6111f26111ed846111b0565b610aad565b90508281526020810184848401111561120e5761120d610a3b565b5b611219848285610af7565b509392505050565b5f82601f83011261123557611234610a37565b5b81356112458482602086016111e0565b91505092915050565b5f6020828403121561126357611262610a2f565b5b5f82013567ffffffffffffffff8111156112805761127f610a33565b5b61128c84828501611221565b91505092915050565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f6112c782611295565b6112d1818561129f565b93506112e18185602086016112af565b6112ea81610a3f565b840191505092915050565b5f6020820190508181035f83015261130d81846112bd565b905092915050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602160045260245ffd5b7f4469646e2774206d6174636820616e7920616c6c6f7761626c65206576656e745f8201527f20696e6465780000000000000000000000000000000000000000000000000000602082015250565b5f61139c60268361129f565b91506113a782611342565b604082019050919050565b5f6020820190508181035f8301526113c981611390565b9050919050565b6113d981610c08565b82525050565b5f6080820190506113f25f8301876113d0565b6113ff60208301866113d0565b61140c60408301856113d0565b61141960608301846113d0565b95945050505050565b5f6040820190506114355f8301856113d0565b61144260208301846113d0565b9392505050565b61145281610cd1565b82525050565b5f60608201905061146b5f830186611449565b61147860208301856113d0565b818103604083015261148a81846112bd565b9050949350505050565b61149d81610c08565b82525050565b602082015f8201516114b75f850182611494565b50505050565b606082015f8201516114d15f850182611494565b5060208201516114e46020850182611494565b5060408201516114f760408501826114a3565b50505050565b5f6080820190506115105f8301856113d0565b61151d60208301846114bd565b9392505050565b5f6020820190506115375f8301846113d0565b92915050565b5f81519050919050565b5f81905092915050565b5f819050602082019050919050565b61156981610efa565b82525050565b5f61157a8383611560565b60208301905092915050565b5f602082019050919050565b5f61159c8261153d565b6115a68185611547565b93506115b183611551565b805f5b838110156115e15781516115c8888261156f565b97506115d383611586565b9250506001810190506115b4565b5085935050505092915050565b5f6115f98284611592565b915081905092915050565b5f82825260208201905092915050565b61161d81610efa565b82525050565b5f61162e8383611614565b60208301905092915050565b5f6116448261153d565b61164e8185611604565b935061165983611551565b805f5b838110156116895781516116708882611623565b975061167b83611586565b92505060018101905061165c565b5085935050505092915050565b5f6020820190508181035f8301526116ae818461163a565b905092915050565b5f6060820190506116c95f8301866113d0565b6116d660208301856113d0565b6116e360408301846113d0565b949350505050565b5f81905092915050565b5f6116ff82611295565b61170981856116eb565b93506117198185602086016112af565b80840191505092915050565b5f61173082846116f5565b915081905092915050565b5f60208201905061174e5f830184611449565b92915050565b5f81519050919050565b5f82825260208201905092915050565b5f61177882611754565b611782818561175e565b93506117928185602086016112af565b61179b81610a3f565b840191505092915050565b5f6020820190508181035f8301526117be818461176e565b905092915050565b5f6040820190506117d95f830185611449565b6117e66020830184611449565b939250505056fea264697066735822122003376e7a5d27c43ad43676e9f1efff563c626b7d1b96bd09006b9562e3dc714b64736f6c634300081e0033",
    "\005\030EMITTER_CONTRACT_RUNTIME\tanonymous\006inputs\aindexed\finternalType",
    "\a\aaddress\004name\004arg0\004type\004arg1\021LogAddressIndexed\005event",
    "\006\024LogAddressNotIndexed\fLogAnonymous\005bytes\001v\bLogBytes\auint256",
    "\004\022LogDoubleAnonymous\fLogDoubleArg\022LogDoubleWithIndex\006string",
    "\004\016LogDynamicArgs\016indexedAddress\016indexedUint256\021nonIndexedAddress",
    "\004\021nonIndexedUint256\020nonIndexedString\027LogIndexedAndNotIndexed\bbytes2[]",
    "\005\vLogListArgs\016LogNoArguments\004arg2\004arg3\017LogQuadrupleArg",
    "\003\025LogQuadrupleWithIndex\022LogSingleAnonymous\fLogSingleArg",
    "\006\022LogSingleWithIndex\tLogString\ncomponents\001a\001b\001c",
    "\003&struct EmitterContract.NestedTestTuple\006nested\005tuple",
    "\003 struct EmitterContract.TestTuple\rLogStructArgs\fLogTripleArg",
    "\004\022LogTripleWithIndex\025logAddressIndexedArgs\aoutputs\017stateMutability",
    "\004\nnonpayable\bfunction\030logAddressNotIndexedArgs\blogBytes",
    "\005\037enum EmitterContract.WhichEvent\005which\005uint8\tlogDouble\016logDynamicArgs",
    "\004\033logIndexedAndNotIndexedArgs\vlogListArgs\tlogNoArgs\flogQuadruple",
    "\006\tlogSingle\tlogString\tlogStruct\tlogTriple\024EMITTER_CONTRACT_ABI\bbytecode",
    "\003\020bytecode_runtime\003abi\025EMITTER_CONTRACT_DATA",
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
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract__internal = NULL;
CPyModule *CPyModule_faster_web3____utils___contract_sources___contract_data___emitter_contract;
PyObject *CPyStatic_globals;
CPyModule *CPyModule_builtins;
char CPyDef___top_level__(void);

static int exec_emitter_contract__mypyc(PyObject *module)
{
    int res;
    PyObject *capsule;
    PyObject *tmp;
    
    extern PyObject *CPyInit_faster_web3____utils___contract_sources___contract_data___emitter_contract(void);
    capsule = PyCapsule_New((void *)CPyInit_faster_web3____utils___contract_sources___contract_data___emitter_contract, "faster_web3._utils.contract_sources.contract_data.emitter_contract__mypyc.init_faster_web3____utils___contract_sources___contract_data___emitter_contract", NULL);
    if (!capsule) {
        goto fail;
    }
    res = PyObject_SetAttrString(module, "init_faster_web3____utils___contract_sources___contract_data___emitter_contract", capsule);
    Py_DECREF(capsule);
    if (res < 0) {
        goto fail;
    }
    
    return 0;
    fail:
    return -1;
}
static PyModuleDef module_def_emitter_contract__mypyc = {
    PyModuleDef_HEAD_INIT,
    .m_name = "faster_web3._utils.contract_sources.contract_data.emitter_contract__mypyc",
    .m_doc = NULL,
    .m_size = -1,
    .m_methods = NULL,
};
PyMODINIT_FUNC PyInit_emitter_contract__mypyc(void) {
    static PyObject *module = NULL;
    if (module) {
        Py_INCREF(module);
        return module;
    }
    module = PyModule_Create(&module_def_emitter_contract__mypyc);
    if (!module) {
        return NULL;
    }
    if (exec_emitter_contract__mypyc(module) < 0) {
        Py_DECREF(module);
        return NULL;
    }
    return module;
}
