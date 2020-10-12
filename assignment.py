import pygame, random


##########################################################
#기본 초기화 ( 반드시 해야 하는 것들 )

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 #width
screen_height = 640 #height
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YoungbinSoftware Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
##########################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("/users/youngbinha/desktop/python/pygame/background.jpg")

character = pygame.image.load("/users/youngbinha/desktop/python/pygame/human.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

enemy = pygame.image.load("/users/youngbinha/desktop/python/pygame/poop.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, (screen_width - enemy_width))
enemy_y_pos = 0 - enemy_height

game_font = pygame.font.Font(None, 40) #  Font(font, size)

character_speed = 0.6

falling_speed = 10
life = 3
running = True #게임이 진행중인가 ? 
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    # 3. 게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 적이 내려오게 하기
    falling_speed += 0.01
    print(falling_speed)
    enemy_y_pos +=  falling_speed
    if enemy_y_pos > 640:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, (screen_width - enemy_width))

    # 충돌 처리 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    life_count = game_font.render(str(int(life)), True, (255,255,255))
    end_script = game_font.render(str("You got shit"), True, (255,0,0))
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        screen.blit(end_script, ((screen_width/2)-(enemy_width/2),(screen_height/2)-(enemy_height / 2)))
        if life == 0:
            running = False
        else:
            enemy_y_pos=0
            life -= 1

    # 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(life_count, (10,10))

    pygame.display.update() # 게임화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)


#pygame 종료
pygame.quit()
