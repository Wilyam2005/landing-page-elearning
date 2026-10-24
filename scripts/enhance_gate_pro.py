import re

path_history = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\history-peserta.html"

with open(path_history, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Perbaiki body & gate section agar proporsional, eye-catching, logo bulat rapih, teks default password dihapus
# Kita buat Gate Section berdesain 3D Glassmorphism mewah
new_gate_html = '''<!-- GATE -->
    <section id="gate" class="relative min-h-screen flex items-center justify-center px-4 py-8 sm:py-12">
        <div class="w-full max-w-md bg-white/95 backdrop-blur-xl border border-amber-200/80 rounded-3xl p-6 sm:p-9 shadow-2xl shadow-amber-900/10 relative z-10 transition-all">
            <!-- Header Brand -->
            <div class="flex items-center gap-4 mb-6 pb-6 border-b border-gray-100">
                <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-tr from-amber-400 to-yellow-200 p-0.5 shadow-md shrink-0 flex items-center justify-center overflow-hidden">
                    <img src="fav icon logo.jpg" alt="Logo ALC" class="w-full h-full object-cover rounded-[14px]">
                </div>
                <div>
                    <span class="inline-block text-[10px] font-extrabold uppercase tracking-widest text-amber-800 bg-amber-100 border border-amber-200 px-2.5 py-0.5 rounded-full mb-1">Akses Terbatas</span>
                    <h1 class="text-xl sm:text-2xl font-black text-gray-900 tracking-tight leading-tight">History Peserta</h1>
                    <p class="text-xs font-semibold text-gray-500">PKBM Assyuro Lombok Creative</p>
                </div>
            </div>
            
            <p class="text-gray-600 text-xs sm:text-sm mb-6 leading-relaxed">
                Silakan masukkan password admin untuk membuka visualisasi statistik dan data riwayat peserta didik.
            </p>

            <form id="gate-form" class="space-y-4">
                <div>
                    <label for="gate-password" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Password Admin</label>
                    <div class="relative flex items-center">
                        <input id="gate-password" type="password" autocomplete="current-password" required class="w-full rounded-2xl bg-gray-50/90 border border-gray-200 px-4 py-3.5 pr-12 text-gray-900 placeholder:text-gray-400 focus:bg-white focus:outline-none focus:ring-2 focus:ring-amber-400 focus:border-amber-400 font-medium transition text-sm shadow-inner" placeholder="Masukkan password admin...">
                        <button type="button" id="toggle-pass" class="absolute right-2.5 w-9 h-9 flex items-center justify-center text-gray-400 hover:text-gray-700 transition rounded-xl hover:bg-gray-100 active:scale-95" aria-label="Tampilkan password">
                            <i class="fa-regular fa-eye text-sm"></i>
                        </button>
                    </div>
                </div>

                <p id="gate-error" class="hidden text-xs sm:text-sm font-semibold text-rose-600 bg-rose-50 border border-rose-200 p-3 rounded-xl flex items-center gap-2 animate-bounce">
                    <i class="fa-solid fa-circle-exclamation text-rose-500"></i> Password tidak sesuai. Silakan coba lagi.
                </p>

                <button type="submit" id="btn-submit-gate" class="w-full rounded-2xl bg-gradient-to-r from-yellow-400 via-amber-400 to-yellow-500 text-gray-950 font-extrabold py-3.5 hover:shadow-xl hover:shadow-yellow-500/25 hover:-translate-y-0.5 active:translate-y-0 transition duration-200 text-sm sm:text-base flex items-center justify-center gap-2 cursor-pointer">
                    <span>Masuk Dashboard</span>
                    <i class="fa-solid fa-arrow-right text-xs"></i>
                </button>

                <div class="pt-2 text-center">
                    <a href="index.html" class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-semibold text-gray-500 hover:text-amber-700 transition">
                        <i class="fa-solid fa-arrow-left text-xs"></i> Kembali ke Beranda
                    </a>
                </div>
            </form>
        </div>
    </section>'''

# Replace gate section
html = re.sub(r'<!-- GATE -->[\s\S]*?<!-- APP -->', new_gate_html + '\n\n    <!-- APP -->', html, count=1)

# 2. Perbaiki Script Toggle Pass dan Form Submit agar selalu berfungsi
new_script_gate = '''        const $ = (id) => document.getElementById(id);

        // Toggle Password Visibility
        const toggleBtn = $('toggle-pass');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', function(e) {
                e.preventDefault();
                const input = $('gate-password');
                const isPassword = input.type === 'password';
                input.type = isPassword ? 'text' : 'password';
                this.innerHTML = isPassword 
                    ? '<i class="fa-regular fa-eye-slash text-sm"></i>' 
                    : '<i class="fa-regular fa-eye text-sm"></i>';
            });
        }

        // Form Submit Handler
        const gateForm = $('gate-form');
        if (gateForm) {
            gateForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const passInput = $('gate-password');
                const entered = (passInput ? passInput.value : '').trim();
                
                // Menerima 'Admin123' atau 'admin123'
                if (entered === PASSWORD || entered.toLowerCase() === PASSWORD.toLowerCase()) {
                    sessionStorage.setItem(SESSION_KEY, '1');
                    const gateErr = $('gate-error');
                    if (gateErr) gateErr.classList.add('hidden');
                    unlock();
                } else {
                    const gateErr = $('gate-error');
                    if (gateErr) gateErr.classList.remove('hidden');
                    if (passInput) passInput.focus();
                }
            });
        }'''

# Replace in script
html = re.sub(
    r"const \$ = \(id\) => document\.getElementById\(id\);[\s\S]*?\$\('gate-form'\)\.addEventListener\('submit'[\s\S]*?\}\);",
    new_script_gate,
    html,
    count=1
)

with open(path_history, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated history-peserta.html gate layout & script!")
