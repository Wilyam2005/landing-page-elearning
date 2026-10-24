import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Perbaiki Hero Section: hilangkan overflow-hidden pada container dalam agar badge floating tidak terpotong sama sekali
# Dari:
# <div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 overflow-hidden py-4">
# Menjadi:
# <div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 py-8 sm:py-12">
html = html.replace(
    '<div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 overflow-hidden py-4">',
    '<div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 py-6 sm:py-10">'
)

# Sesuaikan posisi badge top right & bottom left agar pas dan proporsional di dalam container
old_badges_block = r'''                    <!-- 3D Floating Tag Top Right -->
                    <div class="absolute -top-4 -right-3 sm:-top-5 sm:-right-5 glass-panel float-badge p-3 rounded-2xl shadow-xl z-20 flex items-center gap-2.5 border border-amber-200 hidden sm:flex" style="animation-delay: -2.5s;">
                        <span class="w-8 h-8 rounded-xl bg-amber-400 text-gray-900 flex items-center justify-center font-bold text-sm shadow-sm"><i class="fa-solid fa-bolt"></i></span>
                        <div>
                            <p class="text-xs font-black text-gray-900">E-Learning 24/7</p>
                            <p class="text-[10px] font-semibold text-gray-500">Akses Kapan Saja</p>
                        </div>
                    </div>
                    <!-- Floating Badge -->
                    <div class="absolute -bottom-4 left-4 sm:-bottom-6 sm:-left-6 glass-panel float-badge p-3.5 sm:p-4 rounded-2xl shadow-2xl z-20 flex items-center gap-3 sm:gap-4 border border-amber-200">
                        <div class="bg-yellow-100 p-3 rounded-full text-yellow-600">
                            <i class="fa-solid fa-users text-xl"></i>
                        </div>
                        <div>
                            <p class="text-sm font-extrabold text-gray-900">435+ Peserta</p>
                            <p class="text-[11px] font-semibold text-gray-500">Paket A, B, & C Terdaftar</p>
                        </div>
                    </div>'''

new_badges_block = '''                    <!-- 3D Floating Tag Top Right (Safe Offset, No Clipping) -->
                    <div class="absolute top-3 right-3 sm:-top-4 sm:-right-4 glass-panel float-badge px-3.5 py-2.5 rounded-2xl shadow-xl z-20 flex items-center gap-2.5 border border-amber-300/80" style="animation-delay: -2.5s;">
                        <span class="w-8 h-8 rounded-xl bg-gradient-to-tr from-amber-400 to-yellow-300 text-gray-900 flex items-center justify-center font-bold text-xs shadow-sm"><i class="fa-solid fa-bolt"></i></span>
                        <div>
                            <p class="text-xs font-extrabold text-gray-900">E-Learning 24/7</p>
                            <p class="text-[10px] font-medium text-gray-500">Akses Kapan Saja</p>
                        </div>
                    </div>
                    <!-- 3D Floating Badge Bottom Left (Safe Offset, No Clipping) -->
                    <div class="absolute -bottom-5 left-3 sm:-bottom-6 sm:-left-6 glass-panel float-badge p-3 sm:p-4 rounded-2xl shadow-2xl z-20 flex items-center gap-3 sm:gap-4 border border-amber-300/80">
                        <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-yellow-100 to-amber-100 flex items-center justify-center text-amber-700 shadow-inner">
                            <i class="fa-solid fa-users text-lg"></i>
                        </div>
                        <div>
                            <p class="text-sm sm:text-base font-black text-gray-900">435+ Peserta</p>
                            <p class="text-[11px] font-semibold text-gray-500">Paket A, B, & C Terdaftar</p>
                        </div>
                    </div>'''

html = html.replace(old_badges_block, new_badges_block)

# 2. Tambah Animasi 3D Background yang Lebih Banyak, Proporsional, & Hidup di Seluruh Landing Page
advanced_3d_css = '''
        /* --- Enhanced 3D Ambient Universe & Floating Cubes --- */
        @keyframes rotate-3d-cube {
            0% { transform: perspective(800px) rotateX(0deg) rotateY(0deg) translateY(0px); }
            50% { transform: perspective(800px) rotateX(180deg) rotateY(180deg) translateY(-25px); }
            100% { transform: perspective(800px) rotateX(360deg) rotateY(360deg) translateY(0px); }
        }
        .cube-3d-1 { animation: rotate-3d-cube 20s infinite linear; }
        .cube-3d-2 { animation: rotate-3d-cube 26s infinite linear reverse; }
        .cube-3d-3 { animation: rotate-3d-cube 18s infinite linear 3s; }

        @keyframes pulse-mesh {
            0%, 100% { transform: scale(1) translate(0px, 0px); opacity: 0.45; }
            50% { transform: scale(1.12) translate(20px, -20px); opacity: 0.75; }
        }
        .mesh-glow { animation: pulse-mesh 12s ease-in-out infinite alternate; }

        /* Floating Interactive 3D Geometry */
        .geom-pill {
            background: linear-gradient(135deg, rgba(254, 240, 138, 0.45), rgba(245, 158, 11, 0.2));
            backdrop-filter: blur(8px);
            border: 1px solid rgba(245, 158, 11, 0.35);
            box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.15);
        }
'''

if 'rotate-3d-cube' not in html:
    html = html.replace('</style>', advanced_3d_css + '\n    </style>')

# Tambahkan elemen geometris 3D yang tersebar artistik di Background Hero
old_hero_particles = r'''            <!-- 3D Geometric Floating Shapes -->
            <div class="anim-particle-1 absolute top-24 left-[12%] w-10 h-10 border-2 border-yellow-400/40 rounded-2xl rotate-12 backdrop-blur-sm hidden md:block"></div>
            <div class="anim-particle-2 absolute bottom-28 left-[45%] w-7 h-7 bg-amber-300/30 rounded-full hidden md:block"></div>
            <div class="anim-particle-3 absolute top-36 right-[15%] w-8 h-8 border-2 border-amber-500/30 rotate-45 hidden md:block"></div>'''

new_hero_particles = '''            <!-- 3D Geometric Floating Shapes (Artist-Grade, Well-Balanced) -->
            <div class="cube-3d-1 geom-pill absolute top-20 left-[8%] w-12 h-12 rounded-2xl hidden md:block"></div>
            <div class="cube-3d-2 geom-pill absolute bottom-24 left-[40%] w-8 h-8 rounded-xl hidden md:block"></div>
            <div class="cube-3d-3 geom-pill absolute top-32 right-[8%] w-11 h-11 rounded-2xl hidden md:block"></div>
            <div class="anim-particle-1 absolute bottom-12 right-[25%] w-6 h-6 border-2 border-amber-400/50 rounded-full hidden sm:block"></div>
            <div class="anim-particle-2 absolute top-12 left-[48%] w-5 h-5 bg-yellow-400/30 rounded-lg rotate-12 hidden sm:block"></div>'''

html = html.replace(old_hero_particles, new_hero_particles)

# 3. Beri Background 3D subtle juga di Section Ruang & Layanan
ruang_bg = '''    <section id="ruang" class="py-20 sm:py-24 bg-gradient-to-b from-white via-amber-50/30 to-white relative overflow-hidden">
        <!-- Floating 3D subtle shapes -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="cube-3d-2 geom-pill absolute top-12 right-[5%] w-10 h-10 rounded-2xl opacity-60 hidden md:block"></div>
            <div class="cube-3d-1 geom-pill absolute bottom-10 left-[4%] w-8 h-8 rounded-xl opacity-60 hidden md:block"></div>
        </div>'''

html = re.sub(r'<section id="ruang" class="py-20 bg-white">', ruang_bg, html, count=1)

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html fully upgraded with non-clipped badges and rich 3D animations!")
