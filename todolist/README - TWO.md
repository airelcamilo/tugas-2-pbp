# Tugas 6 Assignment PBP

### Link : http://tugas-2-pbp-airel.herokuapp.com/todolist

***

## Perbedaan *Asynchronus* dan *Synchronous Programming*

| Asynchronus | Synchronous |
| --- | --- |
| Terdapat dalam *multi-threaded* model. | Terdapat dalam *single-threaded* model. |
| Operasi dapat berjalan bersamaan tanpa menunggu *response* dari operasi sebelumnya. | Operasi dilakukan satu per satu dan ketika ada operasi yang sedang berjalan, operasi lainnya harus menunggu. |
| *Request* dapat tidak langsung direspons. | *Request* perlu langsung direspons.
| Lebih cepat. | Lebih lama. |

***

## Paradigma *Event-Driven Progamming*

*Event-driven progamming* adalah paradigma dalam programming yang alur programnya diatur oleh *event* atau peristiwa, seperti tindakan pengguna (menekan tombol, menjalankan mouse), hasil dari sensor, atau pesan dari program lain.

Dalam *event-driven progamming* terdapat beberapa komponen, yaitu:
1. *Event* : Peristiwa yang muncul dalam sebuah sistem yang dapat berupa penekanan tombol, *timer*, hasil dari sensor, dll.

2. *Trigger* : Fungsi yang dijalankan ketika terjadi suatu *event* yang diinginkan.

3. *Event handler* : Komponen yang melakukan aksi ketika *event* terjadi.

4. *Event loop* : Komponen yang berfungsi mencari *event* pada sistem yang berbasis *event*.

Contoh *event-driven programming* dalam tugas ini adalah ketika user klik tombol `Add Task` di model, akan me-*request* AJAX POST. *Request* ini akan menyimpan data judul dan deskripsi task ke dalam *database* dan menampilkan data task tersebut di halaman web.

***

## Penerapan *Asynchronus Programming* pada AJAX

AJAX (*Asynchronous JavaScript And XML*) adalah teknologi web yang dapat mengirim dan mendapatkan informasi dari server dalam bentuk JSON, XML, HTML, dan teks. Dengan AJAX, halaman web dapat diperbarui secara asinkronus dimana hanya suatu bagian yang perlu diperbarui bukan seluruh halaman web. 

Berikut penerapan *asynchronus programming* dalam AJAX:

1. Suatu *event* terjadi di halaman web, seperti *load* halaman web atau tombol diklik user.
2. JavScript membuat objek XMLHttpRequest.
3. Objek XMLHttpRequest ini akan mengirim *request* ke server.
4. Server akan memproses *request* dan mengirim *response* ke halaman web.
5. JavaScript membaca *response* tersebut dan melakukan aksi yang sesuai.

***

## Implementasi

1. AJAX GET

    * Membuat *view* bernama `show_json` yang mengembalikan task user dalam bentuk JSON seperti di Lab 2.
        ```shell
        def show_json(request):
            task = Task.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", task), content_type="application/json")
        ```

    * *Routing* ke path `/todolist/json` di `urls.py`
        ```shell
        ...
        path('json/', show_json, name='show_json'),
        ...
        ```

    * Menambahkan `jQuery` *library* untuk memudahkan akses ke beberapa *Core API* yang ada.
        ```shell
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        ```

        Menambahkan AJAX GET *request* ke `/todolist/json/`. Untuk setiap task di JSON tersebut, digabung dengan sintaks HTML di fungsi `makeTask(task)` dan menambahkannya ke `<article>` dengan class `tasks`.
        ```shell
        function makeTask(task) {
            var html = "<section class='task-"+task.pk+" task card m-3'><h5 class='card-title'>"+task.fields.title+"</h5><h6 class='card-subtitle mb-2 text-muted'>"+task.fields.date+"</h6>";
            if (task.fields.is_finished) {
                html += "<p class='card-subtitle mb-2 text-muted'>Selesai</p>";
            } else {
                html += "<p class='card-subtitle mb-2 text-muted'>Belum Selesai</p>";
            }
            html += "<p class='card-text'>"+task.fields.description+"</p><div class='btn-group mt-auto' role='group'>";
            if (task.fields.is_finished) {
                html += "<a onclick='changeStatus("+task.pk+")' class='btn-hapus btn btn-success'>Belum Selesai</a>";
            } else {
                html += "<a onclick='changeStatus("+task.pk+")' class='btn-hapus btn btn-success'>Selesai</a>";
            }
            html += "<a onclick='deleteTask("+task.pk+")' class='btn btn-danger'>Delete</a></div></section>";
        }

        $(document).ready(function(){
            $.get("/todolist/json", function(data) {
                $.each(data, function(index, task) {
                    $('.tasks').append(makeTask(task));
                });
            });
        });
        ```

2. AJAX POST

    * Membuat tombol `Add Task` dengan ikon tambah yang akan *toggle* modal dengan id `add-task`
        ```shell
            <a class="btn btn-primary align-middle" data-bs-toggle="modal" data-bs-target="#add-task"><span class="material-symbols-outlined align-middle">add</span>Add Task</a>
        ```

        Membuat modal dengan id `add-task`, header 'Add Task' dan tombol close, serta body yang berisi form menambahkan task. Menyesuaikan modal dengan menambah animasi *fade*, memindahkan posisi menjadi di tengah, dan mengubah *background color* agar serasi dengan elemen lainnya.
        ```shell
        <div class="modal fade" id="add-task" tabindex="-1" >
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content card">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5">Add Task</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form method="POST">
                            {% csrf_token %}
                            {{ form.title.label_tag }}
                            {{ form.title }}
                            {{ form.description.label_tag }}
                            {{ form.description }}
                    
                            <div class="d-grid mt-4">
                                <input onclick="addTask();" class="btn btn-outline-primary" type="submit" value="Add Task" data-bs-dismiss="modal"/>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        ```

    * Membuat *view* bernama `add_task` untuk menambahkan task baru ke dalam *database*. Jika *request* yang diterima adalah POST, maka *view* akan membuat objek `ModelForm` baru yang berisi user, judul, dan deskripsi task. Kemudian, *view* ini akan mengembalikan task tersebut dalam bentuk JSON. Apabila tidak ada *request* POST, *view* tidak melakukan apa-apa.
        ```shell
        def add_task(request):
            if request.method == "POST":
                form = forms.CreateTask()
                instance = form.save(commit=False)
                instance.user = request.user
                instance.title = request.POST.get('title')
                instance.description = request.POST.get('description')
                instance.save()
                id = instance.pk

                task = Task.objects.filter(user=request.user, pk=id)
                return HttpResponse(serializers.serialize("json", task), content_type="application/json")
            return HttpResponse('')
        ```

    * *Routing* ke *path* `/todolist/add` di `urls.py`.
        ```shell
        ...
        path('add/', add_task, name='add_task'),
        ...
        ```

    * Menghubungkan form ke *path* `/todolist/add` dengan melakukan AJAX POST ke url tersebut apabila tombol `Add Task` ditekan.

    * Menambahkan kode di bawah ini ke tombol `Add Task` di modal untuk menutup modal setelah menambah task.
        ```shell
        data-bs-dismiss="modal"
        ```

    * Melakukan *refresh* secara *asinkronus* untuk menampilkan task setelah menekan tombol `Add Task`. Setelah menekan tombol, akan dilakukan *request* POST ke url `/todolist/add/` dengan data judul dan deskripsi task dari form serta CSRF Token-nya. Kemudian, *view* akan mengembalikan data task tersebut dalam JSON. Data tersebut akan digabung dengan sintaks HTML di fungsi `makeTask(task)` dan ditambahkan ke `<article>` dengan class `tasks`.
        ```shell
        $(".btn-add-task").click(function(e) {
            e.preventDefault();
            $.post("/todolist/add/", {title: $('#id_title').val(), description: $('#id_description').val(), csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()}, function(data) {
                $.each(data, function(index, task) {
                    $('.tasks').append(makeTask(task));
                });
            });
        });
        ```

***

## Bonus

Menambahkan fungsionalitas hapus dengan AJAX DELETE

1. Sudah membuat kolom baru dengan tombol hapus dari tugas sebelumnya. Tombol ini akan memanggil fungsi `deleteTask(pk)` dengan pk task tersebut.
    ```shell
    <a onclick='deleteTask("+task.pk+")' class='btn btn-danger'>Delete</a>
    ```

2. Memodifikasi fungsi `delete_task` di *view*. Fungsi ini akan menghapus task apabila *request* DELETE dan mengembalikan semua task user dalam bentuk JSON.
    ```shell
    def delete_task(request, id):
        if request.method == "DELETE":
            task = Task.objects.get(user=request.user, pk=id)
            task.delete()

            task = Task.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", task), content_type="application/json")
        return HttpResponse('')
    ```

3. Mengganti *routing* *path* `/todolist/delete-task/{id}` ke `/todolist/delete/{id}` di `urls.py`.
    ```shell
    ...
    path('delete/<int:id>', delete_task, name='delete_task'),
    ...
    ```

4. Membuat fungsi JavaScript bernama `deleteTask(pk)` yang memiliki argumen pk dari task tersebut dan yang memanggil *endpoint* penghapusan task, yaitu url `/todolist/delete-task/{pk}`.

5. Dalam fungsi `delete`, menambah kode AJAX yang akan *request* DELETE ke url `/todolist/delete-task/{pk}`, mempersiapkan CSRF Token, dan menghapus `<section>` yang memiliki class `task-{pk}`.
    ```shell
    function deleteTask(pk) {
    $.ajax({
        url: "/todolist/delete/"+pk,
        method: "DELETE",
        dataType: "json",
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        },
        success: function(data) {
            $('.task-'+pk).remove();
        }
    });
    ```

***

## Credits

Sumber jawaban pertanyaan nomor 1 [Asynchronous vs. Synchronous Programming: Key Similarities and Differences](https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/)

Sumber jawaban pertanyaan nomor 2 [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming) dan [Solace - Event Driven](http://www.myspsolution.com/news-events/solace-event-driven/)

Sumber jawaban pertanyaan nomor 3 [Lab 5: JavaScript dan AJAX](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-5)