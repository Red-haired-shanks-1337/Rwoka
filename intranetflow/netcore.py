import time
import threading
from rich.progress import Progress

def print_progress_with_spinner(message, duration=3):
    """
    Simulates progress messages with a spinner, styled like a pip installation process.
    """
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0

    while time.time() < end_time:
        print(f"{message} {spinner[idx % len(spinner)]}", end="\r")
        idx += 1
        time.sleep(0.2)
    print(" " * len(message), end="\r")  # Clear line

def pip_installation_simulation():
    """
    Simulates a package installation process in a style similar to PyPI's pip.
    """
    print("Collecting netcore package==1.0.0")
    print_progress_with_spinner("  Downloading netcore package.tar.gz (4.5 MB)", 3)
    print("  Downloading netcore package.tar.gz (4.5 MB) done")
    print("  Preparing metadata (setup.py)")
    print_progress_with_spinner("  Preparing metadata", 2)
    print("  Preparing metadata (setup.py) done")

    print("Installing collected packages: netcore package")

    # Using the Rich Progress Bar to simulate the "Installing" part
    with Progress() as progress:
        task = progress.add_task("Installing", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.1)

    print("Successfully installed netcore package-1.0.0")

def main():
    """
    Main entry point for the simulation.
    """
    print("Starting installation process...\n")
    thread = threading.Thread(target=pip_installation_simulation)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
