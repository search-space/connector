# -*- coding: utf-8 -*-
from flask import Response

from swagger_server.utilities.cadde_exception import CaddeException
from swagger_server.utilities.external_interface import ExternalInterface
from swagger_server.utilities.internal_interface import InternalInterface

__CONFIG_CKAN_URL_FILE_PATH = '/usr/src/app/swagger_server/configs/ckan.json'
__CONFIG_CKAN_URL = 'ckan_url'


def search_catalog_meta(
        q: str,
        internal_interface: InternalInterface,
        external_interface: ExternalInterface) -> Response:
    """
    横断検索要求を行い、横断検索サイトからカタログ情報を取得する

    Args:
        q str : 検索条件のクエリストリング
        internal_interface InternalInterface : コンフィグ情報取得処理を行うインタフェース
        external_interface ExternalInterface : GETリクエストを行うインタフェース

    Returns:
        Response : 取得した情報

    Raises:
        Cadde_excption : コンフィグファイルからCKANURLを取得できない場合、エラーコード : 00002E
        Cadde_excption : ステータスコード2xxでない場合 エラーコード : 16002E
    """
    try:
        config = internal_interface.config_read(__CONFIG_CKAN_URL_FILE_PATH)
        ckan_url = config[__CONFIG_CKAN_URL]
    except Exception:
        raise CaddeException(
            message_id='00002E',
            status_code=500,
            replace_str_list=[__CONFIG_CKAN_URL])

    response = external_interface.http_get(ckan_url + q)
    if response.status_code < 200 or 300 <= response.status_code:
        raise CaddeException(
            message_id='16002E',
            status_code=response.status_code,
            replace_str_list=[
                response.text])
    return response


def search_catalog_detail(
        q: str,
        provider_connector_url: str,
        authorization: str,
        external_interface: ExternalInterface) -> Response:
    """
    詳細検索要求を行い、提供者カタログサイトからカタログ情報を取得する

    Args:
        q str : 検索条件のクエリストリング:
        provider_connector_url str : 提供者コネクタのURL
        authorization str HTTPリクエストヘッダで使用する認証トークン
        external_interface ExternalInterface : GETリクエストを行うインタフェース

    Returns:
        str : 取得した情報

    Raises:
        Cadde_excption : ステータスコード2xxでない場合 エラーコード : 17002E
    """
    headers_dict = {'Authorization': authorization}

    response = external_interface.http_get(
        provider_connector_url + q, headers_dict)
    if response.status_code < 200 or 300 <= response.status_code:
        raise CaddeException(
            message_id='17002E',
            status_code=response.status_code,
            replace_str_list=[
                response.text])

    return response
