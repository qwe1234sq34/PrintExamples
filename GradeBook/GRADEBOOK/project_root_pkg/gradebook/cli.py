
"""명령형 실행 인터페이스 (CLI) - 요약형 출력"""
import os
from .models import Student, GradeBook
from .io.csvio import load_students_from_csv

def run_cli(csv_path='students.csv'):
    print("🟢 GradeBook CLI 실행 중...")
    # Try to load CSV; if missing, use default sample data from PPT
    students = []
    if os.path.exists(csv_path):
        print(f"CSV 파일에서 데이터 불러오는 중: {csv_path}")
        students = load_students_from_csv(csv_path)
    else:
        print(f"CSV 파일({csv_path})을 찾을 수 없습니다. 기본 예제 데이터 사용합니다.")
        students = [
            Student("Alice", [90, 85, 92]),
            Student("Bob", [70, 75, 68])
        ]

    gb = GradeBook()
    for s in students:
        gb.add_student(s)

    print("\n=== 학급 성적 요약 ===")
    print(f"전체 학생 수: {len(gb)}")
    print(f"전체 평균: {gb.class_average():.2f}")
    dist = gb.grade_distribution()
    print("학점 분포:")
    print(", ".join([f"{k}: {v}명" for k,v in dist.items()]))
