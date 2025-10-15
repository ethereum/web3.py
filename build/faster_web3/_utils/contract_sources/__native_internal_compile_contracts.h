#ifndef MYPYC_NATIVE_INTERNAL_faster_web3____utils___contract_sources___compile_contracts_H
#define MYPYC_NATIVE_INTERNAL_faster_web3____utils___contract_sources___compile_contracts_H
#include <Python.h>
#include <CPy.h>
#include "__native_compile_contracts.h"

int CPyGlobalsInit(void);

extern PyObject *CPyStatics[110];
extern const char * const CPyLit_Str[];
extern const char * const CPyLit_Bytes[];
extern const char * const CPyLit_Int[];
extern const double CPyLit_Float[];
extern const double CPyLit_Complex[];
extern const int CPyLit_Tuple[];
extern const int CPyLit_FrozenSet[];
extern CPyModule *CPyModule_faster_web3____utils___contract_sources___compile_contracts__internal;
extern CPyModule *CPyModule_faster_web3____utils___contract_sources___compile_contracts;
extern PyObject *CPyStatic_globals;
extern CPyModule *CPyModule_builtins;
extern CPyModule *CPyModule_argparse;
extern CPyModule *CPyModule_os;
extern CPyModule *CPyModule_re;
extern CPyModule *CPyModule_typing;
extern CPyModule *CPyModule_solcx;
extern PyObject *CPyDef__compile_dot_sol_files(PyObject *cpy_r_dot_sol_filename);
extern PyObject *CPyPy__compile_dot_sol_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern PyObject *CPyDef__get_compiled_contract_data(PyObject *cpy_r_sol_file_output, PyObject *cpy_r_dot_sol_filename, PyObject *cpy_r_contract_name);
extern PyObject *CPyPy__get_compiled_contract_data(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef_compile_files(PyObject *cpy_r_file_list);
extern PyObject *CPyPy_compile_files(PyObject *self, PyObject *const *args, size_t nargs, PyObject *kwnames);
extern char CPyDef___top_level__(void);
#endif
