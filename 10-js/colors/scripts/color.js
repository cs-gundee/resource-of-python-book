/*
document.addEventListener('DOMContentLoaded', function(){

    // улаан өнгөтэй болгох
    document.querySelector('#red').onclick = function(){
        document.querySelector("#greeting").style.color = 'red';
    }

    // шар өнгөтэй болгох
    document.querySelector('#yellow').onclick = function(){
        document.querySelector("#greeting").style.color = 'yellow';
    }

    // ногоон өнгөтэй болгох
    document.querySelector('#green').onclick = function(){
        document.querySelector("#greeting").style.color = 'green';
    }
});
*/

/*
document.addEventListener('DOMContentLoaded', () => {
 
    document.querySelectorAll('button').forEach(function(button){
        button.onclick = function(){
            document.querySelector('#greeting').style.color = button.dataset.color;
        }
    });
});
*/

// arrow function
/*
document.addEventListener('DOMContentLoaded', () => {
 
    document.querySelectorAll('button').forEach(button => {
        button.onclick = () => {
            document.querySelector('#greeting').style.color = button.dataset.color;
        }
    });
});
*/

document.addEventListener('DOMContentLoaded', () => {
 
    document.querySelector('select').onchange = function() {
        document.querySelector('#greeting').style.color = this.value;
        }
});

