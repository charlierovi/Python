import pygame
import random
import sys

# ========================
# Configuració inicial
# ========================
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Inicialitzar Pygame i la finestra
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Extensible - Ampliació 4: Menú i Reinici")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# ========================
# So i música
# ========================
pygame.mixer.init() # Els sons i música per cada moment
shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
collision_sound = pygame.mixer.Sound("sounds/collision.wav")
move_sound = pygame.mixer.Sound("sounds/move.wav")
pygame.mixer.music.load("sounds/background_music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
shoot_sound.set_volume(1.0)
collision_sound.set_volume(0.4)
move_sound.set_volume(0.3)

# ========================
# Variables Globals del Joc
# ========================
score = 0
max_score = 0 # Per començar a guardar les puntuacions
difficulty_level = 1
lives = 5
last_difficulty_update_time = pygame.time.get_ticks()
spawn_interval = 2000
ADD_OBSTACLE = pygame.USEREVENT + 1
PAUSE_EVENT = pygame.USEREVENT + 2  # Es crea event per a la pausa


# ========================
# Funcions Auxiliars
# ========================

def draw_text(surface, text, font, color, x, y):
    """Dibuixa un text a la pantalla."""
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

def load_max_score(): # Carrega la puntuació màxima
    global max_score
    try:
        with open("max_score.txt", "r") as f:
            max_score = int(f.read())
    except FileNotFoundError:
        max_score = 0

def save_max_score(): # Es guarda la puntuació màxima
    global max_score
    with open("max_score.txt", "w") as f:
        f.write(str(max_score))

# ========================
# Classes del Joc
# ========================

class Player(pygame.sprite.Sprite):
    """Classe per al jugador."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5
        self.projectiles = pygame.sprite.Group()
        self.last_shot_time = 0

    def update(self):
        """Actualitza la posició del jugador segons les tecles premudes."""
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            moved = True
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moved = True
        if keys[pygame.K_SPACE]:
            self.shoot()
        if moved:
            if not pygame.mixer.get_busy():
                move_sound.play(fade_ms=100)

        # Evitar que el jugador surti de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self): # Dispara el projectil des del jugador i crea el projectil
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 500:  # Cooldown de 500ms
            projectile = Projectile(self.rect.right, self.rect.centery)
            all_sprites.add(projectile)
            self.projectiles.add(projectile)
            shoot_sound.play()
            self.last_shot_time = current_time

class Obstacle(pygame.sprite.Sprite):
    """Classe per als obstacles."""
    def __init__(self):
        super().__init__()
        # Crear un obstacle amb dimensions aleatòries
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # Posició inicial: fora de la pantalla per la dreta
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - height)
        # La velocitat s'incrementa amb la dificultat
        self.speed = random.randint(2 + difficulty_level * 2, 5 + difficulty_level * 2) #Multiplicant per 2 el difficulty_level fem que a mesura que puja la dificultat puji la velocitat.
        self.movement_type = random.choice(["linear", "zigzag", "chasing"]) # Es genera el tipus de moviment de l'objecte
        self.direction = 1  # Per poder fer el zig zag

    def update(self):
        """Actualitza la posició de l'obstacle movent-lo cap a l'esquerra.
           Quan surt completament de la pantalla, s'incrementa la puntuació i s'elimina."""
        global score
        self.rect.x -= self.speed
        if self.rect.right < 0:
            score += 1 + difficulty_level #Afegint el difficulty_level fa que la puntuació s'incrementi cada cop que s'esquiva l'obstacle i passa fora de la pantalla per l'esquerra.
            self.kill()

        if self.movement_type == "linear": # Moviment lineal
            self.rect.x -= self.speed

        elif self.movement_type == "zigzag": # Moviment en zig zag
            self.rect.x -= self.speed
            self.rect.y += self.direction * (self.speed // 2)
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.direction *= -1  # La direcció canvia quan toca els extrems de la pantalla

        elif self.movement_type == "chasing": # Moviment per perseguir
            self.rect.x -= self.speed
            if self.player.rect.y < self.rect.y:
                self.rect.y -= self.speed // 2
            elif self.player.rect.y > self.rect.y:
                self.rect.y += self.speed // 2


# ========================
# Funció per reinicialitzar el Joc
# ========================

def new_game():
    """Reinicialitza totes les variables i grups per començar una nova partida."""
    global score, difficulty_level, lives, last_difficulty_update_time, spawn_interval, all_sprites, obstacles, player
    score = 0
    difficulty_level = 1
    lives = 3
    last_difficulty_update_time = pygame.time.get_ticks()
    spawn_interval = 1500
    pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

# ========================
# Funció per mostrar el menú principal
# ========================

def show_menu():
    """Mostra la pantalla de menú d'inici i espera que l'usuari premi alguna tecla per començar."""
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        screen.fill(WHITE)
        draw_text(screen, "Joc Extensible", font, BLACK, 300, 200)
        draw_text(screen, "Prem qualsevol tecla per començar", font, BLACK, 220, 250)
        pygame.display.flip()

class Projectile(pygame.sprite.Sprite): # Es crea una classe per al projectil
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self): # El projectil es mou i quan surt de pantalla s'elimina
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()
# ========================
# Funció per executar la partida
# ========================

def game_loop():
    global max_score
    global difficulty_level, last_difficulty_update_time, spawn_interval, lives
    new_game()
    score = 0
    game_state = "playing"
    paused = False  # Variable per controlar la pausa
    running = True
    while running and game_state == "playing":
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == ADD_OBSTACLE: # Fa que l'objecte conegui la posició del jugador per fer el chasing en funció del moviment en Y
                obstacle = Obstacle()
                obstacle.player = player
                all_sprites.add(obstacle)
                obstacles.add(obstacle)
            elif event.type == pygame.KEYDOWN: # Pausa el joc al clicar la tecla P.
                if event.key == pygame.K_p:
                    paused = not paused

        if paused: # Al estar en pausa es mostra missatge
            screen.fill(WHITE)
            draw_text(screen, "PAUSE", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 - 20)
            draw_text(screen, "CLICA P PER CONTINUAR", font, BLACK, WIDTH // 2 - 90, HEIGHT // 2 + 20)
            pygame.display.flip()
            continue
        # Incrementar la dificultat cada 15 segons
        current_time = pygame.time.get_ticks()
        if current_time - last_difficulty_update_time >= 10000: #Canviant el 15000 per 10000 la velocitat s'incrementa cada 10 segons.
            difficulty_level += 1
            last_difficulty_update_time = current_time
            spawn_interval = max(300, 1500 - difficulty_level * 100) #Es generen més quantitat d'obstacles.
            pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
        # Actualitzar els sprites
        all_sprites.update()

        for projectile in player.projectiles:
            hit_obstacles = pygame.sprite.spritecollide(projectile, obstacles,True)
            for obstacle in hit_obstacles:
                score += 1 + difficulty_level  # Afegeix puntuació per cada obstacle destruït
                projectile.kill() # S'elimina el projectil quan toca l'obstacle
                collision_sound.play()

        # Comprovar col·lisions
        if pygame.sprite.spritecollideany(player, obstacles):
            lives -= 1
            collision_sound.play()
            if lives > 0:
                # Reinicialitzar la posició del jugador i esborrar els obstacles
                player.rect.center = (100, HEIGHT // 2)
                for obs in obstacles:
                    obs.kill()
                pygame.time.delay(500) # S'afegeix una pausa perquè el jugador es prepari per tornar a començar.
            else:
                if score > max_score: # Es guarda la nova puntuació màxima
                    max_score = score
                    save_max_score()
                game_state = "game_over"
        # Dibuixar la escena
        screen.fill(WHITE)
        all_sprites.draw(screen)
        score_text = font.render("Puntuació: " + str(score), True, BLACK)
        max_score_text = font.render("Puntuació Màxima: " + str(max_score), True, BLACK)
        difficulty_text = font.render("Dificultat: " + str(difficulty_level), True, BLACK)
        lives_text = font.render("Vides: " + str(lives), True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(max_score_text, (10, 100))  # Mostrem la puntuació màxima a la part inferior
        screen.blit(difficulty_text, (10, 40))
        screen.blit(lives_text, (10, 70))
        pygame.display.flip()
    return score

# ========================
# Funció per mostrar la pantalla de Game Over
# ========================

def show_game_over(final_score):
    """Mostra la pantalla de Game Over amb la puntuació final i espera per reiniciar."""
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        screen.fill(WHITE)
        draw_text(screen, "Game Over!", font, RED, 350, 200)
        draw_text(screen, "Puntuació Final: " + str(final_score), font, BLACK, 320, 250)
        draw_text(screen, "Prem qualsevol tecla per reiniciar", font, BLACK, 250, 300)
        pygame.display.flip()

# ========================
# Bucle principal del programa
# ========================

while True:
    show_menu()                   # Mostrar menú d'inici
    final_score = game_loop()       # Executar la partida
    show_game_over(final_score)     # Mostrar pantalla de Game Over i esperar reinici