# pip install rich 가 필요합니다.
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 변수
name = "Alice"
age = 25
score = 95.5
data = {'name': name, 'age': age, 'score': score}

# f-string 스타일 출력
rprint(f"[bold green]Hello, {name}[/]! Your score is [cyan]{score:.2f}[/].")

# 백그라운드로 멀티라인 출력
panel_text = """
[bold]Student Info[/]
Name: [yellow]{name}[/]
Age: [magenta]{age}[/]
- Score: [cyan]{score:.2f}[/]
"""

rprint(Panel(panel_text, title="Profile", border_style="blue"))

# 테이블 생성 (디스플레이리스트로 보기 추가)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

rprint(table)

# sep, end 값과 함께 출력 (rich.print와 동일 동작)
rprint("2025", "09", "23", sep="-", end="\n")