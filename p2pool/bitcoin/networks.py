import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
   
    saffroncoin=math.Object(
        P2P_PREFIX='cf0567ea'.decode('hex'),
        P2P_PORT=19717,
        ADDRESS_VERSION=63,
        RPC_PORT=19710,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'saffroncoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: __import__('saffroncoin_subsidy').GetBlockBaseValue(height),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s
        SYMBOL='SFR',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'saffroncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/saffroncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.saffroncoin'), 'saffroncoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://188.226.165.184/saffron/block_crawler.php?block_hash=',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='http://188.226.165.184/saffron/block_crawler.php?transaction=1',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
   


)
for net_name, net in nets.iteritems():
    net.NAME = net_name
