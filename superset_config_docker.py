SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
ENABLE_PROXY_FIX = True
# PUBLIC_ROLE_LIKE_GAMMA = True
PUBLIC_ROLE_LIKE = 'Gamma'
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True
}
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/superset'

CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*', 'http://localhost:8088', 'host.docker.internal:8088']
}
