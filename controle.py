import pygame
import vgamepad as vg
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle detectado")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

gamepad = vg.VX360Gamepad()

print("Controle detectado:", joystick.get_name())

def clamp(v):
    return max(-1.0, min(1.0, v))

while True:
    pygame.event.pump()

    # Analógicos
    lx = clamp(joystick.get_axis(0))
    ly = clamp(-joystick.get_axis(1))
    rx = clamp(joystick.get_axis(2))
    ry = clamp(-joystick.get_axis(3))

    gamepad.left_joystick_float(lx, ly)
    gamepad.right_joystick_float(rx, ry)

    # Botões (ajuste se necessário)
    if joystick.get_button(0):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if joystick.get_button(1):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if joystick.get_button(2):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if joystick.get_button(3):
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    gamepad.update()
    time.sleep(0.01)