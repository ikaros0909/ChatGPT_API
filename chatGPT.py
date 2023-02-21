import openai
import os
import configparser

# 설정 파일을 읽어들입니다.
config = configparser.ConfigParser()
config.read('config.ini')

# 인증 정보 설정
openai.api_key = config.get('openai', 'api_key')

# API 연결 테스트
model_engine = "text-davinci-002"  # 사용할 모델 엔진 설정
prompt = "what thois it mean that 38 prompt + 79 completion = 117 tokens?"  # 사용할 프롬프트 설정

try:
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50
    )

    print(response["choices"][0]["text"])
except openai.error.APIError as e:
    # API 서버 측에서 오류가 발생한 경우 처리할 코드를 작성합니다.
    print("OpenAI API error:", e)