import qrcode

def generar_qr(texto, nombre_archivo="codigo_qr.png"):
    """
    Genera un código QR a partir del texto proporcionado y lo guarda como una imagen PNG.

    :param texto: Texto o enlace que se codificará en el código QR.
    :param nombre_archivo: Nombre del archivo de imagen de salida.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)
    print(f"Código QR guardado como {nombre_archivo}")


if __name__ == "__main__":
    texto = input("Introduce el texto o URL para generar el código QR: ")
    generar_qr(texto)