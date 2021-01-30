/* let counter = 0;
function count(){
    counter ++;
    // alert(counter);
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 5 === 0) {
        alert(`Таны "Тоолох" товч дээрх даралтын тоо: ${counter}`);
    }    
}

// document.querySelector('button').onclick = count;

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;
    // document.querySelector('button').addEventListener('click', count);
    setInterval(count, 1000);
});
*/

// localStorage
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count(){
    let counter = localStorage.getItem('counter');
    counter ++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);    
}

document.addEventListener('DOMContentLoaded', function(){    
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});