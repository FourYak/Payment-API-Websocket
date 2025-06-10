import sys
sys.path.append("../")

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix = Pix()
    
    # create a payment
    payment_data = pix.create_payment(base_dir="../")

    assert "bank_payment_id" in payment_data
    assert "qr_code_path" in payment_data

    qr_code_path = payment_data['qr_code_path']
    assert os.path.isfile(f"../static/img/{qr_code_path}.png")