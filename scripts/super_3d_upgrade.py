import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"
with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Tambah CSS 3D Super Keren & Multi-Device Smooth Animations
super_3d_css = '''
        /* --- Super 3D World & Interactive Glass Physics --- */
        .card-3d-wrap {
            perspective: 1200px;
            transform-style: preserve-3d;
        }

        .card-3d-inner {
            transition: transform 0.4s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.4s ease;
            transform-style: preserve-3d;
            will-change: transform;
        }

        .card-3d-inner:hover {
            transform: translateY(-10px) rotateX(6deg) rotateY(-4deg) scale(1.025);
            box-shadow: 0 30px 60px -15px rgba(245, 158, 11, 0.25), 0 0 25px rgba(251, 191, 36, 0.15);
        }

        /* Ambient 3D Geometric Floating Universe */
        @keyframes float-geom-1 {
            0% { transform: translateY(0px) rotate(0deg) scale(1); }
            50% { transform: translateY(-30px) rotate(180deg) scale(1.1); }
            100% { transform: translateY(0px) rotate(360deg) scale(1); }
        }
        @keyframes float-geom-2 {
            0% { transform: translateY(0px) rotate(0deg) scale(1); }
            50% { transform: translateY(28px) rotate(-140deg) scale(0.9); }
            100% { transform: translateY(0px) rotate(-360deg) scale(1); }
        }
        @keyframes float-geom-3 {
            0% { transform: translate(0px, 0px) rotate(0deg); }
            33% { transform: translate(25px, -20px) rotate(60deg); }
            66% { transform: translate(-20px, 15px) rotate(120deg); }
            100% { transform: translate(0px, 0px) rotate(0deg); }
        }
        .anim-geom-1 { animation: float-geom-1 16s ease-in-out infinite; }
        .anim-geom-2 { animation: float-geom-2 22s ease-in-out infinite; }
        .anim-geom-3 { animation: float-geom-3 19s ease-in-out infinite; }

        /* Floating 3D Donut / Ring */
        .ring-3d {
            border: 4px solid rgba(251, 191, 36, 0.4);
            border-top-color: rgba(245, 158, 11, 0.85);
            border-radius: 50%;
            box-shadow: 0 10px 30px -5px rgba(245, 158, 11, 0.25);
        }

        /* Dynamic Aurora Glow in Background */
        @keyframes aurora-wave {
            0% { filter: blur(50px) hue-rotate(0deg); transform: scale(1) translateY(0px); }
            50% { filter: blur(65px) hue-rotate(25deg); transform: scale(1.2) translateY(-25px); }
            100% { filter: blur(50px) hue-rotate(0deg); transform: scale(1) translateY(0px); }
        }
        .aurora-glow {
            animation: aurora-wave 12s ease-in-out infinite alternate;
        }

        /* 3D Button Bounce on Hover */
        .btn-3d {
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 6px 0 #d97706, 0 12px 25px rgba(217, 119, 6, 0.3);
        }
        .btn-3d:hover {
            transform: translateY(-3px);
            box-shadow: 0 9px 0 #d97706, 0 18px 30px rgba(217, 119, 6, 0.4);
        }
        .btn-3d:active {
            transform: translateY(3px);
            box-shadow: 0 3px 0 #d97706, 0 6px 15px rgba(217, 119, 6, 0.2);
        }
'''

if '.card-3d-wrap' not in html:
    html = html.replace('</style>', super_3d_css + '\n    </style>')

# 2. Upgrade Seluruh Background Hero agar Penuh dengan Elemen 3D Spektakuler yang Hidup
hero_mesh_old = r'<div class="absolute inset-0 pointer-events-none overflow-hidden">[\s\S]*?</div>\s*<div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 py-6 sm:py-10">'

hero_mesh_new = '''<div class="absolute inset-0 pointer-events-none overflow-hidden">
            <!-- Aurora Ambient Glow -->
            <div class="absolute -top-20 right-0 w-[550px] h-[550px] bg-gradient-to-bl from-yellow-300/40 via-amber-200/30 to-transparent rounded-full aurora-glow translate-x-1/4 -translate-y-1/4"></div>
            <div class="absolute -bottom-24 -left-20 w-[500px] h-[500px] bg-gradient-to-tr from-amber-300/30 via-yellow-200/35 to-transparent rounded-full aurora-glow animation-delay-2000"></div>
            <div class="absolute top-1/2 left-1/3 w-80 h-80 bg-yellow-200/20 rounded-full blur-3xl wave-glow"></div>
            
            <!-- 3D Geometric Floating Objects (Cubes, Pills, Rings, Spheres) -->
            <div class="anim-geom-1 geom-pill absolute top-16 left-[6%] w-14 h-14 rounded-2xl hidden md:flex items-center justify-center text-amber-500/70 shadow-lg text-lg"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="anim-geom-2 ring-3d absolute top-40 left-[22%] w-10 h-10 hidden lg:block"></div>
            <div class="anim-geom-3 geom-pill absolute bottom-20 left-[38%] w-11 h-11 rounded-2xl hidden md:flex items-center justify-center text-amber-600/70 shadow-md text-sm"><i class="fa-solid fa-book"></i></div>
            <div class="anim-geom-2 ring-3d absolute top-24 right-[12%] w-14 h-14 hidden md:block" style="border-width: 5px;"></div>
            <div class="anim-geom-1 geom-pill absolute bottom-24 right-[8%] w-12 h-12 rounded-2xl hidden md:flex items-center justify-center text-yellow-600/70 shadow-lg text-base"><i class="fa-solid fa-laptop"></i></div>
            <div class="anim-geom-3 ring-3d absolute bottom-8 right-[32%] w-7 h-7 hidden sm:block"></div>
            <div class="anim-geom-1 absolute top-10 left-[50%] w-3 h-3 rounded-full bg-amber-400/50 hidden sm:block"></div>
            <div class="anim-geom-2 absolute bottom-36 left-[18%] w-4 h-4 rounded-full bg-yellow-400/40 hidden sm:block"></div>
        </div>

        <div class="container mx-auto px-4 md:px-8 relative z-10 flex flex-col lg:flex-row items-center gap-12 py-8 sm:py-14">'''

html = re.sub(hero_mesh_old, hero_mesh_new, html, count=1)

# 3. Upgrade Section Layanan Unggulan agar Kartu Memiliki Efek 3D Card Depth
html = html.replace(
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 cards-container">',
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 cards-container card-3d-wrap">'
)
html = html.replace(
    '<div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:border-yellow-300 group">',
    '<div class="card-3d-inner bg-white/95 backdrop-blur-md p-8 rounded-3xl shadow-lg shadow-gray-200/50 border border-amber-100/80 hover:border-amber-300 group transition-all">'
)

# 4. Beri Background 3D Floating Geometry di Section Layanan juga
old_layanan_header = r'<section id="layanan" class="py-20 bg-gray-50 border-t border-gray-100 overflow-hidden">'
new_layanan_header = '''<section id="layanan" class="py-20 sm:py-24 bg-gradient-to-b from-gray-50 via-amber-50/20 to-gray-50 border-t border-gray-100 relative overflow-hidden">
        <!-- Floating 3D Geometric Objects -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="anim-geom-2 ring-3d absolute top-12 left-[5%] w-12 h-12 opacity-60 hidden md:block"></div>
            <div class="anim-geom-1 geom-pill absolute bottom-12 right-[6%] w-10 h-10 rounded-2xl opacity-60 hidden md:block"></div>
            <div class="anim-geom-3 ring-3d absolute top-28 right-[20%] w-8 h-8 opacity-40 hidden sm:block"></div>
        </div>'''

html = re.sub(old_layanan_header, new_layanan_header, html, count=1)

# 5. Beri Background 3D Floating Geometry di Section FAQ
old_faq_header = r'<section id="faq" class="py-20 bg-white">'
new_faq_header = '''<section id="faq" class="py-20 sm:py-24 bg-gradient-to-b from-white via-amber-50/20 to-white relative overflow-hidden">
        <!-- Floating 3D Geometric Shapes -->
        <div class="absolute inset-0 pointer-events-none overflow-hidden">
            <div class="anim-geom-1 geom-pill absolute top-16 right-[8%] w-12 h-12 rounded-2xl opacity-50 hidden md:block"></div>
            <div class="anim-geom-2 ring-3d absolute bottom-16 left-[7%] w-11 h-11 opacity-50 hidden md:block"></div>
        </div>'''

html = re.sub(old_faq_header, new_faq_header, html, count=1)

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("Landing page is now packed with rich 3D animations and full multi-device harmony!")
