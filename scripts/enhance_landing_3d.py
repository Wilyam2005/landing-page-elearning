import re

path_index = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\index.html"

with open(path_index, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Tambah CSS 3D & Mobile Perfection Styles
extra_css = '''
        /* --- 3D Depth & Interactive Micro-animations --- */
        .perspective-1000 { perspective: 1000px; }
        .transform-gpu { transform-style: preserve-3d; }
        
        .tilt-card {
            transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease;
            will-change: transform;
        }
        .tilt-card:hover {
            transform: perspective(1000px) rotateX(4deg) rotateY(-3deg) translateY(-8px) scale(1.02);
            box-shadow: 0 25px 50px -12px rgba(180, 83, 9, 0.22);
        }

        /* Ambient floating badge 3D */
        @keyframes float-badge {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-8px) rotate(-1.5deg); }
        }
        .float-badge {
            animation: float-badge 5s ease-in-out infinite;
        }

        /* Glowing Pulse Border */
        @keyframes pulse-border {
            0%, 100% { border-color: rgba(245, 158, 11, 0.4); box-shadow: 0 0 15px rgba(245, 158, 11, 0.2); }
            50% { border-color: rgba(245, 158, 11, 0.8); box-shadow: 0 0 30px rgba(245, 158, 11, 0.4); }
        }
        .glow-active {
            animation: pulse-border 4s infinite;
        }

        /* Glassmorphism Ultra */
        .glass-panel {
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(251, 191, 36, 0.3);
        }
'''

# Sisipkan sebelum </style>
if '.tilt-card' not in html:
    html = html.replace('</style>', extra_css + '\n    </style>')

# 2. Perbaiki Ruang E-Learning Cards agar punya efek Tilt 3D interaktif
old_ruang_grid = r'(<section id="ruang"[\s\S]*?<div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-6 lg:gap-8 cards-container">)([\s\S]*?)(</div>\s*</div>\s*</section>)'

def upgrade_ruang(m):
    cards_block = m.group(2)
    # Ganti class di setiap kartu agar menggunakan tilt-card & shadow 3D
    cards_block = cards_block.replace(
        'class="bg-yellow-50 rounded-2xl p-4 sm:p-6 text-center border border-yellow-100 hover:bg-white hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer group block"',
        'class="glass-panel tilt-card rounded-3xl p-5 sm:p-7 text-center border border-amber-200/80 hover:bg-white cursor-pointer group block shadow-md shadow-amber-900/5 relative overflow-hidden"'
    )
    return m.group(1) + cards_block + m.group(3)

html = re.sub(old_ruang_grid, upgrade_ruang, html, count=1)

# 3. Perbaiki Hero image container agar punya 3D tilt floating badges
old_hero_badge = r'<div class="absolute -bottom-4 left-4 sm:-bottom-6 sm:-left-6 bg-white p-3 sm:p-4 rounded-xl shadow-xl z-20 flex items-center gap-3 sm:gap-4">'
new_hero_badge = r'<div class="absolute -bottom-4 left-4 sm:-bottom-6 sm:-left-6 glass-panel float-badge p-3.5 sm:p-4 rounded-2xl shadow-2xl z-20 flex items-center gap-3 sm:gap-4 border border-amber-200">'

html = html.replace(old_hero_badge, new_hero_badge)

# Tambah badge mengambang di kanan atas hero juga (Siswa Aktif / LMS Resmi)
if 'badge-hero-top' not in html:
    html = html.replace(
        '<img src="IMG_7092.jpg" alt="Siswa Belajar" class="rounded-2xl shadow-2xl z-10 relative object-cover h-64 sm:h-80 md:h-[450px] w-full border-4 border-white">',
        '''<img src="IMG_7092.jpg" alt="Siswa Belajar" class="rounded-3xl shadow-2xl z-10 relative object-cover h-64 sm:h-80 md:h-[450px] w-full border-4 border-white hover:scale-[1.01] transition-transform duration-500">
                    <!-- 3D Floating Tag Top Right -->
                    <div class="absolute -top-4 -right-3 sm:-top-5 sm:-right-5 glass-panel float-badge p-3 rounded-2xl shadow-xl z-20 flex items-center gap-2.5 border border-amber-200 hidden sm:flex" style="animation-delay: -2.5s;">
                        <span class="w-8 h-8 rounded-xl bg-amber-400 text-gray-900 flex items-center justify-center font-bold text-sm shadow-sm"><i class="fa-solid fa-bolt"></i></span>
                        <div>
                            <p class="text-xs font-black text-gray-900">E-Learning 24/7</p>
                            <p class="text-[10px] font-semibold text-gray-500">Akses Kapan Saja</p>
                        </div>
                    </div>'''
    )

# 4. Tambah interaktivitas mouse 3D tilt dinamis di JS untuk desktop
js_3d_tilt = '''
            // Interactive 3D Card Tilt Effect on Mouse Move
            const tiltCards = document.querySelectorAll('.tilt-card, .hover-3d');
            tiltCards.forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    if (window.innerWidth < 768) return; // Non-aktif di mobile agar smooth
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    const rotateX = ((y - centerY) / centerY) * -7;
                    const rotateY = ((x - centerX) / centerX) * 7;
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px) scale(1.02)`;
                });
                card.addEventListener('mouseleave', () => {
                    card.style.transform = '';
                });
            });
'''

if 'Interactive 3D Card Tilt' not in html:
    html = html.replace("document.querySelectorAll('.reveal-bottom, .reveal-left, .reveal-right').forEach(el => scrollObserver.observe(el));", "document.querySelectorAll('.reveal-bottom, .reveal-left, .reveal-right').forEach(el => scrollObserver.observe(el));\n" + js_3d_tilt)

with open(path_index, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with ultra 3D tilt effects & responsiveness!")
