import random

food_list_in = ["맥도날드", "브라운돈까스", "그릭데이", "뜸들이다", "베나레스 커리도시락", "호랑이 소고기 국밥", "미스터국밥", "명륜왕만두", "치교치밥"]
food_list_out = ["영철버거", "고른햇살", "어흥식당", "편의점", "특별식당", "언니네반점", "용초수", "이세돈까스", "아바이 토종 순대국", "히포크라테스 스프", "미스터국밥", "짱가네 돈냉면", "토로 생선구이", "육쌈냉면", "한솥도시락", "이공냉면", "해곤선생", "쿠이도라쿠", "차이니웍", "고래돈까스", "무화"]

print("~~안암 긱사러 메뉴 정하기~~\n\n")
inout = int(input("배달시키면 1, 밖에서 먹으면 2 입력: "))
newran = int(input("새로운 메뉴/식당 입력은 3, 랜덤 메뉴/식당 출력은 4 입력: "))

if newran == 3:
    if inout == 1:
        new_menu = input("새로운 메뉴/식당을 입력해주세요.: ")
        food_list_in.append(new_menu)
        print("추가 완료!\n")
    elif inout == 2:
        new_menu = input("새로운 메뉴/식당을 입력해주세요.: ")
        food_list_in.append(new_menu)
        print("추가 완료!\n")
    else:
        print("숫자를 다시 입력해주세요. 배달시키면 1, 밖에서 먹으면 2를 입력해주세요.")
        inout = int(input())
        
elif newran == 4:
    if inout == 1:
        random_menu = random.sample(food_list_in,1)
    elif inout == 2:
        random_menu = random.sample(food_list_out,1)
    print("오늘 추천하는 메뉴/식당은 {0} 입니다.".format(random_menu))

else:
    print("숫자를 다시 입력해주세요. 새로운 메뉴/식당 입력은 3, 랜덤 메뉴/식당 출력은 4를 입력합니다.: ")
    newran = int(input())