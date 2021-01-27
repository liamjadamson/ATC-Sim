class GameState:
    def __init__(self):
        pass

    def update(self,dt):
        for game_object in self.game_objects:
            if not(game_object.is_paused):
                game_object.update(dt)

    def render(self,dt):
        for game_object in self.game_objects:
            if game_object.is_visible:
                game_object.render(dt)

    def process_input(self):
        for game_object in self.game_objects:
            if game_object.processes_input:
                game_object.process_input()

    def ss_update(self, dt):
        pass

    def ss_render(self,dt):
        pass
    
    def ss_process_input(self):
        pass

    game_objects = []

    processes_input = True
    is_paused = False
    is_visible = True