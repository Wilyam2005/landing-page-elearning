import subprocess

path_history = r"d:\Berkas - Berkas\E-learning ALC\landing-page-elearning-main\history-peserta.html"
with open(path_history, "r", encoding="utf-8") as f:
    text = f.read()

correct_func = '''        function exportSimulationCsv() {
            const headers = ['nama','nisn','tahunAjaran','jenjang','kelas','kursus','progres','tugasSelesai','totalTugas','nilai','aktivitasTerakhir','status'];
            const rows = [headers.join(',')];
            filteredSimulationParticipants().forEach(participant => {
                const metrics = getSimulationMetrics(participant);
                participant.courses.forEach(course => {
                    const values = [participant.nama, participant.nisn || '', participant.tahunAjaran, participant.jenjang, participant.kelas || '', course.name, course.progress, course.tasksCompleted, course.tasksTotal, course.score ?? '', participant.lastActivity, metrics.complete ? 'Semua kursus selesai' : 'Sedang berjalan'];
                    rows.push(values.map(value => `"${String(value).replace(/"/g, '""')}"`).join(','));
                });
            });
            const blob = new Blob(['\\uFEFF', rows.join('\\n')], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'progres-kursus-peserta-pkbm-alc.csv';
            link.click();
            URL.revokeObjectURL(url);
        }'''

# Replace from function exportSimulationCsv to </script>
idx = text.find('function exportSimulationCsv() {')
if idx != -1:
    end_script = text.rfind('</script>')
    text = text[:idx] + correct_func + '\n    ' + text[end_script:]

with open(path_history, "w", encoding="utf-8") as f:
    f.write(text)

# Now test node syntax
idx_start = text.find('<script>\n        const PASSWORD')
js_code = text[idx_start+8:text.rfind('</script>')]
p = subprocess.run(['node', '-c', '-'], input=js_code, text=True, capture_output=True)
print("Node syntax check returncode:", p.returncode)
if p.returncode != 0:
    print("Node error:", p.stderr)
else:
    print("history-peserta.html JS is completely valid!")
