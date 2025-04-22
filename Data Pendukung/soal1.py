def deteksi_hama(gejala):
    if "daun menguning" in gejala and "tanaman layu" in gejala:
        return "Kutu Daun"
    elif "bercak hitam" in gejala:
        return "Jamur"
    elif "daun berlubang" in gejala:
        return "Ulat Grayak"
    elif "daun menguning" in gejala and "bercak hitam" in gejala:
        return "Tungau"
    else:
        return "Hama tidak teridentifikasi"

# Contoh penggunaan
# Gejala: bercak hitam → berdasarkan aturan, ini berarti jenis hama adalah "Jamur"
# jika ingin gejala yang lain tulis gejalanya yang ada di atas. "contoh, bercak hitam berarti jenis hama Jamur"
gejala_input = ["daun menguning", "tanaman layu"] 
print("Jenis hama:", deteksi_hama(gejala_input))

