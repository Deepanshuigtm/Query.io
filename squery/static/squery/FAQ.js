const container = document.querySelectorAll('.container');

container.forEach(container =>{
    const icon = container.querySelector('.icon');
    const ans = container.querySelector('.ans');

    container.addEventListener('click', () =>{
        
        if(icon.classList.contains('active')) {
            icon.classList.remove('active');
            ans.style.maxHeight = null;
        }
        else {
            icon.classList.add('active');
            ans.style.maxHeight = ans.scrollHeight + 'px';
        }
    })
})