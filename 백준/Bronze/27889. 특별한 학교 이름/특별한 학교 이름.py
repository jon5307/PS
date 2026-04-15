# 약칭과 정식 명칭의 매핑
school_names = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy"
}

# 약칭 입력 받기
abbreviation = input().strip()

# 약칭에 해당하는 정식 명칭 출력
print(school_names.get(abbreviation, "Unknown School"))