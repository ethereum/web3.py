from web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)

import_raw_key = Method(
    "personal_importRawKey",
    mungers=[default_root_munger],
)


new_account = Method(
    "personal_newAccount",
    mungers=[default_root_munger],
)


list_accounts = Method(
    "personal_listAccounts",
    mungers=None,
)


send_transaction = Method(
    "personal_sendTransaction",
    mungers=[default_root_munger],
)


lock_account = Method(
    "personal_lockAccount",
    mungers=[default_root_munger],
)


unlock_account = Method(
    "personal_unlockAccount",
    mungers=[default_root_munger],
)


sign = Method(
    "personal_sign",
    mungers=[default_root_munger],
)


sign_typed_data = Method(
    "personal_signTypedData",
    mungers=[default_root_munger],
)


ec_recover = Method(
    "personal_ecRecover",
    mungers=[default_root_munger],
)


#
# Deprecated Methods
#
importRawKey = DeprecatedMethod(import_raw_key, 'importRawKey', 'import_raw_key')
newAccount = DeprecatedMethod(new_account, 'newAccount', 'new_account')
listAccounts = DeprecatedMethod(list_accounts, 'listAccounts', 'list_accounts')
sendTransaction = DeprecatedMethod(send_transaction, 'sendTransaction', 'send_transaction')
lockAccount = DeprecatedMethod(lock_account, 'lockAccount', 'lock_account')
unlockAccount = DeprecatedMethod(unlock_account, 'unlockAccount', 'unlock_account')
signTypedData = DeprecatedMethod(sign_typed_data, 'signTypedData', 'sign_typed_data')
ecRecover = DeprecatedMethod(ec_recover, 'ecRecover', 'ec_recover')