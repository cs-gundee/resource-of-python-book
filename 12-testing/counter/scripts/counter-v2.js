// Хуудас ачаалагдахыг хүлээх
document.addEventListener('DOMContentLoaded', () => {

    // Тоолуур хувьсагч
    let counter = 0;

    // Хэрэв нэмэх товч дээр дарсан бол тоолуур хувьсагчийг нэмэгдүүлж, innerHTML -г өөрчлөх
    document.querySelector('#add').onclick = () => {
        counter++;
        document.querySelector('h1').innerHTML = counter;
    }

    // Хэрэв хасах товч дээр дарсан бол тоолуур хувьсагчийг хорогдуулж, innerHTML -г өөрчлөх
    document.querySelector('#subtract').onclick = () => {
        counter++;
        document.querySelector('h1').innerHTML = counter;
    }
});