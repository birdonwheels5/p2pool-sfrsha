from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    
    saffroncoin=math.Object(
        PARENT=networks.nets['saffroncoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b877474757'.decode('hex'),
        PREFIX='7208c1a555221151'.decode('hex'),
        P2P_PORT=1717,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=1718,
        BOOTSTRAP_ADDRS='p2poolcoin.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-sfr',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None,
    ),
   

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
