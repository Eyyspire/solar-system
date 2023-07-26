import sys
from Display.Displayer import SolarSystemDisplayer
from ursina import *

from SolarSystem.SolarSystem import SolarSystem

def main():

    s = SolarSystem()

    # fig = plt.figure()


    # for _ in range(350):
    #     sun = s.bodies[0]
    #     plt.plot(sun.pos[0], sun.pos[1], 'yo')
    #     for p in s.bodies[1:5]:
    #         plt.plot(p.pos[0], p.pos[1], 'ro')
    #         if p.name == "Earth": print(p.mass)
    #     s.move()
    #     # plt.plot(s.bodies[9].pos[0], s.bodies[9].pos[1], 'bo')
    #     #plt.pause(0.05)


    # plt.show()

    app = Ursina()

    window.title = 'Solar system'                
    window.borderless = False              
    window.fullscreen = False               
    window.exit_button.visible = False      
    window.fps_counter.enabled = False    

    d = SolarSystemDisplayer(s)

    app.run()

if __name__ == "__main__":
    sys.exit(main())