from typing import Any, Dict, Optional

from freqtrade.rpc.rpc import RPC, RPCException

from .webserver import ApiServer


def get_rpc_optional() -> Optional[RPC]:
    return ApiServer._rpc if ApiServer._has_rpc else None


def get_rpc() -> Optional[RPC]:
    if _rpc := get_rpc_optional():
        return _rpc
    else:
        raise RPCException('Bot is not in the correct state')


def get_config() -> Dict[str, Any]:
    return ApiServer._config


def get_api_config() -> Dict[str, Any]:
    return ApiServer._config['api_server']
