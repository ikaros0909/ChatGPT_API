import openai
import os
import configparser

# 설정 파일을 읽어들입니다.
config = configparser.ConfigParser()
config.read('config.ini')

# 인증 정보 설정
openai.api_key = config.get('openai', 'api_key')

# API 연결 테스트
model_engine = "code-davinci-002"  # 사용할 모델 엔진 설정 (text-davinci-002)
strSchema = "### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### "  # 사용할 프롬프트 설정
strQueryMode = "\nSELECT"

strPrompt = "지난 3개월동안 10명 이상의 직원을 고용한 부서의 이름을 나열해줘"
try:
    response = openai.Completion.create(
        model=model_engine, 
        prompt=strSchema+strPrompt+strQueryMode,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    # response = openai.Completion.create(
    #     engine=model_engine, # 사용할 모델 엔진 설정
    #     prompt=prompt, # 사용할 프롬프트 설정
    #     max_tokens=200 # 생성할 토큰의 최대 개수 설정
    # )
    
    # api 호출하는 부분
    

    print(response["choices"][0]["text"])
except openai.error.APIError as e:
    # API 서버 측에서 오류가 발생한 경우 처리할 코드를 작성합니다.
    print("OpenAI API error:", e)