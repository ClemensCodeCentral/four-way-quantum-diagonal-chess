"""A set of chess pieces that can easily be extended"""
import pygame


class Piece:
    """A chess piece that has a given location"""

    def __init__(self, image_path, x: int = 0, y: int = 0, ) -> None:
        self.x = x  # The on-screen location, not the board position
        self.y = y
        self.image = pygame.image.load(image_path).convert()

    def move(self, start):
        """Return the end position with a given start position, simulating a move"""
        end = ...
        # TODO: Return the (x, y) where this piece would be after moving
        return end

    def draw(self):
        pygame.Surface.blit(self.image(self.x, self.y))

# TODO: Create more pieces that extend Piece