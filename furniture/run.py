from method.main import run
import furniture.env
from furniture.config import create_parser
from method.config import add_method_arguments

if __name__ == "__main__":
    # default arguments
    parser = create_parser()

    # arguments related to RL/IL methods
    add_method_arguments(parser)

    # change default values
    parser.set_defaults(wandb_project="furniture")

    # execute training code in method/main.py
    run(parser)


