# LLM MOCK EXAM
> LLM 기반 모의 고사 제작 툴

<br>

## Quick Start Guide
### 1. ```.env``` 파일 작성
```bash
OPENAI_API_KEY="API KEY HERE"
```

<br>

### 2. Install requirements
```bash
pip install -r ./requirements.txt
sudo apt install texlive-xetex
```

<br>

### 3. Install Korean Font
#### In Ubuntu
```bash
sudo apt-get install -y fonts-nanum
sudo fc-cache -fv
```

#### In Window
```NanumBarunGothic.ttf``` 설치

<br>

### 4. modify & run main.py file
main.py ```args``` dictionary에 필요한 정보를 입력

실행:
```bash
python3 main.py
```