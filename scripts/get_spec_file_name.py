import os
from pathlib import Path

p = Path("specs/")
sorted(p.iterdir()).remove

spec_files = sorted([i for i in p.iterdir() if i.name != "README.md"])
current_number = spec_files[-1].stem.split("-")[0]
next_number = int(current_number) + 1

raw_issue_title = os.getenv("ISSUE_TITLE")
assert raw_issue_title is not None

issue_title_parts = [i.lower() for i in raw_issue_title.split(" ")]

print(f"{next_number}-{'-'.join(issue_title_parts)}")
