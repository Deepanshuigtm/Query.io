document.addEventListener("DOMContentLoaded", function () {
    // Your JavaScript code here
    const create_btn = document.getElementById('creatBtn');
    const create_query_block = document.querySelector('.create-popup');
    
    create_btn.addEventListener("click", function(e){
        e.preventDefault();
        console.log("Button clicked"); // Debugging log
        create_query_block.style.display = "block";
        console.log("Popup displayed"); // Debugging log
    });
});
