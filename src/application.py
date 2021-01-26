import pygame as pg

class Application:

    def start(self):
        pg.init()

        window_size = self.window_width, self.window_height
        self.window = pg.display.set_mode(window_size)
        pg.display.set_caption("ATC Sim | v0.0.1")

    def run(self):
        # Main game loop
        update_lag = 0.0
        while self.game_should_run:
            elapsed_time = self.game_clock.tick()
            update_lag = update_lag + elapsed_time

            self.process_input()

            while (update_lag >= self.MS_PER_UPDATE):
                self.update()
                update_lag = update_lag - self.MS_PER_UPDATE

            self.render()


    def stop(self):
        pg.quit()

    def process_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_should_run = False

    def render(self):
        self.window.fill((0,0,0))
        pg.display.flip()

    def update(self):
        pass

    game_clock = pg.time.Clock()
    game_should_run = True

    MS_PER_UPDATE = 1000.0

    window_width = 500
    window_height = 500
    window = pg.display.set_mode((100,100))