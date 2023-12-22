$(document).ready(function () {
    var video = $('<video autoplay style="width: 50vw;"></video>');
    var videoDiv = $('#video-container');
    var canvas = $('<canvas></canvas>')[0]; // Отримання DOM-елементу з jQuery-об'єкту
    var context = canvas.getContext('2d');
    var imgElement;
    var button = $('#button');
    var newPicButton = $('#new-pic');

    function startStream() {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video[0].srcObject = stream; // Встановлення srcObject через властивість DOM-елементу
                videoDiv.empty().append(video);

                button.on('click', function () {
                    canvas.width = video[0].videoWidth;
                    canvas.height = video[0].videoHeight;
                    context.drawImage(video[0], 0, 0, canvas.width, canvas.height);

                    var imgData = canvas.toDataURL('image/png');
                    imgElement = $('<img>').attr('src', imgData);

                    video.remove();
                    videoDiv.append(imgElement);
                    button.text('Верифікувати✅');
                });

                newPicButton.on('click', function () {
                    video = $('<video autoplay style="width: 50vw;"></video>');
                    videoDiv.empty().append(video);
                    button.text('Зробити фото');
                    startStream(); // Перезапуск скрипту для отримання нового відеопотоку
                });
            })
            .catch(function (err) {
                console.error('Помилка отримання доступу до камери:', err);
                alert('Помилка отримання доступу до камери. Перевірте консоль для деталей.');
            });
    }

    startStream(); // Запуск функції для отримання відеопотоку
});
