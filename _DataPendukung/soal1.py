def deteksi_hama(gejala):
    if "daun menguning" in gejala and "tanaman layu" in gejala:
        return "Kutu Daun"  # Aturan 1
    elif "daun menguning" in gejala and "bercak hitam" in gejala:
        return "Tungau"     # Aturan 4
    elif "bercak hitam" in gejala:
        return "Jamur"      # Aturan 2
    elif "daun berlubang" in gejala:
        return "Ulat Grayak"  # Aturan 3
    
    else:
        return "Hama tidak teridentifikasi"

# Contoh input gejala
gejala_input = ["bercak hitam"]  # ← Kamu bisa ganti ini sesuai gejala yang ingin diuji

# Cetak hasil deteksi hama
hasil = deteksi_hama(gejala_input)
print("Jenis hama:", hasil)
