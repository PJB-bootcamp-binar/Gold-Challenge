# Gold-Challenge-Budi-Hidayat
CLEANING TEXT APP

Spesifikasi Aplikasi Clean Text
Fitur Utama

    Input teks: pengguna dapat memasukkan teks melalui form input.
    Upload file CSV: pengguna dapat mengunggah file CSV yang berisi teks yang akan dibersihkan.
    Pembersihan teks: aplikasi akan membersihkan teks dari karakter yang tidak diperlukan, seperti spasi ganda, tanda baca, atau karakter khusus.
    Tampilan hasil pembersihan: aplikasi akan menampilkan teks yang sudah dibersihkan dalam bentuk tabel atau form.

Desain Antarmuka

    Halaman utama: halaman yang menampilkan form input untuk memasukkan teks atau mengunggah file CSV.
    Halaman hasil: halaman yang menampilkan hasil pembersihan teks dalam bentuk tabel atau form.

Desain Teknis

    Framework: Flask
    Dependensi: pandas, flask-wtf
    Metode HTTP: POST untuk mengirimkan data dari form, GET untuk menampilkan halaman hasil.

Rancangan URL

    GET /: menampilkan halaman utama dengan form input.
    POST /upload: menangani pengiriman file CSV dari form upload.
    POST /clean: menangani pengiriman teks dari form input dan memproses pembersihan teks.
    GET /result: menampilkan hasil pembersihan teks dalam bentuk tabel atau form.
