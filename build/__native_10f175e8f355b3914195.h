#ifndef MYPYC_NATIVE_10f175e8f355b3914195_H
#define MYPYC_NATIVE_10f175e8f355b3914195_H
#include <Python.h>
#include <CPy.h>
#ifndef MYPYC_DECLARED_tuple_T3OOO
#define MYPYC_DECLARED_tuple_T3OOO
typedef struct tuple_T3OOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3OOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OO
#define MYPYC_DECLARED_tuple_T2OO
typedef struct tuple_T2OO {
    PyObject *f0;
    PyObject *f1;
} tuple_T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2CO
#define MYPYC_DECLARED_tuple_T2CO
typedef struct tuple_T2CO {
    char f0;
    PyObject *f1;
} tuple_T2CO;
#endif

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

#ifndef MYPYC_DECLARED_tuple_T6OOOOOO
#define MYPYC_DECLARED_tuple_T6OOOOOO
typedef struct tuple_T6OOOOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
    PyObject *f4;
    PyObject *f5;
} tuple_T6OOOOOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T4OOOO
#define MYPYC_DECLARED_tuple_T4OOOO
typedef struct tuple_T4OOOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
    PyObject *f3;
} tuple_T4OOOO;
#endif

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_w3;
    PyObject *_ens;
    PyObject *__resolver_contract;
    PyObject *__reverse_resolver_contract;
} faster_ens___async_ens___AsyncENSObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__coin_type;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_temp__2;
    tuple_T3OOO ___mypyc_temp__3;
    PyObject *___mypyc_generator_attribute__r;
    PyObject *___mypyc_temp__4;
    tuple_T3OOO ___mypyc_temp__5;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__6;
    tuple_T3OOO ___mypyc_temp__7;
    PyObject *___mypyc_generator_attribute__address_as_bytes;
} faster_ens___async_ens___address_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__coin_type;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__8;
    tuple_T3OOO ___mypyc_temp__9;
    PyObject *___mypyc_generator_attribute__owner;
    PyObject *___mypyc_temp__10;
    tuple_T3OOO ___mypyc_temp__11;
    PyObject *___mypyc_temp__12;
    tuple_T3OOO ___mypyc_temp__13;
    PyObject *___mypyc_temp__14;
    tuple_T3OOO ___mypyc_temp__15;
    PyObject *___mypyc_generator_attribute__resolver;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__16;
    tuple_T3OOO ___mypyc_temp__17;
    PyObject *___mypyc_temp__18;
    tuple_T3OOO ___mypyc_temp__19;
} faster_ens___async_ens___setup_address_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__address;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__reversed_domain;
    PyObject *___mypyc_temp__20;
    tuple_T3OOO ___mypyc_temp__21;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_temp__22;
    tuple_T3OOO ___mypyc_temp__23;
    PyObject *___mypyc_temp__2_0;
} faster_ens___async_ens___name_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__24;
    tuple_T3OOO ___mypyc_temp__25;
    PyObject *___mypyc_temp__26;
    tuple_T3OOO ___mypyc_temp__27;
    PyObject *___mypyc_temp__28;
    tuple_T3OOO ___mypyc_temp__29;
    PyObject *___mypyc_generator_attribute__resolved;
    PyObject *___mypyc_temp__30;
    tuple_T3OOO ___mypyc_temp__31;
    PyObject *___mypyc_temp__32;
    tuple_T3OOO ___mypyc_temp__33;
    PyObject *___mypyc_temp__34;
    tuple_T3OOO ___mypyc_temp__35;
    PyObject *___mypyc_temp__36;
    tuple_T3OOO ___mypyc_temp__37;
} faster_ens___async_ens___setup_name_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__38;
    tuple_T3OOO ___mypyc_temp__39;
} faster_ens___async_ens___owner_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__new_owner;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__40;
    tuple_T3OOO ___mypyc_temp__41;
    PyObject *___mypyc_generator_attribute__super_owner;
    PyObject *___mypyc_generator_attribute__unowned;
    PyObject *___mypyc_generator_attribute__owned;
    PyObject *___mypyc_temp__42;
    tuple_T3OOO ___mypyc_temp__43;
    PyObject *___mypyc_generator_attribute__current_owner;
    PyObject *___mypyc_temp__44;
    tuple_T3OOO ___mypyc_temp__45;
    PyObject *___mypyc_temp__46;
    tuple_T3OOO ___mypyc_temp__47;
} faster_ens___async_ens___setup_owner_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__normal_name;
    PyObject *___mypyc_temp__48;
    tuple_T3OOO ___mypyc_temp__49;
    tuple_T2OO ___mypyc_generator_attribute__resolver;
} faster_ens___async_ens___resolver_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__target_address;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__reversed_domain;
    PyObject *___mypyc_temp__50;
    tuple_T3OOO ___mypyc_temp__51;
} faster_ens___async_ens___reverser_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__key;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__52;
    tuple_T3OOO ___mypyc_temp__53;
    PyObject *___mypyc_generator_attribute__r;
    PyObject *___mypyc_temp__54;
    tuple_T3OOO ___mypyc_temp__55;
    PyObject *___mypyc_temp__56;
    tuple_T3OOO ___mypyc_temp__57;
} faster_ens___async_ens___get_text_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__key;
    PyObject *___mypyc_generator_attribute__value;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__58;
    tuple_T3OOO ___mypyc_temp__59;
    PyObject *___mypyc_generator_attribute__r;
    PyObject *___mypyc_temp__60;
    tuple_T3OOO ___mypyc_temp__61;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__62;
    tuple_T3OOO ___mypyc_temp__63;
} faster_ens___async_ens___set_text_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__normal_name;
    PyObject *___mypyc_generator_attribute__fn_name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__current_name;
    PyObject *___mypyc_temp__64;
    tuple_T3OOO ___mypyc_temp__65;
    PyObject *___mypyc_generator_attribute__resolver_addr;
    PyObject *___mypyc_generator_attribute__resolver;
} faster_ens___async_ens____get_resolver_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__resolver_addr;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__66;
    tuple_T3OOO ___mypyc_temp__67;
    PyObject *___mypyc_generator_attribute__namehash;
    PyObject *___mypyc_temp__68;
    tuple_T3OOO ___mypyc_temp__69;
    PyObject *___mypyc_generator_attribute__coro;
    PyObject *___mypyc_temp__70;
    tuple_T3OOO ___mypyc_temp__71;
} faster_ens___async_ens____set_resolver_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__fn_name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__normal_name;
    PyObject *___mypyc_temp__72;
    tuple_T3OOO ___mypyc_temp__73;
    PyObject *___mypyc_generator_attribute__resolver;
    PyObject *___mypyc_generator_attribute__current_name;
    PyObject *___mypyc_generator_attribute__node;
    PyObject *___mypyc_temp__74;
    tuple_T3OOO ___mypyc_temp__75;
    tuple_T2OO ___mypyc_generator_attribute__contract_func_with_args;
    PyObject *___mypyc_generator_attribute__calldata;
    PyObject *___mypyc_temp__76;
    tuple_T3OOO ___mypyc_temp__77;
    PyObject *___mypyc_generator_attribute__contract_call_result;
    PyObject *___mypyc_generator_attribute__result;
    PyObject *___mypyc_generator_attribute__lookup_function;
    PyObject *___mypyc_temp__78;
    tuple_T3OOO ___mypyc_temp__79;
} faster_ens___async_ens____resolve_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__account;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__parent_owned;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__80;
    tuple_T3OOO ___mypyc_temp__81;
    PyObject *___mypyc_temp__2_0;
} faster_ens___async_ens____assert_control_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__owner;
    PyObject *___mypyc_generator_attribute__unowned;
    PyObject *___mypyc_generator_attribute__pieces;
    PyObject *___mypyc_temp__82;
    tuple_T3OOO ___mypyc_temp__83;
} faster_ens___async_ens____first_owner_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__owner;
    PyObject *___mypyc_generator_attribute__unowned;
    PyObject *___mypyc_generator_attribute__owned;
    PyObject *___mypyc_generator_attribute__old_owner;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__84;
    PyObject *___mypyc_temp__85;
    PyObject *___mypyc_generator_attribute__label;
    PyObject *___mypyc_generator_attribute__coro;
    PyObject *___mypyc_temp__86;
    tuple_T3OOO ___mypyc_temp__87;
} faster_ens___async_ens____claim_ownership_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__88;
    tuple_T3OOO ___mypyc_temp__89;
    PyObject *___mypyc_generator_attribute__reverse_registrar;
    PyObject *___mypyc_temp__90;
    tuple_T3OOO ___mypyc_temp__91;
} faster_ens___async_ens____setup_reverse_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__92;
    tuple_T3OOO ___mypyc_temp__93;
    PyObject *___mypyc_generator_attribute__addr;
} faster_ens___async_ens____reverse_registrar_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__name;
    PyObject *___mypyc_generator_attribute__func;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__transact;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__94;
    tuple_T3OOO ___mypyc_temp__95;
    PyObject *___mypyc_generator_attribute__owner;
    PyObject *___mypyc_generator_attribute__transact_from_owner;
    PyObject *___mypyc_temp__96;
    tuple_T3OOO ___mypyc_temp__97;
} faster_ens___async_ens____set_property_AsyncENS_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__resolver;
    PyObject *___mypyc_generator_attribute__interface_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__98;
    PyObject *___mypyc_temp__99;
    PyObject *___mypyc_generator_attribute__func;
    PyObject *___mypyc_temp__100;
    tuple_T3OOO ___mypyc_temp__101;
} faster_ens___async_ens____async_resolver_supports_interface_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__ens_name;
    PyObject *___mypyc_generator_attribute__resolver;
    PyObject *___mypyc_generator_attribute__ens_interface_id;
    PyObject *___mypyc_generator_attribute__interface_name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__102;
    tuple_T3OOO ___mypyc_temp__103;
} faster_ens___async_ens____async_validate_resolver_and_interface_id_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_w3;
    PyObject *_ens;
    PyObject *__resolver_contract;
    PyObject *__reverse_resolver_contract;
} faster_ens___base_ens___BaseENSObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_w3;
    PyObject *_ens;
    PyObject *__resolver_contract;
    PyObject *__reverse_resolver_contract;
} faster_ens___ens___ENSObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    char _is_async;
    PyObject *_base_url;
    double _request_timeout;
    PyObject *__request_session_manager;
} faster_web3___beacon___async_beacon___AsyncBeaconObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__params;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__uri;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
} faster_web3___beacon___async_beacon____async_make_get_request_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__body;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__uri;
    PyObject *___mypyc_temp__2;
    tuple_T3OOO ___mypyc_temp__3;
} faster_web3___beacon___async_beacon____async_make_post_request_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__4;
    tuple_T3OOO ___mypyc_temp__5;
} faster_web3___beacon___async_beacon___get_genesis_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__6;
    tuple_T3OOO ___mypyc_temp__7;
} faster_web3___beacon___async_beacon___get_hash_root_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__8;
    tuple_T3OOO ___mypyc_temp__9;
} faster_web3___beacon___async_beacon___get_fork_data_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__10;
    tuple_T3OOO ___mypyc_temp__11;
} faster_web3___beacon___async_beacon___get_finality_checkpoint_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__12;
    tuple_T3OOO ___mypyc_temp__13;
} faster_web3___beacon___async_beacon___get_validators_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__validator_id;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__14;
    tuple_T3OOO ___mypyc_temp__15;
} faster_web3___beacon___async_beacon___get_validator_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__16;
    tuple_T3OOO ___mypyc_temp__17;
} faster_web3___beacon___async_beacon___get_validator_balances_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__18;
    tuple_T3OOO ___mypyc_temp__19;
} faster_web3___beacon___async_beacon___get_epoch_committees_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__20;
    tuple_T3OOO ___mypyc_temp__21;
} faster_web3___beacon___async_beacon___get_epoch_sync_committees_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__22;
    tuple_T3OOO ___mypyc_temp__23;
} faster_web3___beacon___async_beacon___get_epoch_randao_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__24;
    tuple_T3OOO ___mypyc_temp__25;
} faster_web3___beacon___async_beacon___get_block_headers_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__26;
    tuple_T3OOO ___mypyc_temp__27;
} faster_web3___beacon___async_beacon___get_block_header_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__28;
    tuple_T3OOO ___mypyc_temp__29;
} faster_web3___beacon___async_beacon___get_block_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__30;
    tuple_T3OOO ___mypyc_temp__31;
} faster_web3___beacon___async_beacon___get_block_root_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__32;
    tuple_T3OOO ___mypyc_temp__33;
} faster_web3___beacon___async_beacon___get_block_attestations_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__34;
    tuple_T3OOO ___mypyc_temp__35;
} faster_web3___beacon___async_beacon___get_blinded_blocks_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__36;
    tuple_T3OOO ___mypyc_temp__37;
} faster_web3___beacon___async_beacon___get_rewards_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_root;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__38;
    tuple_T3OOO ___mypyc_temp__39;
} faster_web3___beacon___async_beacon___get_light_client_bootstrap_structure_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__40;
    tuple_T3OOO ___mypyc_temp__41;
} faster_web3___beacon___async_beacon___get_light_client_updates_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__42;
    tuple_T3OOO ___mypyc_temp__43;
} faster_web3___beacon___async_beacon___get_light_client_finality_update_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__44;
    tuple_T3OOO ___mypyc_temp__45;
} faster_web3___beacon___async_beacon___get_light_client_optimistic_update_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__46;
    tuple_T3OOO ___mypyc_temp__47;
} faster_web3___beacon___async_beacon___get_attestations_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__48;
    tuple_T3OOO ___mypyc_temp__49;
} faster_web3___beacon___async_beacon___get_attester_slashings_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__50;
    tuple_T3OOO ___mypyc_temp__51;
} faster_web3___beacon___async_beacon___get_proposer_slashings_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__52;
    tuple_T3OOO ___mypyc_temp__53;
} faster_web3___beacon___async_beacon___get_voluntary_exits_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__54;
    tuple_T3OOO ___mypyc_temp__55;
} faster_web3___beacon___async_beacon___get_bls_to_execution_changes_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__56;
    tuple_T3OOO ___mypyc_temp__57;
} faster_web3___beacon___async_beacon___get_fork_schedule_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__58;
    tuple_T3OOO ___mypyc_temp__59;
} faster_web3___beacon___async_beacon___get_spec_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__60;
    tuple_T3OOO ___mypyc_temp__61;
} faster_web3___beacon___async_beacon___get_deposit_contract_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__state_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__62;
    tuple_T3OOO ___mypyc_temp__63;
} faster_web3___beacon___async_beacon___get_beacon_state_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__64;
    tuple_T3OOO ___mypyc_temp__65;
} faster_web3___beacon___async_beacon___get_beacon_heads_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__66;
    tuple_T3OOO ___mypyc_temp__67;
} faster_web3___beacon___async_beacon___get_node_identity_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__68;
    tuple_T3OOO ___mypyc_temp__69;
} faster_web3___beacon___async_beacon___get_peers_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__peer_id;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__70;
    tuple_T3OOO ___mypyc_temp__71;
} faster_web3___beacon___async_beacon___get_peer_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__72;
    tuple_T3OOO ___mypyc_temp__73;
} faster_web3___beacon___async_beacon___get_peer_count_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__url;
    PyObject *___mypyc_temp__74;
    tuple_T3OOO ___mypyc_temp__75;
    PyObject *___mypyc_generator_attribute__response;
} faster_web3___beacon___async_beacon___get_health_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__76;
    tuple_T3OOO ___mypyc_temp__77;
} faster_web3___beacon___async_beacon___get_version_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__78;
    tuple_T3OOO ___mypyc_temp__79;
} faster_web3___beacon___async_beacon___get_syncing_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__block_id;
    PyObject *___mypyc_generator_attribute__indices;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__indices_param;
    PyObject *___mypyc_temp__80;
    tuple_T3OOO ___mypyc_temp__81;
} faster_web3___beacon___async_beacon___get_blob_sidecars_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__epoch;
    PyObject *___mypyc_generator_attribute__validator_indices;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__82;
    tuple_T3OOO ___mypyc_temp__83;
} faster_web3___beacon___async_beacon___get_attester_duties_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__epoch;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__84;
    tuple_T3OOO ___mypyc_temp__85;
} faster_web3___beacon___async_beacon___get_block_proposer_duties_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__epoch;
    PyObject *___mypyc_generator_attribute__validator_indices;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__86;
    tuple_T3OOO ___mypyc_temp__87;
} faster_web3___beacon___async_beacon___get_sync_committee_duties_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__epoch;
    PyObject *___mypyc_generator_attribute__validator_indices;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__88;
    tuple_T3OOO ___mypyc_temp__89;
} faster_web3___beacon___async_beacon___get_attestations_rewards_AsyncBeacon_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_base_url;
    double _request_timeout;
    PyObject *__request_session_manager;
} faster_web3___beacon___beacon___BeaconObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_method;
    PyObject *_params;
    tuple_T3OOO _response_formatters;
    PyObject *_subscription_id;
    PyObject *_middleware_response_processors;
} faster_web3____utils___caching___caching_utils___RequestInformationObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_func;
    PyObject *_wrapper;
} faster_web3____utils___caching___caching_utils___handle_request_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_handle_request_caching_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__current_threshold;
    char ___mypyc_generator_attribute__cache_allowed_requests;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__chain_id_result;
    CPyTagged ___mypyc_generator_attribute__chain_id;
    tuple_T3OOO ___mypyc_temp__2;
} faster_web3____utils___caching___caching_utils___async_set_threshold_if_empty_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__method;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *___mypyc_generator_attribute__response;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__result;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
    PyObject *___mypyc_generator_attribute__cache_validator;
    PyObject *___mypyc_temp__5;
    tuple_T3OOO ___mypyc_temp__6;
} faster_web3____utils___caching___caching_utils____async_should_cache_response_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_func;
    PyObject *_wrapper;
} faster_web3____utils___caching___caching_utils___async_handle_request_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__method;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *_type;
    PyObject *_value;
    PyObject *_traceback;
    PyObject *_arg;
    PyObject **_stop_iter_ptr;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__request_cache;
    PyObject *___mypyc_generator_attribute__cache_key;
    PyObject *___mypyc_generator_attribute__cache_result;
    PyObject *___mypyc_temp__7;
    tuple_T3OOO ___mypyc_temp__8;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__9;
    tuple_T3OOO ___mypyc_temp__10;
    PyObject *___mypyc_temp__11;
    PyObject *___mypyc_temp__12;
    char ___mypyc_temp__13;
    PyObject *___mypyc_temp__14;
    tuple_T3OOO ___mypyc_temp__15;
    tuple_T3OOO ___mypyc_temp__16;
    PyObject *___mypyc_temp__17;
    tuple_T3OOO ___mypyc_temp__18;
    PyObject *___mypyc_temp__19;
    tuple_T3OOO ___mypyc_temp__20;
    PyObject *___mypyc_temp__21;
    tuple_T3OOO ___mypyc_temp__22;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_request_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_request_caching_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_gen___3_363Object;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_func;
    PyObject *_wrapper;
} faster_web3____utils___caching___caching_utils___async_handle_send_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__method;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *_type;
    PyObject *_value;
    PyObject *_traceback;
    PyObject *_arg;
    PyObject **_stop_iter_ptr;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__request_cache;
    PyObject *___mypyc_generator_attribute__cache_key;
    PyObject *___mypyc_generator_attribute__cached_response;
    PyObject *___mypyc_temp__23;
    tuple_T3OOO ___mypyc_temp__24;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_send_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_send_caching_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_gen___3_396Object;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_func;
    PyObject *_wrapper;
} faster_web3____utils___caching___caching_utils___async_handle_recv_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__rpc_request;
    PyObject *_type;
    PyObject *_value;
    PyObject *_traceback;
    PyObject *_arg;
    PyObject **_stop_iter_ptr;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__method;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *___mypyc_generator_attribute__request_cache;
    PyObject *___mypyc_generator_attribute__cache_key;
    PyObject *___mypyc_generator_attribute__cache_result;
    PyObject *___mypyc_temp__25;
    tuple_T3OOO ___mypyc_temp__26;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__27;
    tuple_T3OOO ___mypyc_temp__28;
    PyObject *___mypyc_temp__29;
    PyObject *___mypyc_temp__30;
    char ___mypyc_temp__31;
    PyObject *___mypyc_temp__32;
    tuple_T3OOO ___mypyc_temp__33;
    tuple_T3OOO ___mypyc_temp__34;
    PyObject *___mypyc_temp__35;
    tuple_T3OOO ___mypyc_temp__36;
    PyObject *___mypyc_temp__37;
    tuple_T3OOO ___mypyc_temp__38;
    PyObject *___mypyc_temp__39;
    tuple_T3OOO ___mypyc_temp__40;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_recv_caching_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_async_handle_recv_caching_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_env__;
} faster_web3____utils___caching___caching_utils___wrapper_gen___3_422Object;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__blocknum;
    PyObject *___mypyc_generator_attribute__block_timestamp;
    int32_t ___mypyc_next_label__;
    char ___mypyc_generator_attribute__cache_allowed_requests;
    PyObject *___mypyc_generator_attribute__threshold;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__threshold_block;
    PyObject *___mypyc_temp__2;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
    PyObject *___mypyc_generator_attribute__block;
    tuple_T3OOO ___mypyc_temp__5;
    PyObject *___mypyc_generator_attribute__e;
} faster_web3____utils___caching___request_caching_validation___async_is_beyond_validation_threshold_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *___mypyc_generator_attribute___result;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__block_id;
    CPyTagged ___mypyc_generator_attribute__blocknum;
    PyObject *___mypyc_temp__6;
    tuple_T3OOO ___mypyc_temp__7;
} faster_web3____utils___caching___request_caching_validation___async_validate_from_block_id_in_params_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute___params;
    PyObject *___mypyc_generator_attribute__result;
    int32_t ___mypyc_next_label__;
    char ___mypyc_generator_attribute__cache_allowed_requests;
    PyObject *___mypyc_generator_attribute__blocknum;
    PyObject *___mypyc_temp__8;
    tuple_T3OOO ___mypyc_temp__9;
    PyObject *___mypyc_generator_attribute__block;
    PyObject *___mypyc_temp__10;
    tuple_T3OOO ___mypyc_temp__11;
    PyObject *___mypyc_temp__12;
    PyObject *___mypyc_temp__13;
    tuple_T3OOO ___mypyc_temp__14;
    tuple_T3OOO ___mypyc_temp__15;
    PyObject *___mypyc_generator_attribute__e;
} faster_web3____utils___caching___request_caching_validation___async_validate_from_blocknum_in_result_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__provider;
    PyObject *___mypyc_generator_attribute__params;
    PyObject *___mypyc_generator_attribute___result;
    int32_t ___mypyc_next_label__;
    char ___mypyc_generator_attribute__cache_allowed_requests;
    PyObject *___mypyc_temp__16;
    tuple_T3OOO ___mypyc_temp__17;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__18;
    tuple_T3OOO ___mypyc_temp__19;
    PyObject *___mypyc_temp__20;
    tuple_T3OOO ___mypyc_temp__21;
    PyObject *___mypyc_generator_attribute__e;
} faster_web3____utils___caching___request_caching_validation___async_validate_from_blockhash_in_params_genObject;

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
    PyObject *___mypyc_generator_attribute__w3;
    CPyTagged ___mypyc_generator_attribute__sample_size;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__latest;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__transaction;
    PyObject *___mypyc_generator_attribute__block;
    CPyTagged ___mypyc_temp__2;
    CPyTagged ___mypyc_temp__3;
    PyObject *___mypyc_generator_attribute___;
    PyObject *___mypyc_temp__4;
    PyObject *___mypyc_temp__5;
} faster_web3___gas_strategies___time_based____get_raw_miner_data_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t bitmap;
    PyObject *___mypyc_generator_attribute__raw_data;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__data_by_miner;
    PyObject *___mypyc_temp__6;
    PyObject *___mypyc_temp__7;
    PyObject *___mypyc_generator_attribute__miner;
    PyObject *___mypyc_generator_attribute__miner_data;
    PyObject *___mypyc_generator_attribute___;
    PyObject *___mypyc_generator_attribute__block_hashes;
    PyObject *___mypyc_generator_attribute__gas_prices;
    double ___mypyc_generator_attribute__price_percentile;
    tuple_T3OOO ___mypyc_temp__8;
} faster_web3___gas_strategies___time_based____aggregate_miner_data_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__miner_data;
    CPyTagged ___mypyc_generator_attribute__wait_blocks;
    CPyTagged ___mypyc_generator_attribute__sample_size;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__miner_data_by_price;
    CPyTagged ___mypyc_temp__9;
    CPyTagged ___mypyc_temp__10;
    CPyTagged ___mypyc_generator_attribute__idx;
    PyObject *___mypyc_generator_attribute__low_percentile_gas_price;
    PyObject *___mypyc_temp__11;
    int64_t ___mypyc_temp__12;
    int64_t ___mypyc_temp__13;
    PyObject *___mypyc_generator_attribute__m;
    PyObject *___mypyc_generator_attribute__num_blocks_accepting_price;
    PyObject *___mypyc_generator_attribute__inv_prob_per_block;
    PyObject *___mypyc_generator_attribute__probability_accepted;
} faster_web3___gas_strategies___time_based____compute_probabilities_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    CPyTagged _max_wait_seconds;
    CPyTagged _sample_size;
    CPyTagged _probability;
    char _weighted;
    PyObject *_time_based_gas_price_strategy;
} faster_web3___gas_strategies___time_based___construct_time_based_gas_price_strategy_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3___gas_strategies___time_based___time_based_gas_price_strategy_construct_time_based_gas_price_strategy_objObject;

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
