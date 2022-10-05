# Tugas 5 Assignment PBP

### Link : tugas-2-pbp-airel.herokuapp.com/todolist

***

## Perbedaan Inline, Internal, External CSS

Perbedaan:
| Inline | Internal | External |
| --- | --- | --- |
| Menambahkan CSS style langsung di elemen HTML, contoh: <br>`<p style="color: red;"></p>` | Menambahkan CSS style dalam tag `<style>` dalam `<head>`, contoh: <br>`<style type="text/css">h1{margin: 20px}</style>`| Menambah CSS style dalam file eksternal `.css` dan di `<head>` HTML ditambahkan link yang merujuk ke file tersebut `<link rel="stylesheet" type="text/css" href="style.css" />`.

1. Inline CSS

    * Kelebihan: <br>Dapat dengan mudah menambahkan style CSS ke dalam elemen HTML. 
    <br>
    Tidak perlu membuat file CSS baru.

    * Kekurangan: <br>Menambah style CSS ke setiap elemen HTML memakan waktu yang lama.<br>Ukuran file HTML akan menjadi besar.

2. Internal CSS

    * Kelebihan:<br>Dapat menggunakan ID dan Class Selectors dalam menambahkan style.<br>Tidak perlu membuat file baru.

    * Kekurangan: <br>Ukuran file HTML akan menjadi besar.

3. External CSS

    * Kelebihan: <br> Style disimpan di file yang berbeda sehingga kode HTML lebih bersih dan ukuran lebih kecil. <br> File `.css` dapat digunakan untuk banyak file HTML.

    * Kekurangan: <br> Halaman web akan ditampilkan dengan benar saat file CSS eksternal dimuat.

***

### Macam-Macam Tag HTML

| Tag | Deskripsi | Tag | Deskripsi |
| --- | --- | --- | --- |
| `<html>` | Membuat dokumen HTML |  `<br>` | Membuat jeda baris |
| `<title>` | Membuat judul halaman | `<!--...-->` | Membuat komentar |
| `<body>` | Membuat tubuh halaman | `<img>` | Memuat gambar |
| `<h1> - <h6>` | Membuat heading | `<a>` | Membuat *hyperlink* | 
| `<p>` | Membuat paragraf | `<table>` | Membuat tabel |
| `<ul>` | Membuat *unordered list* | `<tr>` | Membuat baris dalam tabel |
| `<ol>` | Membuat *ordered list* | `<th>` | Membuat sel *header* dalam tabel |
| `<li>` | Membuat item *list* | `<td>` | Membuat sel data dalam tabel |
| `<div>` | Membuat generik kontainer | `<nav>` | Membuat *navigation bar* |
| `<style>` | Memuat kode CSS | `<script>` | Membuat script sisi klien (JavaScript) |
| `<header>` | Membuat *header* | `<footer>` | Membuat *footer* |
| `<section>` | Membuat bagian | `<article>` | Membuat artikel |
| `<aside>` | Membuat konten yang terkait secara tidak langsung dengan konten utama | `<link>` | Membuat hubungan antara dokumen dengan file eksternal |

Dan masih banyak tag yang lain ...

***

## Macam-Macam CSS Selector

1. Elemen Selector

    Memilih elemen HTML berdasarkan nama elemen, contoh:
    <br>```p {color: blue;}```

2. ID Selector

    Memilih elemen HTML berdasarkan id elemen dengan menulis #{nama-id}. Id merupakan atribut yang unik untuk setiap elemen, contoh:
    <br>```#username {text-align: center;}```

3. Class Selector

    Memilih elemen HTML berdasarkan class elemen dengan menulis .{nama-class}. Class merupakan atribut yang dapat dimasukkan ke lebih dari satu elemen, contoh:
    <br>```.card {display: flex;}```

4. Universal Selector

    Memilih setiap elemen yang ada di dokumen HTML, contoh:
    <br>```* {background-color: green;}```

5. Grouping Selector

    Mengelompokkan semua elemen HTML yang memiliki *style* yang sama.
    <br>```h1, p {color: red;}```

***

## Implementasi No 1
1. Background

    Mengubah background menjadi linear gradient. 
    `body {background: linear-gradient(216deg, rgba(255, 255, 255, 1) 0%, rgba(210, 210, 255, 1) 96%) no-repeat fixed;}`

2. Elemen yang memiliki class `login`, `tasks`, dan `create-task` menggunakan pengaturan layout *flex* dan dapat *wrap*. Kemudian, setiap anak elemen yang ada di dalamnya dibuat berada di tengah.
    ```shell
    .login, .tasks, .create-task {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
    }
    ```

3. Mengubah margin dan arah *flex* yang diberlakukan pada elemen yang memiliki class `login`, `tasks`, dan `create-task`. Elemen `login` dan `create-task` berarah kolom dan `tasks` berarah baris.
    ```shell
    .login, .create-task {
        height: 100vh;
        margin: 0 auto auto auto;
        flex-direction: column;
    }
    .tasks {
        margin: 2rem;
        flex-direction: row;
    }
    ```

4. Menambahkan class `card` ke dalam form login, form register, form menambah task baru, dan setiap task. 
    Class `card` adalah custom class style dari Bootstrap untuk membuat kartu. Lalu, saya ubah warna background dari kartu tersebut.
    ```shell
    .card {
        background-color: rgb(183, 183, 255);
    }
    ```

5. Menggunakan custom style tombol dari Bootstrap untuk semua tombol yang dibuat. Caranya dengan menambahkan clas `btn` dan `btn-{warna}` atau `btn-outline-{warna}`. Dokumentasi lebih lengkap [di sini](https://getbootstrap.com/docs/4.0/components/buttons/)

6. Mengubah tinggi baris tabel di `login.html`, `register.html`, dan `create_task.html` dan menambahkan class `form-control` di setiap input `create_task.html` dengan mengubah class `CreateTask` di `forms.py`.
    ```shell
    <table>
        <tr style="height: 30px;">
            <td>{{ form.title.label_tag }}</td>
        </tr>
        ...
    ```
    ```shell
    class CreateTask(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(CreateTask, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
                field.required = False
    ```

7. Memasukkan class `card` yang sesuai untuk setiap elemen `task` di `todolist.html`. Dokumentasi lebih lengkap [di sini](https://getbootstrap.com/docs/4.0/components/card/)
    ```shell
    Di todolist.html
    {% for task in tasks %}
        <section class="task card m-3">
            <h5 class="card-title">{{task.title}}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{task.date}}</h6>
            {% if task.is_finished %}
                <p class="card-subtitle mb-2 text-muted">Selesai</p>
            {% else %}
                <p class="card-subtitle mb-2 text-muted">Belum Selesai</p>
            {% endif %}
            <p class="card-text">{{task.description}}</p>
            <div class="btn-group mt-auto" role="group">
                {% if task.is_finished %}
                    <a class="btn btn-success" href="{% url 'todolist:change_status' task.id %}">Belum Selesai</a>
                {% else %}
                    <a class="btn btn-success" href="{% url 'todolist:change_status' task.id %}">Selesai</a>
                {% endif %}
                <a class="btn btn-danger" href="{% url 'todolist:delete_task' task.id %}">Delete</a>
            </div>
    </section>
    {% endfor %}
    ```

8. Menambah *navigation bar* di `todolist.html` berisi *username* dan tombol *logout*.
    ```shell
    Di todolist.html
    <nav class="navbar">
        <span class="navbar-brand mx-1 mb-0 p-3 h5">Hello! {{user}}</span>
        <a class="btn btn-outline-primary mx-3" href="{% url 'todolist:logout' %}">Logout</a>
    </nav>
    ```
    ```shell
    Di style.css
    nav {
        box-shadow: 0px 0px 20px -10px rgb(60, 60, 60);
        background-color: rgb(183, 183, 255);
    }
    ```

    Kemudian, menambahkan icon dan memindahkan title beserta tombol Tambah Task Baru ke tengah.
    ```shell
    Di base.html
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    ```
    ```shell
    Di todolist.html
    <div class="text-center title">
        <h1 class="text-center"><span class="material-symbols-outlined">checklist_rtl</span> My Todolist</h1>

        <a class="btn btn-primary align-middle" href="{% url 'todolist:create_task' %}"><span class="material-symbols-outlined align-middle">add</span> Tambah Task Baru</a>
    </div>
    ```

***

# Implementasi No 2

1. Saat ukuran layar <=705px, maka tinggi task akan sesuai dengan tinggi semua elemen dan panjang selayar. Jika ukuran layar > 700px, maka tinggi layar *fixed*, yaitu sebesar 16rem dan *scrollable*.
    ```shell
    @media only screen and (max-width: 705px) {
        .task {
            width: 100%;
            height: auto;
        }
    }
    ```

2. Sementara saat ukuran kayar <=500px, mengubah lebar kartu di `create_task.html` dan mengubah ukuran elemen yang menggunakan class `navbar-brand`, yaitu *username* sehingga akan memotong teks *username* tersebut.
    ```shell
    .navbar-brand {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    @media only screen and (max-width: 500px) {
        .create-task>.card {
            width: 70%;
        }

        .navbar-brand {
            max-width: 200px;
        }
    }
    ```

***

## Bonus
Menambah ukuran dari card dan mengubah warna menjadi lebih gelap ketika melakukan hover pada card di halaman utama todolist.
```shell
.task {
    width: 18rem;
    height: 16rem;
    overflow-y: auto;
    background-color: rgb(183, 183, 255);
    transition: all .1s ease-in-out;
}
.task:hover, .task:active {
    background-color: rgb(173, 173, 255);
    transform: scale(1.01);
}
```

***

## Credits
Sumber jawaban pertanyaan nomor 1 [Types of CSS: Inline, External and Internal Definitions and Differences Explained
](https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css)

Sumber jawaban pertanyaan nomor 2 [Tag-tag Pada HTML beserta Fungsinya](https://gilacoding.com/read/tag-tag-pada-html-beserta-fungsinya)

Sumber jawaban pertanyaan nomor 3 [CSS Selectors](https://www.w3schools.com/css/css_selectors.asp)

***

<details>
  <summary>Tugas 4</summary>

# Tugas 4 Assignment PBP

### Link : tugas-2-pbp-airel.herokuapp.com/todolist

***

## Kegunaan `{% csrf_token %}`

Kegunaan `{% csrf_token %}` adalah untuk melindungi user dari serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika user masuk ke halaman web jahat yang berisi link, tombol, atau kode JavaScript yang melakukan *request* ke halaman web kita. *Request* tersebut akan memaksa user untuk melakukan suatu perbuatan yang tidak diinginkan di halaman web kita dengan autentikasi user yang disimpan di *cookies*.

***

## Membuat Elemen `<form>` Tanpa *Generator*

Kita dapat membuat sebuah form secara manual tanpa menggunakan *generator*. Caranya adalah dengan memanggil satu per satu *field* dengan `{{ form.name_of_field }}`. Selain itu ada `{{ form.name_of_field.label_tag }}` untuk menampilkan label dari *field* dan `{{ form.name_of_field.errors }}` untuk menampilkan pesan error dari *field*.

Akan tetapi, ada kekurangan dari metode ini. Dengan menggunakan *generator*, pesan error akan secara automatis ditampilkan tetapi tidak jika tidak menggunakan *generator*, kita harus menampilkan sendiri pesan error tersebut.

***

## Alur Data

Alur data dari submisi yang dilakukan pengguna adalah sebagai berikut:
1. User menekan tombol `Tambah Task Baru` di `/todolist` dan dialihkan ke halaman `/todolist/create-task` dan memanggil fungsi `create_task` di `views.py`.
2. Fungsi `create_task` akan menghasilkan `create_task.html` yang berisi form.
3. Di halaman `/todolist/create-task`, pengguna mengisi judul dan deskripsi task di form dan menekan tombol `Tambah Task Baru`.
4. Saat menekan tombol, akan meminta `request POST` ke fungsi `create_task` dan fungsi tersebut akan memetakan data di form ke `Task` dalam `models.py` untuk menyimpan data.
5. Kemudian, user akan dialihkan kembali ke `/todolist`.
6. Untuk membuka `/todolist`, harus memanggil `show_todolist` yang akan menampilkan halaman web `todolist.html` beserta data terbaru user tersebut.

***

## Implementasi

1. Membuat Aplikasi `todolist`
   
   Membuat aplikasi baru di Django dengan nama `todolist` dengan mengetik kode:
   ```shell
   python manage.py startapp todolist
   ```

   Kemudian membuka `settings.py` di folder `project_django` dan menambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS`.

   ```shell
   INSTALLED_APPS = [
      ...,
      'todolist',
   ]
   ```

2. Menambah Path `todolist`
   
   Menambahkan potongan kode di bawah ini di `project_django\urls.py`  agar dapat mengakses http://localhost:8000/todolist:
   ```shell
   ...
   path('todolist/', include('todolist.urls'))
   ...
   ``` 

3. Membuat Model `Task`
   
   Membuat class `Task` di `models.py` dan di dalamnya ada beberapa atribut, yaitu `user` yang berelasi dengan `User`, `date` yaitu `Date` yang merupakan tanggal saat task dibuat,`title` dengan tipe `Character` dan panjang kata maksimum 100 kata, dan `description` yang bertipe `Text`.
   ```shell
   from django.contrib.auth.models import User
    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now_add=True)
        title = models.CharField(max_length=100)
        description = models.TextField()
   ```

   Jangan lupa untuk migrasi skema model ke *database* Django lokal
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Implementasi Form Registrasi, *Login*, dan *Logout*

    Dengan mengikuti [Tutorial 3](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3)

    * Form Registrasi

        Tambahkan potongan kode di bawah ini ke `views.py` untuk menghasilkan formulir registrasi secara otomatis dan membuat akun.
        ```shell
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages

        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    return redirect('todolist:login')
            
            context = {'form':form}
            return render(request, 'register.html', context)
        ```

        Kemudian membuat `register.html` di `templates` yang memuat *template*-nya.
        ```shell
        {% extends 'base.html' %}
        {% block meta %}
        <title>Registrasi Akun</title>
        {% endblock meta %}

        {% block content %}  
        <div class = "login">
            <h1>Formulir Registrasi</h1>  
                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}
        </div>  
        {% endblock content %}
        ```
    
    * Membuat Form `Login`

        Tambahkan potongan kode di bawah ini ke `views.py` untuk mengautentikasi user yang login.
        ```shell
        from django.contrib.auth import authenticate, login
        def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:show_todolist')
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)
        ```

        Kemudian membuat `login.html` di `templates` yang memuat *template*-nya.
        ```shell
        {% extends 'base.html' %}
        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>
        </div>

        {% endblock content %}
        ```

    * Membuat Fungsi `Logout`

        Tambahkan potongan kode di bawah ini ke `views.py` untuk melakukan mekanisme *logout*.
        ```shell
        from django.contrib.auth import logout
        def logout_user(request):
            logout(request)
            return redirect('todolist:login')
        ```

        Kemudian menambahkan tombol *logout* di `todolist.html`.
        ```shell
        <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
        ```

5. Membuat Halaman `todolist` 

    Di dalam `views.py` menambahkan fungsi `show_todolist` yang akan menampilkan *template* `todolist.html` dengan *username* dan task user tersebut. Fungsi ini akan dijalankan ketika user sudah login terlebih dahulu.
    ```shell
    @login_required(login_url='/todolist/login/')
    def show_todolist(request):
        tasks = Task.objects.filter(user=request.user)
        context = {
            'user' : request.user,
            'tasks' : tasks,
        }
        return render(request, 'todolist.html', context)
    ```

    Kemudian `todolist.html` akan menampilkan *username*, tombol `Tambah Task Baru` yang *routing* ke  `/create-task`, tombol *logout* yang routing ke `/logout`, beserta task yang disediakan dalam bentuk tabel.
    ```shell
    ...
    <h1>Tugas 4 Assignment PBP/PBD</h1>
    <h3>Username: {{user}}</h3>
    <button><a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a></button>
    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>

    <table>
        <tr>
            <th>Date</th>
            <th>Title</th>
            <th>Description</th>
            <th>Status</th>
        </tr>
        
        {% for task in tasks %}
        <tr>
            <td>{{task.date}}</td>
            <td>{{task.title}}</td>
            <td>{{task.description}}</td>
        </tr>
        {% endfor %}
    </table>
    ...
    ```

6. Membuat Halaman Form Pembuatan Task

    Pertama-tama, membuat file `forms.py` yang berisi class `CreateTask` untuk memetakan model `Task` ke `HTML` form elemen. Semua data dimasukkan kecuali `user` dan `date`, dengan `user` akan terisi nanti dan `date` dengan tanggal saat ini.
    ```shell
    from django import forms
    from . import models

    class CreateTask(forms.ModelForm):
        class Meta:
            model = models.Task
            fields = '__all__'
            exclude = ['user']
    ```

    Kemudian di dalam `views.py` menambahkan fungsi `create_task` untuk menampilkan *template* `create_task.html` dengan form `CreateTask`. Selain itu di dalam fungsi tersebut, akan menyimpan data yang dimasukkan beserta *username* dan kembali ke `/todolist` apabila ada *request* `POST`. Fungsi tersebut akan dijalankan ketika user sudah login terlebih dahulu.
    ```shell
    @login_required(login_url='/todolist/login/')
    def create_task(request):
        form = forms.CreateTask()

        if request.method == "POST":
            form = forms.CreateTask(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('todolist:show_todolist')
                
        context = {'form':form}
        return render(request, 'create_task.html', context)
    ```

    Terakhir, memasukkan `title` dan `description` *field* dari form  ke dalam `create_task.html`.
    ```shell
    {% extends 'base.html' %}
    {% block meta %}
    <title>Tambah Task Baru</title>
    {% endblock meta %}

    {% block content %}  
    <div class = "create-task">
        <h1>Tambah Task Baru</h1>  

        <form method="POST" action={% url 'todolist:create_task'%}>
            {% csrf_token %}
            <table>
                <tr>
                    <td>{{ form.title.label_tag }}</td>
                    <td>{{ form.title }}</td>
                </tr>
                <tr>
                    <td>{{ form.description.label_tag }}</td>
                    <td>{{ form.description }}</td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="Tambah Task Baru"/></td>
                </tr>
            </table>
        </form>
    </div>  
    {% endblock content %}
    ```

7. *Routing*

    Untuk *routing* semua URL tersebut, menambahkan *path* URL ke masing-masing fungsi di `views.py` dan dilakukan di file `urls.py`.
    ```shell
    from todolist.views import *
    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('create-task/', create_task, name='create_task'),
        path('logout/', logout_user, name='logout'),
    ]
    ```

8. *Deployement* ke Heroku
    
    Karena *repository* ini sudah di *deploy* untuk Tugas sebelumnya, tidak perlu mengulang membuat aplikasi di Heroku dan menambah Secret ke *repository*. 

9. Membuat 2 Akun Pengguna dan 3 Dummy Data
    
    * Akun pertama:
        
        Username: `dummy`
        
        Password: `dummypass564`
        
        Data: `[[Kerjain tugas PBP, Bentar lagi deadline!!], [Laundry. Baju mau habis], [Rapat, Ikut rapat Gladiatos]]`

    * Akun kedua:
        
        Username: `pran`
        
        Password: `pransocool`
        
        Data: `[[Beli whiskas, Buat kucing kesayangan], [Ke TA, Jemput adek nonton], [Belajar kuis StatProb, Biar dapet nilai 100]]`


***

# Bonus

1. Menambahkan atribut `is_finished` ke model `Task` di `models.py` dengan *default value* `False`.
    ```shell
    ...
    is_finished = models.BooleanField(default=False)
    ```

    Jangan lupa untuk migrasi skema model ke *database* Django lokal
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

    Membuat dua kolom baru pada tabel task yang berisi status dan tombol untuk mengubah status. Tombol ubah status akan mengalihkan user ke `change_status` di `urls.py` dengan argumen `id` dari task yang mau diubah statusnya.
    ```shell
    ...
    {% if task.is_finished %}
        <td>Selesai</td>
        <td><button><a href="{% url 'todolist:change_status' task.id %}">Belum Selesai</button></td>
    {% else %}
        <td>Belum Selesai</td>
        <td><button><a href="{% url 'todolist:change_status' task.id %}">Selesai</button></td>
    {% endif %}
    ...
    ```

    Kemudian, di `urls.py` akan me-*routing* URL `/todolist/change_status/id` untuk memanggil fungsi `change_status` di `views.py`.
    ```shell
    ...
    path('change-status/<int:id>', change_status, name='change_status'),
    ...
    ```

    Pada fungsi `change_status` di `views.py`, akan menegasi status dari task dengan user dan id yang sama lalu kembali ke `/todolist`.
    ```shell
    def change_status(request, id):
        task = Task.objects.get(user=request.user, pk=id)
        task.is_finished = not task.is_finished
        task.save()
        return redirect('todolist:show_todolist')
    ```

2. Di `todolist.html`, menambahkan kolom baru pada tabel task yang berisi tombol untuk menghapus suatu task. Tombol tersebut akan mengalihkan user ke `delete_task` di `urls.py` dengan argumen `id` task yang mau dihapus.
    ```shell
    ...
    <td><button><a href="{% url 'todolist:delete_task' task.id %}">Delete</button></td>
    ...
    ```

    Kemudian, di `urls.py` menambahkan *path* untuk *routing* URL `/todolist/delete-task/id` untuk memanggil fungsi `delete_task` di `views.py`.
    ```shell
    ...
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    ...
    ```

    Pada fungsi `delete_task` di `views.py`, menghapus task yang sesuai dengan id dan kembali ke `/todolist`.
    ```shell
    def delete_task(request, id):
        task = Task.objects.get(user=request.user, pk=id)
        task.delete()
        return redirect('todolist:show_todolist')
    ``` 

***

# Credits

Sumber pertanyaan pertama: [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/csrf/) dan [Stackhawk Django CSRF Protection](https://www.stackhawk.com/blog/django-csrf-protection-guide/)

Sumber pertanyaan kedua: [Django Documentation](https://docs.djangoproject.com/en/4.1/topics/forms/)

Sumber pertanyaan ketiga: [Slide Kuliah](https://scele.cs.ui.ac.id/pluginfile.php/161881/mod_resource/content/1/05%20-%20Form%2C%20Authentication%2C%20Session%2C%20and%20Cookie.pdf)
</details>