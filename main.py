import OpenGL
OpenGL.ERROR_CHECKING = False

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    
    return texture_id

def draw_face(texture_id, vertices):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(*vertices[0])
    glTexCoord2f(1, 0); glVertex3f(*vertices[1])
    glTexCoord2f(1, 1); glVertex3f(*vertices[2])
    glTexCoord2f(0, 1); glVertex3f(*vertices[3])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 2)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 1)
    
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Lab 3 - Variant 7 (Textured Cube)")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)

    textures = [
        load_texture("1.jpg"),
        load_texture("2.jpg"),
        load_texture("3.jpg"),
        load_texture("4.jpg"),
        load_texture("5.jpg"),
        load_texture("6.jpg")
    ]

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 1, 1, 0) 

        draw_face(textures[0], [(-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1)])
        draw_face(textures[1], [(-1, -1, -1), (-1,  1, -1), ( 1,  1, -1), ( 1, -1, -1)])
        draw_face(textures[2], [(-1, -1, -1), (-1, -1,  1), (-1,  1,  1), (-1,  1, -1)])
        draw_face(textures[3], [( 1, -1,  1), ( 1,  1,  1), ( 1,  1, -1), ( 1, -1, -1)])
        draw_face(textures[4], [(-1,  1, -1), (-1,  1,  1), ( 1,  1,  1), ( 1,  1, -1)])
        draw_face(textures[5], [(-1, -1, -1), ( 1, -1, -1), ( 1, -1,  1), (-1, -1,  1)])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()