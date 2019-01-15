// Функция валидации ввдённого номера телефона
function isNormalInteger(str){
    var n = Math.floor(Number(str));
    return n !== Infinity && String(n) === str && n >= 0;
}

// Функция отправки запроса на сервер для внесения контакта в БД.
function AddOnClick(){
    var result = document.getElementById("Result"); // результат запроса
    result.innerHTML = null;                        // начальное состояние null

    var contactNameElem = document.getElementById("ContactName");   // Форма с именем контакта
    var contactPhoneElem = document.getElementById("ContactPhone"); // Форма с номером контакта

    var obj = {};
    obj.name = contactNameElem.value; // Значение имени из формы
    if(isNormalInteger(contactPhoneElem.value)){
       obj.phone = parseInt(contactPhoneElem.value); // Проверка ввода номера телефона, допускаются только цифры
    }
    else{
        result.innerHTML = "Телефон указан некорректно! Формат: 89887776655";
        return; // Иначе результат запроса вернёт ругальное слово :)
    }

    // Асинхронная передача запросов на сервер
    fetch('http://127.0.0.1/contact/', {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json; charset=utf-8'
         },
         body: JSON.stringify(obj),
    })
    .then(
        function (response)
        {
            response.json().then(
                function(data) {
                   result.innerHTML = data.result;
            });
        }
    )
    .catch(alert);
}

// Функция отправки запроса на сервер для поиска контакта в БД.
function FindOnClick() {
    var result = document.getElementById("Result"); // результат запроса
    result.innerHTML = null;                        // обнуление результата

    var contactNameElem = document.getElementById("ContactName");   // Форма с именем контакта
    var contactPhoneElem = document.getElementById("ContactPhone"); // Форма с номером контакта
    contactPhoneElem.value = null;                                  // обнуление формы номера телефона

    // Асинхронная передача запросов на сервер
    fetch('http://127.0.0.1/contact/' + contactNameElem.value, {
    method: "GET",
    })
    .then(
        function (response)
        {
            response.json().then(function(data) {
              if (data && data.phone) {
                  contactPhoneElem.value = data.phone
              }
              else {
                  result.innerHTML = "Контакт не найден!";
              }
            });
        }
    )
    .catch(alert);
}