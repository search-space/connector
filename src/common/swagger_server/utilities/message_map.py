﻿# -*- coding: utf-8 -*-

__MESSAGE_CODE_MAP = {
    '00001E': {'message': 'パラメータが不正です。リクエストパラメータの値を確認してください。', 'http_status_code': 400},
    '00002E': {'message': 'コンフィグファイルに{0[0]}が設定されていません。サイト管理者に問い合わせてください。', 'http_status_code': 500},
    '01001N': {'message': 'リソースURL:{0[0]}, ヘッダ情報:{0[1]}'},
    '01002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}', 'http_status_code': 500},
    '01003E': {'message': 'ファイルが見つかりませんでした。サイト管理者に問い合わせてください。', 'http_status_code': 404},
    '01004E': {'message': 'HTTP接続時のベーシック認証に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 403},
    '01005E': {'message': 'リソースURLからドメインの取得に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 400},
    '01006E': {'message': 'タイムアウトが発生しました。サイト管理者に問い合わせてください。', 'http_status_code': 408},
    '02001N': {'message': 'リソースURL:{0[0]}'},
    '02002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}', 'http_status_code': 500},
    '02003E': {'message': 'FTP接続の認証に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 403},
    '02004E': {'message': 'ファイルが見つかりませんでした。サイト管理者に問い合わせてください。', 'http_status_code': 404},
    '02005E': {'message': 'タイムアウトが発生しました。サイト管理者に問い合わせてください。', 'http_status_code': 408},
    '02006E': {'message': 'リソースURLからドメインの取得に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 400},
    '03001N': {'message': 'クエリストリング:{0[0]}, 認証トークン:{0[1]}'},
    '03003E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '04001N': {'message': 'リソースURL:{0[0]}, リソース提供手段識別子:{0[1]}, 認証トークン:{0[2]}, データ提供IFが使用するカスタムヘッダー:{0[3]}'},
    '04002E': {'message': 'リソース提供手段識別子の値が不正です。リクエストパラメータの値を確認してください。', 'http_status_code': 400},
    '04009E': {'message': 'データ提供IFが使用するカスタムヘッダーの変換に失敗しました。データ提供IFが使用するカスタムヘッダーを確認してください。', 'http_status_code': 400},
    '04010E': {'message': 'リソースURLに紐づくCKAN情報が取得できませんでした。サイト管理者に問い合わせてください。', 'http_status_code': 500},
    '04013E': {'message': '対象のリソースURLに紐づくCKAN情報で交換実績記録用リソースIDに登録されている値が混在しています。サイト管理者に問い合わせてください。', 'http_status_code': 500},
    '04014E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '04015E': {'message': '認証認可処理を行いましたが、対象のトークンは取得できません。サイト管理者に問い合わせてください。', 'http_status_code': 401},
    '04016E': {'message': '認証認可処理を行いましたが、対象のトークンは使用できないか、リソースURLが認可されていません。サイト管理者に問い合わせてください。', 'http_status_code': 401},
    '04017E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '04018E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '04019E': {'message': 'リソース情報を取得しましたが、リソース情報が設定されていません。サイト管理者に問い合わせてください。', 'http_status_code': 500},
    '04021E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '04022E': {'message': '送信履歴登録に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 500},
    '04023E': {'message': '認可を要するデータ要求に失敗しました。サイト管理者に問い合わせてください。', 'http_status_code': 403},
    '05001N': {'message': 'クエリストリング:{0[0]}, 認証トークン:{0[1]}'},
    '05002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '06001N': {'message': 'リソースURL:{0[0]}, リソース提供種別識別子:{0[1]}, 認証トークン:{0[2]}, データ提供IFが使用するカスタムヘッダー:{0[3]}'},
    '06002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}', 'http_status_code': 500},
    '07001N': {'message': 'クエリストリング:{0[0]},CKAN URL:{0[1]}'},
    '07002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '08001N': {'message': 'リソースURL: {0[0]}'},
    '08002E': {'message': '認証情報が不正です。NGSIコンフィグを確認してください。', 'http_status_code': 401},
    '08003E': {'message': '指定したリソースが見つかりませんでした。', 'http_status_code': 404},
    '08004E': {'message': '指定したリソースに対応するデータが複数存在します。', 'http_status_code': 409},
    '08005E': {'message': 'エラーが発生しました。エラー内容:{0[0]}', 'http_status_code': 500},
    '09001N': {'message': '提供者ID: {0[0]}, 利用者ID:{0[1]}, 交換実績記録用リソースID:{0[2]}'},
    '09002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '09004N': {'message': '提供者ID: {0[0]}, 利用者ID:{0[1]}, 取引ID:{0[2]}, ハッシュ値:{0[3]}, 契約管理サービスURL:{0[4]}, 契約管理サービスキー:{0[5]}'},
    '09005E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A001N': {'message': 'トークン情報: {0[0]}, 提供者コネクタID:{0[1]}, 提供者コネクタのシークレット:{0[2]}'},
    '0A002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A003E': {'message': '認証処理を行いましたが、対象のトークンは使用できません。サイト管理者に問い合わせてください。', 'http_status_code': 401},
    '0A004N': {'message': 'トークン情報: {0[0]}, 提供者コネクタID:{0[1]}, 提供者コネクタのシークレット:{0[2]}'},
    '0A005E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A006N': {'message': '提供者コネクタID:{0[0]}, 提供者コネクタのシークレット:{0[1]}'},
    '0A007E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A008N': {'message': 'トークン情報:{0[0]}, リソースURL:{0[1]}'},
    '0A009E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A010N': {'message': 'トークン情報: {0[0]}, リソースID:{0[1]}, 提供者コネクタID:{0[2]}'},
    '0A011E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A012E': {'message': '認可確認に失敗しました。対象のトークンが使用できないか、リソースURLに認可がありません。サイト管理者に問い合わせてください。', 'http_status_code': 403},
    '0A013N': {'message': 'トークン情報: {0[0]}, リソースID:{0[1]}'},
    '0A014E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '0A015E': {'message': '対象のリソース情報に付加情報がありません。サイト管理者に問い合わせてください。', 'http_status_code': 403},
    '0A016E': {'message': '対象のリソースに対する認可情報が設定されていません。サイト管理者に問い合わせてください。', 'http_status_code': 404},
    '12001N': {'message': 'クエリストリング:{0[0]}, 提供者ID:{0[1]}, 利用者トークン:{0[2]}, 検索種別:{0[3]}'},
    '12002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '12004E': {'message': '検索種別の値が不正です。サイト管理者に問い合わせてください。', 'http_status_code': 400},
    '14001N': {'message': 'リソースURL: {0[0]}, リソース提供手段識別子:{0[1]}, 提供者ID:{0[2]},契約確認要否:{0[3]},利用者トークン:{0[4]}'},
    '14002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '14003E': {'message': 'リソース提供手段識別子の値が不正です。サイト管理者に問い合わせてください。', 'http_status_code': 400},
    '14004E': {'message': 'コネクタロケーションから、提供者コネクタURLと契約管理サービスURLが取得できませんでした。利用者側コネクタメインコンテナのコネクタロケーションを確認してください。', 'http_status_code': 500},
    '14005E': {'message': 'データ提供IFが使用するカスタムヘッダーの変換に失敗しました。データ提供IFが使用するカスタムヘッダーを確認してください。', 'http_status_code': 400},
    '14008E': {'message': '有効な利用者トークンが設定されておりません。有効な利用者トークンを設定してください。', 'http_status_code': 500},
    '15001N': {'message': 'リソースURL: {0[0]}, リソース提供手段識別子:{0[1]}, 提供者コネクタURL:{0[2]},認証トークン:{0[3]},データ提供IFが使用するカスタムヘッダー:{0[4]}'},
    '15002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '16001N': {'message': 'クエリストリング: {0[0]}, 検索種別:{0[1]}'},
    '16002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '17001N': {'message': 'クエリストリング: {0[0]}, 提供者コネクタURL:{0[1]}, 認証トークン:{0[2]},検索種別:{0[3]}'},
    '17002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '18001N': {'message': 'リソースURL: {0[0]}, リソース提供手段識別子:{0[1]}, 提供者ID:{0[2]}, IdP URL:{0[3]}, 利用者トークン:{0[4]}'},
    '18002E': {'message': 'リソース提供手段識別子の値が不正です。リクエストパラメータの値を確認してください。', 'http_status_code': 400},
    '19001N': {'message': '提供者ID: {0[0]}, 利用者ID:{0[1]}, 交換実績記録用リソースID:{0[2]}'},
    '19002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1A001N': {'message': 'トークン情報: {0[0]}, 利用者コネクタID:{0[1]}, 利用者コネクタのシークレット:{0[2]}'},
    '1A002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1A003E': {'message': '認証処理を行いましたが、対象の認証トークンは使用できません。リクエストパラメータに設定した利用者トークンを確認してください。', 'http_status_code': 401},
    '1A004N': {'message': '利用者トークン:{0[0]}, 利用者コネクタID: {0[1]}, 利用者コネクタのシークレット:{0[2]}, IdP:{0[3]}'},
    '1A005E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1A006E': {'message': '認証トークン取得処理を行いましたが、対象の利用者トークンは使用できません。リクエストパラメータに設定した利用者トークンを確認してください。', 'http_status_code': 401},
    '1B001N': {'message': '交換実績記録用リソースID: {0[0]}, 履歴取得方向:{0[1]}, 検索深度:{0[2]}'},
    '1B002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1B003E': {'message': '来歴管理I/Fからのレスポンスを正常に取得できませんでした', 'http_status_code': 500},
    '1B004E': {'message': '履歴取得方向(direction)の値が不正です。履歴取得方向の値を確認してください。', 'http_status_code': 400},
    '1B005E': {'message': '検索深度(depth)の値が不正です。検索深度の値を確認してください。', 'http_status_code': 400},
    '1C001N': {'message': '履歴ID検索用文字列:{0[0]}'},
    '1C002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1C003E': {'message': '来歴管理I/Fからのレスポンスを正常に取得できませんでした', 'http_status_code': 500},
    '1D001N': {'message': '交換実績記録用リソースID: {0[0]}, 履歴取得方向:{0[1]}, 検索深度:{0[2]}'},
    '1D002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1D003E': {'message': '来歴管理I/Fからのレスポンスを正常に取得できませんでした', 'http_status_code': 500},
    '1D004E': {'message': '履歴取得方向(direction)の値が不正です。履歴取得方向の値を確認してください。', 'http_status_code': 400},
    '1D005E': {'message': '検索深度(depth)の値が不正です。検索深度の値を確認してください。', 'http_status_code': 400},
    '1E001N': {'message': '履歴ID検索用文字列:{0[0]}'},
    '1E002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
    '1E003E': {'message': '来歴管理I/Fからのレスポンスを正常に取得できませんでした', 'http_status_code': 500},
    '1F001N': {'message': '提供者ID: {0[0]}, 利用者ID:{0[1]}, 取引ID:{0[2]}, ハッシュ値:{0[3]}, 契約管理サービスURL:{0[4]}, 契約管理サービスキー:{0[5]}'},
    '1F002E': {'message': 'エラーが発生しました。エラー内容:{0[0]}'},
}


def get_message_and_status_code(
        message_id: str,
        replace_str: list = None) -> dict:
    """
    メッセージコードを基にメッセージとHTTPステータスコードを取得する。
    置き換え文字列リストが設定されている場合は、メッセージの置き換え個所を置換える
    Args:
        message_id str : メッセージID
        replace_str list : 置き換え文字列リスト 設定しない場合はNoneを指定

    Returns:
        dict : メッセージとHTTPステータスコード HTTPステータスコードはエラーメッセージでない場合は未設定
               {'message':メッセージ, 'http_status_code':HTTPステータスコード}
    """
    result = __MESSAGE_CODE_MAP[message_id].copy()

    if replace_str is not None:
        result['message'] = result['message'].format(replace_str)
    return result


def get_message(message_id: str, replace_str: list = None) -> str:
    """
    get_message_and_status_codeを呼び出し、メッセージのみを文字列で返す。
    Args:
        message_id str : メッセージID
        replace_str list : 置き換え文字列リスト 設定しない場合はNoneを指定

    Returns:
        str : メッセージ
    """

    return get_message_and_status_code(message_id, replace_str)['message']
