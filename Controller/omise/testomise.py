import websockets
import asyncio
import omise
omise.api_secret = 'skey_test_5ql7g9afar2i5l7svzw'


oc=omise.Charge.retrieve()

print(oc)