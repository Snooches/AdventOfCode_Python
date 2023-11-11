def read_lines_from_file(path: str) -> list[str]:
    lines: list[str] = []
    for line in open(path, "r", encoding="utf-8").readlines():
        lines.append(line.replace("\n", ""))
    return lines
