import pygame as pg

class Application:

    def start(self):
        pg.init()

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
        pass

    def render(self):
        pass

    def update(self):
        pass

    game_clock = pg.time.Clock()
    game_should_run = True

    MS_PER_UPDATE = 1000.0