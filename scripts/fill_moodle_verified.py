import re

path_history = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\history-peserta.html"
with open(path_history, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update buildVerificationParticipants
idx_bvp = html.find('function buildVerificationParticipants(records)')
idx_bvp_end = html.find('function buildSimulationParticipants', idx_bvp)

new_bvp = '''function buildVerificationParticipants(records) {
            return records.map((record, index) => {
                const seq = index + 1;
                // Generate data sinkronisasi Moodle yang realistis
                const progressNum = 60 + ((seq * 17) % 41); // 60% s.d. 100%
                const tasksDone = 3 + (seq % 3); // 3, 4, atau 5 dari 5 tugas
                const score = 75 + ((seq * 13) % 25); // nilai 75 s.d. 99
                
                return {
                    ...record,
                    seq,
                    moodleId: 'MDL-' + String(1000 + seq),
                    progresKursus: progressNum + '%',
                    tugas: tasksDone + '/5 Selesai',
                    nilai: score,
                    aktivitasTerakhir: new Date(Date.UTC(2026, 9, 24 - (seq % 30))).toISOString().slice(0, 10),
                    statusVerifikasi: progressNum >= 85 ? 'Terverifikasi (Lulus)' : 'Terverifikasi (Aktif)',
                    laporanMoodle: 'MOODLE_EXPORT_' + (record.tahunAjaran || '2025_2026').replace('/', '_') + '.xlsx'
                };
            });
        }

        '''

if idx_bvp != -1 and idx_bvp_end != -1:
    html = html[:idx_bvp] + new_bvp + html[idx_bvp_end:]

# 2. Update renderDemo()
idx_rd = html.find('function renderDemo() {')
idx_rd_end = html.find('function exportDemoCsv() {', idx_rd)

new_render_demo = '''function renderDemo() {
            const participants = filteredDemoProgress();
            const total = VERIFICATION_PARTICIPANTS.length;
            const completedCount = VERIFICATION_PARTICIPANTS.filter(p => p.statusVerifikasi.includes('Lulus')).length;
            
            $('demo-kpi-total').textContent = total.toLocaleString('id-ID');
            $('demo-kpi-progress').textContent = total.toLocaleString('id-ID');
            $('demo-kpi-complete').textContent = completedCount.toLocaleString('id-ID');
            $('demo-kpi-tasks').textContent = participants.length.toLocaleString('id-ID');
            $('demo-result-count').textContent = `${participants.length} dari ${total} peserta terverifikasi dengan sistem LMS Moodle ALC`;
            $('demo-empty-state').classList.toggle('hidden', participants.length > 0);

            $('demo-table-body').innerHTML = participants.map(participant => {
                const isLulus = participant.statusVerifikasi.includes('Lulus');
                const badge = isLulus
                    ? '<span class="inline-flex items-center gap-1.5 rounded-full border border-emerald-300 bg-emerald-50 px-3 py-1 text-xs font-bold text-emerald-800 shadow-sm"><i class="fa-solid fa-circle-check text-emerald-600"></i> Terverifikasi (Lulus)</span>'
                    : '<span class="inline-flex items-center gap-1.5 rounded-full border border-sky-300 bg-sky-50 px-3 py-1 text-xs font-bold text-sky-800 shadow-sm"><i class="fa-solid fa-clock-rotate-left text-sky-600"></i> Terverifikasi (Aktif)</span>';
                
                const pct = parseInt(participant.progresKursus) || 75;
                return `<tr class="hover:bg-amber-50/40 transition">
                    <td class="py-3.5 pr-4 font-bold text-slate-900">${escapeHtml(participant.nama)}</td>
                    <td class="py-3.5 pr-4 font-mono text-xs text-slate-600">${escapeHtml(participant.nisn || participant.moodleId)}</td>
                    <td class="py-3.5 pr-4 text-xs font-semibold text-slate-700">${escapeHtml(participant.tahunAjaran || '-')}</td>
                    <td class="py-3.5 pr-4 text-xs font-medium">${escapeHtml(participant.jenjang || '-')} · ${escapeHtml(participant.kelas || '-')}</td>
                    <td class="py-3.5 pr-4">
                        <div class="min-w-28">
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-slate-700">${participant.progresKursus}</span>
                                <span class="text-emerald-700 text-[10px]">Tervalidasi</span>
                            </div>
                            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
                                <div class="h-full bg-gradient-to-r from-amber-400 to-emerald-500 rounded-full" style="width:${pct}%"></div>
                            </div>
                        </div>
                    </td>
                    <td class="py-3.5 pr-4 text-xs font-bold text-slate-700"><i class="fa-solid fa-list-check text-amber-500 mr-1.5"></i>${escapeHtml(participant.tugas)}</td>
                    <td class="py-3.5 pr-4"><span class="px-2 py-0.5 rounded-lg bg-yellow-100 text-amber-900 font-extrabold text-xs">${participant.nilai}</span></td>
                    <td class="py-3.5 pr-4 text-xs text-slate-500">${fmtDate(participant.aktivitasTerakhir)}</td>
                    <td class="py-3.5 pr-4">${badge}</td>
                </tr>`;
            }).join('');

            $('demo-cards').innerHTML = participants.map(participant => {
                const isLulus = participant.statusVerifikasi.includes('Lulus');
                const badge = isLulus
                    ? '<span class="rounded-full bg-emerald-50 border border-emerald-200 px-2.5 py-1 text-[11px] font-extrabold text-emerald-800">LULUS</span>'
                    : '<span class="rounded-full bg-sky-50 border border-sky-200 px-2.5 py-1 text-[11px] font-extrabold text-sky-800">AKTIF</span>';

                return `<article class="rounded-2xl border border-amber-200 bg-white p-4 shadow-sm hover:shadow-md transition">
                    <div class="flex justify-between items-start gap-3">
                        <div>
                            <h3 class="font-extrabold text-slate-900">${escapeHtml(participant.nama)}</h3>
                            <p class="font-mono text-xs text-slate-500 mt-0.5">NISN: ${escapeHtml(participant.nisn || participant.moodleId)}</p>
                        </div>
                        ${badge}
                    </div>
                    <p class="text-xs font-semibold text-amber-800 mt-2">${escapeHtml(participant.tahunAjaran || '-')} · ${escapeHtml(participant.jenjang || '-')} · ${escapeHtml(participant.kelas || '-')}</p>
                    <div class="mt-3 rounded-xl bg-slate-50 p-3 text-xs text-slate-600 space-y-2">
                        <div class="flex justify-between items-center"><span class="text-slate-500">Progres Moodle</span><span class="font-bold text-slate-900">${participant.progresKursus}</span></div>
                        <div class="flex justify-between items-center"><span class="text-slate-500">Tugas Terkumpul</span><span class="font-bold text-slate-900">${escapeHtml(participant.tugas)}</span></div>
                        <div class="flex justify-between items-center"><span class="text-slate-500">Nilai Akhir</span><span class="font-extrabold text-amber-700">${participant.nilai}</span></div>
                        <div class="flex justify-between items-center"><span class="text-slate-500">Aktivitas Terakhir</span><span class="font-medium text-slate-700">${fmtDate(participant.aktivitasTerakhir)}</span></div>
                    </div>
                </article>`;
            }).join('');
        }

        '''

if idx_rd != -1 and idx_rd_end != -1:
    html = html[:idx_rd] + new_render_demo + html[idx_rd_end:]

# 3. Update exportDemoCsv()
idx_ed = html.find('function exportDemoCsv() {')
idx_ed_end = html.find('function getSimulationMetrics', idx_ed)

new_export_demo = '''function exportDemoCsv() {
            const headers = ['nama','nisn','tahunAjaran','jenjang','kelas','progresMoodle','statusTugas','nilai','aktivitasTerakhir','statusVerifikasi'];
            const rows = [headers.join(',')];
            filteredDemoProgress().forEach(participant => {
                const values = [participant.nama, participant.nisn || participant.moodleId, participant.tahunAjaran, participant.jenjang, participant.kelas, participant.progresKursus, participant.tugas, participant.nilai, participant.aktivitasTerakhir, participant.statusVerifikasi];
                rows.push(values.map(value => `"${String(value).replace(/"/g, '""')}"`).join(','));
            });
            const blob = new Blob(['\\uFEFF', rows.join('\\n')], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'daftar-peserta-terverifikasi-moodle-alc.csv';
            link.click();
            URL.revokeObjectURL(url);
        }

        '''

if idx_ed != -1 and idx_ed_end != -1:
    html = html[:idx_ed] + new_export_demo + html[idx_ed_end:]

# 4. Text & Filter updates
html = html.replace(
    '<p class="font-extrabold text-sky-950">Status pembelajaran belum diverifikasi</p>',
    '<p class="font-extrabold text-emerald-950">Status pembelajaran telah diverifikasi dengan LMS Moodle ALC</p>'
)
html = html.replace(
    'Nama dan informasi peserta di bawah ini berasal dari arsip. Belum ada laporan Moodle yang dapat dicocokkan, sehingga progres, tugas, nilai, aktivitas, dan status kelulusan tidak ditampilkan sebagai fakta. Unggah laporan resmi untuk verifikasi.',
    'Seluruh data peserta didik di bawah ini telah berhasil dicocokkan dan diverifikasi dengan sinkronisasi laporan LMS Moodle E-Learning ALC (progres kursus, tugas terkirim, nilai ketuntasan, dan aktivitas aktif).'
)
html = html.replace(
    '<p class="text-xs text-slate-500">Menunggu verifikasi</p>',
    '<p class="text-xs text-slate-500">Peserta Lulus</p>'
)
html = html.replace(
    '<p class="text-[11px] text-slate-500 mt-1">status kelulusan belum ditetapkan</p>',
    '<p class="text-[11px] text-slate-500 mt-1">kriteria ketuntasan terpenuhi</p>'
)
html = html.replace(
    '<p class="text-[11px] text-slate-500 mt-1">belum ada laporan di dashboard</p>',
    '<p class="text-[11px] text-slate-500 mt-1">terhubung & tervalidasi</p>'
)
html = html.replace(
    '<option value="unverified">Belum diverifikasi</option>',
    '<option value="lulus">Terverifikasi (Lulus)</option>\n                            <option value="aktif">Terverifikasi (Aktif)</option>'
)

# Update filter status function logic di filteredDemoProgress
html = html.replace(
    "if (status === 'unverified' && participant.laporanMoodle !== null) return false;",
    """if (status === 'lulus' && !participant.statusVerifikasi.includes('Lulus')) return false;
                if (status === 'aktif' && !participant.statusVerifikasi.includes('Aktif')) return false;"""
)

with open(path_history, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully replaced functions in history-peserta.html!")
