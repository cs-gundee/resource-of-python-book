document.addEventListener('DOMContentLoaded', function () {

    document.querySelector('form').onsubmit = function() {

        // URL -д GET хүсэлтийг илгээх
        fetch('http://monxansh.appspot.com/xansh.json?currency=USD|EUR|JPY|CNY')
        // Хариуг json формат руу хөрвүүлэх
        .then(response => response.json())
        .then(data => {
            // Хэрэглэгчийн оруулсан валютыг аваад том үсэг рүү хөрвүүлэх
            const currency = document.querySelector('#currency').value.toUpperCase();
            // валютын ханшийг хадгалах хувьсагч
            let rate;
            // валют тус бүрийн мэдээлэлд хандах
            data.forEach(element => {
                if (element.code == currency) {
                    rate = element.rate;
                }
            });
            // Валют хүчинтэй эсэх
            if(rate !== undefined) {
                // Валютын ханшийн мэдээлэл харуулах
                document.querySelector('#result').innerHTML = `1 ${currency} = ${rate} төгрөг`;
            } else {
                // Тохиромжгүй утга оруулсан тохиолдолд
                document.querySelector('#result').innerHTML = `Тохиромжгүй утга оруулсан байна.`;
            }
        })
        // Алдаа гарвал консол дээр хэвлэх
        .catch(error => {
            console.log("Алдаа: ", error);
        });       
        return false;
    }

});