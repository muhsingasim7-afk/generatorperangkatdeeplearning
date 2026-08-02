import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Generator Perangkat Deep Learning",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Generator Perangkat Pembelajaran Mendalam")
st.caption("Aplikasi Pembuat Modul RPP, LKPD, Materi, Rubrik, dan Soal Sumatif Berbasis AI")

with st.sidebar:
    st.header("⚙️ Pengaturan Aplikasi")
    api_key = st.text_input("Masukkan API Key Gemini:", type="password", help="Dapatkan API Key gratis di Google AI Studio")
    st.markdown("---")
    st.info("💡 **Petunjuk Penggunaan:**\n1. Masukkan API Key Gemini.\n2. Isi formulir di halaman utama.\n3. Klik tombol Generate.\n4. Salin/Unduh hasil.")

col1, col2 = st.columns(2)

with col1:
    mapel = st.text_input("Mata Pelajaran", value="Matematika")
    jenjang = st.selectbox("Jenjang / Fase", [
        "SD / Fase A (Kelas 1-2)",
        "SD / Fase B (Kelas 3-4)",
        "SD / Fase C (Kelas 5-6)",
        "SMP / Fase D (Kelas 7-9)",
        "SMA / Fase E (Kelas 10)",
        "SMA / Fase F (Kelas 11-12)"
    ], index=3)

with col2:
    alokasi_waktu = st.text_input("Alokasi Waktu", value="2 JP x 40 Menit")
    kearifan_lokal = st.text_input("Konteks / Kearifan Lokal (Opsional)", value="Proses pembuatan Sagu Lempeng")

tujuan_pembelajaran = st.text_area(
    "Tujuan Pembelajaran (TP)", 
    height=100, 
    value="Siswa dapat menganalisis hubungan antara keliling dan diameter lingkaran melalui masalah kontekstual."
)

if st.button("🚀 Buat Perangkat Pembelajaran", type="primary", use_container_width=True):
    if not api_key:
        st.error("❌ Silakan masukkan API Key Gemini di menu sidebar kiri terlebih dahulu!")
    elif not tujuan_pembelajaran:
        st.warning("⚠️ Tujuan Pembelajaran tidak boleh kosong!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            prompt = f"""
            Bertindaklah sebagai Pakar Pengembang Kurikulum dan Instructional Designer Pembelajaran Mendalam (Deep Learning).

            Buatkan 1 paket Perangkat Pembelajaran Mendalam yang utuh dan terintegrasi berdasarkan input berikut:
            - Mata Pelajaran: {mapel}
            - Jenjang/Fase: {jenjang}
            - Alokasi Waktu: {alokasi_waktu}
            - Tujuan Pembelajaran (TP): {tujuan_pembelajaran}
            - Kearifan Lokal/Konteks: {kearifan_lokal}

            Hasilkan output lengkap dengan 5 komponen utama berikut menggunakan format Markdown yang sangat rapi:

            # PERANGKAT PEMBELAJARAN MENDALAM (DEEP LEARNING)
            **Mata Pelajaran:** {mapel} | **Fase/Kelas:** {jenjang} | **Alokasi Waktu:** {alokasi_waktu}
            **TP:** {tujuan_pembelajaran}
            ---

            ## 1. MODUL AJAR / RPP (DEEP LEARNING)
            - **Identitas & Informasi Umum:** Target siswa, model pembelajaran, sarana prasarana.
            - **Kegiatan Awal (Mindful Learning):** Apersepsi memicu kesadaran, motivasi, dan prasangka positif.
            - **Kegiatan Inti (Meaningful & Joyful Learning):** Eksplorasi kontekstual bermakna, diskusi kelompok, pemecahan masalah interaktif.
            - **Kegiatan Penutup (Refleksi Metakognisi):** Umpan balik dan refleksi siswa.

            ---
            ## 2. RINGKASAN MATERI AJAR
            Materi esensial yang disusun sistematis, kontekstual, memuat contoh dunia nyata, dan poin kunci.

            ---
            ## 3. LEMBAR KERJA PESERTA DIDIK (LKPD)
            - Judul & Petunjuk Pengerjaan.
            - Aktivitas Berbasis Pemecahan Masalah (HOTS) yang mendorong berpikir kritis dan kolaborasi.

            ---
            ## 4. RUBRIK PENILAIAN LKPD
            Buat tabel rubrik analitik berjenjang (Sangat Baik, Baik, Cukup, Perlu Bimbingan) dengan kriteria: Penguasaan Konsep, Penalaran Kritis, Kerjasama, dan Kreativitas.

            ---
            ## 5. KISI-KISI DAN SOAL ASESMEN SUMATIF
            - **Tabel Kisi-Kisi:** Indikator Soal, Bentuk Soal, Level Kognitif (C4/C5/C6).
            - **Naskah Soal HOTS:** Minimal 3-5 soal uraian/pilihan ganda.
            - **Kunci Jawaban & Pedoman Penskoran.**
            """

            with st.spinner("⏳ Sedang memproses dan menyusun perangkat pembelajaran lengkap... Mohon tunggu sebentar."):
                response = model.generate_content(prompt)
                hasil_teks = response.text

            st.success("✅ Perangkat Pembelajaran Berhasil Dibuat!")
            st.markdown(hasil_teks)

            st.download_button(
                label="📥 Unduh Hasil (.txt / Markdown)",
                data=hasil_teks,
                file_name=f"Perangkat_Pembelajaran_{mapel}_{jenjang}.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {str(e)}")
