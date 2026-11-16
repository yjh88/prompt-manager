"""나만의 프롬프트 관리 프로그램 (콘솔 기반)

프롬프트를 카테고리별로 분류하고, 검색하고, 즐겨찾기로 관리합니다.
데이터는 프로그램 실행 중에만 유지됩니다. (종료하면 초기화)
"""

# 선택 가능한 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 프롬프트 저장소: 딕셔너리를 담은 리스트
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 10년 경력의 전문 블로거입니다. "
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. "
            "서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. "
            "밝고 깔끔한 배경, 제품이 중앙에 크게 보이는 구도, "
            "16:9 비율, 텍스트 없이 제품에만 집중된 스타일로 만들어주세요."
        ),
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 컨설턴트입니다. "
            "비전문가도 이해할 수 있도록 쉬운 비유로 설명하고, "
            "항상 현실적인 비용과 일정, 위험 요소를 함께 짚어주세요."
        ),
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": (
            "아래 뉴스 기사를 읽고 핵심 내용을 3줄로 요약해주세요. "
            "마지막에는 이 기사가 독자에게 주는 시사점을 한 문장으로 덧붙여주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "광고 스크립트 작성",
        "content": (
            "15초 길이의 제품 광고 영상 스크립트를 작성해주세요. "
            "장면별 화면 설명과 내레이션을 표 형태로 정리하고, "
            "마지막 장면에는 행동을 유도하는 문구를 넣어주세요."
        ),
        "category": "영상 생성",
        "favorite": False,
    },
]

# 메뉴 번호와 이름
MENU = {
    "1": "프롬프트 추가",
    "2": "프롬프트 목록",
    "3": "카테고리별 조회",
    "4": "프롬프트 검색",
    "5": "프롬프트 상세 보기",
    "6": "즐겨찾기 관리",
    "7": "즐겨찾기 목록",
    "0": "종료",
}


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    for number, name in MENU.items():
        print(f"{number}. {name}")


def input_required(label):
    """빈 값이 아닌 입력을 받을 때까지 다시 요청한다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("⚠ 값이 비어 있습니다. 다시 입력해주세요.")


def select_category():
    """목록에서 번호를 고르거나 새 카테고리를 직접 입력해 카테고리를 정한다."""
    print("\n카테고리 선택:")
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}) {category}")
    print("(번호를 고르거나, 새 카테고리 이름을 직접 입력하세요)")

    while True:
        value = input_required("선택: ")
        if value.isdigit():
            number = int(value)
            if 1 <= number <= len(CATEGORIES):
                return CATEGORIES[number - 1]
            print("⚠ 목록에 없는 번호입니다. 다시 선택해주세요.")
        else:
            if value not in CATEGORIES:
                CATEGORIES.append(value)  # 직접 입력한 카테고리는 목록에 추가
            return value


def add_prompt():
    """새 프롬프트를 입력받아 리스트에 추가한다."""
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = select_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,  # 즐겨찾기 기본값
    })
    print("\n프롬프트가 추가되었습니다!")


# ===== 메인 =====

def main():
    """메뉴를 반복해서 보여주고, 입력한 번호의 기능을 실행한다."""
    actions = {
        "1": add_prompt,
        # ACTIONS-END
    }

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        elif choice in actions:
            actions[choice]()
        elif choice in MENU:
            print("아직 준비 중인 기능입니다.")
        else:
            print("⚠ 잘못된 입력입니다. 메뉴에 있는 번호를 입력해주세요.")


if __name__ == "__main__":
    main()

