import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # simulating payment on the "bank"
        bank_payment_id = str(uuid.uuid4())  # Simulating a bank payment ID generation

        #simulating codigo_copia_cola_
        hash_payment = f'hash_payment_{bank_payment_id}'

        #simulating qr code generation
        img = qrcode.make(hash_payment)

        # Save the QR code image to a file
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")


        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}