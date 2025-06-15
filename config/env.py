import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 인스타그램 로그인 정보
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# 환경변수 누락 시 경고를 주고 싶다면 아래 유틸을 사용하세요.
def require_env(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"[환경 변수 누락] {var_name} 값이 설정되지 않았습니다.")
    return value
