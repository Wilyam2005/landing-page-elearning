import re

path_history = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\history-peserta.html"

with open(path_history, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update GATE section with clean modern Light Theme, clear input styling, and reliable toggle-pass
old_gate = r'<!-- GATE -->[\s\S]*?<!-- APP -->'

new_gate = '''<!-- GATE -->
    <section id="gate" class="relative min-h-screen flex items-center justify-center px-4 py-10">
        <div class="w-full max-w-md bg-white border border-amber-200/80 rounded-3xl p-7 sm:p-9 shadow-2xl shadow-amber-900/10 relative z-10">
            <div class="flex items-center gap-3.5 mb-6">
                <img src="fav icon logo.jpg" alt="ALC" class="w-13 h-13 rounded-full object-cover border-2 border-amber-300 shadow-md">
                <div>
                    <span class="inline-block text-[11px] font-extrabold uppercase tracking-wider text-amber-700 bg-amber-100 px-2.5 py-0.5 rounded-full mb-1">Akses Terbatas</span>
                    <h1 class="text-xl sm:text-2xl font-black text-gray-900 tracking-tight">History Peserta PKBM</h1>
                </div>
            </div>
            
            <p class="text-gray-600 text-sm mb-6 leading-relaxed">
                Data peserta didik Paket A/B/C PKBM Assyuro ALC. Masukkan password admin untuk membuka visualisasi dan riwayat data.
            </p>

            <form id="gate-form" class="space-y-4">
                <div>
                    <label for="gate-password" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Password Admin</label>
                    <div class="relative flex items-center">
                        <input id="gate-password" type="password" autocomplete="current-password" required class="w-full rounded-2xl bg-gray-50 border border-gray-300 px-4 py-3.5 pr-12 text-gray-900 placeholder:text-gray-400 focus:bg-white focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 font-medium transition" placeholder="Masukkan password...">
                        <button type="button" id="toggle-pass" class="absolute right-3 w-9 h-9 flex items-center justify-center text-gray-500 hover:text-gray-800 transition rounded-xl hover:bg-gray-200" aria-label="Tampilkan password">
                            <i class="fa-regular fa-eye text-base"></i>
                        </button>
                    </div>
                </div>

                <div class="bg-amber-50 border border-amber-200 rounded-xl p-3 text-xs text-amber-800 flex items-center gap-2">
                    <i class="fa-solid fa-circle-info text-amber-600 text-sm"></i>
                    <span>Default Password: <strong>Admin123</strong> (huruf 'A' kapital)</span>
                </div>

                <p id="gate-error" class="hidden text-sm font-semibold text-rose-600 bg-rose-50 border border-rose-200 p-3 rounded-xl flex items-center gap-2">
                    <i class="fa-solid fa-triangle-exclamation"></i> Password salah. Silakan coba lagi.
                </p>

                <button type="submit" class="w-full rounded-2xl bg-gradient-to-r from-yellow-400 to-amber-500 text-gray-950 font-extrabold py-3.5 hover:shadow-lg hover:shadow-yellow-500/30 hover:-translate-y-0.5 active:translate-y-0 transition duration-200 text-base">
                    Masuk Dashboard
                </button>

                <a href="index.html" class="inline-flex items-center justify-center w-full text-center text-sm font-semibold text-gray-500 hover:text-amber-700 transition gap-1.5 pt-1">
                    <i class="fa-solid fa-arrow-left text-xs"></i> Kembali ke Beranda
                </a>
            </form>
        </div>
    </section>

    <!-- APP -->'''

html = re.sub(old_gate, new_gate, html, count=1)

# 2. Periksa Script toggle-pass dan unlock logic
# Pastikan toggle-pass support klik di icon atau button, dan case-insensitive / trim password
old_js_gate = r"""        $('toggle-pass')\.addEventListener\('click', \(\) => \{[\s\S]*?\}\);

        \$'\('gate-form'\)\.addEventListener\('submit', \(e\) => \{[\s\S]*?\}\);"""

new_js_gate = """        const togglePassBtn = $('toggle-pass');
        if (togglePassBtn) {
            togglePassBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const input = $('gate-password');
                const isPassword = input.type === 'password';
                input.type = isPassword ? 'text' : 'password';
                togglePassBtn.innerHTML = isPassword 
                    ? '<i class="fa-regular fa-eye-slash text-base"></i>' 
                    : '<i class="fa-regular fa-eye text-base"></i>';
            });
        }

        $('gate-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const entered = ($('gate-password').value || '').trim();
            // Mendukung Admin123 atau admin123
            if (entered === PASSWORD || entered.toLowerCase() === PASSWORD.toLowerCase()) {
                sessionStorage.setItem(SESSION_KEY, '1');
                $('gate-error').classList.add('hidden');
                unlock();
            } else {
                $('gate-error').classList.remove('hidden');
            }
        });"""

# Check if old gate script pattern matches
if "$('toggle-pass').addEventListener('click'" in html:
    # replace using regex
    html = re.sub(
        r"\$('toggle-pass')\.addEventListener\('click'[\s\S]*?\}\);\s*\$('gate-form')\.addEventListener\('submit'[\s\S]*?\}\);",
        new_js_gate,
        html
    )
    print("Updated JS gate logic!")
else:
    print("Warning: toggle-pass not found in JS")

with open(path_history, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated history-peserta.html gate UI and logic!")
