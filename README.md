# Gold-Challenge-Budi-Hidayat
CLEANING TEXT APP

Spesifikasi Aplikasi Clean Text
Fitur Utama

    Input teks: pengguna dapat memasukkan teks melalui form input.
    Upload file CSV: pengguna dapat mengunggah file CSV yang berisi teks yang akan dibersihkan.
    Pembersihan teks: aplikasi akan membersihkan teks dari karakter yang tidak diperlukan,bahasa alay, stemming, stopword,spasi ganda, tanda baca, atau karakter khusus.
    Tampilan hasil pembersihan: aplikasi akan menampilkan teks yang sudah dibersihkan dalam bentuk tabel atau form dan grafik chat perubahan masing-masing karakter.

Desain Antarmuka

    Halaman index: halaman yang menampilkan form input untuk memasukkan teks atau mengunggah file CSV.
    Halaman result: halaman yang menampilkan hasil pembersihan teks dalam bentuk tabel atau form.

Desain Teknis

    Framework: Flask
    Dependensi: pandas, numpy, re, string, nltk, nltk.corpus, Sastrawi.Stemmer.StemmerFactory,Sastrawi.StopWordRemover,matplotlib
    Metode HTTP: POST untuk mengirimkan data dari form, GET untuk menampilkan halaman hasil.
    Pada kamus new_alay.csv telah dilakukan penambahan dataset 

Rancangan URL

    GET /: menampilkan halaman utama dengan form input.
    POST /upload: menangani pengiriman file CSV dari form upload.
    POST /clean: menangani pengiriman teks dari form input dan memproses pembersihan teks.
    GET /result: menampilkan hasil pembersihan teks dalam bentuk tabel atau form.
