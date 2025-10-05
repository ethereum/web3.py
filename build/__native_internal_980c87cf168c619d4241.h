#ifndef MYPYC_NATIVE_INTERNAL_980c87cf168c619d4241_H
#define MYPYC_NATIVE_INTERNAL_980c87cf168c619d4241_H
#include <Python.h>
#include <CPy.h>
#include "__native_980c87cf168c619d4241.h"

int CPyGlobalsInit(void);

extern PyObject *CPyStatics[45];
extern const char * const CPyLit_Str[];
extern const char * const CPyLit_Bytes[];
extern const char * const CPyLit_Int[];
extern const double CPyLit_Float[];
extern const double CPyLit_Complex[];
extern const int CPyLit_Tuple[];
extern const int CPyLit_FrozenSet[];
extern CPyModule *CPyModule_faster_web3____utils___http__internal;
extern CPyModule *CPyModule_faster_web3____utils___http;
extern PyObject *CPyStatic_http___globals;
extern CPyModule *CPyModule_builtins;
extern CPyModule *CPyModule_typing;
extern CPyModule *CPyModule_faster_web3;
extern CPyModule *CPyModule_faster_web3____utils___math__internal;
extern CPyModule *CPyModule_faster_web3____utils___math;
extern PyObject *CPyStatic_math___globals;
extern CPyModule *CPyModule_faster_web3___exceptions;
extern CPyModule *CPyModule_faster_web3____utils___type_conversion__internal;
extern CPyModule *CPyModule_faster_web3____utils___type_conversion;
extern PyObject *CPyStatic_type_conversion___globals;
extern CPyModule *CPyModule_eth_utils;
extern CPyModule *CPyModule_eth_typing;
extern PyObject *CPyDef_http___construct_user_agent(PyObject *cpy_r_module, PyObject *cpy_r_class_name);
extern PyObject *CPyPy_http___construct_user_agent(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef_http_____top_level__(void);
extern double CPyDef_math___percentile(PyObject *cpy_r_values, double cpy_r_percentile);
extern PyObject *CPyPy_math___percentile(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef_math_____top_level__(void);
extern PyObject *CPyStatic_type_conversion___to_bytes;
extern PyObject *CPyStatic_type_conversion___to_hex;
extern PyObject *CPyDef_type_conversion___to_hex_if_bytes(PyObject *cpy_r_val);
extern PyObject *CPyPy_type_conversion___to_hex_if_bytes(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern PyObject *CPyDef_type_conversion___to_bytes_if_hex(PyObject *cpy_r_val);
extern PyObject *CPyPy_type_conversion___to_bytes_if_hex(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef_type_conversion_____top_level__(void);
#endif
