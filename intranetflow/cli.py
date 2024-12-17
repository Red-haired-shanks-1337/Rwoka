import argparse
from . import initialize_dependency

def main():
    parser = argparse.ArgumentParser(description="Rwoka CLI tool")
    parser.add_argument(
        "--bg",
        type=str,
        choices=["True", "False"],
        default="True",
        help="Specify whether to run dependency installation in the background (default: True)."
    )
    args = parser.parse_args()

    # Initialize dependency based on user input
    background = args.bg == "True"
    initialize_dependency(background=background)

    # Add the rest of your CLI tool logic here
    print("Rwoka CLI is running. Add your main script logic.")
