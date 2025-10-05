#ifndef MYPYC_NATIVE_375413d3c5455dc0fb2a_H
#define MYPYC_NATIVE_375413d3c5455dc0fb2a_H
#include <Python.h>
#include <CPy.h>
#ifndef MYPYC_DECLARED_tuple_T1O
#define MYPYC_DECLARED_tuple_T1O
typedef struct tuple_T1O {
    PyObject *f0;
} tuple_T1O;
#endif

#ifndef MYPYC_DECLARED_tuple_T3CIO
#define MYPYC_DECLARED_tuple_T3CIO
typedef struct tuple_T3CIO {
    char f0;
    CPyTagged f1;
    PyObject *f2;
} tuple_T3CIO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OO
#define MYPYC_DECLARED_tuple_T2OO
typedef struct tuple_T2OO {
    PyObject *f0;
    PyObject *f1;
} tuple_T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T3OOO
#define MYPYC_DECLARED_tuple_T3OOO
typedef struct tuple_T3OOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3OOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OI
#define MYPYC_DECLARED_tuple_T2OI
typedef struct tuple_T2OI {
    PyObject *f0;
    CPyTagged f1;
} tuple_T2OI;
#endif

#ifndef MYPYC_DECLARED_tuple_T15OOOOOOOOOOOOOOO
#define MYPYC_DECLARED_tuple_T15OOOOOOOOOOOOOOO
typedef struct tuple_T15OOOOOOOOOOOOOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
    PyObject *f4;
    PyObject *f5;
    PyObject *f6;
    PyObject *f7;
    PyObject *f8;
    PyObject *f9;
    PyObject *f10;
    PyObject *f11;
    PyObject *f12;
    PyObject *f13;
    PyObject *f14;
} tuple_T15OOOOOOOOOOOOOOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T5OOOOO
#define MYPYC_DECLARED_tuple_T5OOOOO
typedef struct tuple_T5OOOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
    PyObject *f4;
} tuple_T5OOOOO;
#endif

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___datatypes_____init___3_PropertyCheckingFactory_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___datatypes_____new___3_PropertyCheckingFactory_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_rpc_port;
    PyObject *_endpoint_uri;
    PyObject *_geth_binary;
    PyObject *_datadir;
} faster_web3___tools___benchmark___node___GethBenchmarkFixtureObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    char ___mypyc_temp__2;
    PyObject *___mypyc_generator_attribute__base_dir;
    PyObject *___mypyc_generator_attribute__zipfile_path;
    PyObject *___mypyc_generator_attribute__tmp_datadir;
    PyObject *___mypyc_temp__3;
    PyObject *___mypyc_temp__4;
    char ___mypyc_temp__5;
    PyObject *___mypyc_generator_attribute__zip_ref;
    tuple_T3OOO ___mypyc_temp__6;
    PyObject *___mypyc_generator_attribute__genesis_file;
    tuple_T3OOO ___mypyc_temp__7;
} faster_web3___tools___benchmark___node___build_GethBenchmarkFixture_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__datadir;
    PyObject *___mypyc_generator_attribute__genesis_file;
    PyObject *___mypyc_generator_attribute__rpc_port;
    int32_t ___mypyc_next_label__;
    tuple_T5OOOOO ___mypyc_generator_attribute__init_datadir_command;
    PyObject *___mypyc_generator_attribute__proc;
} faster_web3___tools___benchmark___node____geth_process_GethBenchmarkFixture_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t bitmap;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    CPyTagged ___mypyc_generator_attribute__timeout;
    int32_t ___mypyc_next_label__;
    double ___mypyc_generator_attribute__start;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    char ___mypyc_temp__2;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
    PyObject *___mypyc_generator_attribute__session;
    PyObject *___mypyc_temp__5;
    tuple_T3OOO ___mypyc_temp__6;
    tuple_T3OOO ___mypyc_temp__7;
    PyObject *___mypyc_temp__8;
    tuple_T3OOO ___mypyc_temp__9;
    PyObject *___mypyc_temp__10;
    tuple_T3OOO ___mypyc_temp__11;
    tuple_T3OOO ___mypyc_temp__12;
    PyObject *___mypyc_temp__13;
    tuple_T3OOO ___mypyc_temp__14;
} faster_web3___tools___benchmark___utils___wait_for_aiohttp_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    CPyTagged __size;
    PyObject *__data;
} faster_web3___utils___caching___SimpleCacheObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t bitmap;
    PyObject *___mypyc_generator_attribute__self;
    char ___mypyc_generator_attribute__last;
    double ___mypyc_generator_attribute__timeout;
    int32_t ___mypyc_next_label__;
    double ___mypyc_generator_attribute__start;
    double ___mypyc_generator_attribute__end_time;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    tuple_T3OOO ___mypyc_temp__2;
    double ___mypyc_generator_attribute__now;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
} faster_web3___utils___caching___async_await_and_popitem_SimpleCache_genObject;

#endif
