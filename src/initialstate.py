import gamestate
import gameobject

class InitialState(gamestate.GameState):
    def __init__(self):
        super().game_objects.append(gameobject.GameObject())
        super().game_objects.append(gameobject.GameObject())
        super().game_objects.append(gameobject.GameObject())

    def ss_update(self, dt):
        pass

    def ss_render(self,dt):
        pass
    
    def ss_process_input(self):
        pass