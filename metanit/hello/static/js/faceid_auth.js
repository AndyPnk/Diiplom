let videoStream; // Оголошення змінної для потоку відео

navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
        videoStream = stream; // Зберігаємо посилання на потік відео

        var video = document.createElement('video');
        video.srcObject = stream;
        video.autoplay = true;
        video.style.width = '50vw';
        document.body.appendChild(video);

        var videoDiv = document.getElementById('video-container');
        videoDiv.appendChild(video);

        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');

        var button = document.getElementById('button');

        button.onclick = function () {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);

            var imgData = canvas.toDataURL('image/png');

            var imgElement = document.createElement('input');
            imgElement.setAttribute("id", "photo")
            imgElement.setAttribute("name", "photo")
            imgElement.setAttribute("type", "image")
            imgElement.src = imgData;
            // var imgElement = document.createElement('input')

            // Встановлення типу "image" для елемента input
            //imgElement.setAttribute("type", "image");
            // imgElement.setAttribute("name", "photo");

            // Встановлення шляху до зображення
            imgElement.setAttribute("src", imgData);
            var videoDiv = document.getElementById('video-container');
            videoDiv.innerHTML = '';
            videoDiv.appendChild(imgElement);

            // Перевірка та зупинка попереднього відеопотоку, якщо він існує
            if (videoStream) {
                videoStream.getTracks().forEach(track => track.stop());
            }

            // Запуск нового відеопотоку після зупинки попереднього
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function (newStream) {
                    videoStream = newStream; // Оновлюємо посилання на новий потік
                    video.srcObject = newStream;
                })
                .catch(function (err) {
                    console.error('Помилка отримання доступу до камери:', err);
                });
        };
        send_button.onclick =async function () {
            var imgElement = document.getElementById('photo')
            var imgData = imgElement.src;
            fetch('/upload_photo_auth', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Може бути і 'application/x-www-form-urlencoded'
                    'X-CSRFToken': getCSRFToken() // Отримання CSRF-токена з Django (якщо потрібно)
                },
                body: JSON.stringify({ image: imgData }) // Або відформатований рядок зображення
            })
                .then(function (response) {
                    if (response.ok) {
                        window.location.href = "kab"
                    } else {
                        window.location.href = "LogIn"
                    }
                })
                .catch(function (error) {
                    // Обробка помилок, якщо fetch не вдалося виконати запит
                    console.error('Помилка fetch:', error);
                });
            function getCSRFToken() {
                var csrfToken = null;
                var cookies = document.cookie.split(';');
                cookies.forEach(function (cookie) {
                    var cookiePair = cookie.trim().split('=');
                    if (cookiePair[0] === 'csrftoken') {
                        csrfToken = decodeURIComponent(cookiePair[1]);
                    }
                });
                return csrfToken;
            }
        }
    })
    .catch(function (err) {
        console.error('Помилка отримання доступу до камери:', err);
    });

