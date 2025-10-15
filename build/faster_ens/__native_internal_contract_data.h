#ifndef MYPYC_NATIVE_INTERNAL_faster_ens___contract_data_H
#define MYPYC_NATIVE_INTERNAL_faster_ens___contract_data_H
#include <Python.h>
#include <CPy.h>
#include "__native_contract_data.h"

int CPyGlobalsInit(void);

extern PyObject *CPyStatics[42];
extern const char * const CPyLit_Str[];
extern const char * const CPyLit_Bytes[];
extern const char * const CPyLit_Int[];
extern const double CPyLit_Float[];
extern const double CPyLit_Complex[];
extern const int CPyLit_Tuple[];
extern const int CPyLit_FrozenSet[];
extern CPyModule *CPyModule_faster_ens___contract_data__internal;
extern CPyModule *CPyModule_faster_ens___contract_data;
extern PyObject *CPyStatic_globals;
extern CPyModule *CPyModule_builtins;
extern CPyModule *CPyModule_json;
extern CPyModule *CPyModule_typing;
extern CPyModule *CPyModule_eth_typing;
extern PyObject *CPyStatic_registrar_abi;
extern PyObject *CPyStatic_registrar_bytecode;
extern PyObject *CPyStatic_registrar_bytecode_runtime;
extern PyObject *CPyStatic_resolver_abi;
extern PyObject *CPyStatic_resolver_bytecode;
extern PyObject *CPyStatic_resolver_bytecode_runtime;
extern PyObject *CPyStatic_reverse_registrar_abi;
extern PyObject *CPyStatic_reverse_registrar_bytecode;
extern PyObject *CPyStatic_reverse_registrar_bytecode_runtime;
extern PyObject *CPyStatic_reverse_resolver_abi;
extern PyObject *CPyStatic_reverse_resolver_bytecode;
extern PyObject *CPyStatic_reverse_resolver_bytecode_runtime;
extern char CPyDef___top_level__(void);
#endif
