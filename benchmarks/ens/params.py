# Shared parameter sets for ENS/faster_ens benchmarks

NAMES = [
    "alice.eth",
    "bob.eth",
    "emoji👨🏻.eth",
    "subdomain.alice.eth",
    "a" * 63 + ".eth",
    "",
]

LABELS = [
    "alice",
    "bob",
    "emoji👨🏻",
    "xn--fiqs8s",
    "a" * 63,
    "",
]

ADDRESSES = [
    "0x0000000000000000000000000000000000000000",
    "0x314159265dD8dbb310642f98f50C066173C1259b",
    "0x1111111111111111111111111111111111111111",
]

LABEL_LISTS = [
    ["alice", "bob", "carol"],
    ["a", "b", "c", "d", "e"],
    [],
]

NAMES_VALIDITY = [
    "alice.eth",
    "bob.eth",
    "emoji👨🏻.eth",
    "subdomain.alice.eth",
    "a" * 63 + ".eth",
    "",
    "a..eth",
    "a.eth.",
    "a.eth..",
]

PARENT_NAMES = [
    "foo.bar.eth",
    "bar.eth",
    "eth",
    "",
    "sub.sub2.foo.bar.eth",
]
