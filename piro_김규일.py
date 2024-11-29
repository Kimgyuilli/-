import random
import time

class Character:
    # Charactor 생성자
    def __init__(self, name, hair, clothes, shoes):
        self.name = name
        self.hair = hair
        self.clothes = clothes
        self.shoes = shoes

class DetectiveGame:
    
    #생성자
    def __init__(self):
        self.characters_sample = [
            Character("최승호", "장발이야", "운동복을 입었어", "나이키를 신었어"),
            Character("김민수", "파란 모자를 썼어", "양복을 입었어", "구두를 신었어"),
            Character("이건희", "파마를 했어", "무스탕을 입었어", "아무것도 안 신고 있었어"),
            Character("손관우", "스님 머리야", "셔츠를 입었어", "슬리퍼 신었어"),
            Character("장지요", "단발머리야", "치마를 입었어", "부츠를 신었어"),
            Character("안시환", "투블럭을 했어", "반팔티를 입었어", "크록스를 신었어"),
            Character("이지현", "허리까지 머리카락이 있어", "원피스를 입었어", "힐을 신었어")
        ]

    #인트로 출력, 게임 세팅
    def show_intro(self):
        print("탐정 게임에 오신 것을 환영합니다.")
        time.sleep(1)
        print("탐정님의 성함을 입력해주세요: ", end = '')
        self.set_game()
        print(f"\n{self.detective_name}탐정님 어서 오십시오. 피로그래밍 22기의 해커톤을 즐겨주시기 바랍니다.\n")

        #다잉 메시지 생성, 단서 저장
        dying_message_type = random.choice(["hair", "clothes", "shoes"])
        if dying_message_type == "hair":
            self.dying_message = f"머리스타일은 {self.murderer.hair} 윽..☠️"
            self.clue = self.murderer.hair
        elif dying_message_type == "clothes":
            self.dying_message = f"옷은 {self.murderer.clothes} 윽..☠️"
            self.clue = self.murderer.clothes
        else:
            self.dying_message = f"신발은 {self.murderer.shoes} 윽..☠️"
            self.clue = self.murderer.shoes

        print(f"########################################")
        print(f"#######        평화로운 해커톤              ")
        print(f"########################################")
        time.sleep(1.5)


        print(f"\n코딩에 몰두하던 {self.detective_name}, 눈이 피로해지기 시작한다. 해커톤의 열기가 고조될수록, 정신은 점점 흐릿해진다.")
        time.sleep(1)
        print(f"{self.detective_name}: 이 해커톤, 너무 평화롭기만 하군... 뭔가 재밌는 사건이라도 터져야 할 텐데. 뭐, 코드가 몽땅 날아가는 일이라든지.")
        time.sleep(1)
        print(f"{self.victim.name}: 하하, 탐정님! 그런 무서운 말씀은 제발 그만하세요. 상상만 해도 아찔하네요... 그런 일은 절대로 일어나지 않을 거예요.")
        time.sleep(1)
        print(f"{self.detective_name}: 뭐, 그렇긴 하겠지. 아, 참고로 나는 명탐정 {self.detective_name}! 사건이 터지면 언제든 나를 찾아.")
        time.sleep(1)
        print(f"{self.victim.name}: 하하, 명탐정님! 알겠습니다. 그런데 요즘 제 노트북을 자꾸 누가 훔쳐보는 것 같아서 신경 쓰이긴 해요. 집 앞 카페에서 코딩하다 보면 말이죠...")
        time.sleep(1)
        print(f"그렇게 둘은 헤어졌고, 그로부터 10분 후 갑자기 정전이 일어나게 되는데..\n")
        time.sleep(1)

        print(f"########################################")
        print(f"#######        사건 발생             ")
        print(f"########################################")
        time.sleep(1)

        print(f"갑자기 날카로운 비명 소리가 울려 퍼졌다. {self.victim.name}씨의 노트북 화면이 순식간에 블루스크린으로 바뀌었다.")
        time.sleep(1)
        print(f"그 충격에 {self.victim.name}씨는 정신을 잃고 그대로 쓰러졌다...")
        time.sleep(1)

        print(f"\n현장은 순식간에 혼란에 빠졌고, 바닥에는 {self.victim.name}씨의 메시지가 남겨져 있었다.")
        time.sleep(1)

        print("\n================사망하지는 않았지만 이게 다잉메시지?!================")
        print(f"                    \"{self.dying_message}\"")
        print("=====================================================================")
        time.sleep(1)

        print(f"\n문제의 노트북 주위에 있는 사람은 {len(self.characters)}명입니다.") # 배열의 길이는 len()을 사용하면 얻을 수 있다.
        time.sleep(1)
        print(f"그중, 범인은 바로 이 자리에 있을 것입니다...")
        time.sleep(1)
        print(f"{self.detective_name}님의 임무는 범인을 찾아내는 것입니다. 진실을 밝혀내세요. 기회는 2번입니다.\n")
        time.sleep(1)

        print(f"########################################")
        print(f"#######        추리 시작               ")
        print(f"########################################")
        time.sleep(1)
    
    # 용의자 조사
    def investigate(self):
        print("용의자와 대화를 나누고 인상착의를 수집하세요...\n")
        for index, char in enumerate(self.characters, 1): # 용의자 출력
            print(f"{index}. {char.name}")
        
        # 이름 입력이 잘못되면 메시지 출력 후 반복
        while True:
            print("\n누구를 조사하시겠습니까? 이름을 입력하세요: ", end="")
            choice_name = input().strip()
            self.suspect = next((char for char in self.characters if char.name == choice_name), None) # next를 사용한 array 순회 리스트에 없으면 None 반환
            if self.suspect:
                self.Explain_Suspect(self.suspect)
                break
            else:
                print("잘못된 입력입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
                print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")

    # 용의자 설명
    def Explain_Suspect(self, character): 
        print(f"\n{character.name}의 인상착의를 봅니다.")
        print(f"머리: {character.hair}")
        print(f"옷: {character.clothes}")
        print(f"신발: {character.shoes}")

    # 범인이 맞는지 확인
    def match_clue(self, suspect):
        if self.clue == suspect.hair or self.clue == suspect.clothes or \
                self.clue == suspect.shoes:
            return True
        return False

    # 선택 메서드
    def prompt_choice(self, prompt):
        while True:
            choice = input(prompt).strip()
            if choice in ['네', '아니오']:
                return choice
            print("잘못된 입력입니다. 네 또는 아니오만 입력해 주세요.")


    # 범인 지목
    def accuse(self):
        print("\n범인을 지목할 시간입니다.")

        while True: # 용의자 출력
            for index, char in enumerate(self.characters, 1):
                print(f"{index}. {char.name}")
            
            print("\n누구를 범인으로 지목하시겠습니까? 이름을 입력하세요: ", end="")
            choice_name = input().strip()
            print(f"{self.detective_name}: 범인은 바로 {choice_name}씨야")
            self.suspect = next((char for char in self.characters if char.name == choice_name), None) # 입력이 유효한지 확인

            if self.suspect:
                self.check_outcome() #결과 메서드 호출
                return
            else:
                print("탐정님, 그건 잘못된 선택입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
                print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")
                print(f"{self.detective_name}: 좋아, 이번엔 잘 선택해보자.\n")
                time.sleep(1)

    # 결과출력
    def check_outcome(self):
        if self.match_clue(self.suspect): # 정답
            print("""
----------------------------------------------------------------------------------


     ██████╗  █████╗ ███╗   ███╗███████╗    ██╗    ██╗██╗███╗   ██╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║    ██║██║████╗  ██║
    ██║  ███╗███████║██╔████╔██║█████╗      ██║ █╗ ██║██║██╔██╗ ██║
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║███╗██║██║██║╚██╗██║
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚███╔███╔╝██║██║ ╚████║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝


----------------------------------------------------------------------------------""")
            time.sleep(1)
            print(f"###############################################")
            print(f"#######        당신은 역시 명탐정!!         ")
            print(f"###############################################")
            time.sleep(1)
            print(f"\n정답입니다! 범인은 바로 {self.suspect.name}씨였습니다!")
            time.sleep(1)
            print(f"당신의 추리는 완벽했습니다, 역시 명탐정 {self.detective_name} 답군요.")
            time.sleep(1)
            print(f"\n{self.detective_name}: 왜 노트북을 망가뜨렸습니까?? {self.victim.name}씨의 노트북을 왜 그렇게 했죠?")
            time.sleep(1)
            print(f"{self.suspect.name}: 그게 사실... {self.victim.name}씨의 팀이 해커톤 우승을 못하게 하려고... 그래서 홧김에.. 죄송합니다🥹")
            time.sleep(1)
            print(f"\n{self.suspect.name}씨는 끝내 자신의 범행을 인정했고, 피로그래밍 22기 해커톤에서 퇴출당했습니다.")
            time.sleep(1)
            print(f"사건은 해결되었고, 모든 사람들이 안도의 한숨을 내쉬었습니다. 당신의 활약 덕분입니다.")
            time.sleep(1)
            self.ask_restart()

        else: # 실패 1회
            self.lives -= 1
            if self.lives > 0:
                print(f"\n{self.suspect.name}: 무슨 소리야? 내 인상착의를 봐... 당신 명탐정 맞아? 💢💢💢")
                print(f"\n틀렸습니다... {self.suspect.name}씨는 범인이 아닙니다. 남은 기회는 {self.lives}번입니다.")
                print(f"시간이 얼마 남지 않았어요. 신중하게 선택해주세요.")
                time.sleep(1)
                choice = self.prompt_choice("\n용의자들의 인상착의를 다시 보겠습니까? (네/아니오): ")
                if choice == '네':
                    print(f"{self.detective_name}: 좋았어... 다시 차근차근 보자\n")
                    time.sleep(1)
                else:
                    self.accuse()  # 다시 지목할 기회를 줌
            else: # GAMEOVER
                print(
                    """
----------------------------------------------------------------------------------


    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


----------------------------------------------------------------------------------"""
                )
                time.sleep(1)
                print(f"########################################")
                print(f"#######         추리 실패......           ")
                print(f"########################################")
                time.sleep(1)
                print(f"\n{self.murderer.name}: 명탐정 별거 없네~~~ 해커톤 우승은 내꺼다!!!")
                time.sleep(1)
                print(f"\n안타깝습니다... 범인은 {self.murderer.name}씨였습니다. 모든 기회를 다 써버렸습니다.")
                time.sleep(1)
                print(f"추리는 실패했습니다. {self.detective_name} 탐정님, 이번 사건은 당신에게 큰 상처로 남게 될 것입니다.")
                time.sleep(1)
                print(f"당신은 이 미스터리를 풀 기회를 잃었습니다...")
                time.sleep(1)
                print(f"하지만, 진정한 탐정은 실패에서도 배웁니다. 다음엔 꼭 진실을 밝혀내세요.")
                time.sleep(1)
                self.ask_restart()

    # 게임을 다시 할 건지 물어보는 메서드
    def ask_restart(self):
        choice = self.prompt_choice("게임을 다시 시작하시겠습니까? (네/아니오): ")
        if choice == '네':
            print("----------------------------------------------------------------------------------\n")
            self.play()
        else:
            print("게임을 종료합니다. 감사합니다!")
            self.flag = False
            return
            
    # 변수 초기화
    def set_game(self):
        self.lives = 2 # 남은 목숨
        self.suspect = None # 용의자
        self.detective_name = input().strip() # 탐점
        self.characters = self.characters_sample.copy() # 캐릭터 카피(게임 재시작 시 재사용을 위해)
        self.victim = random.choice(self.characters) # 희생자
        self.characters.remove(self.victim)  # 희생자 캐릭터 목록에서 제거.
        self.murderer = random.choice(self.characters)  # 범인 선택.
        self.flag = True # 게임 진행 boolean

    # 게임 플레이!
    def play(self):
        self.show_intro()
        # 조사 단계 (인상착의를 수집, 무제한)
        while self.flag:
            self.investigate()
            if self.prompt_choice("\n계속 조사하시겠습니까? (네/아니오): ") == '아니오':
                # 범인 지목 (목숨 2개)    
                self.accuse()


# 게임 실행
if __name__ == "__main__":
    game = DetectiveGame()
    game.play()