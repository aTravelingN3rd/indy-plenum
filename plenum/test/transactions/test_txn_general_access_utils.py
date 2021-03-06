import pytest

from plenum.common.constants import NYM, NODE
from plenum.common.txn_util import get_type, set_type, get_payload_data, get_from, get_req_id, get_seq_no, get_txn_id, \
    get_txn_time, get_version
from plenum.common.util import SortedDict


@pytest.fixture()
def txn():
    return {
        "reqSignature": {
            "type": "ED25519",
            "values": [{
                "from": "6ouriXMZkLeHsuXrN1X1fd",
                "value": "2DaRm3nt6H5fJu2TP5vxqbaDCtABPYmUTSX4ocnY8fVGgyJMVNaeh2z6JZhcW1gbmGKJcZopZMKZJwADuXFFJobM"
            }]
        },
        "txn": {
            "data": {
                "type": NYM,
                "something": "nothing",
            },

            "metadata": {
                "from": "6ouriXMZkLeHsuXrN1X1fd",
                "reqId": 1513945121191691,
            },

            "protocolVersion": "2",
            "type": "1",
        },
        "txnMetadata": {
            "seqNo": 144,
            "txnId": "aaaaa",
            "txnTime": 1513945121,
        },
        "ver": "1"
    }


def test_get_type(txn):
    assert get_type(txn) == NYM


def test_set_type(txn):
    txn = set_type(txn, NODE)
    assert get_type(txn) == NODE


def test_get_payload_data(txn):
    expected_paylaod_data = SortedDict({
        "type": NYM,
        "something": "nothing",
    })
    assert SortedDict(get_payload_data(txn)) == expected_paylaod_data


def test_get_from(txn):
    assert get_from(txn) == "6ouriXMZkLeHsuXrN1X1fd"


def test_get_from_none(txn):
    txn["txn"]["metadata"].pop("from", None)
    assert get_from(txn) is None


def test_get_req_id(txn):
    assert get_req_id(txn) == 1513945121191691


def test_get_req_id_none(txn):
    txn["txn"]["metadata"].pop("reqId", None)
    assert get_req_id(txn) is None


def test_get_seq_no(txn):
    assert get_seq_no(txn) == 144


def test_get_seq_no_none(txn):
    txn["txnMetadata"].pop("seqNo", None)
    assert get_seq_no(txn) is None


def test_get_txn_time(txn):
    assert get_txn_time(txn) == 1513945121


def test_get_txn_time_none(txn):
    txn["txnMetadata"].pop("txnTime", None)
    assert get_txn_time(txn) is None


def test_get_txn_id(txn):
    assert get_txn_id(txn) == "aaaaa"


def test_get_txn_id_none(txn):
    txn["txnMetadata"].pop("txnId", None)
    assert get_txn_id(txn) is None


def test_get_txn_version(txn):
    assert get_version(txn) == "1"
