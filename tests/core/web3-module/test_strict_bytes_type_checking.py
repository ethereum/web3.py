from ens import (
    ENS,
)


def test_strict_bytes_type_checking_turns_on_and_off(w3):
    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert w3.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = True
    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")


def test_ens_module_uses_strict_byte_type_check_from_web3_instance_reference(w3):
    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")
    assert w3.ens.w3.strict_bytes_type_checking
    assert not w3.ens.w3.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert not w3.ens.w3.strict_bytes_type_checking
    assert w3.is_encodable("bytes2", b"\x01")
    assert w3.ens.w3.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = True
    assert w3.strict_bytes_type_checking
    assert w3.ens.w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")
    assert not w3.ens.w3.is_encodable("bytes2", b"\x01")


def test_ens_from_web3_inherits_w3_codec_and_strict_byte_type_checking(w3):
    ns = ENS.from_web3(w3)

    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")

    assert ns.w3.strict_bytes_type_checking
    assert not ns.w3.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert w3.is_encodable("bytes2", b"\x01")

    another_ns = ENS.from_web3(w3)
    assert not another_ns.w3.strict_bytes_type_checking
    assert another_ns.w3.is_encodable("bytes2", b"\x01")


def test_modules_use_codec_and_strict_byte_type_check_from_web3_instance_reference(
    w3, module1, module2, module3
):
    assert w3.codec == w3.eth.codec
    assert w3.codec == w3.net.codec
    assert w3.codec == w3.geth.codec

    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")
    assert not w3.eth.codec.is_encodable("bytes2", b"\x01")
    assert not w3.net.codec.is_encodable("bytes2", b"\x01")
    assert not w3.geth.codec.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert w3.is_encodable("bytes2", b"\x01")
    assert w3.eth.codec.is_encodable("bytes2", b"\x01")
    assert w3.net.codec.is_encodable("bytes2", b"\x01")
    assert w3.geth.codec.is_encodable("bytes2", b"\x01")

    # add modules after byte check swap

    w3.attach_modules(
        {
            "module1": module1,
            "module2": (
                module2,
                {
                    "submodule1": (module3,),
                },
            ),
        }
    )

    assert w3.codec == w3.module1.codec
    assert w3.codec == w3.module2.codec
    assert w3.codec == w3.module2.submodule1.codec

    assert w3.module1.codec.is_encodable("bytes2", b"\x01")
    assert w3.module2.codec.is_encodable("bytes2", b"\x01")
    assert w3.module2.submodule1.codec.is_encodable("bytes2", b"\x01")

    w3.strict_bytes_type_checking = True
    assert w3.strict_bytes_type_checking
    assert not w3.is_encodable("bytes2", b"\x01")
    assert not w3.eth.codec.is_encodable("bytes2", b"\x01")
    assert not w3.net.codec.is_encodable("bytes2", b"\x01")
    assert not w3.geth.codec.is_encodable("bytes2", b"\x01")
    assert not w3.module1.codec.is_encodable("bytes2", b"\x01")
    assert not w3.module2.codec.is_encodable("bytes2", b"\x01")
    assert not w3.module2.submodule1.codec.is_encodable("bytes2", b"\x01")
