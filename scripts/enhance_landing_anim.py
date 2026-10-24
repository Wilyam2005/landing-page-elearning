import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update 1000+ Siswa to 435+ Peserta
html = html.replace(
    '<p class="text-sm font-bold text-gray-800">1000+ Siswa</p>',
    '<p class="text-sm font-extrabold text-gray-900">435+ Peserta</p>'
)
html = html.replace(
    '<p class="text-xs text-gray-500">Telah bergabung</p>',
    '<p class="text-[11px] font-semibold text-gray-500">Paket A, B, & C Terdaftar</p>'
)

# 2. Add Animated 3D Floating Particles & Background Waves
bg_anim_css = '''
        /* --- Animated Dynamic Background Particles & Mesh --- */
        @keyframes float-particle {
            0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
            33% { transform: translateY(-30px) translateX(25px) rotate(120deg); }
            66% { transform: translateY(15px) translateX(-20px) rotate(240deg); }
            100% { transform: translateY(0px) translateX(0px) rotate(360deg); }
        }
        .anim-particle-1 { animation: float-particle 14s ease-in-out infinite; }
        .anim-particle-2 { animation: float-particle 18s ease-in-out infinite reverse; }
        .anim-particle-3 { animation: float-particle 22s ease-in-out infinite 3s; }

        @keyframes wave-glow {
            0%, 100% { opacity: 0.35; transform: scale(1) rotate(0deg); }
            50% { opacity: 0.65; transform: scale(1.15) rotate(10deg); }
        }
        .wave-glow { animation: wave-glow 10s ease-in-out infinite alternate; }

        /* Icon Micro-hover Bounce & 3D Tilt */
        .icon-bounce-hover {
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
        }
        .icon-bounce-hover:hover {
            transform: scale(1.18) rotate(-6deg);
        }
'''

if 'anim-particle-1' not in html:
    html = html.replace('</style>', bg_anim_css + '\n    </style>')

# 3. Add background decorative geometric 3D shapes to Hero
hero_old_blob = r'''        <!-- Decorative element (Animasi Blob Bergerak) -->
        <div class="absolute top-0 right-0 w-96 h-96 bg-yellow-200 rounded-full mix-blend-multiply filter blur-3xl opacity-40 translate-x-1/2 -translate-y-1/2 animate-blob"></div>
        <div class="absolute bottom-0 left-0 w-72 h-72 bg-yellow-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 -translate-x-1/2 translate-y-1/2 animate-blob animation-delay-2000"></div>'''

hero_new_blob = '''        <!-- Decorative Animated 3D Background Mesh & Floating Particles -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-gradient-to-bl from-yellow-300/30 to-amber-200/20 rounded-full blur-3xl wave-glow translate-x-1/3 -translate-y-1/3"></div>
            <div class="absolute bottom-0 left-0 w-[450px] h-[450px] bg-gradient-to-tr from-amber-300/25 to-yellow-200/20 rounded-full blur-3xl wave-glow animation-delay-2000 -translate-x-1/4 translate-y-1/4"></div>
            
            <!-- 3D Geometric Floating Shapes -->
            <div class="anim-particle-1 absolute top-24 left-[12%] w-10 h-10 border-2 border-yellow-400/40 rounded-2xl rotate-12 backdrop-blur-sm hidden md:block"></div>
            <div class="anim-particle-2 absolute bottom-28 left-[45%] w-7 h-7 bg-amber-300/30 rounded-full hidden md:block"></div>
            <div class="anim-particle-3 absolute top-36 right-[15%] w-8 h-8 border-2 border-amber-500/30 rotate-45 hidden md:block"></div>
        </div>'''

html = html.replace(hero_old_blob, hero_new_blob)

# 4. Icon Animations di Ruang & Layanan agar pas dan tidak glitch
html = html.replace('group-hover:rotate-6', 'icon-bounce-hover')
html = html.replace('group-hover:-rotate-6', 'icon-bounce-hover')
html = html.replace('group-hover:scale-110', 'icon-bounce-hover')

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated landing page background animations and 435+ peserta badge successfully!")
