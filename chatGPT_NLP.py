import openai
import os
import configparser

# 설정 파일을 읽어들입니다.
config = configparser.ConfigParser()
config.read('config.ini')

# 인증 정보 설정
openai.api_key = config.get('openai', 'api_key')

# API 연결 테스트
model_engine = "text-davinci-003"  # 사용할 모델 엔진 설정 (text-davinci-002 / gpt-3.5-turbo)
# strTrans = "translate Korean to English: "
strSchema = "### 아래의 내용을 토대로 장점 한문장, 단점 한문장으로 요약해줘 :\n#\n### "  # 사용할 프롬프트 설정

strPrompt = "졸업전시회를 준비하며 자신을 표현할수록 작품이 너무 불완전하다고 느껴 제때 제출을 못 했고 성적에도 크게 영향을 미쳤습니다.# 학교폭력예방 및 대책에 관한 법률 제17조 제1항 3호에 따른 교내봉사 10시간 조치(2017.9.25.)를 받음.# 건강상의 이유로 몇 번의 수술과 회복의 과정을 통해 자신에게 주어진 것에 감사하는 것의 현명함을 깨달은 어른 같은 아이임.# 정기적으로 양산시 청소년방과후 아카데미에 방문(2018.03.05.-2018.11.19.)하여 학습 멘토 역할을 함."
try:
    response = openai.Completion.create(
        model=model_engine,
        prompt=strSchema+strPrompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    print(response["choices"][0]["text"])
            
except openai.error.APIError as e:
    # API 서버 측에서 오류가 발생한 경우 처리할 코드를 작성합니다.
    print("OpenAI API error:", e)