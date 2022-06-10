// Add star rating

const rating = document.querySelector('form[name=rating]'); // Ищем форму по имени рейтинг

rating.addEventListener("change", function (e) { // Когда в этой форме происходит событие Change
    // Получаем данные из формы
    let data = new FormData(this); // Передадим все данные из полей
    fetch(`${this.action}`, { // С помощью fetch через url мы будем отправялть запрос url 'add_rating'
        method: 'POST',
        body: data // и в body будем передавать данные из полей
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
});
