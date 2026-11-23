"""
Script rápido para comprobar la conexión con la API de Google Imagen 3 (Google AI Studio).
Genera 1 imagen de prueba y confirma si la clave de API y la cuota están activas.
"""

import os
import sys

def load_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key and os.path.exists('.env'):
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('GEMINI_API_KEY='):
                        key = line.split('=', 1)[1].strip().strip('"').strip("'")
                        break
        except Exception:
            pass
    return key

def test_imagen():
    api_key = load_key()
    if not api_key:
        print("[ERROR] No se encontro GEMINI_API_KEY.")
        print("Configurala con:")
        print("  - PowerShell: $env:GEMINI_API_KEY = 'AIzaSy...'")
        print("  - O crea un archivo .env con: GEMINI_API_KEY=AIzaSy...")
        sys.exit(1)

    print(f"Clave detectada: {api_key[:6]}...{api_key[-4:]}")
    print("Conectando con Google AI Studio (modelo: imagen-3.0-generate-002)...")

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt='Commercial studio footwear photograph of a white sneaker on pure white background',
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="1:1",
                output_mime_type="image/jpeg"
            )
        )

        if response.generated_images:
            os.makedirs('scratch', exist_ok=True)
            out_test = 'scratch/test_imagen_output.jpg'
            with open(out_test, 'wb') as f:
                f.write(response.generated_images[0].image.image_bytes)
            print(f"[EXITO] Conexion confirmada! Imagen de prueba guardada en: {out_test}")
        else:
            print("[RESPUESTA VACIA] La API no devolvio imagenes.")
    except Exception as e:
        print(f"[ERROR DE API]: {e}")
        print("\nConsejos:")
        print("1. Verifica que tu API Key sea de https://aistudio.google.com/")
        print("2. Imagen 3 requiere que el proyecto en Google Cloud tenga facturación (Pay-As-You-Go) vinculada.")

if __name__ == '__main__':
    test_imagen()
