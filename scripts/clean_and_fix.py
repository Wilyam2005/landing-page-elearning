import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"
path_history = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\history-peserta.html"

# --- 1. PROSES INDEX.HTML ---
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# A. Hapus menu navigasi 'Testimoni' (Desktop & Mobile)
html = re.sub(r'<li><a href="#testimoni"[^>]*>Testimoni</a></li>\s*', '', html)

# B. Hapus Section 5 (Testimoni) dan Section 6 (Informasi & Berita)
# Cari dari <!-- 5. Section Testimoni --> sampai sebelum <!-- 7. Section FAQ (Accordion) -->
pattern_sections = r'<!-- 5\. Section Testimoni -->[\s\S]*?(?=<!-- 7\. Section FAQ \(Accordion\) -->)'
if re.search(pattern_sections, html):
    html = re.sub(pattern_sections, '', html)
    print("Berhasil menghapus Section Testimoni & Informasi Berita!")
else:
    print("Warning: Pola section tidak cocok!")

# Ganti nomor section FAQ jika ada (opsional / estetik)
html = html.replace('<!-- 7. Section FAQ (Accordion) -->', '<!-- 5. Section FAQ (Accordion) -->')

# C. Hapus kata-kata simulasi pada index.html di section history
html = html.replace(
    'Dashboard juga menyediakan pratinjau progres pembelajaran berlabel simulasi; verifikasi kelulusan memerlukan laporan resmi Moodle.',
    'Dashboard juga menyediakan rekap progres pembelajaran peserta didik yang terarsip secara transparan dan mudah dipantau.'
)
html = html.replace(
    '<li><i class="fa-solid fa-check text-yellow-400 mr-2"></i> Pratinjau progres kursus dengan data simulasi berlabel</li>',
    '<li><i class="fa-solid fa-check text-yellow-400 mr-2"></i> Rekap dan pemantauan progres kursus peserta didik</li>'
)

# D. Update tautan login & tombol agar target="_blank" dan jelas
# Pastikan semua link login ke elearningalc.online punya target="_blank" dan rel="noopener noreferrer"
html = html.replace(
    'href="https://elearningalc.online/login/index.php"',
    'href="https://elearningalc.online/login/index.php" target="_blank" rel="noopener noreferrer"'
)

# E. Buat Card "Ruang E-Learning" (Ruang Guru, Ruang Murid, Ruang Ujian, Ruang Materi) bisa diklik langsung menuju login LMS
card_pattern = r'<div class="bg-yellow-50 rounded-2xl p-4 sm:p-6 text-center border border-yellow-100 hover:bg-white cursor-pointer group">'
card_replacement = '<a href="https://elearningalc.online/login/index.php" target="_blank" rel="noopener noreferrer" class="bg-yellow-50 rounded-2xl p-4 sm:p-6 text-center border border-yellow-100 hover:bg-white hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer group block">'
html = html.replace(card_pattern, card_replacement)
# Ubah penutup div kartu yang sesuai menjadi </a>
# Karena kartu punya struktur: <div class="bg-yellow-50...">...</div>, setelah diganti pembukanya, penutupnya disesuaikan
# Untuk amannya, kita bisa lakukan dengan regex per kartu di dalam grid
grid_ruang_regex = r'(<div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-6 lg:gap-8 cards-container">)([\s\S]*?)(</div>\s*</div>\s*</section>)'

def replace_cards(m):
    cards_html = m.group(2)
    cards = re.split(r'(?=<div class="bg-yellow-50|<a href="https://elearningalc\.online)', cards_html)
    new_cards = []
    for c in cards:
        if not c.strip():
            continue
        c = re.sub(r'^<div class="bg-yellow-50[^"]*"', card_replacement[:-1], c)
        c = re.sub(r'</div>\s*$', '</a>\n                ', c.rstrip())
        new_cards.append(c)
    return m.group(1) + '\n                ' + ''.join(new_cards) + '\n            ' + m.group(3)

# Cek apakah replacement awal tadi sudah jalan atau jalankan replace_cards
if '<a href="https://elearningalc.online/login/index.php"' in html:
    # Ganti </div> penutup kartu yang berpasangan
    html = re.sub(
        r'(<a href="https://elearningalc\.online/login/index\.php"[^>]*>[\s\S]*?<p class="text-sm text-gray-600 hidden md:block">[^<]*</p>\s*)</div>',
        r'\1</a>',
        html
    )

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)
print("Selesai memproses index.html!")

# --- 2. PROSES HISTORY-PESERTA.HTML (Sisa kata simulasi) ---
with open(path_history, "r", encoding="utf-8") as f:
    h_html = f.read()

h_html = h_html.replace('<span class="sr-only">Cari akun simulasi</span>', '<span class="sr-only">Cari akun peserta</span>')
h_html = h_html.replace('aria-label="Filter tahun ajaran simulasi"', 'aria-label="Filter tahun ajaran"')
h_html = h_html.replace('aria-label="Filter jenjang simulasi"', 'aria-label="Filter jenjang"')
h_html = h_html.replace('aria-label="Filter status simulasi"', 'aria-label="Filter status"')

with open(path_history, "w", encoding="utf-8") as f:
    f.write(h_html)
print("Selesai memproses history-peserta.html!")
