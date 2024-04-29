import pygame

# Inicializar pygame
pygame.init()

# Obtener la cantidad de joysticks disponibles
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    print("Se encontraron {} joysticks.".format(num_joysticks))
    # Inicializar el primer joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Ciclo principal
    while True:
        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Obtener las coordenadas X e Y del joystick
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        # Imprimir las coordenadas
        print("Coordenada X: {:.2f}, Coordenada Y: {:.2f}".format(x_axis, y_axis))

else:
    print("No se encontraron joysticks conectados.")










