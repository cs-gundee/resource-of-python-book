document.addEventListener('DOMContentLoaded', function(){

    document.querySelector('form').onsubmit = function(){
        const fname = document.querySelector('#firstname').value;
        alert(`Сайн байна уу? ${fname}`);
    };

});