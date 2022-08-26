from re import U
from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

pairs = [
### Skenario Sapaan ###
#1
    ['(start|mulai|perkenalan|intro)',
    ['PDMbot menyediakan informasi terkait: 1. Profil 2.Pendaftaran pegawai 3.Donasi 4.Penelitian 5.Struktur Kepengurusan 6.Umum ']],
 
    ['(1|satu|one|profil)',
    ['PROFIL : Pada bagian profil terdapat 8 topik informasi, kamu bisa bertanya seputar tahun berdiri, alamat, struktur, organisasi, dan amal usaha']],
#2  
    ['(2|dua|two|pendaftaran pegawai)',
    ['PENDAFTARAN PEGAWAI : Pada bagian Pendaftaran Pegawai terdapat 6 topik informasi, kamu bisa bertanya seputar informasi lowongan, persyaratan pendaftaran dan prosedur seleksi']],
    
    ['(3|tiga|three|info donasi)',
    ['DONASI : Pada bagian Donasi terdapat 8 topik informasi, kamu bisa bertanya seputar informasi prosedur donasi,infaq dan shadaqah']],
#3    
    ['(4|empat|four|penelitian)',
    ['PENELITIAN : Pada bagian Penelitian terdapat 4 topik informasi, kamu bisa bertanya seputar syarat dan prosedur penelitian di lingkungan PDM Kota Yogyakarta']],

    ['(5|lima|five|pengurus)',
    ['Struktur Kepengurusan : Pada bagian Struktur Kepengurusan terdapat 4 topik informasi, kamu bisa bertanya seputar jabatan dan struktur kepengurusan di PDM Kota Yogyakarta']],
#4  
    ['(6|enam|six|umum)',
    ['UMUM : Pada bagian ini memuat informasi terkait Muhammadiyah dan info kontak PDM Kota Yogyakarta']],

#5
    ['(.*)(Assalamualaikum|hello|hi|halo|hai|hey|holla|hola|pagi|siang|malam|sore|petang|kabar|tes|ping|check)',
    ['Halo, selamat datang, perkenalkan saya chatbot layanan web PDM, ada yang bisa saya bantu?']],
   
    ['(Assalamualaikum|hello|hi|halo|hai|hey|holla|hola|pagi|siang|malam|sore|petang|kabar|tes|ping|check)',
    ['Halo, selamat datang, perkenalkan saya chatbot layanan web PDM, ada yang bisa saya bantu?']],
#6
    ['(.*)(tanya|bertanya|bantu|tolong)',
    ['mau tahu info tentang apa?, akan saya coba jawab ya']],
    
    ['(tanya|bertanya|bantu|tolong)',
    ['mau tahu info tentang apa?, akan saya coba jawab ya']],
    
#### 1.LIST PERTANYAAN SEPUTAR PROFILE ORGANISASI (PDM KOTA YOGTAKARTA) ####
#1
    ['(.*) (berdiri|didirikan|tahun|kapan|tanggal)',
    ['PDM berdiri tahun 1968 Untuk info detail silahkan klik link berikut:https://pdmjogja.org/sejarah-singkat/']],
    
    ['(PDM berdiri|PDM didirikan)',
    ['PDM berdiri tahun 1968 Untuk info detail silahkan klik link berikut:https://pdmjogja.org/sejarah-singkat/']],
#2  
    ['(.*) (lokasi|alamat|tempat)',
    ['Jalan Sultan Agung No. 14, Kota Yogyakarta, Kode Pos 5515']],
    
    ['(lokasi pdm|alamat pdm)',
    ['Jalan Sultan Agung No. 14, Kota Yogyakarta, Kode Pos 5515']],
#3  
    ['(.*) (struktur pimpinan)',
    ['Struktur pimpinan PDM Kota Yogyakarta terdiri dari: 1. Penasehat 2. Pimpinan Harian 3. Ketua Majelis 4. Ketua Lembaga Untuk detail pengurus bisa klik tautan berikut: https://pdmjogja.org/struktur-pimpinan/']],
    
    ['(struktur pimpinan)',
    ['Struktur pimpinan PDM Kota Yogyakarta terdiri dari: 1. Penasehat 2. Pimpinan Harian 3. Ketua Majelis 4. Ketua Lembaga Untuk detail pengurus bisa klik tautan berikut: https://pdmjogja.org/struktur-pimpinan/']],
#4  
    ['(.*) (struktur majelis)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah Kota Yogyakarta memiliki 12 (duabelas) majelis. 1. Majelis Tarjih dan Tarjik (MTT) 2. Majelis Tabligh (MT) 3. Majelis Pendidikan Dasar dan Menengah (DIKDASMEN) 4. Majelis Pendidikan Kader (MPK) 5. Majelis Pelayanan Kesehatan Umum (MPKU) 6. Majelis Pelayanan Sosial (MPS) 7.Majelis Ekonomi dan Kewirausahaan (MEK) 8. Majelis Wakaf dan Kehartabendaan (Wakaf) 9. Majelis Pemberdayaan Masyarakat (MPM) 10. Majelis Hukum dna HAM(MHH) 11. Majelis Lingkungan Hidup (MLH) 12. Majelis Pustaka dan Informasi (MPI). Untuk detail informasi silahkan menuju tautan berikut: https://pdmjogja.org/majelis/']],
    
    ['(struktur majelis)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah Kota Yogyakarta memiliki 12 (duabelas) majelis. 1. Majelis Tarjih dan Tarjik (MTT) 2. Majelis Tabligh (MT) 3. Majelis Pendidikan Dasar dan Menengah (DIKDASMEN) 4. Majelis Pendidikan Kader (MPK) 5. Majelis Pelayanan Kesehatan Umum (MPKU) 6. Majelis Pelayanan Sosial (MPS) 7.Majelis Ekonomi dan Kewirausahaan (MEK) 8. Majelis Wakaf dan Kehartabendaan (Wakaf) 9. Majelis Pemberdayaan Masyarakat (MPM) 10. Majelis Hukum dna HAM(MHH) 11. Majelis Lingkungan Hidup (MLH) 12. Majelis Pustaka dan Informasi (MPI). Untuk detail informasi silahkan menuju tautan berikut: https://pdmjogja.org/majelis/']],
#5  
    ['(.*) (Struktur lembaga)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah Kota Yogyakarta memiliki 7 (tujuh) lembaga. 1. Lembaga Pengembagan Cabang dan Ranting (LPCR) 2. Lembaga Pembina dan Pengawasan Keuangan (LPPK) 3. Lembaga Penanggulangan Bencana (LPB/ MDMC) 4. Lembaga Zakat Infaq Shadaqah (Lazismu) 5. Lembaga Hikmah dan Kebijakan Publik (LHKP) 6. Lembaga Seni Budaya dan Olahraga (LSBO) 7. Lembaga Pengembangan Pesantren. Untuk detail informasi silahkan menuju tautan berikut: https://pdmjogja.org/lembaga/']],

    ['(Struktur lembaga)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah Kota Yogyakarta memiliki 7 (tujuh) lembaga. 1. Lembaga Pengembagan Cabang dan Ranting (LPCR) 2. Lembaga Pembina dan Pengawasan Keuangan (LPPK) 3. Lembaga Penanggulangan Bencana (LPB/ MDMC) 4. Lembaga Zakat Infaq Shadaqah (Lazismu) 5. Lembaga Hikmah dan Kebijakan Publik (LHKP) 6. Lembaga Seni Budaya dan Olahraga (LSBO) 7. Lembaga Pengembangan Pesantren. Untuk detail informasi silahkan menuju tautan berikut: https://pdmjogja.org/lembaga/']],
#6
    ['(.*) (Struktur cabang|cabang)',
    ['Pimpinan Daerah Muhammadiyah kota Yogyakarta menaungi 14 (empat belas) Cabang Muhammadiyah, yaitu: 1. Kecamatan Tegalrejo 2. Kecamatan Jetis 3. Kecamatan Gedongtengen 4. Kecamatan Wirobrajan 5. Kecamatan Mantrijeron 6. Kecamatan Kraton 7. Kecamatan Ngampilan 8. Kecamatan Gondongmana 9. Kecamatan Mergangsan 10. Kecamatan Pakualaman 11. Kecamatan Danurejan 12. Kecamatan Gondokusuman 13. Kecamatan Umbulharjo 14. Kecamatan Kotagede Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/cabang/']],

    ['(Struktur cabang|cabang)',
    ['Pimpinan Daerah Muhammadiyah kota Yogyakarta menaungi 14 (empat belas) Cabang Muhammadiyah, yaitu: 1. Kecamatan Tegalrejo 2. Kecamatan Jetis 3. Kecamatan Gedongtengen 4. Kecamatan Wirobrajan 5. Kecamatan Mantrijeron 6. Kecamatan Kraton 7. Kecamatan Ngampilan 8. Kecamatan Gondongmana 9. Kecamatan Mergangsan 10. Kecamatan Pakualaman 11. Kecamatan Danurejan 12. Kecamatan Gondokusuman 13. Kecamatan Umbulharjo 14. Kecamatan Kotagede Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/cabang/']],
#7
    ['(.*) (Organisasi ortonom|ortonom|organisasi)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah terdapat 7 (tujuh) buah organisasi otonom Muhammadiyah. 1. ‘Aisyiyah 2. Pemuda Muhamadiyah (PM) 3. Nasyiatul ‘Aisyiah (NA) 4. Ikatan Pelajar Muhammadiyah (IPM) 5. Tapak Suci Muhammadiyah (TSPM) 6. Ikatan Mahasiswa Muhammadiyah (IMM) 7. Hizbul Wathan (HW) Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/organisasi-otonom/']],
    
    ['(Organisasi ortonom|ortonom|organisasi)',
    ['Di lingkungan Pimpinan Daerah Muhammadiyah terdapat 7 (tujuh) buah organisasi otonom Muhammadiyah. 1. ‘Aisyiyah 2. Pemuda Muhamadiyah (PM) 3. Nasyiatul ‘Aisyiah (NA) 4. Ikatan Pelajar Muhammadiyah (IPM) 5. Tapak Suci Muhammadiyah (TSPM) 6. Ikatan Mahasiswa Muhammadiyah (IMM) 7. Hizbul Wathan (HW) Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/organisasi-otonom/']],
#8  
    ['(.*) (amal usaha|Amal|Usaha)',
    ['Amal Usaha Muhammadiyah adalah salah satu bentuk lembaga / instansi yang menjadi wujud dari usaha Muhammadiyah dalam mencapai maksud dan tujuannya. Amal usaha muhammadiyah bisa bergerak di bidang sosial, ekonomi, pendidikan, kesehatan, dan bidang lainnya. Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/amal-usaha/']],
    
    ['(amal usaha|Amal|Usaha)',
    ['Amal Usaha Muhammadiyah adalah salah satu bentuk lembaga / instansi yang menjadi wujud dari usaha Muhammadiyah dalam mencapai maksud dan tujuannya. Amal usaha muhammadiyah bisa bergerak di bidang sosial, ekonomi, pendidikan, kesehatan, dan bidang lainnya. Informasi lanjut dapat menuju tautan berikut: https://pdmjogja.org/amal-usaha/']],


#### 2. List pertanyaan seputar lowongan dan pendaftaraan pegawai ####
#1   
    ['(.*) (informasi lowongan|lowongan pegawai|info lowongan pegawai|info lowongan)',
    ['Untuk informasi lowongan Silahkan kunjungi tautan berikut: https://pdmjogja.org/gptt/lowongan/']],
   
    ['(informasi lowongan|lowongan pegawai|info lowongan pegawai|info lowongan)',
    ['Untuk informasi lowongan Silahkan kunjungi tautan berikut: https://pdmjogja.org/gptt/lowongan/']],
#2  
    ['(.*) (syarat pendaftaran|informasi syarat pendaftaran|persyaratan pegawai|persyaratan pendaftaran|syarat daftar|syarat karyawan|syarat GTT|syarat PTT)',
    ['Untuk persyaratan pendaftar terdiri dari persyaratan umum dan persyaratan administrasi']],
    
    ['(syarat pendaftaran|informasi syarat pendaftaran|persyaratan pegawai|persyaratan pendaftaran|syarat daftar|syarat karyawan|syarat GTT|syarat PTT)',
    ['Untuk persyaratan pendaftar terdiri dari persyaratan umum dan persyaratan administrasi']],
#3  
    ['(.*) (persyaratan umum|syarat umum|persayaratan umum pegawai)',
    ['Persyaratan umum: 1. Warga Negara Republik Indonesia, taat beribadah dan mengamalkan ajaran Islam, serta dapat membaca Al-Qur’an secara tartil. 2. Setia pada prinsip – prinsip dasar perjuangan dan garis kebijakan pimpinan Muhammadiyah.3. Sehat jasmani dan rohani, serta berkelakuan baik sesuai norma dan akhlak Islami. 4.Tidak menjadi anggota organisasi partai politik dan atau organisasi yang berafiliasi dengan partai politik.']],

    ['(persyaratan umum|syarat umum|persayaratan umum pegawai)',
    ['Persyaratan umum: 1. Warga Negara Republik Indonesia, taat beribadah dan mengamalkan ajaran Islam, serta dapat membaca Al-Qur’an secara tartil. 2. Setia pada prinsip – prinsip dasar perjuangan dan garis kebijakan pimpinan Muhammadiyah.3. Sehat jasmani dan rohani, serta berkelakuan baik sesuai norma dan akhlak Islami. 4.Tidak menjadi anggota organisasi partai politik dan atau organisasi yang berafiliasi dengan partai politik.']],
#4  
    ['(.*) (persyaratan administrasi|persyaratan administrasi pegawai|syarat administrasi)',
    ['Persyaratan Administrasi: 1. Surat lamaran pekerjaan yang ditujukan kepada Majelis Pendidikan Dasar dan Menengah Pimpinan Daerah Muhammadiyah Kota Yogyakarta (Jl. Sultan Agung 14, Yogyakarta). 2. Surat rekomendasi yang sah dari Pimpinan Ranting Muhammadiyah / Pimpinan Cabang Muhammadiyah / Ortom tempat tinggal pelamar. 3. Biodata dan pas foto warna ukuran (3×4) cm sebanyak 2 lembar, 1 di tempel di biodata dan 1 ditempel pada bukti pendaftaran 4. Fotokopi Kartu Tanda Anggota Muhammadiyah (KTAM) sebanyak 1 lembar, atau keterangan dari kepala kantor PP Muhammadiyah Jl. Cik Di Tiro yang menunjukkan KTAM sedang dalam proses (dapat menyusul). 5. Usia maksimal 35 tahun, dibuktikan dengan fotokopi Kartu Tanda Penduduk (KTP) sebanyak 1 lembar. 6. Sehat jasmani dan rohani, dibuktikan dengan surat keterangan sehat dari dokter / RS PKU Muhammadiyah. 7. Fotokopi Ijazah yang dilegalisasi sesuai dengan kualifikasi masing-masing 1 lembar. 8. Fotokopi Transkrip Nilai yang dilegalisasi dengan IPK minimal 2,75 untuk S1 sebanyak 1 lembar. 9. Fotokopi sertifikat komputer dan sertifikat – sertifikat penunjang kemampuan lainnya. Untuk informasi detail ku jungi tautan berikut: https://pdmjogja.org/gptt/prosedur']],
    
    ['(persyaratan administrasi|persyaratan administrasi pegawai|syarat administrasi)',
    ['Persyaratan Administrasi: 1. Surat lamaran pekerjaan yang ditujukan kepada Majelis Pendidikan Dasar dan Menengah Pimpinan Daerah Muhammadiyah Kota Yogyakarta (Jl. Sultan Agung 14, Yogyakarta). 2. Surat rekomendasi yang sah dari Pimpinan Ranting Muhammadiyah / Pimpinan Cabang Muhammadiyah / Ortom tempat tinggal pelamar. 3. Biodata dan pas foto warna ukuran (3×4) cm sebanyak 2 lembar, 1 di tempel di biodata dan 1 ditempel pada bukti pendaftaran 4. Fotokopi Kartu Tanda Anggota Muhammadiyah (KTAM) sebanyak 1 lembar, atau keterangan dari kepala kantor PP Muhammadiyah Jl. Cik Di Tiro yang menunjukkan KTAM sedang dalam proses (dapat menyusul). 5. Usia maksimal 35 tahun, dibuktikan dengan fotokopi Kartu Tanda Penduduk (KTP) sebanyak 1 lembar. 6. Sehat jasmani dan rohani, dibuktikan dengan surat keterangan sehat dari dokter / RS PKU Muhammadiyah. 7. Fotokopi Ijazah yang dilegalisasi sesuai dengan kualifikasi masing-masing 1 lembar. 8. Fotokopi Transkrip Nilai yang dilegalisasi dengan IPK minimal 2,75 untuk S1 sebanyak 1 lembar. 9. Fotokopi sertifikat komputer dan sertifikat – sertifikat penunjang kemampuan lainnya. Untuk informasi detail ku jungi tautan berikut: https://pdmjogja.org/gptt/prosedur']],
#5  
    ['(.*) (prosedur pendaftaran|proses pendaftaran)',
    ['Persyaratan administrasi dijilid menjadi satu bendel dengan ketentuan : 1. Mengisi Format sampul, Blangko Kelengkapan, dan Biodata yang dapat didownload dibawah. 2. Blangko kelengkapan syarat administrasi disertakan di halaman pertama bendel berkas sesudah sampul.3. Jilid dengan sampul berwarna : a. MERAH TUA : pelamar formasi pendidik / guru tingkat Sekolah Dasar. b. HIJAU DAUN : pelamar formasi pendidik / guru tingkat Sekolah Menengah Pertama / Madrasah Tsanawiyah. c. BIRU MUDA : pelamar formasi pendidik / guru tingkat Sekolah Menengah Atas / Madrasah Aliyah. d. BIRU TUA : pelamar formasi pendidik / guru tingkat Sekolah Menengah Kejuruan. f. COKLAT TUA : pelamar formasi tenaga kependidikan (TU, Bendahara, tenaga perpustakaan dan tenaga lainya). Pendaftaran : 1. Berkas diserahkan di Kantor Sekretariat Majelis Pendidikan Dasar dan Menengah Pimpinan Daerah Muhammadiyah Kota Yogyakarta (Jl. Sultan Agung 14, Yogyakarta, Lantai III sayap timur pojok utara). 2. Layanan pendaftaran bagi para pelamar di buka mulai 9 Mei s.d 15 Juni 2019. 3. Pendaftaran dilakukan pada hari dan jam kerja : Senin-Kamis (Pk. 08.00 – 14.00 WIB), Jumat (Pk. 08.00-11.00 WIB), dan Sabtu (Pk. 08.00-13.00 WIB). 4. Setelah menyerahkan berkas ke Sekretariat Majelis DIKDASMEN PDM Kota Yogyakarta dan mendapatkan nomor kode pendaftaran, pelamar wajib melakukan pengisian data secara online di menu dibawah. 5. Hasil Seleksi Administrasi akan diumumkan pada tanggal 21 Juni 2019 di Website.']],
    
    ['(prosedur pendaftaran|proses pendaftaran)',
    ['Persyaratan administrasi dijilid menjadi satu bendel dengan ketentuan : 1. Mengisi Format sampul, Blangko Kelengkapan, dan Biodata yang dapat didownload dibawah. 2. Blangko kelengkapan syarat administrasi disertakan di halaman pertama bendel berkas sesudah sampul.3. Jilid dengan sampul berwarna : a. MERAH TUA : pelamar formasi pendidik / guru tingkat Sekolah Dasar. b. HIJAU DAUN : pelamar formasi pendidik / guru tingkat Sekolah Menengah Pertama / Madrasah Tsanawiyah. c. BIRU MUDA : pelamar formasi pendidik / guru tingkat Sekolah Menengah Atas / Madrasah Aliyah. d. BIRU TUA : pelamar formasi pendidik / guru tingkat Sekolah Menengah Kejuruan. f. COKLAT TUA : pelamar formasi tenaga kependidikan (TU, Bendahara, tenaga perpustakaan dan tenaga lainya). Pendaftaran : 1. Berkas diserahkan di Kantor Sekretariat Majelis Pendidikan Dasar dan Menengah Pimpinan Daerah Muhammadiyah Kota Yogyakarta (Jl. Sultan Agung 14, Yogyakarta, Lantai III sayap timur pojok utara). 2. Layanan pendaftaran bagi para pelamar di buka mulai 9 Mei s.d 15 Juni 2019. 3. Pendaftaran dilakukan pada hari dan jam kerja : Senin-Kamis (Pk. 08.00 – 14.00 WIB), Jumat (Pk. 08.00-11.00 WIB), dan Sabtu (Pk. 08.00-13.00 WIB). 4. Setelah menyerahkan berkas ke Sekretariat Majelis DIKDASMEN PDM Kota Yogyakarta dan mendapatkan nomor kode pendaftaran, pelamar wajib melakukan pengisian data secara online di menu dibawah. 5. Hasil Seleksi Administrasi akan diumumkan pada tanggal 21 Juni 2019 di Website.']],
#6  
    ['(.*) (proses seleksi|seleksi)',
    ['1. Pengumuman. 2. Pendaftaran Offline dan Online. 3. Seleksi Administrasi. 4. Pengumuman hasil seleksi administrasi. 5. Ujian Tulis ISMUBA dan Psikotes. 6. Ujian Microteaching / uji kompetensi dan wawancara persekolahan. 7. Tes Baca Al Qur`an, Praktek Wudhu dan Shalat. 8. Wawancara Kemuhammadiyahan dan Loyalitas. 9. Pengumuman hasil seleksi akhir. 10.Pengarahan bagi Calon GTT/PTT yang diterima.']],
    
    ['(proses seleksi|seleksi)',
    ['1. Pengumuman. 2. Pendaftaran Offline dan Online. 3. Seleksi Administrasi. 4. Pengumuman hasil seleksi administrasi. 5. Ujian Tulis ISMUBA dan Psikotes. 6. Ujian Microteaching / uji kompetensi dan wawancara persekolahan. 7. Tes Baca Al Qur`an, Praktek Wudhu dan Shalat. 8. Wawancara Kemuhammadiyahan dan Loyalitas. 9. Pengumuman hasil seleksi akhir. 10.Pengarahan bagi Calon GTT/PTT yang diterima.']],


#### 3. List pertanyaan seputar donasi ####
#1
    ['(.*) (donasi|muzakki)',
    ['Berikut ini layanan penerimaan Z.I.S dari para donatur / muzakki yang disediakan : 1. Jemput Z.I.S, 2. Setor tunai Z.I.S']],
    
    ['(donasi|muzakki)',
    ['Berikut ini layanan penerimaan Z.I.S dari para donatur / muzakki yang disediakan : 1. Jemput Z.I.S, 2. Setor tunai Z.I.S']],
#2  
    ['(.*) (Jemput|Jemput Z.I.S)',
    ['Kapanpun dan dimanapun petugas kami siap menjalankan amanah mulia untuk membantu anda menunaikan zakat, infaq dan shodaqoh dengan menjemput langsung donasi anda']],
    
    ['(Jemput Z.I.S)',
    ['Kapanpun dan dimanapun petugas kami siap menjalankan amanah mulia untuk membantu anda menunaikan zakat, infaq dan shodaqoh dengan menjemput langsung donasi anda']],
#3 
    ['(.*) (Setor Tunai|Setor Tunai Z.I.S)',
    ['Anda dapat langsung menyetor secara tunai zakat, infaq dan shadaqah anda ke kantor LAZISMU PDM Kota Yogyakarta maupun kantor LAZISMU yang terdapat di kota Yogyakarta.']],
    
    ['(Setor Tunai|Setor Tunai Z.I.S)',
    ['Anda dapat langsung menyetor secara tunai zakat, infaq dan shadaqah anda ke kantor LAZISMU PDM Kota Yogyakarta maupun kantor LAZISMU yang terdapat di kota Yogyakarta.']],
#4  
    ['(.*) (kantor lazismu|alamat lazismu)',
    ['Kantor LAZISMU UPZ PDM Kota Yogyakarta Alamat : Ruko depan Kantor PDM Kota Yogyakarta (Jl. Sultan Agung No. 14, Kota Yogyakarta, DIY, Kode Pos 55151). Waktu Layanan : senin – sabtu pukul 09.00 – 15.00 WIB.']],

    ['(kantor lazismu|alamat lazismu)',
    ['Kantor LAZISMU UPZ PDM Kota Yogyakarta Alamat : Ruko depan Kantor PDM Kota Yogyakarta (Jl. Sultan Agung No. 14, Kota Yogyakarta, DIY, Kode Pos 55151). Waktu Layanan : senin – sabtu pukul 09.00 – 15.00 WIB.']],
#5
    ['(.*) (cara transfer|transfer Z.I.S)',
    ['Menyerahkan Z.I.S anda lebih aman dan cepat dengan transfer via Bank (ATM) di seluruh indonesia. Apabila sudah melakukan transfer Z.I.S melalui bank jangan lupa mengkonfirmasi kepada kami dengan cara mengirim SMS / WA dengan format : #Nama#Bank Tujuan#Tgl Donasi# Jumlah Donasi#Tujuan Donasi ke nomor']],
    
    ['(cara transfer|transfer Z.I.S)',
    ['Menyerahkan Z.I.S anda lebih aman dan cepat dengan transfer via Bank (ATM) di seluruh indonesia. Apabila sudah melakukan transfer Z.I.S melalui bank jangan lupa mengkonfirmasi kepada kami dengan cara mengirim SMS / WA dengan format : #Nama#Bank Tujuan#Tgl Donasi# Jumlah Donasi#Tujuan Donasi ke nomor']],
#6  
    ['(.*)(transfer zakat|transfer shadaqah)',
    ['Transfer Zakat pada REK BRI Syariah: 702.64.80.501 a.n. Andjadi qq Lembaga ZIS PDM Kota Yogyakarta.']],
    
    ['(transfer zakat|transfer shadaqah)',
    ['Transfer Zakat pada REK BRI Syariah: 702.64.80.501 a.n. Andjadi qq Lembaga ZIS PDM Kota Yogyakarta.']],
#7  
    ['(.*) (info zakat|infaq|shadaqah)',
    ['untuk informasi lengkap terkait infaq zakat dan shadaqah bisa mengunjungi tautan berikut : https://pdmjogja.org/lazismu/']],
    
    ['(info zakat|infaq|shadaqah)',
    ['untuk informasi lengkap terkait infaq zakat dan shadaqah bisa mengunjungi tautan berikut : https://pdmjogja.org/lazismu/']],
    
#### 4. LIST PERTANYAAN BAGIAN LAYANAN Penelitian DI PDM KOTA YOGYAKARTA ####
#1
    ['(.*) (syarat penelitian|persyaratan penelitian)',
    ['Persyaratan administrasi yang harus dipenuhi peneliti: 1.Surat rekomendasi penelitian dari Fakultas yang ditujukan kepada Majelis DIKDASMEN PDM Kota Yogyakarta. Didalam surat tersebut harus spesifik sekolah Muhammadiyah yang dituju. 2.Proposal penelitian. 3.Memo / surat resmi dari sekolah Muhammadiyah yang mengizinkan penelitian di lingkungan sekolahnya']],
    
    ['(syarat penelitian|persyaratan penelitian)',
    ['Persyaratan administrasi yang harus dipenuhi peneliti: 1.Surat rekomendasi penelitian dari Fakultas yang ditujukan kepada Majelis DIKDASMEN PDM Kota Yogyakarta. Didalam surat tersebut harus spesifik sekolah Muhammadiyah yang dituju. 2.Proposal penelitian. 3.Memo / surat resmi dari sekolah Muhammadiyah yang mengizinkan penelitian di lingkungan sekolahnya']],
    
#2   
    ['(.*) (Surat|Memo)',
    ['Untuk mendapatkan memo / surat resmi dari sekolah Muhammadiyah yang dituju peneliti dapat menyerahkan surat rekomendasi penelitian fakultas untuk dipelajari olah pihak sekolah yang menjadi lokasi penelitian.']],

    ['(Surat|Memo)',
    ['Untuk mendapatkan memo / surat resmi dari sekolah Muhammadiyah yang dituju peneliti dapat menyerahkan surat rekomendasi penelitian fakultas untuk dipelajari olah pihak sekolah yang menjadi lokasi penelitian.']],
   
#3    
    ['(.*) (kumpul|pengumpulan administrasi|dikumpulkan|pengumpulan)',
    ['Seluruh persyaratan administrasi diserahkan kepada sekretariat Majelis DIKDASMEN PDM Kota Yogyakarta yang berlokasi di Kantor PDM Kota Yogyakarta Jalan Sultan Agung No.14, Kota Yogyakarta, Daerah Istimewa Yogyakarta lantai 3 pojok sayap timur gedung.']],

    ['(kumpul|pengumpulan administrasi|dikumpulkan|pengumpulan)',
    ['Seluruh persyaratan administrasi diserahkan kepada sekretariat Majelis DIKDASMEN PDM Kota Yogyakarta yang berlokasi di Kantor PDM Kota Yogyakarta Jalan Sultan Agung No.14, Kota Yogyakarta, Daerah Istimewa Yogyakarta lantai 3 pojok sayap timur gedung.']],
    
#4
    ['(.*) (info penelitian|penelitian)',
    ['Pimpinan Daerah Muhammadiyah Kota Yogyakarta membuka kesempatan seluas – luasnya kepada para akademisi dan intelektual di Yogyakarta untuk melakukan penelitian dengan objek penelitian Muhammadiyah apakah itu berupa : Civitas akademika di sekolah muhammadiyah, Pimpinan, Warga, Organisasi Muhammadiyah, Faham agama / ideologi Muhammadiyah, Dan objek penelitian lainnya yang berhubungan dengan Muhammadiyah. lebih lengkap kunjungi : https://pdmjogja.org/izin-penelitian/']],
    
    ['(info penelitian|penelitian)',
    ['Pimpinan Daerah Muhammadiyah Kota Yogyakarta membuka kesempatan seluas – luasnya kepada para akademisi dan intelektual di Yogyakarta untuk melakukan penelitian dengan objek penelitian Muhammadiyah apakah itu berupa : Civitas akademika di sekolah muhammadiyah, Pimpinan, Warga, Organisasi Muhammadiyah, Faham agama / ideologi Muhammadiyah, Dan objek penelitian lainnya yang berhubungan dengan Muhammadiyah. lebih lengkap kunjungi : https://pdmjogja.org/izin-penelitian/']],


#### 5. pertanyaan baru seputar pengurus jabatan pimpinan ####
#1
    ['(.*)(penasehat|jabatan penasehat)',
    ['Penasehat PDM Kota Yogyakarta saat ini : 1.Drs. H. Hadjam Murusdi, SU. 2.H. Marwan DS']],
    
    ['(penasehat|jabatan penasehat)',
    ['Penasehat PDM Kota Yogyakarta saat ini : 1.Drs. H. Hadjam Murusdi, SU. 2.H. Marwan DS']],
#2  
    ['(.*)(pimpinan harian|nama pimpinan harian)',
    ['Struktur Pimpinan Daerah Muhammadiyah Kota Yogyakarta saat ini : Drs.H. Akhid Widi Rahmanto. Wakil Ketua : H.Aris Madani, S.Pd.I. Wakil Ketua : Dr.H. Nur Ahmad Ghojali, S.Ag., M.A. Wakil Ketua :H.Heniy Astiyanto, S.H. Wakil Ketua : H. Ashad Kusuma Djaya. Wakil Ketua : Drs. H. Suparto, M.A. Wakil Ketua : Abdul Latief Baedhowi, S.Ag. Wakil Ketua : H. Sigit Haryo Yudanto, S.Psi. Sekretaris : H. Moch. Muzani, S.Sos. Wakil Sekretaris: -  Bendahara : H.S. Giyok Sutanta, SH. Wakil Bendahara : -']],
    
    ['(.*)(pimpinan harian|nama pimpinan harian)',
    ['Struktur Pimpinan Daerah Muhammadiyah Kota Yogyakarta saat ini : Drs.H. Akhid Widi Rahmanto. Wakil Ketua : H.Aris Madani, S.Pd.I. Wakil Ketua : Dr.H. Nur Ahmad Ghojali, S.Ag., M.A. Wakil Ketua :H.Heniy Astiyanto, S.H. Wakil Ketua : H. Ashad Kusuma Djaya. Wakil Ketua : Drs. H. Suparto, M.A. Wakil Ketua : Abdul Latief Baedhowi, S.Ag. Wakil Ketua : H. Sigit Haryo Yudanto, S.Psi. Sekretaris : H. Moch. Muzani, S.Sos. Wakil Sekretaris: -  Bendahara : H.S. Giyok Sutanta, SH. Wakil Bendahara : -']],
#3  
    ['(.*)(Ketua Majelis|nama Ketua Majelis)',
    ['Struktur Ketua Majelis PDM Kota Yogyakarta saat ini : Majelis Tarjih dan Tajdid : Wahyu wijaya, S.Th.I. Majelis Tabligh : Drs. Fathoni Siraj. Majelis Pendidikan Dasar dan Menengah : Drs. H. Aris Thobirin, M.Si . Majelis Pendidikan Kader : Ahmad Ahid Mudayana, S.KM., M.PH. Majelis Pembina Kesehatan Umum dan Pelayanan Sosial : H. Edi Sukoco, A.Md.Kep. Majelis Ekonomi dan Kewirausahaan : Muhammad Iqbal, SE. Majelis Wakaf dan Kehartabendaan : Drs.H. Marjuki. Majelis Pemberdayaan Masyarakat : Ir. Rusianto Wartono. Majelis Hukum dan Hak Asasi Manusia : DR. M. Arief Setiawan, SH., MH. Majelis Lingkungan Hidup : Hery Setiawan, M.Si. Majelis Pustaka dan Informasi : Fuad Hasyim, SS., M.A.']],
    
     ['(.*)(Ketua Majelis|nama Ketua Majelis)',
    ['Struktur Ketua Majelis PDM Kota Yogyakarta saat ini : Majelis Tarjih dan Tajdid : Wahyu wijaya, S.Th.I. Majelis Tabligh : Drs. Fathoni Siraj. Majelis Pendidikan Dasar dan Menengah : Drs. H. Aris Thobirin, M.Si . Majelis Pendidikan Kader : Ahmad Ahid Mudayana, S.KM., M.PH. Majelis Pembina Kesehatan Umum dan Pelayanan Sosial : H. Edi Sukoco, A.Md.Kep. Majelis Ekonomi dan Kewirausahaan : Muhammad Iqbal, SE. Majelis Wakaf dan Kehartabendaan : Drs.H. Marjuki. Majelis Pemberdayaan Masyarakat : Ir. Rusianto Wartono. Majelis Hukum dan Hak Asasi Manusia : DR. M. Arief Setiawan, SH., MH. Majelis Lingkungan Hidup : Hery Setiawan, M.Si. Majelis Pustaka dan Informasi : Fuad Hasyim, SS., M.A.']],
    #4  
    ['(.*)(ketua lembaga|nama ketua lembaga)',
    ['Struktur Ketua Lembaga PDM Kota Yogyakarta saat ini  Lembaga Pengembangan Cabang dan Ranting : Agni Sutanta, S.IP. Lembaga Pembina dan Pengawas Keuangan : H. Suradiyono, S.Sos. Lembaga Penanggulangan Bencana : Subhi Waltono, S.I.Pust. Lembaga Zakat, Infaq dan Shadaqah : Dai Iskandar, S.Ag, M.Si. Lembaga Hikmah dan Kebijakan Publik : Drs. Abd Samik Sandhi. Lembaga Seni Budaya dan Olahraga : Arif Hidayat, ST. Lembaga Pengembangan Pesantren : Ghofar Ismail, S.Ag., MA.']],

    ['(.*)(ketua lembaga|nama ketua lembaga)',
    ['Struktur Ketua Lembaga PDM Kota Yogyakarta saat ini  Lembaga Pengembangan Cabang dan Ranting : Agni Sutanta, S.IP. Lembaga Pembina dan Pengawas Keuangan : H. Suradiyono, S.Sos. Lembaga Penanggulangan Bencana : Subhi Waltono, S.I.Pust. Lembaga Zakat, Infaq dan Shadaqah : Dai Iskandar, S.Ag, M.Si. Lembaga Hikmah dan Kebijakan Publik : Drs. Abd Samik Sandhi. Lembaga Seni Budaya dan Olahraga : Arif Hidayat, ST. Lembaga Pengembangan Pesantren : Ghofar Ismail, S.Ag., MA.']],

#### 6. LIST PERTANYAAN UMUM SEPUTAR PDM KOTA YOGYAKARTA/MUHAMMADIYAH ####
#1
    ['(.*) (visi|visi muhammadiyah)',
    ['Visi: Muhammadiyah sebagai  gerakan Islam yang berlandaskan Al – Qur’an dan As – Sunnah dengan watak tajdid yang dimilikinya senantiasa istiqomah dan aktif dalam melaksanakan dakwah Islam amar ma’ruf nahi munkar di semua bidang dalam upaya mewujudkan Islam sebagai rahmatan lil ‘alamin menuju terciptanya / terwujudnya masyarakat Islam yang sebenar – benarnya.']],
     
    ['(visi|visi muhammadiyah)',
    ['Visi: Muhammadiyah sebagai  gerakan Islam yang berlandaskan Al – Qur’an dan As – Sunnah dengan watak tajdid yang dimilikinya senantiasa istiqomah dan aktif dalam melaksanakan dakwah Islam amar ma’ruf nahi munkar di semua bidang dalam upaya mewujudkan Islam sebagai rahmatan lil ‘alamin menuju terciptanya / terwujudnya masyarakat Islam yang sebenar – benarnya.']],
#2   
    ['(.*) (misi|misi muhammadiyah)',
    ['Misi: Muhammadiyah sebagai gerakan Islam, dakwah amar ma’ruf nahi munkar memiliki misi : 1. Menegakkan keyakinan tauhid yang murni sesuai dengan ajaran Allah SWT yang dibawa oleh para Rasul sejak Nabi Adam as. Hingga Nabi Muhammad saw. 2. Memahami agama dengan menggunakan akal fikiran sesuai dengan jiwa ajaran Islam untuk menjawab dan menyelesaikan persoalan – persoalan kehidupan. 3. Menyebarluaskan ajaran Islam yang bersumber pada Al – Qur’an sebagai kitab Allah terakhir dan Sunnah Rasul untuk pedoman hidup umat manusia. 4. Mewujudkan amalan – amalan Islam dalam kehidupan pribadi, keluarga dan masyarakat.']],

    ['(misi|misi muhammadiyah)',
    ['Misi: Muhammadiyah sebagai gerakan Islam, dakwah amar ma’ruf nahi munkar memiliki misi : 1. Menegakkan keyakinan tauhid yang murni sesuai dengan ajaran Allah SWT yang dibawa oleh para Rasul sejak Nabi Adam as. Hingga Nabi Muhammad saw. 2. Memahami agama dengan menggunakan akal fikiran sesuai dengan jiwa ajaran Islam untuk menjawab dan menyelesaikan persoalan – persoalan kehidupan. 3. Menyebarluaskan ajaran Islam yang bersumber pada Al – Qur’an sebagai kitab Allah terakhir dan Sunnah Rasul untuk pedoman hidup umat manusia. 4. Mewujudkan amalan – amalan Islam dalam kehidupan pribadi, keluarga dan masyarakat.']],
#3
    ['(.*) (kontak|info kontak|email|telpon|informasi kontak|narahubung)',
    ['Informasi kontak: 1. Sekretariat : 0274-375116 pdmjogja@yahoo.com, 2.Dikdasmen : 0274-375917 dikdasmenjogja@gmail.com, 3.Keuangan   : 0274-389201 pdmjogja@gmail.com']],
    
    ['(info kontak|email|telpon|informasi kontak|narahubung|kontak)',
    ['Informasi kontak: 1. Sekretariat : 0274-375116 pdmjogja@yahoo.com, 2.Dikdasmen : 0274-375917 dikdasmenjogja@gmail.com, 3.Keuangan   : 0274-389201 pdmjogja@gmail.com']],
   
#GREETINGS
    ['(.*)(Terimakasih|makasih|ok|thanks|thank|thank you|quit|keluar|selesai)',
    ['Terimakasih sudah menggunakan layanan PDMbot, semoga informasinya dapat bermanfaat ya :)']],  
]


app = Flask(__name__, template_folder='templates')

app = Flask(__name__)
app.static_folder = 'static'


def chatbot_respon(msg):
  chat=Chat(pairs,reflections)
  return chat.respond(msg)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_respon(userText)
      
           
if __name__ == '__main__':
    app.run()