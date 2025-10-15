#ifndef MYPYC_NATIVE_INTERNAL_faster_ens___abis_H
#define MYPYC_NATIVE_INTERNAL_faster_ens___abis_H
#include <Python.h>
#include <CPy.h>
#include "__native_abis.h"

int CPyGlobalsInit(void);

extern PyObject *CPyStatics[193];
extern const char * const CPyLit_Str[];
extern const char * const CPyLit_Bytes[];
extern const char * const CPyLit_Int[];
extern const double CPyLit_Float[];
extern const double CPyLit_Complex[];
extern const int CPyLit_Tuple[];
extern const int CPyLit_FrozenSet[];
extern CPyModule *CPyModule_faster_ens___abis__internal;
extern CPyModule *CPyModule_faster_ens___abis;
extern PyObject *CPyStatic_globals;
extern CPyModule *CPyModule_builtins;
extern CPyModule *CPyModule_typing;
extern CPyModule *CPyModule_eth_typing;
extern PyObject *CPyStatic_ENS;
extern PyObject *CPyStatic_AUCTION_REGISTRAR;
extern PyObject *CPyStatic_DEED;
extern PyObject *CPyStatic_FIFS_REGISTRAR;
extern PyObject *CPyStatic_PUBLIC_RESOLVER_2;
extern PyObject *CPyStatic_PUBLIC_RESOLVER_2_EXTENDED;
extern PyObject *CPyStatic_REVERSE_RESOLVER;
extern PyObject *CPyStatic_REVERSE_REGISTRAR;
extern char CPyDef___top_level__(void);
#endif
