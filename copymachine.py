from datetime import datetime
import pyperclip

# Ambil tanggal hari ini dalam format "04 Desember 2025"
tanggal = datetime.now().strftime("%d %B %Y")

# Template strukturnya
template = f"""{tanggal}
    -

> Kendala
    -

> Solusi yang sudah dicoba
    -

"""

# Copy ke clipboard
pyperclip.copy(template)

# Optional: tampilkan di console juga
print(template)
