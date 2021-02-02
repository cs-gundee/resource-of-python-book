// Хуудсыг гүйлгэх үйлдлийг илрүүлэх Event listener
window.onscroll = () => {
    // Хуудасны доод талд хүрсэн
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        document.querySelector('body').style.background = 'purple';
    } else {
        document.querySelector('body').style.background = 'white';
    }
};

document.addEventListener('DOMContentLoaded', function() {
    const body = document.querySelector('body');
    for(i = 1; i < 100; i++) {
        let p = document.createElement('p');
        p.innerHTML = i;
        body.append(p);
    }
});