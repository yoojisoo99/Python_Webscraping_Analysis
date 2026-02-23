import os
import sys

current_dir = os.getcwd()  
python_version = sys.version  
os_name = os.name  
path_env = os.environ.get('PATH', '')  
path_sample = ":".join(path_env.split(":")[:3])

target_dir = "/Users/username/documents"
file_name = "report.txt"
full_path = os.path.join(target_dir, file_name)
extension = os.path.splitext(file_name)[1]

print(f"현재 작업 디렉토리: {current_dir}")
print(f"Python 버전: {python_version}")
print(f"운영체제: {os_name}")
print(f"환경 변수 PATH 일부: {path_sample}")

print("\n파일 경로 정보:")
print(f"- 디렉토리: {target_dir}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {extension}")

print(f"\n파일 존재 여부: {os.path.exists(full_path)}")