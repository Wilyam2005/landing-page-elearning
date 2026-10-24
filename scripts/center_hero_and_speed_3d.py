import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. PERBAIKI PADDING HERO SECTION:
# Dari: pt-28 pb-16 sm:pt-32 sm:pb-20 lg:pt-48 lg:pb-32
# Menjadi: min-h-screen pt-20 sm:pt-24 lg:pt-28 pb-12 sm:pb-16 flex items-center
# Di container: dari py-8 sm:py-14 menjadi py-4 sm:py-6
html = html.replace(
    'class="relative pt-28 pb-16 sm:pt-32 sm:pb-20 lg:pt-48 lg:pb-32 bg-gradient-to-br from-amber-50 via-white to-yellow-50 overflow-hidden"',
    'class="relative min-h-[92vh] sm:min-h-screen pt-20 pb-12 sm:pt-24 sm:pb-16 lg:pt-28 lg:pb-20 flex items-center justify-center bg-gradient-to-br from-amber-50/90 via-white to-yellow-50/70 overflow-hidden"'
)

html = html.replace(
    'class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 py-8 sm:py-14"',
    'class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-8 lg:gap-12 py-4 sm:py-6 my-auto"'
)

# 2. PERCEPAT & PERJELAS ANIMASI 3D (dari 16s-22s menjadi 6s-9s, floating 3s, pergerakan lebih dinamis tapi tetap halus)
old_anim_css = r'''        /\* Ambient 3D Geometric Floating Universe \*/
        @keyframes float-geom-1 \{
            0% \{ transform: translateY\(0px\) rotate\(0deg\) scale\(1\); \}
            50% \{ transform: translateY\(-30px\) rotate\(180deg\) scale\(1\.1\); \}
            100% \{ transform: translateY\(0px\) rotate\(360deg\) scale\(1\); \}
        \}
        @keyframes float-geom-2 \{
            0% \{ transform: translateY\(0px\) rotate\(0deg\) scale\(1\); \}
            50% \{ transform: translateY\(28px\) rotate\(-140deg\) scale\(0\.9\); \}
            100% \{ transform: translateY\(0px\) rotate\(-360deg\) scale\(1\); \}
        \}
        @keyframes float-geom-3 \{
            0% \{ transform: translate\(0px, 0px\) rotate\(0deg\); \}
            33% \{ transform: translate\(25px, -20px\) rotate\(60deg\); \}
            66% \{ transform: translate\(-20px, 15px\) rotate\(120deg\); \}
            100% \{ transform: translate\(0px, 0px\) rotate\(0deg\); \}
        \}
        \.anim-geom-1 \{ animation: float-geom-1 16s ease-in-out infinite; \}
        \.anim-geom-2 \{ animation: float-geom-2 22s ease-in-out infinite; \}
        \.anim-geom-3 \{ animation: float-geom-3 19s ease-in-out infinite; \}'''

new_anim_css = '''        /* Ambient 3D Geometric Floating Universe (Lebih cepat, jelas, dinamis & elegan) */
        @keyframes float-geom-1 {
            0% { transform: translateY(0px) rotate(0deg) scale(1); }
            50% { transform: translateY(-24px) rotate(180deg) scale(1.15); }
            100% { transform: translateY(0px) rotate(360deg) scale(1); }
        }
        @keyframes float-geom-2 {
            0% { transform: translateY(0px) rotate(0deg) scale(1); }
            50% { transform: translateY(22px) rotate(-180deg) scale(0.85); }
            100% { transform: translateY(0px) rotate(-360deg) scale(1); }
        }
        @keyframes float-geom-3 {
            0% { transform: translate(0px, 0px) rotate(0deg); }
            33% { transform: translate(20px, -18px) rotate(120deg); }
            66% { transform: translate(-18px, 14px) rotate(240deg); }
            100% { transform: translate(0px, 0px) rotate(360deg); }
        }
        .anim-geom-1 { animation: float-geom-1 7s ease-in-out infinite; }
        .anim-geom-2 { animation: float-geom-2 8.5s ease-in-out infinite; }
        .anim-geom-3 { animation: float-geom-3 6.5s ease-in-out infinite; }'''

html = re.sub(old_anim_css, new_anim_css, html, count=1)

# Percepat floating effect hero image dari 6s ke 3.5s
html = html.replace('.floating {\n            animation: float 6s ease-in-out infinite;\n        }', '.floating {\n            animation: float 3.5s ease-in-out infinite;\n        }')

# Percepat aurora wave dari 12s ke 7s
html = html.replace('.aurora-glow {\n            animation: aurora-wave 12s ease-in-out infinite alternate;\n        }', '.aurora-glow {\n            animation: aurora-wave 6.5s ease-in-out infinite alternate;\n        }')

# Perjelas kontras & kilau elemen geometris 3D
html = html.replace(
    'background: linear-gradient(135deg, rgba(254, 240, 138, 0.45), rgba(245, 158, 11, 0.2));',
    'background: linear-gradient(135deg, rgba(254, 240, 138, 0.75), rgba(245, 158, 11, 0.35));'
)
html = html.replace(
    'border: 4px solid rgba(251, 191, 36, 0.4);',
    'border: 4px solid rgba(245, 158, 11, 0.65);'
)

# 3. Posisikan kembali floating geometry di area hero agar tidak menabrak / terlalu tinggi di atas navbar
old_hero_shapes = r'''            <!-- 3D Geometric Floating Objects \(Cubes, Pills, Rings, Spheres\) -->[\s\S]*?</div>\s*<div class="container mx-auto'''

new_hero_shapes = '''            <!-- 3D Geometric Floating Objects (Posisi Pas, Beranimasi Cepat & Elegan) -->
            <div class="anim-geom-1 geom-pill absolute top-28 left-[5%] w-13 h-13 rounded-2xl hidden md:flex items-center justify-center text-amber-600 shadow-xl text-lg font-bold"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="anim-geom-2 ring-3d absolute top-48 left-[18%] w-11 h-11 hidden lg:block"></div>
            <div class="anim-geom-3 geom-pill absolute bottom-16 left-[34%] w-10 h-10 rounded-2xl hidden md:flex items-center justify-center text-amber-700 shadow-md text-sm"><i class="fa-solid fa-book"></i></div>
            <div class="anim-geom-2 ring-3d absolute top-28 right-[10%] w-14 h-14 hidden md:block" style="border-width: 5px;"></div>
            <div class="anim-geom-1 geom-pill absolute bottom-16 right-[6%] w-12 h-12 rounded-2xl hidden md:flex items-center justify-center text-amber-600 shadow-xl text-base"><i class="fa-solid fa-laptop"></i></div>
            <div class="anim-geom-3 ring-3d absolute bottom-6 right-[28%] w-8 h-8 hidden sm:block"></div>
            <div class="anim-geom-1 absolute top-20 left-[48%] w-3.5 h-3.5 rounded-full bg-amber-400 hidden sm:block shadow-md"></div>
            <div class="anim-geom-2 absolute bottom-28 left-[14%] w-4 h-4 rounded-full bg-yellow-400 hidden sm:block shadow-md"></div>
        </div>

        <div class="container mx-auto'''

html = re.sub(old_hero_shapes, new_hero_shapes, html, count=1)

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("Hero section is now perfectly vertically centered on open, with faster & vibrant 3D animations!")
