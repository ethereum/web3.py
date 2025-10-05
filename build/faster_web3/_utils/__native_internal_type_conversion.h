#ifndef MYPYC_NATIVE_INTERNAL_faster_web3____utils___type_conversion_H
#define MYPYC_NATIVE_INTERNAL_faster_web3____utils___type_conversion_H
#include <Python.h>
#include <CPy.h>
#include "__native_type_conversion.h"

int CPyGlobalsInit(void);

extern PyObject *CPyStatics[29];
extern const char * const CPyLit_Str[];
extern const char * const CPyLit_Bytes[];
extern const char * const CPyLit_Int[];
extern const double CPyLit_Float[];
extern const double CPyLit_Complex[];
extern const int CPyLit_Tuple[];
extern const int CPyLit_FrozenSet[];
extern CPyModule *CPyModule_faster_web3____utils___type_conversion__internal;
extern CPyModule *CPyModule_faster_web3____utils___type_conversion;
extern PyObject *CPyStatic_globals;
extern CPyModule *CPyModule_builtins;
extern CPyModule *CPyModule_typing;
extern CPyModule *CPyModule_eth_utils;
extern CPyModule *CPyModule_eth_typing;
extern CPyModule *CPyModule_faster_web3___exceptions;
extern PyObject *CPyStatic_to_bytes;
extern PyObject *CPyStatic_to_hex;
extern PyObject *CPyDef_to_hex_if_bytes(PyObject *cpy_r_val);
extern PyObject *CPyPy_to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern PyObject *CPyDef_to_bytes_if_hex(PyObject *cpy_r_val);
extern PyObject *CPyPy_to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef___top_level__(void);
#endif
