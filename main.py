import sys
import random

import pygame
from pygame.locals import *

from config import *
from table import *
from ui import *
from items import *
from recorder import Recorder


class SimpleCarGame:
    def __init__(self, rec: Recorder):
        self.running = False

        self.rec = rec
        self.screen = pygame.display.get_surface()
        self.size = Screen.current_size()
        self.clock = pygame.time.Clock()
        self.st = SoundTable()
        self.ft = FontTable()

        self.crash_sound = self.st.get("Crash")
        self.back_sound = self.st.get("Background")
        self.engine_sound = self.st.get("Engine")

    def setup(self):
        self.road = Road()
        self.score = 0
        self.window = Window((0, 0), (0.3, 0.3), white)
        self.score_area = pygame.Surface((65, 200))
        self.speed: int = self.rec.get("simplecar.and.start_speed")
        self.higth_scope: int = self.rec.get("simplecar.higth_scope")
        self.fps: int = self.rec.get("g.s.FPS")
        self.back_sound.play()

    def print_score(self, sc, sp):
        self.score_area.fill((60, 220, 0))
        text = self.simple_f.render("score:", True, "black")
        self.score_area.blit(text, [0, 0])
        text1 = self.simple_bf.render(str(sc), True, "red")
        self.score_area.blit(text1, [10, 20])

        game_over_message = self.simple_f.render("speed:", True, "black")
        self.score_area.blit(game_over_message, [0, 60])
        game_over_message1 = self.simple_bf.render(f"{str(sp)}m/s", True, "blue")
        self.score_area.blit(game_over_message1, [3, 90])
        self.screen.blit(self.score_area, [0, 0])

    def run_game(self, speed_):
        car_speed = speed_
        game_over = False
        game_close = False

        # highway_image = pygame.image.load('highways.jpg')
        # highway_width, highway_height = 300, 700
        # highway_image = pygame.transform.scale(highway_image, (highway_width, highway_height))

        # highway_loc = highway_image.get_rect()
        # highway_loc.x = width/2 - highway_loc.width/2
        # highway_loc.y = 0

        car_image = pygame.image.load(car1)
        car_width, car_height = 80, 160  # Set the desired width and height for the car
        car_image = pygame.transform.scale(
            car_image, (car_width, car_height)
        )  # Resize the car image

        car_loc = car_image.get_rect()
        car_loc.x = (
            self.root.size[0] / 3 - car_loc.width / 2
        )  # Set the x-coordinate to center the car horizontally
        car_loc.y = (
            self.root.size[1] * 0.7
        )  # Set the y-coordinate to position the car vertically

        if random.randint(0, 1) == 0:
            car_image1 = pygame.image.load(car2)
            car_width1, car_height1 = (
                80,
                160,
            )  # Set the desired width and height for the car
            car_image1 = pygame.transform.scale(
                car_image1, (car_width1, car_height1)
            )  # Resize the car image

            car_loc1 = car_image1.get_rect()
            car_loc1.x = (
                self.root.size[0] / 3 - car_loc1.width / 2
            )  # Set the x-coordinate to center the car horizontally
            car_loc1.y = (
                self.root.size[1] * 0.02
            )  # Set the y-coordinate to position the car vertically

        else:
            car_image1 = pygame.image.load(carq)
            car_width1, car_height1 = (
                100,
                160,
            )  # Set the desired width and height for the car
            car_image1 = pygame.transform.scale(
                car_image1, (car_width1, car_height1)
            )  # Resize the car image

            car_loc1 = car_image1.get_rect()
            car_loc1.x = (
                self.root.size[0] / 3 - car_loc1.width / 2
            )  # Set the x-coordinate to center the car horizontally
            car_loc1.y = (
                self.root.size[0] * 0.02
            )  # Set the y-coordinate to position the car vertically

        counter = 0
        car_sc = 0
        car_sp = 0
        hight_scope = self.rec.get("g.c.sc.higth_scope")
        width, height = self.root.size
        while not game_over:
            counter += 1
            print("#1")
            while not game_close:
                score = self.rec.get("g.c.sc.higth_scope")
                game_over_message1 = self.simple_bf.render(
                    f"your highest score '{score}'",
                    True,
                    "black",
                )
                print("#2")
                self.root.display.blit(game_over_message1, [width / 6, height / 9])
                game_over_message1 = self.simple_bf.render("crashed!", True, red)
                self.root.display.blit(game_over_message1, [width / 4, height / 5])
                game_over_message = self.simple_bf.render("Game Over!", True, orange)
                self.root.display.blit(game_over_message, [width / 4, height / 3])
                game_over_message2 = self.simple_bf.render(
                    "tap to restart!", True, "purple"
                )
                self.root.display.blit(game_over_message2, [width / 4, height / 2])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            game_over = True
                            game_close = False

                        if event.key == pygame.K_PAGEDOWN:
                            self.run_game(car_speed)

                        if event.key == pygame.K_SPACE:
                            self.run_game(car_speed)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if game_close == True:
                            self.run_game(car_speed)
                            # game_over = False

                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
            right_lane = int(width / 2.1 + car_loc1.width / 2)
            left_lane = int(width / 3 - car_loc1.width / 2)
            self.engine_sound.play()
            if counter == 1024:
                car_speed += 0.15
                counter = 0
            # highway_loc[1] += 700
            # if highway_loc[1] > height:
            #     highway_loc[1] = -200
            car_loc1[1] += car_speed
            if car_loc1[1] > height:
                car_loc1[1] = -200
                car_sc = car_sc + 3
                car_sp = car_sp + 1
                if car_sc > hight_scope:
                    self.rec.set("g.c.sc.higth_scope", car_sc)

                if random.randint(0, 1) == 0:
                    car_loc1.x, car_loc1.y = right_lane, -200

                else:
                    car_loc1.x, car_loc1.y = left_lane, -200

            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        if car_loc.x > width / 2:
                            car_loc = car_loc.move([-int(self.road_w / 2), 0])
                    if event.key in [K_d, K_RIGHT]:
                        if car_loc.x < width / 2:
                            car_loc = car_loc.move([int(self.road_w / 2), 0])

                    if event.key in [K_d, K_2]:
                        game_close = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # print(mouse_x, mouse_y)

                    if mouse_x > width / 2 and car_loc.right < self.road_w:
                        car_loc = car_loc.move([int(self.road_w / 2), 0])

                    if mouse_x < width / 2 and car_loc.left > int(self.road_w / 2):
                        car_loc = car_loc.move([-int(self.road_w / 2), 0])

                # if event.type == pygame.MOUSEBUTTONUP:
                #     print('mouse up')

                # if event.type == pygame.FINGERDOWN:
                #     print("Finger touched the screen")
                # if event.type == pygame.FINGERUP:
                #     print("Finger touched the screen")

            if car_loc.colliderect(car_loc1):
                self.back_sound.stop()  # stop background audio then start play crash sound then it will play
                self.crash_sound.play()
                game_close = True

            self.draw_image(car_image, car_loc, car_image1, car_loc1)
            # screen.blit(highway_image, highway_loc)

            self.print_score(car_sc, car_sp)
            self.back_sound.play()
            pygame.display.update()

        pygame.quit()
        quit()

    def output(self):
        font = self.ft.get("Simple")
        font_size = self.ft.size("Simple")
        bfont = self.ft.get("SimpleBig")
        bfont_size = self.ft.size("SimpleBig")
        self.window.add_context(
            Text("score:", font),
            Text(str(self.score), bfont, (int(float(font_size) * 1.2), bfont_size)),
            Text(
                "speed:",
                font,
                (int(float(font_size) * 1.2) + int(float(bfont_size) * 1.2), 0),
            ),
            Text(
                str(self.speed),
                bfont,
                (
                    int(float(font_size * 2.6)) + int(float(bfont_size * 1.2)),
                    bfont_size,
                ),
            ),
        )

    def update(self):
        self.road.update()
        self.output()
        self.window.update()

    def eventcheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def eventloop(self):
        while self.running:
            self.screen.fill(green)
            self.eventcheck()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)

    def draw(self):
        self.road.draw(self.screen)
        self.screen.blit(self.window.image, self.window.rect)

    def run(self):
        self.running = True
        self.setup()
        self.eventloop()
        # self.run_game(self.rec.get(f"simplecar.higth_scope"))


class PygameEra:
    def setup(self):
        pygame.init()
        self.rec = Recorder()
        if sys.platform == "android":
            screen_size = pygame.display.Info()
            size = (screen_size.current_w, screen_size.current_h)
        else:
            size = PC_W_SIZE
        self.display = Screen(size)

    def __init__(self):
        self.setup()

    def run(self):
        self.manager_game = SimpleCarGame(self.rec)
        self.manager_game.run()


game = PygameEra()
game.run()
