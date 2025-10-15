#ifndef MYPYC_NATIVE_f8380e4197eb622eb831_H
#define MYPYC_NATIVE_f8380e4197eb622eb831_H
#include <Python.h>
#include <CPy.h>
#ifndef MYPYC_DECLARED_tuple_T4CIOO
#define MYPYC_DECLARED_tuple_T4CIOO
typedef struct tuple_T4CIOO {
    char f0;
    CPyTagged f1;
    PyObject *f2;
    PyObject *f3;
} tuple_T4CIOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OO
#define MYPYC_DECLARED_tuple_T2OO
typedef struct tuple_T2OO {
    PyObject *f0;
    PyObject *f1;
} tuple_T2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T3CIO
#define MYPYC_DECLARED_tuple_T3CIO
typedef struct tuple_T3CIO {
    char f0;
    CPyTagged f1;
    PyObject *f2;
} tuple_T3CIO;
#endif

#ifndef MYPYC_DECLARED_tuple_T3OOO
#define MYPYC_DECLARED_tuple_T3OOO
typedef struct tuple_T3OOO {
    PyObject *f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3OOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T1O
#define MYPYC_DECLARED_tuple_T1O
typedef struct tuple_T1O {
    PyObject *f0;
} tuple_T1O;
#endif

#ifndef MYPYC_DECLARED_tuple_T0
#define MYPYC_DECLARED_tuple_T0
typedef struct tuple_T0 {
    int empty_struct_error_flag;
} tuple_T0;
#endif

#ifndef MYPYC_DECLARED_tuple_T3IOO
#define MYPYC_DECLARED_tuple_T3IOO
typedef struct tuple_T3IOO {
    CPyTagged f0;
    PyObject *f1;
    PyObject *f2;
} tuple_T3IOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OI
#define MYPYC_DECLARED_tuple_T2OI
typedef struct tuple_T2OI {
    PyObject *f0;
    CPyTagged f1;
} tuple_T2OI;
#endif

#ifndef MYPYC_DECLARED_tuple_T2T2OOT2OO
#define MYPYC_DECLARED_tuple_T2T2OOT2OO
typedef struct tuple_T2T2OOT2OO {
    tuple_T2OO f0;
    tuple_T2OO f1;
} tuple_T2T2OOT2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T3T2OOT2OOT2OO
#define MYPYC_DECLARED_tuple_T3T2OOT2OOT2OO
typedef struct tuple_T3T2OOT2OOT2OO {
    tuple_T2OO f0;
    tuple_T2OO f1;
    tuple_T2OO f2;
} tuple_T3T2OOT2OOT2OO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2T2OOO
#define MYPYC_DECLARED_tuple_T2T2OOO
typedef struct tuple_T2T2OOO {
    tuple_T2OO f0;
    PyObject *f1;
} tuple_T2T2OOO;
#endif

#ifndef MYPYC_DECLARED_tuple_T2OT3OOO
#define MYPYC_DECLARED_tuple_T2OT3OOO
typedef struct tuple_T2OT3OOO {
    PyObject *f0;
    tuple_T3OOO f1;
} tuple_T2OT3OOO;
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

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *__original_text;
    PyObject *__original_codepoints;
    PyObject *__normalized_codepoints;
    char _restricted;
} faster_ens____normalization___TokenObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *__original_text;
    PyObject *__original_codepoints;
    PyObject *__normalized_codepoints;
    char _restricted;
} faster_ens____normalization___EmojiTokenObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *__original_text;
    PyObject *__original_codepoints;
    PyObject *__normalized_codepoints;
    char _restricted;
} faster_ens____normalization___TextTokenObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_type;
    PyObject *_tokens;
} faster_ens____normalization___LabelObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_labels;
} faster_ens____normalization___ENSNormalizedNameObject;

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
} faster_ens___exceptions___ENSValueErrorObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___AddressMismatchObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___UnauthorizedErrorObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___UnownedNameObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___ResolverNotFoundObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___UnsupportedFunctionObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___BidTooLowObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___InvalidBidHashObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___InvalidLabelObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___OversizeTransactionObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___UnderfundedBidObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_ens___exceptions___ENSValidationErrorObject;

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
    PyObject *___mypyc_generator_attribute__async_w3;
    PyObject *___mypyc_generator_attribute__block_identifier;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_temp__2;
    tuple_T3OOO ___mypyc_temp__3;
    PyObject *___mypyc_generator_attribute__requested_block;
} faster_web3____utils___contracts___async_parse_block_identifier_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__async_w3;
    CPyTagged ___mypyc_generator_attribute__block_identifier_int;
    int32_t ___mypyc_next_label__;
    CPyTagged ___mypyc_generator_attribute__block_num;
    PyObject *___mypyc_temp__4;
    tuple_T3OOO ___mypyc_temp__5;
    PyObject *___mypyc_generator_attribute__last_block;
    CPyTagged ___mypyc_generator_attribute__last_block_num;
} faster_web3____utils___contracts___async_parse_block_identifier_int_genObject;

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
    PyObject *___mypyc_self__;
    PyObject *_to_wrap;
    PyObject *_already_called;
    PyObject *_wrapped;
} faster_web3____utils___decorators___reject_recursive_repeats_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___decorators___wrapped_reject_recursive_repeats_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_replace_message;
    PyObject *_decorator;
} faster_web3____utils___decorators___deprecated_for_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *___mypyc_env__;
    PyObject *_to_wrap;
    PyObject *_wrapper;
    PyObject *_replace_message;
    PyObject *_decorator;
} faster_web3____utils___decorators___decorator_deprecated_for_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___decorators___decorator_deprecated_for_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___decorators___wrapper_deprecated_for_decorator_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_web3____utils___encoding___FriendlyJsonSerdeObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    char _is_dynamic;
} faster_web3____utils___encoding___DynamicArrayPackedEncoderObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
} faster_web3____utils___encoding___Web3JsonEncoderObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__mapping;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    CPyTagged ___mypyc_temp__1;
    int64_t ___mypyc_temp__2;
    PyObject *___mypyc_temp__3;
    PyObject *___mypyc_generator_attribute__key;
    PyObject *___mypyc_generator_attribute__val;
    tuple_T3OOO ___mypyc_temp__4;
    PyObject *___mypyc_generator_attribute__exc;
} faster_web3____utils___encoding____json_mapping_errors_FriendlyJsonSerde_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__iterable;
    int32_t ___mypyc_next_label__;
    CPyTagged ___mypyc_temp__5;
    CPyTagged ___mypyc_generator_attribute__index;
    PyObject *___mypyc_temp__6;
    PyObject *___mypyc_temp__7;
    PyObject *___mypyc_generator_attribute__element;
    tuple_T3OOO ___mypyc_temp__8;
    PyObject *___mypyc_generator_attribute__exc;
} faster_web3____utils___encoding____json_list_errors_FriendlyJsonSerde_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__async_eth;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__fee_history;
} faster_web3____utils___fee_utils___async_fee_history_priority_fee_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_func;
    PyObject *_recurse;
    PyObject *_data;
} faster_web3____utils___formatters___recursive_map_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___formatters___recurse_recursive_map_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_value;
    PyObject *_inner;
} faster_web3____utils___formatters___static_return_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___formatters___inner_static_return_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_result;
    PyObject *_inner;
    PyObject *_value;
} faster_web3____utils___formatters___static_result_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___formatters___inner_static_result_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_key_mappings;
    PyObject *_get_key;
    PyObject *_apply_key_map_curried;
} faster_web3____utils___formatters___apply_key_map_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___formatters___get_key_apply_key_map_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___formatters___apply_key_map_curried_apply_key_map_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *_logger;
    PyObject *__lock;
    PyObject *_session_cache;
    PyObject *_session_pool;
} faster_web3____utils___http_session_manager___HTTPSessionManagerObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__session;
    PyObject *___mypyc_generator_attribute__request_timeout;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__cache_key;
    PyObject *___mypyc_generator_attribute__evicted_items;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    char ___mypyc_temp__2;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
    PyObject *___mypyc_generator_attribute__cached_session;
    PyObject *___mypyc_generator_attribute__session_is_closed;
    PyObject *___mypyc_generator_attribute__session_loop_is_closed;
    PyObject *___mypyc_generator_attribute__warning;
    PyObject *___mypyc_temp__5;
    tuple_T3OOO ___mypyc_temp__6;
    PyObject *___mypyc_generator_attribute___session;
    tuple_T3OOO ___mypyc_temp__7;
    PyObject *___mypyc_temp__8;
    tuple_T3OOO ___mypyc_temp__9;
    PyObject *___mypyc_temp__10;
    tuple_T3OOO ___mypyc_temp__11;
    PyObject *___mypyc_generator_attribute__evicted_sessions;
    PyObject *___mypyc_temp__12;
    int64_t ___mypyc_temp__13;
    PyObject *___mypyc_generator_attribute__evicted_session;
} faster_web3____utils___http_session_manager___async_cache_and_return_session_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__14;
    tuple_T3OOO ___mypyc_temp__15;
    PyObject *___mypyc_generator_attribute__session;
    PyObject *___mypyc_temp__16;
    tuple_T3OOO ___mypyc_temp__17;
} faster_web3____utils___http_session_manager___async_get_response_from_get_request_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__18;
    tuple_T3OOO ___mypyc_temp__19;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__20;
    tuple_T3OOO ___mypyc_temp__21;
} faster_web3____utils___http_session_manager___async_json_make_get_request_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__22;
    tuple_T3OOO ___mypyc_temp__23;
    PyObject *___mypyc_generator_attribute__session;
    PyObject *___mypyc_temp__24;
    tuple_T3OOO ___mypyc_temp__25;
} faster_web3____utils___http_session_manager___async_get_response_from_post_request_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__26;
    tuple_T3OOO ___mypyc_temp__27;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__28;
    tuple_T3OOO ___mypyc_temp__29;
} faster_web3____utils___http_session_manager___async_json_make_post_request_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__self;
    PyObject *___mypyc_generator_attribute__endpoint_uri;
    PyObject *___mypyc_generator_attribute__data;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__30;
    tuple_T3OOO ___mypyc_temp__31;
    PyObject *___mypyc_generator_attribute__response;
    PyObject *___mypyc_temp__32;
    tuple_T3OOO ___mypyc_temp__33;
} faster_web3____utils___http_session_manager___async_make_post_request_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    uint32_t bitmap;
    PyObject *___mypyc_generator_attribute__self;
    double ___mypyc_generator_attribute__timeout;
    PyObject *___mypyc_generator_attribute__evicted_sessions;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__34;
    tuple_T3OOO ___mypyc_temp__35;
    PyObject *___mypyc_temp__36;
    int64_t ___mypyc_temp__37;
    PyObject *___mypyc_generator_attribute__evicted_session;
    PyObject *___mypyc_temp__38;
    tuple_T3OOO ___mypyc_temp__39;
    PyObject *___mypyc_temp__40;
    int64_t ___mypyc_temp__41;
} faster_web3____utils___http_session_manager____async_close_evicted_sessions_HTTPSessionManager_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__0_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__1_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__2_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__3_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__4_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__5_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
} faster_web3____utils___method_formatters_____mypyc_lambda__6_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__formatter_maps;
    PyObject *___mypyc_generator_attribute__method_name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__0;
    PyObject *___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__formatter_map;
} faster_web3____utils___method_formatters___combine_formatters_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__formatters;
    PyObject *___mypyc_generator_attribute__module;
    PyObject *___mypyc_generator_attribute__method_name;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_temp__2;
    PyObject *___mypyc_temp__3;
    PyObject *___mypyc_generator_attribute__f;
} faster_web3____utils___method_formatters___apply_module_to_formatters_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_duplicates;
    PyObject *_dup_sel;
} faster_web3____utils___validation____prepare_selector_collision_msg_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___validation_____mypyc_lambda__0__prepare_selector_collision_msg_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_abi;
    PyObject *_e;
    PyObject *_functions;
    PyObject *_selectors;
} faster_web3____utils___validation___validate_abi_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___validation_____mypyc_lambda__1_validate_abi_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_self__;
    PyObject *_args;
    PyObject *_kwargs;
    PyObject *_vals;
} faster_web3____utils___validation___has_one_val_envObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    vectorcallfunc vectorcall;
    PyObject *___mypyc_env__;
} faster_web3____utils___validation_____mypyc_lambda__2_has_one_val_objObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__async_w3;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__normalizers;
    PyObject *___mypyc_generator_attribute__abi_element_identifier;
    PyObject *___mypyc_generator_attribute__transaction;
    PyObject *___mypyc_generator_attribute__block_id;
    PyObject *___mypyc_generator_attribute__contract_abi;
    PyObject *___mypyc_generator_attribute__fn_abi;
    PyObject *___mypyc_generator_attribute__state_override;
    PyObject *___mypyc_generator_attribute__ccip_read_enabled;
    PyObject *___mypyc_generator_attribute__decode_tuples;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__call_transaction;
    PyObject *___mypyc_temp__0;
    tuple_T3OOO ___mypyc_temp__1;
    PyObject *___mypyc_generator_attribute__return_data;
    PyObject *___mypyc_generator_attribute__output_types;
    PyObject *___mypyc_generator_attribute__contract_call_return_data_formatter;
    PyObject *___mypyc_generator_attribute__request_information;
    PyObject *___mypyc_generator_attribute__method_and_params;
    PyObject *___mypyc_generator_attribute__current_response_formatters;
    PyObject *___mypyc_generator_attribute__current_result_formatters;
    PyObject *___mypyc_generator_attribute__updated_result_formatters;
    tuple_T3OOO ___mypyc_generator_attribute__response_formatters;
    PyObject *___mypyc_generator_attribute__output_data;
    tuple_T3OOO ___mypyc_temp__2;
    PyObject *___mypyc_generator_attribute__e;
    PyObject *___mypyc_temp__3;
    tuple_T3OOO ___mypyc_temp__4;
    char ___mypyc_generator_attribute__is_missing_code_error;
    PyObject *___mypyc_generator_attribute__msg;
    PyObject *___mypyc_generator_attribute___normalizers;
    PyObject *___mypyc_generator_attribute__normalized_data;
    PyObject *___mypyc_generator_attribute__decoded;
} faster_web3___contract___utils___async_call_contract_function_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__async_w3;
    PyObject *___mypyc_generator_attribute__abi_element_identifier;
    PyObject *___mypyc_generator_attribute__transaction;
    PyObject *___mypyc_generator_attribute__contract_abi;
    PyObject *___mypyc_generator_attribute__fn_abi;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__transact_transaction;
    PyObject *___mypyc_temp__5;
    tuple_T3OOO ___mypyc_temp__6;
    PyObject *___mypyc_generator_attribute__txn_hash;
} faster_web3___contract___utils___async_transact_with_contract_function_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__async_w3;
    PyObject *___mypyc_generator_attribute__abi_element_identifier;
    PyObject *___mypyc_generator_attribute__transaction;
    PyObject *___mypyc_generator_attribute__contract_abi;
    PyObject *___mypyc_generator_attribute__fn_abi;
    PyObject *___mypyc_generator_attribute__block_identifier;
    PyObject *___mypyc_generator_attribute__state_override;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__estimate_transaction;
    PyObject *___mypyc_temp__7;
    tuple_T3OOO ___mypyc_temp__8;
} faster_web3___contract___utils___async_estimate_gas_for_function_genObject;

typedef struct {
    PyObject_HEAD
    CPyVTableItem *vtable;
    PyObject *___mypyc_generator_attribute__address;
    PyObject *___mypyc_generator_attribute__async_w3;
    PyObject *___mypyc_generator_attribute__abi_element_identifier;
    PyObject *___mypyc_generator_attribute__transaction;
    PyObject *___mypyc_generator_attribute__contract_abi;
    PyObject *___mypyc_generator_attribute__fn_abi;
    PyObject *___mypyc_generator_attribute__args;
    PyObject *___mypyc_generator_attribute__kwargs;
    int32_t ___mypyc_next_label__;
    PyObject *___mypyc_generator_attribute__prepared_transaction;
    PyObject *___mypyc_temp__9;
    tuple_T3OOO ___mypyc_temp__10;
} faster_web3___contract___utils___async_build_transaction_for_function_genObject;

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
