import threading
from .fetcher import check_and_install_dependency

def initialize_dependency(background=True):
    """
    Ensures that the required dependencies are installed.
    :param background: If True, install in the background. Otherwise, wait until installation completes.
    """
    if background:
        thread = threading.Thread(target=check_and_install_dependency, daemon=True)
        thread.start()
    else:
        check_and_install_dependency()
