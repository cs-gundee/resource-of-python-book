// Бичвэрийн эхлэл
let counter = 1;

// Нэг дор 10 бичвэрийг ачаалах
const quantity = 10;

// DOM ачаалах үед эхний 10 бичвэрийг үзүүлэх
document.addEventListener('DOMContentLoaded', load);

// Хуудасны төгсгөлд хүрсэн бол дараагийн 10 бичвэрийг ачаалах
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Нуух товч дээр дарвал бичвэрийг устгах функц
document.addEventListener('click', event => {

    // Дарагдсан элементийг олох
    const element = event.target;

    // Нуух товч дээр дарсан бол
    if (element.className === 'hide') {
        //element.parentElement.remove()
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove();
        });
    }
    
});

// Бичвэрүүдийг ачаалах
function load() {
    // Бичвэрийн эхлэл, төгсгөлийн цэгийг тохируулах, counter хувьсагчийн утгыг шинэчлэх
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Шинэ бичвэр татаж авах, бичвэр нэмэх
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
    })
};

// Шинэ бичвэрийг DOM -д нэмэх
function add_post(contents) {
    const post = document.createElement('div');
    post.className = 'post';
    //post.innerHTML = contents;
    post.innerHTML = `${contents} <button class="hide">Нуух</button>`;

    document.querySelector('#posts').append(post);
};