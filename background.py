from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def write_notification(email: str, message: str = ""):
    """
    백그라운드에서 실행될 작업 함수.
    이메일 주소와 메시지를 받아 로그 파일에 기록합니다.
    """
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}:{message}\n"
        email_file.write(content)


@app.get("/send-notification/{email}")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    """
    이 엔드포인트에 요청이 들어오면,
    write_notification 작업을 백그라운드로 실행하고
    즉시 응답을 반환합니다.
    """
    # 백그라운드 작업 등록
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
