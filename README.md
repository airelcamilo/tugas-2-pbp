# Lab 1 Assignment PBP

### Link Heroku App: https://tugas-2-pbp-airel.herokuapp.com/katalog

***

## Bagan Urls, Views, Models, dan Template
Bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`

![bagan-request-response-django](./bagan-request-response-django.png)

Ketika pengguna meminta suatu halaman website, URL router `urls.py` akan mencocokan *path* permintaan tersebut dengan pola URL yang tersedia. Apabila ada yang cocok, `urls.py` akan meneruskannya ke `views.py` yang sesuai. `views.py` merupakan logika dari suatu halaman web yang akan memanggil `models.py` apabila membutuhkan *read/write* data dari *database*. Setelah permintaan diproses, `views.py` akan memetakan data dari *database* ke dalam berkas template `HTML`. Barulah template `HTML` tersebut, ditampilkan ke pengguna sebagai respons.

***
## Alasan Menggunakan Virtual Environment
Virtual environment adalah sebuah folder yang dibutuhkan untuk menjalankan Python yang ringan dan terisolasi.

Manfaat menggunakan virtual environment, yaitu:
1. Dapat meng-*install* lebih dari satu versi *package*. Misalkan kita membuat dua aplikasi yang membutuhkan versi Django yang berbeda, jika tidak menggunakan virtual environment, versi Django yang baru di *install* akan menjadi versi yang default sehingga susah untuk mengerjakan dua aplikasi tersebut.

2. Agar *package* yang di install hanya *package* yang diperlukan saja. Jika tidak menggunakan virtual environment, *package* yang dibutuhkan di projek lain mungkin dapat memengaruhi pembuatan aplikasi Django secara tidak sengaja.

Sebenarnya pembuatan aplikasi Django tanpa menggunakan virtual environment dibolehkan, tetapi tidak dianjurkan agar dapat meng-*install* lebih dari satu versi *package*, terhindar dari masa;ah *dependencies*, dan *package* yang di-*install* seperlunya saja sehingga tidak dipengaruhi *package* lain.

***
## Implementasi
1. Membuat sebuah fungsi pada `views.py` untuk melakukan pengambilan data dari model dan dikembalikan ke HTML.
   * Sebelumnya, menjalankan beberapa perintah di bawah untuk migrasi skema model dan memasukkan data `initial_catalog_data.json` ke dalam *database* Django lokal.
      ```shell
      python manage.py makemigrations
      python manage.py migrate
      python manage.py loaddata initial_catalog_data.json
      ```

   * Lanjut ke potongan kode `views.py`:
      ```shell
      from katalog.models import CatalogItem

      def show_katalog(request):
         data_katalog = CatalogItem.objects.all()
         context = {
            'list_katalog': data_katalog,
            'name': 'Airel Camilo Khairan',
            'id': '2106652581'
         }
         return render(request, "katalog.html", context)
      ```
      Penjelasan: Pertama melakukan *import* class `CatalogItem` dari file `models.py`. Kemudian, *assign* variabel `data_katalog` dengan semua data `CatalogItem` yang ada dan dimasukkan ke dictionary `context` bersama nama dan npm. Terakhir, memasukkan `context` sebagai argumen dari fungsi `render`. Fungsi `render` berfungsi untuk menggabungkan file template HTML dengan `context` dan menghasilkan objek `HttpResponse`.

2. Membuat routing untuk memetakan fungsi pada `views.py`
   * Berikut potongan kode `urls.py` di folder `project_django`:
      ```shell
      ...
      path('katalog/', include('katalog.urls'))
      ...
      ```
      Penjelasan: Menambahkan potongan kode tersebut, agar ketika membuka http://localhost:8000/katalog/ akan menjalankan kode `urls.py` di folder `katalog`. 
      
   * Selanjutnya di `urls.py` folder `katalog` menambahkan potongan kode ini.
      ```shell
      from katalog.views import show_katalog

      app_name = 'katalog'

      urlpatterns = [
         path('', show_katalog, name='show_katalog'),
      ]
      ```
      Penjelasan: Saat membuka http://localhost:8000/katalog/, potongan kode tersebut akan menjalankan fungsi `show_katalog` yang berada di `views.py`

3. Memetakan data ke dalam HTML dengan sintaks dari Django.
   * Mengganti kata *Fill me!* di bawah *Name* dan *Student ID:* dengan data `name` dan `id` yang tersedia di `context`.
      ```shell
      <h5>Name: </h5>
      <p>{{name}}</p>

      <h5>Student ID: </h5>
      <p>{{id}}</p>
      ```
   
   * Kemudian, menambahkan *for loop* di bawah comment untuk menampilkan baris tabel baru yang berisi setiap `item` di dalam `list_katalog`. Setiap baris berisi data nama, harga, stok, deskripsi, serta link url dari item tersebut.
      ```shell
      {% for item in list_katalog %}
      <tr>
         <td>{{item.item_name}}</td>
         <td>{{item.item_price}}</td>
         <td>{{item.item_stock}}</td>
         <td>{{item.rating}}</td>
         <td>{{item.description}}</td>
         <td>{{item.item_url}}</td>
      </tr>
      {% endfor %}
      ```

4. Melakukan `deployment` ke Heroku
   1. Log in ke akun Heroku.
   2. Klik tombol `New -> Create new app`.
   3. Masukkan nama app, yaitu `tugas-2-pbp-airel` dan klik `Create app`.
   4. Klik `Account settings` dan copy `API key`.
   5. Masuk ke repository github `https://github.com/airelcamilo/tugas-2-pbp`.
   6. Klik `Settings -> Secrets -> Actions -> New repository secret`.
   7. Buat variabel `HEROKU_API_KEY` dan masukkan `API key` yang di copy tadi serta variabel `HEROKU_APP_NAME` dan masukkan nama app, yaitu `tugas-2-pbp-airel`.
   8. Selesai, aplikasi dapat diakses di `https://tugas-2-pbp-airel.herokuapp.com/katalog`.

***
## Credits

Memanfaatkan template dari [Github PBP Ganjil 22/23](https://github.com/pbp-fasilkom-ui/assignment-repository)

Sumber jawaban pertanyaan nomor 1 [Django: Request/Response Cycle](https://medium.com/@ksarthak4ever/django-request-response-cycle-2626e9e8606e) dan [Lab 1 - PBP Ganjil 22/23](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1)

Sumber jawaban pertanyaan nomor 2 [Real Python - Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments)