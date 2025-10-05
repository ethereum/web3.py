#ifndef MYPYC_NATIVE_7997cc2706ea16582bbe_H
#define MYPYC_NATIVE_7997cc2706ea16582bbe_H
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
