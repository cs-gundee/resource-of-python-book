/*
document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#submit').disabled = true;
    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit').disabled = false;
        } else {
            document.querySelector('#submit').disabled = true;
        }
    }

    document.querySelector('form').onsubmit = () => {
        // Хэрэглэгчийн илгээсэн утгыг хадгалж авах
        const task = document.querySelector('#task').value;    
        // console.log(task);   
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#tasks').append(li);

        document.querySelector('#task').value = '';
        document.querySelector('#submit').disabled = true;

        // Форм руу өгөгдөл илгээхийг зогсоох
        return false;
    }
});
*/

document.addEventListener('DOMContentLoaded', () => {

    // Нэмэх товч болон оролтын талбарыг хувьсагчид хадгалах
    const submit = document.querySelector('#submit');
    const newTask = document.querySelector('#task');

    // Хуудсыг анх ачаалахад Нэмэх товчийг идэвхгүй болгох
    submit.disabled = true;

    // Оролтын талбарт тэмдэгт бичсэн эсэхийг сонсох
    newTask.onkeyup = () => {
        if (newTask.value.length > 0) {
            submit.disabled = false;
        } else {
            submit.disabled = true;
        }
    }

    // формыг бөглөж илгээх event
    document.querySelector('form').onsubmit = () => {
        // Хэрэглэгчийн илгээсэн утгыг хадгалж авах
        const task = document.querySelector('#task').value;
        // li элементийг үүсгэж, түүнд хэрэглэгчийн илгээсэн утгыг хадгалах
        const li = document.createElement('li');
        li.innerHTML = task;
        // ul жагсаалтад шинэ элементийг нэмэх
        document.querySelector('#tasks').append(li);
        // Оролтын талбарыг хоослох
        newTask.value = '';
        // Нэмэх товчийг дахин идэвхгүй болгох
        submit.disabled = true; 
        return false;
    }
});