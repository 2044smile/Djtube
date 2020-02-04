# Auth
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

#Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '2820024684762865'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b8dddc1b978f44520481da72c945fb59'

#Kakao
SOCIAL_AUTH_KAKAO_KEY = '891a168540fbb272a30fbb62111d1fa7'
SOCIAL_AUTH_KAKAO_SECRET = 'a58d2e0e40de68f01667f169308f6e5e'

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
