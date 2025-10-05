#ifndef MYPYC_NATIVE_e60543e00a47358a5fd8_H
#define MYPYC_NATIVE_e60543e00a47358a5fd8_H
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

#endif
