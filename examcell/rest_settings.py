import datetime
REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'accounts.api.utils.custom_exception_handler',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
}
# OAUTH2_PROVIDER = {
#     # this is the list of available scopes
#     'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
# }
ASGI_APPLICATION = "honwautomation.routing.application"
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_USE_CUSTOM_EXCEPTION_HANDLER': True,
    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'accounts.api.jwt.utils.jwt_response_payload_handler',
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,
}
