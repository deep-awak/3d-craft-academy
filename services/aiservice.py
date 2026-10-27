import subprocess
import sys
import os
from .logservice import LogService

_LOG = LogService.get_logger("services.aiservice")

class AiService:
    """
    Service for handling AI dependencies and external library management for MPFB.
    """

    @staticmethod
    def ensure_dependencies():
        """
        Check for and install required AI libraries (mediapipe, opencv-python).
        Returns True if all dependencies are available, False otherwise.
        """
        dependencies = ["mediapipe", "cv2"]
        missing = []

        for dep in dependencies:
            try:
                __import__(dep if dep != "cv2" else "cv2")
            except ImportError:
                missing.append(dep)

        if not missing:
            return True

        _LOG.info(f"Missing AI dependencies: {missing}. Attempting installation...")

        try:
            # Use the current Blender Python executable to install missing packages
            pip_cmd = [sys.executable, "-m", "pip", "install"]

            # Map internal names to pip package names
            pip_packages = []
            for m in missing:
                if m == "cv2":
                    pip_packages.append("opencv-python")
                else:
                    pip_packages.append(m)

            pip_cmd.extend(pip_packages)

            _LOG.debug(f"Running command: {' '.join(pip_cmd)}")
            subprocess.check_call(pip_cmd)
            _LOG.info("AI dependencies installed successfully.")
            return True
        except Exception as e:
            _LOG.error(f"Failed to install AI dependencies: {e}")
            return False

    @staticmethod
    def get_ai_model_path(model_name):
        """
        Placeholder for resolving model paths via LocationService.
        """
        # This will be integrated with LocationService and Preferences in later steps
        return None
