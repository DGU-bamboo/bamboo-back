# 기반 이미지 설정 (예: Python 3.9 사용)
FROM python:3.9

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 필요한 파일 복사 (requirements.txt, Django 프로젝트 디렉토리 전체)
COPY requirements.txt .
COPY . .

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn 실행 명령어 설정
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
