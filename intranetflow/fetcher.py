import subprocess
import sys
import importlib.util

DEPENDENCY_NAME = "thredrequest"
GITHUB_PACKAGE = "git+https://github.com/username/thredrequest.git"

def is_installed(package_name):
    """
    Checks if a package is installed by trying to import it.
    """
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def check_and_install_dependency():
    """
    Checks if the dependency is installed, and installs it if missing.
    """
    if not is_installed(DEPENDENCY_NAME):
        try:
            print(f"Dependency '{DEPENDENCY_NAME}' not found. Installing...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", GITHUB_PACKAGE],
                stdout=subprocess.DEVNULL,  # Use DEVNULL to make it silent
                stderr=subprocess.DEVNULL
            )
            if not is_installed(DEPENDENCY_NAME):
                raise RuntimeError(f"Failed to install {DEPENDENCY_NAME}.")
        except Exception as e:
            print(f"Error installing {DEPENDENCY_NAME}: {e}")
            raise
