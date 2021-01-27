import pygame as pg
import initialstate

class Application:

    def start(self):
        pg.init()

        window_size = self.window_width, self.window_height
        self.window = pg.display.set_mode(window_size)
        pg.display.set_caption("ATC Sim | v0.0.1")

        # Initial game state
        self.game_states.append(initialstate.InitialState())

    def run(self):
        # Main game loop
        update_lag = 0.0
        while self.game_should_run:
            elapsed_time = self.game_clock.tick()
            update_lag = update_lag + elapsed_time

            self.process_input()

            # Fixed rate update
            while (update_lag >= self.MS_PER_UPDATE):
                self.update(self.MS_PER_UPDATE)
                update_lag = update_lag - self.MS_PER_UPDATE

            self.render(elapsed_time)


    def stop(self):
        pg.quit()

    def process_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_should_run = False

        for state in self.game_states:
            if state.processes_input:
                state.ss_process_input()
                state.process_input()

    def render(self,dt):
        self.window.fill((0,0,0))
        pg.display.flip()

        for state in self.game_states:
            if state.is_visible:
                state.ss_render(dt)
                state.render(dt)

    def update(self,dt):
        for state in self.game_states:
            if not(state.is_paused):
                state.ss_update(dt)
                state.update(dt)

    game_clock = pg.time.Clock()
    game_should_run = True

    MS_PER_UPDATE = 1000.0

    window_width = 500
    window_height = 500
    window = pg.display.set_mode((100,100))

    game_states = []
