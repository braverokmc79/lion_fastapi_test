# 🚀 FastAPI CRUD 예제

FastAPI를 이용한 간단한 CRUD API 예제입니다.
`items.py`에 정의된 라우터를 통해 아이템 데이터를 생성, 조회, 수정, 삭제할 수 있습니다.

---

## 프로젝트 구조

```
FastAPI/
├── main.py         # FastAPI 앱 실행 파일
├── items.py        # CRUD 로직 정의
└── README.md       # 실행 및 설명 문서
```

---

## ▶️ 실행 방법

### 1. 의존 패키지 설치

```bash
pip install fastapi uvicorn
```

### 2. 서버 실행

```bash
uvicorn main:app --reload
```

* `main`: main.py 파일 이름
* `app`: FastAPI 인스턴스 이름
* `--reload`: 코드 수정 시 자동 반영 (개발 시 권장)

---

## 파이프리더를 통한 문서 조회

FastAPI는 자동으로 인터래티브 문서를 생성해줍니다.

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 테스트용 예제 요청

```http
POST /items/
Content-Type: application/json

{
  "id": 1,
  "name": "Apple",
  "description": "A juicy fruit",
  "price": 1.5,
  "tax": 0.1
}
```

---

## 참고

* 공식 문서: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
