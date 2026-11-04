#!/usr/bin/env python3
"""Usage: python3 make_qr.py https://<username>.github.io/<repo>/  [out.png]"""
import sys, qrcode
url = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else "qr.png"
q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=20, border=4)
q.add_data(url); q.make(fit=True)
q.make_image(fill_color="#14151a", back_color="white").save(out); print("saved", out, "for", url)
