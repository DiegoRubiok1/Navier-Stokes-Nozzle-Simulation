"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""
from fluidsimulation import FluidSimulation
import pygame

# TODO: define update() and draw()

class Graph:
    """Graphical implement of a 2d cage with water"""
    def __init__(self):
        
        # Fluid simulation instance
        self.simulation = FluidSimulation(
            rho=1000, mhu=0.001, 
            p_zero=10, p_gradient=-1, 
            Ny=100, Nx=100, 
            height=1, width=1
            )
        # Initial pressure matrix
        self.simulation.p_matrix(
            self.simulation.Nx, self.simulation.Ny, self.simulation.p_zero
            )
        
        # Pygame initialize
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Fluid simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.fps = 3

    
    def handle_events(self):
        """Handle de events in screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        """Actualize the logic of the simulation."""

        # Pressure gradient zone actualize
        self.simulation.set_preassure_gradient(self.simulation.p_gradient)

        # Set the walls with velocity 0
        self.simulation.update_walls()

        # Update pressure grid
        self.simulation.update_pressure()

        # Update velocity grid
        self.simulation.update_velocity()

        

    def draw(self):
        """Draws elements in screen"""
        self.screen.fill(0)
        
        self.draw_grid()

    def draw_grid(self):
        """Draws the pressure grid with 8 pixel squares"""
        for i in range(len(self.simulation.p)):
            for j in range(len(self.simulation.p[i])):
                
                color = (self.simulation.p[i][j], 0, 0) # Color pressure
                size = 8    # Size
                pos = (size*j, size*i)  # Position
                # Draw rectangle
                pygame.draw.rect(self.screen, color, pos[0], pos[1], size, size)
        

    def run(self):
        """Executes the main loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == "__main__":
    graph = Graph()
    graph.run()



