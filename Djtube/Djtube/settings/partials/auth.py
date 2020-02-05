from . import secret
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/login/'

SIGNUP_SUCCESS_MESSAGE = '성공적으로 회원가입 완료'
LOGIN_SUCCESS_MESSAGE = '성공적으로 로그인 완료'
LOGOUT_SUCCESS_MESSAGE = '성공적으로 로그아웃 완료'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.kakao.KakaoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = secret.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = secret.SOCIAL_AUTH_FACEBOOK_SECRET
SOCIAL_AUTH_KAKAO_KEY = secret.SOCIAL_AUTH_KAKAO_KEY
SOCIAL_AUTH_KAKAO_SECRET = secret.SOCIAL_AUTH_KAKAO_SECRET

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)
