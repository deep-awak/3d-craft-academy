import subprocess
import sys
import os

def install_ai_dependencies():
    print("--- MPFB AI DEPENDENCY INSTALLER ---")

    # 1. Identifier le chemin du Python de Blender
    python_exe = sys.executable
    print(f"Python utilisé: {python_exe}")

    # 2. Liste des packages à installer
    packages = ["pip", "opencv-python", "mediapipe"]

    try:
        # Mise à jour de pip d'abord
        print("Mise à jour de pip...")
        subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

        for package in packages:
            print(f"Installation de {package}...")
            # --user permet d'installer même sans droits admin dans certains cas
            subprocess.check_call([python_exe, "-m", "pip", "install", package])

        print("\n✅ SUCCÈS : Toutes les dépendances AI sont installées !")
        print("Veuillez REDÉMARRER Blender pour activer les modules.")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ ERREUR lors de l'installation : {e}")
        print("\nCONSEIL : Si vous êtes sur Windows, essayez de lancer Blender en tant qu'ADMINISTRATEUR et relancez ce script.")
    except Exception as e:
        print(f"\n❌ ERREUR INCONNUE : {e}")

if __name__ == "__main__":
    install_ai_dependencies()
