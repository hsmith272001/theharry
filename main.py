import pygame
import random

display_width = 1200
display_height = 1200
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Catan!")
game_colour = (56, 184, 212)
image_sizes = (150,150)

#images
hills_image = pygame.image.load("Images/Hills_low.png")
mountains_image = pygame.image.load("Images/mountains_low.png")
forests_image = pygame.image.load("Images/forestPNG.png")
fields_image = pygame.image.load("Images/fields_low.png")
desert_image = pygame.image.load("Images/dessertPNG.png")
pasture_image = pygame.image.load("Images/PasturePNG.png")

#sizing down the images
mountains_image = pygame.transform.scale(mountains_image, image_sizes)
hills_image = pygame.transform.scale(hills_image, image_sizes)
forests_image = pygame.transform.scale(forests_image, image_sizes)
fields_image = pygame.transform.scale(fields_image, image_sizes)
desert_image = pygame.transform.scale(desert_image, image_sizes)
pasture_image = pygame.transform.scale(pasture_image, image_sizes)

#coordinates
img_coord1 = (((display_height/2)-(image_sizes[0]/2)), ((display_width/2)-(image_sizes[1]/2)))
img_coord2 = (img_coord1[0], (img_coord1[1] - image_sizes[1] - 7))
img_coord3 = (img_coord2[0], (img_coord2[1] - image_sizes[1] - 7))
img_coord4 = (img_coord1[0], (img_coord1[1] + image_sizes[1] + 7))
img_coord5 = (img_coord4[0], (img_coord4[1] + image_sizes[1] + 7))
img_coord6 = ((img_coord1[0] - (image_sizes[0] - 27)), (img_coord2[1] - (image_sizes[1] / 2)))
img_coord7 = (img_coord6[0], (img_coord6[1] + image_sizes[1] + 7))
img_coord8 = (img_coord7[0], (img_coord7[1] + image_sizes[1] + 7))
img_coord9 = (img_coord8[0], (img_coord8[1] + image_sizes[1] + 7))
img_coord10 = ((img_coord1[0] + (image_sizes[0] - 27)), (img_coord2[1] - (image_sizes[1] / 2)))
img_coord11 = (img_coord10[0], (img_coord10[1] + image_sizes[1] + 7))
img_coord12 = (img_coord11[0], (img_coord11[1] + image_sizes[1] + 7))
img_coord13 = (img_coord12[0], (img_coord12[1] + image_sizes[1] + 7))
img_coord14 = ((img_coord6[0] - (image_sizes[0] - 27)), (img_coord7[1] - (image_sizes[1] / 2)))
img_coord15 = (img_coord14[0], (img_coord14[1] + image_sizes[1] + 7))
img_coord16 = (img_coord15[0], (img_coord15[1] + image_sizes[1] + 7))
img_coord17 = ((img_coord11[0] + (image_sizes[0] - 27)), img_coord2[1])
img_coord18 = (img_coord17[0], img_coord1[0])
img_coord19 = (img_coord18[0], img_coord4[1])



def random_board():
    TILE_TYPES = {
        0: hills_image,
        1: mountains_image,
        2: forests_image,
        3: fields_image,
        4: pasture_image,
        5: desert_image
    }

    tile_selection = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
    random.shuffle(tile_selection)

    COORDS = {
        0: img_coord1,
        1: img_coord2,
        2: img_coord3,
        3: img_coord4,
        4: img_coord5,
        5: img_coord6,
        6: img_coord7,
        7: img_coord8,
        8: img_coord9,
        9: img_coord10,
        10: img_coord11,
        11: img_coord12,
        12: img_coord13,
        13: img_coord14,
        14: img_coord15,
        15: img_coord16,
        16: img_coord17,
        17: img_coord18,
        18: img_coord19
    }

    coords_selection = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    random.shuffle(coords_selection)

    for i in range(19):
        load(TILE_TYPES[tile_selection[i]], COORDS[coords_selection[i]])

def load(image, coord):

    gameDisplay.blit(image, coord)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gameDisplay.fill(game_colour)
        random_board()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

'''TILE_TYPES = {
    0: pygame.image.load("Images/Hills_low.png"),
    1: pygame.image.load("Images/mountains_low.png"),
    2: pygame.image.load("Images/forestPNG.png"),
    3: pygame.image.load("Images/fields_low.png"),
    4: pygame.image.load("Images/dessertPNG.png"),
    5: pygame.image.load("Images/PasturePNG.png")
}'''