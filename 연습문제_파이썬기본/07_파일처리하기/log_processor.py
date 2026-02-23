from datetime import datetime

raw_logs = [
    {"time": "2025-07-20 09:15:00", "level": "WARNING", "message": "메모리 사용량이 높습니다"},
    {"time": "2025-07-20 10:30:00", "level": "ERROR", "message": "데이터베이스 연결 실패"},
    {"time": "2025-07-20 11:45:00", "level": "ERROR", "message": "파일을 찾을 수 없음"},
    {"time": "2025-07-20 12:00:00", "level": "WARNING", "message": "디스크 공간 부족"},
]

def print_filtered_logs(logs):
    print("로그 파일이 생성되었습니다.")
    print("\n")

    print("ERROR 레벨 로그들:")
    for log in logs:
        if log["level"] == "ERROR":
            print(f"{log['time']} - {log['level']} - {log['message']}")
    
    print("\n")

    print("WARNING 레벨 로그들:")
    for log in logs:
        if log["level"] == "WARNING":
            print(f"{log['time']} - {log['level']} - {log['message']}")

if __name__ == "__main__":
    print_filtered_logs(raw_logs)