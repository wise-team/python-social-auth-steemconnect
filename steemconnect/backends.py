import json
from social_core.backends.oauth import BaseOAuth2


class SteemConnectOAuth2(BaseOAuth2):
    """SteemConnect v2 OAuth authentication backend"""

    name = 'steemconnect'

    BASE_URL = 'https://steemconnect.com'
    AUTHORIZATION_URL = BASE_URL + '/oauth2/authorize'
    ACCESS_TOKEN_URL = BASE_URL + '/oauth2/token'
    ACCESS_TOKEN_METHOD = 'GET'
    REVOKE_TOKEN_URL = BASE_URL + '/api/oauth2/token/revoke'
    ACCESS_TOKEN_METHOD = 'POST'
    USER_INFO_URL = BASE_URL + '/api/me'

    RESPONSE_TYPE = None
    REDIRECT_STATE = False
    STATE_PARAMETER = False

    ID_KEY = 'user'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires_in', 'expires'),
        ('scope', 'granted_scopes'),
        ('account', 'account'),
        ('username', 'username'),
        ('name', 'name'),
    ]

    @staticmethod
    def _get_headers(token):
        return {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': token
        }

    def get_user_details(self, response):
        """Return user details from GitHub account"""

        account = response['account']
        metadata = json.loads(account.get('json_metadata') or '{}')
        account['json_metadata'] = metadata

        return {
            'id': account['id'],
            'username': account['name'],
            'name': metadata.get("profile", {}).get('name', ''),
            'account': account,
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""

        return self.get_json(self.USER_INFO_URL, method="POST", headers=self._get_headers(access_token))

    def request_access_token(self, *args, **kwargs):
        return self.strategy.request_data()

    def revoke_token_headers(self, token, uid):
        params = super(SteemConnectOAuth2, self).revoke_token_headers(token, uid)
        params.update(self._get_headers(token))
        return params

    def process_revoke_token_response(self, response):
        success = super(SteemConnectOAuth2, self).process_revoke_token_response(response)
        return success and response.json() == {'success': True}
