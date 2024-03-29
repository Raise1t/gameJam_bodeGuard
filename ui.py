import pygame
from item import Item
from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface,UI_BG_COLOR, bg_rect )

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR, current_rect,2)

    def display(self,player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, (255,0,0))
        for x in 10, 100, 190, 280:
            self.selection_box(x,678)
        
        selectedRect = pygame.Rect(12 + 90*player.selectedSlot, 680, ITEM_BOX_SIZE-3, ITEM_BOX_SIZE-3)
        pygame.draw.rect(self.display_surface, (160, 160, 160), selectedRect)
        self.displayInventory(player)
        self.showEffects(player)


    def selection_box(self,left,top):
        bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,2)

    def displayInventory(self, player):
        font = pygame.font.SysFont("monospace", 20, bold = True)
        x = 17
        for key, value in player.getInventory().items():
            pygame.Surface.blit(self.display_surface, pygame.transform.rotozoom(Item.items[key].getImage(), 0, 2), (x, 684))
            self.display_surface.blit(font.render(str(value), 1, (0, 0, 0)), (x+45, 730))
            x += 90
    
    def howDidWeGetHere(self):
        pass

    def showEffects(self, player):
        font = pygame.font.SysFont("Monospace", 30, bold = True)
        y = 5
        for key, value in player.effects.items():
            if value:
                width, height = font.size(key)
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, pygame.Rect(WIDTH - (width + 15), y, width + 10, height + 5))
                self.display_surface.blit(font.render(key, 1, UI_EFFECT_TEXT_COLOR), (WIDTH - (width + 10), y + 5))
                y = y + height + 10

