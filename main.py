from Game.Core.game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

# Use for performance testing:
"""
import pstats
import cProfile
cProfile.run("main()", sort="cumtime")"
"""