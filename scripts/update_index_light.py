import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"

with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Section History to Light Theme & 3D Interactive
old_history_sec = r'<!-- History Peserta PKBM -->[\s\S]*?</section>'

new_history_sec = '''<!-- History Peserta PKBM -->
    <section id="history" class="py-20 sm:py-24 bg-gradient-to-br from-amber-50 via-white to-yellow-50/60 text-gray-800 relative overflow-hidden border-t border-b border-amber-100">
        <!-- Floating 3D Orbs / Ambient -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="absolute -top-24 -right-16 w-80 h-80 bg-yellow-300/25 rounded-full blur-3xl animate-blob"></div>
            <div class="absolute -bottom-20 -left-16 w-96 h-96 bg-amber-400/20 rounded-full blur-3xl animate-blob animation-delay-2000"></div>
        </div>

        <div class="container mx-auto px-4 md:px-8 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <!-- Left Info with 3D Reveal -->
                <div class="reveal-left">
                    <div class="inline-flex items-center gap-2 bg-yellow-100 text-primaryDark font-bold px-4 py-1.5 rounded-full text-xs uppercase tracking-wider mb-4 border border-yellow-200 shadow-sm">
                        <i class="fa-solid fa-database"></i> Data Internal PKBM
                    </div>
                    <h2 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-gray-900 mb-6 tracking-tight leading-tight">
                        History Peserta Didik <span class="text-transparent bg-clip-text bg-gradient-to-r from-primaryDark to-yellow-600">Paket A, B, dan C</span>
                    </h2>
                    <p class="text-gray-600 text-base sm:text-lg leading-relaxed mb-8">
                        Arsip lengkap peserta PKBM Assyuro ALC tahun ajaran 2024/2025 hingga 2026/2027 dengan pencarian interaktif, grafik demografi, serta rekap pemantauan progres kursus peserta didik.
                    </p>
                    
                    <div class="space-y-3.5 text-gray-700 mb-9 text-sm sm:text-base">
                        <div class="flex items-center gap-3">
                            <span class="w-7 h-7 rounded-full bg-amber-100 text-primaryDark flex items-center justify-center shrink-0 font-bold text-xs"><i class="fa-solid fa-check"></i></span>
                            <span>Grafik interaktif gender, jenjang, kelas, usia, dan sebaran alamat</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="w-7 h-7 rounded-full bg-amber-100 text-primaryDark flex items-center justify-center shrink-0 font-bold text-xs"><i class="fa-solid fa-check"></i></span>
                            <span>Pencarian instan + kartu responsif khusus pengguna HP</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="w-7 h-7 rounded-full bg-amber-100 text-primaryDark flex items-center justify-center shrink-0 font-bold text-xs"><i class="fa-solid fa-check"></i></span>
                            <span>Fitur ekspor laporan CSV lengkap dan rekap progres kursus</span>
                        </div>
                    </div>

                    <a href="history-peserta.html" class="inline-flex w-full sm:w-auto justify-center items-center gap-3 bg-gradient-to-r from-yellow-400 to-amber-500 text-gray-900 px-8 py-4 rounded-full font-extrabold hover:shadow-xl hover:shadow-yellow-500/25 hover:-translate-y-1 transition-all duration-300 btn-shine text-base">
                        <span>Buka Dashboard History</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>

                <!-- Right 3D Cards Grid -->
                <div class="grid grid-cols-2 gap-4 sm:gap-6 reveal-right">
                    <!-- Stat Card 1 -->
                    <div class="bg-white/90 backdrop-blur-md border border-amber-200/80 rounded-3xl p-6 sm:p-7 shadow-lg shadow-amber-900/5 hover-3d group">
                        <div class="w-12 h-12 rounded-2xl bg-amber-100 text-primaryDark flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-users"></i>
                        </div>
                        <p class="text-3xl sm:text-4xl font-extrabold text-gray-900 mb-1 tracking-tight">435</p>
                        <p class="text-xs sm:text-sm font-semibold text-gray-500">Catatan Peserta</p>
                    </div>

                    <!-- Stat Card 2 -->
                    <div class="bg-white/90 backdrop-blur-md border border-amber-200/80 rounded-3xl p-6 sm:p-7 shadow-lg shadow-amber-900/5 hover-3d group">
                        <div class="w-12 h-12 rounded-2xl bg-yellow-100 text-amber-700 flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-calendar-days"></i>
                        </div>
                        <p class="text-3xl sm:text-4xl font-extrabold text-amber-600 mb-1 tracking-tight">3</p>
                        <p class="text-xs sm:text-sm font-semibold text-gray-500">Tahun Ajaran</p>
                    </div>

                    <!-- Stat Card 3 -->
                    <div class="bg-white/90 backdrop-blur-md border border-sky-100 rounded-3xl p-6 sm:p-7 shadow-lg shadow-sky-900/5 hover-3d group">
                        <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-600 flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-mars"></i>
                        </div>
                        <p class="text-3xl sm:text-4xl font-extrabold text-sky-600 mb-1 tracking-tight">189</p>
                        <p class="text-xs sm:text-sm font-semibold text-gray-500">Laki-laki</p>
                    </div>

                    <!-- Stat Card 4 -->
                    <div class="bg-white/90 backdrop-blur-md border border-pink-100 rounded-3xl p-6 sm:p-7 shadow-lg shadow-pink-900/5 hover-3d group">
                        <div class="w-12 h-12 rounded-2xl bg-pink-100 text-pink-600 flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform shadow-inner">
                            <i class="fa-solid fa-venus"></i>
                        </div>
                        <p class="text-3xl sm:text-4xl font-extrabold text-pink-600 mb-1 tracking-tight">246</p>
                        <p class="text-xs sm:text-sm font-semibold text-gray-500">Perempuan</p>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

html = re.sub(old_history_sec, new_history_sec, html, count=1)

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html history section to light 3D theme!")
