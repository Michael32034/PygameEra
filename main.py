import os
import sys
import random

import pygame
from pygame.locals import *

from config import *
from table import *
from recorder import Recorder

road_w = int(450 / 1.4)
roadmark_w = int(450 / 60)


car1 = os.path.abspath("storage/car1.png")
car2 = os.path.abspath("storage/car2.png")
carq = os.path.abspath("storage/carq.png")

class Windows:
    def __init__(self, size):
        self.size = size
        self.display = pygame.display.set_mode(
            size,
        )
        self.display.fill((60, 220, 0))
        pygame.display.set_caption("PygameEra")

class SimpleCar:
    def __init__(self, rec, display):
        self.running = False
        self.rec = rec
        self.display = display
        self.st = SoundTable()
        self.crash_sound = self.st.get("Crash")
        self.back_sound = self.st.get("Background")
        self.engine_sound = self.st.get("Engine")
        self.simple_f = FontTable(self.display.size).get("Simple")
        self.simple_bf = FontTable(self.display.size).get("SimpleBig")


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
        self.display.display.blit(self.score_area, [0, 0])

    def draw_image(self, car_image, car_loc, car_image1, car_loc1):
        pygame.draw.rect(
            self.display.display,
            (50, 50, 50),
            (self.display.size[0] / 2 - road_w / 2, 0, road_w, self.display.size[1]),
        )
        pygame.draw.rect(
            self.display.display,
            (255, 240, 60),
            (
                self.display.size[0] / 2 - roadmark_w / 2,
                0,
                roadmark_w,
                self.display.size[1],
            ),
        )
        pygame.draw.rect(
            self.display.display,
            (255, 255, 255),
            (
                self.display.size[0] / 2 - road_w / 2 + roadmark_w * 2,
                0,
                roadmark_w,
                self.display.size[1],
            ),
        )
        pygame.draw.rect(
            self.display.display,
            (255, 255, 255),
            (
                self.display.size[0] / 2 + road_w / 2 - roadmark_w * 3,
                0,
                roadmark_w,
                self.display.size[1],
            ),
        )
        self.display.display.blit(car_image, car_loc)
        self.display.display.blit(car_image1, car_loc1)


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
            self.display.size[0] / 3 - car_loc.width / 2
        )  # Set the x-coordinate to center the car horizontally
        car_loc.y = (
            self.display.size[1] * 0.7
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
                self.display.size[0] / 3 - car_loc1.width / 2
            )  # Set the x-coordinate to center the car horizontally
            car_loc1.y = (
                self.display.size[1] * 0.02
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
                self.display.size[0] / 3 - car_loc1.width / 2
            )  # Set the x-coordinate to center the car horizontally
            car_loc1.y = (
                self.display.size[0] * 0.02
            )  # Set the y-coordinate to position the car vertically

        counter = 0
        car_sc = 0
        car_sp = 0
        hight_scope = self.rec.get("g.c.sc.higth_scope")
        width, height = self.display.size
        while not game_over:
            counter += 1

            while game_close:
                score = self.rec.get("g.c.sc.higth_scope")
                game_over_message1 = self.simple_bf.render(
                    f"your highest score '{score}'",
                    True,
                    "black",
                )
                self.display.display.blit(game_over_message1, [width / 6, height / 9])
                game_over_message1 = self.simple_bf.render("crashed!", True, red)
                self.display.display.blit(game_over_message1, [width / 4, height / 5])
                game_over_message = self.simple_bf.render("Game Over!", True, orange)
                self.display.display.blit(game_over_message, [width / 4, height / 3])
                game_over_message2 = self.simple_bf.render("tap to restart!", True, "purple")
                self.display.display.blit(game_over_message2, [width / 4, height / 2])
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
                        self.rec.safe()

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
                            car_loc = car_loc.move([-int(road_w / 2), 0])
                    if event.key in [K_d, K_RIGHT]:
                        if car_loc.x < width / 2:
                            car_loc = car_loc.move([int(road_w / 2), 0])

                    if event.key in [K_d, K_2]:
                        game_close = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # print(mouse_x, mouse_y)

                    if mouse_x > width / 2 and car_loc.right < road_w:
                        car_loc = car_loc.move([int(road_w / 2), 0])

                    if mouse_x < width / 2 and car_loc.left > int(road_w / 2):
                        car_loc = car_loc.move([-int(road_w / 2), 0])

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


    def setup(self):
        self.score_area = pygame.Surface((65, 200))

    def run(self):
        self.running = True
        self.setup()
        self.run_game(self.rec.get(f"simplecar.higth_scope"))


class PygameEra:
    def setup(self):
        pygame.init()
        self.rec = Recorder()
        if sys.platform == "android":
            screen_size = pygame.display.Info()
            size = (screen_size.current_w, screen_size.current_h)
        else:
            size = PC_W_SIZE
        self.display = Windows(size)

    def __init__(self):
        self.setup()

    def run(self):
        self.manager_game = SimpleCar(self.rec, self.display)
        self.manager_game.run()


game = PygameEra()
game.run()
